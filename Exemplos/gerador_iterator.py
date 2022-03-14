def counter():
    index = 0
    while True:
        yield index
        index += 1

generator = counter()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))