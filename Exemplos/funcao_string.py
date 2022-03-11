company = 'FPF Tech'
names = ['Marcos', 'Castro']

print('tamanho')
print(len(company))

print('quantidade')
print(company.count('F'))

print('posição')
print(company.find('T'))

print('minúsculo')
print(company.lower())

print('maiúsculo')
print(company.upper())

print('separar')
print(company.split(' '))

print('capitalizar')
print(company.lower().capitalize())

print('substituir')
print(company.replace('Tech', 'Fundação'))

print('capitalizar ambos elementos')
print(company.lower().title())

print('juntar')
print(', '.join(names))