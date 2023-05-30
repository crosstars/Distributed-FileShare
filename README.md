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
sending reals books are not implimented , it is simulated by list elements , book names are random integer strings , book contents list element is returned as file eklements 
### How-to
##### configuration
configure the server by editing configure.py

##### indexing server - How-to

You must run the indexing server first. So you run the python server.py first
* Run _server.py_ . Output should look like this:
`````
 arcshare]$ python3 server.py
started
looping 0



```
when a peer connects 
output should look like this :
```
connection from ('127.0.0.1', 44602)
b'\x80\x04\x95.\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x05#@REG\x94]\x94(\x8c\x0299\x94\x8c\x03260\x94\x8c\x03107\x94\x8c\x03188\x94\x8c\x03190\x94ee.'
['#@REG', ['99', '260', '107', '188', '190']]
--- Active Connections : 1 ---

looping 0
{(1, '127.0.0.1', 44603): ['99', '260', '107', '188', '190']}

```
In the above running example,
 We run _client.py_ one more time to run peer.
##### Peer - How-to
```
1 - Run Server
2 - Run Peer
Please select whichever you want.
2
```
```
Please enter server's port number
45000
```
You have to enter server's port number which it is currently listening to, which is _45000_(check indexing server configurations) in our case.
```
Please enter servers IP number in the following format XXX.XXX.XXX.XXX and 0 for localhost
0
```
We choose "_0_" since we are running on local machine. Next output is:
```
1 - Search for a filename and download it.
2 - Register to the indexing server.
2
```
We chose "_2_" in order to register files to the indexing server(choose "_1_" if you have registered files already).
```
Please enter your port number
25000
Please enter your IP number in the following format XXX.XXX.XXX.XXX and 0 for localhost
0
``` 
We chose a random port (_25000_) as a peer to listen to for incoming requests to download specific files, and "_0_" for localhost
```
Please enter the directory path of which you want to share its files.
/path/to/this/project/peer/testing_files
Congratulations you have been registered successfully.
[*] You will now be put to the listening state.
[*] Started listening on localhost : 25000
```
You are now blocked and waiting for another peers to request files to download. Now let's search for a file.
We run _main.py_ one more time as a peer and we enter same configurations for the server and we get to the following output again. 
_(Case that only one peer has the file)_
```
1 - Search for a filename and download it.
2 - Register to the indexing server.
1
Please enter filename you want to search for.
1.txt
File 1.txt was found in the following one or more peers. Peer/s details are::

Peer port: 25000 

Peer host: localhost 

Shared file path: /path/to/this/project/peer/testing_files 

File shared at: 2017-10-31 20:27:41 

Do you want to download it (Y/N): y
Successfully get the file
connection closed
```
_(Case that one or more peer has the file)_
```
File 6.txt was found in the following one or more peers. Peer/s details are:

Peer ID: 1 

Peer port: 25000 

Peer host: localhost 

File shared at: 2017-12-09 21:11:42 

-------------------------------------
Peer ID: 2 

Peer port: 35000 

Peer host: localhost 

File shared at: 2017-12-09 21:11:53 

-------------------------------------
Do you want to download it (Y/N):
y
Please specify Peer ID
1
Successfully get the file
connection closed
```
Downloaded file should be found in: _/path/to/this/project/peer/downloads/downloaded_1.txt_

For the peer that is running waiting for requests the output is(Which has the actual file):
```
[*] You will now be put to the listening state.
[*] Started listening on localhost : 25000
[*] Got a connection from  127.0.0.1 : 51702
Done sending
```
Hopefully that illustrated how this project runs and overall idea of _Napster File-Sharing System_

### Enhancements
Possible enhancements to this project are:
* Allow editing files for the registered peer.
* Ping the requesting peer to calculate latency.
* Assign the network bandwidth to each peer.
### Issues
Please for any code issues feel free to submit an issue to this repository and I will answer shortly
