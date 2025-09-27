# name = "admin"
# age = 20
# print(name, type(name))
# print(age, type(age))
# print(name + str(age))
# from operator import index
# import json
# a = 4  # комментарий
# b = 5
# print("a =", a, id(a))
# print("b =", b, id(b))
# a = b
# print("a =", a, id(a))
# print("b =", b, id(b))

# # a = b = c = 5
# a, b, c = 5, "Hello", 9.2
# # print(a)
# # print(b)
# # print(c)
# print(a, b, c)

# first_name = "admin"
# print(first_name)

# import keyword
#
# print(keyword.kwlist)

# PI = 3.14
# print(PI)

# a = 7
# b = 15
# print("a:", a)
# print("b:", b)
#
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# a, b = b, a
#
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка символов \nстрока символов строка символов строка символов строка символов строка символов строка '
#       'символов строка символов строка символов строка символов')

# print("\tДокумент \"file.py\" находится \tпо     пути: \rD:\\folder\\file.py")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3)
# print(s3 * 3)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 ** 2)
# print(6 / 2)
# print(7 // 2)
# print(7 % 2)

# a, b, c = 5, 7, 3
# res = a + b + c
# print("Сумма:", res)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", res / 3)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3
# print(num)  # 12
#
# num *= 4
# print(num)  # 48

# num = 9753  # 43
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)


# num = 4321  # 43
# print("Исходное число:", num)
# res = num % 10 * 1000  # 1000
# num //= 10  # num = num // 10
# res += num % 10 * 100  # 200
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Обратное число:", res)


# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)

# print(int(2.987))
# print(round(2.587, 2))

# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2
# print(res)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", end="\n\n", sep="")
# print("Новая строка")

# name = input("Ваше имя: ")
# print("Hello,", name)

# num = int(input("Введите число: "))  # num = 5
# power = int(input("Введите степень: "))
# # print(num, type(num))
# # print(power, type(power))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# b1 = True
# b2 = False
# # print(b1, type(b1))
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# print(bool("python"))
# print(bool(" "))
# print(bool(""))
# print(bool(5))
# print(bool(-5))
# print(bool(0))
# print(bool(0.1))
# print(bool(0.0))
# print(bool(True))
# print(bool(False))
# print(bool(None))

# test = None
# print(test, type(test))
# test = 5
# print(test, type(test))

# print(7 == 7)
# print(2 + 5 == 7 + 3)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 >= 8)
# print(8 < 5)
# print(8 <= 8)
#
# print("hellor" > "H{ello")  # 104 > 72

# print(2 < 4 < 9)  # True && True  -> True
# print(2 * 5 > 7 >= 4 + 3)  # True && True -> True
# print(3 * 3 <= 7 >= 2)  # False && True -> False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True : False => False
# print(5 - 3 > 2 and 1 + 3 == 4)  # False : True => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False : False => False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True : False => True
# print(5 - 3 > 2 or 1 + 3 == 4)  # False : True => True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False : False => False


# print(not 9 - 7)  # not True -> False
# print(not 7 - 7)  # not False -> True

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
#     print("Добро пожаловать")
#     # pass
# else:
#     print("Доступ запрещен")
#     # ...


# import this
# print(this)

# a = 5
# b = 5
#
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("a == b")

# a = input("Введите первую строну: ")
# b = input("Введите вторую строну: ")
# c = input("Введите третью строну: ")
#
# if a == b == c:  # '10' == '10' == '10'
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)  # 1 <= 2 <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# time = int(input('Введите номер месяца: '))
# if 1 <= time <= 2:
#     print('Зима')
# elif time == 12:
#     print('Зима')
# elif 3 <= time <= 5:
#     print('Весна')
# elif 6 <= time <= 8:
#     print('Лето')
# elif 9 <= time <= 11:
#     print('Осень')
# else:
#     print('Такого месяца не существует')

# time = int(input('Введите номер месяца: '))
# if time == 1 or time == 2 or time == 12:
#     print('Зима')
# elif 3 <= time <= 5:
#     print('Весна')
# elif 6 <= time <= 8:
#     print('Лето')
# elif 9 <= time <= 11:
#     print('Осень')
# else:
#     print('Такого месяца не существует')


# month = int(input("Введите номер месяца (цифрой): "))
# if 1 <= month <= 12:
#     print("Время года данного месяца - ", end="")
#     if 1 <= month <= 2 or month == 12:
#         print("зима")
#     if 3 <= month <= 5:
#         print("весна")
#     if 6 <= month <= 8:
#         print("лето")
#     if 9 <= month <= 11:
#         print("осень")
# else:
#     print("Неверно указан номер месяца")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# password = 'qwerty'
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")

# day = "вторник"
# time = 15
#
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# Тернарное выражения

# a, b = 30, 20
# print(a if a < b else b)


# a, b = 20, 30
# print("a == b" if a == b else "a > b" if a > b else "a < b")


# Исключения

# a = 0
# b = "2a2"
# print(a + int(b))

# a = 5
# b = 0
# print(a / b)

# try:  # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
#
# # n = int(input("Введите целое число: "))
# # print(n * 2)
# print("Код ниже")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = float(input("Введите делимое: "))
#     m = float(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)

# n = input("Введите первое число: ")  # '2'
# m = input("Введите второе число: ")  # 'пять'
#
# try:
#     n = int(n)  #
#     m = int(m)
# except ValueError:
#     n = str(n)  #
# finally:
#     print(n + m)

# Цикл while

# i = 0  # переменная счетчик
# while i < 5:  # условие
#     print("i =", i)
#     i += 1  # i = i + 1  # изменение счетчика

# Итерация - один шаг цикла

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
#
# print()
# i = 1
# while i <= 20:
#     print(i + 1, end=" ")
#     i += 2

# n = int(input("Введите количество символов: "))
# print("+-" * n)
#
# # i = 0
# # while i < n:
# #     if i % 2 == 0:
# #         print("+", end="")
# #     else:
# #         print("-", end="")
# #     i += 1
#
# while n > 0:
#     if n % 2:
#         print("+", end="")
#     else:
#         print("-", end="")
#     n -= 1


# a = int(input("Введите начало диапазона: "))  # 1
# b = int(input("Введите конец диапазона: "))  # 5
# res = 0
# while a <= b:
#     if a % 2:  # a % 2 == 1  a % 2 != 0
#         print(a, end=" ")
#         res += a
#     a += 1
#
# print("Сумма целых нечетных элементов:", res)

# n = input("Введите целое число: ")
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
#
# print("Результат:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)
#
# i = 1
#
# while i < 5:  # 5
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:  # 1
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^ ", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:  # 5
#     j = 0  # 0
#     while j < i:  # 0 < 4
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0  # 5
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1

# print()
# print("*" * 0)

# for element in collection:
#     print(element)

# for i in "Hello", "World":
#     print(i)

# range(start, stop, step)  #  start=0, step=1
# print(range(1, 9, 2))
#
# for i in range(10):  # for(let i = 0; i < 10; i++)
#     print(i, end=" ")
#
# print()
#
# i = 2
# while i < 10:
#     print(i, end=" ")
#     i += 3


# ch = int(input("Введите целое число: "))
# for i in range(1, ch + 1):  # 1 2 3 4 5
#     if ch % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=" ")
# print()
#
# for i in range(10, 100):  # 15 => 1
#     if i % 10 == i // 10:
#         print(i, end=" ")


# for i in range(3):
#     if i == 1:
#         continue
#     print(i)
# else:
#     print("Конец цикла")

# for i in range(3):  # 0 1 2
#     print("+++")
#     for j in range(2):  # 0 1
#         print("-----")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# st = [i * 2 for i in "Hello"]
# print(st)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Список (list)

# num = [14, 16, 18, 20, 22, 24, 26, 28, "Hello", True, 2.8]
# print(num)
# # print(type(num))
# # print(num[0])
# # print(num[-3])
# # num[0] = 256
# # print(num)
# # num[1] += 100
# # print(num)
# print(len(num))
# print(num[-1])
# print(num[11])

# s = []
# print(s, type(s))
#
# s2 = list("Hello")
# print(s2, type(s2))

# s1 = [1, 2, 3]
# s2 = [4, 5, 6]
# s3 = s1 + s2
# print(s3)
# print(s3 * 2)

# n = list(range(10))
# print(n)
# n = list(range(2, 10))
# print(n)
# n = list(range(10, 2, -2))
# print(n)


# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)  # [0, 0, 0, 0, 0]
#
# n = 5
# a = [i for i in range(n + 1)]
# print(a)  # [0, 1, 2, 3, 4]

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("n: ")))]
# print(a)

# lst = [5, 9, 8, 2, 3]
#
# for i in range(len(lst)):  # 0 1 2 3 4
#     print(lst[i], end=" ")
#
# print()
#
# for i in lst:  # 5 9 8 2 3
#     print(i, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных элементов:", s)


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# s = 0
# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов:", s)

# n = list(range(21, 41))
# print(n)
# s = 0
# k = 0
# for i in range(len(n)):
#     if n[i] % 2:
#         s += n[i]
#     else:
#         k += 1
#
# print("Количество четных элементов:", k)
# print("Сумма нечетных элементов:", s)

# n = list(range(21, 41))
# print(n)
# s = 0
# k = 0
# for i in n:
#     if i % 2:
#         s += i
#     else:
#         k += 1
#
# print("Количество четных элементов:", k)
# print("Сумма нечетных элементов:", s)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in a:
#     if i % 2 == 0:
#         print(i, end=" ")

# lst = [9, 8, 7, 4, 6, 2]
# print(lst[1])
# print(lst[0])


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# j = a[0]  #
# for i in a:  # [3, 7, 4, 6, 2]
#     if i > j:  # 4 > 7
#         print(i, end=" ")
#     j = i  # 7

# Срез
# Список[start:stop:step] , start=0, stop=len(), step=1
# lst = [3, 7, 4, 6, 2]
# print(lst[1:3])
# print(lst[1:])
# print(lst[:4])
# print(lst[::-1])
# print(lst[3:1:-1])
# print(lst[10:20])

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[0:1])
# print(lst[6:])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "HelloWorld"
# print(st[1:5])
# print(st[::-1])


# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2] = 120
# print(s)
# s[100:] = [200]
# print(s)
# print(len(s))

# print(dir(list))

# Методы списков
# s = [5, 20, 120, 200]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список в конец списка
# print(s)
# s.insert(2, 100)  # добавляет элемент в список по заданному индексу
# print(s)
#
# lst = []  # [3, 1, 7, 8, 9]
# n = int(input("Кол-во элементов списка: "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     lst.insert(0, x)
# print(lst)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 7, 3, 2]
# c = []  # [2, 1, 4, 3]
#
# for i in a:  # 2
#     for j in b:  # 2
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 7, 3, 2]
# c = []  # [2, 1, 4, 3]
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
#
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):  # 0 1 2 3 4
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0 1 2 3 4
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
#
# print(c)

# s = [5, 20, 120, 200, 120]
# print(s)
# s[1:3] = []
# del s[0]
# del s[1:3]
# s.remove(120)  # удаляет (первое вхождение) элемент из списка по значению
# num = 5
# if num in s:
#     s.remove(num)
# s.pop()  # удаляет последний элемент из списка
# ind = 3
# try:
#     num = s.pop(ind)  # удаляет элемент по заданном индексу
#     print(num)
# except IndexError:
#     print(ind, "- такого индекса не существует")
# s.clear()
# print(s)

# print("Введите элементы списка:")
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# try:
#     a.pop(k)
# except IndexError:
#     print("Элемент удалить не удалось.", k, "- такого индекса не существует")
# print(a)

# s = [5, 20, 120, 200, 120]
# print(s)
#
# num = s.count(20)  # кол-во заданных значений в списке
# print(num)
#
# ind = s.index(120, 3)  # вернет индекс первого вхождения заданного значения
# print(ind)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
#
# a.append(20)
# print("a =", a)
# print("b =", b)
#
# b.append(200)
# print("a =", a)
# print("b =", b)


# b = [51, 32, 3, 200]
# print(b)
# # b.reverse()
# b.sort(reverse=True)  #
# print(b)
#
# # s = ["Виталий", "Сергей", "Александр", "Анна"]
# # print(s)
# # s.sort(reverse=True, key=len)
# # print(s)
# print()
# c = [51, 32, 3, 200]
# print(c)
# lst = sorted(c, reverse=True)
# print(c)
# print(lst)

# Генерация случайных данных

# import random

# print(dir(random))

# print(random.random())
# print(random.randint(0, 9))
# print(random.randrange(2, 9, 2))
# print(round(random.uniform(10.5, 25.5), 2))

# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 16]
# print(random.choice(city))
# print(random.choice(s))
#
# print(random.choices(city, k=3))
# print(random.choices(s, k=3))
#
# random.shuffle(city)
# print(city)
# random.shuffle(s)
# print(s)

# import random
#
# mas = [random.randint(20, 40) for i in range(10)]
# print(mas)


# lst = [34, 32, 20, 38, 35, 36, 33, 29, 32, 40]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
#
# lst = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))

# import random

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# max_1 = max(lst)
# print("MAX =", max_1)
# lst.remove(max_1)
# lst.insert(0, max_1)
# print(lst)


# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# min_1 = min(lst)
# print("MIN =", min_1)
#
# ind = lst.index(min_1)
# print("INDEX =", ind)
#
# del lst[0:ind]
# print(lst)
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список:", c)

# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
#
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Третий список:", c)


# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
#
# print("Третий список:", c)

# c = [min(a), min(b), max(a), max(b)]
# print("Третий список:", c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# # print(m[2][2])
# #
# # st = ["Hello", "World"]
# # print(st[1][4])
# print("Вариант 1")
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
#
# print("Вариант 2")
# for i in m:
#     for j in i:
#         print(j, end="\t\t")
#     print()


# Modules

# import geometry
#
# num1 = geometry.sqrt(2)
# num2 = geometry.ceil(3.2)
# num3 = geometry.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# import geometry as m
#
# num1 = m.sqrt(2)
# num2 = m.ceil(3.2)
# num3 = m.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from geometry import sqrt, ceil, floor
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from geometry import *
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from geometry import pi
#
# # print(pi)
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * radius, 2))


# import time
# import locale

# print(time.time())
# print(time.ctime(5426405591))
# print(time.localtime())
# res = time.localtime()
# print(res.tm_year)
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(5426405591)))
# print(time.strftime("Today is %B %d, %Y."))
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y."))

# pause = 1.5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "seconds")

# start = time.time()
# time.sleep(5)
# finish = time.time() - start
# print(finish)


# Function

# def hello(name, age):
#     print("Меня зовут:", name, "Мне", age, "лет")
#
#
# hello("Irina", 20)
# hello(18, "Ivan")

# def get_sum(a, b):
#     print("Сумма чисел: ", end="")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def test(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(test(10, 5))
# # print(test(5, 10))
# num1 = 10
# num2 = 15
# if test(num1, num2):
#     print(num1, ">", num2)
# else:
#     print(num1, "<", num2)


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_number = False
#     has_special = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_number = True
#         if "!" or "@" or "%":
#             has_special = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_number and has_special:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2, c=3))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)  # True
# print(a is b)  # True
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False


# lt1 = [1, 2, 3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))
# lt1.pop(1)
# print(lt1, id(lt1))

# s = "Hello"
# print(s, id(s))
# # s = s + "!"
# s += "!"  # s = s + "!"
# print(s, id(s))

# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

# def test(lst):
#     lst.append(4)
#
#
# x = [1, 2, 3]
# print(test(x))
# print(x)
#
#
# def test1(n):
#     n = 5
#
#
# x1 = 3
# print(test1(x1))
# print(x1)

# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# print(lst[1])
# print(tpl[1])
#
# lst[1] = 50

# a = ()
# print(a, type(a))
#
# b = tuple("Hello")
# print(b, type(b))


# a = (1, 2, 3, 4, 5, 6)
# print(a, type(a))
# print(a[2])
# print(a[1:4])


# s = tuple(int(input("-> ")) for i in range(5))
# print(s)

# from random import randint
#
# s = tuple(randint(50, 100) for i in range(5))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# # print(t1)
# # print(t2)
# t3 = t1 + t2
# print(t3)


# print(t3 * 3)
# print(t3.count("l"))
# # print(t3.count("a"))
# # if 'a' in t3:
# #     print(t3.index("a"))
# # else:
# #     print("Такого символа нет")
# print(t3.index("l", 4))

# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))


# point = 10
#
# match point:
#     case (0, 0):
#         print("Точка находится в координате 0:0")
#     case (x, y):
#         print("Точка находится в", x, "по оси X и в", y, "координат по оси Y")
#     case (x, 0):
#         print("Точка находится в", x, "по оси X и в 0 координат по оси Y")
#     case (0, y):
#         print("Точка находится в 0 по оси X и в", y, "координат по оси Y")
#     case _:
#         print("Это не координаты точки")

# t = (10, "Python", (1, 2, 3), [4, 5, 6], ["hello", "world"])
# print(t)
# t[4][0] = "new"
# print(t)
# t[4].append("hi")
# print(t)

# Распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # Распаковка кортежа
# # x, y, z = 1, 2, 3
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)


# t = (1, 2, 3)
# del t
# print(t)

# t = (1, 2, 3, 4, 5)
# print(t, type(t))
# lst = list(t)
# print(lst, type(lst))
# lst.append(6)
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for county in countries:
#     country_name, county_population, cities = county
#     print("\nСтрана: ", country_name, ", население = ", county_population,  sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population,  sep="")


# s = input("Введите по порядку, без пробелов элементы кортежа: ")
# tpl = tuple(s)
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))

# Множество (set)

# s = {"one", "two", "three", "two", "three"}
# print(s)
# # print(len(s))
# for i in s:
#     print(i)

# a = {}  # dict
# print(a, type(a))

# b = set("Hello")
# print(b, type(b))
# s = list(b)
# print(s)

# s = {x * x for x in range(10)}
# s = {input("-> ") for x in range(10)}
# print(s)


# s = {"one", "two", "three"}
# print("two" in s)
# print("four" in s)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if 'a' in i])
# # print(tuple(i for i in lst if 'a' in i))
# # print({i for i in lst if 'a' in i})
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst])
# # print(tuple('A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst))
# # print({'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst})
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'])
# print(tuple('A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'))
# print({'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'})


# for i in lst:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])


# s = {"one", "two", "three"}
# s.add("four")  # добавляет элемент в множество
# print(s)
# # s.remove("four")  # KeyError
# # print(s)
#
# # el = "two"
# # if el in s:
# #     s.remove(el)  # удаляет элемент по значению, может выбрасываться исключение KeyError
# #
# # print(s)
# # s.discard("five")  # удаляет элемент по значению,
# # # исключение не выбрасывается при отсутствии элемента
# # print(s)
#
# # el = s.pop()  # удаляет один элемент из множества
# # print(s)
# # print(el)
# s.clear()  # очищает множество
# print(s)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # print(c)
# # c = a & b
# # print(c)
# # c = a - b
# # print(c)
# c = a ^ b
# print(c)
# # a |= b
# # print(a)
# # a &= b
# # print(a)
# # a -= b
# # print(a)
# a ^= b
# print(a)

# s1 = "Hello"
# s2 = "How are you"
# s3 = set(s1) & set(s2)
# print(s3)
# for i in s3:
#     print(i, end=" ")


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)
# print(a <= b)

# a = {3, 4, 0, 1, 2}
# print(a, type(a))
# lst = list(a)
# print(lst, type(lst))
# # lst = tuple(a)
# # print(lst, type(lst))
# b = set(lst)
# print(b, type(b))


# s = frozenset("hello")
# print(s)
#
# s = frozenset({"hello", "world"})
# print(s)
#
# a = frozenset({i ** 2 for i in range(10)})
# print(a)

# Словарь (dict)

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(lst, type(lst))
# print(d, type(d))
# print(lst[1])
# print(d["two"])
# d["two"] = 200
# print(d, type(d))


# d = {"one": 1, "two": 2}
# print(d, type(d))
#
# d1 = dict(one=1, two=2)
# print(d1, type(d1))


# def func(one, two):
#     return one, two
#
#
# print(func(two=1, one=2))

# lst = [["one", 1], ["two", 2], ["three", 3]]
#
# print(lst)
# print(dict(lst))

# d = {0: "text", True: 1, (1, 2): "кортеж", "список": [5, 6, 7], 1: 10, False: [5, 6, 7]}
# print(d)
# print(d["список"][1])
# print(d[(1, 2)])
# print(d[0][0])

# d = {i * 2: i ** 2 for i in range(7)}
# print(d)

# d = {input("-> "): input("-> ") for i in range(7)}
# print(d)

# from random import randint
#
# d = {randint(1, 10): randint(50, 100) for i in range(7)}
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# # print("one" in d)
# # print(2 in d)
# key = "two"
# try:
#     print(d[key])
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# del d["two1"]
# print(d)

# for key in d:
#     print(key, d[key])

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# q = int(input("Какой элемент исключить: "))
# del d[q]
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# print(len(d))

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core i5-4570K", 3, 8500],
#     "3": ["AMD FX-6300", 4, 3700],
#     "4": ["Pentium G3220", 5, 2100],
#     "5": ["Core i5-3450", 6, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     while True:
#                         if count > 0:
#                             goods[n][1] += count
#                             break
#                         else:
#                             print("Количество должно быть положительным числом")
#                             count = int(input("Количество: "))
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")


# print(dir(dict))

# d = {"one": 1, "two": 2, "three": 3}

# print(d.keys())
# print(d.values())
# print(d.items())
#
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))
#
# for i in d:
#     print(i, end=" ")
# print()
# for i in d.keys():
#     print(i, end=" ")
# print()
# for i in d.values():
#     print(i, end=" ")
# print()
# for i in d.items():
#     print(i, end=" ")
# print()
# for i, j in d.items():
#     print(i, ":", j)


# d = {"one": 1, "two": 2, "three": 3}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d2["two"] = 200
# print("D =", d)
# print("D2 =", d2)
# d["four"] = 4
# print("D =", d)
# print("D2 =", d2)


# d = {"one": 1, "two": 2, "three": 3}
# print(d["three"])  # KeyError
# value = d.get("three2", "Такого элемента в словаре нет")
# value = d.pop("two", "Такого ключа не существует")
# item = d.popitem()
# print(item)
# d.clear()
# item = d.setdefault("four", 4)
# item = d.setdefault("two1", 4)
# print(item)
# print(d)
# # d2 = {"four": 4, "five": 5, "two": 22}
# d2 = [("four", 4), ("five", 5), ("two", 22)]
# print(d2)
# # d3 = d | d2
# # print(d3)
#
# d.update(d2)
# print(d)


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
#
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
#
# print(d)
# print(new_d)


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# print(d)
# d["location"] = d.pop("city")
# print(d)

# s = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
#
# print(s)
#
# for x in s:
#     print(x)
#     for y in s[x]:
#         print("\t", y, ": ", s[x][y], sep="")
# print()
#
# for x, y in s.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ": ", j, sep="")

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({key: value for key, value in d.items()})
# print({value: key for key, value in d.items()})
# print({key: value for key, value in d.items() if value <= 2})

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print(list(d))
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()  # {"one": [1, 2, 3], }
# s = None
#
# for i in a:
#     if type(i) is str:  # type(i) == str
#         d[i] = []
#         s = i  # "two"
#     else:
#         d[s].append(i)
#
#
# print(d)


# zip()

# a = ["Декабрь", "Январь", "Февраль", "Март"]
# b = [12, 1, 2, 3]
# c = [1.0, 2.0, 3.0]
# print(dict(zip(b, a)))
# print(list(zip(a, b)))
# print(tuple(zip(a, b, c)))
# # print(list(zip(a)))

# month = [('Декабрь', 12), ('Январь', 1), ('Февраль', 2), ('Март', 3)]
# a, b = zip(*month)
# print(a)
# print(b)


# one = {"name": "Irina", "surname": "Petrova", "job": "Consultant"}
# # two = {"name": "Igor", "surname": "Vetrov", "job": "Manager"}
# #
# # for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
# #     print(k1, "->", v1)
# #     print(k2, "->", v2)
#
# print(sorted(one.items()))

# letters = ['b', 'a', 'c', 'd']
# numbers = [3, 4, 1, 2]
#
# lst = list(zip(letters, numbers))
# print(lst)
# lst.sort()
# print(lst)
# print(dict(lst))
#
# lst1 = list(zip(numbers, letters))
# print(lst1)
# lst1.sort()
# print(lst1)
# print(dict(lst1))
# print({v: k for k, v in lst1})

# a = [1, 2, 3]
# # b = [*a, 4, 5, 6]
# # print(b)
# print(*a)
# # print(type(*a))
#
# one = {"one": 1, "two": 2}
# two = {"three": 3, "four": 4, "two": 22}
# print({**one, **two})  # {"one": 1, "two": 2, "three": 3, "four": 4}

# a = ["Январь", "Февраль", "Март"]
# i = 1
# for value in a:
#     print(i, ") ", value, sep="")
#     i += 1
# print()
# for i, value in enumerate(a, start=1):
#     print(i, ") ", value, sep="")


# one = {"name": "Irina", "surname": "Petrova", "job": "Consultant"}
#
# for i, (k, v) in enumerate(one.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
# print(summa(7, 8, 9, 10))

# def search(*args):
#     average = sum(args) / len(args)
#     print(average)
#
#     res = []
#     for num in args:
#         if num < average:
#             res.append(num)
#     return res
#
#
# print(search(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(search(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(5, 1, 2, 3, 4))


# def print_scors(student, *scores):
#     print("Student Name:", student, end=". Score: ")
#     for score in scores:
#         print(score, end=", ")
#     print()
#
#
# print_scors("Irina", 100, 95, 88, 92, 99)
# print_scors("Igor", 96, 20, 33, 56)
# print_scors("Nikita")


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(one="один"))

# def info(**data):
#     for k, v in data.items():
#         print(k, ": ", v, sep="")
#     print("\n")
#
#
# info(name="Irina", surname="Vertova", age=22, phone="22-33-44")
# info(name="Igor", age=25, phone="99-88-77", email="igor@mail.ru")


# def func(a, b, *args, m=100, n=10, **kwargs):
#     print(args[0])
#     print(kwargs['c'])
#     return a, b, args, kwargs, m, n
#
#
# print(func(5, 1, 2, 3, 4, 5, 6, n=20, c=47, m=200, d=54, e=79))


# Области видимости (scope)

# name = "Tom"  # глобальная переменная
#
#
# def hi():
#     global name
#     name = "Same"
#     surname = "Jonson"  # локальные переменные
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# print1 = 5
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lst))

# def add(a):
#     x = 2
#
#     def inner():
#         print("x =", x)
#         return a + x
#
#     return inner()
#
#
# print(add(3))
# print(inner())


# def outer(who):
#     def inner():
#         print("Hello", who)
#     inner()
#
#
# outer("World")


# def outer():
#     a = 6  # 2
#
#     def inner(b):
#         a = 4  # 5
#         print("Сумма:", a + b)  # 6
#
#     print("a =", a)  # 3
#     inner(5)  # 4
#
#
# outer()  # 1


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# c = x + t  # 25 + 30 => 55  # 25 + 35 => 60
# print(c)

# x = 5


# def fn1():
#     x = 25  # 55
#
#     def fn2():
#         x = 33  # 55
#         d = x
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)  # 33
#         print("d", d)
#
#     fn2()
#     print("fn1.x =", x)  # 25
#
#
# fn1()
# print(x)


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# def func1():
#     a = 1
#     b = "line"  # line!
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         print(a)
#         # a = 5
#         a = a + 1
#         # b = b + "!"
#         return a, b, c
#
#     return func2()
#
#
# print(func1())


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# p1 = outer(5)
# print(p1(10))
# print(p1(11))
#
# p2 = outer(6)
# print(p2(4))
#
# print(outer(5)(4))


# def func(city):
#     count = 0  # 5  # 3
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res2()
#
# res1()
# res1()

# def func(x, y):
#     res = x + y
#     return res
#
#
# print(func(3, 4))
#
# # Анонимные функции (Lambda-выражения)
#
# print((lambda x, y: x + y)(1, 2))
#
# fn = lambda x, y: x + y
# print(fn(5, 6))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))


# print((lambda a, b, c: a + b + c)(1, 2, 3))
# print((lambda a, b, c=3: a + b + c)(1, 2))
# print((lambda a, b, c=3: a + b + c)(b=1, a=2))
#
# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6))


# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
#
# for t in c:
#     print(t("abc__"))

#
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(5)
# print(f(10))
#
#
# outer = lambda n: lambda x: n + x
# f = outer(5)
# print(f(10))
#
#
# print((lambda n: lambda x: n + x)(5)(10))

# def sort_list(i):
#     return i[1]
#
#
# d = {'b': 3, 'c': 1, 'a': 2}
# print(d)
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=sort_list)
# print(lst)
# print(dict(lst))

# players = [
#     {"name": "Антон", "last name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last name": "Бодня", "rating": 10},
#     {"name": "Федор", "last name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last name": "Семенов", "rating": 6}
# ]
#
# print(sorted(players, key=lambda item: item["last name"]))
# print(sorted(players, key=lambda item: item["rating"], reverse=True))
# print(sorted(players, key=lambda item: item["rating"]))


# lst = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(lst[0](10, 5))
# print(lst[2](10, 5))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[7]()

# print((lambda a, b: a if a > b else b)(15, 7))

# map(func, *iterable), filter(func, *iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))

# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))


# t = (2.88, -1.75, 100.55)
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# val = [2.0, 5.4, 7.8, 9.4, 7.4]
# print(list(map(lambda x, y, z: (x, y, z), st, num, val)))
# print(dict(map(lambda x, y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# # [5, 7, 9]
#
# new_list = list(map(lambda x, y: x + y, l1, l2))
# print(new_list)

# t = ("abcd", "abc", "adefg", "def", "ghi")
#
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# t2 = tuple(filter(lambda s: len(s), t))
# print(t2)

# b = [66, 99, 68, 59, 76, 60, 88, 74, 81, 68]
# # res = list(filter(lambda s: s > 75, b))
# res = list(filter(lambda s: s > sum(b) / len(b), b))
# print(res)

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
#
# print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(filter(lambda x: x % 2, range(1, 10))))  # [1, 3, 5, 7, 9]
# print(list(map(lambda x: x ** 2, [1, 3, 5, 7, 9])))  # [1, 9, 25, 49, 81]
#
# print([x ** 2 for x in range(1, 10) if x % 2])

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(type(test))
# print(test())


# def my_decorator(func):
#     def inner():
#         print("Код до вызова функции")
#         func()
#         print("Код после вызова функции")
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print("Код до вызова функции")
#         func()
#         print("Код после вызова функции")
#     return inner
#
#
# @my_decorator   # декоратор
# def func_test():  # декорируемая функции
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# print()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# @cnt
# def world():
#     print("World")
#
#
# hello()
# hello()
# hello()
# world()
# world()
# hello()

# def outer(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


# def outer(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @outer
# def print_students(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_students("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_students("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(arg):
#     def outer(fn):
#         def inner(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#         return inner
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:  # !=
#                     raise TypeError("Некорректный тип данных")
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) is not kwargs[k]:
#                     raise TypeError("Некорректный тип данных для именованного параметра")
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Hello"))
# print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World", z=5))
# print(typed_fn3("Hello", "World", z="Python"))

# print(bin(18))  # 0b10010 - двоичная
# print(oct(18))  # 0o22 - восьмеричная
# print(hex(18))  # 0x12 - шестнадцатеричная
#
# print(0B10010)
# print(0O22)
# print(0X12)
# print(0x12 + 0b10010 + 0o22 + 18)

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)

# s = "Hello"
# print(s, id(s))
# # print(s[1])
# # print(s[1:3])
# # print(s[-1])
# # print('a' in s)
# # s[1] = 'a'
# s = s + "!"
# print(s, id(s))

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.py")
# print(r"C:\folder\file.py")
# print(r"C:\folder\\"[:-1])
# print(r"C:\folder" + "\\")
# print("C:\\folder\\")

# print(b"a1b2c4")

# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")
# print(f"{round(45.4564647987, 2)}")
# print(f"{45.4564647987:.2f}")
# num = 74
# print(f"{{{{{num}}}}}")

# dir_name = "folder"
# file_name = "file.py"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)
# print("home\\", dir_name, "\\", file_name, sep="")

# s1 = ("Много    строчный \n"
#       "     текст")
# print(s1)
#
# s = """Мног остро   чный
#     тек
#     ст"""
# print(s)
#
# s2 = '''Мног остро   чный
#     тек
#     ст'''
# print(s2)

# a = """
# Многострочный
# комментарий
# """
#
# b = "Многострочный"
# "комментарий"
#
# print(a)
# print(b)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)

# print(min([1, 5, 6, 4, 7]))
# print(max([1, 5, 6, 4, 7]))
# print(len([1, 5, 6, 4, 7]))

# from geometry import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('Ц'))


# while True:
#     n = input("-> ")
#     if n == "-1":
#         break
#     else:
#         print(ord(n))


# my_str = "Test string for me "
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))
# print(chr(1068))

# a = 97
# b = 122
# if b > a:
#     a, b = b, a
# for i in range(b, a + 1):
#     print(chr(i), end=" ")
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# from random import randint
#
# shortest = 6
# longest = 16
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     random_length = randint(shortest, longest)
#     res = ""
#     for i in range(random_length):
#         res += chr(randint(min_ascii, max_ascii))  # uyi
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# print(dir(list))
# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.

# print(s.lower().count("l"))
# print(s.count('h', 1, -4))

# print(s.find("Python"))  # возвращает индекс искомой подстроки, если совпадения нет, то возвращает значение "-1"
# print(s.find("l", 4, 19))
#
# print(s.index("Python"))  # возвращает индекс искомой подстроки, если совпадения нет, то выбрасывает
# исключение ValueError


# st = "пять два"
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second + " " + first)

# print(s.find("l"))
# print(s.rfind("l"))
# print(s.rindex("l"))

# print(s.endswith("on."))
# print(s.endswith("LD!", 10, 13))
# print(s.index("LD!"))
# print(s.startswith("hel"))
# print(s.startswith("I am", 14))
# print(s.index("I am"))

# print("abc123".isalnum())  # определяет состоит ли строка из букв и цифр
# print("abc!!!123".isalnum())
# print("abС123".isalnum())
#
# print("ABCabc".isalpha())  # определяет состоит ли строка из букв (любой регистр)
# print("ABCabc7".isalpha())
# print("ABCabc@".isalpha())
#
# print("123".isdigit())  # определяет состоит ли строка из цифр
# print("123a".isdigit())
# print("123@".isdigit())
#
# print("abc".islower())  # проверяет находятся ли буквы в нижнем регистре (допускает цифры и спецсимволы)
# print("abc5@D".islower())
#
# print("ABC".isupper())  # проверяет находятся ли буквы в верхнем регистре (допускает цифры и спецсимволы)
# print("ABC2#".isupper())

# print("py".center(10))
# print("py".center(10, "-"))
# print("py".center(1))

# print("      py dfs df sdf".lstrip())
# print("py      ".rstrip())
# print("        py      ".strip())

# print("https://www.python.orgw".lstrip("/:psth").rstrip(".orgw"))
# print("https://www.python.orgw".strip("/:psth.orgw"))

# s = "hello, Python! I am learning Python. Мне нравится Python."
# print(s.replace("Python", "JavaScript", 2))

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("...".join(['1', '99']))
# print(":".join("Hello"))


# print("Строка разделенная пробелами".split())
# print("www.python.org".split("."))
# print("www.python.org.ru".split(".", 2))
# print("www.python.org.ru".rsplit(".", 2))

# fio = input("Введите ФИО: ").split()
# print(fio)
# print(f"{fio[0]} {fio[1][0]}. {fio[2][0]}.")

# lst = input("Введите числа через пробел: ").split()
# print(lst)
# lst = list(map(int, lst))
# print(lst)
# print(sum(lst))


# print("Вносим изменения в локальный репозиторий")

# print("Работа на новом устройстве")

# import re
# from os import write

# s = "Я ищу совпадения в 2025 году. \"И я их найду в 2 счё-та\". [6789]. H.ello_World."
# # reg = "\\."
# # reg = r"\."
# # reg = r"[205]"
# # reg = r"[12][0-9][0-9][0-9]"
# # reg = r"[А-яЁё]"
# # reg = r"[A-Z\[a-z\].-]"
# # reg = r"[^0-9]"
# # reg = r"\d"
# # reg = r"\D"
# # reg = r"\s"
# # reg = r"\S"
# # reg = r"\w"
# # reg = r"\W"
# # reg = r"\AЯ ищу"
# # reg = r"World.\Z"
# # reg = r"сов\B"
# # reg = r"\w+"
# # reg = r"\w*"
# # reg = r"^\w+\s\w+"
# # reg = r"\w+\.$"
# reg = r"я"
# reg = r"20*"
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# print(re.search(reg, s))  # месторасположение первого совпадения с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # месторасположение первого совпадения с шаблоном в начале строки
# print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, "!", s))  # поиск и замена
# print(re.findall(reg, s))
# st = "Час в 24-часовом формате от 00 до 23. 2021T21:40. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09"
# reg1 = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg1, st))

# print(re.findall(reg, s))


# d = "Цифры: 7, +17, --42, 0013, 0.3"
# # print(re.findall(r"[+-]?\d+\.?\d*", d))
# print(re.findall(r"[+-]?\d+[.\d]*", d))


# d = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s#.*", "", d))
# print("Дата рождения:", re.sub(r"-", ".", d))
# print("Дата рождения:", re.sub(r"-", ".", re.sub(r"\s#.*", "", d)))
# # print("Дата рождения:", "05.03.1987")


# st = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# # reg1 = r"\w+\s*=\s*\w+[\s\w.]*"
# reg1 = r"\w+\s*=[^;]+"
# print(re.findall(reg1, st))
# print(re.split(r";\s+", st))

# s1 = "12 сентября 2025 года"
# # reg1 = r"\d{4}"
# # reg1 = r"\d{2,4}"
# # reg1 = r"\d{,4}"
# reg1 = r"\d{2,}"
# print(re.findall(reg1, s1))

# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg1 = r"\+?7\d{10}"
# print(re.findall(reg1, st))

# print(re.findall(reg, s, re.IGNORECASE))

# print(re.findall(reg, s))
#
# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9_-]{3,16}$", login)
#
#
# print(validate_login("maasdss"))
# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
# text = "hello world"
# print(re.findall(r"\w\+", text, flags=re.DEBUG))


# text = """
# one
# two
# """
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
#
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))


# print(re.findall("""
# [a-z._-]+  # part1
# @          # @
# [a-z.-]+   # part2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# # python,
# # PYTHON"""
# reg1 = "(?mi)^python"
# print(re.findall(reg1, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))


# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# s1 = "12 сентября 2025 года 456543131"
# # reg1 = r"\d{2}"
# # reg1 = r"\d{2,4}?"
# # reg1 = r"\d{,4}?"
# reg1 = r"\d{2,}?"
# print(re.findall(reg1, s1))


# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Виктор"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0, int"
# # reg = r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# reg = r"((int|float)\s*=\s*(\d[.\w+]*))"
# print(re.findall(reg, s))
# print(re.search(reg, s).groups(3))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])
# print(m[3])


# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# a = "31-10-2021"
# pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(pattern, a))
# print(re.search(pattern, a))

# s = "Самолет прилетает 10/23/2025. Будет рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))


# Рекурсия

# def elevator(n):  # 0
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # стек: 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = 5
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         return lst[0]  # 9
#     else:
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):  # n = 15, base = 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # F
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14]  =>  E
#
#
# print(to_str(254, 16))  # FE

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_item(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))

# Файлы

# f = open("text.txt")
# f = open(r"E:\Python417\417\text.txt")
# print(f)
# print(*f)
# print(f.name)
# print(f.mode)
# print(f.encoding)
# f.close()
# print(f.closed)

# f = open("text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()


# f = open("text1.txt", "w")
# f.write("This is line1\nThis is line2\nThis is line3\n")
# f.close()


# f = open("text1.txt", "r")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open("text1.txt", "r")
# print(f.readlines(26))
# print(f.readlines())
# f.close()


# f = open("text1.txt", "r")
# for line in f:
#     print(line)
# f.close()


# f = open("xyz.txt", "w")
# f.write("Hello\nWorld")
# f.close()


# lines = ["This is line1\n", "This is line2\n", "This is line3\n"]
# f = open("xyz.txt", "a")
# # f.write("\nNew text")
# f.writelines(lines)
# f.close()

# f = open("xyz.txt", "w")
# lst = [str(i) for i in range(10, 1000, 10)]
# print(lst)
# for ind in lst:
#     f.write(ind + '\t')
# f.close()


# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл;\n")
# f.close()
#
# f = open("text2.txt", "r")
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello World\n"
# print(read_file)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_file)
# f.close()

# f = open("text.txt")
# print(f.read(3))
# print(f.tell())  # возвращает позицию условного курсора в файле
# print(f.seek(1))  # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text4.txt", "a+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# f = open("text7.txt", "r+")
# f.read()
# f.close()


# with open("text.txt", "w+") as f:
#     print(f.write("0123456789"))
# print(f.closed)

# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)  # "4.5 2.8 3.9 1.0 0.3 4.33 7.777"
#
#
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))
#
# print("Файл создан")


# with open("res.txt", "r") as f:
#     num = f.read()
#
# print(num)
# num_list = list(map(float, num.split()))
# print(num_list)
# res = 1
# for i in num_list:
#     res *= i
#
# print(res)

# file_name = "res1.txt"
#
# with open(file_name, "w") as f:
#     f.write("Файл именованная область данных на носителе информации, используемая как базовый объект"
#             " с данными в операционных системах.")   # взаимодействия
#
#
# def longest_words(file):
#     with open(file, "r") as text:
#         w = text.read().split()
#         print(w)
#         res = len(max(w, key=len))
#         print(res)
#         lst = [word for word in w if len(word) == res]
#         if len(lst) == 1:
#             return lst[0]
#         return lst
#
#
# print(longest_words(file_name))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
#
# with open("one.txt", "w") as f:
#     f.write(text)


# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# Модуль OS и OS.PATH

# import os

# print(os.getcwd())
# print(os.listdir())
# print(os.listdir("folder"))
# os.mkdir("folder1")
# os.makedirs("nested1/nested2/nested3")
# os.rmdir("folder1")
# os.remove("xyz.txt")
# os.rename("two.txt", "two_new.txt")
# os.rename("two_new.txt", "folder/two_new_1.txt")
# os.renames("text6.txt", "test/text6_1.txt")

# for root, dirs, files in os.walk("nested1", topdown=True):
#     print("Root:", root)
#     print("\tDirs:", dirs)
#     print("\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена")
#     print("-" * 50)
#
#
# remove_empty_dirs("nested1")


# print(os.listdir("nested1/folder1"))

# import os
# import os.path

# print(os.path.split(r"nested1\nested2\nested3\text5.txt"))
# print(os.path.join("nested1", "nested2", "nested3", "text5.txt"))
# print(os.path.join("nested2", r"D:\nested1", "nested3", "text5.txt"))
# print(os.path.isdir(r"nested1\nested2\nested3"))
# print(os.path.isfile(r"nested1\nested2\nested3\text5.txt"))


# import os

# dirs = [r"Work\F1", r"Work\F2\F21"]
# for d in dirs:
#     os.makedirs(d)

# files = {
#     "Work": ["w.txt"],
#     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, "w").close()
#
# files_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
#
# for file in files_with_text:
#     with open(file, "w") as f:
#         f.write(f"Какой-то текст в файле {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {"сверху вниз" if topdown else "снизу вверх"}")
#     for root, dirs, my_file in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(my_file)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)


# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt


# import os
# import time
#
# path = r"main.py"
# kb = os.path.getsize(path)
# print(kb // 1024)
# atime = os.path.getatime(path)  # дата последнего доступа к документу
# ctime = os.path.getctime(path)  # возвращает время создания файла или время последнего изменения файла
# mtime = os.path.getmtime(path)  # время последнего изменения файла
#
# print(atime)
# print(ctime)
# print(mtime)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(ctime)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 2
#
#     def set_coords(self, x1, y1):
#         self.x = x1
#         self.y = y1
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 100
# # p1.y = 200
# # print(p1.x, p1.y)
# p1.set_coords(100, 200)
# Point.set_coords(p1, 111, 222)
# # print(p1.__dict__)
# #
# p2 = Point()
# # p2.x = 10
# # p2.y = 20
# # print(p2.x, p2.y)
# p2.set_coords(10, 20)
# # print(p2.__dict__)
# #
# # print(Point.__dict__)
# # print(Point.__doc__)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}"
#               f"\nСтрана: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name())


# class Person:
#     skill = 10  # статическое свойство
#
#     def __init__(self, name, surname):
#         self.name = name  # динамические свойства
#         self.surname = surname
#         print("Инициализатор")
#
#     def __del__(self):
#         print("Финализатор (деструктор)")
#
#     def print_info(self):
#         print("\nДанные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill)
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
# p1 = 5
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0  # 3
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(1, 2)
# p2 = Point(10, 20)
# p3 = Point(100, 200)
# print(Point.count)
# print(p1.count)
# print(p2.count)
# print(p3.count)

# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot('P-5CO')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов:", Robot.k)


# class Point:
#     __slots__ = "__x", "__y"
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def __check_value(c):
#         # if isinstance(c, int) or isinstance(c, float):
#         # if isinstance(c, (int, float)):
#         #     return True
#         # return False
#         return isinstance(c, (int, float))
#
#     def set_coord(self, x, y):
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#
# p1 = Point(5, 10)
# # p1.z = 3
# # print(p1.z)
# # print(p1.__dict__)
# # print(p1.__x)
# # p1.set_coord(1, 2.5)
# print(p1.get_coord())
# p1._Point__x = 111
# print(p1.__dict__)
# print(Point.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Вызов __set_x")
#         self.__x = x
#
#     def __get_x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# # print(p1.x)
# p1.x = 50
# print(p1.x)
# del p1.x

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property   # геттер
#     def x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     @x.setter  # сеттер
#     def x(self, x):
#         if isinstance(x, int):
#             self.__x = x
#         else:
#             print("Некорректный тип данных")
#
#     # @x.deleter
#     # def x(self):
#     #     print("Удаление свойства")
#     #     del self.__x
#
#
# p1 = Point(5, 10)
# # print(p1.x)
# p1.x = 50
# print(p1.x)
# # del p1.x

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg  # _KgToPounds__kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.kg, "кг =>", w.to_pound(), "фунтов")
# w.kg = 41
# print(w.kg, "кг =>", w.to_pound(), "фунтов")
# w.kg = "десять"


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# # print(Point.__dict__)
# print(Point.get_count())


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# # print(Point.__dict__)
# print(Point.get_count())

# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))

# class Change:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#     def print_info(self):
#         print("Печать информации", self.name)
#
#
# print(Change.inc(10), Change.dec(10))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a  # 3
#         if b > mx:  # 5 > 3
#             mx = b  # 5
#         if c > mx:  # 7 > 5
#             mx = c  # 7
#         if d > mx:  # 9 > 7
#             mx = d  # 9
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print(Numbers.max(3, 5, 7, 9))
# print(Numbers.min(3, 5, 7, 9))
# print(Numbers.average(3, 5, 7, 9))
# print(Numbers.factorial(5))

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#     @classmethod
#     def from_string(cls, sting_date):
#         day, month, year = map(int, sting_date.split("."))
#         # date = cls(day, month, year)
#         # return date
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(sting_date):
#         if sting_date.count(".") == 2:
#             day, month, year = map(int, sting_date.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#
# dates = [
#     "23.10.2025",
#     "30-12-2025",
#     "01.01.2025",
#     "12.31.2025",
# ]
#
# for i in dates:
#     if Date.is_date_valid(i):
#         date1 = Date.from_string(i)
#         print(date1.string_to_db())
#     else:
#         print("Неправильная дата или формат строки с датой")


# date1 = Date.from_string("23.10.2025")
# print(date1.string_to_db())
#
# date2 = Date.from_string("15.12.2024")
# print(date2.string_to_db())

# sting_date = "23.10.2025"
# day, month, year = map(int, sting_date.split("."))  # ["23", "10", "2025"]
# # print(day, month, year)
# date = Date(day, month, year)
# print(date.string_to_db())
# "23.10.2025" => 2025-10-23

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percent()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or not 14 < old < 70:  # old < 14 or old > 70
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 70 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор класса Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self) -> None:
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw_rect(self) -> None:
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# # line._width = 10
# line.draw_line()
# # print(line._width)
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть больше 0")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть больше 0")
#
#     def area(self):
#         return self.__width * self.__height
#
#     def print_info(self):
#         print(f"Прямоугольник\nШирина: {self.__width}\nВысота: {self.__height}\nЦвет: {self.color}\n"
#               f"Площадь: {self.area()}")
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.__dict__)
# rect.print_info()

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def __str__(self):
#         return f"{self.width} {self.height} {self.fon}"
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
# #
# #
# # class RectBorder(Rect):
# #     def __init__(self, width, height, width1, types, color):
# #         super().__init__(width, height)
# #         self.width1 = width1
# #         self.type = types
# #         self.color = color
# #
# #     def show_rect(self):
# #         super().show_rect()
# #         print(f"Рамка: {self.width1} {self.type} {self.color}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print(shape1)
# shape2 = RectBorder(600, 300, "1px", "solid", "red")
# shape2.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# Перегрузка методов

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x=None, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(1, 2)
# print(p1.__dict__)
# p1.set_coord(10, 20)
# print(p1.__dict__)
# p1.set_coord(100)
# print(p1.__dict__)
# p1.set_coord(y=200)
# print(p1.__dict__)

# Абстрактные методы и Абстрактные классы

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self) -> None:
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self) -> None:
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self) -> None:
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 20)))
# figs.append(Line(Point(10, 10), Point(20, 30)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(70, 70), Point(200, 200)))
#
# for f in figs:
#     f.draw()

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print("Ферзь перемещен н аe2e4")
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()

# from geometry import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         # if length is None and radius is None:
#         #     self.width = self.length = width
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SquareTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = SquareTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SquareTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def print_info(self):
#         self.print_value()
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 71.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print("*" * 50)
# for elem in d:
#     elem.print_info()
# print("*" * 50)
# for elem in e:
#     elem.print_info()

# Интерфейс

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Реализация метода display 1")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("Реализация метода display 2")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()

# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def other_static_method():
#         print("Метод наружного класса")
#
#     def other_obj_method(self):
#         print("Метод экземпляра наружного класса")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj  # self.obj = MyOuter('внешний')
#
#         def inner_method(self):
#             print("Метод во внутреннем классе", MyOuter.age, self.obj.name)
#             MyOuter.other_static_method()
#             self.obj.other_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# class LightGreen:
#     def __init__(self):
#         self.name = "Light Green"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = LightGreen()
#         self.dg = self.DarkGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class DarkGreen:
#         def __init__(self):
#             self.name = "Dark Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# print(outer.name)
# g = outer.lg
# d = outer.dg
# g.display()
# d.display()
#
# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i9"
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7, 8)
# print(len(p))

# import geometry
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = geometry.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# print(p1.length)
# # print(p1.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt1 =", pt1.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is slipping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.sleep()
# dog.play()
# dog.bark()

# class A:
#     def __init__(self):
#         print("Init A")
#
#
# class B(A):
#     def __init__(self):
#         print("Init B")
#
#
# class C(A):
#     def __init__(self):
#         print("Init C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Init D")
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)
#
#
# class A:
#     def __init__(self):
#         print("Init A")
#
#
# class AA:
#     def __init__(self):
#         print("Init AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Init B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Init C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Init D")
#
#
# d = D()
# print(D.mro())


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Init Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Init Pos")
#         self.sp = sp
#         self.ep = ep
#         # Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self.sp} {self.ep} {self.color} {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()

# Миксины

# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name} {self.weight} {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 15:54 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n2 = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2.save_sell_log()

# Перегрузка операторов

# Число секунд в одном днеЖ 24 * 60 * 60 = 86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)  # Clock(300)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         if item == "min":
#             return (self.sec // 60) % 60
#         if item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должен быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
#
# c1["hour"] = 14
# c1["min"] = 20
# c1["sec"] = 50
# print(c1["hour"], c1["min"], c1["sec"])

# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# c3 = c1 + c2 + c4  # Clock(300) + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# c1 += c2
# print(c1.get_format_time())
# print(c4.get_format_time())
# print(c3.get_format_time())
# if c1 == c2:
#     print("Время одинаковое")
# else:
#     print("Время разное")
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время одинаковое")


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)  # [5, 5, 3, 4, 5]
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 => 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#
#         self.marks[key] = value  # [5, 5, 3, 4, 5, None, None, None, None, None, 4]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#
#         del self.marks[key]
#
#     def append(self, item):
#         self.marks.append(item)
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# s1.append(3)

# print(s1.marks)

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("Not name", 0, choice(["M", "F"])) for _ in range(1, randint(2, 6))]  # range(1, 1)
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# # cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimeter())

# from abc import ABC, abstractmethod
# import geometry
#
#
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def info(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         super().__init__(color)
#         self.side = side
#
#     def get_perimeter(self):
#         return self.side * 4
#
#     def get_area(self):
#         return self.side * self.side
#
#     def draw(self):
#         return ("*  " * self.side + "\n") * self.side
#
#     def info(self):
#         print(f"=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}\n"
#               f"Площадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         super().__init__(color)
#         self.length = length
#         self.width = width
#
#     def get_perimeter(self):
#         return (self.length + self.width) * 2
#
#     def get_area(self):
#         return self.length * self.width
#
#     def draw(self):
#         return ("*  " * self.width + "\n") * self.length
#
#     def info(self):
#         print(f"=== Прямоугольник ===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}\n"
#               f"Площадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# class Triangle(Shape):
#     def __init__(self, side_1, side_2, side_3, color):
#         super().__init__(color)
#         self.side_1 = side_1
#         self.side_2 = side_2
#         self.side_3 = side_3
#
#     def get_perimeter(self):
#         return self.side_1 + self.side_2 + self.side_3
#
#     def get_area(self):
#         p = self.get_perimeter() / 2
#         return round(geometry.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)), 2)
#
#     def draw(self):
#         rows = []  # []
#         for n in range(self.side_2):  # range(0, 6)  # 3
#             rows.append(" " * n + "*" * (self.side_1 - 2 * n))  # " " +
#         rows.reverse()
#         return "\n".join(rows)
#
#     def info(self):
#         print(f"=== Треугольник ===\nСторона 1: {self.side_1}\nСторона 2: {self.side_2}\n"
#               f"Сторона 3: {self.side_3}\nЦвет: {self.color}\n"
#               f"Площадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# # sq = Square(3, "red")
# # sq.info()
#
# # rect = Rectangle(3, 7, "green")
# # rect.info()
#
# # tr = Triangle(11, 6, 6, "yellow")
# # tr.info()
#
# figs = [Square(3, "red"), Rectangle(3, 7, "green"), Triangle(11, 6, 6, "yellow")]
#
# for g in figs:
#     g.info()


# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1("  ?  : Hello World!  ; "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s1 = StringStrip("?:!.; ")
# print(s1("  ?  : Hello World!  ; "))


# Класс как декоратор

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self):
#         print("Перед вызовом")
#         self.fn()
#         print("После вызова")
#
#
# @MyDecorator
# def func():
#     print("text")
#
#
# func()


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, a, b):
#         # print("Перед вызовом")
#         res = self.fn(a, b)
#         # print("После вызова")
#         return f"Перед вызовом\n{res} \nПосле вызова"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, a, b):
#         return self.fn(a, b) ** 2
#
#
# @Power
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         return f"Перед вызовом\n{self.fn(*args, **kwargs)} \nПосле вызова"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             print("Перед вызовом")
#             print(self.name)
#             fn(*args, **kwargs)
#             print("После вызова")
#         return wrap
#
#
# @MyDecorator("test")
# def func(a, b):
#     print(a, b)
#
#
# func(2, 5)


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrapper(a, b):
#             return fn(a, b) ** self.arg
#
#         return wrapper
#
#
# @Power(2)
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(2, 2))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# Дескрипторы

#
# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Данные должны быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.__name = StringD(name)
#         self.__surname = StringD(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Ivan", "Petrov")


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#
# p = Person("Ivan", "Petrov")
# p.name = "Viktor"
# print(p.name)

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Значение должно быть положительным")
#         instance.__dict__[self.name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple_order = Order('apple', 5, 10)
# print(apple_order.total())


# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     "MyList",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# print(lst, lst.get_length())


# import geometry.rect
# import geometry.sq
# import geometry.trian


# from geometry import *

# from geometry import rect, sq, trian
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.perimeter())
#
#
# if __name__ == '__main__':
#     run()

# import pickle


# filename = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоко", "манго"],
#     "овощи": ("морковь", "лук"),
#     "бюджет": 1000
# }
#
# with open(filename, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(filename, "rb") as f:
#     res = pickle.load(f)
#
# print(res)

# class Test:
#     num = 35
#     string = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\nСписок: {Test.lst}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
# # print(obj)


# my_obj = pickle.dumps(obj)
#
# res = pickle.loads(my_obj)
# print(res)


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)
# print(item3)


# import json

# data = {
#     'name': 'Olga',
#     'age': 35,
#     20: None,
#     True: 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 6
#         }
#     ],
#     None: "Кортеж"
# }
#
# with open("data_file.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
#
# with open("data_file.json", "r", encoding="utf-8") as f:
#     data1 = json.load(f)
#
# print(data1)
#
# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string, type(json_string))
#
# res = json.loads(json_string)
# print(res, type(res))


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'k', 'l', 'm', 'n']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):  # {"name": ..., "tel": ...}
#     try:
#         data = json.load(open('persons.json'))  # [{"name": ..., "tel": ...}, {"name": ..., "tel": ...}]
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)  # [{"name": ..., "tel": ...}, {"name": ..., "tel": ...}, {"name": ..., "tel": ...}]
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # st = ''
#         # for i in self.marks:
#         #     st += str(i) + ", "
#         # return f"Студент: {self.name}: {st[:-2]}"
#         # st = ", ".join(map(str, self.marks))
#         # return f"Студент: {self.name}: {st}"
#         return f"Студент: {self.name}: {", ".join(map(str, self.marks))}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_marks(self):
#         return sum(self.marks) / len(self.marks)
#
#     def get_file_name(self):
#         return self.name + ".json"
#
#     def dump_to_json(self):
#         data = {"name": self.name, 'marks': self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         # st = ""
#         # for i in self.students:
#         #     st += str(i) + "\n"
#         st = "\n".join(map(str, self.students))
#         return f"Группа: {self.group}\n{st}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         # st = gr1.remove_student(index)
#         # gr2.add_student(st)
#         gr2.add_student(gr1.remove_student(index))
#
#     def get_file_name(self):
#         return self.group.lower().replace(" ", "-") + ".json"
#
#     def dump_to_json(self):
#         data = [{"name": student.name, 'marks': student.marks} for student in self.students]
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# # print(st1)
# # print(st2)
# sts1 = [st1, st2]
# group1 = Group(sts1, "ГК Python")
# # print(group1)
# print()
# group1.add_student(st3)
# # print(group1)
# print()
# group1.remove_student(1)
# print(group1)
# print()
# sts2 = [st2]
# group2 = Group(sts2, "ГК Web")
# print(group2)
# Group.change_group(group1, group2, 0)
# print()
# print(group1)
# print(group2)
# group2.dump_to_json()
# group2.load_from_file()
# # st1.add_mark(5)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(4, 4)
# # print(st1)
# # print(st1.average_marks())
# # st2.dump_to_json()
# # st2.load_from_file()


# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def load(file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#
#         with open(file_name, "w") as f:
#             json.dump(data, f)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, "w") as f:
#                 json.dump(data, f)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(file_name):
#         county = input("Введите название страны: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if county in data:
#             print(f"Страна {county.capitalize()} столица {data[county].capitalize()} есть в словаре")
#         else:
#             print(f"Страны {county.capitalize()} нет в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input("Введите страну для корректировки: ").lower()
#         new_capital = input("Введите новое название столицы: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             data[country] = new_capital
#             with open(file_name, 'w') as f:
#                 json.dump(data, f)
#         else:
#             print("Такой страны в базе нет")
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}   # {1: 11, 2: 2}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]
#
# max_complete = top_users[0][1]
# print(max_complete)  # 12
#
# users = []  # [5, 10]
# for user, num_complete in top_users:
#     if num_complete < max_complete:  # 11 < 12
#         break
#     users.append(str(user))
#
# print(users)  # ['5', '10']
#
# max_users = " and ".join(users)
# print(max_users)
#
# print(f"Users {max_users} completed {max_complete} TOSOs")
#
#
# def keep(todo1):
#     is_complete = todo1["completed"]
#     has_max_count = str(todo1["userId"]) in users
#     return is_complete and has_max_count
#
#
# with open("filtered_data.json", "w") as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)
#
# with open("filtered_data.json", "r") as f:
#     print(json.load(f))


# import csv

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=",")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#
#     print(f"Всего в файле {count} строки.")


# with open("data.csv") as f:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=",", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1


# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Маша", 11, 17])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
#
# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

#
# with open("student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# Парсинг данных с сайтов

# from bs4 import BeautifulSoup
# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open("index.html").read()
# soup = BeautifulSoup(f, "html.parser")
# # row = soup.find("div", class_="name").text
# # row = soup.find_all("div", class_="name")
# # row = soup.find_all("div", class_="row")[2].find("div", {"class": "name"})
# # row = soup.find_all("div", {"data-set": "salary"})
# # row = soup.find_all("div", string="Alena")
# # row = soup.find("div", string="Alena").parent
# # row = soup.find("div", string="Alena").find_parent(class_="row")
# # row = soup.find("div", id="whois3")
# # row = soup.find("div", id="whois3").find_next_sibling()
# # row = soup.find("div", id="whois3").find_previous_sibling()
#
# # copywriter = []
# # row = soup.find_all("div", class_="row")
# # for i in row:
# #     cw = get_copywriter(i)
# #     if cw:
# #         copywriter.append(cw)
# # print(copywriter)
#
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)
#
# # print(row)

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("h1", class_="wp-block-heading").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=",", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[2]
#     plugins = p1.find_all("li")
#     for plugin in plugins:
#         name = plugin.find("h3", class_="entry-title").text
#         # url = plugin.find("h3", class_="entry-title").find("a").get("href")
#         url = plugin.find("h3", class_="entry-title").find("a")["href"]
#         rating = plugin.find("span", class_="rating-count").text
#         r = refined(rating)
#
#         data = {"name": name, "url": url, "rating": r}
#         write_csv(data)
#     # return plugins
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refind_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='utf-8-sig') as f:
#         writer = csv.writer(f, delimiter=",", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['tested']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("li", class_="wp-block-post")
#     for el in p1:
#         name = el.find("h3", class_="entry-title").text
#         url = el.find("h3", class_="entry-title").find('a').get("href")
#         snippet = el.find("div", class_="entry-excerpt").text.strip()
#         active = el.find("span", class_="active-installs").text.strip()
#         test = el.find("span", class_="tested-with").text.strip()
#         cy = refind_cy(test)
#         data = {'name': name,
#                 'url': url,
#                 'snippet': snippet,
#                 'active': active,
#                 'tested': cy}
#         write_csv(data)
#
#
# def main():
#     for i in range(3, 23):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# from parser import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == "__main__":
#     main()

# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != "GET":
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def geterate_content(code, url):
#     if code == 404:
#         return "<h1>404</h1><h3>Page Not Found</h3>"
#     elif code == 405:
#         return "<h1>405</h1><h3>Method Not Allowed</h3>"
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     # body = URLS.get(url, 'Error 404')
#     body = geterate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()


# import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date TEXT
#     )""")
#
#     cur.execute("DROP TABLE users")

# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # phone BLOB NOT NULL DEFAULT "+79991234567",
#     # age INTEGER CHECK(age>0 AND age<100),
#     # email TEXT UNIQUE
#     # )""")
#
#     # переименование таблицы
#     # cur.execute("""
#     # ALTER TABLE person
#     # RENAME TO person_table;
#     # """)
#
#     # добавление нового столбца
#     # cur.execute("""
#     #    ALTER TABLE person_table
#     #    ADD COLUMN address TEXT;
#     #    """)
#
#     # переименование столбца
#     # cur.execute("""
#     #    ALTER TABLE person_table
#     #    RENAME COLUMN address TO home_address;
#     #    """)
#
#     # # удаление столбца
#     # cur.execute("""
#     #    ALTER TABLE person_table
#     #    DROP COLUMN home_address;
#     #    """)
#
#     # удаление таблицы
#     # удаление столбца
#     cur.execute("""
#        DROP TABLE person_table;
#        """)

# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM T1
#         LIMIT 2, 5;
#     """)
#
#     for res in cur:
#         print(res)
#
#     res2 = cur.fetchall()
#     print(res2)
#
#     res4 = cur.fetchmany(2)
#     print(res4)
#
#     res3 = cur.fetchone()
#     print(res3)

# import sqlite3


# with sqlite3.connect("person.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS companies(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL)""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     company_id INTEGER,
#     FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE SET NULL
#     )""")


# with sqlite3.connect("book.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS books(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     count_page INTEGER NOT NULL CHECK(count_page > 0),
#     price REAL CHECK(price > 0)
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS author(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER CHECK (age > 16)
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS author_books(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         books_id INTEGER NOT NULL,
#         author_id INTEGER NOT NULL,
#         FOREIGN KEY (books_id) REFERENCES books(id)
#         FOREIGN KEY (author_id) REFERENCES author(id)
#         )""")


# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS student(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     surname TEXT NOT NULL,
#     name TEXT NOT NULL,
#     patronymic  TEXT NOT NULL,
#     age INTEGER NOT NULL CHECK(age >= 17 AND age <= 50),
#     [group] TEXT NOT NULL,
#     FOREIGN KEY ([group]) REFERENCES groups (id) ON DELETE RESTRICT
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS groups(
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        group_name TEXT NOT NULL)
#        """)
#
#     cur.execute("""
#      CREATE TABLE IF NOT EXISTS lessons(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      lesson_title TEXT NOT NULL
#      )""")
#
#     cur.execute("""
#      CREATE TABLE IF NOT EXISTS association(
#      group_id INTEGER,
#      lesson_id INTEGER,
#      PRIMARY KEY (group_id, lesson_id)
#      FOREIGN KEY (group_id) REFERENCES groups(id)
#      FOREIGN KEY (lesson_id) REFERENCES lessons(id)
#      )""")


import sqlite3

# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
# with sqlite3.connect("automobile.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")
# for car in cars_list:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)  # ('BMW', 54000),

# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {"Price": 0})

# cur.executescript("""
# DELETE FROM cars WHERE model LIKE 'B%';
# UPDATE cars SET price = price + 100;
# """)

# con.commit()
# con.close()

# con = None
# try:
#     con = sqlite3.connect("automobile.db")
#     cur = con.cursor()
#     cur.executescript("""
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars2 SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()


# with sqlite3.connect("automobile.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     # last_id = cur.lastrowid
#     # buy_id = 2
#     # cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_id, buy_id))
#
#     cur.execute("SELECT model, price FROM cars")
#     for res in cur:
#         print(res['model'], res['price'])
#
#     # print(cur.fetchone())
#     # print(cur.fetchmany(5))
#     # print(cur.fetchall())

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#     #     return False
#     # return True
#
#
# with sqlite3.connect("automobile.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );""")
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#     write_ava("out.png", img)


# with sqlite3.connect("automobile.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", 'w') as f:
#         for sql in con.iterdump():
#             f.write(sql)

# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

#  =================================================

import os

from django.utils.lorem_ipsum import words

from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group

from sqlalchemy import and_, or_, not_, desc, func, distinct


# if __name__ == '__main__':
#     db_is_creator = os.path.exists(DATABASE_NAME)
#     if not db_is_creator:
#         db_creator.create_database()
#
#     session = Session()
#
#     print(session.query(Lesson).all())
#     print("*" * 60)
#
#     for it in session.query(Lesson):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Lesson):
#         print(it.lesson_title)
#     print("*" * 60)
#
#     print(session.query(Lesson).count())
#     print("*" * 60)
#
#     print(session.query(Lesson).first())
#     print("*" * 60)
#
#     for it in session.query(Lesson).filter(Lesson.id >= 3):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Lesson).filter(Lesson.id >= 3, Lesson.lesson_title.like('Ф%')):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('М%'))):
#         print(it)
#     print("*" * 60)
#
#     for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(association_table.c.lesson_id == Lesson.id, association_table.c.group_id == Group.id, Group.group_name == 'MDA-9'):
#         print(it, gr)
#     print("*" * 60)
#
#     for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('М%'))):
#         print(it)
#     print("*" * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
#     print("*" * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
#     print("*" * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all())
#     print("*" * 60)
#
#     print(session.query(Student).filter(Student.age.between(16, 17)).all())
#     print("*" * 60)
#
#     print(session.query(Student).filter(not_(Student.age.between(17, 24))).all())
#     print("*" * 60)
#
#     for it in session.query(Student).filter(Student.age.like("1%")).limit(4):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Student).order_by(desc(Student.surname)):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-9'):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name).having(func.count(Student.surname) < 25):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(distinct(Student.age)):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Student.age).filter(Student.age < 20).distinct():
#         print(it)
#     print("*" * 60)

#  =================================================

# from jinja2 import Template

# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a*2 }} лет. Меня зовут {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)


# per = {'name': "Игорь", 'age': 28}
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)

# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """<select>
#     {% for c in cities %}
#         {% if c.id > 3 %}
#             <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#         {% elif c.city == 'Москва' %}
#             <option>{{ c['city'] }}</option>
#         {% else %}
#             {{c['city']}}
#         {% endif %}
#     {% endfor %}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
# link = """<ul>
#     {% for i in menu %}
#         {% if i.link == 'Главная' %}
#         <li><a href='{{ i['href'] }}' class='active'>{{ i['link'] }}</a></li>
#         {% else %}
#         <li><a href='{{ i['href'] }}'>{{ i['link'] }}</a></li>
#         {% endif %}
#     {% endfor %}
# </ul>"""
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44200},
#     {'model': 'Wolksvagen', 'price': 31300},
# ]
# cars = [4, 5, 6, 7, 8, 9, 10]
# tpl = "{{ cs | sum(attribute='price') }}"
# tpl = "{{ cs | sum }}"

# tpl = "{{ (cs | min(attribute='price')).model }}"
# tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)
#
# print(cars)


# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 32, "weight": 94.1},
# ]
#
# tpl = '''
# {% for u in users %}
# {% filter upper %}{{ u.name }}{% endfilter %}
# {% endfor %}
# '''
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)
#
# html = """
# {% macro fun_input(name, value='', type='text', size=20) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size={{ size }}>
# {% endmacro %}
#
# <p>{{ fun_input('username', '', 'text', 40) }}</p>
# <p>{{ fun_input('email', 'Email', 'email') }}</p>
# <p>{{ fun_input('password', 'Пароль', 'password') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# # =================================================

# from jinja2 import Environment, FileSystemLoader
#
# # persons = [
# #     {"name": "Алексей", "year": 18, "weight": 78.5},
# #     {"name": "Никита", "year": 28, "weight": 82.3},
# #     {"name": "Виталий", "year": 32, "weight": 94.1},
# # ]
# #
# # # html = """
# # # {% macro list_users(list_of_user) %}
# # #     <ul>
# # #         {% for u in list_of_user %}
# # #             <li>{{ u.name }} {{ caller(u) }}</li>
# # #         {% endfor %}
# # #     </ul>
# # # {% endmacro %}
# # #
# # # {% call(user) list_users(users) %}
# # #     <ul>
# # #         <li>age: {{ user.year }}</li>
# # #         <li>weight: {{ user.weight }}</li>
# # #     </ul>
# # # {% endcall %}
# # #
# # #
# # # """
# # #
# # # tm = Template(html)
# # # msg = tm.render(users=persons)
# # #
# # # print(msg)
# #
# # file_loader = FileSystemLoader('templates')
# # env = Environment(loader=file_loader)
# #
# # tm = env.get_template('home.html')
# # msg = tm.render(users=persons, title="About Jinja")
# #
# # print(msg)
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render()
#
# print(msg)


