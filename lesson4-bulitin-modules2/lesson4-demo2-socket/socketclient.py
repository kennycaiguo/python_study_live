import socket

host = "127.0.0.1"
port = 9999
buf_size = 4096
addr = (host,port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

while True:
    data = input(">>>")
    if not data: break
    if data == 'quit':
        break
    client.send(data.encode())
    recv_data = client.recv(buf_size)
    if not recv_data:break
    print(f"received data:{recv_data.decode()}")

client.close()

    