
class Parent:
    def land(self):
        print("This is my Property (parents'property)")
class child1(Parent):
    def MyShare(self):
        print("This is my share in my parent's property (child1)")
class child2(Parent):
    def Myshare2(self):
        print("This is my share in my parent's property (child2)")
c1=child1()
c2=child2()
c1.MyShare()
c1.land()
c2.Myshare2()
c2.land()