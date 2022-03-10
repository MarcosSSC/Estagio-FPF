list = [1, 2, 3, 4, 5]
sumeven = 0
sumodd = 0

for i in list:
    if i % 2 == 0:
        sumeven = sumeven + i
    else:
        sumodd = sumodd + i

print(f'A soma dos pares é: {sumeven}')
print(f'A soma dos impares é: {sumodd}')