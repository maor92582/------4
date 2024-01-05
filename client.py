import socket
from tkinter import filedialog
from tkinter import *
import customtkinter
import os
import time
global name1
name1=input ('put file name')
ct=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ct.connect((socket.gethostbyname(socket.gethostname()),65534))
def openfile():
    global filepath
    filepath=filedialog.askopenfile()
    print(filepath)
    app.destroy()
def openpath():
    global filepath
    filepath=filedialog.askdirectory()
    print(filepath)
def se():
    global t
    t="send"
    ct.send(t.encode())
    app1.destroy()
def rec():
    global t
    t="rec"
    ct.send(t.encode())
    app1.destroy()
customtkinter.set_appearance_mode("System")
app1=customtkinter.CTk()
app1.geometry('350x300')
app1.resizable(width=False,height=False)
color1='#020f12'
color2='#05d7ff'
color3='#65e7ff'
color4='black'
button1=Button(text="send",command=se,background=color1,foreground=color2,activebackground=color3,activeforeground=color4,highlightthickness=2,highlightbackground=color2,highlightcolor='white',width=13,height=2,border=0,cursor='hand1',font=('Arial',16,'bold'))
button2=Button(text="res",command=rec)
button1.pack()
button2.pack()
app1.mainloop()
file_byets=b""
if(t=="send"):
    app=customtkinter.CTk()
    button=Button(text="open",command=openfile)
    button.pack()
    app.mainloop()
    filepath=filepath.name


    name=os.path.basename(filepath)
    print(name)
    filesize=os.path.getsize(filepath)
    filesize=str(filesize)
    file=open(filepath,'rb')
    data=file.read()
    ct.send(name.encode())
    ct.send(filesize.encode())
    time.sleep(5)
    ct.sendall(data)
    file.close()
    ct.close()
if(t=="rec"):
    ct.send(name1.encode())
    ct.close
    ct=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ct.bind((socket.gethostbyname(socket.gethostname()),65535))
    ct.listen()
    while True:
        server,m=ct.accept()
        print(type(m))
        print(m)
        p=server.recv(10000000)
        p=p.decode()
        print(p)
        if(p=="file not found"):
            break
        if(p=="file were found"):
            openpath()
            os.chdir(filepath)
            done=False
            while not done:
                file=server.recv(1000000000)
                if(file_byets[-5:]==b"<END>"):
                    done=True
                else:
                   file_byets+=file 
            filec=open(name1,'wb')
            filec.write(file_byets) 
            filec.close
            
                     
            break
ct.close()