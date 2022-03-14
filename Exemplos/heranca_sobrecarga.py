from functools import singledispatchmethod

class Calculator:

    @singledispatchmethod
    def add(self, a, b):
        raise NotImplementedError('Aqui não vai ser implementado')

    @add.register
    def integer(self, a: int, b:int):
        print('int')
        return a+b

    @add.register
    def strings(self, a: str, b: str):
        print('str')
        return a + b

c = Calculator()
print(c.add(10, 10))
print(c.add('10', '10'))

