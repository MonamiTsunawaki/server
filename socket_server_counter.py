import socket

#サーバー側のポート番号
PORT = 8008
HOST = '127.0.0.1'
CRLF = "\r\n"
BUFFER_SIZE = 1024

def createResponse(visit_count):
    message_lists = [
            'HTTP/1.1 200 OK',
            'Date: Mon, 26 Mar 2018 04:07:56 GMT',
            'Set-Cookie: count='+str(visit_count),
            'Content-Type: text/html; charset=utf-8',
            'Connection: keep-alive'
            ]

    HTML = '<!DOCTYPE html><html><head><meta charset=\"UTF-8\"></head><body><h1>Visit count : {}</h1></body></html>'.format(visit_count)
    send_message=""
    for message in message_lists:
        send_message += message+CRLF
    send_message += CRLF
    send_message += HTML
    send_binary = send_message.encode()
    return send_binary

def main(visit_count):

    ### .socket(ソケットが利用できるアドレス体系,ソケットの性質)　ソケットを作成する
    # AF_INET:IPv4 によるソケット
    # AF_INET6:IPv6 によるソケット
    # AF_UNIX:ローカルなプロセス間通信用のソケット
    # SOCK_STREAM:順序性と信頼性があり、双方向の接続されたバイトストリーム（byte stream）を提供する(TCP)
    # SOCK_DGRAM:データグラム（接続、信頼性なし、固定最大長メッセージ）をサポートする(UDP)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #(IPアドレス,ポート)の指定
        s.bind((HOST, PORT))
        #キューの最大数を指定
        s.listen(5)
        while True:
            #(コネクション，クライアント側のポート番号)
            (connection, client) = s.accept()
            try:
                print('Client connected', client)
                #データ取得
                data = connection.recv(BUFFER_SIZE).decode()
                print('data : {}, addr: {}'.format(data, client))
                if ('Cookie:' in data) == True:
                    visit_count+=1
                print("visit count")
                print(visit_count)

                connection.send(createResponse(visit_count))
            finally:
                connection.close()

if __name__=='__main__':
    main(0)