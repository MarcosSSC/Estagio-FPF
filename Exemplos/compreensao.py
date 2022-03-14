employees= []

e1 = {'nome': 'Marcos', 'salário': 1600, 'sexo': 'M'}
e2 = {'nome': 'Lívia', 'salário': 4000, 'sexo': 'F'}
e3 = {'nome': 'Guilherme', 'salário': 13000, 'sexo': 'M'}
e4 = {'nome': 'Flávia', 'salário': 10000, 'sexo': 'F'}

employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)

male = sum([e['salário'] for e in employees if e['sexo'] == 'M'])
female = sum([e['salário'] for e in employees if e['sexo'] == 'F'])

print(male)
print(female)