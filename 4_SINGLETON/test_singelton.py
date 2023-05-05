import unittest


class Singelton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singelton, cls)\
                .__call__(*args, **kwargs)

        return cls._instances[cls]


class Database(metaclass=Singelton):
    def __init__(self):
        self.population = {}
        f = open('/home/serhii/dev/design_patern_practice/4_SINGLETON/capitals.txt', 'r')
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()]=\
                int(lines[i+1].strip())
        f.close()

class SingeltonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result

class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]


class SingeltonTests(unittest.TestCase):
    def test_is_singelton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singelton_total_population(self):
        rf = SingeltonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(17500000+17400000, tp)

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(db=self.ddb)
        names = ['alpha', 'beta', 'gamma']
        tp = crf.total_population(names)
        self.assertEqual(6, tp)


if __name__ == '__main__':
    unittest.main()
