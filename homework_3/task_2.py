# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample


def list_rand_nums(count: int) -> list:
    if count <= 0:
        print("Число должно быть больше 0")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums

def multiplication(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])
    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list

list_a = list_rand_nums(int(input("Задайте длинну списка: ")))
print(list_a)
print(multiplication(list_a))