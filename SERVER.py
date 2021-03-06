import socket, select
import sys, os, socket

def server():

    port_wan = 11111
    port_mob = 11112
    port_sat = 11113

    sock_lst = []
    host = ''
    backlog = 5 # Number of clients on wait.
    buf_size = 1024

    try:
        for item in port_wan, port_mob, port_sat:
            sock_lst.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
            sock_lst[-1].setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
            sock_lst[-1].bind((host, item)) 
            sock_lst[-1].listen(backlog)
    except socket.error, (value, message):
        if sock_lst[-1]:
            sock_lst[-1].close()
            sock_lst = sock_lst[:-1]
        print 'Could not open socket: ' + message
        sys.exit(1)

    while True:
        read, write, error = select.select(sock_lst,[],[])

        for r in read:
            for item in sock_lst:
                if r == item:
                    accepted_socket, adress = item.accept()

                    print 'We have a connection with ', adress
                    data = accepted_socket.recv(buf_size)
                    if data:
                        print data
                        accepted_socket.send('Hello, and goodbye.')
                    accepted_socket.close()

server()
