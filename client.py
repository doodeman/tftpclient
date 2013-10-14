import socket
import random

def read(serverURL, filename, port):
    sock = openConnection(serverURL, port)
    
    host = (serverURL, port)
    string = RRQ(filename)
    sock.sendto(string, host)
    
    data, addr = sock.recvfrom(5000)
    print (addr)
    print(data)
    
def write(serverURL, filename, port):
    pass

def openConnection(serverURL, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    randport = random.randrange(40000, 59999)
    #sock.bind(('127.0.0.1', randport))
    return sock

def RRQ(filename):
    s = ""
    s += '01 '
    s += filename
    s += ' 0 '
    s += 'octet'
    s += ' 0'
    return s

def WRQ(filename):
    s = ""
    s += '02 '
    s += filename
    s += ' 0 '
    s += 'octet'
    s += ' 0'
    return s

def DATA(filename, chunkNo, data):
    s = ""
    s += '03 '
    s += str(chunkNo)
    s += ' ' + data
    return s
    
def ACK(chunkNo):
    s = ""
    s += '04 '
    s += chunkNo
    return s

