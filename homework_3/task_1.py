# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample


def list_rand_nums(count: int) -> list:
    if count <= 0:
        print("Число должно быть больше 0")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def sum_odd_pos(list_nums: list):
    sum_nums = 0
    for k in range(0, len(list_nums), 2):
        sum_nums += list_nums[k]
    return sum_nums


list_a = list_rand_nums(int(input("Задайте длинну списка: ")))
print(list_a)
print(sum_odd_pos(list_a))