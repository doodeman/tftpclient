#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import struct
import socket

def read(serverURL, filename, port):
    sock = openConnection(serverURL, port)
    
    host = (serverURL, port)
    sock.sendto(RRQ(filename), host)
    
    chunks = []
    while True:
        data, addr = sock.recvfrom(5000)
        host = (serverURL, addr[1])
        data = data[4:]
        chunks.append(data)
        sock.sendto(ACK(len(chunks)), host)
        if (len(data) < 512):
            print("packet received, is " + str(len(data)) + " bytes long, terminating")
            break
        else:
            print("packet received, is " + str(len(data)) + " bytes long, continuing")
    
    unifyFile(chunks, filename)
    
def write(serverURL, filename, port):
    sock = openConnection(serverURL, port)
    host = (serverURL, port)
    
    chunks = splitFile(filename,512)
    sock.sendto(WRQ(filename), host)
    for i, chunk in enumerate(chunks):
        data, addr = sock.recvfrom(5000)
        #print(data)
        host = (serverURL, addr[1])
        sock.sendto(DATA(i+1, chunk), host)
        print("packet " + str(i+1) + " of " + str(len(chunks)) + " sent to server")
    print("done")

def openConnection(serverURL, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return sock

def RRQ(filename):
    return struct.pack('!h' + str(len(filename)) + 'sb5sb', 1, filename.encode('utf-8'), 0, b"octet", 0)

def WRQ(filename):
    return struct.pack('!h' + str(len(filename)) + 'sb5sb', 2, filename.encode('utf-8'), 0, b"octet", 0)

def DATA(chunkNo, data):
    return struct.pack('!hh' + str(len(data)) + 's', 3, chunkNo, data)
    
def ACK(chunkNo):
    return struct.pack("!hh", 4, chunkNo)

def splitFile(file, chunkSize):
    f = open(file, 'rb')
    chunkSize = int(chunkSize)
    bytes = f.read()
    f.close()
    
    length = len(bytes)
    noChunks = int(length/chunkSize)
    
    if (length%chunkSize != 0): 
        noChunks += 1
    
    chunks = []
    for x in range(noChunks):
        startpos = x*chunkSize
        endpos = startpos + 512
        chunks.append(bytes[startpos:endpos])
    
    return chunks
    
def unifyFile(chunks, outfile):
    f = open(outfile, 'wb')
    
    for chunk in chunks:
        f.write(chunk)
        
args = sys.argv
del args[0]

if not (2 < len(args) < 5):
    print("Rangur fjöldi skipana.")
    sys.exit()
    
serverURL = args[0]
command = args[1]
document = args[2]
try:
    port = args[3]
except: 
    port = 69

if (command == 'lesa'):
    read(serverURL, document, port)
elif (command == 'skrifa'):
    write(serverURL, document, port)
else: 
    print("Óþekkt skipun")
    

