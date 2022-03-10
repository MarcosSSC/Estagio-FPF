employees = 4
men_salary = 0
women_salary = 0

for i in range(employees):
    name = str(input('nome: '))
    sex = str(input('sexo: '))
    salary = float(input('salario: '))

    if sex == 'masculino':
        men_salary = men_salary + salary

    else:
        women_salary = women_salary + salary

print(f'Salário dos homens é {men_salary} e das mulheres é {women_salary}')