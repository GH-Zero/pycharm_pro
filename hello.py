from socket import *
IP_port=('192.168.0.107',8090)
bank_log=5
buffer_size=1024
tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(IP_port)
tcp_server.listen(bank_log)
conn,ad=tcp_server.accept()
print('双相连接',conn)
print('客户地址',ad)
while True:
    a=conn.recv(buffer_size)
    print('客户发的消息',a.decode('utf-8'))
    h=input('请回复：')
    n=conn.send(h.encode('utf-8'))
conn.close()
tcp_server.close()
