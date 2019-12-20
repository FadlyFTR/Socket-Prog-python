#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Copyright 2019 John <John@DESKTOP-MTPHK00>
import socket 
def Main(): 
    host = input("IP : ") 
    port = 2500 #int(input("PORT : "))
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 

    sep = ''
    print('Send \"bye\" to exit conversation')
    print('Server Busy... Waiting for connection...')
    s.send('Default Hello'.encode('ascii'))
    
    while True: 
  

        try:
            data = s.recv(100) 
            print('Server :',str(data.decode('ascii'))) 
        except socket.error:
            #nothing recieved
            print('')

        message = input('Client : ')
        s.send(message.encode('ascii')) 
  
        if message == 'bye': 
            s.close()
            break
        else: 
            continue
    s.close() 
if __name__ == '__main__': 
    Main() 
