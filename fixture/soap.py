

from suds.client import Client
from suds import WebFault
from fixture.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app


    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.3.4/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects(self):
        client = Client("http://localhost/mantisbt-1.3.4/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible("administrator", "secret")
        project_list = []
        for project in projects:
            name = project.name
            desc = project.description
            project_list.append(Project(name=name, desc=desc))
        return project_list
