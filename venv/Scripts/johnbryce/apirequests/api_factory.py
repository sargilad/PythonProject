import requests


class RestClient:
    def __init__(self):
        pass

    def get(self, url):
        return requests.get(url)

    def post(self, url, body, headers_list):
        return requests.post(url, data=body, headers=headers_list)
