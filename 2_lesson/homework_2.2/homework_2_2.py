# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())
stepen_two = 1

while stepen_two <= n:
    print(stepen_two, end=" ")
    stepen_two *= 2