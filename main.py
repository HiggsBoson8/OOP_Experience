import os
os.system("clear")



class User():
    """
    Это класс User, и его документа 
    """

    def __init__(self, name, age):
        # Инициализируем атрибуты имени и возраста
        self.name = name
        self.age = age


    def __str__(self):
        return f"юзер класс {self.name}"

a = User("Иван", 20) 
print(a)
# Печатаем атрибут dict экземпляра
print(a.__dict__) 

# Напечайте имя модуля экземпляра 
print(a.__module__)

# Напечатайте строку документации класса
print(a.__doc__)

# Напечатайте атрибут dir объекта
print(a.__dir__())

# Напечатайте результат вызова метода reduce(вызовет исключение AttributeError, так как этот метод не реализован)
try:
    print(a.__reduce__())
except AttributeError:
    print("AttributeError: 'User' object has no attribute '__reduce__' ")



