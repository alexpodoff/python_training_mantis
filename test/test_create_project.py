from model.project import Project
from random_generator import name_generator as ng


def test_create_project(app):
    project = Project(name=ng(10), desc=ng(30))
    old_projects = app.project.get_project_list()
    old_soap_projects = app.soap.get_projects()
    app.project.create_project(project)
    app.project.confirm()
    old_projects.append(project)
    old_soap_projects.append(project)
    new_projects = app.project.get_project_list()
    new_soap_projects = app.soap.get_projects()
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
    assert sorted(old_soap_projects, key=lambda p: p.name) == sorted(new_soap_projects, key=lambda p: p.name)
