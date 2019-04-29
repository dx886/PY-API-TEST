import requests
class HttpRequest:
    def __init__(self):
        self.session = requests.sessions.session()
    def Request(self, method, url, data=None, json=None):
        method = method.upper()
        if method == 'GET':
            resp = self.session.request(method=method, url=url, params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method=method, url=url, json=json)
            else:
                resp = self.session.request(method=method, url=url, data=data)
        else:
            resp = None
            print('UN-support method')
        return resp

    def close(self):
        self.session.close()
