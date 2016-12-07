##############################################################################
# Seiren : Simple Python Messaging Network
# CPSC 3780 Project
# Authors: Tyler Bertram, Jarvis Zazalack
#   A simple, object-oriented and dynamically-constructed messaging network
#   using UDP to pass message strings while handling small-scale routing
#   between multiple networks.
#
#   server.py:
#       Server object which contains all relevant functions for using Seiren 
#       in server mode.
##############################################################################

import time
import socket
import pickle
from modules.message import Message
from modules.message_factory import construct_message

class MessageServer():
    def __init__(self, port):
        self.host = '142.66.140.69'
        self.port = port
        self.rank = 0                       # Rank is used to determine which
                                            # other server the server should
                                            # talk to when updating client
                                            # lists. While it always starts at
                                            # 0, upon hooking a server into a
                                            # network, it will slot itself
                                            # into the highest open rank. 
        self.peers = set()
        self.client_list = {}
        self.messages = []
        

    def activate(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s.setdefaulttimeout(5)
        s.bind((self.host, self.port))
        #s.listen(1)
        #conn, addr = s.accept()



        while True:
            data, addr = s.recvfrom(65536)
            print ("Connected by ", addr)
            unpickled_data = pickle.loads(data)
            print ("Client sent message: ", unpickled_data.payload)
#            if (unpickled_data.type == 'SRV'):         
            if unpickled_data.type is 'SND':
                self.messages.append(unpickled_data)
            elif unpickled_data.type is 'IDR':
                if (addr in self.client_list):
                    pass
                else:
                    new_id = randint(1, 100000000)  
                    while True:
                        if (new_id in self.client_list):
                            new_id = randint(1, 1000000000)
                        else:
                            break
                    self.client_list[new_id] = self.host
                    wrapped_msg = construct_message(5, self.mess_seq, 0, new_id, "")
                    s.sendto(pickle.dumps(wrapped_msg), (addr, 5000))
            #elif unpickled_data.type is 'OFF':

        """while True:
            new_id = randint(1, 100000000)
            while True:
                if new_id in self.client_list:
                    new_id = randint(1, 1000000000)
                else:
                    break
            id_str = '{:0>10}'.format(new_id)
            self.client_list.update({'id_str': 
                                     s.gethostbyname(gethostname())})
            id_assign = construct_message("ASN", new_id, id_str)
            conn.send(self.pickle_message(id_assign))
            uselist_string = ""
            for key in self.client_list:
                uselist_string = uselist_string + " " + key
            uselist_message = construct_message("USR", uselist_string, id_str)
            conn.send(self.pickle_message(uselist_message))
            break"""
        
