import socket
import random, string
import re

class MyHttpServer:

    def __init__(self):
        self.PORT = 8005
        self.HOST = '127.0.0.1'
        self.CRLF = "\r\n"
        self.BUFFER_SIZE = 1024
        self.COOKIE_SIZE = 10
        self.session_dic = {}
    
    def createRandom(self, n):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
        return ''.join(randlst)

    def createResponse(self, data):
        if "Cookie" in data:
            id_found = (re.search(r'id=([a-xA-Z0-9_]+)', data)).group()
            id_register = id_found[3:]
        else:
            id_register = self.createRandom(self.COOKIE_SIZE)
        message_lists = [
                'HTTP/1.1 200 OK',
                'Date: Mon, 26 Mar 2018 04:07:56 GMT',
                'Content-Type: text/html; charset=utf-8',
                'Connection: keep-alive'
                ]

        # HTML = '<!DOCTYPE html><html><head><meta charset=\"UTF-8\"></head><body><h1>Visit count : {}</h1></body></html>'.format(visit_count)
        send_message=""
        for message in message_lists:
            send_message += message+self.CRLF
        send_message += self.get(id_register)
        send_binary = send_message.encode()
        return send_binary

    def session_get(self, id, key):
        if self.session_dic.get(id) is None:
            return None
        else:
            return (self.session_dic.get(id)).get(key)

    def session_set(self, id, key, value):
        self.session_dic[id][key] = value

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #(IPアドレス,ポート)の指定
            s.bind((self.HOST, self.PORT))
            #キューの最大数を指定
            s.listen(5)
            while True:
                #(コネクション，クライアント側のポート番号)
                (connection, client) = s.accept()
                try:
                    print('Client connected', client)
                    #データ取得
                    data = connection.recv(self.BUFFER_SIZE).decode()
                    print('data : {}, addr: {}'.format(data, client))
                    connection.send(self.createResponse(data))
                    print(self.session_dic)
                finally:
                    connection.close()

class HttpError:
    pass