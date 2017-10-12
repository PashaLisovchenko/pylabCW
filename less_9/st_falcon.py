import falcon
import json

data = []


class Resource():

    def on_get(self, req, resp):
        resp.body = json.dumps(data)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if req.content_length:
            req_data = json.loads(req.stream.read().decode())
            data.append(req_data)
        resp.status = falcon.HTTP_201
        print(data)


app = application = falcon.API()

app.add_route('/', Resource())


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        http_srv = make_server('localhost', 8080, app)
        http_srv.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')

# curl --data '{"mess": "hello"}' http://lacalhost:8080/
#Tornado, aiohttp, Twisted, RPC gRPC SOAP
#  coroutines
# async.io
# async/awayt PEP 5..
# async def a():
#     await b()