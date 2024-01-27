import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('localhost', 3000))

cmd = 'GET http://localhost:3000 HTTP/1.0\n\n'.encode()

my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
my_socket.close()
