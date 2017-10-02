from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "index page"

@app.route('/')
@app.route('/<hash_url>', methods = ['GET'])
def mhash(hash_url=0):
    req = request
    a = vars(req)
    print(a['environ']['REQUEST_METHOD'])
    return render_template('hash.html', hash=hash_url, params = range(5))

if __name__ == "__main__":
    app.run()