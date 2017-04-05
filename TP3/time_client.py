"""
Le premier client en Python
* Client
Ce client se connecte au Time serveur et recupere l'heure de serveur.
@author Alexandra Dobrescu
@date 06.04.2017
"""

import socket
import threading
import sys

# get local machine name
host = socket.gethostname()
port = 6666

#Apres ca on peut demarer le serveur

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind to the port
server_address =(host, port)
serversocket.connect((server_address))
# queue up to 5 requests
serversocket.listen(5)

def client_send():
    while True:
            message = raw_input("Text: ")
            serversocket.send(message)
 
def client_recv():
    while True:
        reply = serversocket.recv(1024)
            print "received", repr(reply)
 
 
thread_send = []
thread_rcv = []
num_threads = 5
 
for boucle1 in range(num_threads):
    thread_send.append(threading.Thread(target = client_send))
    thread_send[-1].start()
 
for boucle2 in range(num_threads):
    thread_rcv.append(threading.Thread(target = client_recv))
    thread_rcv[-1].start()

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
