import socket


def main():
	host = '127.0.0.1'
	port = 5001
	

	server=('127.0.0.1',5000)

	s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	message = input("Enter message:  ")
	while message !='q':
		s.sendto(str(message).encode('ASCII'),server)
		data, addr = s.recvfrom(1024)
		print("Recieved from server: "+ data.decode('ASCII'))
		message = input("Enter another message: ")
	s.close()

if __name__=='__main__':
 main()