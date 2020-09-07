# 1. Работа с перемеными
name = input('Как вас завут?')
age = input('Сколько вам лет?')
print(f"Привет {name} ваш возраст {age}")
if int(age) >= 18:
    print('Вам больше 18 лет')
else:
    print('Вам меньше 18 лет')

# 2. Математические выражения
print("Операция сложение")
a = input('Введите число a: ')
b = input('Введите число b: ')
summ = float(a) + float(b)
print(f"Сумма a + b = {summ}")

print("Операция разность чисел")
a = input('Введите число a: ')
b = input('Введите число b: ')
summ = float(a) - float(b)
print(f"Разность a - b = {summ}")

print("Операция умножение чисел")
a = input('Введите число a: ')
b = input('Введите число b: ')
summ = float(a) * float(b)
print(f"Результат уможения a * b = {summ}")

print("Операция деления чисел")
a = input('Введите число a: ')
b = input('Введите число b: ')
summ = float(a) / float(b)
print(f"Результат деления a * b = {summ}")
