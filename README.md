# Multi-threaded Socket Chat

A terminal-based chat application implemented using Python's low-level `socket` library and multi-threading for concurrent client-server communication.

## Features
* **Concurrent Connections**: Supports multiple simultaneous clients using the `threading` module.
* **TCP/IP Networking**: Built on the Transmission Control Protocol for reliable data delivery.
* **Server-side Management**: Real-time monitoring of active connections and automated cleanup of disconnected peers.
* **Broadcast Logic**: Efficient message distribution from the server to all connected users.

## Tech Stack
* **Language**: Python 3.14.3
* **Core Modules**: `socket`, `threading`, `sys`

# How to Run
### Clone repo
```bash
git clone https://github.com/quantumlgm/socket-chat.git
cd socket-chat
```
### Start the Server
```bash
python server.py
```
### Start the Client (Connect from multiple terminals to communicate!)
```bash
python client.py
```
