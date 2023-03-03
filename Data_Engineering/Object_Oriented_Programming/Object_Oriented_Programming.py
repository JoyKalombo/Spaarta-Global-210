class Car():
    pass


my_first_object = Car()
my_first_object


class Dog():
    animal_kind = "canine"

    def __init__(self, name="Kenji", breed="Shiba Inu"):
        # Attributes (we get these from the user)
        self.name = name
        self.breed = breed

    # my_dog = Dog(name="shakati", breed="Berger de Beauce")

    def bark(self, age):
        """
        this is a method that makes the dog bark
        :param age:
        :return:
        """
        print("woof and my name is {} and my age is {}".format(self.name, age))


my_dog3 = Dog(name="shakti", breed="Berger de Beauce")

my_dog3.bark()

class circle():

    def __init__(self, radius, pi):
            # Attributes for the circle
        self.pi = 3.14
        self.radius = radius

    def circle_area(self):
        return self.radius * self.radius * self.pi

    def circle_circumference(self):
        return self.radius * self.pi * 2




