from entity import my_udp_client, my_udp_server

type_of_user = int(input(("Select type of user:\n"
                          " [1] Server\n"
                          " [2] Client\n")))

if type_of_user == 1:
    host = input('Enter server address')
    server = my_udp_server.MyUdpServer(host, 8888)
    server.server_run()

else:
    address = input('Enter server address: ')  # "192.168.100.139"
    client = my_udp_client.MyUdpClient(address, 8888)
    client.client_run()
