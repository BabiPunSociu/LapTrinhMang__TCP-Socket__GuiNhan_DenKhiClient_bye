# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:34:35 2023

@author: ADMIN
"""

import socket

if __name__=='__main__':
    host='localhost'
    port=9050
    sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind((host,port))
    sk.listen(1)
    client_sk,client_add=sk.accept()
    print('Ket noi den ', client_add)
    # Gui 1
    client_sk.send('hello client'.encode('utf-8'))
    print('send to client: hello client')
    while True:
        # Nhan 2
        data=client_sk.recv(1024)
        if data.decode('utf-8')=='bye':
            client_sk.close()
            break
        print('recv from client:',data.decode('utf-8'))
        # Gui 3
        data = input("send to client: ")
        client_sk.send(data.encode('utf-8'))
        