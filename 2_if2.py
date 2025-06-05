"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def string_comparing(string1, string2) -> int:
    """
    Функция сравнивает две строки и возвращает код ответа
    """
    result = -1
    if not (isinstance(string1, str) and isinstance(string2, str)):
        result = 0
    elif string1 == string2:
        result = 1
    elif string1 != string2:
        if len(string1) > len(string2):
            result = 2
        elif string2 == 'learn':
            result = 3
    return result


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    result = string_comparing(0, 0)
    print(f'0. {result}')
    result = string_comparing('один', 'один')
    print(f'1. {result}')
    result = string_comparing('больше', 'два')
    print(f'2. {result}')
    result = string_comparing('три', 'learn')
    print(f'3. {result}')


if __name__ == "__main__":
    main()
