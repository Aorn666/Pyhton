
import random

def get_list_random_elements(length_list: int, min_el: int,
                             max_el: int) -> list:

    if length_list < 0:
        print("не то число")
        return []

    new_list = []

    for i in range(length_list):
        e = random.randint(min_el, max_el)
        new_list.append(e)
    print(new_list)
    return new_list


def unique_elements_list(start_list: list) -> list:
    un_el_list = []
    count = 0

    for i in range(len(start_list)):
        un_el_list.append(start_list[i])

        for g in range(len(start_list)):

            if un_el_list[-1] == start_list[g]:
                count += 1
            
            if count == 2:
                del un_el_list[-1]
                break

        count = 0

    return un_el_list




num = int(input("Введите натуральное число: "))
print(unique_elements_list(get_list_random_elements(num, 1, num)))
