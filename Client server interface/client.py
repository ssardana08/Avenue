import socket
 
def client():
        host = '127.0.0.1'
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = input(" -> ")
         
        while message != 'q':
                mySocket.send(message.encode())
               
                message = input(" -> ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    client()
