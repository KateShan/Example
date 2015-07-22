import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'python prog'


def pscan(port):
	try:
		s.connect((server,port))
		return True
	except:
		return False


for x in range(9000,9010):
	if pscan(x):
		print('Port',x, ' is open')
	else:
		print('.')