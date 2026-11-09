# Phase 01 — Python Fundamentals: Complete Notes
Beginner to Advanced
Interview + Practical + Exam Preparation
These notes will take you from zero-level Python to advanced Python fundamentals. I'll explain every topic in simple English with Hinglish explanations, syntax, examples, outputs, important points, and interview questions.

How to study these notes:

1. Understand the concept.
2. Learn the syntax.
3. Run the code in VS Code or Jupyter Notebook.
4. Practice the examples yourself.
5. Revise the interview questions.

# 1. Variables & Data Types

## 1.1 What is Python?

Python is a high-level, interpreted, general-purpose programming language.

It is popular because its syntax is simple and easy to understand.
Example:

```
print("Hello, World!")
```

Output:

```
Hello, World!
```

Applications of Python:

- Artificial Intelligence (AI)
- Machine Learning (ML)
- Data Science
- Web Development
- Automation
- Game Development
- Cybersecurity

## 1.2 What is a Variable?

A variable is a named memory reference used to store a value.

Simple meaning: Variable ek container ki tarah hota hai jisme hum data store karte hain.

Syntax:

```
variable_name = value
```

Example:

```
name = "Pushpa"age = 20marks = 89.5print(name)print(age)print(marks)
```

Output:

```
Pushpa
20
89.5
```

### Rules for naming variables

1. Variable names can contain letters, numbers and underscores.
2. A variable cannot start with a number.
3. Spaces are not allowed.
4. Python keywords cannot be used.
5. Variable names are case-sensitive.

```
student_name = "Rahul"  # Validage2 = 20               # Valid_marks = 90             # Valid# 2age = 20              # Invalid# student name = "A"     # Invalid
```

### Multiple variable assignment

```
a, b, c = 10, 20, 30print(a)print(b)print(c)
```

Same value to multiple variables:

```
x = y = z = 100
```

## 1.3 What are Data Types?

Data types define the type of value a variable holds.

Python has several built-in data types.

| Data type | Meaning                       | Example         |
| --------- | ----------------------------- | --------------- |
| int       | Integer numbers               | `10`            |
| float     | Decimal numbers               | `10.5`          |
| complex   | Complex numbers               | `2+3j`          |
| str       | Text                          | `"Python"`      |
| bool      | True/False                    | `True`          |
| list      | Ordered, mutable collection   | `[1, 2, 3]`     |
| tuple     | Ordered, immutable collection | `(1, 2, 3)`     |
| set       | Unique elements               | `{1, 2, 3}`     |
| dict      | Key-value pairs               | `{"name": "A"}` |

### Example:

```
a = 10b = 10.5c = 2 + 3jd = "Python"e = Trueprint(type(a))print(type(b))print(type(c))print(type(d))print(type(e))
```

Output:

```
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'bool'>
```

## 1.4 Type Conversion

Type conversion means changing one data type into another.

There are two types:

1\. Implicit Type Conversion

Python automatically converts a value into another compatible type.

```
a = 10b = 5.5result = a + bprint(result)print(type(result))
```

Output:

```
15.5
<class 'float'>
```

2\. Explicit Type Conversion

The programmer manually converts a data type.

```
a = "100"b = int(a)print(b + 50)
```

Output:

```
150
```

Important conversion functions:

| Function  | Purpose            |
| --------- | ------------------ |
| `int()`   | Convert to integer |
| `float()` | Convert to float   |
| `str()`   | Convert to string  |
| `bool()`  | Convert to Boolean |
| `list()`  | Convert to list    |
| `tuple()` | Convert to tuple   |
| `set()`   | Convert to set     |

Important: `int("hello")` gives a `ValueError` because `"hello"` cannot be converted into an integer.

### Interview Questions

1. What is a variable?
2. What are Python data types?
3. What is dynamic typing?
4. What is the difference between implicit and explicit conversion?
5. Is Python case-sensitive?

# 2. Input / Output

## 2.1 What is Input?

Input means taking information from the user.

Python uses the `input()` function.

Syntax:

```
variable = input("Enter something: ")
```

Example:

```
name = input("Enter your name: ")print("Welcome", name)
```

Output:

```
Enter your name: Pushpa
Welcome Pushpa
```

Important: The `input()` function always returns a string by default.

Example:

```
age = input("Enter your age: ")print(type(age))
```

Output:

```
<class 'str'>
```

If you want a number, convert it:

```
age = int(input("Enter your age: "))print(age + 5)
```

## 2.2 What is Output?

Output means displaying information to the user.

Python uses the `print()` function.

```
print("Hello Python")print(100)print(10 + 20)
```

Output:

```
Hello Python
100
30
```

## 2.3 Important print() parameters

sep: Separates multiple values.

```
print("Python", "Java", "C++", sep=" | ")
```

Output:

```
Python | Java | C++
```

end: Controls what is printed at the end.

```
print("Hello", end=" ")print("World")
```

Output:

```
Hello World
```

## 2.4 Formatted Output (f-strings)

f-strings are used to insert variable values inside strings.

```
name = "Pushpa"age = 20print(f"My name is {name} and I am {age} years old.")
```

Output:

```
My name is Pushpa and I am 20 years old.
```

### Practice Program: Add Two Numbers

```
num1 = int(input("Enter first number: "))num2 = int(input("Enter second number: "))total = num1 + num2print(f"Sum = {total}")
```

### Interview Questions

1. What is the use of `input()`?
2. What is the default return type of input()?
3. What is the difference between `print()` and `input()`?
4. What is an f-string?
5. What are `sep` and `end`?

# 3. Operators

## 3.1 What are Operators?

Operators are symbols or keywords used to perform operations on values and variables.

Example:

```
a = 10b = 5print(a + b)
```

Here, `+` is an operator.

## 3.2 Types of Operators

### A. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning        | Example   | Result |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `10 + 5`  | 15     |
| `-`      | Subtraction    | `10 - 5`  | 5      |
| `*`      | Multiplication | `10 * 5`  | 50     |
| `/`      | Division       | `10 / 5`  | 2.0    |
| `//`     | Floor division | `11 // 2` | 5      |
| `%`      | Modulus        | `11 % 2`  | 1      |
| `**`     | Exponent       | `2 ** 3`  | 8      |

Example:

```
a = 11b = 2print(a / b)print(a // b)print(a % b)print(a ** b)
```

### B. Comparison Operators

Used to compare two values. The result is always Boolean (`True` or `False`).

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal to              |
| `!=`     | Not equal to          |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

```
a = 10b = 20print(a == b)  # Falseprint(a != b)  # Trueprint(a < b)   # True
```

### C. Logical Operators

Used to combine conditions.

| Operator | Meaning                                  |
| -------- | ---------------------------------------- |
| `and`    | True when both conditions are true       |
| `or`     | True when at least one condition is true |
| `not`    | Reverses the Boolean result              |

```
age = 20print(age > 18 and age < 60)print(age < 18 or age > 60)print(not(age > 18))
```

### D. Assignment Operators

Used to assign or update values.

| Operator | Example   | Equivalent   |
| -------- | --------- | ------------ |
| `=`      | `x = 5`   | Assign 5     |
| `+=`     | `x += 2`  | `x = x + 2`  |
| `-=`     | `x -= 2`  | `x = x - 2`  |
| `*=`     | `x *= 2`  | `x = x * 2`  |
| `/=`     | `x /= 2`  | `x = x / 2`  |
| `//=`    | `x //= 2` | `x = x // 2` |
| `%=`     | `x %= 2`  | `x = x % 2`  |
| `**=`    | `x **= 2` | `x = x ** 2` |

### E. Membership Operators

Check whether an element exists inside a sequence or collection.

- `in`
- `not in`

```
languages = ["Python", "Java", "C++"]print("Python" in languages)print("PHP" not in languages)
```

Output:

```
True
True
```

### F. Identity Operators

Check whether two variables refer to the same object.

- `is`
- `is not`

```
a = [1, 2, 3]b = ac = [1, 2, 3]print(a is b)  # Trueprint(a is c)  # Falseprint(a == c)  # True
```

Important difference:

- `==` compares values.
- `is` compares object identity.

### G. Bitwise Operators

Work on the binary representation of integers.

\| Operator | Meaning |\
\|---|---|\
\| `&` | AND |\
\| `|` | OR |\
\| `^` | XOR |\
\| `~` | NOT |\
\| `<<` | Left shift |\
\| `>>` | Right shift |

Example:

```
a = 5b = 3print(a & b)print(a | b)print(a ^ b)print(a << 1)
```

Output:

```
1
7
6
10
```

### Interview Questions

1. What are operators?
2. Difference between `/` and `//`?
3. Difference between `==` and `is`?
4. Difference between `and` and `or`?
5. What are membership operators?

# 4. Conditions (Decision Making)

## 4.1 What are Conditional Statements?

Conditional statements allow a program to make decisions based on conditions.

Simple meaning: Agar condition true hai toh ek task perform hoga, otherwise doosra task perform hoga.

Python provides:

1. `if`
2. `if-else`
3. `if-elif-else`
4. Nested if

## 4.2 if Statement

Executes code only when the condition is true.

```
age = 20if age >= 18:    print("You are eligible to vote.")
```

Output:

```
You are eligible to vote.
```

## 4.3 if-else Statement

Executes one block if true and another if false.

```
age = 16if age >= 18:    print("Eligible")else:    print("Not Eligible")
```

Output:

```
Not Eligible
```

## 4.4 if-elif-else Statement

Used when multiple conditions need to be checked.

```
marks = 85if marks >= 90:    print("Grade A+")elif marks >= 80:    print("Grade A")elif marks >= 70:    print("Grade B")elif marks >= 60:    print("Grade C")else:    print("Fail")
```

Output:

```
Grade A
```

## 4.5 Nested if

An if statement inside another if statement.

```
age = 20has_id = Trueif age >= 18:    if has_id:        print("Entry allowed")    else:        print("ID required")else:    print("Underage")
```

## 4.6 Ternary Operator

A short way to write if-else.

```
age = 20result = "Adult" if age >= 18 else "Minor"print(result)
```

Output:

```
Adult
```

## 4.7 Match-Case (Python 3.10+)

Used for matching a value against multiple patterns.

```
day = 2match day:    case 1:        print("Monday")    case 2:        print("Tuesday")    case 3:        print("Wednesday")    case _:        print("Invalid day")
```

### Practice Programs

- Check positive, negative or zero.
- Check even or odd.
- Find the largest of three numbers.
- Check leap year.
- Create a simple calculator using conditions.

### Interview Questions

1. What is an if statement?
2. Difference between if-else and if-elif-else?
3. What is nested if?
4. What is a ternary operator?
5. What is match-case?

# 5. Loops

## 5.1 What are Loops?

Loops are used to execute a block of code repeatedly.

Simple meaning: Jab hume same task baar-baar perform karna hota hai, tab hum loops use karte hain.

Python has two main loops:

- `for` loop
- `while` loop

## 5.2 for Loop

Used to iterate over a sequence such as a string, list, tuple or range.

Syntax:

```
for variable in sequence:    statements
```

Example:

```
for i in range(1, 6):    print(i)
```

Output:

```
1
2
3
4
5
```

### Understanding range()

`range()` generates a sequence of integers.

```
range(start, stop, step)
```

- Start: Starting value (included).
- Stop: Ending value (excluded).
- Step: Difference between values.

Example:

```
for i in range(2, 11, 2):    print(i)
```

Output:

```
2
4
6
8
10
```

## 5.3 while Loop

Repeats code as long as the condition remains true.

Syntax:

```
while condition:    statements
```

Example:

```
i = 1while i <= 5:    print(i)    i += 1
```

Output:

```
1
2
3
4
5
```

Important: Always update the loop variable when needed. Otherwise, an infinite loop may occur.

## 5.4 break Statement

Terminates the loop immediately.

```
for i in range(1, 6):    if i == 3:        break    print(i)
```

Output:

```
1
2
```

## 5.5 continue Statement

Skips the current iteration and moves to the next iteration.

```
for i in range(1, 6):    if i == 3:        continue    print(i)
```

Output:

```
1
2
4
5
```

## 5.6 pass Statement

Does nothing. It is used as a placeholder.

```
for i in range(5):    pass
```

## 5.7 Nested Loops

A loop inside another loop.

```
for i in range(1, 4):    for j in range(1, 4):        print(i, j)
```

## 5.8 Loop with else

Python supports an `else` block with loops. It executes when the loop completes normally, not when it exits through `break`.

```
for i in range(1, 4):    print(i)else:    print("Loop completed")
```

### Important Pattern Programs

Square pattern:

```
for i in range(4):    for j in range(4):        print("*", end=" ")    print()
```

Output:

```
* * * *
* * * *
* * * *
* * * *
```

Right triangle pattern:

```
for i in range(1, 5):    print("* " * i)
```

Output:

```
*
* *
* * *
* * * *
```

Multiplication table:

```
num = 5for i in range(1, 11):    print(f"{num} x {i} = {num * i}")
```

### Interview Questions

1. What is a loop?
2. Difference between for and while loops?
3. Difference between break and continue?
4. What is an infinite loop?
5. What is a nested loop?
6. What is the use of pass?

# 6. Strings

## 6.1 What is a String?

A string is a sequence of characters enclosed in single, double or triple quotes.

```
name = "Python"city = 'Meerut'message = """Welcome to Python Programming"""print(name)print(city)print(message)
```

Strings are immutable, which means their individual characters cannot be changed after creation.

## 6.2 String Indexing

Each character has an index.

```
text = "PYTHON"
```

Positive indexing

P

0

Y

1

T

2

H

3

O

4

N

5

Negative indexing

P

-6

Y

-5

T

-4

H

-3

O

-2

N

-1

Example:

```
text = "PYTHON"print(text[0])print(text[2])print(text[-1])
```

Output:

```
P
T
N
```

## 6.3 String Slicing

Slicing is used to extract a part of a string.

Syntax:

```
string[start:stop:step]
```

Example:

```
text = "PYTHON"print(text[0:3])print(text[2:5])print(text[::-1])
```

Output:

```
PYT
THO
NOHTYP
```

## 6.4 Important String Methods

| Method         | Purpose                             |
| -------------- | ----------------------------------- |
| `upper()`      | Convert to uppercase                |
| `lower()`      | Convert to lowercase                |
| `title()`      | Capitalize each word                |
| `capitalize()` | Capitalize first character          |
| `strip()`      | Remove surrounding whitespace       |
| `replace()`    | Replace text                        |
| `split()`      | Split into a list                   |
| `join()`       | Join strings                        |
| `find()`       | Find substring position             |
| `count()`      | Count occurrences                   |
| `startswith()` | Check starting text                 |
| `endswith()`   | Check ending text                   |
| `isdigit()`    | Check if all characters are digits  |
| `isalpha()`    | Check if all characters are letters |

Example:

```
text = "  hello python  "print(text.upper())print(text.lower())print(text.strip())print(text.replace("python", "world"))print(text.strip().title())
```

## 6.5 String Concatenation

Joining strings using `+`.

```
first = "Hello"second = "Python"result = first + " " + secondprint(result)
```

Output:

```
Hello Python
```

## 6.6 String Repetition

```
print("Python " * 3)
```

Output:

```
Python Python Python
```

### Practice Programs

1. Reverse a string.
2. Check palindrome.
3. Count vowels and consonants.
4. Count words in a sentence.
5. Find the frequency of each character.
6. Remove spaces from a string.

Palindrome example:

```
text = "madam"if text == text[::-1]:    print("Palindrome")else:    print("Not Palindrome")
```

### Interview Questions

1. What is a string?
2. Are strings mutable or immutable?
3. What is indexing?
4. What is slicing?
5. Difference between `find()` and `index()`?
6. Difference between `split()` and `join()`?

# 7. Lists

## 7.1 What is a List?

A list is an ordered collection of elements. It allows duplicate values and can store different data types.

Lists are mutable, meaning we can modify their elements after creation.

Syntax:

```
list_name = [element1, element2, element3]
```

Example:

```
students = ["Pushpa", "Mohit", "Rahul"]print(students)print(type(students))
```

Output:

```
['Pushpa', 'Mohit', 'Rahul']
<class 'list'>
```

## 7.2 Characteristics of Lists

1. Ordered collection.
2. Mutable.
3. Allows duplicate values.
4. Supports indexing.
5. Supports slicing.
6. Can store different data types.
7. Can contain nested lists.

```
data = [10, "Python", 20.5, True]
```

## 7.3 Accessing List Elements

```
numbers = [10, 20, 30, 40, 50]print(numbers[0])print(numbers[2])print(numbers[-1])
```

Output:

```
10
30
50
```

## 7.4 List Slicing

```
numbers = [10, 20, 30, 40, 50]print(numbers[1:4])print(numbers[:3])print(numbers[::2])print(numbers[::-1])
```

Output:

```
[20, 30, 40]
[10, 20, 30]
[10, 30, 50]
[50, 40, 30, 20, 10]
```

## 7.5 Important List Methods

| Method      | Purpose                            |
| ----------- | ---------------------------------- |
| `append()`  | Add one element at the end         |
| `extend()`  | Add multiple elements              |
| `insert()`  | Add an element at a specific index |
| `remove()`  | Remove first matching element      |
| `pop()`     | Remove and return an element       |
| `clear()`   | Remove all elements                |
| `index()`   | Return the index of an element     |
| `count()`   | Count occurrences                  |
| `sort()`    | Sort the list                      |
| `reverse()` | Reverse the list                   |
| `copy()`    | Create a shallow copy              |

Example:

```
numbers = [10, 20, 30]numbers.append(40)print(numbers)numbers.insert(1, 15)print(numbers)numbers.remove(20)print(numbers)numbers.pop()print(numbers)
```

Output:

```
[10, 20, 30, 40]
[10, 15, 20, 30, 40]
[10, 15, 30, 40]
[10, 15, 30]
```

## 7.6 List Mutability

```
numbers = [10, 20, 30]numbers[0] = 100print(numbers)
```

Output:

```
[100, 20, 30]
```

## 7.7 List Comprehension

List comprehension provides a short way to create lists.

Syntax:

```
new_list = [expression for item in iterable]
```

Example:

```
squares = [x**2 for x in range(1, 6)]print(squares)
```

Output:

```
[1, 4, 9, 16, 25]
```

With condition:

```
even_numbers = [x for x in range(1, 11) if x % 2 == 0]print(even_numbers)
```

Output:

```
[2, 4, 6, 8, 10]
```

## 7.8 Nested Lists

A list inside another list.

```
matrix = [    [1, 2, 3],    [4, 5, 6],    [7, 8, 9]]print(matrix[0])print(matrix[1][2])
```

Output:

```
[1, 2, 3]
6
```

### Practical Example: Find the Largest Number

```
numbers = [10, 45, 20, 90, 35]largest = max(numbers)print("Largest number:", largest)
```

Output:

```
Largest number: 90
```

### Interview Questions

1. What is a list?
2. Why are lists mutable?
3. Difference between `append()` and `extend()`?
4. Difference between `remove()` and `pop()`?
5. What is list comprehension?
6. What is a nested list?
7. What is the difference between `sort()` and `sorted()`?

# 8. Tuples

## 8.1 What is a Tuple?

A tuple is an ordered collection of elements that cannot be modified after creation.

Tuples are immutable.

Syntax:

```
tuple_name = (element1, element2, element3)
```

Example:

```
student = ("Pushpa", 20, "CSE")print(student)print(type(student))
```

Output:

```
('Pushpa', 20, 'CSE')
<class 'tuple'>
```

## 8.2 Characteristics of Tuples

- Ordered.
- Immutable.
- Allows duplicate elements.
- Supports indexing.
- Supports slicing.
- Can contain different data types.

## 8.3 Accessing Tuple Elements

```
numbers = (10, 20, 30, 40)print(numbers[0])print(numbers[-1])
```

## 8.4 Tuple Methods

Tuples have two main built-in methods:

| Method    | Purpose               |
| --------- | --------------------- |
| `count()` | Counts an element     |
| `index()` | Finds the first index |

Example:

```
numbers = (10, 20, 10, 30, 10)print(numbers.count(10))print(numbers.index(20))
```

Output:

```
3
1
```

## 8.5 Single Element Tuple

A single-element tuple must have a comma.

```
a = (10,)print(type(a))
```

Output:

```
<class 'tuple'>
```

Without a comma:

```
a = (10)print(type(a))
```

Output:

```
<class 'int'>
```

## 8.6 Tuple Packing and Unpacking

Packing: Putting multiple values into a tuple.

```
student = "Pushpa", 20, "CSE"
```

Unpacking: Assigning tuple elements to separate variables.

```
student = ("Pushpa", 20, "CSE")name, age, course = studentprint(name)print(age)print(course)
```

## 8.7 Tuple vs List

| Feature    | List            | Tuple            |
| ---------- | --------------- | ---------------- |
| Brackets   | `[]`            | `()`             |
| Mutable    | Yes             | No               |
| Ordered    | Yes             | Yes              |
| Duplicates | Allowed         | Allowed          |
| Methods    | More methods    | Two main methods |
| Use        | Changeable data | Fixed data       |

### Interview Questions

1. What is a tuple?
2. Why are tuples immutable?
3. Difference between tuple and list?
4. How do you create a single-element tuple?
5. What are tuple packing and unpacking?

# 9. Sets

## 9.1 What is a Set?

A set is an unordered collection of unique elements.

It automatically removes duplicate values.

Syntax:

```
set_name = {element1, element2, element3}
```

Example:

```
numbers = {10, 20, 30, 20, 10}print(numbers)
```

Output (order may vary):

```
{10, 20, 30}
```

## 9.2 Characteristics of Sets

- Unordered collection.
- No duplicate elements.
- Mutable collection.
- Does not support indexing or slicing.
- Elements must be hashable.
- Can perform mathematical set operations.

## 9.3 Creating an Empty Set

```
a = set()b = {}print(type(a))print(type(b))
```

Output:

```
<class 'set'>
<class 'dict'>
```

Remember: `{}` creates an empty dictionary, not an empty set.

## 9.4 Important Set Methods

| Method      | Purpose                                      |
| ----------- | -------------------------------------------- |
| `add()`     | Add one element                              |
| `update()`  | Add multiple elements                        |
| `remove()`  | Remove an element; raises KeyError if absent |
| `discard()` | Remove an element; no error if absent        |
| `pop()`     | Remove and return an arbitrary element       |
| `clear()`   | Remove all elements                          |
| `copy()`    | Create a shallow copy                        |

Example:

```
numbers = {10, 20, 30}numbers.add(40)print(numbers)numbers.update([50, 60])print(numbers)numbers.discard(20)print(numbers)
```

## 9.5 Set Operations

Consider:

```
A = {1, 2, 3, 4}B = {3, 4, 5, 6}
```

A. Union

Combines all unique elements.

```
print(A | B)print(A.union(B))
```

Output:

```
{1, 2, 3, 4, 5, 6}
```

B. Intersection

Returns common elements.

```
print(A & B)print(A.intersection(B))
```

Output:

```
{3, 4}
```

C. Difference

Returns elements present in the first set but not in the second.

```
print(A - B)
```

Output:

```
{1, 2}
```

D. Symmetric Difference

Returns elements that are present in either set but not both.

```
print(A ^ B)
```

Output:

```
{1, 2, 5, 6}
```

E. Subset

```
A = {1, 2}B = {1, 2, 3, 4}print(A.issubset(B))
```

Output:

```
True
```

F. Superset

```
print(B.issuperset(A))
```

Output:

```
True
```

### Practical Example: Remove Duplicates

```
numbers = [10, 20, 10, 30, 20, 40]unique_numbers = list(set(numbers))print(unique_numbers)
```

Note: This removes duplicates, but the original ordering is not guaranteed.

### Interview Questions

1. What is a set?
2. Why doesn't a set allow duplicates?
3. Difference between `remove()` and `discard()`?
4. Difference between union and intersection?
5. Can we access set elements using indexing?
6. Difference between set and frozen set?

# 10. Dictionaries

## 10.1 What is a Dictionary?

A dictionary is a collection of data stored in key-value pairs.

Simple meaning: Har value ko access karne ke liye ek unique key hoti hai.

Syntax:

```
dictionary = {    "key1": "value1",    "key2": "value2"}
```

Example:

```
student = {    "name": "Pushpa",    "age": 20,    "course": "B.Tech CSE",    "marks": 90}print(student)print(student["name"])print(student["age"])
```

Output:

```
{'name': 'Pushpa', 'age': 20, 'course': 'B.Tech CSE', 'marks': 90}
Pushpa
20
```

## 10.2 Characteristics of Dictionaries

- Store data as key-value pairs.
- Mutable.
- Keys must be unique.
- Values can be duplicated.
- Keys must be hashable.
- Maintain insertion order in modern Python.

## 10.3 Accessing Dictionary Values

```
student = {    "name": "Pushpa",    "age": 20}print(student["name"])print(student.get("age"))print(student.get("city", "Not found"))
```

Important difference:

- `student["city"]` raises `KeyError` if the key does not exist.
- `student.get("city")` returns `None` by default.

## 10.4 Adding and Updating Values

```
student = {    "name": "Pushpa",    "age": 20}student["city"] = "Meerut"student["age"] = 21print(student)
```

## 10.5 Removing Dictionary Elements

```
student = {    "name": "Pushpa",    "age": 20,    "city": "Meerut"}student.pop("age")print(student)
```

Other methods:

```
student.popitem()  # Removes last inserted pairstudent.clear()    # Removes all pairs
```

## 10.6 Important Dictionary Methods

| Method         | Purpose                            |
| -------------- | ---------------------------------- |
| `keys()`       | Returns keys                       |
| `values()`     | Returns values                     |
| `items()`      | Returns key-value pairs            |
| `get()`        | Safely accesses a value            |
| `update()`     | Updates dictionary                 |
| `pop()`        | Removes a specified key            |
| `popitem()`    | Removes last inserted pair         |
| `setdefault()` | Returns value or inserts a default |
| `copy()`       | Creates a shallow copy             |
| `clear()`      | Removes all elements               |

Example:

```
student = {    "name": "Pushpa",    "age": 20,    "course": "CSE"}print(student.keys())print(student.values())print(student.items())
```

## 10.7 Looping Through a Dictionary

```
student = {    "name": "Pushpa",    "age": 20,    "course": "CSE"}for key, value in student.items():    print(key, ":", value)
```

## 10.8 Nested Dictionary

A dictionary inside another dictionary.

```
students = {    "student1": {        "name": "Pushpa",        "age": 20    },    "student2": {        "name": "Mohit",        "age": 21    }}print(students["student1"]["name"])
```

Output:

```
Pushpa
```

## 10.9 Dictionary Comprehension

```
squares = {x: x**2 for x in range(1, 6)}print(squares)
```

Output:

```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Practical Example: Student Marks

```
marks = {    "Python": 90,    "Java": 85,    "DBMS": 88}total = sum(marks.values())average = total / len(marks)print("Total:", total)print("Average:", average)
```

### Interview Questions

1. What is a dictionary?
2. Can dictionary keys be duplicated?
3. Difference between `get()` and square-bracket access?
4. What are `keys()`, `values()` and `items()`?
5. What is a nested dictionary?
6. What is dictionary comprehension?

# 11. Functions

## 11.1 What is a Function?

A function is a reusable block of code designed to perform a particular task.

Simple meaning: Ek baar code likho aur zarurat padne par use baar-baar call karo.

Advantages:

- Code reusability.
- Better readability.
- Less repetition.
- Easier debugging.
- Better program organization.

## 11.2 Defining a Function

Python uses the `def` keyword.

Syntax:

```
def function_name():    statements
```

Example:

```
def greet():    print("Hello, Welcome to Python!")greet()
```

Output:

```
Hello, Welcome to Python!
```

## 11.3 Function with Parameters

Parameters are variables written in the function definition.

```
def greet(name):    print("Hello", name)greet("Pushpa")
```

Output:

```
Hello Pushpa
```

## 11.4 Function with Return Statement

The `return` statement sends a result back to the caller.

```
def add(a, b):    return a + bresult = add(10, 20)print(result)
```

Output:

```
30
```

Difference between print and return:

- `print()` displays information.
- `return` sends a value back to the calling code.

## 11.5 Types of Function Arguments

A. Positional Arguments

Values are passed according to their position.

```
def student(name, age):    print(name, age)student("Pushpa", 20)
```

B. Keyword Arguments

Values are passed using parameter names.

```
student(age=20, name="Pushpa")
```

C. Default Arguments

A parameter has a default value.

```
def greet(name="Student"):    print("Hello", name)greet()greet("Pushpa")
```

Output:

```
Hello Student
Hello Pushpa
```

\*D. Variable-Length Arguments: args

Allows a function to accept multiple positional arguments.

```
def total(*numbers):    print(sum(numbers))total(10, 20)total(10, 20, 30, 40)
```

\*\*E. Variable-Length Keyword Arguments: kwargs

Allows a function to accept multiple keyword arguments.

```
def student_info(**details):    for key, value in details.items():        print(key, value)student_info(name="Pushpa", age=20, course="CSE")
```

## 11.6 Scope of Variables

Scope determines where a variable can be accessed.

Local Variable: Created inside a function.

```
def show():    x = 10    print(x)show()
```

Global Variable: Created outside a function.

```
x = 100def show():    print(x)show()
```

global keyword: Used to reassign a global variable inside a function.

```
x = 10def change():    global x    x = 50change()print(x)
```

Output:

```
50
```

nonlocal keyword: Used in nested functions to refer to a variable in the nearest enclosing function scope.

```
def outer():    x = 10    def inner():        nonlocal x        x = 20    inner()    print(x)outer()
```

Output:

```
20
```

## 11.7 Lambda Functions

A lambda is a small anonymous function written in one expression.

Syntax:

```
lambda arguments: expression
```

Example:

```
square = lambda x: x * xprint(square(5))
```

Output:

```
25
```

## 11.8 map(), filter() and reduce()

map(): Applies a function to every element.

```
numbers = [1, 2, 3, 4]result = list(map(lambda x: x * 2, numbers))print(result)
```

Output:

```
[2, 4, 6, 8]
```

filter(): Selects elements satisfying a condition.

```
numbers = [1, 2, 3, 4, 5, 6]result = list(filter(lambda x: x % 2 == 0, numbers))print(result)
```

Output:

```
[2, 4, 6]
```

reduce(): Combines elements into a single result.

```
from functools import reducenumbers = [1, 2, 3, 4]result = reduce(lambda a, b: a + b, numbers)print(result)
```

Output:

```
10
```

## 11.9 Docstrings

Docstrings explain what a function does.

```
def add(a, b):    """This function adds two numbers."""    return a + bprint(add.__doc__)
```

### Interview Questions

1. What is a function?
2. Difference between parameter and argument?
3. Difference between print and return?
4. What are \*args and \*\*kwargs?
5. What is lambda?
6. What is variable scope?
7. Difference between local and global variables?
8. What are map(), filter() and reduce()?

# 12. Recursion

## 12.1 What is Recursion?

Recursion is a programming technique in which a function calls itself to solve a smaller version of the same problem.

Simple meaning: Ek function apne aap ko call karta hai.

Every proper recursive solution needs:

1. Base Case: Stops recursion.
2. Recursive Case: Calls the function again with a smaller or simpler problem.

## 12.2 Example: Countdown

```
def countdown(n):    if n == 0:        print("Finished")        return    print(n)    countdown(n - 1)countdown(5)
```

Output:

```
5
4
3
2
1
Finished
```

## 12.3 Factorial Using Recursion

Factorial:

\\[ n! = n \times (n-1) \times \cdots \times 1 \\]

And:

\\[ 0! = 1 \\]

Code:

```
def factorial(n):    if n < 0:        raise ValueError("Factorial is not defined for negative integers")    if n == 0 or n == 1:        return 1    return n * factorial(n - 1)print(factorial(5))
```

Output:

```
120
```

### Dry Run

| Function call | Calculation      |
| ------------- | ---------------- |
| factorial(5)  | 5 × factorial(4) |
| factorial(4)  | 4 × factorial(3) |
| factorial(3)  | 3 × factorial(2) |
| factorial(2)  | 2 × factorial(1) |
| factorial(1)  | 1                |

Returning:

\\[ 5 \times 4 \times 3 \times 2 \times 1 = 120 \\]

## 12.4 Fibonacci Series Using Recursion

```
def fibonacci(n):    if n <= 1:        return n    return fibonacci(n - 1) + fibonacci(n - 2)for i in range(7):    print(fibonacci(i), end=" ")
```

Output:

```
0 1 1 2 3 5 8
```

## 12.5 Advantages of Recursion

- Makes some problems easier to express.
- Useful in tree and graph algorithms.
- Useful in divide-and-conquer algorithms.
- Can reduce complex code.

## 12.6 Disadvantages of Recursion

- Function-call overhead.
- Uses call stack memory.
- Can be slower than iteration.
- Deep recursion can cause `RecursionError`.

### Recursion vs Iteration

| Recursion                 | Iteration                               |
| ------------------------- | --------------------------------------- |
| Function calls itself     | Uses loops                              |
| Uses call stack           | Usually uses less stack memory          |
| Can be elegant for trees  | Often efficient for repeated operations |
| May reach recursion limit | Depends on loop termination             |

### Interview Questions

1. What is recursion?
2. What is a base case?
3. What is a recursive case?
4. What is stack overflow?
5. Difference between recursion and iteration?
6. What is the time complexity of naive recursive Fibonacci?

# 13. Modules & Packages

## 13.1 What is a Module?

A module is a Python file containing reusable code, such as functions, variables and classes.

Example: `math`, `random`, `datetime`.

## 13.2 Importing a Module

```
import mathprint(math.sqrt(25))print(math.pi)
```

Output:

```
5.0
3.141592653589793
```

## 13.3 Import Specific Functions

```
from math import sqrt, factorialprint(sqrt(36))print(factorial(5))
```

## 13.4 Using an Alias

```
import math as mprint(m.sqrt(49))
```

## 13.5 Creating Your Own Module

Create two Python files:

```
Python_Project/
│
├── main.py
└── calculator.py
```

calculator.py

```
def add(a, b):    return a + bdef subtract(a, b):    return a - b
```

main.py

```
import calculatorprint(calculator.add(10, 20))print(calculator.subtract(20, 5))
```

Output:

```
30
15
```

## 13.6 What is a Package?

A package is a way of organizing related Python modules into directories.

Example:

```
my_package/
│
├── __init__.py
├── calculator.py
└── message.py
```

Import example:

```
from my_package.calculator import add
```

`__init__.py` is commonly used to mark a regular Python package and can contain package initialization code. Modern Python also supports namespace packages without it.

## 13.7 Important Built-in Modules

| Module        | Purpose                        |
| ------------- | ------------------------------ |
| `math`        | Mathematical operations        |
| `random`      | Random values                  |
| `datetime`    | Date and time                  |
| `os`          | Operating system interactions  |
| `sys`         | Python interpreter information |
| `statistics`  | Statistical calculations       |
| `json`        | JSON data handling             |
| `re`          | Regular expressions            |
| `collections` | Specialized containers         |
| `pathlib`     | File system paths              |

Example:

```
import randomnumber = random.randint(1, 10)print(number)
```

Output: Any random integer from 1 to 10.

## 13.8 pip

`pip` is the standard Python package installer.

Install a package:

```
pip install numpy
```

Install multiple packages:

```
pip install pandas matplotlib scikit-learn
```

View installed packages:

```
pip list
```

Save dependencies:

```
pip freeze > requirements.txt
```

Install dependencies:

```
pip install -r requirements.txt
```

## 13.9 Virtual Environment

A virtual environment creates an isolated Python environment for a project.

Windows PowerShell:

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Deactivate:

```
deactivate
```

### Interview Questions

1. What is a module?
2. What is a package?
3. Difference between module and package?
4. What is pip?
5. What is a virtual environment?
6. What is the use of `__init__.py`?
7. Difference between `import math` and `from math import sqrt`?

# 14. File Handling

## 14.1 What is File Handling?

File handling allows Python programs to create, read, write and modify files.

Examples:

- Text files.
- CSV files.
- JSON files.
- Binary files.

## 14.2 Opening a File

Python uses the `open()` function.

Syntax:

```
file = open("filename.txt", "mode")
```

## 14.3 File Opening Modes

| Mode | Meaning                                 |
| ---- | --------------------------------------- |
| `r`  | Read                                    |
| `w`  | Write; overwrites existing contents     |
| `a`  | Append                                  |
| `x`  | Create; fails if file exists            |
| `b`  | Binary mode                             |
| `t`  | Text mode (default)                     |
| `r+` | Read and write                          |
| `w+` | Write and read; truncates existing file |
| `a+` | Append and read                         |

## 14.4 Writing into a File

```
file = open("student.txt", "w")file.write("Name: Pushpa\n")file.write("Course: B.Tech CSE")file.close()
```

This creates the file if it doesn't exist and replaces its previous content if it does.

## 14.5 Reading a File

```
file = open("student.txt", "r")content = file.read()print(content)file.close()
```

## 14.6 read(), readline() and readlines()

```
file.read()       # Reads all remaining contentfile.readline()   # Reads one linefile.readlines()  # Returns remaining lines as a list
```

Example:

```
with open("student.txt", "r") as file:    print(file.readline())
```

## 14.7 Appending Data

```
with open("student.txt", "a") as file:    file.write("\nLearning Python")
```

## 14.8 The with Statement

The `with` statement manages the file automatically and closes it when the block exits.

```
with open("student.txt", "r") as file:    content = file.read()    print(content)
```

This is the recommended approach for ordinary file operations.

## 14.9 File Pointer Methods

- `tell()` returns the current file position.
- `seek()` moves the file position.

```
with open("student.txt", "r") as file:    print(file.tell())    file.read(5)    print(file.tell())    file.seek(0)    print(file.read())
```

## 14.10 Working with CSV Files

CSV means Comma-Separated Values.

```
import csvwith open("students.csv", "w", newline="") as file:    writer = csv.writer(file)    writer.writerow(["Name", "Age", "Course"])    writer.writerow(["Pushpa", 20, "CSE"])    writer.writerow(["Mohit", 21, "AI & ML"])
```

Reading CSV:

```
import csvwith open("students.csv", "r") as file:    reader = csv.reader(file)    for row in reader:        print(row)
```

## 14.11 Working with JSON

JSON means JavaScript Object Notation. It is commonly used to store and exchange structured data.

```
import jsonstudent = {    "name": "Pushpa",    "age": 20,    "course": "CSE"}with open("student.json", "w") as file:    json.dump(student, file, indent=4)
```

Reading JSON:

```
import jsonwith open("student.json", "r") as file:    data = json.load(file)print(data["name"])
```

### Interview Questions

1. What is file handling?
2. What are file modes?
3. Difference between `w` and `a`?
4. Difference between `read()` and `readline()`?
5. Why is `with open()` preferred?
6. What is the use of CSV and JSON?
7. What are `seek()` and `tell()`?

# 15. Exception Handling

## 15.1 What is an Exception?

An exception is an error that occurs while a program is running and interrupts its normal execution.

Example:

```
a = 10b = 0print(a / b)
```

Output:

```
ZeroDivisionError: division by zero
```

Instead of allowing the program to crash unexpectedly, we can handle exceptions.

## 15.2 Types of Errors

1\. Syntax Error

Occurs when Python syntax rules are violated.

```
# Missing closing bracketprint("Hello"
```

2\. Runtime Error / Exception

Occurs during program execution.

```
print(10 / 0)
```

3\. Logical Error

The program runs but produces an incorrect result.

```
a = 10b = 20# Wrong formula for additionresult = a - bprint(result)
```

## 15.3 try and except

- `try`: Contains code that may cause an exception.
- `except`: Handles the exception.

```
try:    a = 10    b = 0    result = a / b    print(result)except ZeroDivisionError:    print("Cannot divide by zero!")
```

Output:

```
Cannot divide by zero!
```

## 15.4 Multiple Except Blocks

```
try:    num = int(input("Enter a number: "))    result = 100 / num    print(result)except ValueError:    print("Please enter a valid integer.")except ZeroDivisionError:    print("Number cannot be zero.")
```

## 15.5 else Block

The `else` block executes when no exception occurs in the `try` block.

```
try:    num = int(input("Enter number: "))except ValueError:    print("Invalid input")else:    print("You entered:", num)
```

## 15.6 finally Block

The `finally` block executes whether an exception occurs or not, barring unusual termination of the process.

```
try:    print("Program started")    result = 10 / 2    print(result)except ZeroDivisionError:    print("Error occurred")finally:    print("Program completed")
```

Output:

```
Program started
5.0
Program completed
```

## 15.7 raise Keyword

The `raise` keyword is used to manually generate an exception.

```
age = 15if age < 18:    raise ValueError("Age must be 18 or above")print("Eligible")
```

## 15.8 Custom Exceptions

We can create our own exception classes.

```
class InvalidAgeError(Exception):    passdef check_age(age):    if age < 18:        raise InvalidAgeError("You must be 18 or older")    return "Access granted"try:    print(check_age(16))except InvalidAgeError as e:    print(e)
```

Output:

```
You must be 18 or older
```

## 15.9 Common Python Exceptions

| Exception             | Meaning                          |
| --------------------- | -------------------------------- |
| `ValueError`          | Correct type but invalid value   |
| `TypeError`           | Unsupported operation for a type |
| `NameError`           | Variable or name not defined     |
| `IndexError`          | Invalid sequence index           |
| `KeyError`            | Dictionary key not found         |
| `ZeroDivisionError`   | Division by zero                 |
| `FileNotFoundError`   | File does not exist              |
| `ImportError`         | Import operation failed          |
| `AttributeError`      | Attribute does not exist         |
| `ModuleNotFoundError` | Module cannot be found           |

### Interview Questions

1. What is exception handling?
2. Difference between syntax error and exception?
3. What is try-except?
4. What is the use of finally?
5. Difference between raise and assert?
6. What is a custom exception?
7. Why should we avoid using a bare `except:` unnecessarily?

# 16. Object-Oriented Programming (OOP)

Very Important for Interviews

## 16.1 What is OOP?

Object-Oriented Programming is a programming approach based on classes and objects.

It helps organize code into reusable structures.

Simple meaning: Real-world objects ko programming ke through represent karna OOP kehlata hai.

Real-world example:

Consider a car.

- Properties: Color, model, speed.
- Behaviours: Start, stop, accelerate.

In Python, we can represent this using a class and object.

## 16.2 What is a Class?

A class is a blueprint or template used to create objects.

Syntax:

```
class ClassName:    # Attributes    # Methods
```

Example:

```
class Student:    name = "Pushpa"    age = 20    def display(self):        print(self.name)        print(self.age)
```

## 16.3 What is an Object?

An object is an instance of a class.

```
class Student:    def display(self):        print("Hello Student")s1 = Student()s1.display()
```

Output:

```
Hello Student
```

Here:

- `Student` is a class.
- `s1` is an object.
- `display()` is a method.

## 16.4 Constructor: init()

A constructor is a special method that initializes an object when it is created.

```
class Student:    def __init__(self, name, age):        self.name = name        self.age = age    def display(self):        print("Name:", self.name)        print("Age:", self.age)s1 = Student("Pushpa", 20)s2 = Student("Mohit", 21)s1.display()s2.display()
```

Output:

```
Name: Pushpa
Age: 20
Name: Mohit
Age: 21
```

## 16.5 What is self?

`self` refers to the current instance of the class.

It is used to access instance attributes and methods.

```
class Student:    def __init__(self, name):        self.name = name    def show(self):        print(self.name)s1 = Student("Pushpa")s1.show()
```

Important: `self` is a conventional parameter name, not a Python keyword. It is supplied automatically when an instance method is called through an object.

## 16.6 Types of Variables in Classes

A. Instance Variables

Belong to individual objects.

```
class Student:    def __init__(self, name):        self.name = names1 = Student("Pushpa")s2 = Student("Mohit")print(s1.name)print(s2.name)
```

B. Class Variables

Shared by all instances unless overridden on an instance.

```
class Student:    college = "Shobhit University"    def __init__(self, name):        self.name = names1 = Student("Pushpa")s2 = Student("Mohit")print(s1.college)print(s2.college)
```

## 16.7 Types of Methods

1\. Instance Method

Works with instance data.

```
class Student:    def show(self):        print("Instance method")s1 = Student()s1.show()
```

2\. Class Method

Works with class-level data. Uses `@classmethod`.

```
class Student:    college = "Shobhit University"    @classmethod    def show_college(cls):        print(cls.college)Student.show_college()
```

3\. Static Method

Does not receive an automatic instance or class reference.

```
class Calculator:    @staticmethod    def add(a, b):        return a + bprint(Calculator.add(10, 20))
```

## 16.8 Four Pillars of OOP

## Four pillars of OOP

Encapsulation

Bundling data and methods together.

Inheritance

Creating a new class from an existing class.

Polymorphism

One interface, multiple behaviours.

Abstraction

Hiding implementation details.

### A. Encapsulation

Encapsulation means combining data and methods inside a class and controlling access to internal data.

Python naming conventions:

- `name` — public.
- `_name` — protected by convention.
- `__name` — name-mangled attribute.

Example:

```
class BankAccount:    def __init__(self, balance):        self.__balance = balance    def deposit(self, amount):        if amount > 0:            self.__balance += amount    def get_balance(self):        return self.__balanceaccount = BankAccount(1000)account.deposit(500)print(account.get_balance())
```

Output:

```
1500
```

Explanation: The internal balance is accessed through methods rather than directly through the normal public interface.

### B. Inheritance

Inheritance allows one class to reuse and extend another class.

Parent class = Base class.

Child class = Derived class.

```
class Animal:    def eat(self):        print("Animal is eating")class Dog(Animal):    def bark(self):        print("Dog is barking")d = Dog()d.eat()d.bark()
```

Output:

```
Animal is eating
Dog is barking
```

#### Types of Inheritance

1\. Single Inheritance

One child class inherits from one parent class.

```
class A:    passclass B(A):    pass
```

2\. Multiple Inheritance

One child class inherits from multiple parent classes.

```
class Father:    def skills(self):        print("Gardening")class Mother:    def talent(self):        print("Cooking")class Child(Father, Mother):    passc = Child()c.skills()c.talent()
```

3\. Multilevel Inheritance

A class inherits from a child class.

```
class A:    def show_a(self):        print("Class A")class B(A):    def show_b(self):        print("Class B")class C(B):    def show_c(self):        print("Class C")obj = C()obj.show_a()obj.show_b()obj.show_c()
```

4\. Hierarchical Inheritance

Multiple child classes inherit from the same parent.

```
class Animal:    def eat(self):        print("Eating")class Dog(Animal):    passclass Cat(Animal):    pass
```

5\. Hybrid Inheritance

Combination of two or more inheritance types.

## 16.9 Method Overriding

When a child class provides its own implementation of a method inherited from the parent class, it is called method overriding.

```
class Animal:    def sound(self):        print("Animal makes sound")class Dog(Animal):    def sound(self):        print("Dog barks")d = Dog()d.sound()
```

Output:

```
Dog barks
```

## 16.10 super() Function

The `super()` function is used to access methods from a parent class according to Python's method resolution order (MRO).

```
class Parent:    def show(self):        print("Parent method")class Child(Parent):    def show(self):        super().show()        print("Child method")obj = Child()obj.show()
```

Output:

```
Parent method
Child method
```

## 16.11 Polymorphism

Polymorphism means the same method or interface can behave differently for different objects.

Example:

```
class Dog:    def sound(self):        print("Bark")class Cat:    def sound(self):        print("Meow")animals = [Dog(), Cat()]for animal in animals:    animal.sound()
```

Output:

```
Bark
Meow
```

### Duck Typing

Python focuses on whether an object supports the required behaviour rather than requiring a particular class.

```
class Dog:    def sound(self):        print("Bark")class Robot:    def sound(self):        print("Beep")def make_sound(obj):    obj.sound()make_sound(Dog())make_sound(Robot())
```

## 16.12 Abstraction

Abstraction means exposing essential functionality while hiding implementation details.

Python provides the `abc` module for abstract base classes.

```
from abc import ABC, abstractmethodclass Shape(ABC):    @abstractmethod    def area(self):        passclass Rectangle(Shape):    def __init__(self, length, width):        self.length = length        self.width = width    def area(self):        return self.length * self.widthr = Rectangle(10, 5)print(r.area())
```

Output:

```
50
```

You cannot instantiate `Shape` directly while its abstract methods remain unimplemented.

## 16.13 Operator Overloading

Operator overloading allows operators to work with user-defined objects by implementing special methods.

```
class Number:    def __init__(self, value):        self.value = value    def __add__(self, other):        return self.value + other.valuea = Number(10)b = Number(20)print(a + b)
```

Output:

```
30
```

## 16.14 Magic / Dunder Methods

Dunder means double underscore.

Examples:

| Method       | Purpose                             |
| ------------ | ----------------------------------- |
| `__init__()` | Initializes an object               |
| `__str__()`  | User-friendly string representation |
| `__repr__()` | Developer-oriented representation   |
| `__len__()`  | Defines behaviour for `len()`       |
| `__add__()`  | Defines `+`                         |
| `__eq__()`   | Defines `==`                        |
| `__call__()` | Makes an object callable            |

Example:

```
class Student:    def __init__(self, name):        self.name = name    def __str__(self):        return f"Student: {self.name}"s = Student("Pushpa")print(s)
```

Output:

```
Student: Pushpa
```

## 16.15 Composition

Composition means building a class using objects of other classes.

```
class Engine:    def start(self):        print("Engine started")class Car:    def __init__(self):        self.engine = Engine()    def start_car(self):        self.engine.start()        print("Car started")car = Car()car.start_car()
```

Composition is useful when one object contains or uses another object.

### OOP Interview Questions

1. What is OOP?
2. What is a class?
3. What is an object?
4. What is a constructor?
5. What is self?
6. Explain the four pillars of OOP.
7. What is inheritance?
8. What are the five types of inheritance?
9. Difference between method overriding and overloading?
10. What is polymorphism?
11. What is abstraction?
12. What is encapsulation?
13. What is super()?
14. What are magic methods?
15. Difference between class and instance variables?
16. Difference between composition and inheritance?

# 17. Advanced Python

This section covers important concepts used in real-world software development, Data Science, AI and Machine Learning.

## 17.1 List, Set and Dictionary Comprehensions

Comprehensions allow us to create collections in a concise way.

List comprehension:

```
squares = [x*x for x in range(1, 6)]print(squares)
```

Set comprehension:

```
squares = {x*x for x in range(1, 6)}print(squares)
```

Dictionary comprehension:

```
squares = {x: x*x for x in range(1, 6)}print(squares)
```

## 17.2 Iterators

An iterator is an object that returns elements one at a time.

It implements:

- `__iter__()`
- `__next__()`

Example:

```
numbers = [10, 20, 30]iterator = iter(numbers)print(next(iterator))print(next(iterator))print(next(iterator))
```

Output:

```
10
20
30
```

When there are no more elements, `next()` raises `StopIteration`.

## 17.3 Generators

A generator is a special kind of iterator that produces values one at a time.

It uses the `yield` keyword.

Example:

```
def generate_numbers():    yield 10    yield 20    yield 30for number in generate_numbers():    print(number)
```

Output:

```
10
20
30
```

### Why use Generators?

- Memory efficient.
- Useful for large datasets.
- Generates values when needed.
- Avoids creating an entire sequence in memory.

Generator vs Normal Function

| Normal function                  | Generator                      |
| -------------------------------- | ------------------------------ |
| Uses `return` to return a result | Uses `yield` to produce values |
| Returns a result                 | Returns a generator iterator   |
| Usually completes in one call    | Can pause and resume execution |

## 17.4 Decorators

A decorator is a function that modifies or extends another function's behaviour without changing its original source code.

Example:

```
def my_decorator(func):    def wrapper():        print("Before function")        func()        print("After function")    return wrapper@my_decoratordef greet():    print("Hello Python")greet()
```

Output:

```
Before function
Hello Python
After function
```

Real-world uses:

- Logging.
- Authentication.
- Measuring execution time.
- Caching.
- Access control.

## 17.5 Closures

A closure is a function that remembers variables from its enclosing scope even after the outer function has finished executing.

```
def outer(x):    def inner(y):        return x + y    return inneradd_five = outer(5)print(add_five(10))
```

Output:

```
15
```

## 17.6 \*args and \*\*kwargs

These are useful when the number of arguments is not fixed.

```
def display(*args, **kwargs):    print("Positional:", args)    print("Keyword:", kwargs)display(10, 20, name="Pushpa", age=20)
```

Output:

```
Positional: (10, 20)
Keyword: {'name': 'Pushpa', 'age': 20}
```

## 17.7 Shallow Copy and Deep Copy

Copying means creating another object based on an existing object.

Shallow Copy: Creates a new outer collection but keeps references to nested objects.

```
import copyoriginal = [[1, 2], [3, 4]]shallow = copy.copy(original)shallow[0][0] = 100print(original)
```

Output:

```
[[100, 2], [3, 4]]
```

The nested list is shared.

Deep Copy: Recursively copies nested objects.

```
import copyoriginal = [[1, 2], [3, 4]]deep = copy.deepcopy(original)deep[0][0] = 100print(original)print(deep)
```

Output:

```
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

| Shallow copy                 | Deep copy                         |
| ---------------------------- | --------------------------------- |
| Copies outer object          | Recursively copies nested objects |
| Nested references are shared | Nested objects are copied         |
| `copy.copy()`                | `copy.deepcopy()`                 |

## 17.8 Regular Expressions (Regex)

Regular expressions are used for pattern matching in strings.

Python provides the `re` module.

Example:

```
import retext = "My phone number is 9876543210"result = re.findall(r"\d+", text)print(result)
```

Output:

```
['9876543210']
```

Important regex symbols:

| Symbol | Meaning                                 |
| ------ | --------------------------------------- |
| `\d`   | Digit                                   |
| `\D`   | Non-digit                               |
| `\w`   | Word character                          |
| `\W`   | Non-word character                      |
| `\s`   | Whitespace                              |
| `.`    | Any character except newline by default |
| `^`    | Start of string                         |
| `$`    | End of string                           |
| `+`    | One or more                             |
| `*`    | Zero or more                            |
| `?`    | Zero or one                             |
| `{n}`  | Exactly n repetitions                   |

Important functions:

- `re.match()`
- `re.search()`
- `re.findall()`
- `re.sub()`
- `re.split()`

## 17.9 Context Managers

Context managers manage resources such as files and connections.

The `with` statement is the most common way to use one.

```
with open("data.txt", "w") as file:    file.write("Learning Advanced Python")
```

We can also create custom context managers using `__enter__()` and `__exit__()`.

## 17.10 Exception Handling in Advanced Programs

Use specific exceptions and preserve useful error information.

```
def divide(a, b):    try:        return a / b    except ZeroDivisionError as error:        print("Error:", error)        return Noneprint(divide(10, 0))
```

## 17.11 Python Memory Management

Python manages memory automatically.

Important concepts:

1\. Reference Counting

Python tracks references to objects. When an object's reference count reaches zero, it can generally be deallocated.

2\. Garbage Collection

Python also has a garbage collector to handle certain reference cycles.

3\. `del` Keyword

Deletes a name or removes a reference.

```
x = [10, 20, 30]del x
```

## 17.12 Global Interpreter Lock (GIL)

The GIL is a mechanism in conventional CPython builds that allows only one thread at a time to execute Python bytecode within an interpreter.

Important points:

- It affects CPU-bound multithreaded execution in conventional GIL-enabled CPython.
- Threads are still useful for many I/O-bound tasks.
- Multiprocessing can use multiple processes for CPU-bound work.
- Python also supports free-threaded CPython builds in newer versions.

## 17.13 Multithreading

Multithreading allows multiple threads to execute within a process.

Useful for:

- Downloading files.
- Network requests.
- Waiting for APIs.
- I/O-bound operations.

Example:

```
import threadingdef task():    print("Task is running")t1 = threading.Thread(target=task)t1.start()t1.join()print("Program completed")
```

`start()` begins the thread and `join()` waits for it to finish.

## 17.14 Multiprocessing

Multiprocessing uses separate processes.

Useful for CPU-intensive operations.

```
from multiprocessing import Processdef task():    print("Process is running")if __name__ == "__main__":    p = Process(target=task)    p.start()    p.join()
```

Important for Windows: Use the `if __name__ == "__main__":` guard when starting multiprocessing processes.

### Multithreading vs Multiprocessing

| Multithreading               | Multiprocessing         |
| ---------------------------- | ----------------------- |
| Multiple threads             | Multiple processes      |
| Shared process memory        | Separate process memory |
| Good for I/O-bound work      | Good for CPU-bound work |
| Lower overhead in many cases | Higher process overhead |

## 17.15 Asynchronous Programming

Asynchronous programming allows tasks to pause while waiting and lets other tasks make progress.

Python uses `async` and `await`.

```
import asyncioasync def greet():    print("Hello")    await asyncio.sleep(1)    print("Python")asyncio.run(greet())
```

Useful in:

- FastAPI.
- Web applications.
- API requests.
- Network programming.
- I/O-heavy systems.

## 17.16 Type Hints

Type hints indicate the expected types of variables, parameters and return values.

```
def add(a: int, b: int) -> int:    return a + bresult: int = add(10, 20)print(result)
```

Type hints improve readability and support static analysis. Python does not automatically enforce them at runtime.

## 17.17 Enumerate()

`enumerate()` returns an index and its corresponding element while iterating.

```
languages = ["Python", "Java", "C++"]for index, language in enumerate(languages, start=1):    print(index, language)
```

Output:

```
1 Python
2 Java
3 C++
```

## 17.18 Zip()

`zip()` combines corresponding elements from multiple iterables.

```
names = ["Pushpa", "Mohit", "Rahul"]marks = [90, 85, 88]result = zip(names, marks)for name, mark in result:    print(name, mark)
```

Output:

```
Pushpa 90
Mohit 85
Rahul 88
```

By default, `zip()` stops at the shortest iterable.

## 17.19 Sorting with key

```
students = [    ("Pushpa", 90),    ("Mohit", 85),    ("Rahul", 95)]students.sort(key=lambda student: student[1])print(students)
```

Output:

```
[('Mohit', 85), ('Pushpa', 90), ('Rahul', 95)]
```

## 17.20 Useful Built-in Functions

| Function       | Purpose                           |
| -------------- | --------------------------------- |
| `len()`        | Returns length                    |
| `type()`       | Returns type                      |
| `id()`         | Returns object identity           |
| `range()`      | Generates integer sequences       |
| `sum()`        | Calculates total                  |
| `min()`        | Finds minimum                     |
| `max()`        | Finds maximum                     |
| `sorted()`     | Returns a sorted list             |
| `reversed()`   | Returns a reverse iterator        |
| `enumerate()`  | Provides index and element        |
| `zip()`        | Combines iterables                |
| `any()`        | True if at least one item is true |
| `all()`        | True if all items are true        |
| `isinstance()` | Checks object type                |
| `abs()`        | Absolute value                    |
| `round()`      | Rounds a number                   |

### Advanced Python Interview Questions

1. What is an iterator?
2. What is a generator?
3. Difference between `yield` and `return`?
4. What is a decorator?
5. What is a closure?
6. Difference between shallow copy and deep copy?
7. What is the GIL?
8. Difference between multithreading and multiprocessing?
9. What is asynchronous programming?
10. What are context managers?
11. What are regular expressions?
12. What are type hints?
13. Difference between `enumerate()` and `zip()`?
14. What is garbage collection?
15. What is the difference between `sorted()` and `sort()`?

# 18. Python Fundamentals — Quick Revision Sheet

This table will help you revise all 17 topics quickly.

| No. | Topic                  | Most important concept                       |
| --- | ---------------------- | -------------------------------------------- |
| 1   | Variables & Data Types | Variables, `type()`, type conversion         |
| 2   | Input / Output         | `input()`, `print()`, f-strings              |
| 3   | Operators              | Arithmetic, logical, comparison              |
| 4   | Conditions             | if, elif, else, match                        |
| 5   | Loops                  | for, while, break, continue                  |
| 6   | Strings                | Indexing, slicing, string methods            |
| 7   | Lists                  | Mutable collections, list methods            |
| 8   | Tuples                 | Immutable collections                        |
| 9   | Sets                   | Unique elements, set operations              |
| 10  | Dictionaries           | Key-value pairs                              |
| 11  | Functions              | Parameters, arguments, return                |
| 12  | Recursion              | Base case, recursive call                    |
| 13  | Modules & Packages     | Import, pip, virtual environments            |
| 14  | File Handling          | Read, write, append, JSON, CSV               |
| 15  | Exception Handling     | try, except, finally, raise                  |
| 16  | OOP                    | Class, object, four pillars                  |
| 17  | Advanced Python        | Generators, decorators, iterators, threading |

# 19. Practical Python Projects

After completing these concepts, build these small projects to improve your programming skills.

[Kursus Python Data Science Terbaik 2026, 1 Murid 1 Instruktur](https://images.openai.com/static-rsc-4/yh6slQM58xVVsHr1SMqtLWAqdEZ8fxSoHfq4cbwkKtMDsQW4Hn_vhxPcUTtHPccF-PTi5uAFKlh4ZEI9ICaB-u0KfIR14x_n_PeHHUP871CA4Yu5kvMadPoS3_VsE_YGyuIXR58TJ97bAZBZKtTH4tQjPejdNnFZnaR8K8W5soU?purpose=inline)

1\. Calculator Application

Concepts: Variables, operators, functions, conditions.

Beginner

[GitHub - Rahul9121/Student-Management-System-Rahul: A modern, web-based Student Management System built with Flask and SQLAlchemy, featuring a beautiful gradient UI and comprehensive academic data management capabilities. · GitHub](https://images.openai.com/static-rsc-4/3Slsd_B7lDog5z68n883gg8v5HuuBuI0SEU1oZfN89vQVnluju63kKnDctWIULZihQE54oC3RtA_8gmRBokXPKhXOfVvZioVgpBxs6K0W1xJqtpS4wmwO0KHYvlcvksb1IrXO4kpfAJSnyYl4GEbXPTvvRqVszsAYLDOyikZDx4?purpose=inline)

2\. Student Management System

Concepts: Lists, dictionaries, functions, file handling.

Beginner

[class 12 computer science python project with source code — Bank Management System. | by Hrithik Kumar Singh | Medium](https://images.openai.com/static-rsc-4/eOVvYx5uEUA1gDQtS73kpISPzI5Ic5OWgI93w3DjoZImYujg6RAey_2Fw7_JLS-4gMwrqSkxV4vg1TO2Yj6Z-o44zzPc8Eg0c6IMGWbFGfeGMnyS0nhncH2vujMmmQ6O0NOjgOdf4nP3AlIsGzM1_DU17b0t1OlVwemUFHFTjtQ?purpose=inline)

3\. Bank Management System

Concepts: OOP, classes, objects, exception handling.

Intermediate

[A Personal Finances Tracker in Streamlit - Show the Community! - Streamlit](https://images.openai.com/static-rsc-4/lVq95ONBKOXFtMR3A41maMBGhHhlZNf69fHpp84WCN6aEwWQM05w9QzKL21cO7_87dcOtwQbSJ_kK4UHjyYkon3TUd_36YYNv1UF2Aqqq3131gqxIO7m8TTvJ_0goA7zGNy1-nfGPNxrypDKdkXlhfzC0qyckjPHvkMvgco80us?purpose=inline)

4\. Expense Tracker

Concepts: Functions, dictionaries, CSV, JSON.

Intermediate

[Weather Dashboard - Dark mode by Micsaela on Dribbble](https://images.openai.com/static-rsc-4/2PZlXKbY704uJ6MVUfJ_AiNZYbUSvC1Zs5-0O8g7-oocqBzWxTh1CcJLeFXZjsimFVCLBci03TqHYdubPPakttljQXOe7HjmllmwQAdbXecJMugj349gYaW98-Y1m1uXdxAIY8vi9jY7LaoUnqKflXclAWimyrJ4UkQvLB6CSzU?purpose=inline)

5\. Weather Application

Concepts: APIs, modules, JSON, exception handling.

Intermediate

# 20. Your Phase 01 Completion Checklist

Use this checklist to track your learning progress.

Python Fundamentals Progress


0 of 17 topics completed

Variables & Data Types

Input / Output

Operators

Conditions

Loops

Strings

Lists

Tuples

Sets

Dictionaries

Functions

Recursion

Modules & Packages

File Handling

Exception Handling

OOP

Advanced Python

Reset checklist



For each topic, follow this routine:

| Activity                   | Daily time |
| -------------------------- | ---------- |
| Read notes                 | 30 minutes |
| Understand examples        | 20 minutes |
| Write code yourself        | 30 minutes |
| Solve coding questions     | 20 minutes |
| Revise interview questions | 20 minutes |
| Total                      | 2 hours    |

Important for your AI/ML career: After Python Fundamentals, give special attention to NumPy, Pandas, Matplotlib, SQL, DSA and Scikit-learn. These will help you build stronger AI/ML projects.

My recommendation: Don't just memorize Python syntax. Try to understand what happens internally when your code executes.

I can also prepare a daily set of 5 Python coding problems with solutions, dry runs and interview questions to help you practise after these notes.

Daily Python practice questionsTap to set up