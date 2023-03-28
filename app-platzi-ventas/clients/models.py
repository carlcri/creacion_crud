
class Client:

    def __init__(self, name, company, position, salary):
        self.name = name
        self.company = company
        self.position = position


    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['name', 'company', 'position', 'salary']