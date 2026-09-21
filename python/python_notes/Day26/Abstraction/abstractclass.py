
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):#abstract method no implementation
        pass
class Dog(Animal): #concreate class
    def sound(self): 
        print("Dog barks")
d = Dog() #create object for concrete class
d.sound()