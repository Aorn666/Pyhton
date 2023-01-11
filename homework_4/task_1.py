# 1. Вычислить число c заданной точностью d

from decimal import Decimal

def rez(n: str, accuracy: str) -> float:
    result = Decimal(n)
    result = result.quantize(Decimal(accuracy))

    return result

number = (input('число: '))
num = (input('точность: '))

print (rez(number,num))