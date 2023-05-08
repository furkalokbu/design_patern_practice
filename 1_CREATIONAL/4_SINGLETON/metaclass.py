


class Singelton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singelton, cls)\
                .__call__(*args, **kwargs)
        
        return cls._instance[cls]


class Database(metaclass=Singelton):
    def __init__(self):
        print('Database create')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1 == d2)
