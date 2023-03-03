class Animal():
    def __init__(self):
        print("Hey everyone, Animal created!.")

    def who_am_i(selfself):
        print("I am an animal")


class Dog(Animal):
    pass


my_dog = Dog()
my_dog.who_am_i()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


x = Student()
x.printname()
