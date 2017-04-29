import socket 
def server():
	
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
     print("Server's IP Address:"+host)
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
       
            
             
    conn.close()
     
if __name__ == '__main__':
    server()
