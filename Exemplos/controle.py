age = int(input('Digite sua idade: '))

if age >= 18:
    print('Adulto')
elif age >= 12 and age < 18:
    print('Adolescente')
else:
    print('Criança')