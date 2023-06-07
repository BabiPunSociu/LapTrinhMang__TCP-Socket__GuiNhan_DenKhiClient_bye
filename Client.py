# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:34:36 2023

@author: ADMIN
"""

import socket

if __name__=='__main__':
    host='localhost'
    port=9050
    sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.connect((host,port))
    # Nhan 1
    data=sk.recv(1024)
    print('recv from server:', data.decode('utf-8'))
    while True:
        data=input("send to server: ")
        # Gui 2: Neu la 'bye' thi dung
        if data=='bye':
            sk.send(data.encode('utf-8'))
            sk.close()
            break
        sk.send(data.encode('utf-8'))
        # Nhan 3
        data=sk.recv(1024)
        print('recv from server:', data.decode('utf-8'))