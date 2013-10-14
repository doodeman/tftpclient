import socket

def readFile(serverURL, filename, port):
    sock = openConnection(serverURL, port)
    
    sock.sendTo(RRQ(filename), host)

def writeFile(serverURL, filename, port):
    pass

def openConnection(serverURL, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return sock

def RRQ(filename):
    s = ""
    s += '01 '
    s += 'octet '
    s += '0 '
    s += mode
    s += ' 0'
    return s

def WRQ(filename):
    s = ""
    s += '02 '
    s += 'octet '
    s += '0 '
    s += mode
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

