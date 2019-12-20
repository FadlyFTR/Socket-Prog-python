#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Copyright 2019 John <John@DESKTOP-MTPHK00>
import socket  
from _thread import *
import threading 
  
count = 1

print_lock = threading.Lock() 
def threaded(c):
    global count 
    data = ''
    buf = b''
    while True: 
        #print('Server: ')
        data = str(c.recv(4096).decode('ascii')) 
        print('Client ',count,':', data)
        if not data: 
            print('Bye Client ',count) 
            print_lock.release() 
            break

        if data == 'bye':
            count += 1
            c.close()
            print('Bye bye')
            print_lock.release()
            break
        data = input('Server : ')
        c.send(data.encode('ascii')) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = input("IP : ") 
    port = 4000 #int(input("PORT : "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("Socket binded to port:", port) 
  
    s.listen(5) 
    print("Connection Established") 
   
    while True: 
        c, addr = s.accept() 

        print_lock.acquire() 
        # print('Connected to :', addr[0], ':', addr[1]) 

        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
