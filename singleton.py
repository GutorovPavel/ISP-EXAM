
#######################  Decorator  ########################


class SingletonDec:
    _instance = None

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        if self._instance is None:
            self._instance = self._cls()
            return self._instance
        return self._instance

    def __call__(self):
        raise TypeError('Singletone must be called by Instance().')


@SingletonDec
class MyClass1:
    pass


#################  Meta class  ####################


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass2(metaclass=SingletonMeta):
    pass


##################  Base class  ##################


class SingletonBase(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass3(SingletonBase):
    pass







