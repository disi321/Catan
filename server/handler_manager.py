import socket

class auth_handler:
    def __init__(self, conn : socket.socket):
        self.conn = conn
        print("create auth_handler")
    def handle(self):
        print("auth_handler")
        self.conn.send(b'enter 1 to sign up, 2 to sign in, 3 to exit\n')
        while True:
            data = self.conn.recv(1024)
            if data == b'1':
                self.conn.send(b'enter your name\n')
                name = self.conn.recv(1024)
                self.conn.send(b'enter your password\n')
                password = self.conn.recv(1024)
                # TODO: check if name is already taken
                return 1
            elif data == b'2':
                self.conn.send(b'enter your name\n')
                name = self.conn.recv(1024)
                self.conn.send(b'enter your password\n')
                password = self.conn.recv(1024)
                # TODO: login and check if name and password are correct
                return 1
            elif data == b'3':
                self.conn.send(b'goodbye')
                self.conn.close()
                return 0 
            else:
                self.conn.send(b'wrong input\nenter 1 to sign up, 2 to sign in, 3 to exit')
                
 
class menu_handler:
    def __init__(self, conn : socket.socket):
        self.conn = conn
        print("create menu_handler for")
    def handle(self):
        print("menu_handler")
        self.conn.send(b'enter 1 to create room, 2 to join room, 3 to signout, 4 to exit\n')
        while True:
            data = self.conn.recv(1024)
            if data == b'1':
                self.conn.send(b'set room password\n')
                name = self.conn.recv(1024)
                return 2

            elif data == b'2':
                self.conn.send(b'enter room id\n')
                name = self.conn.recv(1024)
                self.conn.send(b'enter room password\n')
                password = self.conn.recv(1024)
                return 2, name, password

            elif data == b'3':
                self.conn.send(b'signout successfully')
                self.conn.close()
                return 1

            elif data == b'4':
                self.conn.send(b'goodbye')
                self.conn.close()
                return 0

            else:
                self.conn.send(b'wrong input\nenter 1 to sign up, 2 to sign in, 3 to exit')

class game_handler:
    def __init__(self, conn : socket.socket):
        self.conn = conn
    def handle(self):
        pass
        

class handler_manager:
    def __init__(self):
        pass
    
    def get_auth_handler(self):
        a = auth_handler()
        return a

    def get_auth_handler(self):
        return menu_handler()

    def get_auth_handler(self):
        return game_handler()


handler_manager = handler_manager()
def get_handler_manager():
    return handler_manager
