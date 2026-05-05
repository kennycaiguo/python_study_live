import socket
import threading

def handle_client(sock_cl,addr):
    try:
        while True:
            request = sock_cl.recv(1024)
            if request.lower() == "close":
               sock_cl.send("Client closed".encode('utf-8')) 
               print("closing...")
               break
            print(f"Client Message:{request.decode('utf-8')}")
            response = f"Client Message {request.decode('utf-8')} Accepted"
            sock_cl.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error when hanlding client: {e}")

    finally:      
        sock_cl.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")

def run_server():
    ip = "127.0.0.1"
    port = 8000
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip,port))
        server.listen(0)
        print("Waiting for client:")
        while True:
            conn,addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr,))
            thread.start()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()

if __name__ == '__main__':
    run_server()        
         
        