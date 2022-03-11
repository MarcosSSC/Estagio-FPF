def add(*numbers):
    counter = 0
    for n in numbers:
        counter += n
    return counter

numbers2 = range(100)

print(add(10, 20, 30))
print(add(*numbers2))

