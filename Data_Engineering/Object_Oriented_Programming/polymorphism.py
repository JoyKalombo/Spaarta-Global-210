class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


fluffy = Dog("Fluffy")
sushi = Cat("Sushi")

fluffy.speak()

sushi.speak()


def pet_speak(pet):
    print(pet.speak())

for pet in [fluffy,sushi]:
    pet_speak(pet)