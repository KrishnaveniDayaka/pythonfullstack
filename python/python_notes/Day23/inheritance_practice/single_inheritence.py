
class Animal:
    def Sleep(self):
        print("Animals are Sleeping")
    def Bark(self):
        print("Animals are sounding")
class Dog(Animal):
    def Eat(self):
        print("Dog is Eating")
d=Dog()
d.Sleep()
d.Eat()
d.Bark()
