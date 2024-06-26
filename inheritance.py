class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'Iam {self.name} and my age is {self.age}')

class Cat(Pet):

    def speak(self):
        print('meow')

class Dog(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

        print(f'Iam {self.name} and my age is {self.age} and my colour is {self.color}')

    def speak(self):
        print('bark')


p = Pet('Tim',8)
p.show()
d=Dog('Rocky',2, 'black')
d.show()
c = Cat('Jil',4)
c.show()

d.speak()