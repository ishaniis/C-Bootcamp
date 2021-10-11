import socket 

HEADERSIZE = 10
#AF_INET corresponds to IPv4
#SOCK_STREAM corresponds to tcp communication protocoal 

#Socket is your endpoint that receives and send the data

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5000))

#For Incomming connections
s.listen(5)

while True:  
    clientsocket, address = s.accept()
    #clientsocket is the ip 
    print(f"Connection from the client: {address} has been established")
    
    msg = "Welcome to the Server"
    print = f'{len(msg):<{HEADERSIZE}}'+msg     

    clientsocket.send(bytes(msg, "utf-8"))
    clientsocket.close()

