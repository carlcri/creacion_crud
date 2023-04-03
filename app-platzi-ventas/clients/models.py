
class Client:

    def __init__(self, name, company, position, salary):
        self.name = name.capitalize()
        self.company = company.capitalize()
        self.position = position.capitalize()
        self.salary = salary


    def to_dict(self):
        return vars(self)


    @staticmethod
    def schema():
        return ['name', 'company', 'position', 'salary']