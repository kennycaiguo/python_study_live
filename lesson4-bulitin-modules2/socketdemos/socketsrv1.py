"""
socket server
"""
import socket
import time

# 1. 创建Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定地址和端口
server_socket.bind(('127.0.0.1', 9999))
# 3. 监听
server_socket.listen(5)
print("服务器等待连接...")

while True:
    # 4. 接受连接
    client_socket, addr = server_socket.accept()
    print(f"连接来自: {addr}")
    
    # 5. 接收数据
    data = client_socket.recv(1024)
    print(f"收到数据: {data.decode()}")
    
    # 发送数据
    client_socket.send(f"{time.ctime()},client data:{data.decode()}".encode())
    client_socket.close()

