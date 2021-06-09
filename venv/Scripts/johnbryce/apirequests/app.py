from app_requests import RestRequests
from rest_entities import OpenProjectEntities
from utilities import CommonUtilities
import configparser

config_parser = configparser.ConfigParser()
config_parser.read('config.ini')
questions_sections_list = config_parser.sections()

domain = config_parser['env']['domain']
api_token = config_parser['user']['api_token']


def main():
    entities = OpenProjectEntities()
    rest_requests = RestRequests(domain, api_token)

    # create project
    body = entities.get_project_create_body(project_name=CommonUtilities.get_random_string(prefix="proj_"))
    project = rest_requests.create_project(body)

    # Get project
    project = rest_requests.get_single_project(id=project['id'])

    # Update project
    body = entities.get_project_update_body(description="This is a project description")
    project = rest_requests.update_project(project['id'], body)

    # Delete project
    project = rest_requests.delete_project(id=project['id'], body={})

    # Create work package
    body = entities.get_project_create_body(project_name=CommonUtilities.get_random_string(prefix="proj_"))
    project = rest_requests.create_project(body)

    body = entities.get_create_work_package_body(pkg_name=CommonUtilities.get_random_string(prefix="pkg_"),
                                                 project_ref=project['_links']['self']['href'],
                                                 pkg_type="/api/v3/types/1")
    pkg = rest_requests.create_work_package(body=body)

    # GET work package
    pkg = rest_requests.get_work_package(id=pkg['id'])

    # update work package
    lock_version = pkg['lockVersion']
    body = entities.get_work_package_update_body(lock_version=lock_version, description="This is a package description")
    pkg = rest_requests.update_work_package(id=pkg['id'], body=body)

    # delete work package
    pkg = rest_requests.delete_work_package(id=pkg['id'])


if __name__ == '__main__':
    main()
