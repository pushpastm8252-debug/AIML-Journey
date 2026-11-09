print("====operators=====")
a=4
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print("====comparison operators=====")
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print("====logical operators=====")
age=20
print(age>18 and age<30)
print(age>18 or age<30)
print(not(age>18 and age<30))
print("====membership operators=====")
languages=["python","java","c++"]
print("python" in languages)
print("ruby" not in languages)
print("=====identity operators=====")
a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)
print(a is not c)
print(a== c)
print("=====Bitwise operators=====")
a=7
b=3
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<1)
print(a>>1)
