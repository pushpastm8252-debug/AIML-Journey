print("====oops===")
print("====class====")
class Student:

    name = "Pushpa"
    age = 20

    def display(self):
        print(self.name)
        print(self.age)
print("=====object=======")
class Student:

    def display(self):
        print("Hello Student")


s1 = Student()

s1.display()
print("=====constructor=======")
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Pushpa", 20)
s2 = Student("Mohit", 21)

s1.display()
s2.display()
print("====self====")
class Student:
  def __init__(self,name):
    self.name=name
  def show(self):
      print(self.name)
s1=Student("pushpa")
s1.show()
print("====instance variable====")
class student:
  def __init__(self,name):
    self.name=name
s1=student("pushpa")
s2=student("mohit")
print(s1.name)
print(s2.name)
print("====class varible======")
class Student:

    college = "Shobhit University"

    def __init__(self, name):
        self.name = name


s1 = Student("Pushpa")
s2 = Student("Mohit")

print(s1.college)
print(s2.college)
print("====instance method====")
class Student:
  def show(self):
    print("instance method")
s1=Student()
s1.show()
print("====class method====")
class student:
  college="shobhit university"
  @classmethod
  def show_college(cls):
    print(cls.college)
student.show_college()
print("====static method====")
class calculator:
  @staticmethod
  def add(a,b):
    return a+b
print(calculator.add(10,20))
print("====encapsulation====")
class bankaccount:
  def __init__(self,balance):
    self.__balance=balance
  def deposite(self,amount):
    if amount>0:
      self.__balance+=amount
  def get_balance(self):
    return self.__balance
account=bankaccount(1000)
account.deposite(500)
print(account.get_balance())
print("=====inheritance====")
class animal:
  def eat(self):
    print("animal is eating")
class dog(animal):
  def bark(self):
    print("dog is barking")
d=dog()
d.eat()
d.bark()
print("=====single inheritance=====")
class A:
  pass
class B(A):
  pass
print("====multiple inheritance======")
class Father:

    def skills(self):
        print("Gardening")


class Mother:

    def talent(self):
        print("Cooking")


class Child(Father, Mother):
    pass


c = Child()

c.skills()
c.talent()
print("====multilevel inheritance====")
class A:
  def show_a(self):
    print("class A")
class B(A):
  def show_b(self):
    print("class B")
class C(B):
  def show_b(self):
    print("class ")
print("=====hierarchical inheritance=====")
class animal:
  def eat(self):
    print("eating")
class dog(animal):
  pass
class cat(animal):
  pass
print("====method overriding====")
class Animal:
  def sound(self):
    print("animal makes sound")
class dog(animal):
  def sound(self):
    print("dog barks")
d=dog()
d.sound()
print("===super function====")
class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        super().show()
        print("Child method")


obj = Child()
obj.show()
print("===polymorphism=====")
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
print("===duck typing====")
class Dog:

    def sound(self):
        print("Bark")


class Robot:

    def sound(self):
        print("Beep")


def make_sound(obj):
    obj.sound()


make_sound(Dog())
make_sound(Robot()) 
print("====abstraction====")
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle(10, 5)

print(r.area())