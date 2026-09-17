
class Car:
    def __init__(self,make,model,speed):
        self.make=make
        self.model=model
        self.speed=speed
    def display(self):
        print(f"Company name is {self.make} , model name is {self.model} ,speed of car is {self.speed}")
    def accelerate(self,new_speed):
        self.speed=self.speed+new_speed
        print("speed after acceleration:",self.speed)
    def brake(self,brake1):
        if brake1<=self.speed:
            self.speed=self.speed-brake1
            print("Speed after brake: ",self.speed)
        else:
            self.speed=0
            print("Car is not moving")
make=input("Enter company name:")
model=input("Enter model name:")
speed=int(input("Enter speed :"))
new_speed=int(input("Enter new speed of car:"))
brake1=int(input("Enter brake speed "))
c=Car(make,model,speed)
c.display()
c.accelerate(new_speed)
c.brake(brake1)
