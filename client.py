import socket
import struct
import fileUnifier
import fileSplitter

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
    
    fileUnifier.unifyFile(chunks, filename)
    
def write(serverURL, filename, port):
    sock = openConnection(serverURL, port)
    host = (serverURL, port)
    
    chunks = fileSplitter.splitFile(filename,512)
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

