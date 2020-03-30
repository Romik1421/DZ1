#print("Hello world!")

i = int(input("Пожалуйста введите любое положительное число: "))
x = 0
while i > 10:
    d = i % 10
    i //= 10
    if d > x:
        x = d
print("Максимальное число =", x)