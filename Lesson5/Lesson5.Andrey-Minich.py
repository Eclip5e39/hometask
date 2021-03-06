# 1. Написать лямбда функцию определяющую чётное/нечётное.Функция принимает
# параметр (число) и если чётное то выдаёт слово “чётное”, если нет - то “нечётное”.
# 2. Дан список чисел. Вернуть список, где при помощи функции map() каждое число
# переведено в строку. В качестве функции в map() используется lambda.
# 3. При помощи функции filter() из котрежа слов отфильтровать только те, которые
# являются полиндромами (которые читаюся одинаково в обе стороны.)
# 4. Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка: from datetime import datetime      time = datetime.now()


""" 1. Написать лямбда функцию определяющую чётное/нечётное.Функция принимает
параметр (число) и если чётное то выдаёт слово “чётное”, если нет - то “нечётное”."""

def do_operation(x, operation):
    result = operation(x)
    if result == True:
        print(f'Четное')
    else:
        print(f'Не четное')


date = int(input('Введите число: '))
do_operation(date, lambda x: x % 2 == 0)


""" 2. Дан список чисел. Вернуть список, где при помощи функции map() каждое число
переведено в строку. В качестве функции в map() используется lambda."""

numbers = [i for i in range(6)]
print(list(map(lambda x: str(x), numbers)))

print()


"""3. При помощи функции filter() из котрежа слов отфильтровать только те, которые
являются полиндромами (которые читаюся одинаково в обе стороны.)"""

def is_palindrome(n):
    n = str(n)
    m = str(n[::-1])
    return n == m


words = ('дом', 'шалаш', 'комок', 'земля', 'поп')
output = filter(is_palindrome, words)
print('Слова палиндромы:', list(output))


"""4. Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
Подсказка: from datetime import datetime      time = datetime.now()"""




