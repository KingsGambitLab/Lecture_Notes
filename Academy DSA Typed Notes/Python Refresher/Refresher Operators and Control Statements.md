# Refresher: Operators and Control Statements

### Question

What is the output of the following?
`print(type("1"))`

**Choices**

- [ ] int
- [ ] float
- [x] str
- [ ] bool



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

**Rules for converting string to bool are:**
- Empty string will be converted to False.
- Everything else will be converted to True.

Here we have a string "0", so it has some value, it is not empty, so it will be True.




---
### Question

```python
print("Rahul", "Rohit", "Emma Watson", sep = " ")
print("Yash KGF")
```

**Choices**

- [x] Rahul Rohit Emma Watson
      Yash KGF
- [ ] Rahul Rohit Emma Watson Yash KGF
- [ ] Not Sure

**Explanation**

```python
print("Rahul", "Rohit", "Emma Watson", sep = " ")
print("Yash KGF")
```

We have specified `sep` as `" "`, and by default `end` will be a new line, so Yash KGF will be printed in a new line.




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


### Operators 

Before operators, we just understand what is expression, 
**Expression:** is just a simple equation we write.

**Example of expression:**
`a = b + c`

Here, 
- `a`, `b` and `c` are variables, or we can also call these operands.
- `=` and `+` are operators.

So, if we want to do certain operations then we need operators.

Operators are classified into different types based on their functionalities:
1. Arithmetic Operators.
2. Comparison Operators.
3. Assignment Operators.
4. Logical Operators.



### Arithmetic Operators 
Arithmetic Operators are used for arithmetic calculations.
Different arithmetic operators are explained below:

### Addition
`+` is used for addition, it can not work at one value, it always takes two values.



**Example:**
```python
a = 1
b = 4
print(a + b)
```

**Output:**
```plaintext
5
```

**Type change in addition:**
- **int + int -> int** We can add an integer and integer value to get an int value.
- **float + float -> float**, we can add float and float value to get float value.
* **int + float -> float**, we can add integer and float value to get float value
* **int/float + bool -> int/float,** we can add int/float and bool value and it will give int/float value as a result.

**Example:**
```python
print(2.5 + True)
```

**Output:**
```plaintext
3.5
```

Here True will be converted to float value i.e. 1.0, and then it will be added to 2.5 which will give 3.5 as a result.


**Example:**
```python
print(2.5 + False)
```

**Output:**
```plaintext
2.5
```

Here False will be converted to float value i.e. 0.0, and it will be added to 2.5 which will give 2.5 as a result.



* **string + string -> string** (concatenation)


**Example:**
```python
print('1' + '1')
```

**Output:**
```plaintext
11
```

**Not allowed in Python:**
* **int/float/bool + string**, Python does not allow to add int/float/bool to string, it will give an error.

**Example:**
```python
print('1' + 1)
```

**Output:**
```plaintext
TypeError Traceback (most recent call last)
Cell In[20], line 1
----> 1 print('1' + 1)
TypeError: can only concatenate str (not "int") to str
```


* **int/float/bool/string + None,** we can not do any arithmetic operations wth none.


**Example:**
```python
print(1 + None)
```

**Output:**
```plaintext
TypeError Traceback (most recent call last)
Cell In[24], line 1
----> 1 print(1 + None)
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```


### Subtraction
`-` is used for Subtraction.

It can be directly used with constants.
**Example:**
```python
print(2 - 3)
```

**Output:**
```plaintext
-1
```

We can also perform subtraction on variables.

**Example:**
```python
a = 1
a_b = 2
print(a - a_b)
```

**Output:**
```plaintext
-1
```

**Type change in subtraction**
* **int - int -> int**
* **float - float -> float**
* **int - float -> float**
* **int/float - bool -> int/float**

**Example:**
```python
print(2.5 - True)
```

**Output:**
```plaintext
1.5
```

True will be converted into `1.0`, and then it will subtracted.

**Example:**
```python
print(2.5 - False)
```

**Output:**
```plaintext
2.5
```

False will be converted into `0.0`, then it will subtracted.

**Not allowed**
* **string - string,** in string subtraction is not allowed, we can add strings.
* **int/float/bool - string**
* **int/float/bool/string - None**



### Multiplication
`*` is used for Multiplication.

**Example:**
```python
print(2 * 3)
```

**Output:**
```plaintext
6
```


**Type change in multiplication**
* **int * int -> int**
* **float * float -> float**
* **int * float -> float**
* **int/float * bool -> int/float,** if multiplied by False, then we will always get 0 or 0.0, or if multiplied with True, then it will be the same number.
* **int * string -> string (duplication),** we can multiply an integer with a string, it will duplicate the string to the number of times of integer value.



**Example:**
```python
print('I am Sorry \n' * 10)
```

**Output:**
```plaintext
I am Sorry
I am Sorry
I am Sorry
I am Sorry
I am Sorry
I am Sorry
I am Sorry
I am Sorry
I am Sorry
I am Sorry 
```



**Not allowed**
* **string * string**
* **float * string**
* **int/float/bool/string * None**



### Division
`/` is used for Division.



**Example:**
```python
print(3 / 2)
```

**Output:**
```plaintext
1.5
```


**Type change in division**


* **int / int -> float**
**Example:**
```python
print(2 / 2)
```

**Output:**
```plaintext=
1.0
```
* **float / float -> float**
* **int / float -> float**


**Not allowed**

* **string/string**
* **float/string**
* **int/float/bool/string / None**

**Example:**
```python
print(-3 / 2)
```

**Output:**
```plaintext
-1.5
```



### Modulus (mod) - Remainder
`%` is a Modulus (mod) operator symbol, it calculates the remainder.




**Example:**
```python
print(5 % 2)
```

**Output:**
```plaintext
1
```


**Example:**
```python
print(8 % 3)
```

**Output:**
```plaintext
2
```

**Type change in modulus**
- int % int -> int


### Floor Division
`//` is the floor division operator, it first divides the number, and it gives the previous smaller integer value of the quotient as a result.



**Example:**
```python
print(8 // 3)
```

**Output:**
```plaintext
2
```


**floor:**
`floor(-2.5) = -3`
as a previous smaller integer of -2.5 is -3,

![image](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/066/343/original/upload_163e464f1cd2704c9797ee2e0af04249.png?1708929562)

`floor(3.25) = 3`
as a previous smaller integer of 3.25 is 3.

![image](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/066/346/original/upload_833df7cf571f014a904936d4581ec744.png?1708929625)


**Example:**
```python
import math
print(math.floor(-2.5))
print(int(-2.5))
print(math.floor(3.00001))
```

**Output:**
```plaintext
-3
-2
3
```


**Type change in floor division**
- **int/float // int/float -> integral part**, floor division gives integer for float values division also, it always give integral floor value of float quotient.


Integer typecasting simply removes the number available after the decimal point, but floor division gives the previous smaller integer value of the quotient.

### Power
`**` works as a power operator in Python.



**Example:**
```python
print(2 ** 3)
```

**Output:**
```plaintext
8
```

It can have float values also.


**Example:**
```python
print(2 ** 0.5)
```

**Output:**
```plaintext
1.4142135623730951
```

The above code gives us a square root of 2.

**Type change in floor division**
- **int/float ** int/float -> int/float**



**Example:**
```python
print(3.5 ** 2)
```

**Output:**
```plaintext
12.25
```





---
### Question

What is the output of the following?
```python
print(10 % 3)
```

**Choices**

- [ ] 0
- [x] 1
- [ ] 2
- [ ] 3




---
### Question

What is the output of the following?
```python
print(2 ** 3)
```

**Choices**

- [ ] 5
- [ ] 6
- [ ] 7
- [x] 8



---
### Question

What is `floor(2.0)`?
**Choices**

- [x] 2
- [ ] 1
- [ ] 3





---
### Question
`print(-8 // 3)`

**Choices**

- [ ] -2.666
- [ ] -2
- [x] -3


**Explanation**

```python
print(-8 // 3)
```


As -8/3 = -2.6666666666666665, if we calculate its floor then it will be -3, as the previous integer value of -2.6666666666666665 is **-3**.


---
## Comparison Operator

### Comparison Operator
Comparison Operator is used for comparison, when we want to compare the value of two things, we can compare in the following ways.
* Equal
* Not Equal
* Less than / Greater than
* Less than and equal / Greater than and equal

**Comparison Operator always returns bool,** it always tells us True or False.


### Equal
`==` is equal operator in Python.


**Example:**
```python
print(2 == 2)
```

**Output:**
```plaintext
True
```


**Example:**
```python
print(2 == 3)
```

**Output:**
```plaintext
False
```

**We can compare:**
- **int and int**
- **int and float**


**Example:**
```python
print(2 == 2.0)
```

**Output:**
```plaintext
True
```


**Example:**
```python
print(2 == 2.00001)
```

**Output:**
```plaintext
False
```

- **int and string**

**Example:**
```python
print(2 == '2')
```

**Output:**
```plaintext
False
```

- **int and None**, if we compare a value with none, we always get a False result.


**Example:**
```python
print(2 == None)
```

**Output:**
```plaintext
False
```

But we can compare any type value with any other value type.


### Not Equal
`!=` is a not equal operator in Python.


**Example:**
```python
print(2 != '2')
```

**Output:**
```plaintext
True
```

**Example:**
```python
print('2' != '22')
```

**Output:**
```plaintext
True
```

**Example:**
```python
print('Aakar' != 'Aakar')
```

**Output:**
```plaintext
False
```


**Example:**
```python
print('ABC' != 'abc')
```

**Output:**
```plaintext
True
```

**Explaination:**
As python is a case sensitive language so `ABC` and `abc` are considered different.

### Less Than / Greater Than

**Example:**
```python
print(2 < 3)
```

**Output:**
```plaintext
True
```

We can not compare integer and string values.

**Example:**
```python
print(2 < '2')
```

**Output:**
```plaintext
TypeError Traceback (most recent call last)
Cell In[65], line 1
----> 1 print(2<'2')
TypeError: '<' not supported between instances of 'int' and 'str'
```

We can have a comparison between integer and float values.

**Example:**
```python
print(2 < 2.0001)
```

**Output:**
```plaintext
True
```
We can not compare integer and None values.


**Example:**
```python
print(2 < None)
```

**Output:**
```plaintext
TypeError Traceback (most recent call last)
Cell In[67], line 1
----> 1 print(2< None)
TypeError: '<' not supported between instances of 'int' and 'NoneType'

```


We can have a comparison between string and string values.

**Example:**
```python
print('a' < 'b')
```

**Output:**
```plaintext
True
```





**Example:**
```python
print('Vicky' < 'Kusum')  # Will be covered in String class
```

**Output:**
```plaintext
False
```

We can also do a comparison with negative values.


**Example:**
```python
print(2 > -3.43)
```

**Output:**
```plaintext
True
```


**Example:**
```python
print(100 >= 32)
```

**Output:**
```plaintext
True
```


**Example:**
```python
print(31 <= -43)
```

**Output:**
```plaintext
False
```


---
## Assignment Operator

`=` is an assignment operator, it will assigne value to the variable.

**Example:**
```python
a = 2 + 5
print(a)
```
**Output:**
```plaintext
7
```


### Shorthand
In place of `a = a (op) b`, we can write `a (op)= b`.



**Example:**
```python
a = 1
a = a + 5
print(a)



a = 1
a += 5
print(a)
```
**Output:**
```plaintext
6
6
```



**Example:**
```python
a = 11
a = a % 5
print(a)

a = 11
a %= 5
print(a)
```
**Output:**
```plaintext
1
1
```


---
## Logical Operator
We have the following logical operators:
* And (Both the values should be True then True otherwise False)
* Or (Any of the values should be true then True otherwise False)
* Not (Reverse)

**Logical operator always takes bool as input**

### AND
The truth table of AND:

*  True and True -> True
* True and False -> False
*  False and True -> False
*  False and False -> False

AND will only give True output, if we have both values True, otherwise in all other cases(if any one value is False) it will give us False.



**Example:**
```python
(2 < 3) and (2 < 4)
```
**Output:**
```plaintext
True
```
Both conditions result is True, so AND will also give True.


**Example:**
```python
('Aakar' == 'Aakar') and (-2 < -3)
```
**Output:**
```plaintext
False
```

`(-2<-3)` gives False, so AND will also give False.

### OR
The truth table of OR:

*  True or True -> True
*  True or False -> True
*  False or True -> True
*  False or False -> False

OR will give a True output, if any one of the input values is True, and it will give False only if both input values are False.



**Example:**
```python
(2 < 3) or (2 < 4)
```
**Output:**
```plaintext
True
```



**Example:**
```python
('Aakar' == 'aakar') or (-2 < -3)
```
**Output:**
```plaintext
False
```

Both conditions give us False, so the output will also be False.


**Example:**
```python
('Aakar' == 'aakar')
```
**Output:**
```plaintext
False
```



**Example:**
```python
(-2 < -3)
```
**Output:**
```plaintext
False
```



### Not
`not` is Not operator.
Truth Table
*  not True -> False
*  not False -> True



**Example:**
```python
not ('Aakar' == 'aakar')
```

**Output:**
```plaintext
True
```

`('Aakar' == 'aakar')` will give us False, and not False gives us True.




---
### Question
What is the output of the following?
`print(10 <= 8)`

**Choices**

- [ ] True
- [x] False




---
### Question
What is the output of the following?
`print(False == 1)`

**Choices**

- [ ] True
- [x] False
- [ ] Error




---
### Question
What is the output of the following?
`print('1' < 2)`

**Choices**

- [ ] True
- [ ] False
- [x] Error



---
### Question
What is the output of the following?
```python
a = 3
a *= 4
print(a)
```

**Choices**

- [ ] 3
- [ ] 4
- [ ] 7
- [x] 12



---
### Question
What is the output of the following?
```python
print(True and (not False))
```

**Choices**

- [x] True
- [ ] False
- [ ] Error



---
## Conditional Statements
A conditional statement is a Boolean expression that, if True, executes a piece of code.
A conditional statement has some conditions, if it will be true then we have some piece of code to execute, and if it is false, then we have another piece of code to execute.


![image](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/066/349/original/upload_c9d3eb69c79d04312bc8c53c803c2741.png?1708929771)


There are the following Conditional patterns in Python:
* if
* if else
* if elif
* if elif else


**Python is an indentation-based language,** in place of curly braces for blocks we use the same indentation for a single block code.

### if

```python
if(<condition>):
    this
    is
    a
    block
```

`()` is not necessary in Python for specifying the conditions.

Any number of spaces can give us an indentation, but a single block has the same indentation for all lines.

**Example:**
```python
if(2 < 3):
    print('two is less')
```

**Output:**
```plaintext
two is less
```

If we add extra indentation in the same block, then it will give an error.


**Example:**
```python
if(2 < 3):
    print('two is less')
        print('yayy') # will not work because of extra indentation
```

**Output:**
```plaintext
Cell In[107], line 3
 print('yayy') # will not work because of extra indentation
 ^
IndentationError: unexpected indent
```


if block will only be executed if condition, otherwise normal flow will be continued.



**Example:**
```python
if(2 > 3):
    print('two is less')
print('yayy')
```

**Output:**
```plaintext
yayy
```


### If Else
if the condition is True, then the `if` block code will be executed, otherwise `else` block code will be executed.


**Example:**
```python
if(2 > 3):
    print('two is greater than 3')
else:
    print('two is not greater than 3')
print('yayy')
```

**Output:**
```plaintext
two is not greater than 3
yayy
```

### elif

`elif` is used for checking multiple conditions.

**Example:**
```python
weather = input('What the weather like? ')
if(weather == 'Sunny'):
    print('Take Googles')
elif (weather == 'Rainy'):
    print('Take Umbrella')
elif (weather == 'Snowy'):
    print('wear boots')
else:
    print('I dont know this weather')
print('normal execution')
```

`else` is optional here, it is executed if any of the conditions is not true.


**Output 1:**
```plaintext
What the weather like? Sunny
Take Googles
normal execution
```

**Output 2:**
```plaintext
What the weather like? Mist
I dont know this weather
normal execution
```




---
## Problem Statement: Traffic Lights

You have to ask about the color of the traffic light from the user, if:
- it is green, then print go,
- it is yellow, then print wait,
- it is red, then print stop


* green -> go
* yellow -> wait
* red -> stop

:::warning
Please take some time to think about the solution on your own before reading further.....
:::


### Solution

**Code:**
```python
light = input()
if (light == 'green'):
    print('go')
elif (light == 'yellow'):
    print('wait')
elif (light == 'red'):
    print('stop')
else:
    print('Wrong input')
```

**Output 1:**
```plaintext
green
go
```

**Output 2:**
```plaintext
yellow
wait
```

**Output 3:**
```plaintext
red
stop
```


**Output 4:**
```plaintext
asgsg
Wrong input
```


---
## Problem Statement: Maximum of two
 Given two integers, print the maximum of them.
 
### Solution

**Code:**
```python
a = int(input())
b = int(input())
if(a > b):
    print('Maximum of two is', a)
else:
    print('Maximum of two is', b)
```


**Output 1:**
```plaintext
100
-100
Maximum of two is 100
```


**Output 2:**
```plaintext
12
22
Maximum of two is 22
```


---
## Problem Statement: Maximum of two and check equality also
Given two integers, print the maximum of them or say both are equal.

### Solution

:::warning
Please take some time to think about the solution on your own before reading further.....
:::


**Code:**
```python
a = int(input())
b = int(input())
if(a == b):
    print('Both numbers are equal')
elif(a > b):
    print('Maximum of two is', a)
else:
    print('Maximum of two is', b)
```


**Output 1:**
```plaintext
100
100
Both numbers are equal
```


**Output 2:**
```plaintext
12
22
Maximum of two is 22
```


---
## Problem Statement: Check even or odd
Take an integer and print if it is even or odd

### Solution

**Code:**
```python
a = int(input())
if(a % 2 == 0):
    print('Number is even')
else:
    print('Number is odd')
```

**Output:**
```plaintext
-3
Number is odd
```


---
## Problem Statement: Print the grade

Take marks as input, then print the grade accordingly as given below:
* A --> (90, 100]
* B --> (80, 90]
* C --> (70, 80]
* D --> [0, 70]

**Take it as homework**

---
## Problem Statement: FizBuz
Given an integer as input:
* if it is only a multiple of 3 print only Fizz
* if it is only a multiple of 5 print only Buzz
* if it is a multiple of both 3 and 5 print Fizz-Buzz

### Solution
n be a multiple of a if **n%a == 0**

**Code:**
```python
a = int(input())
if (a % 3 == 0 and a % 5 == 0):
    print('Fizz-Buzz')
elif (a % 3 == 0):
    print('Fizz')
elif (a % 5 == 0):
    print('Buzz')
```

**Output 1:**
```plaintext 
15
Fizz-Buzz
```

**Output 2:**
```plaintext 
27
Fizz
```

**Output 3:**
```plaintext 
25
Buzz
```

**Output 4:**
```plaintext 
8
```



---
### Question
What is the output of the following?
```python
a = 5
if(a < 6):
    print('Option 1')
if(a < 3):
    print('Option 2')
else:
    print('Option 3')
```

**Choices**

- [ ] Option 1 
- [ ] Option 2
- [ ] Option 3
- [x] Option 1
      Option 3



```python
a = 5
if(a < 6):
    print('Option 1')
if(a < 3):
    print('Option 2')
else:
    print('Option 3')
```

If we see in the code,
```python
a = 5
if(a < 6):
    print('Option 1')
```

```python
if(a < 3):
    print('Option 2')
else:
    print('Option 3')
```

Both these codes have separate conditions, so in the first condition, it will check for `if(a < 6)`, then again it will check for `if(a < 3)`, and in this case condition will be false, so `else` will be executed.



---
## Nested if
We can have another `if` inside the `if`.

**Example:**
```python
a = input('Is your character Male?')
if(a == 'yes'):
    b = input('Is your character good?')
    if(b == 'yes'):
        print('Your chacter name is chota Bheem')
    else:
        print('Your character name is Kaliya')
else:
    print('Your character name is chutki')

```

**Output 1:**
```plaintext 
Is your character Male?yes
Is your character good?no
Your character name is Kaliya
```

**Output 2:**
```plaintext 
Is your character Male?no
Your character name is chutki
```

**Homework:** Make a small game over some concept


---
## Operators Hierarchy(Precedence)

Operators Precedence In Python.

![image](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/066/352/original/upload_8a401d3788635239b652d7ddfbf04922.png?1708930106)


- High precedence operators are calculated first.
- For operators with the same precedence will be evaluated from left to right.

**Example 1:**
`3 * 10 / 2`

**Solution**
`*` and `/` have the same precedence so we will evaluate it from left to right.

`= ((3 * 10) / 2)`
`= 30 / 2`
`= 15`

**Answer:** 15


**Example 2:**
`10 - 5 / 5`

**Solution**
`/` have higher precedence than `-` so first `/`  will be evaluated, then `-`  will be evaluated

`= 10 - 1`
`= 9`

**Answer:** 9


**Example 3:**
`45 % 10 / 2`

**Solution**
`%` and `/` have the same precedence so we will evaluate it from left to right.

`= ((45 % 10) / 2)`
`= 5 / 2`
`= 2.5`

**Answer:** 2.5


**Example 4:**
`True and not False`

**Solution**
`not` has higher precedence than `and`, so first `not`  will be evaluated, then `and`  will be evaluated

`= True and (not False)`
`= True and True`
`= True`

**Answer:** True


**Example 5:**
`False or not False and True`

**Solution**
`not` has higher precedence than `or` and `and`, so first `not`  will be evaluated, then between`and` and `or`, `and` have higher precedence, so `and` will be evaluated then `or` will be evaluated.

`= False or (not False) and True`
`= False or (True and True)`
`= False or True`
`= True`

**Answer:** True