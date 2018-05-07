import socket
#from select import select
import select
s_global = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_global.setblocking(0)
s_global.bind(("", 9093))
backlog = 0xFF
s_global.listen(backlog)
s_local = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_local.setblocking(0)
s_local.bind(("127.0.0.1", 9094))
s_local.listen(backlog)

#PRINT = True
PRINT = False

def handle(sock_in, ip_addr):
	if PRINT:
		print ('got incoming connection from  ' + str(ip_addr)  + 'on port ' + str(sock_in))
	if '9093' in str(sock_in):
		print ('Got Incoming Connection on 9093')
	if '9094' in str(sock_in):
		print ('Got Incoming Connection on 9094')

TIMEOUT = 1 #seconds
terminate = False # variable to be modified externally to end the loop
listening_sockets = [s_global, s_local]
while (not terminate):
    notified_socket_list = select.select(listening_sockets, [], [], TIMEOUT)[0]
    for notified_socket in notified_socket_list:
        incoming_socket, addr = notified_socket.accept()
        handle(incoming_socket, addr)
