#Подключаем модуль для работы со случайными числами
import random


#Создаем переменную n
n = None


#Вводим число n
while n == None:
    try:
        n = int(input("Введите число n: "))
        if n < 0:
            print("Вы ввели отрицательное число n. Попробуйте ещё раз")
            n = None
    except ValueError:
        print("Вы ввели не целое положительное число или вообще не число. Попробуйте ещё раз")


#Заполняем кортежи десятью случайными числами
first = tuple([random.randint(0, n) for _ in range(10)])
second = tuple([random.randint(-1 * n, 0) for _ in range(10)])


#Создаем третий кортеж, объединив два предыдущих
third = first + second


#Выводим третий кортеж и кол-во нулей в нём
print(third)
if third.count(0) % 10 == 1 and third.count(0) != 11:
    print("В третьем кортеже", third.count(0), "нуль")
elif (third.count(0) % 10 == 2 or third.count(0) % 10 == 3 or third.count(0) % 10 == 4) and (third.count(0) < 10 or third.count(0) > 20):
    print("В третьем кортеже", third.count(0), "нуля")
else:
    print("В третьем кортеже", third.count(0), "нулей")