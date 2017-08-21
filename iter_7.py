# Iteration 7

class Contract:
    # Own the "dot" (Descriptor)
    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    # Python 3.6+
    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        pass

class Typed(Contract):
    type = None
    @classmethod
    def check(cls, value):
        assert isinstance(value, cls.type), f'Expected {cls.type}'
        super().check(value)

class Integer(Typed):
    type = int

class String(Typed):
    type = str

class Positive(Contract):
    @classmethod
    def check(cls, value):
        assert value > 0, 'Must be positive'
        super().check(value)

class Nonempty(Contract):
    @classmethod
    def check(cls, value):
        assert len(value) > 0, 'Must be nonempty'
        super().check(value)

class PositiveInteger(Integer, Positive):
    pass

class NonemptyString(String, Nonempty):
    pass

class Base:
    # Python 3.6+
    @classmethod
    def __init_subclass__(cls):
        # Instantiate the contracts
        for name, val in cls.__annotations__.items():
            contract = val()
            contract.__set_name__(cls, name)
            setattr(cls, name, contract)

class Player(Base):
    name: NonemptyString
    x: Integer
    y: Integer

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def left(self, dx):
        self.x -= dx

    def right(self, dx):
        self.x += dx

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        Integer.check(value)
        self._x = value