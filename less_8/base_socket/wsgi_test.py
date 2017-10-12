from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    # qs = parse_qs(environ['QUERY_STRING'])
    # a = escape(qs.get('name',[''])[0])
    # print(a)
    # return [('{} = {}\n'.format(k, str(v))).encode('UTF-8') for k, v in qs.items()]
    # try:
    #     size = int(environ.get('CONTENT_LENGTH',0))
    # except ValueError:
    #     size = 0
    # data = environ['wsgi.input'].read(size)
    # m_data = parse_qs(data)
    # # curl --data "param1=value1&param2=value2" http://localhost:8080/
    # return [('{} = {}\n'.format(k, str(v))).encode('UTF-8') for k, v in m_data.items()]

httpserv = make_server('localhost', 8080, app)
httpserv.serve_forever()