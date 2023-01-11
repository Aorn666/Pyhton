# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.



def prime_factors(start_num: int) -> list:
    list_p_f = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result_list = []

    for i in range(len(list_p_f)):

        while start_num % list_p_f[i] == 0:
            if start_num % list_p_f[i] == 0:
                result_list.append(list_p_f[i])
                start_num /= list_p_f[i]
            else:
                continue
        
        if start_num == 1:
            break

    return result_list


num = int(input("Введите натуральное число: "))
print(prime_factors(num))