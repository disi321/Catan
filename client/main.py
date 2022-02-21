import threading
import socket
import time


def main():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8080))  
    while True:
        data = s.recv(1024)
        if data == b'goodbye':
            break
        print(data.decode())
        s.send(input().encode())
    s.close()
    print('connection closed')





if __name__ == "__main__":
    main()