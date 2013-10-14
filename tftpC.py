#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import client

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
    client.read(serverURL, document, port)
elif (command == 'skrifa'):
    client.write(serverURL, document, port)
else: 
    print("Óþekkt skipun")
    
