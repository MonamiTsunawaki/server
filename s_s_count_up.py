from myhttpserver import MyHttpServer, HttpError

class CountUp(MyHttpServer):

    def __init__(self):
        super().__init__()

    def get(self, id):
        counter = self.session_get(id, 'counter')
        if counter is None:
            self.session_dic[id] = {'counter':0}
        counter = self.session_get(id, 'counter')
        counter += 1
        self.session_set(id, 'counter', counter)
        send_cookie = 'Set-Cookie: id='
        send_cookie += id
        send_cookie += self.CRLF+self.CRLF
        send_cookie += '<!DOCTYPE html><html><head><meta charset=\"UTF-8\"></head><body><h1>Hello, world!</h1> <p>You have visited this page for {0} times.</p></body></html>'.format(counter)
        print(send_cookie)
        return send_cookie

    def post(self):
        raise HttpError(405, 'Post method is not supported')


if __name__ == '__main__':
    count_up = CountUp()
    count_up.start()