from app_requests import RestRequests
from rest_entities import OpenProjectEntities
from utilities import CommonUtilities

# todo: bring from config file
domain = "https://jbfinal3.openproject.com/"
api_token = "YXBpa2V5OjE5ZjgxMjM1ZGRiMjVjMDM2N2RjMjA2YjE4MTFmZGUwMzViYWU5NWIzOTg1MGY1N2I3Mjk0ZTc5ODUxYTg4YWI="

def main():
    entities = OpenProjectEntities()
    posts_requests = RestRequests(domain, api_token)

    # create project
    body = entities.get_project_create_body(CommonUtilities.get_random_string(prefix="project_"))
    project = posts_requests.create_project(body)

    # Get project
    project = posts_requests.get_single_project(project['id'])
    print()




if __name__ == '__main__':
    main()
