
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def DisplayPerson(self):
        print('Name: ',self.name)
        print('Age: ', self.age)

class Student(Person):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.name, self.age, "to the class of", self.graduationyear)


p1 = Student('khang',6,2019)
# p1.DisplayPerson()
p1.welcome()



