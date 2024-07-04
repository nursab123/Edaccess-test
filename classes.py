'''class StringHandling:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input("Enter a string: ")
    def printString(self):
        print(self.string.upper())

sh = StringHandling()  # create an instance
sh.getString()  # get input from the users
sh.printString()  # print the input in uppercase'''# task 1


'''class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

square = Square(4)
print (square.area())''' # task 2


'''class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 6)
print (rectangle.area())'''# task 3


'''import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point ({self.x}, {self.y})")
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other_point):
        return math.sqrt((self.x-other_point.x)**2 + (self.y-other_point.y)**2)

p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()
p2.show()
print(p1.dist(p2))

p1.move(3, 4)
p1.show()
print(p1.dist(p2))'''# task 4


'''class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}")
    def withdraw(self, amount):
        if amount>self.balance:
            print("Withdrawal amount exceeds available balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is {self.balance}")

account = Account("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)'''# task 5