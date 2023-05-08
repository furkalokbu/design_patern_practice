import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} leave at {self.address}'

# address = Address('123 London Road', 'Londonm', 'UK')
# John = Person('John', address)
# print(John)
# print('------')
# Jane = Person('Jane', address)
John = Person('John', Address('123 London Road', 'Londonm', 'UK'))
Jane = copy.deepcopy(John)
Jane.name = 'Jane'
Jane.address.street_address = '123B London Road'
print(John)
print(Jane)
