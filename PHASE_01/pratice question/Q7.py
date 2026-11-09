print("list methods")
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))
print(my_list[0])
print(my_list[-1])
print(my_list[2:5])
print("====list methods=====")
my_list = [1, 2, 3, 4, 5]
print(my_list.append(6))
print(my_list.insert(2, 1))
print(my_list.extend([7, 8, 9]))
print(my_list.remove(4))
print(my_list.pop())
print(my_list.index(3))
print(my_list.count(2))
print(my_list.sort())
print(my_list.reverse())
print(my_list.copy())
print(my_list.clear())
print(my_list.sort(reverse=True))
print("====list comprehension=====")
squares = [x**2 for x in range(10)]
print(squares)
print("====nested list=====")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])