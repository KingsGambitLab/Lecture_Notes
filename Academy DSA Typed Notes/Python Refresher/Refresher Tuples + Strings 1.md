# Refresher: Tuples + Strings 1
# Introduction to Tuples


### Introduction

We delve into the fundamentals of Tuples and Strings in Python, two powerful data types that play a crucial role in various programming scenarios. Let's start by understanding the essence of Tuples.

## Planets Example

Let's start with an example using an array to store the names of all the planets in our solar system.

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
```

### Adding the Sun
Now, imagine we someone is trying to include the Sun in our list of planets. Since arrays in Python are mutable, someone might be tempted to do this:

```python
planets.append("Sun")
```

However, this is where mutability can lead to errors. While the code above will add "Sun" to the list, it's not accurate to consider the Sun a planet. This illustrates a potential problem with mutable structures when trying to maintain data integrity.

## Tuples

### Definition

Now, let's explore tuples - a different kind of data structure. Tuples are similar to arrays but are immutable. This immutability provides certain advantages, especially in situations where data integrity is crucial.


### Creating Tuples with Numbers
We can create a tuple with numbers like this:

```python
# Definition
a = (1, 2, 3, 4)
print(type(a))  # Output: <class 'tuple'>

# Exception
b = (1,)
print(type(b))  # Output: <class 'tuple'>

c = (1, 2)
print(type(c))  # Output: <class 'tuple'>

d = ()
print(type(d))  # Output: <class 'tuple'>
```

#### Explanation

 - In the first example, `a` is a tuple containing the numbers 1 through 4. The `type` function confirms that it's indeed a tuple.
 - The second example, `b`, demonstrates the need for a comma even when creating a tuple with a single element. Without the comma, Python interprets it as a different data type.
 - The third example, `c`, is a tuple with two elements.
 - The fourth example, `d`, is an empty tuple.

### Creating Tuples with the range Keyword
Tuples can also be created using the `range` keyword:

```python
a = tuple(range(10))
print(type(a))  # Output: <class 'tuple'>
print(a)        # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

#### Explanation

In this example, `a` is a tuple created using the `tuple` constructor with the `range(10)` function, resulting in a tuple with the numbers 0 through 9.


### Tuples in Functions

Consider the following function that swaps the values of two variables:

```python
def swap(a, b):
    return b, a

a, b = swap(2, 3)
```

#### Explanation

In this example, the `swap` function takes two parameters `a` and `b`. Then the function creates and returns a tuple. When the function is called with `swap(2, 3)`, it returns a tuple containing the values of `b` and `a`. This tuple is then unpacked into the variables `a` and `b` on the left side of the assignment statement.

After this line executes, `a` will have the value `3`, and `b` will have the value `2`. This is a powerful and elegant way to swap the values of two variables without needing a temporary variable.

### Partially Immutable Tuples

Consider the following example of a partially immutable tuple:

```python
# Partially Immutable
a = (1, 2, 3, ['a', 'b'])
a[3].append('c')
print(a)
```

### Output

The output of this code will be:

```plaintext
(1, 2, 3, ['a', 'b', 'c'])
```

### Explanation

Tuples themselves are immutable, but the elements within them may be mutable. In this case, the list inside the tuple is mutable. The line `a[3].append('c')` accesses the fourth element of the tuple (which is a list) and appends the string 'c' to it. Even though the tuple is partially immutable, the list inside it can be modified.



---
### Question

What will be the output of the following?
```python
t = (1, 2, 3)
t[0] = 4
print(t)
```

**Choices**

- [ ] (4, 2, 3)
- [ ] (1, 2, 3)
- [x] Error

Tuples in Python are immutable, meaning their elements cannot be modified after creation. In the given code, attempting to assign a new value (`4`) to the first element of the tuple (`t[0]`) will result in an error.


---
### Question

What will be the output of the following?
```python
a = 23
t = (a)
print(type(t))
```

**Choices**

- [ ] tuple
- [ ] list
- [ ] str
- [x] int

The code assigns the value 23 to the variable 'a' and then creates a tuple 't' with a single element, which is the value of 'a'. When the type of 't' is printed, it will output 'int' because the tuple contains only one integer element.


---
### Question

What will be the output of the following?
```python
t = (10, 20, 30, 40)
print(t[1:-1])
```

**Choices**

- [ ] 10, 20, 30
- [ ] Nothing
- [ ] 20, 30, 40
- [x] 20, 30


The slice `t[1:-1]` extracts elements from index 1 to one position before the last index (-1) in the tuple `t`, resulting in the elements 20 and 30 being printed.

---
## Strings in Python

## Strings

### String Literals

Strings in Python can be created using single quotes (`'`) or double quotes (`"`). Both forms are equivalent, and you can choose the one that suits your preference. Here's an example:

```python
a = "abc"
b = 'abc'
print(type(a))
print(type(b))
```

### Output

```plaintext
<class 'str'>
<class 'str'>
```

### Explanation

In this example, both `a` and `b` are strings with the content "abc." The `type` function confirms that they are indeed string objects. Python treats single and double quotes as equivalent for defining strings.

### ASCII and Related Functions

ASCII (American Standard Code for Information Interchange) is a character encoding standard that represents each character with a unique number. Python provides `ord` and `chr` functions to work with ASCII values.

```python
print(ord('A'))
print(ord('0'))
print(ord('9'))
print(chr(129))
```

### Output

```plaintext
65
48
57
ü
```

### Explanation

- `ord('A')` returns the ASCII value of the character 'A', which is 65.
- `ord('0')` returns the ASCII value of the digit '0', which is 48.
- `ord('9')` returns the ASCII value of the digit '9', which is 57.
- `chr(129)` returns the character corresponding to the ASCII value 129, which is 'ü'.

These functions are useful for working with character encodings and converting between characters and their ASCII representations. Keep in mind that ASCII values are integers representing characters in the ASCII table.


### Properties of Strings

Strings in Python possess several important properties, including mutability, homogeneity, iterability, and case sensitivity.

```python
# Variable
a = 'Scaler Academy'
```

### Mutability

Strings in Python are **immutable**, meaning their values cannot be changed after creation.

```python
# Attempt to modify a character in the string
a[0] = 's'
```

#### Output
```plaintext
TypeError: 'str' object does not support item assignment
```

#### Explanation

The attempt to modify the first character of the string `a` raises a `TypeError`. This demonstrates the immutability of strings.

### Homogeneity

Strings are **homogeneous**, meaning they can only contain characters of the same type.

```python
# Concatenating string and integer
result = a + 42
```

#### Output
```plaintext
TypeError: can only concatenate str (not "int") to str
```

#### Explanation

Attempting to concatenate a string (`a`) with an integer (`42`) raises a `TypeError`, emphasizing the homogeneity requirement of strings.

### Iterability

Strings are **iterable**, allowing you to loop through each character.

```python
# Iterating through each character
for char in a:
    print(char)
```

#### Output
```plaintext
S
c
a
l
e
r

A
c
a
d
e
m
y
```

#### Explanation

The `for` loop iterates through each character in the string `a`, printing them one by one.

### Case Sensitivity

Strings are **case-sensitive**, distinguishing between uppercase and lowercase characters.

```python
# Comparing strings
b = 'scaler academy'
print(a == b)
```

#### Output
```plaintext
False
```

#### Explanation

The comparison between `a` and `b` returns `False` because of case sensitivity. The uppercase 'S' in `a` is not equal to the lowercase 's' in `b`.



---
### Question

Which one of the following is a valid string?

**Choices**

- [ ] "ScaLer#'
- [ ] %adfa"
- [x] "^&abc#"
- [ ] 'academy'

The correct answer is "^&abc#". This is a valid string because it is enclosed in double quotation marks, and its contents consist of a combination of letters, numbers, and symbols.


---
### Question

What will be the output of the following?
```python
print(ord('c'))
```

**Choices**

- [ ] 98
- [x] 99
- [ ] 100
- [ ] 101

The correct answer is 99. The `ord` function in Python returns the Unicode code point of a given character. In this case, it prints the Unicode code point of the character 'c', which is 99.


---
### Question

What will be the output of the following?
```python
print(chr(70))
```

**Choices**

- [ ] C
- [ ] E
- [x] F
- [ ] G

The `chr()` function in Python returns a string representing a character whose Unicode code point is the integer passed to it. In this case, `chr(70)` returns the character with Unicode code point 70, which is 'F'. 


---
### Question

What will be the output of the following?
```python
s = 'Scaler Academy'
print(s[0:5])
```

**Choices**

- [ ] Sae
- [ ] Scaler
- [x] Scale
- [ ] cale


The code `s[0:5]` extracts the substring from index 0 to 4 (5 exclusive) from the string 'Scaler Academy', resulting in the output 'Scale'.

---
### Question

What will be the output of the following?
```python
a = '1'
b = '2'
c = a + b
print(c)
```

**Choices**

- [ ] 3
- [ ] '3'
- [x] 12
- [ ] 1 2

The correct answer is: 12

In Python, when you use the `+` operator with two strings, it concatenates them. So, `a + b` where `a` is '1' and `b` is '2' results in the string '12', and that is what will be printed.


---
### Question

What will be the output of the following?
```python
a = 'abcd'
a += 'e'
print(len(a))
```

**Choices**

- [ ] 3
- [ ] 4
- [x] 5
- [ ] 6


The code initializes a string variable 'a' with the value 'abcd', then concatenates 'e' to it using the `+=` operator. Finally, it prints the length of the modified string 'a', which is now 'abcde'. The length of 'abcde' is 5, so the output is 5.


---
## Functions in Strings

### capitalize()

The `capitalize()` method in Python is used to capitalize the first letter of a string.

```python
# Example
'john doe'.capitalize()
```

### Output
```plaintext
'John doe'
```

### Explanation

In this example, the `capitalize()` function capitalizes the first letter of the string, transforming 'john doe' into 'John doe'.

### title()

The `title()` method capitalizes the first letter of each word in a string.

```python
# Example
'sneha sudam'.title()
```

### Output
```plaintext
'Sneha Sudam'
```

### Explanation

The `title()` function capitalizes the first letter of each word in the string, resulting in 'Sneha Sudam'.

### count(substring)

The `count(substring)` method counts the occurrences of a substring in the string.

```python
# Example
'pooja nikam'.count('ni')
```

### Output
```plaintext
2
```

### Explanation

The `count()` function counts the occurrences of the substring 'ni' in the string, returning the value `2`.

### replace(old, new)

The `replace(old, new)` method replaces occurrences of the old substring with the new substring.

```python
# Example
'Vicky Sharma'.replace('a', 'e')
```

### Output
```plaintext
'Vicky Sherme'
```

### Explanation

The `replace()` function replaces occurrences of 'a' with 'e' in the string, resulting in 'Vicky Sherme'.

### replace(old, new, count)

The `replace(old, new, count)` method replaces a specified number of occurrences of the old substring with the new substring.

```python
# Example
'Vicky Sharma'.replace('a', 'e', 1)
```

### Output
```plaintext
'Vicky Sherma'
```

### Explanation

In this example, only the first occurrence of 'a' is replaced with 'e' in the string, resulting in 'Vicky Sherma'.


### split(separator)

The `split(separator)` method splits a string into a list of substrings based on the specified separator.

```python
# Example
a = 'Aakar, Saurav, Kusum'
print(a.split(','))
```

### Output
```plaintext
['Aakar', ' Saurav', ' Kusum']
```

### Explanation

The `split()` function divides the string into a list of substrings based on the specified separator (`,` in this case), resulting in `['Aakar', ' Saurav', ' Kusum']`.

```python
# Example
a = 'There——are—-many-—places——to——visit.'
print(a.split('——'))
```

### Output
```plaintext
['There', 'are', 'many', 'places', 'to', 'visit.']
```

### Explanation

The `split()` function divides the string using the specified separator (`'——'` in this case), resulting in `['There', 'are', 'many', 'places', 'to', 'visit.']`.

### Print ASCII Letter

This example takes user input and prints the ASCII values of each letter in the input string.

```python
# Example
s = input()
for char in s:
    print(ord(char), end=' ')
```

### Output (for input 'hello')
```plaintext
104 101 108 108 111
```

### Explanation

The `ord()` function is used to get the ASCII value of each character in the input string. The `end=' '` parameter ensures that the values are printed with a space in between.


### Formatted Strings

Formatted strings in Python provide a convenient way to embed variable values or expressions into a string, making it more readable and flexible. 

```python
# Example
name = 'Aakar'
gender = 'Mate'
age = 25
print('Name:—', name, 'gender:—', gender, 'age:—', age)
```

### Output
```plaintext
Name:— Aakar gender:— Mate age:— 25
```

### Explanation

In this example, a formatted string is created using the variables `name`, `gender`, and `age`, resulting in the output `Name:— Aakar gender:— Mate age:— 25`.

There are several ways to achieve string formatting in Python, but one commonly used method involves the `format()` method.

```python
# Example
template = 'Name:— {}, gender:— {}, age:— {}'
print(template.format(name, gender, age))
```

### Output
```plaintext
Name:— Aakar, gender:— Mate, age:— 25
```

### Explanation

The `format()` method is used to insert the values of `name`, `gender`, and `age` into the string template, resulting in the formatted output `Name:— Aakar, gender:— Mate, age:— 25`.

```python
# Example
template = 'Name:— {0}, gender:— {1}, age:— {2}'
print(template.format(name, gender, age))
```

### Output
```plaintext
Name:— Aakar, gender:— Mate, age:— 25
```

### Explanation

In this example, positional placeholders `{0}`, `{1}`, and `{2}` are used in the template to indicate the positions of `name`, `gender`, and `age` in the `format()` method. The output is the same as the previous example.



---
### Question

What will be the output of the following?
```python
a = 'Scaler Academy'
print(a.count('a'))
```

**Choices**

- [x] 2
- [ ] 3
- [ ] 4
- [ ] 0

The output of the given Python code will be 2. This is because the `count()` method is used to count the number of occurrences of a specified substring (in this case, the letter 'a') within the given string 'Scaler Academy'.


---
### Question

What will be the output of the following?
```python
a = 'i-am-awesome'
b = a.split('-')
print(len(b))
```

**Choices**

- [ ] 2
- [x] 3
- [ ] 4
- [ ] 5



The correct answer is 3. The code splits the string 'i-am-awesome' at each occurrence of the hyphen ('-') and creates a list `b` with three elements: ['i', 'am', 'awesome']. The `len(b)` then outputs 3, indicating the number of elements in the list.