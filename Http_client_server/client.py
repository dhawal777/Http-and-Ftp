import socket
while True:
    s=socket.socket()
    port=1261
    print("Enter quit to leave Conversation")
    print('Enter the url')
    url = input()
    if url=="quit":
        print("Thank u for conversation")
        s.close()
        break
    else:
        ip_extract=url.split('/')
        s.connect((ip_extract[0],port))
        #s.send("Are u done".encode())
        s.send(url.encode())
        w=s.recv(10240).decode()
        #print(w)
        x=w.split("@")
        print(x[0])
        if x[0]=="200":
            if(len(x[3])!=int(x[2])):
                print("Response is corrupted")
            else:
                print(w)
            
        else:
            print("404 Path not found")

        #print(s.recv(1024)) 

    s.close()
