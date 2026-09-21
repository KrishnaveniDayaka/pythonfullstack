
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")
class Pet(Dog, Cat):
    def play(self):
        print("Pet is playing")
p = Pet()
p.eat()
p.bark()
p.meow()
p.play()