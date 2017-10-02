from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule


def mindex(req):
    return Response('index page')

def mhash(req, hash_url):
    return Response('hash = {}'.format(hash_url))

map_rule = Map([
    Rule('/', endpoint='index'),
    Rule('/<hash_url>', endpoint='hash')

])
views = {
    'index': mindex,
    'hash': mhash,
}
# def app(environ, start_response):
#     req = Request(environ)
#     # req.-> files, path, method, headers.
#     print(req.args, req.form)
#
#     resp = Response('hello', mimetype='text/plain')
#     return resp(environ, start_response)


@Request.application
def app_dec(request):
    res = Response('Hello')
    res.status = '200 OK'
    print(request.args.getlist('a'))
    return res


def app(environ, start_response):
    urls = map_rule.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
    except Exception:
        start_response('404 Not found')
        return [b'rule not found']
    print(endpoint)
    print(args)
    resp = views[endpoint](Request(environ), **args)
    return resp(environ, start_response)


if __name__ == '__main__':
    try:
        from werkzeug.serving import run_simple
        run_simple('localhost', 2000, app)
    except KeyboardInterrupt:
        print('Goodbye.')