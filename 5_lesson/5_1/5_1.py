# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# 8
# 5 4 2 2 4 2 2 5

num = int(input())
grades = list(map(int, input().split()))
num_max = max(grades)
num_min = min(grades)

grades_change = [num_min if j == num_max else j for j in grades]
print(grades_change)
