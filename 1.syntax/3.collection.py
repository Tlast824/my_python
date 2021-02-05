# *** Список (list) ***

# Создание пустого списка
my_list = []
my_list_2 = list()

# добавление объекта (в конец списка)
my_list.append(100)
my_list.append(77)
my_list.append("А")
my_list.append([1,2,3])

# обращение к элементам списка
my_list[0] = 5
my_list[-2] = "B"

# чтение значений
element_value = my_list[1]

# удаление значений
# del my_list[-1]


my_list.remove(5)

# my_list.pop(0)

# print(my_list, a)

# создание заполненного списка

my_list_2 = [10, 20, 30, "А", "hello", True, 3.14, [1,2,3]]
# "длина" списка - количество элементов
# print(len(my_list_2))


# создание списка из строки
s = "Привет, Мир!"
lislFromStr = list(s)

# print(lislFromStr)

# методы списка


x = [1,2,3,4,5]
# представление
y = x

# y[2] = 100

# копия
z = x.copy()

# print(f"x: {x}; z: {z}")