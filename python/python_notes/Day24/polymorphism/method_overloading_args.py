class Calculator:
    def add(self, *numbers):
        total = 0
        for number in numbers:
            total = total + number
        print(total)
c = Calculator()
c.add(10)
c.add(10, 20)
c.add(10, 20, 30)