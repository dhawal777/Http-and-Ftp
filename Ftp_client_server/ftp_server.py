import socket
import os
s=socket.socket()
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#s is socket object
port1 =50048
port=50049
s.bind(('127.0.0.1',port))
s.listen(5)
while True:
    c,addr=s.accept()
    received_data=c.recv(1024).decode()
    x=received_data.split('/')
    #print(type(x))
    path=""
    s2=""
    try:
        with open("config", "r") as ins:
            for line in ins:
                r=line.split("@")
                if str(r[0])==str(x[0]):
                    path=r[1]
        path=path+received_data[received_data.index('/'):]
    except:
        s2="404"+"@"+"text"+"@"+"0"+"@"+" "  
    exists = os.path.isfile(path)
    if exists:
        f=open(path,"r")
        content=f.read()
        s2="200"+"@"+"text"+"@"+str(len(content))+"@"+content
        f.close()
    else:
        s2="404"+"@"+"text"+"@"+"0"+"@"+" "
    #creation of data socket on server side
    #s.send("send".encode)
    try:
        x="ok"
        print(x)
        c.send(x.encode())
        r=c.recv(10240)
        s1=socket.socket()
        
        #data port
        s1.connect((addr[0],port1))
        
        s1.send(s2.encode())
        s1.close()
    except Exception as E:
        print(E)
    #data port is temprory so close each time
    
    c.close()
s.close()
       
    