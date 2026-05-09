import socket
import ssl

def ssl_demo1():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    context = ssl.create_default_context()
    ssl_s = context.wrap_socket(sock=s,server_hostname='google.com')

    # 连接服务器
    ssl_s.connect(('www.google.com', 443))
    # 发送数据
    ssl_s.send(b'GET / HTTP/1.1\r\n\r\n')

    # 接收数据
    data = ssl_s.recv(1024)
    print(data.decode('utf-8'))

    ssl_s.close()

def ssl_demo2():
    import socket
    import ssl

    # 1. 创建一个标准的TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 创建一个SSL上下文，推荐使用默认配置
    context = ssl.create_default_context()

    # 3. 使用wrap_socket包装socket，需指定服务器的主机名用于证书验证
    # 这一步会处理SSL握手
    secure_sock = context.wrap_socket(sock, server_hostname='google.com')

    # 4. 连接服务器
    secure_sock.connect(('www.google.com', 443))

    # 5. 安全地发送和接收数据
    # secure_sock.sendall(b"GET / HTTP/1.1\r\nHost: ://google.com\r\n\r\n")
    secure_sock.sendall(b"GET / HTTP/1.1\r\n\n")
    print(secure_sock.recv(1024))

    # 6. 关闭连接
    secure_sock.close() # 包装后的socket会自动处理底层socket的关闭 
def ssl_demo3():
    import socket
    import ssl

    hostname = 'www.python.org'
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            # print(ssock.version())     
            ssock.send(b'GET / HTTP/1.1\r\n\r\n')  
            data = ssock.recv(1024)
            print(data.decode('utf-8'))

if __name__ == '__main__':
    # ssl_demo1()    
    # ssl_demo2()    
    ssl_demo3()    

    