

class Project:

    def __init__(self, name=None, desc=None):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return '%s:%s' % (self.name, self.desc)

    def __eq__(self, other):
        return self.name == other.name and self.desc == other.desc