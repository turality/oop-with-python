class Person:
    number_of_people = 0
    def __init__(self,name):
        self.name = name
        Person.add_person()
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people+=1

p1 = Person("Tural")
p2 = Person("Jill")
# print(p1.number_of_people)
# print(p2.number_of_people)
# print(Person.number_of_people)
# Person.number_of_people = 9
# print(p1.number_of_people)
# print(p2.number_of_people)
# print(Person.number_of_people)
p3 = Person("Bill")
print(Person.number_of_people_())