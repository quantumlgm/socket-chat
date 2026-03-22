# Multi-threaded Console Chat on Python Sockets
A simple, robust terminal-based chat application built with Python using low-level sockets and multi-threading

## 📂 Features
* **Multi-user Support**: Multiple clients can join and chat simultaneously.
* **Concurrency**: Powered by `threading` to handle I/O operations without blocking.
* **Connection Management**: Automatic cleanup and removal of disconnected clients.
* **Minimalist UI**: Clean, distraction-free terminal interface.

## 🔧 Tech stack
* **Language**: Python 3.x (3.14.3)
* **Modules**: `socket`, `threading`, `sys`


# 📦 How to Run
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
