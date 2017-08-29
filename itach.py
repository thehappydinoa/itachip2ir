import socket
import time
import sys

itach_ip = ''

def send_command(command):
	if (itach_ip == ''):
		raise Exception('No IP set. Please set using set_ip(ip) to set ip.')
	else:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((itach_ip, 4998))
		s.settimeout(2)
		s.sendall(command+"\r")
		msg = s.recv(4096)
		s.close()
		del s
		return msg	
	
def set_ip(ip):
	global itach_ip
	itach_ip = str(ip)
	return True
	
	