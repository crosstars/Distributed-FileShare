
import pickle
import socket
import threading
import types
from config import *


class Server:
    commands = [REGISTER,DISCONNECT,UPDATE,DEREGISTER,SEARCH]
    const = types.SimpleNamespace()
    const.REGISTER = REGISTER
    const.DISCONNECT = DISCONNECT
    const.UPDATE = UPDATE
    const.DEREGISTER = DEREGISTER
    const.SEARCH = SEARCH
    semaphore = threading.Semaphore()
    def printdata(self):
        print(self.data)
    def __init__(self):

        self.id = '000000'
        self.data = {}
        self.sock = None
        self.start()
    
    def start(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((SERVER_IP, SERVER_PORT))
        self.sock.listen(MAX_CONNECTIONS)
        print("started")
        i=0
        while True:
            print("looping",i)
            conn,address = self.sock.accept()
            
            print(f"connection from {address}")
            address=(address[0],address[1]+1)
            thread = threading.Thread(target=self.handler,args=(conn,address))
            thread.start()

            print(f"--- Active Connections : {str(threading.active_count() - 1)} ---\n")
    
    def handler(self,conn,addr):# handels clients
        
        data = ""
        connected = True    # turns false when user wants to disconnect
        while connected:
            data = conn.recv(SIZE)
            print(data)
            if data is [None]:
                connected = False
            message = pickle.loads(data)
            print(message)

            match(message[0]):

                case self.const.DISCONNECT:
                    self.semaphore.acquire()
                    self.remove(addr)
                    self.semaphore.release()
                    conn.close()
                    connected = False
                    self.printdata()
                    



                case self.const.SEARCH:
                    self.semaphore.acquire()
                    filename = message[1]
                    result = self.search(filename)
                    result = pickle.dumps(result)
                    conn.send(result)
                    self.printdata()
                    self.semaphore.release()

                    
                case self.const.REGISTER:
                    self.semaphore.acquire()
                    host = addr[0]
                    port = addr[1]
                    blist = message[1]
                    idno = len(self.data)+1
                    self.data[(idno,host,port)] = blist
                    conn.send(pickle.dumps([SUCCESS,idno]))
                    self.printdata()
                    self.semaphore.release()
                    

                case self.const.UPDATE:
                    self.semaphore.acquire()
                    my_id = message[1]
                    host = message[2]  
                    port = message[3]
                    b_data = message[4]
                    self.update(my_id,host,port,b_data)
                    self.printdata()
                    self.semaphore.release()

                case self.const.DEREGESTER:
                    self.semaphore.acquire()
                    self.remove(addr)
                    self.semaphore.release()
                    conn.close()
                    connected = False
                    self.printdata()

    def remove(self,addr):
        for i in self.data.keys():
            if i[1]==addr[0] and i[2]==addr[1]:
                del self.data[i]
                return

    def search(self,filename):
        for i in self.data.keys():
            if filename in self.data[i]:
                return [i]
        else: 
            return [None]
        
    def update(self,my_id,host,port,b_data):  
        for i in self.data.keys():
            if i[1]==host and i[2]==port:
                delkey = i
            if i[0]==my_id:
                addkey = i
        try:
            self.data[delkey].remove(b_data)
        except:
            pass
        self.data[addkey].append(b_data)

sv=Server()
if input() == "s":
    sv.data = {}
    sv.sock.close()             
            
            



