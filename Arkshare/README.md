# Napster like file-sharing system

Brief about this project

Peer-to-Peer(P2P) Technologies are being widely used for sharing the data between the servers and the clients. One of the major technology for file sharing that is implemented nowadays is the Napster-Style Peer-to-Peer File Sharing System. The older versions of the systems used to have a single server which stores the files in its directory that are received from the clients. The major drawback of these systems was that if a new file has been created in one of the peers, it must be transferred to the server before another peer can access it, which delays the process of transfer from one peer to another. This can be conquered using the Napster system which allows the peer to peer file transfer.
this is a prototype to mimic napster called arkshare


### System Requirements:
* Python 3.10 environment installed
* pickle 

### Design
Entire project is designed using Python 3.10 where I used some network programming concepts such as sockets, multi-threading for establishing connections between peers. Major components of this project are:
* Indexing Server
* Peer _( Which acts as client and a server )_

#### Indexing server
Indexing server indexes the content of all peers  using dictionary with a key  (_peer id_,_peer host_,_peer port_) and value the list of books shared pairs. It provides two funcitons which are **register** and **search** .

### Peer
Major function of the peer: Register and Listen to clients that wants to download . Search for a filename and ask to download it. Firstly, as a client, user can request a file name to the indexing server. The indexing server returns a peer data whcih shares this file with all of its details. The user then connects to this peer and downloads the file. Secondly, as a server,the peer waits for requests from other peers and sends the requested file when receiving a request. So peers here, act as both the client and the server. This server is different from the central index server which only indexes the files. But, the server functionality of the peer can be used to download the files from its directory. The peer also acts as a client to download the files from other peers into its directory.

## Limitations
sending real book files are not implimented , it is simulated by list elements , book names are random integer strings , book contents list element is returned as file eklements {the extraa folder filer.py will take care of these operations , these are not implimented}
### How-to
##### configuration
configure the server by editing configure.py
#### run
first run the _server.py_ , then run the _client.py_ .
the list of numbers printed are the _book names (numbers)_.
client have an interactive menu to guide the user.
server and client will reflect book location changes.
### Sample output
running the server , then the client will automatically register to the running server
the server reciving the connections :
```
started
looping 0
connection from ('127.0.0.1', 41930)
--- Active Connections : 1 ---

looping 0
b'\x80\x04\x95/\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x05#@REG\x94]\x94(\x8c\x03162\x94\x8c\x03195\x94\x8c\x03286\x94\x8c\x03190\x94\x8c\x03226\x94ee.'
['#@REG', ['162', '195', '286', '190', '226']]
{(1, '127.0.0.1', 41931): ['162', '195', '286', '190', '226']}
connection from ('127.0.0.1', 51094)
b'\x80\x04\x95.\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x05#@REG\x94]\x94(\x8c\x0296\x94\x8c\x03187\x94\x8c\x03205\x94\x8c\x03244\x94\x8c\x03186\x94ee.'
--- Active Connections : 2 ---
['#@REG', ['96', '187', '205', '244', '186']]

looping 0
{(1, '127.0.0.1', 41931): ['162', '195', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186']}
connection from ('127.0.0.1', 51096)
b'\x80\x04\x95,\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x05#@REG\x94]\x94(\x8c\x0270\x94\x8c\x03283\x94\x8c\x0214\x94\x8c\x0299\x94\x8c\x03296\x94ee.'
--- Active Connections : 3 ---
['#@REG', ['70', '283', '14', '99', '296']]

looping 0
{(1, '127.0.0.1', 41931): ['162', '195', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186'], (3, '127.0.0.1', 51097): ['70', '283', '14', '99', '296']}
connection from ('127.0.0.1', 51102)
--- Active Connections : 4 ---

looping 0
b'\x80\x04\x95,\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x05#@REG\x94]\x94(\x8c\x0253\x94\x8c\x015\x94\x8c\x03280\x94\x8c\x03277\x94\x8c\x03135\x94ee.'
['#@REG', ['53', '5', '280', '277', '135']]
{(1, '127.0.0.1', 41931): ['162', '195', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186'], (3, '127.0.0.1', 51097): ['70', '283', '14', '99', '296'], (4, '127.0.0.1', 51103): ['53', '5', '280', '277', '135']}
connection from ('127.0.0.1', 53046)
--- Active Connections : 5 ---

looping 0
b'\x80\x04\x95/\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x05#@REG\x94]\x94(\x8c\x03164\x94\x8c\x03144\x94\x8c\x03233\x94\x8c\x03132\x94\x8c\x03297\x94ee.'
['#@REG', ['164', '144', '233', '132', '297']]
{(1, '127.0.0.1', 41931): ['162', '195', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186'], (3, '127.0.0.1', 51097): ['70', '283', '14', '99', '296'], (4, '127.0.0.1', 51103): ['53', '5', '280', '277', '135'], (5, '127.0.0.1', 53047): ['164', '144', '233', '132', '297']}

```
the server prints its data whenever any operation is made

now the client when run
```
('127.0.0.1', 53046)
None
registered successfully with id 5
['164', '144', '233', '132', '297']

Operations:
1. Query Book
2. print library
3. QUIT
(Enter choice):

```
now when a book is searched 3 casees are possible:
(1) book is in client's own library

**call to server is not made in this case** 
```
1. Query Book
2. print library
3. QUIT
(Enter choice):1
enter the book name164
file already in your folder
['164', '144', '233', '132', '297']
```

(2) book is in anothers clients library 
* server
```
['#@SEARCH', '195']
{(1, '127.0.0.1', 41931): ['162', '195', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186'], (3, '127.0.0.1', 51097): ['70', '283', '14', '99', '296'], (4, '127.0.0.1', 51103): ['53', '5', '280', '277', '135'], (5, '127.0.0.1', 53047): ['164', '144', '233', '132', '297']}
b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x05#@UPD\x94K\x05\x8c\t127.0.0.1\x94M\xcb\xa3\x8c\x03195\x94e.'
['#@UPD', 5, '127.0.0.1', 41931, '195']
{(1, '127.0.0.1', 41931): ['162', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186'], (3, '127.0.0.1', 51097): ['70', '283', '14', '99', '296'], (4, '127.0.0.1', 51103): ['53', '5', '280', '277', '135'], (5, '127.0.0.1', 53047): ['164', '144', '233', '132', '297', '195']}

```
* client peer
```
['164', '144', '233', '132', '297']

Operations:
1. Query Book
2. print library
3. QUIT
(Enter choice):1       
enter the book name 195
[(1, '127.0.0.1', 41931)]
book found in peer 1 want to download (y for yes )y
51
receiving data...
recived the data
['164', '144', '233', '132', '297', '195']

```
* server peer
```
('127.0.0.1', 41930)
None
registered successfully with id 1
['162', '195', '286', '190', '226']

Operations:
1. Query Book
2. print library
3. QUIT
(Enter choice):    
 Accepted connection from ('127.0.0.1', 60188) ---

done sending
['162', '286', '190', '226']

```


(3) book is not available anywhere
* server
```
['#@SEARCH', '234']
{(1, '127.0.0.1', 41931): ['162', '195', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186'], (3, '127.0.0.1', 51097): ['70', '283', '14', '99', '296'], (4, '127.0.0.1', 51103): ['53', '5', '280', '277', '135'], (5, '127.0.0.1', 53047): ['164', '144', '233', '132', '297']}
```
* client
```
(Enter choice):1
enter the book name 234
[None]
book 234  not found
['164', '144', '233', '132', '297']

```
print client
```
Operations:
1. Query Book
2. print library
3. QUIT
(Enter choice):2
['164', '144', '233', '132', '297', '195']
['164', '144', '233', '132', '297', '195']
```

Quit

* client
```
Operations:
1. Query Book
2. print library
3. QUIT
(Enter choice):3
--- Connection with Server closed ---
['164', '144', '233', '132', '297', '195']
```

* server
```
{(1, '127.0.0.1', 41931): ['162', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186'], (3, '127.0.0.1', 51097): ['70', '283', '14', '99', '296'], (4, '127.0.0.1', 51103): ['53', '5', '280', '277', '135'], (5, '127.0.0.1', 53047): ['164', '144', '233', '132', '297', '195']}
b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00]\x94\x8c\x06#@QUIT\x94a.'
['#@QUIT']
{(1, '127.0.0.1', 41931): ['162', '286', '190', '226'], (2, '127.0.0.1', 51095): ['96', '187', '205', '244', '186'], (3, '127.0.0.1', 51097): ['70', '283', '14', '99', '296'], (4, '127.0.0.1', 51103): ['53', '5', '280', '277', '135']}
```
 
### Testing 
mannually tested with 1 server and 5 clients in default configuration.

### Enhancements
Possible enhancements to this project are:
* Ping the requesting peer to calculate latency.
* Assign the network bandwidth to each peer.
### Issues
Possible issues to this project are:
* if a client crashes server still contains it's data.

