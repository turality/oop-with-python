class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name)
    def add_one(self,x):
        return x+1
    def get_name(self):
        return self.name
    def bark(self):
        print("bark")
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age

d = Dog("Ja",2)
print(d.get_name())
d.set_age(1)
print(d.get_age())
