# Refresher: Introduction To Python and Data Types

---
### Intermediate Refresher Module Description


* Refresher: Introduction To Python and Data Types
* Refresher: Operators and Control Statements
* Refresher: Iteration 1
* Refresher: Iteration 2
* Refresher: Functions
* Refresher: List 1
* Refresher: List 2
* Refresher: List 3
* Refresher: Tuples + Strings 1
* Refresher: Strings 2
* Refresher: Sets and Dictionaries
* Refresher Practice Test
    * Will be given more information later on

Let's Begin with the Content!

---
### Agenda for Today!


1. Basics of Python
    * Interpreter
    * First Program
    * Case Sensitive
3. Arithmetic Calculations
4. Data Types 
5. Variables
6. Comments
7. Type Casting
8. Lots of Quizzes Quizzes
9. Dashboard Walkthrough

---
## Introduction to Python 

* Python is a high-level language and it is a very simple language.
* Python is one of the most used languages.

---
## Python Interpreter
For the Python interpreter, we do not need to install any extra software in our system.
* You just need to open our browser.
* Search Colab Google in the browser and open the first link.
* Create a new notebook.
* Now blank environment will be opened on your screen.
* You can simply write code on it and run it.



---
## First Python Program

We will write the first program to print Hello World
```python
print("Hello World")
```

Then we will run it, then colab will automatically run it, we do not need to install Python explicitly.


**Output:**
```plaintext
Hello World
```

But colab sometimes works slowly, so we can also use jupyter notebook for Python programs.

We have learnt one thing from the above program:
- Anything written in `" "` will be printed as it is in output.

Let us try to run one more code

```python
print("Hi how are you?")
```

It will print Hi how are you? as it is.

**Output:**
```plaintext
Hi how are you?
```

If we try to print any random content by `print()`, then that will also be printed as it is:


```python
print("hjasghkjelf2176189*4#$sljhadsfghbdas")
```


**Output:**
```plaintext
hjasghkjelf2176189*4#$sljhadsfghbdas
```


---
### Question

What will be the output of this code snippet?
`print("10")`

**Choices**

- [x] 10
- [ ] "10"
- [ ] ten
- [ ] Error

**Explanation**

`print()` will not print `""`, it only prints the content written inside it.

So `print("10")` will print only `10` as output.


If we do not write `" "` in print then it will print the variable value.

```python
print(10)
```

**Output:**
```plaintext
10
```

If we do not write `" "` in print then it will perform arithmetic calculation.

```python
print(10 + 30)
```

**Output:**
```plaintext
40
```

If we write `" "` in print then it will perform string concatenation.

```python
print("10" + "30")
```

**Output:**
```plaintext
1030
```

---
### Question

Predict the output
`print("10 + 10")`

**Choices**

- [ ] 20
- [ ] "10 + 10"
- [x] 10 + 10
- [ ] Error


**Explanation**

Whatever will be written in `""`, python will print it as it is without changing anything in it, so it will not perform any addition and print it as it is.

So `print("10 + 10")` will print only `10 + 10` as output.

---
## Python Is a Case-Sensitive Language

The computer is a very dumb machine, it does not understand instructions, as normal people do so If I say what is 10 + 20 then you will say 30, then if I ask you to spell it, you will say `t h i r t y`, but programming language does not do like that.
- Programming language is hardware-driven it will do the things that are programmed only.


If we write `prent()` instead of `print()`, then normal people can understand it is a `print()` and a person wants to print something, but Python would not understand.
Also, we forgot to add parentheses in the print statement, then also we got an error.



---
## Arithmetic Calculations in print()

- We can do substractions in `print()`.
```python
print(10 - 1)
```

**Output:**
```plaintext 
9   
```

- We can also do multiplications in `print()`.
```python
print(10 * 2)
```

**Output:**
```plaintext 
20
```


---
### Question

`print(10 + 20)`

**Choices**

- [x] 30
- [ ] 30.00
- [ ] 33


---
### Question

What is the output of the following piece of code?
`Print(10 * 22)`

**Choices**

- [ ] 220
- [ ] 2200
- [x] Error
- [ ] 10 * 22


**Explanation**

Here we have `Print(10 * 22)` and Python is a case-sensitive language, so it will not understand print with `P` and it will throw a `NameError`.

---
### Question

What is the output of the following piece of code?
`print(8 * 6)`

**Choices**

- [ ] 54
- [x] 48
- [ ] 8 * 6
- [ ] 86


---
## Primitive data types in Python
Every data is in a certain form, for example, a name is a String.
 
Let us take an example of **Student details**,
- **Name: string**, we never name as 1, 2, etc, it will always be a string.
-  **Roll number: integer**
-  **marks: decimal(float)**, marks can be decimal value as sometimes there may be half marks
-  **is_absent: True/false**, the student is absent or present, so it is a boolean value.

**Data types:** is a type of data we have in Python programming language.

In Python, we have a function named `type`, if we pass any data to it, it will print the type of that data.


### Integer:

**For example:**
```python=
print(type(23))
```

**Output:**
```plaintext 
<class 'int'>
```

It is an integer value so it will print `int`, just ignore the class part.


**Example:**
```python=
print(type(-122))
```

**Output:**
```plaintext 
<class 'int'>
```

-122 is also an integer.

**So integer can be any numeric value from - infinity to + infinity without a decimal in it.**


### Float

**If we add a decimal into the integer then it will be a float**.

**For example:**

```python
print(type(12.5))
```

**Output:**
```plaintext 
<class 'float'>
```

**Example:**
```python
print(type(12.0))
```

**Output:**
```plaintext 
<class 'float'>
```

If we add `.0`, then also it is considered as a floating number.


### String


Any value inside double inverted `" "`, or single inverted `' '` commas will be considered as a string.


```python
print(type("abcd"))
```

**Output:**
```plaintext 
<class 'str'>
```

**Example:**
```python
print(type('abcd'))
```

**Output:**
```plaintext 
<class 'str'>
```

But you can't do it in a way that starts with a single inverted and ends with double inverted commas. It will give us a syntax error.

**Example:**
```python
print(type('abcd"))
```

**Output:**
```plaintext
ERROR!
File "<string>", line 1
    print(type('abcd"))
               ^
SyntaxError: unterminated string literal (detected at line 1)
```
Either use both single inverted commas or both double inverted commas.

### Multi-line strings

If we write any paragraph or multiple line strings, then it is also considered as a string

**Example:**
```python
print(type(
"""
Hey!!!
Welcome everyone
"""
))
```

**Output:**
```plaintext 
<class 'str'>
```

### Boolean
There are two boolean values, True and False, and True means 1 and False means 0.


**Example:**
```python
print(type(True))
print(type(False))
```

**Output:**
```plaintext 
<class 'bool'>
<class 'bool'>
```


## None
If we print the type of `None`, then it will be `NoneType`.

**Example:**
```python
print(type(None))
```

**Output:**
```plaintext 
<class 'NoneType'>
```



---
### Question

What will be the output of the following?
`print(type(true))`

**Choices**

- [ ] True
- [ ] False
- [ ] Bool
- [x] Error


---
### Question

What is the output of the following piece of code?
`print(type(5.0))`

**Choices**

- [ ] int
- [x] float
- [ ] str
- [ ] bool

---
### Question

What is the output of the following?
`Print(type(False))`

**Choices**

- [ ] bool
- [ ] int
- [ ] str
- [x] Error

**Explanation**

```python
Print(type(False))
```
Here `p` is capital P in print so it gives an error.


---
## Comments
A comment is a way to explain what a code does. In Python comments start with the symbol `#`.
- Anything written in comments would not get run.

**Example:**
```python
# print('hello world')

```

Nothing will be printed in the output, as we have commented print statement.

### Multi-line comments
If we want multi-line comments in Python, then we need to write the `#` symbol in every line.

**Example:**
```python
# this
# is
# a multi-line comment
```

You can also make multi-line comments by writing multi-line strings.

**Example:**
```python
"""
this
is
a multi-line comment
"""
```



---
## Variables
Variables are like containers, which allow to store values, or we can say variables are like storage.

**Example:**
```python
a = 10
```
Here `a` is a variable.

We can also change the value of `a`.

**Example:**
```python
a = 10
a = 20
```

But when we print the value of `a`, it will print the latest value of `a`.


**Example:**
```python
a = 10
a = 20

print(a)
```

**Output:**
```plaintext 
20
```

And if we check the type of variable `a`, then it will be an integer.

**Example:**
```python
a = 10
a = 20

print(a)

print(type(a))
```

**Output:**
```plaintext 
20
<class 'int'>
```

**In Python, variables take the type of their value**
So if we assign a float value to a variable, then its type becomes float.


**Example:**
```python
pi = 3.14

print(type(pi))
```

**Output:**
```plaintext 
<class 'float'>
```

### Rules for Naming Variables in Python
1. A variable name must start with a letter(a-z, A-Z) or the underscore(_) character.
2. A variable name cannot start with a number.
3. A variable name can only contain alpha-numeric characters and underscores(means can only have A-Z, a-z, 0-9, and _ ).
4. Variable names are case-sensitive (age, Age and AGE are three different variables).

`a1s = 1`, is the correct variable as it starts with a character, does not start with a number, it only has alphanumeric characters and underscores.

**Example for last rule:**
```python
a = 1
A = 2
print(a)
print(A)
```

**Ouput:**
```plaintext
1
2
```
Both a will be treated differently and print their values.




---
### Question

Which of the following is a valid variable name?


**Choices**

- [x] hELLO
- [ ] 1_name_Input
- [ ] `a * b * c`
- [ ] Cod3$#



---
## Cases for Variables

Cases are just a way to write variables.
Let us assume we want to create a variable for storing Shubham marks, then we can have 

**Camel Case:**
```python
shubhamMarks =  10
```

**Title Case:**
```python
ShubhamMarks =  10
```

But in the above two cases, the camel case is preferred more.

**Snake Case:**
```python
shubham_marks =  10
```

**Example:**
```python
thisisavariable = 1234
thisIsAVariable = 1234 # It is more readable in comparison to the above variable name
this_is_a_variable = 4567 # can have an underscore in a variable name
print(thisIsAVariable)
print(this_is_a_variable)
```

**Output:**
```plaintext
1234
4567
```


---
## Type Casting
Casting is converting a variable of one type to another type. For example, if we have some value in a string, but we want it in an integer or float, then we need type casting.


### Converting String To integers
If we have some integer value in string form, but we want to convert it to an integer for performing some arithmetic operations, then we have a `int()` function for it.

For converting string to integer, we just need to wrap in `int()`.

**Example:**
```python
# Converting String
# To integers
a = "1234"
b = int(a)
print(type(b))
```

**Output:**
```plaintext
<class 'int'>
```

But if we try to convert a string have some string value into an integer then it will give an error.


**Example:**
```python
a = "welcome"
b = int(a)
print(type(b))
```

**Output:**
```plaintext
ValueError Traceback (most recent call last)
Cell In[48], line 2
 1 a = "welcome"
----> 2 b = int(a)
 3 print(type(b))
ValueError: invalid literal for int() with base 10: 'welcome'
```


**Example:**
```python
a = "12a"
b = int(a)
print(type(b))
```

**Output:**
```plaintext
ValueError Traceback (most recent call last)
Cell In[48], line 2
 1 a = "12a"
----> 2 b = int(a)
 3 print(type(b))
ValueError: invalid literal for int() with base 10: '12a'
```

### Converting String To Float

For converting string to float, we just need to wrap in `float()`.

**Example:**
```python
# Converting String
# To float
a = "12"
b = float(a)
print(type(b))
```

**Output:**
```plaintext
<class 'float'>
```

**Example:**
```python
a = "12.5"
b = float(a)
print(b)
print(type(b))

```

**Output:**
```plaintext
12.5
<class 'float'>
```

But if we have two decimal points in the string, then it will give an error.


**Example:**
```python
a = "12.5.0"
b = float(a)
print(type(b))
print(b)

```

**Output:**
```plaintext
ValueError Traceback (most recent call last)
Cell In[53], line 2
 1 a = "12.5.0"
----> 2 b = float(a)
 3 print(type(b))
 4 print(b)
ValueError: could not convert string to float: '12.5.0'
```


### Converting String To Bool
Converting string to bool is a little tricky:
- Empty string is  False,
- Everything else is True.

`bool()` will convert string to bool.

**Example:**
```python
a = ""
b = bool(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'bool'>
False
```


If we even write space in a string, then also its bool value will be true.

**Example:**
```python
a = " "
b = bool(a)
print(type(b))
print(b)

```

**Output:**
```plaintext
<class 'bool'>
True
```



### Converting Integer To String 
`str()` is used for converting Integer To String.

**Example:**
```python
a = 1234
b = str(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'str'>
1234
```


If the integer value is 0, then also it will be converted to a string.

**Example:**
```python
a = 0
b = str(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'str'>
0
```

### Converting Integer To Float 

`float()` is used for converting an integer to float, and it will simply add `.0` to the integer value for converting it into float.

**Example:**
```python
a = 1234
b = float(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'float'>
1234.0
```



### Converting Integer To Bool 

`bool()` is used for converting an integer to bool, 
- 0 is False,
- Everything else is True.

**Example:**
```python
a = 1234
b = bool(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'bool'>
True
```

Negative value is also True, as 0 is only False.

**Example:**
```python
a = -1
b = bool(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'bool'>
True
```




### Converting Float To String 
`str()` is used for converting Float To String.

**Example:**
```python
a = 3.14
b = str(a)
print(type(b))
print(b)

```

**Output:**
```plaintext
<class 'str'>
3.14
```

### Converting Float To Integer

`int()` is used for converting integers to float, and it will remove everything after decimal.

**Example:**
```python
a = 3.14
b = int(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'int'>
3
```



### Converting Float To Bool 

`bool()` is used for converting float to bool, 
- Everything that is 0.0 is False,
- Everything else is True.

**Example:**
```python
a = 0.00000001
b = bool(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'bool'>
True
```

Because `0.00000001` is also something value above `0.0`. 


### Converting Bool To Integer

- True will be converted to 1.
- False will be converted to 0.

**Example:**
```python
a = True
b = int(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'int'>
1
```

**Example:**
```python
a = False
b = int(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'int'>
0
```



### Converting Bool To String 

- True will be converted to True in string.
- False will be converted to False in the string.

**Example:**
```python
a = False
b = str(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'str'>
False
```


**Example:**
```python
a = True
b = str(a)
print(type(b))
print(b)
```

**Output:**
```plaintext
<class 'str'>
True
```


---
### Question

What is the output of the following?
`print(bool("0"))`

**Choices**

- [x] True
- [ ] False
- [ ] Error

**Explanation**

`print(bool("0"))`

"0" is a string and only the empty string is false, everything else is true, here we have a string having some value so it will be True.



---
### Question

What is the output of the following?
`print(bool("apple"))`

**Choices**

- [x] True
- [ ] False


---
### Question

What is the output of the following?
`# print("101")`

**Choices**

- [ ] 101
- [ ] "101"
- [x] Nothing
- [ ] Error

**Explanation**

`# print("101")`

Here this print statement is commented, so nothing will be printed in the output.



---
### Question

What is the output of the following?
`print(int(15.99))`

**Choices**

- [x] 15
- [ ] 16
- [ ] 15.99
- [ ] Error


---
## Input Statement
Not every value is always available in the program, many times we need to take the values input from the user.

`input()` is used in Python for taking user from input.

We can also pass the message in `input()` which will be printed for taking input from the user.

**Example:**

```python
a = input()
print(a)
```

**Output:**
```plaintext
67
67
```

We can also pass the message "Enter an integer value "


**Example:**

```python
a = input("Enter an integer value ")
print(a)
```

**Output:**
```plaintext
Enter an integer value 67
67
```

But it should not always be guaranteed that the user will enter an integer value, the user can also enter `ten` as input.

So it's our responsibility to typecast the user input value according to our requirements.


`input()` will always return a string value.


**Example:**

```python
a = input("Enter an integer value ")
print(a)
print(type(a))
```

**Output:**
```plaintext
Enter an integer value 67
67
<class 'str'>
```

If we enter any floating value, then it also be taken as a string.

**Example:**

```python
a = input("Enter an integer value ")
print(a)
print(type(a))
```

**Output:**
```plaintext
Enter an integer value 67.7
67.7
<class 'str'>
```

If we want to change the type of input value, then we have to do type casting.

**Example:**

```python
a = input("Enter an integer value ")
b = int(a)
print(b)
print(type(b))
```

**Output:**
```plaintext
Enter an integer value 12
12
<class 'int'>
```

Now if the user gives string value as input then it will throw an error during type casting.


**Example:**

```python
a = input("Enter an integer value ")
b = int(a)
print(b)
print(type(b))
```

**Output:**
```plaintext
Enter an integer value john
ValueError Traceback (most recent call last)
Cell In[82], line 2
 1 a = input("Enter an integer value ")
----> 2 b = int(a)
 3 print(b)
 4 print(type(b))
ValueError: invalid literal for int() with base 10: 'john'

```


---
## Problem Statement
Take two numbers as input and print the sum of those numbers.

### Solution

1. First we need to take two input user
```python
a = input()
b = input()
```

2. The next step is to do the sum of it.
```python
a = input()
b = input()
print(a + b)
```

**Output:**
```plaintext
10
20
1020
```

As `input()` will take everything as a string, so if we try to add input value, then the string concatenation will be performed by it.
3. So we need to convert the input value into int first, and then we will add those values.
```python
a = int(input())
b = int(input())
print(a+b)
```

**Output:**
```plaintext
10
20
30
```


---
### Question

What is the output of the following?
```python
b = input() # input value = 234
print(type(b))
```

**Choices**

- [ ] int
- [x] string
- [ ] not sure



---
### Extra - Print Statement

**Example:**
```python
a = 10
b = 20
print(a, b)
```

**Output:**
```plaintext
10 20
```

**Example:**
```python
a = 10
b = 20
c = 30
print(a, b)
print(c)
```

**Output:**
```plaintext
10 20
30
```

### Sep and End
We can pass the `sep` and `end` values in the print statement.

- **sep** is what should come between the values of the print statement.
- **end:** is what should come after the print statement content.

default value of sep is `' '`(space) and end is `\n`(new line character).

**Example:**
```python
print(13, 134, 134, 1324,134, sep = ' ', end = '\n') #default values
```

**Output:**
```plaintext
13 134 134 1324 134
```

If we pass `-` as a separator value, then a dash will be added between the values.


**Example:**
```python
print('John', 'Doe', sep = '-')
```

**Output:**
```plaintext
John-Doe
```

**Example:**
```python
a = 10
b = 20
print(a, b, sep = '@')
```

**Output:**
```plaintext
10@20
```

`\n` will work as a new line character, if we pass it as a separator then every value will be printed in a new line.


**Example:**
```python
a = 10
b = 20
print(a, b, sep = '\n')
```

**Output:**
```plaintext
10
20
```

If we pass `' '`(space) as a value of `end`, then after print statement values it will not go to a new line, it will simply add space after that.



**Example:**
```python
a = 10
b = 20
c = 30
print(a, b, end = ' ')
print(c)
print(40)
```

**Output:**
```plaintext
10 20 30
40
```

In the above code, we have not mentioned any `sep` value, so it will be space automatically.


**Example:**
```python
print(1, 2, 3, 4, sep = '-', end = '+')
print(5)
```

**Output:**
```plaintext
1 - 2 - 3 - 4 + 5
```


---
### Question

What will the output of the following?
```python
a = 5
b = 6
print(a, b)
```

**Choices**

- [ ] 56
- [ ] 5 
      6
- [x] 5 6
- [ ] Error




---
### Question

What is the output of the following?
```python
a = 5
b = 6
print(a)
print(b)
```

**Choices**
- [ ] 56
- [x] 5
      6
- [ ] 5 6
- [ ] Error



---
### Question

What is the output of the following?
```python
print("I", "Love", "Scaler", sep = "-")
```

**Choices**

- [ ] I Love Scaler
- [x] I-Love-Scaler
- [ ] I-love-scaler
- [ ] Error