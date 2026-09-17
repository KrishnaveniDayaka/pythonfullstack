
class Animal:
    def sound(self):
        print("Animal make sounds")
class Dog(Animal):
    def sound(self):
        print("Dog make sound Bark")
class Cat(Animal):
    def sound(self):
        print("Cat make sound like meow")
    
d=Dog()
c=Cat()
d.sound()
c.sound()