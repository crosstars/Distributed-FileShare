import math
import pickle
import socket
import time
from config import *
import threading
import filer


class Client:
    def __init__(self):
        self.serve_thread = None
        self.id = None
        self.dataset = None
        self.server = None   # socket to interact with server
        self.peer = None    # socket to interact with peer
        self.running = True
        self.start()
        exit(0)
    
    def printdata(self):
        print(self.dataset)#print booklist
    
    def start(self):
        self.connect()
        self.menu()
        self.close()
    
    #start the connection
    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((SERVER_IP,SERVER_PORT))

        self.peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.peer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serve_thread = threading.Thread(target=self.share,args=())
        self.serve_thread.start()
        self.printdata()
    #close the connection
    def close(self):
        self.server.send(pickle.dumps([DISCONNECT]))
        self.server.close() 
        print ("--- Connection with Server closed ---")
        self.printdata()
    
    #display the options
    def menu(self):
        
        self.dataset = filer.loadlist()
        
        self.register()
        self.printdata()

        while True :
            print("\nOperations:\n1. Query Book\n2. print library\n3. QUIT")
            choice = input("(Enter choice):") # stores which operation to perform
            match(choice):
                case "1":
                    self.query(input("enter the book name"))
                    self.printdata()
                case "3":
                    break
                case "2":self.printdata()
                case _:
                    print("invalid input")
            self.running=False
            self.printdata()


    def share(self):
        address = self.server.getsockname()
        print(address) # get own address
        address = (address[0],address[1]+1)
        self.peer.bind(address)
        self.peer.listen(1)

        while self.running:
            c, addr = self.peer.accept()
            print("\n Accepted connection from "+str(addr)+" ---")
            
            
            message = c.recv(SIZE)
            request =pickle.loads(message)
            size,response = self.getbook(request[0])
            c.send(pickle.dumps(size))
            
            
            time.sleep(5)
                
                # send book back
            c.send(pickle.dumps(response))
            if awk := c.recv(SIZE) :
                
                print("\ndone sending")
                self.deletebook(request[0])
                self.printdata()

    #query for book
    def query(self,name):
        if name in self.dataset:
            print("file already in your folder")
        else:
            self.server.send(pickle.dumps([SEARCH,name]))
            responce = pickle.loads(self.server.recv(SIZE))
            print(responce)
            if responce == [None]:
                print(f"book {name}  not found")
            elif input(f"book found in peer {responce[0][0]} want to download (y for yes )").strip().lower() == "y":
                self.download(responce[0], name)
                self.printdata()
            else:
                print("aborting download")

    
    def download(self, responce, name):
        id0,host,port = responce[0],responce[1],responce[2]
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host,port))

        conn.send(pickle.dumps([name]))
        data =b""
        size_message = pickle.loads(conn.recv(SIZE))
        
        if size_message is None:
            self.query(name)#client do not have the book so request the server again  
        print(size_message)#get book size

        itr = math.ceil(size_message/SIZE)
        print('receiving data...')
        while itr > 0:
            itr = itr-1
            data0 = conn.recv(size_message)#get the whole book
            data = data + data0
        
        print("recived the data")
          
        responce = pickle.loads(data)
        filer.create(name,responce)
        conn.send(pickle.dumps(["yess"]))
        #method to update the server
        self.dataset.append(name)
        self.deletebookreq(host,port,name)
        conn.close()


    
    def deletebook(self,bookname):
        self.dataset.remove(bookname)
        filer.deletebook(bookname)
    
    def getbook(self,bookname):
        return filer.booktostring(bookname) if bookname in self.dataset else None
            
    def deletebookreq(self , host , port,name):
        self.server.send(pickle.dumps([UPDATE,self.id,host,port,name]))
    
    def register(self):
        self.server.send(pickle.dumps([REGISTER,self.dataset]))
        response = self.server.recv(SIZE)
        response = pickle.loads(response)
        self.id = response[1]
        if response[0]==SUCCESS:
            print(f"registered successfully with id {self.id}")
        else:
            print("failed")

client = Client()