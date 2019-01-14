import socket
import os
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
#s is socket object
port =1261
s.bind(('',port))
s.listen(5)
while True:
    c,addr=s.accept()
    received_data=c.recv(1024).decode()
    x=received_data.split('/')
    #print(type(x))
    path=""
    try:
        with open("config", "r") as ins:
            for line in ins:
                r=line.split("@")
                # print(r[0])
                # print(x[0])
                if str(r[0])==str(x[0]):
                    path=r[1]
        path=path+received_data[received_data.index('/'):]
    except:
        s1="404"+"@"+"text"+"@"+"0"+"@"+" "
        c.send(s1.encode())
    #print(path)    
    exists = os.path.isfile(path)
    if exists:
        f=open(path,"r")
        content=f.read()
        s1="200"+"@"+"text"+"@"+str(len(content))+"@"+content
        c.send(s1.encode())
        f.close()

    else:
        s1="404"+"@"+"text"+"@"+"0"+"@"+" "
        c.send(s1.encode())
    c.close()