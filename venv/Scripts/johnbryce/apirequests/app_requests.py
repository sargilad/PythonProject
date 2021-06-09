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

    def create_project(self, body) -> json:
        try:
            response = self.rest_client.post(self.projects_url, body, self._build_request_header())
            if response.status_code == HTTPStatus.CREATED:
                print(f"project CREATE: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None

    def get_single_project(self, id: int) -> json:
        try:
            response = self.rest_client.get(self.projects_url + str(id), self._build_request_header())
            if response.status_code == HTTPStatus.OK:
                print(f"project GET: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None  # might cause NPE

    def update_project(self, id, body):
        try:
            response = self.rest_client.patch(self.projects_url + str(id), body, self._build_request_header())
            if response.status_code == HTTPStatus.OK:
                print(f"project PATCH: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None

    def delete_project(self, id, body):
        try:
            response = self.rest_client.delete(self.projects_url + str(id), body, self._build_request_header())
            response_code = response.status_code
            if response_code == HTTPStatus.NO_CONTENT:
                print(f"project DELETE: success")
                return ""
        except Exception as e:
            print(e)
            return None

    def create_work_package(self, body) -> json:
        try:
            response = self.rest_client.post(self.work_pkg_url, body, self._build_request_header())
            if response.status_code == HTTPStatus.CREATED:
                print(f"package CREATE: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None

    def get_work_package(self, id: int) -> json:
        try:
            response = self.rest_client.get(self.work_pkg_url + str(id), self._build_request_header())
            if response.status_code == HTTPStatus.OK:
                print(f"package GET: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None  # might cause NPE

    def update_work_package(self, id, body):
        try:
            response = self.rest_client.patch(url=self.work_pkg_url + str(id), body=body,
                                              headers_list=self._build_request_header())
            if response.status_code == HTTPStatus.OK:
                print(f"package PATCH: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None

    def delete_work_package(self, id:int, body:dict={}):
        try:
            response = self.rest_client.delete(self.work_pkg_url + str(id), body, self._build_request_header())
            response_code = response.status_code
            if response_code == HTTPStatus.NO_CONTENT:
                print(f"package DELETE: success")
                return ""
        except Exception as e:
            print(e)
            return None

    def _build_request_header(self) -> dict:
        return {self._HeadersEnum.AUTHORIZATION.value: 'Basic ' + self.api_token,
                self._HeadersEnum.CONTENT_TYPE.value: self._HeadersEnum.APPLICATION_JSON.value}

    class _HeadersEnum(Enum):
        CONTENT_TYPE = 'Content-type'
        APPLICATION_JSON = 'application/json; charset=UTF-8'
        AUTHORIZATION = 'Authorization'
