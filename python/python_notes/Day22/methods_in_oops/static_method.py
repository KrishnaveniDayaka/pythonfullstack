
#A static method is a method defined inside a class that does not depend on instance data
#  or class data. It does not take self or cls as its first parameter.
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
print(Calculator.add(10, 20))