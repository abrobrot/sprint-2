#Напиши декоратор `timer`, который будет измерять время выполнения функции и выводить его в секундах.
# Декоратор должен работать с любыми функциями.
def timer_(func):
    from time import time
    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f'Время выполнения функции: {end_time-start_time} сек.')
        return value
    return wrapper

@timer_
def summa(a, b):
    from time import sleep
    sleep(3)
    return a + b
print(summa(8,14))
