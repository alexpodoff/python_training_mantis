from model.project import Project
from random_generator import name_generator as ng


def test_create_project(app):
    app.session.login("administrator", "secret")
    project = Project(name=ng(10), desc=ng(30))
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    app.project.confirm()
    old_projects.append(project)
    new_contacts = app.project.get_project_list()
    assert old_projects == new_contacts

