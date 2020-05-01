from myhttpserver import MyHttpServer

class CountUp(MyHttpServer):

    def __init__(self):
        super().__init__()

    def get(self, request):
        counter = request.session_get('counter')
        if counter is None:
            counter = 0
        counter += 1
        request.session_set('counter', counter)
        print(self.session_dic)
        send_cookie = '<!DOCTYPE html><html><head><meta charset=\"UTF-8\"></head><body><h1>Hello, world!</h1> <p>You have visited this page for {0} times.</p><form method="post"><button type="submit">post</button></body></html>'.format(counter)
        print(send_cookie)
        return send_cookie

    def post(self):
        return '<!DOCTYPE html><html><head><meta charset=\"UTF-8\"></head><body><h1>post method used</h1></body></html>'


if __name__ == '__main__':
    count_up = CountUp()
    count_up.start()