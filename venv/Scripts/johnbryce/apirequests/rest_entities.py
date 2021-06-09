class OpenProjectEntities:

    def get_project_create_body(self, project_name):
        return {
            "name": project_name,
        }
