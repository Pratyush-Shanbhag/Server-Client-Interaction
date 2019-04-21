import socket

line = " "


line = open("marks.csv", 'r')
print("This is the contents of marks.csv: ")
print line.read()


mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind(("127.0.0.1", 1050))
mysocket.listen(5)
(client, (ip, port)) = mysocket.accept()

client.send("\n\n\nI am the server. Here are the contents of marks.csv: ")
client.send(line)













                                                                                                                                                                                                                                                                                                                                                            
