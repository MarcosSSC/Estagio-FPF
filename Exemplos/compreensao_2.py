from collections import namedtuple
from datetime import date

employee = namedtuple('Funcionário', ['nome', 'salário', 'sexo', 'aniversário'])

e1 = employee(nome='Marcos', salário='1600', sexo='M', aniversário=date(2000, 8, 16))
e2 = employee(nome='Lívia', salário='4000', sexo='F', aniversário=date(2001, 1, 12))
e3 = employee(nome='Guilherme', salário='13000', sexo='M', aniversário=date(1992, 1, 25))
e4 = employee(nome='Flávia', salário='10000', sexo='F', aniversário=date(1998, 9, 30))

employees = []
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)

print(employees)

print(min(e.aniversário for e in employees))