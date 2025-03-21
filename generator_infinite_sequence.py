#Напиши генератор `infinite_sequence`, который будет возвращать бесконечную последовательность чисел, начиная с 0.
# Генератор должен возвращать числа по одному при каждом вызове.
# Чтобы избежать бесконечного цикла, ограничь вывод первых N чисел.
def infinite_sequence():
    num_ = 0
    while True:
        yield num_
        num_ += 1


my_num = int(input('Введите колличество чисел: '))
for num in infinite_sequence():
    if num < my_num :
        print(num)
    else:
        break
