# Iteration 2

class Contract:
    @classmethod
    def check(cls, value):
        pass

class Typed(Contract):
    type = None
    @classmethod
    def check(cls, value):
        assert isinstance(value, cls.type), f'Expected {cls.type}'

class Integer(Typed):
    type = int

class String(Typed):
    type = str

class Positive(Contract):
    @classmethod
    def check(cls, value):
        assert value > 0, 'Must be positive'

class Nonempty(Contract):
    @classmethod
    def check(cls, value):
        assert len(value) > 0, 'Must be nonempty'

def gcd(a, b):
    Integer.check(a)
    Positive.check(a)
    Integer.check(b)
    Positive.check(b)
    while b:
        a, b = b, a % b
    return a
