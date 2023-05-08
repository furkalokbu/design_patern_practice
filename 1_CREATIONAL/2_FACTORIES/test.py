class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    id = 0
    def create_person(self, name):
        person = Person(self.id, name)
        self.id += 1
        return person


pf = PersonFactory()
p1 = pf.create_person('Serhii')
p2 = pf.create_person('Ivan')
print(f'{p1.id}: {p1.name}')
print(f'{p2.id}: {p2.name}')