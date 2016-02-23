#Submitted By: Meenal Jain

from socket import *
from datetime import datetime
from time import time

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.connect(('localhost', 12000))     #Host and Port to connect to server
count = 0                           #Count Initialized

while count < 10:
    count = count + 1
    t1 = datetime.now()
    message = 'ping '+ str(count) + ' ' + str(t1)            #Message Format: Ping Sequence_Number Time
    client_socket.sendto(message, ('localhost', 12000))
    client_socket.settimeout(1)         #Response should be received within 1 second
    try:
        new_message, address = client_socket.recvfrom(1024)
        t2 = datetime.now()
        rtt = t1 - t2           #Round Trip Time
        print '\n',new_message  #Received Message
        print 'Round Trip Time(Micro seconds)-->', rtt.microseconds         
    except timeout:
        # If response is not received within 1 second
        print '\nRequest Timed Out'

    if count == 10:
        print '------------Ten attempts done------------'
        client_socket.close()   #Closing Connection


