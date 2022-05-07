class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'I am {self.name}. I am {self.age}.')
    def speak(self):
        print("idk what to say")
class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("meow")
    def show(self):
        super().show()
        print(f"I am {self.color}")
class Dog(Pet):
    def speak(self):
        print("bark")
class Fish(Pet):
    pass
p = Pet("Tural",19)
p.speak()
c = Cat("Bill",34,"red")
c.speak()
c.show()
d = Dog("Jill",25)
d.speak()
f = Fish("Bubbles",19)
f.speak()