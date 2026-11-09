print("====conditional statements=====")
print("====if statement=====")
age=20
if age>=18:
    print("you are eligible for voting")
print("====if-else statement=====")
age=17
if age>=18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")
print("====if-elif-else statement=====")
marks=75
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
else:
    print("grade C")
print("====nested if statement=====")
marks=85
if marks>=80:
    print("grade B")
    if marks>=90:
        print("excellent")
    else:
        print("good")
print("====Ternary operator=====")
age=20
status="eligible" if age>=18 else "not eligible"
print(status)
print("switch case statement")
day=2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")