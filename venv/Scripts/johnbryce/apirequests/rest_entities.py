class OpenProjectEntities:

    def get_project_create_body(self, project_name) -> dict:
        return {
            "name": project_name,
        }

    def get_project_update_body(self, description) -> dict:
        return {
            "description": {
                "raw": description
            }
        }

    def get_create_work_package_body(self, pkg_name: str, project_ref: str, pkg_type: str) -> dict:
        return {
            "subject": pkg_name,
            "percentageDone": 0,
            "_links": {
                "type": {
                    "href": pkg_type
                },
                "project": {
                    "href": project_ref
                }
            }
        }

    def get_work_package_update_body(self, lock_version: int, description: str = "This is a description") -> dict:
        return {
            "lockVersion": lock_version,
            "_links": {},
            "description": {
                "raw": description
            }
        }
