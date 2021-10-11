import socket 

HEADERSIZE = 10
# gethostname for the reason, as of now the configuration is
# on the local machine
#It translates that the client and server socket are on the same local
#machine itself. 

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5001))

#1024 is our buffer
#In how many chunks of data we want to receive at once

full_msg = ''
new_msg = True 

while True: 
    msg = s.recv(16)
    if new_msg:
        print(f"new message length: {msg[:HEADERSIZE]}")
        msglen = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg. decode("utf-8")

    if len(full_msg) - HEADERSIZE == msglen:
        print("Full message received")
        print(full_msg[HEADERSIZE:])
        new_msg = True
        full_msg = ''

print(full_msg)

