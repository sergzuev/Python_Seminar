# Найдите сумму цифр трёхзначного числа

print('Введите трёхзначное число: ')
num = int(input())
num_sum = 0

while num:
    num_sum += num % 10
    num //= 10

print(num_sum)