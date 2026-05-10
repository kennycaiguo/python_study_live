import socket
import concurrent.futures

# 存活探测
def alive_scan(ip):
    port_list = [22, 23, 53, 80, 443, 3389, 10022]
    port_len = len(port_list)
    num = 0
    for port in port_list:
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, port))
            sock.close()
            return True
        except socket.error:
            num += 1
            if num == port_len:
                return False
            else:
                continue

# 全端口探测
# 利用socket tcp进行探测端口存活
def all_port_scan(ip,port,live_port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock_https = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip, port))
        sock_https.connect((ip,port))
        sock.close()
        live_port.append(port)
        return live_port
    except socket.error as error:
        # print(error)
        # print(port)
        return 1

# 线程调度模块
def threadMode(ip):
    thread_list = []
    live_port = []
    num = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=20000) as executor:
        print("目标:{},端口探测中".format(ip))
		# 这里选择探测端口的范围，这里也可以改成列表形式，自定义扫描端口。当然也可以改成(1,65536)进行全端口探测，只是发包太大，结果失真。
        for port in range(1,6000):
            # num+=1
            # if num in [5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000]:
            #     time.sleep(3)
            thread_task = executor.submit(all_port_scan,ip,port,live_port)
            thread_list.append(thread_task)
        for res in concurrent.futures.as_completed(thread_list):
            result = res.result()
            if result != 0 and result != 1:
                # 返回存活端口列表
                return result
            else:
                return 1

# 进程，线程之间的调度逻辑中心模块
def power_control_mode(ip_list):
    process_list = []
	# 这里通过concurrent.futures创建四个进程，每个进程在分配到各自需要探测的IP后后会传入多线程模块，启动多线程~
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as process_executor:
        for ip in ip_list:
            process_task = process_executor.submit(threadMode,ip)
            process_list.append(process_task)
        for res in concurrent.futures.as_completed(process_list):
            port_live = res.result()
            if port_live != 1:
                print("存活端口列表")
                print(port_live)
            else:
                pass


if __name__ == "__main__":
    iplist = ["1.1.1.1"]
    live_ip = []
    for i in iplist:
        status = alive_scan(i)
        print("目标:{}:{}".format(i,status))
        live_ip.append(i)
        if status:
            power_control_mode(live_ip)