
class Parent:
    def sleep(self):
        print("I am Sleeping")
    def eat(self):
        print("I am eating")
    def work(self):
        print("I have personal work")
class Mother:
    def cook(self):
        print("I am cooking")
class child(Parent,Mother):
    def study(self):
        print("I am studying")
c=child()
c.study()
c.cook()
c.eat()
c.sleep()