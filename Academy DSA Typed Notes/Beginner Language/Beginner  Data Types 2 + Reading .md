# Beginner : Data Types 2 + Reading Inputs

---

Recap: Start the class with Revising the previous session rules:

:::success
There are a lot of quizzes in this session, please take some time to think about the solution on your own before reading further.....
:::

## Revision: Type Casting Rules

1. Int data can be stored in long and there wont be any loss of data, so there wont be any issues. 
Ex: 
int a = 10;
long b = a;
System.out.print(b); --> 10
			
2. Long data cannot be stored in int, there can be a loss of data so we will get an error
Ex: 
long a = 100;
int b = a;
System.out.print(b); Error 
			
3. If we want to still force we need to keep explicitly type cast it 
Ex : 
long a = 100;
int b = (int)a;
System.out.print(b) --> 100

---

# Question


```
int a = 10000;
long b = a;
System.out.print(b);
```

# Choices

- [x] 10000

- [ ] Compilation Error

- [ ] 100000.0

- [ ] 10000L

---

**Explanation:**
First line we create a variable of type int then we are creating a long type variable "b" and trying to store the value of "a" in it. This is Implicit Typecasting. 
Ans= 10000


---

# Question


```
long x = 10000;
System.out.print(x);
```

# Choices

- [ ] 10000L

- [ ] Compilation Error

- [x] 10000

- [ ] None of the above

---

**Explanation:**
First line automatic typecasting is happening between Int and Long. 
Ans= 10000

---

# Question


```
long x = 10000;
int y = x;
System.out.print(y);
```
# Choices

- [ ] 10000L

- [x] Compilation Error

- [ ] 10000

- [ ] None of the above


---

**Explanation:**
First line we create a variable of type long then we are creating a int type variable "y" and trying to store the value of "x" in it. In this acse there is a possiblilty of Data Loss. 
Error- Possible lossy conversion from long to int. 

---

# Question


```
long x = 1000;
int y = (int)x;
System.out.print(y);
```

# Choices

- [x] 1000

- [ ] Compilation Error

- [ ] 1000L

- [ ] None of the above

---

**Explanation:**
`int y = (int)x;` Now with this line we are forcing the compiler to typecast it to int. 
It is explicit Typecasting.
Ans= 1000. 

---

# Question


```
long a = 10000000000L;
int b = (int)a;
System.out.print(b);
```

# Choices

- [ ] 10000000000

- [x] Random Value

- [ ] 10

- [ ] None of the above

---

**Explanation:**
`int b = (int)a;` Here we are forcing the compiler to store the value 10^10 into int. Because of that overflow will happen. 
Ans= Some random value. 


---

## Taking input from the user:

Tool to take input from the user: Scanner. 

**Syntax of Scanner:**
```
Scanner scn = new Scanner(System. in);
```

> We dont need to know what is this scanner. Just exactly follow the syntax to take input from the user. 

Now in order to use scanner also we need to write one line: 

``` 
import java.util.*;
```

> Consider this like in order to play pubg we need to import some files, some packages similarly to use scanner we need to import java files. 


### Take Input and print the output:
```
int x = scn.nextInt();
System.out.print(x);
```
**Explanation:**
Here we are taking the help of scanner by using its name scn and asking the user for an integer value which we will store in "x" varaible.

> Just try to give different integer values in the custom input and explain how it got printed. 

**Take input and print twice the number:**

```
int y = scn.nextInt();
System.out.print(2 * y);
```

---

# Question

Predict the output for given input:
Input: 100

```
scanner sc = new scanner(System.in);
int xyz = sc.nextInt();
System.out.print(xyz);
```

# Choices
- [ ] xyz
- [x] Error
- [ ] 100
- [ ] Goodnight :)

---

**Explanation:**
At line 1, scanner is in small letter. Because Java is case sensitive. 


---

# Question

Predict the output for given input:
Input: 594

```
Scanner sc = new Scanner(system.in);
int abc = sc.nextInt();
System.out.print(abc);
```

# Choices
- [ ] 594
- [x] Error
- [ ] abc
- [ ] Only here to watch!

---

**Explanation:**
Error: S in System should be capital. 

---

# Question

Predict the output for given input:
Input: 5000

```
Scanner scn = new Scanner(System.in);
int a = scn.nextInt();
System.out.print(a);
```

# Choices
- [ ] Error
- [x] 5000
- [ ] Watching Netflix on the side!

---


**Explanation:**
Here we are creating a variable "a" and taking integer from the user. 
 

---

# Question

Predict the output for given input:
Input: 24 30
```
Scanner sc = new Scanner(System.in);
int a = sc.nextInt();
int b = sc.nextInt();
System.out.print(a);
```
# Choices
- [x] 24
- [ ] 30
- [ ] Error

---


**Explanation:**

The first value will be stored in first variable and second value will be stored in second variable.


---

# Question

Predict the output for given input:
Input: 33 11

```
Scanner sc = new Scanner(System.in);
int c = sc.nextInt();
int d = sc.nextInt();
System.out.print(c + d);
```
# Choices
- [ ] 3311
- [ ] c + d
- [x] 44
- [ ] Error

---


**Explanation:**

"c" variable will have value 33, and "d" variablle will have value 11. 


---

# Question

What will be the output for the following input?
```
Input: 15 21
Scanner sc = new Scanner(System.in); 
int a = sc.nextInt(); 
int b = sc.nextInt(); 
int c = sc.nextInt();
System.out.print(a + b + c);
```
# Choices
- [ ] 36
- [ ] a + b + c
- [ ] 36c
- [x] Error

---


**Explanation:**
"a" variable will have value 15, then variable "b" will have value 21, but for "c" variable user is not giving any input. 
Ans = Error, No such element exception. 

---


### Input for long data type:
```
Scanner scn = new Scanner(System .in);
long c = scn.nextLong();
```

---

# Question
How to take input for a long variable?

# Choices
- [ ] sc.nextlong()
- [ ] sc.nextint()
- [x] sc.nextLong()
- [ ] sc.nextInt()

---

# Question

Predict the output for the following input:
Input: 10000000000
```
Scanner scn = new Scanner(System.in);
long N = scn.nextLong();
System.out.println(N);
```
# Choices
- [x] 10000000000
- [ ] Error
- [ ] 10000000000L

---

# Question

Predict the output for the following input:
Input: 10000000000L

```
Scanner scn = new Scanner(System.in):
long N = scn.nextLong();
System.out.println(N);
```
# Choices
- [ ] 10000000000
- [x] Error
- [ ] 10000000000L

---

**Explanation:**

Here, when we give L in the input, then the whole input is not a number anymore. 
Ans = Error, Input Mismatch. 

> Do not write L in the input section to give a long value. 

---

# Question
```
Input: 2500
long x = scn.nextInt();
System.out.print(x);
```
# Choices
- [x] 2500
- [ ] Error
- [ ] 2500L

---

**Explanation:**

First 2500 is considered an integer value, ans we can store an integer value into long. It is implicit typecasting. 


---

# Question
```
Input: 2500
int x = scn.nextLong();
System.out.print(x);
```
# Choices
- [ ] 2500
- [x] Error
- [ ] 2500L

---

**Explanation:**
Now here from long to int, it cannot happen automatically. 
Ans = Error, possible lossy conversion from long to int. 

**Correct**
```
Input: 2500
int x = (int)scn.nextLong();
System.out.print(x);
```

Ans = 2500. 

---

## Float vs Double
			        
1. Non Decimal{Integers} --> Datatypes : int  long
2. Decimal --> float  double
Ex : 1.24 , 1.56 , 20.0,and soon...
			
			
**Declare a variable of any Type 
Syntax: type name = value;**

---

# Question

```
double d = 6.17;
System.out.print(d);
```

# Choices

- [ ] Compilation Error
- [ ] 6
- [x] 6.17
- [ ] None of the above

---

**Explanation:**
We are creating a variable of type double. 
Ans= 6.17

---

# Question

```
float x = 3.14;
System.out.print(x);
```

# Choices

- [x] Compilation Error
- [ ] 3.14f
- [ ] 3.1400001
- [ ] 3.14

---

**Explanation:**
Error-> Possible lossy conversion from double to float. 

> Rule : In JAVA, Any decimal number is considered as double


---

# Question


```
float a = 3.14f;
System.out.print(a);
```

# Choices

- [ ] 3.1400001
- [x] 3.14
- [ ] Compilation Error
- [ ] None of the above

---

**Explanation:**
Now when we add "f" in front of it, Basically we are trying to tell compiler, consider this as float. 
Ans= 3.14

---

### Difference Between Float and Double?

```
float a = 10.0f;
float b = 3.0f;
float c = (a/b); 
System.out.println(c);
```

```
double x = 10.0;
double y = 3.0;
double z = x/y;
System.out.println(z);
```
**Output:**
```plaintext
3.3333333
3.3333333333333335
```
**Explanation:**
* float -> can have upto 6 to 7 digits after decimal point.
* double -> can have upto 15 to 16 digits after decimal point.
* double is more precise [more digits after decimal point]

---

## Type Casting Float vs Double
**Rules:**

Same Rules of int vs long apply here, 

1. When we store float to double no loss of data hence no issue
{Implicit Type Casting}.
				
2. When we store double to float there can be a loss of data, complier will raise an error. 
```
double d = 3.14
float f = d // Error 
```
3. If we want to still force we need to keep explicitly type cast it.
```
double d = 3.14
float f = (float)d; // doubtle --> Explicilty --> float 
System.out.print(f); // 3.14
```

---
# Question


```
double x = 3.14;
float y = x;
System.out.print(y);
```

# Choices

- [ ] 3.14f
- [ ] 3.14
- [x] Compilation Error
- [ ] None of the above

---

**Explanation:**
Here we are trying to store a double type value into float. 
Error- Possible lossy conversion from double to float. 

---

# Question


```
double x = 17.67;
float y = (float)x;
System.out.print(y);
```

# Choices

- [x] 17.67
- [ ] 17.669999999999998
- [ ] Compilation Error
- [ ] None of the above

---

**Explanation:**
In this case, we are forcing the compiler to convert double to float. 
This is known as Explicit Typecasting. 
Ans= 17.67

**No data loss -> No error**
* int (45)  ->  double   -> No error 
* double (45.6)  -> int  -> Error

---

## Type Casting Decimal vs Non Decimal
For typecasting just remember 2 rules: 
1. 	If there is is no loss of data then no error : Implicit from non-decimal to decimal  : Implicit. 					
2. 	If there is chance for loss of data then error but We can still do this type casting forcefully : Explicit from decimal to non - decimal : Explicilty. 


---

# Question


```
double x = 3.45;
int y = x;
System.out.print(y);
```

# Choices

- [ ] 3
- [ ] 3.45
- [x] Compilation Error
- [ ] None of the above

---
**Output:**
```
Error- Possible lossy conversion from double to int. 
```

---

# Question


```
double x = 3.45;
int y = (int)x;
System.out.print(y);
```

# Choices

- [x] 3
- [ ] 3.45
- [ ] Compilation Error
- [ ] None of the above


---

**Explanation:**
Here we are forcing the compiler to convert 3.14 to int, We will only get the integer part. 
Ans= 3. 

---

# Question 

Quiz 24:
```
int x = 40;
double y = x;
System.out.print(y);
```

# Choices

- [ ] 40
- [x] 40.0
- [ ] Compilation Error
- [ ] None of the above


---

**Explanation:**
In this example, we are trying to store a int type value into double. 
Double stores decimal values, and here we can easily convert 40 to 40.0, therefore it is called Implicit Typecasting. 
Ans= 40.0


---


## Reading Inputs for Float and Double

```
How to take input for a float variable?
```
```
Scanner scn = new Scanner(System.in);
float a = scn.nextFloat();
```


```
How to take input for a double variable?
```
```
Scanner scn = new Scanner(System.in);
double a = scn.nextDouble();
```

#Ques 1:
```
float x = sc.nextFloat();
System.out.println(x);
```

 Explain we don't need to write "f" while taking inputs for float. 

---

# Question 


```
Input : 3.14
 
Scanner sc = new Scanner(System.in); 
float a = sc.nextFloat(); 
System.out.print(2 * a);
```

# Choices

- [ ] 2.0
- [ ] 3.14
- [x] 6.28
- [ ] 1.57

---

**Explanation:**
Now this 3.14 is stored on variable "a", Then we are trying to print 2*a-> 2* 3.14. 
Ans= 6.28

---

# Question


```
Input : 3.14 20
 
Scanner sc = new Scanner(System.in); 
int a = sc.nextInt(); 
int b = sc.nextInt();
System.out.print(a + b);
```

# Choices

- [ ] 17
- [ ] 3
- [ ] 14
- [x] Error

---

**Explanation:**
In the first line, we are trying to take an integer type input, But the user is not giving an integer value for the first time. 
Error-> Input mismatch. 

---

# Question 


```
Input : 3.14
 
Scanner sc = new Scanner(System.in); 
float a = sc.nextFloat(); 
float b = sc.nextFloat()
System.out.print(2 * a);
```

# Choices

- [ ] 6.28
- [ ] 3.14
- [x] Error
- [ ] None of the above


---

**Explanation:** 
There are 2 errors, 
In line `float b = sc.nextFloat()` semicolon is missing. 
We are only giving one input. 
Error- No such element exeception. 

---

# Ques 1

**Code:**
```
Input: 3.45
int x = sc.nextDouble();
System.out.println(x);
```
Explanation:

According to rules of typecasting, we cannot do it there is a chance of data loss. 
Ans=Error


**Correct Code:**
```
Input: 3.45
int x = (int)sc.nextDouble();
System.out.println(x);
```
Explanation:

In this case, we are forcing the compiler to do it, But int can only store integer value, so we will only get the integer part as output.
Ans=3


# Ques 2
```
Input: 3
double y = sc.nextInt();
System.out.println(y);
```

Explanation:

We can easily Typecast from integer to decimal. 
Ans=3.0

---
## Dividing numbers by zero

```
System.out.println(4 / 0); 
```
Output: 
```
Error
```

```
System.out.println(4.0 / 0);
```
Output:
```plaintext
Infinity
```
```
System.out.println(4.0f / 0); 
```
Output:
```plaintext
infinity
```

```
System.out.println(0 / 0); 
```

Output:
```plaintext
Error.
```

```
System.out.println(0.0 / 0);
```
Output:
```plaintext
NAN[Not A Number]. 
```



---
## Boolean Input


 Ques1:
```
boolean x = false;
System.out.println(x);
````

Output:
```
false.
```

boolean -> true / false only, it will work on True/False, but give answer in lowercase only. 

Ques2:
```

Input: true
Scanner sc = new Scanner(System.in);
boolean y = sc.nextBoolean();
System.out.println(y);
```

Output:
```
true
```
###  Take inputs like True/False/false also. 

---
## Arithmetic Operators

+, -, *, / are very basic arithmetic operators. Confirm whether the students know about them. And directly give the below quiz.

---


# Question
What will be the output?
```
int a = 10;
int b = 24;
System.out.println(a+b);
System.out.println(a-b);
System.out.println(a*b);
System.out.println(b/a);
```

# Choices
- [ ] 34<br>-14<br>240<br>2.4
- [ ] 34<br>14<br>240<br>2
- [x] 34<br>-14<br>240<br>2
- [ ] None of them

---


# Explanation

a + b -> 10 + 24 = 34
a - b -> 10 - 24 = -14
a * b -> 10 * 24 = 240
b / a -> 24 / 10 = 2 (Because both are integers, so the result should be an integer.)

---

One more arithmetic operator:
% -> Modulus Operator (Gives remainder of divison of two numbers as output)

### Examples
12 % 4 = 0
9 % 7 = 2
24 % 5 = 4

Now, give the following quiz.


---


# Question
What will be the output?
```
System.out.print(36 % 6);
```

# Choices
- [ ] 3
- [ ] 6
- [x] 0
- [ ] Error


---


# Question
What will be the output?
```
System.out.print(5 % 3);
```

# Choices
- [ ] 1
- [x] 2
- [ ] 3
- [ ] Error

If necessary, take some more examples.


---


**Q.** What are Relational operators?
**A.** Relational operators are used to check the relations between two operands. After comparison, the relational operators return a boolean value.

**Syntax:**
```
operand1 relational_operator operand2
```


|    Relation between a and b     | Syntax | a = 45, b = 16 | a = 5, b = 5 |
|:-------------------------------:|:------:|:--------------:|:------------:|
|       a is greater than b       | a > b  |      True      |    False     |
|        a is less than b         | a < b  |     False      |    False     |
| a is greater than or equal to b | a >= b |      True      |     True     |
|  a is less than or equal to b   | a <= b |     False      |     True     |
|         a is equal to b         | a == b |     False      |     True     |
|       a is not equal to b       | a != b |      True      |    False     |


**Note:** Explain the difference between assignment operator (=) and equality operator (==).

