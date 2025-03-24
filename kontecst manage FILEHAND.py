#Напиши контекстный менеджер `FileHandler`, который будет открывать файл в указанном режиме,
# автоматически закрывать его после выхода из блока `with`, а также обрабатывать исключения,
# связанные с файловыми операциями ( прочитай про такие ошибки, или используй свою, к примеру нельзя цифры писать в файл ).
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            if exc_type == TypeError and "write() argument must be str" in str(exc_val):
                print("Нельзя записывать числа в файл.")
                return True
        return False

with FileHandler("test.txt", "w") as file:
    file.write(57657)

with FileHandler("test.txt", "w") as file:
    file.write("Hello, world!")
