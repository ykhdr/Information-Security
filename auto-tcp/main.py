import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ("nsuctf.ru", 30002)
client_socket.connect(server_address)

for i in range(0, 100):
    data = client_socket.recv(1024)
    print(data.decode("utf-8"))
    response = data.decode("utf-8").split()
    num1 = int(response[0])
    num2 = int(response[2])
    summ = num2 + num1
    print(str(summ))
    client_socket.send(str(summ).encode("utf-8"))

print(client_socket.recv(1024).decode("utf-8"))
client_socket.close()