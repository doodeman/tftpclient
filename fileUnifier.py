def unifyFile(chunks, outfile):
    f = open(outfile, 'wb')
    
    for chunk in chunks:
        f.write(chunk)
    

#import fileSplitter

#chunks = fileSplitter.splitFile("doge.jpg", 512)
#unifyFile(chunks, "anotherdoge.jpg")