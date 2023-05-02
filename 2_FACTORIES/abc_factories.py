from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print(f'This tea is delicious')

class Coffe(HotDrink):
    def consume(self):
        print(f'This coffe is delicious')

class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water,'
              f'pour {amount} water, enjoy!')
        return Tea()

class CoffeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in coffe bag, boil water,'
              f'pour {amount} water, enjoy!')
        return Coffe()

def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffe':
        return CoffeFactory().prepare(50)
    else:
        None

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])
        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input('Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    # entry = input('What kind of the drink would you like?')
    # drink = make_drink(entry)
    # drink.consume()
    hdm = HotDrinkMachine()
    hdm.make_drink()