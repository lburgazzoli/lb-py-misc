import socket
import sys
import thread
import time

def server():
    ds = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ds.bind(('',int(sys.argv[1])))
    ds.listen(5)
    while True:
        csock = ds.accept()[0]
        rsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rsock.connect((sys.argv[2],int(sys.argv[3])))
        thread.start_new_thread(forward,(csock,rsock))
        thread.start_new_thread(forward,(rsock,csock))

def forward(src,dst):
    string = ' '
    while string:
        string = src.recv(1024)
        if string:
            dst.sendall(string)
            sys.stdout.write(string)
        else:
            src.shutdown(socket.SHUT_RD)
            dst.shutdown(socket.SHUT_WR)

if __name__ == '__main__':
    server()
