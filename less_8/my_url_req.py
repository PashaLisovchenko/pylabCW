from urllib.request import urlopen
import requests

# Request(url, data, headers, orh, ..., method)
# data, timeout, context
# data POST
with urlopen('http://google.com') as r:
    print(r.read())


r = requests.get('http://google.com', params={}, auth={})
print(r.headers)
# text, content, json
# requests.post('http://google.com',
#               params={},
#               data={},
#               headers={},
#               allow_redirect=True,
#               json={})
