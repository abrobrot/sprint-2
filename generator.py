#Напиши генератор `number_generator`, который будет возвращать числа от 1 до N
# (где N — это число, передаваемое в генератор).
# Генератор должен возвращать числа по одному при каждом вызове.
def generator_number(my_number):
    i = 0
    while i  <= my_number:
        i += 1
        yield i


for num in generator_number(3):
    print(num)