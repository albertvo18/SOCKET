import socket
#from select import select
import select

TCP_PORT1 = 2100
TCP_PORT2 = 3200
s_global = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_global.setblocking(0)
s_global.bind(("", TCP_PORT1))
backlog = 0xFF
s_global.listen(backlog)
s_local = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_local.setblocking(0)
s_local.bind(("127.0.0.1", TCP_PORT2))
s_local.listen(backlog)

#PRINT = True
PRINT = False

def handle(sock_in, ip_addr):
	if PRINT:
		print ('got incoming connection from  ' + str(ip_addr)  + 'on port ' + str(sock_in))
	if str(TCP_PORT1) in str(sock_in):
		print ('Got Incoming Connection on ', TCP_PORT1)
	if str(TCP_PORT2) in str(sock_in):
		print ('Got Incoming Connection on ', TCP_PORT2)

TIMEOUT = 1000000000 #seconds
terminate = False # variable to be modified externally to end the loop
listening_sockets = [s_global, s_local]
while (not terminate):
  notified_socket_list = select.select(listening_sockets, [], [], TIMEOUT)[0]
#    for notified_socket in notified_socket_list:
#        incoming_socket, addr = notified_socket.accept()
#        handle(incoming_socket, addr)


  for notified_socket in notified_socket_list:
    incoming_socket, addr = notified_socket.accept()
    if notified_socket == s_global:
#            handle_global(incoming_socket, addr)
#      data = s_global.recv(1024)	
      data = incoming_socket.recv(1024)	
      print ('Got Incoming on ' ,str(TCP_PORT1), data.strip())
    else:
#            handle_local(incoming_socket, addr)
#      data = s_local.recv(1024)	
      data = incoming_socket.recv(1024)	
      print ('Got Incoming on ',str(TCP_PORT2), data.strip())
