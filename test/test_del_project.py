from model.project import Project
import random


def test_del_project(app):
    if app.project.get_project_list() == 0:
        app.project.create_project(Project(name="test"))
        app.project.confirm()
    old_projects = app.project.get_project_list()
    old_soap_projects = app.soap.get_projects()
    project = random.choice(old_projects)
    app.project.delete_project(project.name)
    new_projects = app.project.get_project_list()
    new_soap_projects = app.soap.get_projects()
    old_soap_projects.remove(project)
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
    assert sorted(old_soap_projects, key=lambda p: p.name) == sorted(new_soap_projects, key=lambda p: p.name)


