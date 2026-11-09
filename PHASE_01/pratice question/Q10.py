print("====dictionary=====")
dictonary = {"name": "pushpa", "age": 20, "course": "CSE"}
print(dictonary)
print(type(dictonary))
print(dictonary["age"])
print("====dicionary value=====")
student = {"name": "pushpa", "age": 20, "course": "CSE"}
print(student.get("name"))
print(student.get("age"))
print("====updating dictionary=====")
student={"name": "pushpa", "age": 20, "course": "CSE"}
student ["age"]=21
print(student)
print("====methods of dictionary=====")
student={"name": "pushpa", "age": 20, "course": "CSE"}
print(student.keys())
print(student.values())
print(student.items())
print(student.pop("age"))
print(student.popitem())
print(student.clear())
print(student.copy())
print(student.update({"name": "sita"}))
print(student)
print(student.setdefault("age", 21))
print(student)
print(student.setdefault("gender", "female"))
print("====looping through dictionary=====")
student={"name": "pushpa", "age": 20, "course": "CSE"}
for key, value in student.items():
    print(key, ":", value)
    print("====nested dictonary=====")
    students={
      "student1": {"name": "pushpa", "age": 20, "course": "CSE"},
      "student2": {"name": "sita", "age": 21, "course": "ECE"},
    }
    print(students["student1"]["name"])
    print("====dictionary comprehension=====")
    squared_numbers = {x: x**2 for x in range(1, 6)}
    print(squared_numbers)