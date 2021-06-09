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
    posts_requests = RestRequests(domain, api_token)

    # create project
    body = entities.get_project_create_body(CommonUtilities.get_random_string(prefix="dummy_"))
    project = posts_requests.create_project(body)

    # Get project
    project = posts_requests.get_single_project(project['id'])

    # Update project
    body = entities.get_project_update_body("This is a project description")
    project = posts_requests.update_project(project['id'], body)

    # Delete project
    project = posts_requests.delete_project(project['id'], {})

    









if __name__ == '__main__':
    main()
