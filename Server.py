from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def addnewuser(newuser,adduser): 
    username = newuser.recv(BufferSize).decode("utf8")
    usermessage = 'Welcome %s to chatroom! Enter LEAVE to exit the chatroom ' % username
    newuser.send(bytes(usermessage, "utf8"))
    userwelcomemessage = "%s has joined the chat room! " % username
    messageBroadcast(bytes(userwelcomemessage, "utf8"))
    userList[newuser] = username

    while True:
        userwelcomemessage = newuser.recv(BufferSize)
        if userwelcomemessage != bytes("LEAVE", "utf8"):
            messageBroadcast(userwelcomemessage, "Message from User - "+username+": ")
        else:
            newuser.send(bytes("LEAVE", "utf8"))
            newuser.close()
            del userList[newuser]       
            messageBroadcast(bytes("%s left the chat room." % username, "utf8"))
            print("%s:%s has disconnected." % adduser)
            break

def addconnection():
    while True:
        server,userList = SERVER.accept()
        print("%s:%s has connected." % userList)
        server.send(bytes("Welcome to Chat room. To join enter your Name and begin chatting.", "utf8"))
        Thread(target=addnewuser, args=(server,userList)).start()

def messageBroadcast(userwelcomemessage, nameId=""):  
    for socketConn in userList:
        socketConn.send(bytes(nameId, "utf8")+userwelcomemessage)

userList = {}
addressList = {}

port = int(input("Enter port number: "))
host = ''
BufferSize = 1024
Address = (host, port)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(Address)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for new users....")
    ACCEPT = Thread(target=addconnection)
    ACCEPT.start() 
    ACCEPT.join()  
    SERVER.close()


