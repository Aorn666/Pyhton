# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# AB = √(xb - xa)2 + (yb - ya)2

x1 = int(input("введите x1: "))
y1 = int(input("введите y1: "))
x2 = int(input("введите x2: "))
y2 = int(input("введите y2: "))
print(((x2 - x1)**2 + (y2 -y1)**2)**0.5)