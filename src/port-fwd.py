#!/usr/bin/env python
#
#
#  Copyright 2012 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
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
