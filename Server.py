import socket

fd = open("marks.csv", 'r')

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.86.61"
port = 10101

mysocket.bind((host, port))
mysocket.listen(5)

for line in fd.readlines():
    print line
    (client_socket, address) = mysocket.accept()
    client_socket.send(line)
    client_socket.close()
