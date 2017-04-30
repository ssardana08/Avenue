import socket
import pyautogui as pyag
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
            if (data == 'b!'):
                pyag.press('left')
            elif (data == 'd!'):
                pyag.press('right')
            elif (data == 'a!'):
                pyag.hotkey('shift','f5')
            elif (data == 'c!'):
                pyag.press('esc')
             
       
            
             
    conn.close()
     
if __name__ == '__main__':
    server()
