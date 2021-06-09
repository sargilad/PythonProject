from enum import Enum
from http import HTTPStatus

from api_factory import RestClient
import json


class RestRequests:
    projects_url = ''
    work_pkg_url = ''
    rest_client = None
    api_token = ''

    def __init__(self, domain: str, api_token: str):
        self.rest_client = RestClient()
        self.projects_url = domain + "api/v3/projects/"
        self.work_pkg_url = domain + "api/v3/work_packages/"
        self.api_token = api_token

    def create_project(self, body):
        try:
            response = self.rest_client.post(self.projects_url, body, {
                HeadersEnum.AUTHORIZATION.value: 'Basic ' + self.api_token, })
            if response.status_code == HTTPStatus.CREATED:
                return response.json()
        except Exception as e:
            print(e)
            return None

    def get_single_project(self, id: int) -> json:
        try:
            response = self.rest_client.get(self.domain + str(id))
            response_code = response.status_code
            if response_code == 200:
                return response.json()
        except Exception as e:
            print(e)
            return None  # might cause NPE

    def update_project(self, body):
        try:
            response = self.rest_client.post(self.domain, body, {'Content-type': 'application/json; charset=UTF-8', })
            response_code = response.status_code
            if response_code == 200:
                return response.json()
        except Exception as e:
            print(e)
            return None

    def delete_project(self, body):
        try:
            response = self.rest_client.post(self.domain, body, {'Content-type': 'application/json; charset=UTF-8', })
            response_code = response.status_code
            if response_code == HTTPStatus.CREATED:
                return response.json()
        except Exception as e:
            print(e)
            return None

    def get_posts(self) -> json:
        try:
            response = self.rest_client.get(self.domain)
            response_code = response.status_code
            if response_code == 200:
                return response.json()
        except Exception as e:
            print(e)
            return None  # might cause NPE


class HeadersEnum(Enum):
    CONTENT_TYPE = 'Content-type'
    APPLICATION_JSON = 'application/json; charset=UTF-8'
    AUTHORIZATION = 'Authorization'
