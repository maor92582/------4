import socket
import os
import time
host =''
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',65534))
s.listen()
os.chdir('C:\\Users\\maori\\Documents\\upload')
while True:
    clients,adrr=s.accept()
    print(type(adrr))
    print(adrr)
    msg=clients.recv(1000000000).decode()
    print(msg)
    if(msg=="send"):
        name=clients.recv(1000000000).decode()
        print(name)
        size=clients.recv(1024).decode()
        print(size)
        file=clients.recv(1000000000)
        filec=open(name,'wb')
        filec.write(file)
        break
    if(msg=="rec"):
        name1=clients.recv(1000000000).decode()
        s.close()
        clients.close()
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostbyname(socket.gethostname()),65535))
        try:
            t="file were found"
            s.send(t.encode())

            file= open(name1,'rb')
            data=file.read()
            s.sendall(data)
            s.send(b"<END>")
            
            s.close()
            break
            


        except Exception as error:
            print(error)
            t="file not found"
            
            s.send(t.encode())
            break
                

        