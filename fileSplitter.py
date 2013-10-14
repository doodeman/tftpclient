def splitFile(file, chunkSize):
    f = open(file, 'rb')
    bytes = f.read()
    f.close()
    
    length = len(bytes)
    noChunks = length/chunkSize
    
    if (length%chunkSize != 0): 
        noChunks += 1
    
    chunks = []
    for x in range(noChunks):
        startpos = x*chunkSize
        endpos = startpos + 512
        chunks.append(bytes[startpos:endpos])
    
    return chunks
    
#splitFile('doge.jpg', 512)