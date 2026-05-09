from ftplib import FTP

# use your real username to assign to user ,your real password assign to passwd
def main(host='192.168.100.138', port=21, user='your user name', passwd='your password', start_dir=''):
    ftp = FTP()
    ftp.connect(host=host, port=port)
    ftp.login(user=user, passwd=passwd)
    ftp.cwd(start_dir)
    L = ftp.nlst()
    print(L)


if __name__ == '__main__':
    main()