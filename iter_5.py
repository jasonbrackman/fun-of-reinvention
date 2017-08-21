# Iteration 5

class Contract:
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

class Player:
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
