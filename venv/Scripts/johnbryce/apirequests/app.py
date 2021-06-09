from app_requests import RestRequests
from rest_entities import OpenProjectEntities
from utilities import CommonUtilities

domain = "https://jbfinal3.openproject.com/"
api_token = "YXBpa2V5OjE5ZjgxMjM1ZGRiMjVjMDM2N2RjMjA2YjE4MTFmZGUwMzViYWU5NWIzOTg1MGY1N2I3Mjk0ZTc5ODUxYTg4YWI="

entities = OpenProjectEntities()
posts_requests = RestRequests(domain, api_token)

body = entities.get_project_create_body(CommonUtilities.get_random_string(prefix="project_"))
response = posts_requests.create_project(body)
print(response)
