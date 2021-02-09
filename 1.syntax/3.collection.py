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


# *** Кортеж (tuple) ***

# неизменяемая (immuntable) коллекция
my_tuple = (10, 20, 30)

# чтение данных 
el = my_tuple[-1]

# нельзя делать срез кортежи
el = my_tuple[-1:-3:-1]

# rjgbz
z =x.copy()

z(Z) = 100

# print(F"x: {x}; z: {z}")

# срез списка
my_list = [10,20,30,40,50,60,70]

# прямой срез
slice_f = my_list[1:4] #  с первого индекса до 4

slice_f = my_list[2:] # со 2 индекса до

slice_f = my_list[::2] # с самого начала до шага 2

slice_f = my_list[1:6:2]

# print(slice_f)

# обратный срез 

# *** Словарь (dictionary) ***

# Создание словаря
# {ключ:значение} (пара "ключ-значение")
my_dict = {1 : 100, 2:200, 3:777}
me_dict_2 = {"ф":10, "b":"hello", "с":[1,2,3]}

# чтение данных
item = me_dict_2[10]

# применеие алтернативы условным операторам
condition = "key_1"_
d = {"key_1":100, "key_2":200}
print(d[condition])