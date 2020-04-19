from datetime import datetime
import socket

def main():
    print('The client started at', datetime.now())

    HOST = '127.0.0.1'
    CRLF = "\r\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 8000))

        message_lists = [
            'GET / HTTP/1.1',
            'host:www.google.com',
            ]
        send_message=""
        for message in message_lists:
            send_message += message+CRLF
        send_message += CRLF
        send_binary = send_message.encode()

        s.sendall(send_binary)
        data = s.recv(1024).decode()
        print(data)

if __name__=='__main__':
    main()