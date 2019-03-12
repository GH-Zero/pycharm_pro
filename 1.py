from socket import *
ip_port=('192.168.0.107',8090)
long=5
siazi=1024

cilan=socket(AF_INET,SOCK_STREAM)
cilan.connect(ip_port)
while True:
    d=input('请输入:')
    if not d:
     print('请重新请输入')
    else:
     cilan.send(d.encode('utf-8'))
     d=cilan.recv(siazi).decode('utf-8')
     print('服务端回复：',d)

cilan.close()
