
# for i in range(50) :
#     print("Good morning students !")

#     i = 1
#     while i <=5:
#         print("Good morning students!")
#     i <= 1
 
# def greet():
#         print("hello students")
#         print("welcome to python programming      ")
# greet()


#

# student = {
#     "name": "a",
#     "usn" : 146,
#     "marks": 90,
#     "passed": True
# }
# student["college"] = "gopalan college of Engineering and Management"
# student["course"] = "cse"
# print(student["name"])
# print(student["college"])
# print(student["marks"])


# class student:
#     def display(self):
#         print("hello students")
#         print("welcome to python programming")

# s1 = student()

# s1.display()

# class student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)

# s1 = student("a", 23, 85.5)
# s2 = student("b", 22, 90.0)
# s1.display()
# s2.display()

# class student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#        self.__marks = marks

#     def show_marks(self):
#         print("Marks:", self.__marks)

#         s1 = student()
#         s1.set_marks(85.5)
#         s1.show_marks()


# class father:
#     def house(self):
#         print("Father has a house")

# s = son()
# s.house()
# s.car()

# class grandfather:
#     def land(self):
#         print("Grandfather has a land")

# class son(father):
#     def car(self):
#         print("Son has a car")

# s.land()
# s.house()
# s.car()

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     animal.sound()


from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class Card(payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")

p1 = UPI()
p2 = Card()
p1.pay(1000)
p2.pay(2000)