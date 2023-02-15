# Задача 26
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3**5)
# A = 2; B = 3 -> 8

def stepeni(a,b):
    result = 1
    for i in range(b):
        result *=a
    return(result)

a = stepeni(2,3)
print(a)