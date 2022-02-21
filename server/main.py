import sys, os
import socket
import threading
from colorama import  init, Fore, Back, Style

import handler_manager


def handle_client(conn, addr):
    print('client', addr, 'connected')
    try:
        conn.send(b'Welcome to the server. Type your name:')
        data = conn.recv(1024)
        print(Fore.GREEN + 'received:', data)
        handler = handler_manager.auth_handler(conn)
        id = handler.handle()

    finally:
        print(Fore.RED + 'connection closed with', addr)
        conn.close()

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8080))
    s.listen()
    print(Fore.GREEN + 'server is listening')
    print('waiting for connection...')
    while True:
        # accept connection from client
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
        
        

def main():
    t = threading.Thread(target=listen).start()
    try:
        while True:
            com = input(Fore.WHITE + "enter command: ")
            if com == "exit":
                raise KeyboardInterrupt
                break
    except KeyboardInterrupt:
        print(Fore.YELLOW + 'end')
        os._exit(0)



if __name__ == "__main__":
    main()