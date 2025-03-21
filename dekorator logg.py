#Напиши декоратор `logger`, который будет записывать в файл `log.txt`
# информацию о вызовах функции:
# имя функции, переданные аргументы и возвращаемое значение.
def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):

            result = func(*args, **kwargs)

            with open(filename, 'w') as f:
                f.write(str(result))

            return result
        return wrapped
    return decorator


@logger('log.txt')
def summator(num_list):
    return sum(num_list)

summator([1, 2, 8])

with open('log.txt' ) as f:
    print(f.read())
