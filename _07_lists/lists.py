fruits = ['apple', 'banana', 'mango']
print(fruits)

# my_list = list([1, 2, 3])
# print(my_list)

# Получение длинны списка
list_length = len(fruits)
print(list_length)

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
# Проверка по значению
print(list_1 == list_2)  # True
# Проверка по ссылке в памяти
print(list_1 is list_2)  # False

# Приведение к boolean
print(bool([]))  # False
print(bool([1]))  # True

# Проверка элемента на наличие в списке
print('banana' in fruits)  # True
print('avocado' in fruits)  # False

# Приведение строки к списку
my_string = 'my_string'
print(list(my_string))  # ['m', 'y', '_', 's', 't', 'r', 'i', 'n', 'g']

# Складываем списки
array_of_nums_1 = [1, 2, 3]
array_of_nums_2 = [4, 5, 6]
array_of_nums_3 = array_of_nums_1 + array_of_nums_2
print(array_of_nums_3)  # [1, 2, 3, 4, 5, 6]

# Методы списков

## append
appendRes = fruits.append('watermelon')  # Добавляет элемент в конец списка и мутирует список
print(appendRes)  # None
print(fruits)  # ['apple', 'banana', 'mango', 'watermelon']

## pop
popRes = fruits.pop()  # Возвращает последний элемент списка и мутирует список
print(popRes)  # watermelon
print(fruits)  # ['apple', 'banana', 'mango']

## extend

list_1 = ['string', 'boolean']
list_2 = ['array', 'number']
list_3 = list_1.extend(list_2)
print(list_1)  # ['string', 'boolean', 'array', 'number']
print(list_2)  # ['array', 'number']
print(list_3)  # None

## sort

list_of_nums = [1, 5, 3, 2, 9, 10, 2, 3, 1, 6]
sorted_list_of_nums = list_of_nums.sort()
reversed_sorted_list_of_nums = list_of_nums.sort(reverse=True)

print(list_of_nums)  # [10, 9, 6, 5, 3, 3, 2, 2, 1, 1]
print(sorted_list_of_nums)  # None
print(reversed_sorted_list_of_nums)  # None
