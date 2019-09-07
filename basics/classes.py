#OOP. classes and objects

class MyClass:
    def __init__(self):
        self.number = 0
    def say_hello(self):
        print("Экземпляр класса")
    def set(self,n):
        self.number = n
    def get(self):
        print("MyClass.number is ",self.number)

class Elevator():
    def __init__(self):
        self.floor = 1
        self.MINWEIGHT = 0
        self.MAXWEIGHT = 100
        self.weight = 0
        self.door_open = True
    def closeDoors(self):
        self.door_open = False