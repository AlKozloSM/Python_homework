# -*- coding: utf-8 -*-
__author__= 'Kozlov Aleksandr Anatiolevich'

#Level: hard
# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

"""Как вариант только бесконечность, но бесконечность не является числом"""

number = float('inf')
if number == number ** 2 and number == number * 2 and number > 999999:
    print(True)
else:
    print(False)