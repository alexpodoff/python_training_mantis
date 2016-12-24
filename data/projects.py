from model.project import Project
from random_generator import name_generator as ng


testdata = [Project(name="", desc="")] + [
    Project(name=ng(10), desc=ng(20))
    for i in range(5)
]