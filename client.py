from socket import *
a=('127.0.0.1',9021)
l=5
s=1024
def suib():
    m=socket(AF_INET,SOCK_STREAM)
    m.bind(a)
    m.listen(l)
    conn,add=m.accept()
    conn.recv(s)
    conn.sendall(bytes('<http/1.1 OK\r\n\r\n','utf-8'))
    conn.sendall(bytes('<h1>nimabi</h1>'.encode('utf-8')))

    conn.close()
if __name__ == '__main__':
    suib()