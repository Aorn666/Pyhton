# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int (input ('Введите длину списка: '))
sum_and = 0
list_end = []
for i in range(1,n+1):
    a = round((1 + 1/i) ** i,3)
    list_end.append(a)
    sum_and += a


print (list_end)
print (sum_and)