"""
Le premier serveur en Python
* Serveur
Ce serveur accepte 5 clients concurents et indique l'heure de serveur.
@author Alexandra Dobrescu
@date 06.04.2017
"""
import socket
import time
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
#serversocket.listen(5)
 
print "Le serveur marche :) "

def client_envoi():
        while True:
                message = raw_input("Text: ")
                serversocket.send(message)
 
def client_recieve():
        while True:
                reply = serversocket.recv(1024)
                print "recu", repr(reply)
 
 
thread_send = []
thread_rcv = []
num_threads = 5
 
for boucle1 in range(num_threads):
        thread_send.append(threading.Thread(target = client_envoi))
        thread_send[-1].start()
 
for boucle2 in range(num_threads):
        thread_rcv.append(threading.Thread(target = client_recieve))
        thread_rcv[-1].start()


while True:
    # establish a connection
    
    clientsocket,addr = serversocket.accept()
    print("Connection de client avec IP %s" % str(addr))
    
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))

    temps = serversocket.recv(1024)
    print time.ctime(time.time()) + str(addr) + str(temps)
    
    clientsocket.close()
    
