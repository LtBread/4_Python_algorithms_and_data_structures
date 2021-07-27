# 4. Написать программу, которая генерирует в указанных пользователем
#  границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся
# эти символы. Программа должна вывести на экран любой символ алфавита
# от 'a' до 'f' включительно.

import random

min, max = map(
    int, input('Введите границы диапазона для целого числа '
               '(через пробел): ').strip().split())
print('Случайное целое:', random.randint(min, max))
minf, maxf = map(
    float, input('Введите границы диапазона для целого числа '
                 '(через пробел): ').strip().split())
print(f'Случайное вещественное {random.uniform(minf, maxf):.2f}')
l_char, r_char = input(
    'Введите границы диапазона для латинской буквы '
    '(через пробел): ').strip().split()
print('Случайная буква:', chr(random.randrange(ord(l_char), ord(r_char) + 1)))
