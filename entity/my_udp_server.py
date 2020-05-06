import socket


class MyUdpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.users = {}

    def server_bind(self):
        self.server.bind((self.host, self.port))
        print("Server is running")

    def server_run(self):
        self.server_bind()

        while True:
            data, address = self.server.recvfrom(1024)
            if address not in self.users:
                self.register_on_chat(address)
            self.send_message_to_chat(data, address)

    def register_on_chat(self, address):
        self.server.sendto('Enter your name: '.encode(), address)
        name, address = self.server.recvfrom(1024)
        self.users[address] = name.decode()
        self.server.sendto(('Welcome to chat, ' + str(name.decode())).encode(), address)
        self.send_message_to_chat((str(name.decode()) + ' logged into chat.').encode(), address)

    def send_message_to_chat(self, data, address):
        sending_message = ('From ' + self.users[address] + ': ' + data.decode()).encode()
        for client in self.users:

            if client == address:
                print(sending_message.decode())
                continue

            self.server.sendto(sending_message, client)
