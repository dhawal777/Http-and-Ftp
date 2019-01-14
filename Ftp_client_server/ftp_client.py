import socket
port1 =50048
port=50049
while True:
    s=socket.socket()
    print("Quit to exit")
    print('Enter the url')
    url = input()
    if url=="quit":
        print("Thank u for conversation")
        break
    else:
        ip_extract=url.split('/')
        s.connect((ip_extract[0],port))
        s.send(url.encode())
        try:
            k=s.recv(10240).decode()
            print(k)
            if k=="ok":
            #url on command port
            #Created Data Socket when server ask to connect
                x="ready to listen"
                print('Ok')
                
                s1=socket.socket()
                # s1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
                s1.bind(('',port1))
                s1.listen(5)
                
                s.send(x.encode())
                # s.send("send".encode())
                c,addr=s1.accept()
                print(addr)
                w=c.recv(10240).decode()
                #print(w)
                x=w.split("@")
                #print(x[0])
                c.close()
                s1.close()
                if x[0]=="200":
                    if(len(x[3])!=int(x[2])):
                        print("Response is corrupted")
                    else:
                        print(w)
                    
                else:
                    print("404 Path not found")
                
        except Exception as E:
             print(E)
    s.close()
        #print(s.recv(1024)) 

             