numbers = [1, 2, 3, 4, 5, 100, 200, 500, 600]
smaller_than_100 = []

for n in numbers:
    if n < 100:
        smaller_than_100.append(n)

print(smaller_than_100)