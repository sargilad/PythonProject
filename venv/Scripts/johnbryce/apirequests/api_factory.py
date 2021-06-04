import http.client


class RestClient:
    host = ""
    conn = None

    def __init__(self, host):
        self.host = host
        self.conn = http.client.HTTPConnection(host,None, 5)

    def get(self, url):
        self.conn.request("GET", url)
        return self.conn.getresponse()



