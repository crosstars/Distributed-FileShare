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
server and client will reflect location changes.
### Sample output

### Testing 
mannually tested with 1 server and 5 clients in default configuration.

### Enhancements
Possible enhancements to this project are:
* Ping the requesting peer to calculate latency.
* Assign the network bandwidth to each peer.
### Issues
Possible issues to this project are:
* if a client crashes server still contains it's data.

