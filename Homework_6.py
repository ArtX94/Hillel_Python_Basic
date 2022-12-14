print(
    "<-------------------- Task 1 --------------------->")
"""Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. 
Якщо перетворити не вдається функція має повернути 0."""

def arg_to_float(arg):
    try:
        return float(arg)
    except ValueError:
        return 0

digit = input("Enter some digit: ")
print(arg_to_float(digit))

print(
    "<-------------------- Task 2 --------------------->")
"""Напишіть функцію, що приймає два аргументи. Функція повинна:
- якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
- якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
- у будь-якому іншому випадку повернути кортеж з цих аргументів"""

def two_arguments(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    else:
        return (arg1, arg2)

print(two_arguments('py','thon'))



print(
    "<-------------------- Task 3 --------------------->")
"""Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
Попросіть користувача ввести свсвій вік.
- якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
- якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
- якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
- якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...)."""


def word_definition(age):
    word_endings = ( 'років', 'рік', 'роки', 'роки', 'роки', 'років', 'років', 'років', 'років', 'років')
    if(age >= 10 and age < 20):
        return 'років'
    elif(age >= 20):
        age = int(str(age)[-1])
    return word_endings[age]

def age_check(age):
    try:
        age = int(age)
        if(age < 1):
            return False
    except:
        return False

    if(age < 7):
        return f"Тобі ж {age} {word_definition(age)}! Де твої батьки?"
    elif(age > 7 and age <= 16):
        return f"Тобі лише {age} {word_definition(age)}, а це е фільм для дорослих!"
    elif(age > 65 and ('7' in str(age) == False)):
        return f"Вам {age} {word_definition(age)}? Покажіть пенсійне посвідчення!"
    elif('7' in str(age)):
        return f"Вам {age} {word_definition(age)}, вам пощастить"
    else:
        return f"Незважаючи на те, що вам {age} {word_definition(age)}, білетів всеодно нема!"

while (True):
        result = age_check(input("Введіть свій вік: "))
        if (result):
            print(result)
            break