class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

def make_animal_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()

make_animal_sound(dog)
make_animal_sound(cat)
