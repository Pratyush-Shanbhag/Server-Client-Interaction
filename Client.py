import socket

for i in range(5):
    temp = raw_input("Press enter: ")
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect(("192.168.86.61", 10101))
    data = mysocket.recv(2048)
    print data
    
