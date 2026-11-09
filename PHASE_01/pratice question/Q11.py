print("===functions=====")
def greet():
  print("hello")
greet()
print("====function with parameter=====")
def greet(name):
    print("Hello", name)
greet("Pushpa")
print("====return statement=====")
def add(a,b):
  return a+b
result=add(10,20)
print(result)
print("====type of function=====")
print("====positional arguments===== ")
def student(name,age):
  print(name,age)
student("Pushpa",20)
print("====keyword arguments=====")
student(age=20,name="Pushpa")
print("====default arguments=====")
def greet(name="student"):
  print("hello",name)
greet()
greet("pushpa")
print("====variable length arguments=====")
def total(*numbers):
  print(sum(numbers))
total(10,20)
total(10,20,30,40)
print("====variable length keyword arguments=====")
def student(**details):
  for key,value in details.items():
    print(key,":",value)
student(name="pushpa",age=20,course="CSE")
print("=====scope of variable=====`")
def show():
  x=10
  print(x)
show()
print("====lambda function=====")
square=lambda x:x*x
print(square(6))
print( "=====map function=====")
numbers=[1,2,3,4,5]
result=list(map(lambda x:x*2,numbers))
print(result)
print("====filter function=====")
numbers=[1,2,3,4,5]
result=list(filter(lambda x:x%2==0,numbers))
print(result)
print("====reduce function=====")
from functools import reduce
number=[1,2,32,4]
result=reduce(lambda x,y:x+y,number)
print(result)
print("====docstring=====")
def greet(a,b):
  """This function takes two numbers and returns their sum."""
  return a+b
print(greet.__doc__)