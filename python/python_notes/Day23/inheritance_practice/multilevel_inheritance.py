
class Animal:
    def sound(self):
        print("Animal can make sounds")
class Dog(Animal):
    def bark(self):
        print("Dog makes Barking")
class Puppy(Dog):
    def cry(self):
        print("Puppy is crying")
p=Puppy()
p.sound()
p.bark()
p.cry()