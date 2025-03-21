# Напиши декоратор `validate_args`, который будет проверять, что аргументы функции являются положительными числами.
# Если аргументы не соответствуют условию, декоратор должен вызывать исключение `ValueError`.
# Используй функцию isinstance, и посмотри что такое args и kwargs
def takes_positive(func):
    def wrapper(*args, **kwargs):
        for value in args + tuple(kwargs.values()):
            if not isinstance(value, int):
                raise TypeError
            if value <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper

@takes_positive
def summator(a):
    a = c
    print(a)

c = int(input())
summator(c)
