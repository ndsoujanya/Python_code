## **Lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension**

In this video, we will learn how to use `for` loops with **Lists** and **Dictionaries**, followed by advanced techniques using **List Comprehension** and **Dictionary Comprehension**. These tools are essential for writing concise and efficient Python code.

---

### **1. Looping Through Lists**

A `for` loop is the most common way to iterate through items in a list.

#### **Example**: Sum of all numbers in a list
```python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)
```

**Output**:
```
Total sum: 150
```

#### **Example**: Doubling each number in a list
```python
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled List:", doubled)
```

**Output**:
```
Doubled List: [2, 4, 6, 8, 10]
```

#### **Example**: Printing Kannada food items
```python
foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")
```

**Output**:
```
I like Dosa
I like Idli
I like Vada
I like Bisibelebath
```

---

### **2. Looping Through Dictionaries**

You can use `for` loops to iterate over dictionaries by accessing both keys and values.

#### **Example**: Iterating over dictionary keys
```python
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(student)
```

**Output**:
```
Anand
Geetha
Kumar
```

#### **Example**: Iterating over dictionary values
```python
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for marks in student_marks.values():
    print(marks)
```

**Output**:
```
85
90
78
```

#### **Example**: Iterating over both keys and values
```python
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")
```

**Output**:
```
Anand scored 85 marks
Geetha scored 90 marks
Kumar scored 78 marks
```

---

### **3. `for` Loops with `range()`**

You can also use `for` loops with the `range()` function to loop through a sequence of numbers.

#### **Example**: Adding marks to students using index values
```python
students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)
```

**Output**:
```
{'Anand': 85, 'Geetha': 90, 'Kumar': 78}
```

---

### **4. List Comprehension**

List comprehension provides a more concise way to create lists by applying an expression to each element in an existing list.

#### **Syntax**:
```python
new_list = [expression for item in iterable if condition]
```

#### **Example 1**: Squaring numbers in a list
```python
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
```

**Output**:
```
[1, 4, 9, 16, 25]
```

#### **Example 2**: Filtering even numbers
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
```

**Output**:
```
[2, 4, 6]
```

#### **Example 3**: Uppercasing Kannada city names
```python
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
uppercased_cities = [city.upper() for city in cities]
print(uppercased_cities)
```

**Output**:
```
['BENGALURU', 'MYSURU', 'HUBBALLI', 'MANGALURU']
```

---

### **5. Dictionary Comprehension**

Similar to list comprehension, dictionary comprehension provides a concise way to create dictionaries.

#### **Syntax**:
```python
new_dict = {key_expression: value_expression for item in iterable if condition}
```

#### **Example 1**: Creating a dictionary of squares
```python
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num ** 2 for num in numbers}
print(squares_dict)
```

**Output**:
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### **Example 2**: Converting a list of names to a dictionary of name lengths
```python
names = ["Anand", "Geetha", "Kumar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)
```

**Output**:
```
{'Anand': 5, 'Geetha': 6, 'Kumar': 5}
```

#### **Example 3**: Filtering cities with population above 10 lakhs (Localized Example)
```python
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)
```

**Output**:
```
{'Bengaluru': 84, 'Mysuru': 11}
```

---

### **6. Splitting Strings to Create Lists**

In Python, the `split()` method allows you to break a string into a list of words or elements based on a specified separator (like space, comma, etc.). This is very useful when you have data in string format and want to convert it into a list.

#### **Syntax**:
```python
string.split(separator, maxsplit)
```
- **separator** (optional): The character or substring on which to split the string (default is space).
- **maxsplit** (optional): The maximum number of splits (default is unlimited).

---

#### **Example 1**: Splitting a sentence into words
```python
sentence = "I love coding in Python"
words = sentence.split()
print(words)
```

**Output**:
```
['I', 'love', 'coding', 'in', 'Python']
```
Here, the default separator (space) is used to split the string into individual words.

---

#### **Example 2**: Splitting a string with commas
```python
data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)
```

**Output**:
```
['apple', 'banana', 'mango']
```
Here, the comma (`,`) is used as the separator to split the string into different fruit names.

---

#### **Example 3**: Limiting the number of splits
```python
sentence = "Python is fun to learn"
words = sentence.split(" ", 2)
print(words)
```

**Output**:
```
['Python', 'is', 'fun to learn']
```
In this example, the string is split only twice. The rest of the string remains as the final element.

---

### **Practical Application**

You can use the `split()` method when reading data from a text file or processing input from a user where the data is separated by spaces, commas, or any other delimiters. Once you split the data, you can work with it as a list, applying any list manipulation techniques you've learned.

---

### **Homework**

1. **List Manipulation**:
   - Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

2. **Sum of Prices**:
   - Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a `for` loop.

3. **List of Squares**:
   - Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.

4. **Student Data Task**:
   - Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.

5. **Dictionary Comprehension**:
   - Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.
  
6. **Nested List Challenge**:
   Write a Python program that takes a list of lists (a 2D list) as input and:
   - Prints the entire matrix row by row.
   - Prints the sum of each row in the matrix.
   
   **Example**:
   ```python
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   ```

---
