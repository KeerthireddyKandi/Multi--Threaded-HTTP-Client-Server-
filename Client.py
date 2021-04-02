from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
userconnection = socket(AF_INET, SOCK_STREAM)
PORT_NO = int(input('Enter port number: '))
HOST_NO = input('Enter host number: ')
BufferSize = 1024
ADDR = (HOST_NO, PORT_NO)
userconnection.connect(ADDR)
def sendText(): 
     sText=input()
     userconnection.send(bytes(sText, "utf8"))
     if sText == "LEAVE":         
        userconnection.close()
        exit()
     sendText()
def receiveText():
     while True:
        try:
            rText = userconnection.recv(BufferSize ).decode("utf8")
            print(rText)
        except OSError:  
            break

if __name__ == '__main__':
    Thread(target = receiveText).start()
    Thread(target = sendText).start()
