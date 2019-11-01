generator = (i ** 2 for i in range(0, 100)if i % 2 == 0)
print("------------------------")
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print("------------------------")
for numero in generator:
    print(numero)