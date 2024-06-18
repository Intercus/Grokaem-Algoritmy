#Шпаргалка Рекурсии
#Когда функция вызывает саму себя это называется рекурсией
#В каждой рекурсивной функции должно быть два случая:базовый и рекурсивный
#Стек поддерживает две операции занесение и извлечение элементов
#Все вызовы функций сохраняются в стеке вызовов
#Если стек вызовов станет очень большим он займет слишком много память
#Наблюдение
#Если будет рекурсия без условия остановки то python не даст выполнить 
#С ошибкой:maximum recursion depth exceeded(превышена максимальная глубина рекурсии)
#Факториал числа с помощью рекурсии
def fact(x):
    if x == 0:
        return 1
    else:
        print(x)
        return x * fact(x-1)
print(fact(5))

#Подсчет суммы рекурсией
def sum_recursive(lst):
    if len(lst) == 0: #Проверка если список пуст
        return 0
    else:
        return lst[0] + sum_recursive(lst[1:])

# Пример использования
my_list = [1, 2, 3, 4, 5]
print(sum_recursive(my_list))  # Вывод: 15

#Подсчет количества элементов в списке
def kol_element(lst):
    if not lst: #Проверка если список пуст
        return 0
    return 1 + kol_element(lst[1:])

# Пример использования
my_list = [1, 2, 3, 4, 5]
print(kol_element(my_list))  # Вывод: 5

#Поиск большего числа в списке
def max_number(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = max_number(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

my_list = [7,8,6,3,4,5]
print(max_number(my_list))# Вывод: 8
