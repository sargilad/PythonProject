class OpenProjectEntities:

    def get_project_create_body(self, project_name):
        return {
            "name": project_name,
        }

    def get_project_update_body(self, description):
        return {
            "description": {
                "raw": description
            }
        }
