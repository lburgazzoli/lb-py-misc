#!/usr/bin/env python
#
# Copyright (c) 2012, Luca Burgazzoli
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met: 
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer. 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import socket
import sys
import thread

################################################################################
#
################################################################################

class PortForwarder:
    def __init__(self):
        pass
    
    def run(self,listenPort,remoteHost,remotePort):
        ds = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ds.bind(('',listenPort))
        ds.listen(5)
        while True:
            csock = ds.accept()[0]
            rsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            rsock.connect((remoteHost,remotePort))
            thread.start_new_thread(self.__forward,(csock,rsock))
            thread.start_new_thread(self.__forward,(rsock,csock))
    
    def __forward(self,src,dst):
        string = ' '
        while string:
            string = src.recv(1024)
            if string:
                dst.sendall(string)
                sys.stdout.write(string)
            else:
                src.shutdown(socket.SHUT_RD)
                dst.shutdown(socket.SHUT_WR)

################################################################################
#
################################################################################

if __name__ == '__main__':
    pf = PortForwarder()
    pf.run(int(sys.argv[1]),sys.argv[2],int(sys.argv[3]))
