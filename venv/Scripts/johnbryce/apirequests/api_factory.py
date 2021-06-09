import requests


class RestClient:
    def __init__(self):
        pass

    def get(self, url):
        return requests.get(url)

    def post(self, url, body, headers_list):
        return requests.post(url, json=body, headers=headers_list)

    def patch(self, url, body, headers_list):
        return requests.patch(url, json=body, headers=headers_list)

    def delete(self, url, body, headers_list):
        return requests.delete(url, json=body, headers=headers_list)
