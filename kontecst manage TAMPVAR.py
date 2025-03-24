#Напиши контекстный менеджер `TempVar`, который будет временно изменять значение переменной на указанное,
# а после выхода из блока `with` возвращать её исходное значение.
class TempVar:
    def __init__(self, var_ref, temp_value):
        self.var_ref = var_ref
        self.temp_value = temp_value
        self.original_value = None

    def __enter__(self):
        self.original_value = self.var_ref[0]
        self.var_ref[0] = self.temp_value
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.var_ref[0] = self.original_value


x = [10]

print("До блока with:", x[0])

with TempVar(x, 40) as tmp:
    print("Внутри блока with:", x[0])

print("После блока with:", x[0])
