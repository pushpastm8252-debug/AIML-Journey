# DBMS (Database Management System) – Complete Detailed Notes

SUBJECT NOTES · BEGINNER TO ADVANCED · ENGLISH

These notes cover DBMS from basic concepts to advanced topics, including definitions, examples, SQL commands, normalization, keys, transactions, concurrency control, indexing, and important examination questions.

# UNIT 1: INTRODUCTION TO DBMS

## 1. What is Data?

Data refers to raw facts and figures that have not yet been processed or organized into meaningful information.

Examples:

- Student name: Rahul
- Roll number: 101
- Marks: 85
- Age: 20

Data itself may not provide complete meaning until it is processed.

## 2. What is Information?

Information is processed, organized, and meaningful data that helps people make decisions.

Example:

- Data: 85, 90, 75, 80
- Information: The average marks of a student are 82.5.

Difference between Data and Information

| Data                  | Information              |
| --------------------- | ------------------------ |
| Raw facts and figures | Processed data           |
| May not have meaning  | Has meaningful context   |
| Used as input         | Produced as output       |
| Not always organized  | Organized and structured |

## 3. What is a Database?

A database is an organized collection of related data that can be easily accessed, managed, updated, and retrieved.

Examples:

1. Student database
2. Banking database
3. Hospital database
4. Railway reservation database
5. Library management database
6. E-commerce database

Example of a Student Database:

| Student_ID | Name  | Course | Marks |
| ---------- | ----- | ------ | ----- |
| 101        | Rahul | B.Tech | 85    |
| 102        | Priya | BCA    | 90    |
| 103        | Aman  | B.Tech | 78    |

## 4. What is DBMS?

DBMS stands for Database Management System.

A DBMS is software that allows users to create, store, organize, retrieve, update, and manage data in a database.

It acts as an interface between the database and its users or applications.

Examples of DBMS:

- MySQL
- Oracle Database
- Microsoft SQL Server
- PostgreSQL
- SQLite
- Microsoft Access

[PPT - Lec1 - Introduction PowerPoint Presentation, free download - ID:6355332](https://images.openai.com/static-rsc-4/b2n6I8aA7bgNaVstJqqVGIf3Sc6q_kY4QapPNf48pmOm8P06Qk-nvi_0dgtf2AfwFVSX4LGWigFd_ikuPgMfoMHqedKviEIwgsaiBtuNL0O0WZVsty1K5tFFlUWFfmauA6S36iklP80AqyMXSiHVKQ1rtTKh8v79ErNmyzfQyF0?purpose=inline)

[slideserve.com](https://www.slideserve.com/chaney-morris/lec1-introduction-powerpoint-ppt-presentation?utm_source=chatgpt.com)

### Main Functions of DBMS

1. Data Storage: Stores large amounts of data.
2. Data Retrieval: Retrieves required information.
3. Data Insertion: Adds new records.
4. Data Updating: Modifies existing records.
5. Data Deletion: Removes unwanted records.
6. Security: Protects data from unauthorized access.
7. Backup and Recovery: Restores data after failures.
8. Data Integrity: Maintains accuracy and consistency.
9. Concurrency Control: Allows multiple users to access data safely.
10. Data Sharing: Enables authorized users to share data.

## 5. Characteristics of DBMS

1. Data Independence: Changes in database structure can be made with minimal impact on applications.
2. Reduced Data Redundancy: Avoids unnecessary duplication of data.
3. Data Consistency: Maintains accurate and consistent data.
4. Data Security: Protects data using authentication and authorization.
5. Data Integrity: Ensures data follows defined rules.
6. Data Sharing: Multiple users can access the database.
7. Backup and Recovery: Provides protection against data loss.
8. Concurrent Access: Supports simultaneous database operations.
9. Multiple Views: Different users can see different views of the same database.
10. Centralized Management: Data can be managed through a common system.

## 6. Advantages of DBMS

- Reduces data duplication.
- Improves data security.
- Maintains data consistency.
- Provides backup and recovery.
- Supports multiple users.
- Improves data accessibility.
- Maintains data integrity.
- Makes data management easier.
- Provides data independence.
- Supports efficient query processing.

## 7. Disadvantages of DBMS

- High installation and maintenance costs.
- Requires trained database administrators.
- Complex to design and manage.
- Requires additional hardware and software resources.
- Database failure may affect multiple applications.
- Security breaches can expose large amounts of data.
- Regular backup and maintenance are required.

## 8. Applications of DBMS

| Industry           | Application                        |
| ------------------ | ---------------------------------- |
| Banking            | Account and transaction management |
| Education          | Student and examination records    |
| Healthcare         | Patient and medical records        |
| Railway            | Ticket booking and reservation     |
| E-commerce         | Products and customer information  |
| Airlines           | Flight and passenger management    |
| Telecommunications | Customer and call records          |
| Government         | Citizen and public records         |
| Social Media       | User profiles and posts            |
| Libraries          | Books and member records           |

# UNIT 2: DBMS ARCHITECTURE

## 9. DBMS Architecture

DBMS architecture describes how users interact with a database and how data is stored and managed.

There are three main levels of DBMS architecture:

1. One-Tier Architecture
2. Two-Tier Architecture
3. Three-Tier Architecture

### A. One-Tier Architecture

In one-tier architecture, the user directly interacts with the database system.

The application, DBMS, and database are located on the same machine.

[DBMS Architecture  - Scaler Topics](https://images.openai.com/static-rsc-4/jxHCaKaxO05CV-Q5OPDMDYTPhgn2NwmXkbqDmrvm9eyb8-WKjjAXOqJ8p50Ur4Bhrb5PqWMCArn1eSdlmrzMmvV-QuHoNZSb9n0VqhptHNvXQV4svfgTbaJj4jZepBsUbdGRxr0WHZCnsYkZW82cok-luImrncrx9jkZHkd8JKc?purpose=inline)

[scaler.com](https://www.scaler.com/topics/dbms/dbms-architecture/?utm_source=chatgpt.com)

Advantages:

- Simple architecture.
- Easy to develop.
- Suitable for local applications.

Disadvantages:

- Limited security.
- Difficult to scale.
- Not suitable for large multi-user applications.

Example: A local SQLite database application.

### B. Two-Tier Architecture

In two-tier architecture, the client application communicates directly with the database server.

It consists of:

1. Client Layer
2. Database Server Layer

[DBMS Series Part 2: DBMS Architecture](https://images.openai.com/static-rsc-4/eXXUTVnIj2UDYoporXS7X--wRDRu41JxFD3D8wKiUHSw2IvH3yN_GxOeW6PWThTZ5RVkSNYPlQQlidZFFPGATU1chbga_f-naO7Ue0LDRHM5f-bCT15o3SvhxXnsuV9k4FU0gSlORCiGLOq55oUUVlWB5iGyDfsMsAoPEtf4CrI?purpose=inline)

[blog.codingminutes.com](https://blog.codingminutes.com/dbms-architecture?utm_source=chatgpt.com)

Advantages:

- Easy to implement.
- Better data management.
- Suitable for small applications.

Disadvantages:

- Limited scalability.
- Direct database access can create security risks.
- More difficult to manage many clients.

Example: A desktop application connected directly to MySQL.

### C. Three-Tier Architecture

Three-tier architecture divides an application into three layers:

1. Presentation Layer
2. Application Layer
3. Database Layer

[Client-Server Architecture Explained](https://images.openai.com/static-rsc-4/-RAmcmHL7IUsl3mQKvlVspjiatIjxnugbRT5Pxu51HhoBiU4BLQVkkc_Dlc_ejDhU3M4lz3wbfjzMK7c21fq5pgLiQKgFK961lMNHaYCfouTbNFBMeczz5i2jwK_R0Q_MRqiY8r6jyTlsBBtXkHvwijlTU0QIX4gzI696U1T4sY?purpose=inline)

[blog.algomaster.io](https://blog.algomaster.io/p/client-server-architecture-explained?utm_source=chatgpt.com)

1\. Presentation Layer

The user interface through which users interact with the application.

Example: HTML, CSS, JavaScript, React.

2\. Application Layer

Processes user requests and contains business logic.

Example: Python, Java, PHP, Node.js.

3\. Database Layer

Stores and manages application data.

Example: MySQL, PostgreSQL, Oracle.

Advantages:

- Better security.
- Easy maintenance.
- High scalability.
- Separation of responsibilities.
- Suitable for enterprise applications.

Disadvantages:

- More complex architecture.
- Higher development costs.
- Communication between layers may increase latency.

## 10. Three-Schema Architecture

The three-schema architecture separates a database into three levels.

[Get This Database Management System PPT And Google Slides](https://images.openai.com/static-rsc-4/2gnnCL8xchxDLuJ2ePtYrKiY_RJQCpMvgGdI0iaJPOftuAeuYk8CJ_BWmq30688qFZEiwJybwSyhas8pGrRjDr6Dq5A9ueMX9r7mxX0YBJxKF6-GkDdanllabrNy45TcWO2hPkDCKZxxo44btIirwJuqb7EBCWGRTnX2KJ-Pb3k?purpose=inline)

[slideegg.com](https://www.slideegg.com/database-management-system?utm_source=chatgpt.com)

### A. External Level (View Level)

- Highest level of abstraction.
- Describes how individual users view data.
- Different users can have different views.

Example: A student sees marks, while an accountant sees fee details.

### B. Conceptual Level (Logical Level)

- Describes the overall logical structure of the database.
- Defines entities, relationships, attributes, and constraints.
- Does not describe physical storage details.

### C. Internal Level (Physical Level)

- Lowest level of abstraction.
- Describes how data is physically stored.
- Includes file organization, indexes, and storage structures.

## 11. Data Independence

Data independence means the ability to modify the database schema at one level without requiring changes at the next higher level.

There are two types:

A. Physical Data Independence

The ability to change the internal storage structure without affecting the conceptual schema.

Example:

- Changing file organization.
- Creating an index.
- Moving data to another storage device.

B. Logical Data Independence

The ability to change the conceptual schema without affecting external views or application programs.

Example:

- Adding a new column to a student table.
- Adding a new entity to the database.

| Physical Independence            | Logical Independence             |
| -------------------------------- | -------------------------------- |
| Changes internal schema          | Changes conceptual schema        |
| Easier to achieve                | More difficult to achieve        |
| Does not affect conceptual level | Should not affect external views |

# UNIT 3: DATA MODELS

## 12. What is a Data Model?

A data model defines how data is organized, stored, connected, and manipulated in a database.

### Types of Data Models

1\. Hierarchical Data Model

Data is organized in a tree-like structure.

- Parent-child relationship.
- One parent can have multiple children.
- Each child generally has one parent.

[Hierarchical Database vs Relational Databases: Differences & Similarities | Airbyte](https://images.openai.com/static-rsc-4/ZgEOmKhOhmA8pkISbjw7aoKaAe2P_nAb-W7uqbrAJDivstc_RU0iU3BnN3YJQJgyPY4-XQoDYEfMg6nsOXUkFEfY0yl8fPzc9BAqIvdvzI6kjEKXfZy1-jjyX5DXdgeDDLbSSK9nbYyrp72mzNPC-9_v_Xzt3FYdLYsd659IV_0?purpose=inline)

[airbyte.com](https://airbyte.com/data-engineering-resources/hierarchical-vs-relational-database?utm_source=chatgpt.com)

Example: Company organizational structure.

2\. Network Data Model

Data is organized using a graph-like structure.

- Supports many-to-many relationships.
- A record can have multiple parent records.
- More flexible than the hierarchical model.

[Database Models: Different Types and Structures Explained](https://images.openai.com/static-rsc-4/j5JTVHePZNb9ElIlruV0KDi5HpYesZXJWxf47KA1Tm2I45kYvO8h9yAme1JYzAlvxnT3tg5IMugpLml4EFHlSbCh_maRoE_n1udXfLcKmlWoJDhvqhwQAdkXykUJS8CgCOOxPQftv7QjoOkGbFrfTz4_M3hN8QujqHBmsdtwVYY?purpose=inline)

[exasol.com](https://www.exasol.com/hub/database/models/?utm_source=chatgpt.com)

Example: Students enrolled in multiple courses.

3\. Relational Data Model

Data is stored in tables consisting of rows and columns.

[Data Models in DBMS: All Major Types Explained](https://images.openai.com/static-rsc-4/bAMYTTvcDtl2j0XP7ZkGR09ogB7vxp3x40q_5GeWaG63uMfn3WN0K5_s290Z-NSUo3yHF4hLPzrNBuPQN-lpxsut7kuKb95FjXjymRe4kEaq8ISrHju0RcJWH2JFveuI5vucjWLweLjs6vgSDMnBzFyTWUhhMYEeoA1Hwx4Dlj8?purpose=inline)

[unstop.com](https://unstop.com/blog/data-model-in-dbms?utm_source=chatgpt.com)

Example: Student, Course, and Department tables.

4\. Entity-Relationship Model

Represents real-world entities, their attributes, and relationships.

Example:

- Student
- Teacher
- Course
- Department

5\. Object-Oriented Data Model

Stores data in the form of objects, similar to object-oriented programming.

6\. Object-Relational Data Model

Combines relational database concepts with object-oriented features.

# UNIT 4: ER MODEL (ENTITY RELATIONSHIP MODEL)

## 13. What is an ER Model?

The Entity-Relationship Model is a conceptual database model used to represent entities, attributes, and relationships.

It is mainly used during database design.

## 14. Entity

An entity is a real-world object that can be uniquely identified.

Examples:

- Student
- Teacher
- Employee
- Department
- Product

### Types of Entities

A. Strong Entity

An entity that has its own primary key and can exist independently.

Example: Student.

B. Weak Entity

An entity that cannot be uniquely identified using its own attributes alone and depends on an owner entity.

Example: A dependent associated with an employee.

## 15. Attribute

An attribute is a property or characteristic of an entity.

Example:

Student entity:

- Student_ID
- Name
- Age
- Email
- Address

### Types of Attributes

| Type          | Meaning                           | Example       |
| ------------- | --------------------------------- | ------------- |
| Simple        | Cannot be divided further         | Age           |
| Composite     | Can be divided into parts         | Full Name     |
| Single-valued | Has one value                     | Roll Number   |
| Multi-valued  | Can have multiple values          | Phone Numbers |
| Derived       | Calculated from another attribute | Age from DOB  |
| Key           | Uniquely identifies a record      | Student_ID    |
| Stored        | Physically stored                 | Date of Birth |

## 16. Relationship

A relationship represents an association between two or more entities.

Example: A student enrolls in a course.

### Types of Relationships

1\. One-to-One (1:1)

One entity is associated with only one entity of another type.

Example: One person has one passport (in a simplified model).

2\. One-to-Many (1:M)

One entity is associated with multiple entities.

Example: One department has many employees.

3\. Many-to-One (M:1)

Many entities are associated with one entity.

Example: Many employees work in one department.

4\. Many-to-Many (M:N)

Multiple entities are associated with multiple entities.

Example: Many students enroll in many courses.

[Entity-Relationship (ER) Diagram Symbols and Notations | EdrawMax](https://images.openai.com/static-rsc-4/7pjMiGsoDB_rdX6y2GA-JrDVlg434yOaOC7EER_x-d6Mv2VFJFREDFHO9toyGNk3NXkBPTpmdSBD7XNhj-P8UZFsX1cATV0196pSQVJj1d1TtTF_ucc-CACdABUJ_ThcnmnzKAGshz_jmoIC6c4aePU5WXeuF0LQMsVhYfMKHOw?purpose=inline)

[edrawsoft.com](https://www.edrawsoft.com/er-diagram-symbols.html?utm_source=chatgpt.com)

## 17. ER Diagram Symbols

| Symbol               | Meaning                  |
| -------------------- | ------------------------ |
| Rectangle            | Strong entity            |
| Double rectangle     | Weak entity              |
| Oval                 | Attribute                |
| Underlined attribute | Key attribute            |
| Double oval          | Multivalued attribute    |
| Dashed oval          | Derived attribute        |
| Diamond              | Relationship             |
| Double diamond       | Identifying relationship |
| Connecting line      | Association              |

# UNIT 5: RELATIONAL DATABASE MODEL

## 18. What is a Relational Database?

A relational database stores data in tables called relations.

Each table consists of rows and columns.

Example:

STUDENT Table

| Student_ID | Name  | Age |
| ---------- | ----- | --- |
| 101        | Rahul | 20  |
| 102        | Priya | 21  |
| 103        | Aman  | 19  |

### Important Terminologies

1\. Relation: A table in a relational database.

2\. Tuple: A row in a table.

3\. Attribute: A column in a table.

4\. Domain: The set of valid values allowed for an attribute.

5\. Degree: Number of attributes (columns) in a relation.

6\. Cardinality: Number of tuples (rows) in a relation.

7\. NULL: Represents missing, unknown, or unavailable data.

8\. Schema: The logical structure or design of a database.

9\. Instance: The actual data stored in a database at a particular time.

## 19. Properties of a Relation

- Every relation has a unique name.
- Each column has a unique name within a table.
- Each cell contains a single value in the classical relational model.
- Values in a column belong to the same domain.
- Duplicate tuples are not allowed in the mathematical relational model.
- The order of rows is not important.
- The order of columns is not important.

# UNIT 6: KEYS IN DBMS

## 20. What is a Key?

A key is an attribute or combination of attributes used to identify records uniquely in a database.

Keys help maintain data integrity and establish relationships between tables.

### Types of Keys

1\. Super Key

A super key is a set of one or more attributes that can uniquely identify a row.

Example:

Student table:

- Student_ID
- Email
- Name

Possible super keys:

- Student_ID
- Email
- Student_ID + Name
- Email + Name

2\. Candidate Key

A candidate key is a minimal super key. It contains no unnecessary attributes.

Example:

- Student_ID
- Email

If both uniquely identify students, both can be candidate keys.

3\. Primary Key

A primary key is the candidate key selected to uniquely identify each record.

Properties:

- Must be unique.
- Cannot contain NULL values.
- Only one primary key constraint per table.
- Can contain multiple columns (composite primary key).

Example: Student_ID.

4\. Alternate Key

Candidate keys that are not selected as the primary key are called alternate keys.

Example: If Student_ID is primary, Email can be an alternate key.

5\. Foreign Key

A foreign key is an attribute or set of attributes that references a candidate key, usually the primary key, of another table.

Example:

Department Table:

| Dept_ID | Dept_Name |
| ------- | --------- |
| 1       | CSE       |
| 2       | AIML      |

Student Table:

| Student_ID | Name  | Dept_ID |
| ---------- | ----- | ------- |
| 101        | Rahul | 1       |
| 102        | Priya | 2       |

Here, Dept_ID in Student is a foreign key referencing Department.

6\. Composite Key

A key consisting of two or more attributes.

Example:

- Student_ID
- Course_ID

Together, they uniquely identify a student-course enrollment.

7\. Unique Key

A constraint that ensures values in a column or combination of columns are unique.

8\. Surrogate Key

An artificially generated key with no direct business meaning.

Example: An automatically generated numeric ID.

### Difference Between Primary Key and Foreign Key

| Primary Key                          | Foreign Key                        |
| ------------------------------------ | ---------------------------------- |
| Uniquely identifies rows             | Establishes relationships          |
| Must be unique                       | Can contain duplicate values       |
| Cannot be NULL                       | Can be NULL if permitted           |
| One primary key constraint per table | Multiple foreign keys are possible |
| Identifies records in its own table  | References another table's key     |

# UNIT 7: SQL (STRUCTURED QUERY LANGUAGE)

## 21. What is SQL?

SQL stands for Structured Query Language.

It is a standard language used to communicate with relational database management systems.

SQL is used to:

- Create databases.
- Create tables.
- Insert records.
- Retrieve records.
- Update records.
- Delete records.
- Control access.
- Manage transactions.

Popular SQL databases:

- MySQL
- PostgreSQL
- Oracle
- SQL Server
- SQLite

## 22. Categories of SQL Commands

There are five major categories:

1. DDL
2. DML
3. DQL
4. DCL
5. TCL

### A. DDL – Data Definition Language

DDL commands define and modify database structures.

1\. CREATE

Creates a database or table.

```
CREATE DATABASE College;
```

Create a table:

```
CREATE TABLE Student (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Course VARCHAR(50)
);
```

2\. ALTER

Modifies an existing table.

Add a column:

```
ALTER TABLE Student
ADD Email VARCHAR(100);
```

Modify a column's data type (syntax varies by DBMS):

```
ALTER TABLE Student
ALTER COLUMN Age TYPE SMALLINT;
```

3\. DROP

Deletes a database object permanently.

```
DROP TABLE Student;
```

4\. TRUNCATE

Removes all rows from a table while keeping its structure.

```
TRUNCATE TABLE Student;
```

5\. RENAME

Renames a table (syntax varies by DBMS).

```
ALTER TABLE Student
RENAME TO Students;
```

### B. DML – Data Manipulation Language

DML commands modify data stored inside tables.

1\. INSERT

```
INSERT INTO Student
(Student_ID, Name, Age, Course)
VALUES
(101, 'Rahul', 20, 'B.Tech');
```

2\. UPDATE

```
UPDATE Student
SET Age = 21
WHERE Student_ID = 101;
```

3\. DELETE

```
DELETE FROM Student
WHERE Student_ID = 101;
```

### C. DQL – Data Query Language

DQL is used to retrieve data.

SELECT

```
SELECT * FROM Student;
```

Retrieve selected columns:

```
SELECT Name, Course
FROM Student;
```

### D. DCL – Data Control Language

DCL manages user access and permissions.

1\. GRANT

Provides permissions.

```
GRANT SELECT ON Student TO user1;
```

2\. REVOKE

Removes permissions.

```
REVOKE SELECT ON Student FROM user1;
```

Exact syntax and supported privileges depend on the DBMS.

### E. TCL – Transaction Control Language

TCL manages database transactions.

1\. COMMIT

Permanently saves transaction changes.

```
COMMIT;
```

2\. ROLLBACK

Undoes uncommitted changes.

```
ROLLBACK;
```

3\. SAVEPOINT

Creates a point inside a transaction to which you can roll back.

```
SAVEPOINT sp1;
```

4\. ROLLBACK TO SAVEPOINT

```
ROLLBACK TO SAVEPOINT sp1;
```

### SQL Commands Summary

| Category | Full Form                    | Commands                      |
| -------- | ---------------------------- | ----------------------------- |
| DDL      | Data Definition Language     | CREATE, ALTER, DROP, TRUNCATE |
| DML      | Data Manipulation Language   | INSERT, UPDATE, DELETE        |
| DQL      | Data Query Language          | SELECT                        |
| DCL      | Data Control Language        | GRANT, REVOKE                 |
| TCL      | Transaction Control Language | COMMIT, ROLLBACK, SAVEPOINT   |

## 23. SQL Operators

### Arithmetic Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| +        | Addition                 |
| -        | Subtraction              |
| \*       | Multiplication           |
| /        | Division                 |
| %        | Modulus (DBMS-dependent) |

### Comparison Operators

| Operator | Meaning |
| -------- | ------- |
| =        | Equal   |

\| != or&#x20;

\| Not equal |\
\| > | Greater than |\
\| < | Less than |\
\| >= | Greater than or equal |\
\|  18 AND Course = 'B.Tech';

````

## 24. Important SQL Clauses

**1. WHERE**

Filters rows based on a condition.

```sql
SELECT *
FROM Student
WHERE Age > 20;
````

2\. ORDER BY

Sorts results.

```
SELECT *
FROM Student
ORDER BY Age DESC;
```

3\. GROUP BY

Groups rows with the same values.

```
SELECT Course, COUNT(*)
FROM Student
GROUP BY Course;
```

4\. HAVING

Filters grouped results.

```
SELECT Course, COUNT(*)
FROM Student
GROUP BY Course
HAVING COUNT(*) > 5;
```

5\. DISTINCT

Removes duplicate values from query results.

```
SELECT DISTINCT Course
FROM Student;
```

6\. LIMIT

Restricts the number of returned rows in databases that support it.

```
SELECT *
FROM Student
LIMIT 5;
```

7\. BETWEEN

Checks whether a value is within a range.

```
SELECT *
FROM Student
WHERE Age BETWEEN 18 AND 22;
```

8\. IN

Checks whether a value matches any value in a list.

```
SELECT *
FROM Student
WHERE Course IN ('B.Tech', 'BCA');
```

9\. LIKE

Searches using patterns.

```
SELECT *
FROM Student
WHERE Name LIKE 'A%';
```

Pattern symbols:

- `%` = Zero or more characters.
- `_` = Exactly one character.

10\. IS NULL

Checks for NULL values.

```
SELECT *
FROM Student
WHERE Email IS NULL;
```

## 25. Aggregate Functions

Aggregate functions perform calculations on multiple rows and return a single result.

| Function | Purpose                        |
| -------- | ------------------------------ |
| COUNT()  | Counts rows or non-NULL values |
| SUM()    | Calculates total               |
| AVG()    | Calculates average             |
| MAX()    | Finds maximum                  |
| MIN()    | Finds minimum                  |

Examples:

```
SELECT COUNT(*) FROM Student;

SELECT AVG(Age) FROM Student;

SELECT MAX(Age) FROM Student;

SELECT MIN(Age) FROM Student;

SELECT SUM(Age) FROM Student;
```

## 26. SQL Constraints

Constraints are rules applied to table columns to maintain data accuracy and integrity.

### Types of Constraints

1\. NOT NULL

Prevents NULL values.

```
Name VARCHAR(50) NOT NULL
```

2\. UNIQUE

Ensures unique values.

```
Email VARCHAR(100) UNIQUE
```

3\. PRIMARY KEY

Uniquely identifies records.

```
Student_ID INT PRIMARY KEY
```

4\. FOREIGN KEY

Maintains relationships between tables.

```
FOREIGN KEY (Dept_ID)
REFERENCES Department(Dept_ID)
```

5\. CHECK

Ensures values satisfy a condition.

```
Age INT CHECK (Age >= 18)
```

6\. DEFAULT

Provides a default value.

```
City VARCHAR(50) DEFAULT 'Meerut'
```

# UNIT 8: JOINS IN SQL

## 27. What is a JOIN?

A JOIN is used to combine rows from two or more tables based on a related column.

Consider these two tables:

Student

| Student_ID | Name  | Dept_ID |
| ---------- | ----- | ------- |
| 1          | Rahul | 10      |
| 2          | Priya | 20      |
| 3          | Aman  | 30      |

Department

| Dept_ID | Dept_Name |
| ------- | --------- |
| 10      | CSE       |
| 20      | AIML      |
| 40      | IT        |

### Types of Joins

1\. INNER JOIN

Returns only matching records from both tables.

[INNER JOIN : le type de JOIN le plus important - IONOS](https://images.openai.com/static-rsc-4/30cfv-NXUWQq4nGLcm2-1lO-MFwoseTRGLtSo6Ps0lsu4rjNmykL6oI7sPDRMe9bQkWCkfEsoiIUC6L3XBar9ZZ3zd8kHcdBp6_teqSeDkDc2I4sR7nrUoSH9sl5a8vReNxnNUSh2DMqN7XOGMe4rw6oeMM2uj8fr7N-u_-uVqA?purpose=inline)

[ionos.fr](https://www.ionos.fr/digitalguide/hebergement/aspects-techniques/sql-inner-join/?utm_source=chatgpt.com)

```
SELECT Student.Name, Department.Dept_Name
FROM Student
INNER JOIN Department
ON Student.Dept_ID = Department.Dept_ID;
```

Result:

| Name  | Dept_Name |
| ----- | --------- |
| Rahul | CSE       |
| Priya | AIML      |

2\. LEFT JOIN (LEFT OUTER JOIN)

Returns all rows from the left table and matching rows from the right table. Unmatched right-side values are NULL.

[Understanding Joins in PostgreSQL | by Megha Muraleedharan | Medium](https://images.openai.com/static-rsc-4/i_xK0zznOGDsw7dQvtQRuXxh4PXBIJCvOoJDxHHzTsvK-wmf-DTUm4J1zBi9KEwZQW59Dt9LhlgTpIegsx_Z1i8KW7EinVFaM85nMKBVbJexET3uiIVBBNtRlE8a3A8Wt4KK3DhKT-UF5IHeX7Obz-78CRSFn1JJLHDPsyqIhSQ?purpose=inline)

[medium.com](https://medium.com/%40megsatish15/understanding-joins-in-postgresql-d246683b0243?utm_source=chatgpt.com)

```
SELECT Student.Name, Department.Dept_Name
FROM Student
LEFT JOIN Department
ON Student.Dept_ID = Department.Dept_ID;
```

3\. RIGHT JOIN (RIGHT OUTER JOIN)

Returns all rows from the right table and matching rows from the left table.

[Facts About Different Types of SQL Joins: How They Work and When to Use Them | by Anh Trần Tuấn | tuanhdotnet | Medium](https://images.openai.com/static-rsc-4/B4_on5F5qLSFf7qUhw0n5wo5aqQxsuk3KJoTeMw3jlsDZnnColoIeiNawYD2zfAtWAHtS_VaSujGVrhPt-n0yktKAeTt8cmIBhG9a7Mkf0TVaCFNhuHI_owelz5or_yRgaDea0ypLTAHCTovLDNVe9hn1w_DC9VBucc3Rprtuuw?purpose=inline)

[medium.com](https://medium.com/tuanhdotnet/facts-about-different-types-of-sql-joins-how-they-work-and-when-to-use-them-841a972065cd?utm_source=chatgpt.com)

```
SELECT Student.Name, Department.Dept_Name
FROM Student
RIGHT JOIN Department
ON Student.Dept_ID = Department.Dept_ID;
```

4\. FULL OUTER JOIN

Returns all matching and non-matching rows from both tables.

[What to know about SQL Full Outer Join | PDQ](https://images.openai.com/static-rsc-4/y-cz4N3wL4gleyD6AxgNNWbwZcpjzl-Z_hu6e-Pp66r7FF7MzTzWx-AXlMXyc-dBEHNCBt_CJ9S0bYZD8uHBllBNDMC6ScZjNIfzG0U-aCZftZl37BZdXkKFxRA7G7K9vggoBa-hiI8rmpB-IgyMpl8P3k_6SYqCBOw0HbNePs8?purpose=inline)

[pdq.com](https://www.pdq.com/blog/sql-full-outer-join/?utm_source=chatgpt.com)

```
SELECT Student.Name, Department.Dept_Name
FROM Student
FULL OUTER JOIN Department
ON Student.Dept_ID = Department.Dept_ID;
```

Note: Some DBMSs, including MySQL and SQLite, do not support the FULL OUTER JOIN syntax directly.

5\. CROSS JOIN

Returns the Cartesian product of two tables.

```
SELECT *
FROM Student
CROSS JOIN Department;
```

If the first table has 3 rows and the second has 4 rows, the result has 12 rows.

6\. SELF JOIN

A table is joined with itself.

```
SELECT A.Name, B.Name
FROM Employee A
JOIN Employee B
ON A.Manager_ID = B.Employee_ID;
```

### JOIN Summary

| Join            | Result                    |
| --------------- | ------------------------- |
| INNER JOIN      | Matching rows only        |
| LEFT JOIN       | All left rows + matches   |
| RIGHT JOIN      | All right rows + matches  |
| FULL OUTER JOIN | All rows from both tables |
| CROSS JOIN      | Cartesian product         |
| SELF JOIN       | Table joined with itself  |

# UNIT 9: NORMALIZATION

## 28. What is Normalization?

Normalization is the process of organizing data in a database to reduce redundancy and prevent data anomalies.

Its main objectives are:

- Reduce duplicate data.
- Improve data consistency.
- Avoid insertion anomalies.
- Avoid update anomalies.
- Avoid deletion anomalies.
- Improve database structure.

## 29. Database Anomalies

1\. Insertion Anomaly

Occurs when data cannot be inserted without adding unrelated data.

Example: A new department cannot be stored unless at least one student is enrolled.

2\. Update Anomaly

Occurs when the same information is stored in multiple places and all copies are not updated.

Example: Changing a department name in only some records creates inconsistent information.

3\. Deletion Anomaly

Occurs when deleting one record unintentionally removes other important information.

Example: Deleting the last student of a department also removes the only stored record of that department.

## 30. Normal Forms

### First Normal Form (1NF)

A table is in 1NF when:

- Each cell contains a single atomic value.
- There are no repeating groups.
- Each row can be uniquely identified.

Not in 1NF:

| Student_ID | Name  | Phone      |
| ---------- | ----- | ---------- |
| 1          | Rahul | 9876, 8765 |

In 1NF:

| Student_ID | Name  | Phone |
| ---------- | ----- | ----- |
| 1          | Rahul | 9876  |
| 1          | Rahul | 8765  |

### Second Normal Form (2NF)

A table is in 2NF if:

1. It is already in 1NF.
2. Every non-prime attribute is fully functionally dependent on every candidate key.

It removes partial dependencies.

Example:

Consider:

`Enrollment(Student_ID, Course_ID, Student_Name, Course_Name, Marks)`

Composite key: (Student_ID, Course_ID).

Dependencies:

- Student_ID → Student_Name
- Course_ID → Course_Name
- (Student_ID, Course_ID) → Marks

Student_Name depends only on Student_ID, and Course_Name depends only on Course_ID. These are partial dependencies.

Decompose into:

Student Table

| Student_ID | Student_Name |
| ---------- | ------------ |
| 1          | Rahul        |

Course Table

| Course_ID | Course_Name |
| --------- | ----------- |
| 101       | DBMS        |

Enrollment Table

| Student_ID | Course_ID | Marks |
| ---------- | --------- | ----- |
| 1          | 101       | 90    |

### Third Normal Form (3NF)

A table is in 3NF if:

1. It is already in 2NF.
2. It has no transitive dependency of non-prime attributes on candidate keys.

Example:

`Student(Student_ID, Student_Name, Dept_ID, Dept_Name)`

Dependencies:

- Student_ID → Dept_ID
- Dept_ID → Dept_Name

Therefore, Student_ID indirectly determines Dept_Name through Dept_ID.

Decompose into:

Student Table

| Student_ID | Student_Name | Dept_ID |
| ---------- | ------------ | ------- |
| 1          | Rahul        | 10      |

Department Table

| Dept_ID | Dept_Name |
| ------- | --------- |
| 10      | CSE       |

### Boyce-Codd Normal Form (BCNF)

A relation is in BCNF if, for every non-trivial functional dependency X → Y, X must be a super key.

BCNF is stricter than 3NF.

4NF (Fourth Normal Form)

A table is in 4NF if:

- It is in BCNF.
- It contains no non-trivial multivalued dependency unless its determinant is a super key.

5NF (Fifth Normal Form)

A table is in 5NF if:

- It is in 4NF.
- Every non-trivial join dependency is implied by candidate keys.

### Normalization Summary

| Normal Form | Main Requirement                                       |
| ----------- | ------------------------------------------------------ |
| 1NF         | Atomic values; no repeating groups                     |
| 2NF         | 1NF + no partial dependency                            |
| 3NF         | 2NF + no transitive dependency of non-prime attributes |
| BCNF        | Every determinant is a super key                       |
| 4NF         | No problematic multivalued dependencies                |

\| 5NF | No problematic join dependencies |

[What Is Normalization 1nf 2nf 3nf Bcnf Database Example 1158x774](https://images.openai.com/static-rsc-4/q7F5Z3gEHQzv-L_jLdUzpPBOeZMtmrkIXwS1LJa1iso3xWsXzUjzpMTyXGjrex3ZI9r7ZtVsoC_rnXmxkc7XE4LvDG8IacddkgTMTsl-LSZE9rm8C6N_lffDUOca0zFBqa0UM496oV4AArNmu0ZIm4OFOYcjDAZDIIIdVHtqgaE?purpose=inline)

[narodnatribuna.info](https://narodnatribuna.info/lists/e/what-is-normalization-1nf-2nf-3nf-bcnf-database-example/?utm_source=chatgpt.com)

# UNIT 10: FUNCTIONAL DEPENDENCY

## 31. What is Functional Dependency?

A functional dependency describes a relationship between attributes in a database.

If attribute X uniquely determines attribute Y, it is represented as:

\\[ X \rightarrow Y \\]

Example:

\\[ Student\\\_ID \rightarrow Student\\\_Name \\]

This means that each Student_ID determines exactly one Student_Name.

### Types of Functional Dependencies

1. Trivial Functional Dependency: Y is a subset of X.
2. Non-Trivial Functional Dependency: Y is not a subset of X.
3. Full Functional Dependency: An attribute depends on the entire candidate key.
4. Partial Dependency: An attribute depends on only part of a composite candidate key.
5. Transitive Dependency: X determines Y, and Y determines Z, so X indirectly determines Z.

### Armstrong's Axioms

These are fundamental inference rules for functional dependencies.

1\. Reflexivity

If Y is a subset of X, then:

\\[ X \rightarrow Y \\]

2\. Augmentation

If:

\\[ X \rightarrow Y \\]

Then:

\\[ XZ \rightarrow YZ \\]

3\. Transitivity

If:

\\[ X \rightarrow Y,\quad Y \rightarrow Z \\]

Then:

\\[ X \rightarrow Z \\]

# UNIT 11: TRANSACTIONS IN DBMS

## 32. What is a Transaction?

A transaction is a logical unit of work that consists of one or more database operations.

Example: Transferring ₹1,000 from Account A to Account B.

Operations:

1. Deduct ₹1,000 from Account A.
2. Add ₹1,000 to Account B.

Both operations must be completed successfully for the transaction to be successful.

## 33. ACID Properties

ACID properties ensure reliable transaction processing.

[System Design Series Part 4: Database Design & Sharding - Wasil Zafar](https://images.openai.com/static-rsc-4/JScSqdypouosQi5Ukh8Fxj2p2XGQeNCW9Vt8ubBmGR96LYeUehR9yrXbiKhVmwgqMQxWk0BdsbpcB7jm0Jl9rjKIeXDjuYfanbpBjUb2U1MBr-nRqH1s6hm-gIzhBIy-VTZsfm3gGX6j0ALcYwcm6d3Bqqmaye3Nn1G2bj19qFA?purpose=inline)

[wasilzafar.com](https://www.wasilzafar.com/pages/series/system-design/system-design-database-sharding.html?utm_source=chatgpt.com)

A – Atomicity

A transaction is treated as a single unit. Either all operations are completed or none are applied.

Example: If money is deducted but cannot be credited, the deduction must be rolled back.

C – Consistency

A transaction must move the database from one valid state to another valid state while preserving constraints.

Example: A bank balance must follow defined business rules.

I – Isolation

Concurrent transactions should not interfere with one another in ways that violate the required isolation guarantees.

Example: Two users transferring money at the same time should not cause incorrect balances.

D – Durability

Once a transaction is committed, its changes must survive system failures, subject to the database's durability guarantees.

Example: A completed bank transfer should remain recorded even after a restart.

### ACID Summary

| Property    | Meaning                                    |
| ----------- | ------------------------------------------ |
| Atomicity   | All or nothing                             |
| Consistency | Maintains valid database state             |
| Isolation   | Controls interference between transactions |
| Durability  | Committed changes persist                  |

## 34. Transaction States

A transaction passes through several states:

1. Active: Transaction is executing.
2. Partially Committed: Final statement has executed, but commit is not yet fully completed.
3. Committed: Transaction completed successfully.
4. Failed: Transaction cannot proceed.
5. Aborted: Transaction has been rolled back.
6. Terminated: Transaction has finished.

   [ACID Properties in DBMS - Scaler Topics](https://images.openai.com/static-rsc-4/QuLDjhMG1k67LMU_bFCK-VpgAVF1CBHShSPHIx30loo66dnSmU_jFaNxitJAgVITtEojZstpb23ZZTzig3yuaO9X72w01934C2wX5VvNCdYqnxvmQwFz4m43bOg997PQ6jXTSNuIsPdHAVpb6bqxWbajwYGRE1Fh-2mL67djic0?purpose=inline)

   [scaler.com](https://www.scaler.com/topics/dbms/acid-properties-in-dbms/?utm_source=chatgpt.com)

# UNIT 12: CONCURRENCY CONTROL

## 35. What is Concurrency Control?

Concurrency control is the process of managing multiple transactions executing simultaneously while maintaining database consistency.

It prevents conflicts between concurrent operations.

### Problems in Concurrent Transactions

1\. Lost Update Problem

Occurs when one transaction overwrites the update made by another transaction.

2\. Dirty Read Problem

Occurs when one transaction reads uncommitted data written by another transaction.

3\. Non-Repeatable Read

Occurs when the same row is read twice and returns different committed values because another transaction updated it.

4\. Phantom Read

Occurs when repeating a query returns additional or missing rows because another transaction inserted or deleted matching records.

## 36. Lock-Based Protocol

Locks control access to database items.

### Types of Locks

1\. Shared Lock (S-Lock)

Allows multiple transactions to read the same data.

2\. Exclusive Lock (X-Lock)

Allows a transaction to read and write data while preventing conflicting access.

### Two-Phase Locking (2PL)

Two-phase locking is a concurrency control protocol.

It has two phases:

1. Growing Phase: A transaction can acquire locks but cannot release them.
2. Shrinking Phase: A transaction can release locks but cannot acquire new locks.

   [Two Phase Locking Protocol | Scaler Topics](https://images.openai.com/static-rsc-4/oa2pWPTKIkTAII1ByO3O-zXJSd50tNA6YPEnx7Zci2yIxbxEc4aBJ-fyfEAOXoPfabam_GOC43q3s2ARKcrnyiLd2EJcEJ_XlS32gYqOs27EHqCSrgfB5T7V-SDjzzckqYI-_gLGBXltTHOqqS9-IGXHwyhjGiw0RA6_EJzXvX4?purpose=inline)

   [scaler.com](https://www.scaler.com/topics/two-phase-locking-protocol/?utm_source=chatgpt.com)

### Types of 2PL

- Basic 2PL
- Conservative 2PL
- Strict 2PL
- Rigorous 2PL

## 37. Deadlock

A deadlock occurs when two or more transactions wait indefinitely for resources held by one another.

Example:

- Transaction T1 holds Resource A and waits for Resource B.
- Transaction T2 holds Resource B and waits for Resource A.

Neither transaction can proceed.

### Deadlock Handling

1. Deadlock Prevention: Ensure deadlock cannot occur.
2. Deadlock Avoidance: Grant resources only when a safe state is maintained.
3. Deadlock Detection: Identify deadlocks using a wait-for graph.
4. Deadlock Recovery: Abort or roll back one or more transactions.

# UNIT 13: INDEXING IN DBMS

## 38. What is Indexing?

Indexing is a technique used to improve the speed of data retrieval from a database table.

An index is a separate data structure that helps the database locate records without scanning the entire table.

Example:

A book index helps readers find a topic without reading every page.

[System Design Concepts - by Neo Kim](https://images.openai.com/static-rsc-4/nx5hBZxTHn_c49yxHKv-588FkY6QVsLNtotvf1MH5Sd0aeg3aP2L1kbdUhYXZMIp-mfairjEMgPEf6VX0nbb-kvO0GLC4O8gs6xuBvprT3lrtpBOK9eTobfBH2LtEp7b6sQSpQflnBMBtNrBdJXs0NlFunBq1RRefrL2qSPCtZI?purpose=inline)

[newsletter.systemdesign.one](https://newsletter.systemdesign.one/p/system-design-concepts?utm_source=chatgpt.com)

### Advantages of Indexing

- Faster data retrieval.
- Improves query performance.
- Helps with searching and sorting.
- Can improve JOIN performance.

### Disadvantages of Indexing

- Requires additional storage.
- Increases INSERT operation overhead.
- Increases UPDATE operation overhead.
- Increases DELETE operation overhead.
- Requires maintenance.

## 39. Types of Indexing

1\. Primary Index

An index associated with the primary key or ordering key of a file, depending on the storage organization.

2\. Secondary Index

An additional index built on a non-ordering attribute.

3\. Clustered Index

An index that determines or closely corresponds to the physical organization of table data. Exact implementation varies by DBMS.

4\. Non-Clustered Index

An index stored separately from the actual table data and containing references to records.

5\. Dense Index

Contains an index entry for every search-key value or record, depending on the structure.

6\. Sparse Index

Contains entries for only some search-key values, usually when the data is ordered.

7\. Composite Index

An index created using multiple columns.

Example:

```
CREATE INDEX idx_student
ON Student(Name, Age);
```

## 40. B-Tree and B+ Tree

### B-Tree

A B-Tree is a balanced tree data structure used for efficient searching, insertion, and deletion.

### B+ Tree

A B+ Tree is a balanced tree where:

- Internal nodes store search keys and child pointers.
- Actual data entries or record pointers are stored at leaf level.
- Leaf nodes are linked for efficient sequential and range access.

  [Chapter 14: Indexing - ddccffq's Blog](https://images.openai.com/static-rsc-4/WZDY3EiRsL8Ttpg6H1eQftoKFtUqPI-7C-HQgpVBiHJUGz_J1NNdIouZKNz2JpDnQmojRCesGclreCXmyGsmy_QJ1miO_nA0kdW5QpwmA1HRp8xON69HawbsM5peNvysWG0d83dPvK2vTnov0Ss-L6BMq0iF7lrybi59yygCMro?purpose=inline)

  [ddccffq.github.io](https://ddccffq.github.io/2025/12/01/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F%E5%8E%9F%E7%90%86/Indexing/?utm_source=chatgpt.com)

B+ Trees are widely used in database indexing because of their efficient range queries and disk access patterns.

# UNIT 14: DATABASE SECURITY

## 41. What is Database Security?

Database security refers to the techniques and policies used to protect databases from unauthorized access, modification, disclosure, or destruction.

### Main Security Techniques

1. Authentication: Verifies user identity.
2. Authorization: Determines what users can access.
3. Access Control: Restricts database operations.
4. Encryption: Protects data using cryptographic techniques.
5. Auditing: Tracks database activities.
6. Backup: Creates copies of database data.
7. Password Protection: Secures user accounts.
8. Role-Based Access Control: Assigns permissions based on user roles.

### Types of Database Users

- Database Administrator (DBA)
- Database Designer
- Application Programmer
- End User
- System Analyst
- Database Operator

## 42. Database Administrator (DBA)

A Database Administrator is responsible for managing and maintaining the database system.

### Responsibilities of DBA

1. Database installation and configuration.
2. Database design and maintenance.
3. User account management.
4. Security management.
5. Backup and recovery.
6. Performance monitoring.
7. Database optimization.
8. Storage management.
9. Troubleshooting.
10. Ensuring database availability.

# UNIT 15: BACKUP AND RECOVERY

## 43. What is Database Backup?

Database backup is the process of creating a copy of database data to protect against data loss.

### Types of Backup

1\. Full Backup

Copies the entire database.

2\. Incremental Backup

Copies changes made since the most recent backup of any type.

3\. Differential Backup

Copies changes made since the most recent full backup.

4\. Transaction Log Backup

Copies transaction log records to help restore the database to a specific point in time, where supported.

## 44. Database Recovery

Database recovery is the process of restoring a database to a correct and consistent state after a failure.

### Types of Database Failures

1. Transaction Failure
2. System Crash
3. Disk Failure
4. Software Failure
5. Human Error
6. Network Failure

### Recovery Techniques

- Log-Based Recovery
- Checkpointing
- Shadow Paging
- Backup Restoration
- Rollback and Redo Operations

Undo: Reverses changes made by transactions that should not remain.

Redo: Reapplies changes that need to be preserved during recovery.

# UNIT 16: VIEWS AND STORED PROCEDURES

## 45. What is a View?

A view is a virtual table created using the result of an SQL query.

It generally stores the query definition rather than a separate copy of the underlying data.

Example:

```
CREATE VIEW Student_View AS
SELECT Student_ID, Name
FROM Student;
```

Retrieve view data:

```
SELECT * FROM Student_View;
```

### Advantages of Views

- Improves security.
- Simplifies complex queries.
- Provides customized data presentation.
- Hides unnecessary columns.
- Helps maintain logical data independence.

### Types of Views

1. Simple View
2. Complex View
3. Materialized View

A materialized view stores the result of a query physically and must be refreshed according to the DBMS and configuration.

## 46. What is a Stored Procedure?

A stored procedure is a named collection of SQL statements stored in a database and executed when called.

Example (MySQL):

```
DELIMITER //

CREATE PROCEDURE GetStudents()
BEGIN
    SELECT * FROM Student;
END //

DELIMITER ;
```

Execute:

```
CALL GetStudents();
```

### Advantages

- Code reusability.
- Reduces repeated SQL code.
- Improves maintainability.
- Can reduce network communication.
- Supports centralized business logic.

## 47. What is a Trigger?

A trigger is a database program that automatically executes when a specified database event occurs.

Examples of events:

- INSERT
- UPDATE
- DELETE

Example (MySQL):

```
CREATE TRIGGER before_student_insert
BEFORE INSERT ON Student
FOR EACH ROW
SET NEW.Name = TRIM(NEW.Name);
```

### Types of Triggers

- BEFORE Trigger
- AFTER Trigger
- INSTEAD OF Trigger (supported by some DBMSs)
- Row-Level Trigger
- Statement-Level Trigger

# UNIT 17: RELATIONAL ALGEBRA

## 48. What is Relational Algebra?

Relational algebra is a procedural query language used to perform operations on relations (tables).

It forms a theoretical foundation for relational database query processing.

### Fundamental Operations

1\. Selection (σ)

Selects rows that satisfy a condition.

\\[ \sigma\_{Age>18}(Student) \\]

2\. Projection (π)

Selects specific columns.

\\[ \pi\_{Name,Age}(Student) \\]

3\. Union (∪)

Combines tuples from two union-compatible relations.

\\[ R \cup S \\]

4\. Set Difference (−)

Returns tuples present in one relation but not the other.

\\[ R-S \\]

5\. Cartesian Product (×)

Combines every tuple of one relation with every tuple of another.

\\[ R \times S \\]

6\. Rename (ρ)

Renames a relation or its attributes.

\\[ \rho\_{NewStudent}(Student) \\]

### Additional Operations

- Intersection (∩)
- Join (⋈)
- Division (÷)

# UNIT 18: NOSQL DATABASE

## 49. What is NoSQL?

NoSQL stands for Not Only SQL.

It refers to database systems designed to store and process data using models other than the traditional relational table model, or with flexible relational alternatives.

NoSQL databases are commonly used for large-scale applications, flexible data structures, and distributed systems.

### Types of NoSQL Databases

1\. Document Database

Stores data in document formats such as JSON-like structures.

Example: MongoDB.

```
{
  "student_id": 101,
  "name": "Rahul",
  "course": "B.Tech"
}
```

2\. Key-Value Database

Stores data as key-value pairs.

Example: Redis.

3\. Column-Family Database

Stores data in column families.

Example: Apache Cassandra.

4\. Graph Database

Stores data as nodes and relationships.

Example: Neo4j.

[SQL vs NoSQL: A Comparison of Database Technologies for Data Engineers | Airbyte](https://images.openai.com/static-rsc-4/OOVZvuG7W6j1l6FnRgSSQCLKIWWRf1smuJBGvKtaezrFSfAqia6ZkUoX0wdhzhKC9ZnoOeGPH1kvqGgOAg_O_wLUKbKFHDgC_6_cgsRyqeRGer07mrmRl1rBW3gB_iUhPRV4JH81-C14oy_Zuhpo9e5x-WO_ce87d2BNWbYht6Y?purpose=inline)

[airbyte.com](https://airbyte.com/data-engineering-resources/sql-vs-nosql?utm_source=chatgpt.com)

## 50. Difference Between SQL and NoSQL

| SQL Database                     | NoSQL Database                     |
| -------------------------------- | ---------------------------------- |
| Relational model                 | Multiple data models               |
| Tables with rows and columns     | Documents, key-value, graphs, etc. |
| Usually predefined schemas       | Often flexible schemas             |
| Supports SQL                     | Query methods vary                 |
| Relationships commonly use JOINs | Relationships handled differently  |
| Strong relational constraints    | Consistency and constraints vary   |
| Examples: MySQL, PostgreSQL      | MongoDB, Redis, Cassandra          |

# UNIT 19: DISTRIBUTED DATABASE

## 51. What is a Distributed Database?

A distributed database is a collection of logically related databases distributed across multiple physical locations and connected through a network.

[Distribution Model in NoSql. When it comes to NoSql one thing to… | by Tejas shelke | Medium](https://images.openai.com/static-rsc-4/YvyWVivE4WQpNCdwJBOTD5nSB33EE1tDbwWwEFSuB4RzDVcewL1jDK9aeto6k9wsXvNQLJaawRcyIrnLEOeq9ToEewFQbS2344_NEAltsDG0n7SV_Bj4xFGGBxBeq3JUeXAk5J8BfVmaVNdRPiABmkMFboCTvchAXW0RcdMy6Lo?purpose=inline)

[medium.com](https://medium.com/%40tejsshelke8/distribution-model-in-nosql-9244edc424bc?utm_source=chatgpt.com)

### Advantages

- Improved availability.
- Better scalability.
- Data can be stored closer to users.
- Supports distributed workloads.
- Can improve fault tolerance.

### Disadvantages

- Complex management.
- Network dependency.
- Distributed transaction challenges.
- Security management is more difficult.
- Data consistency can be challenging.

### Types of Distributed Databases

1. Homogeneous Distributed Database: Uses the same DBMS at different locations.
2. Heterogeneous Distributed Database: Uses different DBMSs at different locations.

### Data Distribution Techniques

1\. Fragmentation

Dividing a database into smaller parts.

- Horizontal Fragmentation
- Vertical Fragmentation
- Mixed Fragmentation

2\. Replication

Maintaining copies of data at multiple locations.

3\. Allocation

Deciding where database fragments or replicas should be stored.

# UNIT 20: CAP THEOREM

## 52. What is CAP Theorem?

The CAP theorem describes three properties of distributed data systems:

C – Consistency

Every read receives the latest successful write or an error, according to the consistency model.

A – Availability

Every request to a non-failing node receives a response, although that response may not contain the latest data.

P – Partition Tolerance

The system continues operating despite communication failures between network partitions.

The CAP theorem states that when a network partition occurs, a distributed system must make a trade-off between consistency and availability.

[Understanding CAP Theorem • Mehdi Mehdikhani](https://images.openai.com/static-rsc-4/MIG4veZdHF8hwOBBWf05GcfdtZXf8qrjVZ_4MQUaaWCEyFV2DAW47SiPFpQnvLkNddHqpksRmunJRfxh00ZkMlco_g0gSHFHZt-Xg4wYXvEBkItU3TZtJuFX6YgFmTepO1GxBgA74O221GZEdLS493k9bKqtzE2cel_Wszgkmjo?purpose=inline)

[mehdik.dev](https://mehdik.dev/posts/system-design/cap-theorem/?utm_source=chatgpt.com)

# UNIT 21: IMPORTANT DIFFERENCES FOR EXAMS

## 53. DBMS vs RDBMS

| DBMS                                 | RDBMS                                    |
| ------------------------------------ | ---------------------------------------- |
| Database Management System           | Relational Database Management System    |
| General database management software | Relational database management software  |
| May use different data models        | Uses relational model                    |
| Relationships depend on the model    | Relationships are represented using keys |
| Examples: Various database systems   | MySQL, PostgreSQL, Oracle                |

## 54. DELETE vs TRUNCATE vs DROP

| DELETE                            | TRUNCATE                   | DROP                       |
| --------------------------------- | -------------------------- | -------------------------- |
| Removes selected rows or all rows | Removes all rows           | Removes entire table       |
| Supports WHERE                    | Does not support WHERE     | Does not support WHERE     |
| Table structure remains           | Table structure remains    | Table structure is removed |
| DML command                       | Commonly classified as DDL | DDL command                |
| Usually logs row-level changes    | Often uses less logging    | Removes database object    |

Transaction and rollback behavior depends on the database system.

## 55. WHERE vs HAVING

| WHERE                                                            | HAVING                       |
| ---------------------------------------------------------------- | ---------------------------- |
| Filters individual rows                                          | Filters groups               |
| Applied before GROUP BY grouping                                 | Applied after grouping       |
| Commonly used without GROUP BY                                   | Commonly used with GROUP BY  |
| Cannot directly filter aggregate results in the same query block | Can filter aggregate results |

## 56. Primary Key vs Unique Key

| Primary Key                          | Unique Key                          |
| ------------------------------------ | ----------------------------------- |
| Uniquely identifies a record         | Enforces uniqueness                 |
| Cannot contain NULL                  | NULL behavior varies by DBMS        |
| One primary key constraint per table | Multiple unique constraints allowed |
| Can be composite                     | Can be composite                    |

## 57. CHAR vs VARCHAR

| CHAR                             | VARCHAR                                    |
| -------------------------------- | ------------------------------------------ |
| Fixed-length character type      | Variable-length character type             |
| Uses fixed declared length       | Stores varying-length strings              |
| Suitable for fixed-length values | Suitable for variable-length values        |
| May use padding                  | Does not generally pad to declared maximum |

## 58. Centralized vs Distributed Database

| Centralized Database                  | Distributed Database                        |
| ------------------------------------- | ------------------------------------------- |
| Stored at one central location        | Stored across multiple locations            |
| Easier administration                 | More complex administration                 |
| Central point of failure              | Can provide greater fault tolerance         |
| Network access may be needed remotely | Supports geographically distributed storage |
| Limited distribution                  | Supports distributed operations             |

# UNIT 22: IMPORTANT DBMS INTERVIEW QUESTIONS

## Basic Questions

1\. What is DBMS?

DBMS is software that allows users to create, store, retrieve, update, and manage data in a database.

2\. What is RDBMS?

RDBMS is a type of DBMS that stores data in related tables consisting of rows and columns.

3\. What is SQL?

SQL is a standard language used to manage and retrieve data from relational databases.

4\. What is a primary key?

A primary key uniquely identifies every record in a table and cannot contain NULL values.

5\. What is a foreign key?

A foreign key is an attribute that references a candidate key in another or the same table.

6\. What is normalization?

Normalization is the process of organizing database tables to reduce redundancy and prevent anomalies.

7\. What is denormalization?

Denormalization is the intentional introduction of redundancy or precomputed data to improve read performance in certain situations.

8\. What is a tuple?

A tuple is a row in a relational table.

9\. What is an attribute?

An attribute is a column in a relational table.

10\. What is a schema?

A schema defines the structure and organization of a database.

## Intermediate Questions

11\. What are ACID properties?

Atomicity, Consistency, Isolation, and Durability.

12\. What is a JOIN?

A JOIN combines records from two or more tables using related columns.

13\. What is an index?

An index is a data structure that helps retrieve database records efficiently.

14\. What is a view?

A view is a virtual table based on an SQL query.

15\. What is a trigger?

A trigger is a database program that executes automatically in response to specified events.

16\. What is a deadlock?

A deadlock occurs when transactions wait indefinitely for resources held by each other.

17\. What is a candidate key?

A candidate key is a minimal set of attributes that uniquely identifies a record.

18\. What is a composite key?

A composite key consists of two or more attributes used together to uniquely identify a record.

19\. What is data independence?

Data independence is the ability to modify one schema level without requiring changes to the next higher level.

20\. What is concurrency control?

Concurrency control manages simultaneous transactions while preserving database correctness.

## Advanced Questions

21\. What is BCNF?

BCNF is a normal form in which every determinant of a non-trivial functional dependency is a super key.

22\. What is two-phase locking?

It is a concurrency control protocol that divides locking into growing and shrinking phases.

23\. What is a phantom read?

A phantom read occurs when repeating a query returns a different set of rows because another transaction changed matching records.

24\. What is a B+ Tree?

A B+ Tree is a balanced indexing structure in which data entries or record pointers are stored at the leaf level.

25\. What is a distributed database?

A distributed database stores logically related data across multiple physical locations.

26\. What is referential integrity?

Referential integrity ensures that foreign key values correctly reference existing records in the referenced table, subject to NULL and constraint rules.

27\. What is query optimization?

Query optimization is the process of selecting an efficient execution plan for a database query.

28\. What is a subquery?

A subquery is a query nested inside another SQL query.

29\. What is a correlated subquery?

A correlated subquery is a subquery that references columns from its outer query and is logically evaluated in relation to the outer query's rows.

30\. What is a database cursor?

A cursor is a database mechanism used to process query results row by row.

# UNIT 23: IMPORTANT SQL PRACTICE QUESTIONS

Use the following table for practice.

```
CREATE TABLE Employee (
    Emp_ID INT PRIMARY KEY,
    Emp_Name VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10,2),
    Age INT
);
```

Insert sample records:

```
INSERT INTO Employee VALUES
(1, 'Rahul', 'IT', 50000, 25),
(2, 'Priya', 'HR', 40000, 24),
(3, 'Aman', 'IT', 60000, 27),
(4, 'Neha', 'Finance', 45000, 26),
(5, 'Rohit', 'HR', 35000, 23);
```

### Practice Queries

Q1. Display all employees.

```
SELECT * FROM Employee;
```

Q2. Display employees whose salary is greater than 40,000.

```
SELECT *
FROM Employee
WHERE Salary > 40000;
```

Q3. Display employee names in alphabetical order.

```
SELECT Emp_Name
FROM Employee
ORDER BY Emp_Name ASC;
```

Q4. Find the highest salary.

```
SELECT MAX(Salary)
FROM Employee;
```

Q5. Find the average salary.

```
SELECT AVG(Salary)
FROM Employee;
```

Q6. Count total employees.

```
SELECT COUNT(*)
FROM Employee;
```

Q7. Find department-wise employee count.

```
SELECT Department, COUNT(*)
FROM Employee
GROUP BY Department;
```

Q8. Find department-wise average salary.

```
SELECT Department, AVG(Salary)
FROM Employee
GROUP BY Department;
```

Q9. Find employees whose names start with R.

```
SELECT *
FROM Employee
WHERE Emp_Name LIKE 'R%';
```

Q10. Find the second-highest distinct salary.

```
SELECT MAX(Salary)
FROM Employee
WHERE Salary < (
    SELECT MAX(Salary)
    FROM Employee
);
```

# UNIT 24: IMPORTANT FULL FORMS

| Abbreviation | Full Form                                      |
| ------------ | ---------------------------------------------- |
| DBMS         | Database Management System                     |
| RDBMS        | Relational Database Management System          |
| SQL          | Structured Query Language                      |
| DDL          | Data Definition Language                       |
| DML          | Data Manipulation Language                     |
| DQL          | Data Query Language                            |
| DCL          | Data Control Language                          |
| TCL          | Transaction Control Language                   |
| ER           | Entity Relationship                            |
| ACID         | Atomicity, Consistency, Isolation, Durability  |
| DBA          | Database Administrator                         |
| BCNF         | Boyce-Codd Normal Form                         |
| 1NF          | First Normal Form                              |
| 2NF          | Second Normal Form                             |
| 3NF          | Third Normal Form                              |
| 4NF          | Fourth Normal Form                             |
| 5NF          | Fifth Normal Form                              |
| OLTP         | Online Transaction Processing                  |
| OLAP         | Online Analytical Processing                   |
| NoSQL        | Not Only SQL                                   |
| JDBC         | Java Database Connectivity                     |
| ODBC         | Open Database Connectivity                     |
| CRUD         | Create, Read, Update, Delete                   |
| CAP          | Consistency, Availability, Partition Tolerance |
| XML          | Extensible Markup Language                     |
| JSON         | JavaScript Object Notation                     |

# UNIT 25: IMPORTANT EXAMINATION QUESTIONS

## 1-Mark Questions

1. Define DBMS.
2. What is a database?
3. What is SQL?
4. Define primary key.
5. What is a foreign key?
6. What is a tuple?
7. What is an attribute?
8. Define normalization.
9. What is a transaction?
10. Expand ACID.

## 4-Mark Questions

1. Explain the characteristics of DBMS.
2. Differentiate between DBMS and RDBMS.
3. Explain different types of keys.
4. Explain different types of SQL commands.
5. Explain the types of joins.
6. Explain the advantages and disadvantages of DBMS.
7. Explain data independence.
8. Explain the different types of attributes.
9. Explain database constraints.
10. Differentiate between DELETE, DROP, and TRUNCATE.

## 10-Mark Questions

1. Explain DBMS architecture with a suitable diagram.
2. Explain the ER model and its components.
3. Explain normalization from 1NF to BCNF with examples.
4. Explain ACID properties in detail.
5. Explain SQL commands with suitable examples.
6. Explain different types of joins with diagrams and examples.
7. Explain concurrency control and deadlock management.
8. Explain indexing and different types of indexes.
9. Explain relational algebra and its operations.
10. Explain distributed databases and the CAP theorem.

# DBMS COMPLETE REVISION ROADMAP

Use this checklist to track your preparation.

Your DBMS Preparation

# 0%

0 of 24 topics completed

Introduction to DBMS

DBMS Architecture

Data Models

ER Model

Relational Database Model

Keys in DBMS

SQL Commands

SQL Operators and Clauses

SQL Joins

Normalization

Functional Dependencies

Transactions and ACID

Concurrency Control

Indexing

Database Security

Backup and Recovery

Views, Procedures and Triggers

Relational Algebra

NoSQL Databases

Distributed Databases and CAP Theorem

Important Differences

SQL Practice

Interview Questions

Full Forms and Exam Revision

Reset Progress

Recommended study order: First understand DBMS fundamentals and architecture, then ER diagrams and keys, followed by SQL, normalization, transactions, concurrency control, and indexing. Finally, practise SQL queries and revise the examination questions.

These notes provide a complete foundation for college examinations, viva preparation, and entry-level DBMS interviews.