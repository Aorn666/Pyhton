# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


num = int(input('Введите число : '))
a, b = 1, 1

list_nums = [0]

for i in range(num):
    list_nums.append(a)
    list_nums.insert(0, a * (-1) ** i)
    a, b = b, b + a

print(*list_nums)