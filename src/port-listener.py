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

################################################################################
#
################################################################################

class PortListener:
    def __init__(self):
        pass
    
    def run(self,listenPort):
        ds = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ds.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ds.bind(('',listenPort))
        ds.listen(5)

        while True:
            csock  = ds.accept()[0]
            chunks = []
            while True:
                chunks = csock.recv(24)
                if len(chunks) > 0:
                    for b in chunks:
                        if int(b) > 32:
                            print("c -> %c" % (int(b)))
                        #else:
                        #    print("d -> %d" % (int(b)))

                else:
                    csock.shutdown(socket.SHUT_RD)
                    csock.shutdown(socket.SHUT_WR)
                    break

################################################################################
#
################################################################################

if __name__ == '__main__':
    pf = PortListener()
    pf.run(int(sys.argv[1]))
