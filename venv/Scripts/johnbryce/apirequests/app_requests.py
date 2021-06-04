from api_factory import RestClient
import json


class PostsRequests:
    uri = '/posts'
    rest_client = None

    def __init__(self, host):
        self.rest_client = RestClient(host)

    def get_single_post(self, id: int) -> str:
        try:
            response = self.rest_client.get(self.uri + '/' + str(id))
            response_code = response.status
            if response_code == 200:
                response_data = response.read().decode("utf-8")
                return json.loads(response_data)
        except Exception as e:
            print(e)
            return None  # might cause NPE

    def get_posts(self):
        try:
            response = self.rest_client.get(self.uri)
            response_code = response.status
            if response_code == 200:
                response_data = response.read().decode("utf-8")
                return json.loads(response_data)
        except Exception as e:
            print(e)
            return None  # might cause NPE
