class person(object):
    def __init__(self, name = None):
        self.name = name

    def __str__(self) -> str:
        return self.name

class pj(person):
    def __init__(self, name = None, cnpj = None):
        super().__init__(name=name)
        self.cnpj = cnpj

class pf(person):
    def __init__(self, name = None, cpf = None):
        super().__init__(name=name)
        self.cpf = cpf

fpf = pj()
fpf.name = 'FPF TECH'
fpf.cnpj = '000.000.000/0001-20'
print(fpf)

marcos = pf()
marcos.name = 'Marcos Castro'
fpf.cnf = '000.000.000-00'
print(marcos)