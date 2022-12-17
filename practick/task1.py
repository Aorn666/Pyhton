a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
#print('Да' if a**2==b or b**2==a else 'Нет')

if a==b**2 or b==a**2:
    print("yes")
else:
    print("no")
