# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
n = int(input('введите число: '))
sum = 1
list_end = []
for i in range(n):
    sum *= i+1
    list_end.append(sum)

print (list_end)