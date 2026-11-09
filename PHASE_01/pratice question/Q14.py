print("====file handaling=====")
file = open("student.txt", "w")

file.write("Name: Pushpa\n")
file.write("Course: B.Tech CSE")

file.close()
import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Pushpa", 20, "CSE"])
    writer.writerow(["Mohit", 21, "AI & ML"])
    import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
        import json

student = {
    "name": "Pushpa",
    "age": 20,
    "course": "CSE"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
    import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])