

# объявляем класс и создаем метод
class Parrot:

    # атрибуты экземпляра через конструктор класса (не позволит создать экземпляр без передачи name, age)
    def __init__(self, name, age):
        print(f"Появился попугай {name}")
        self.name = name
        self.age = age

    # метод экземпляра
    def sing(self, song):
        return f'{self.name} поет: "{song}"'

    def dance(self, style):
        return "{} танцует {}".format(self.name, style)

    def __del__(self):
        print(f"Попугай {self.name} закончил")


# создаем экземпляры класса
kesha = Parrot("Кеша", 10)
trunya = Parrot("Труня", 20)

# вызываем методы экземпляра
print(kesha.sing("А моей женой накормили толпу"))
print(kesha.dance("брейк"))

print(trunya.sing("Трунь-трунь-трунь"))
print(trunya.dance("казачок"))