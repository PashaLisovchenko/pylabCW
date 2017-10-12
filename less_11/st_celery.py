from celery import Celery

BROKER_URL = ''
app = Celery('hello', broker=BROKER_URL)


@app.task
def hello():
    return 'hello world'