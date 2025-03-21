#Напиши контекстный менеджер `Timer`, который будет измерять время выполнения блока кода внутри блока `with`
# и выводить его в секундах.

import time


class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f'Время выполнения: {self.end - self.start:.2f} секунд')


with Timer():
    time.sleep(2)
