print(float('10'))

print(int('10'))

print(str(10))

print(bool(1))

print('Hello World')

print(len([1, 2, 3, 4, 5, 6]))

print(max([1, 2, 3, 4, 5, 6]))

print(min([1, 2, 3, 4, 5, 6]))

for index, element in enumerate([1, 2, 3, 4, 5]):
    print(f'index: {index}')
    print(f'element: {element}')

print(sum([1, 2, 3, 4, 5, 6]))

input('Digite seu nome: ')

fruits = ['maçã', 'laranja', 'pessego', 'morango']

def item_size(item: str):
    return len(item)

transformed = map(item_size, fruits)

transformed2 = map(lambda item: len(item), fruits)

print(f'transformado: {list(transformed)}')
print(f'tranformado 2: {list(transformed2)}')

numbers = [100, 200, 300, 1, 4, 2, 3, 5, 6]

orderly_list = sorted(numbers)
orderly_list_desc = sorted(numbers, reverse = True)

print(orderly_list)
print(orderly_list_desc)

def even(item):
    return item % 2 == 0

even1 = filter(even, numbers)
even2 = filter(lambda item: item % 2 == 0, numbers)

print(list(even1))
print(list(even2))