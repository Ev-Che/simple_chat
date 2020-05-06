import socket
import threading


class MyUdpClient:
    def __init__(self, host, port):
        self.server_host = host
        self.server_port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def receive_message(self):
        while True:
            data = self.client.recv(1024)
            print(data.decode())

    def send_message(self):
        while True:
            message = input()
            self.client.sendto(message.encode(), (self.server_host, self.server_port))

    def client_run(self):
        self.client.sendto(('').encode(), (self.server_host, self.server_port))
        receive_thread = threading.Thread(target=self.receive_message)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send_message)
        send_thread.start()
