print("==== Loops =====")
print("==== for loop =====")
for i in range(5):
    print(i)
print("==== while loop =====")
i = 0
while i <= 5:
    print(i)
print("====break statement=====")
for i in range(10):
    if i == 5:
        break
    print(i)
print("====continue statement=====")
for i in range(10):
    if i == 5:
        continue
    print(i)
print("====pass statement=====")
for i in range(10):
    if i == 5:
        pass
    else:
        print(i)
print("====nested loop=====")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)