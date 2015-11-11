from socket import socket, AF_INET, SOCK_DGRAM

sock = socket(AF_INET, SOCK_DGRAM)

def send(message, port = 56765): 
	sock.sendto(message.getBytes(), ('127.0.0.1', port))