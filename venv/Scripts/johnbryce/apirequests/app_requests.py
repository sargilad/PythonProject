from api_factory import RestClient
import json


class PostsRequests:
    domain = "https://jsonplaceholder.typicode.com/posts/"
    rest_client = None

    def __init__(self):
        self.rest_client = RestClient()

    def get_single_post(self, id: int) -> json:
        try:
            response = self.rest_client.get(self.domain + str(id))
            response_code = response.status_code
            if response_code == 200:
                return response.json()
        except Exception as e:
            print(e)
            return None  # might cause NPE

    def get_posts(self) -> json:
        try:
            response = self.rest_client.get(self.domain)
            response_code = response.status_code
            if response_code == 200:
                return response.json()
        except Exception as e:
            print(e)
            return None  # might cause NPE

    def create_post(self, body):
        try:
            self.rest_client.post(self.domain, body, "{'Content-type': 'application/json; charset=UTF-8',}")
        except Exception as e:
            print(e)
            return None
