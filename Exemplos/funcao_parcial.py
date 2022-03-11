from functools import partial

def compute_salary(value_hour, hours_worked, extra_hours, extra_100 = False):
    if extra_100:
        return (value_hour * hours_worked) + (value_hour * extra_hours)
    else:
        return (value_hour * hours_worked) + ((value_hour / 2) * extra_hours)

value_hour = float(input('Informe o valor da hora: '))
hours_worked = int(input('Informe as horas trabalhadas: '))
extra_hours = int(input('Informe as horas extras: '))

base_salary = partial(
    compute_salary,
    value_hour = value_hour,
    hours_worked = hours_worked,
    extra_hours = 5
)

extra_100 = base_salary(extra_100=True)
extra_50 = base_salary()

print(f'Salário com extra de 100%: {extra_100}')
print(f'Salário com extra de 50%: {extra_50}')