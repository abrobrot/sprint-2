# Создай генератор `filter_generator`, который будет принимать на вход итерируемый объект и функцию-фильтр.
# Генератор должен возвращать только те элементы, для которых функция-фильтр возвращает `True`.
# ( Функция фильтр, к примеру функция фильтрует только четные значения или нечетные или т.п.)
def filter_generator(new_my_object):
    new_my_object = my_object.split(' ')
    for num in new_my_object:
        if int(num) % 2 != 0:
            yield True, print(num)
        else:
            yield False
num = ()
my_object = input('Введите числа: ')
new_my_object = my_object.split(' ')
for blen in filter_generator(num):
    if num == True:
        print(blen)
