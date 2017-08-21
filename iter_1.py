# Iteration 1

class Contract:
    @classmethod
    def check(cls, value):
        pass

class Integer(Contract):
    @classmethod
    def check(cls, value):
        assert isinstance(value, int), 'Expected int'

class String(Contract):
    @classmethod
    def check(cls, value):
        assert isinstance(value, str), 'Expected str'

def gcd(a, b):
    Integer.check(a)
    Integer.check(b)
    while b:
        a, b = b, a % b
    return a
