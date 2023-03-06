# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
#
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# https://www.delftstack.com/ru/howto/python/python-isprime/

def prime_num(num):
    if num == 2 or num == 3:
         return True
    if num % 2 == 0 or num < 2:
         return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


print(prime_num(int(input())))
