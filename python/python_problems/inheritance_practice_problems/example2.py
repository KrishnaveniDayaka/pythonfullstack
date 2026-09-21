
class vehicle:
    def type_of_vehicle(self):
        print("IT is a Vechicle")
class Bike(vehicle):
    def type_of_vehicle(self):
        print("It is two wheeler vechicle")
class Car(vehicle):
    def type_of_vehicle(self):
        print("It is a four wheeler vehicle")
b=Bike()
c=Car()
b.type_of_vehicle()
c.type_of_vehicle()