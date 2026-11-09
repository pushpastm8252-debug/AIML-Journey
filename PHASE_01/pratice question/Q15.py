print("====exception handaling======")
a = 10
b = 0

print(a / b)
try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

else:
    print("You entered:", num)