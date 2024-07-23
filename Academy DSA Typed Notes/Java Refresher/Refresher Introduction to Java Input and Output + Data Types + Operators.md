# Introduction to Problem Solving

---
## Agenda

1. Output in Java
2. Data Types
3. Typecasting 
4. Input
5. Quizzes
6. Dashboard Walkthrough


---
## Output in  Java
Let's start with the famous example - **Hello World**


### Code to Print string/sentence/text
```cpp
public static void main(){

    System.out.print("Hello World!");

}
```

### Code to **print number**
```cpp
public static void main(){

    System.out.print(1);

}

```

### Observation
* Whenever we print a string, we put double quotes **" "** around it.
* Double quotes are not required for printing numbers.

---
### Question
System.out.print("Hey There");

**Choices**
- [x] Hey There
- [ ] "Hey There"
- [ ] Error
- [ ] "Hey There

**Explanation**
String between **""** will get printed. Therefore, solution is **Hey There**

---
### Question
system.out.print(10);

**Choices**
- [x] Error
- [ ] 2
- [ ] 10
- [ ] "10"


**Solution**
There is syntax error in above code.
Instead of **"system"** it should be **"System"**.
Error thrown is - "error: package system does not exist"


---
### Question

Predict the output:
System.out.print("5 * 10");

**Choices**

- [x] 5 * 10
- [ ] "5 * 10"
- [ ] 50
- [ ] Error


**Solution**

Prints the sentence / string / charactes between **""**, so instead of doing calculation & printing 50, we get :-
**5 * 10**

---
### Output in  Java Continued

#### Code to Print Answers to Basic Arithimetic Operations

```cpp
public static void main(){

    System.out.print(5 * 10);  // gives 50 as output
    System.out.print(10 / 5);  // gives 2 as output
    System.out.print(10 + 5);  // gives 15 as output
    System.out.print(10 - 5);  // gives 5  as output   
 
}
```
* **We use println to print in next line**

```cpp
public static void main(){
    System.out.println("My name is [instructor]");
    System.out.print("I am from [Hometown]");
}
```

---
### Question

```java
System.out.println("This question");
System.out.println("is easy!");
```
What's output of the above program ?


**Choices**
- [ ] This question is easy!
- [ ] This questionis easy!
- [x] This question
      is easy!
- [ ] This question's easy!


**Solution**

In first statement println is written hence "This question" gets printed and control goes to new line, then in next line, again println is there, so "is easy!" gets printed and control goes to next line.


---
### Question
```java
System.out.println("Red");
System.out.print("Blue ");
System.out.println("Green");
System.out.print("Yellow");
```
What's output of the above programme ?

**Choices**
- [ ] Red
      Blue Green Yellow
- [x] Red
      Blue Green
      Yellow
- [ ] Red
      BlueGreen
      Yellow
- [ ] Red Blue Green Yellow


**Solution**

First line has println, so after "Red" gets printed, control goes to new line.
Second statement has print, so after "Blue " gets printed, controls stays in the same line
Third line has println, so after "Green" gets printed, control goes to new line.
Fourth statement has print, so after "Yellow" gets printed, controls stays in the same line

---
### Output in  Java Continued

* We can do single line comments by ---> **//** 
```cpp
// single line comment
```
* We can do multi-line comments by ---> /* */
```cpp
/*
    this 
    is a
    multiline
    comment
*/
```
* Shortcut to do multi-line comments is to select the part to be commented and press ctrl + /

* We can concatenate two strings like:-
```cpp
System.out.println("Ram " + "Shayam"); // output: ram shayam and the control will go to the next line
System.out.println("My age is " +  25 ); // output: My age is 25 and the control will go to the next line
```

---
### Question

Predict the output:
System.out.print( 7 + 1 + "156");

**Choices**
- [ ] 71156
- [x] 8156
- [ ] 1568
- [ ] 15617

---
### Question

Predict the output:
System.out.print("156" + 7 + 1);

**Choices**
- [ ] 1568
- [ ] 15678
- [x] 15671
- [ ] 1568

**Solution**

Calculation shall happen from left to right.
For first +, one operand is number and another is string, so it will concatenate them, i.e 1567.
Then for second +, both operands are string, therefore concatenation will happen.
Hence, **answer is 15671**.

---
## Data types in  java

### Data types

1. **Primitive Data Types**
    These are predefined in the Java programming language.
**For example:** byte, short, int, long, double, float, boolean, char

2. **Non-Primitive Data Types**

    These are not predefined but defined by the programmer according to the need for a particular task.
**For example:** String, Arrays, class, etc.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/018/original/upload_8cbd044be7918278a42d8de841f78dac.png?1695053574)


**Primitive data types** are divided into two different types of values.

1. Numeric Data Types
2. Non-Numeric Data Types


#### Numeric Data Types
Numeric data types are used to store numeric values such as whole numbers and fractional numbers. They are divided into two parts, **integer** and **floating**.

**1. Integer**

**Byte, short, long, and int** these data types are used to store **whole numbers**
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/020/original/upload_b72992ead956aa0b3a1c17308ceca576.png?1695053630)

A. **Byte** Datatype:

It is commonly used when we want to store very small numbers of very limited size. Their data value is in the range of -128 to 127.
```cpp
byte a = 123; 
System.out.print(a); //Printing 123
```

B. **Short** Data Type

The short data type can have data values- in the range of -32,768 to 32767.

```cpp
short a = 123;
System.out.println(a);  //Printing 123
```

C. **Int** Data Type

The int data type is commonly used when we want to save memory in large arrays. The range is from -2,147,483,648 (-2^31) to 2,147,483,647 (2^31-1).

```cpp
int a = 123;
System.out.println(a);  //Printing the 123 
```

D. **Long** Data Type

The long data type is used when the int data type cannot handle a wider range than the int data type range. Data values is in the range of -9,223,372,036,854,775,808(-2^61) to 9,223,372,036,854,775,807(2^61 - 1).

```cpp
long a = 123123123;
System.out.println(a); //Printing the value of a
```

**2. Floating Values Data Types** 
There are two types of Floating values data types in java that are used to store fractional number values.

E. **Float** Data Type:
This data type is used to store numbers that have decimals up to 6 and 7 points.
```cpp
float a = 1231.231;
System.out.println(a); //Printing the value of a
```

F. **Double** Data Type:
This data type is used to store numbers that have decimals up to 15 decimals
```cpp
double a = 12312.23123;
System.out.print(a); //Printing the value of a
```

We generally use Integer and Long Data Types.
Remember their actual range is very tricky. Therefore, we can remember by stating in power of 10.

### Close Approximations:
**Int** - { -10^9 to 10^9 }
**Long** - { -10^18 to 10^18 }

#### Non Numeric Data Types

**String**
Strings can be created by giving sequence of characters surrounded by double quotes to a variable.

Example:

String S = “This is a String”

**Note:** We will study non primitive data types later.

---
## Typecasting in  java


### Typecasting
* Typecasting is converting one datatype to another.
* We can understand the concept of typecasting by following analogy.
* Let's have two tanks 
  * one large, with more capacity(say 100ml)
  * one small (say 50ml) 
* The large tanks corresponds to long datatype and small one corresponds to int datatype.
* Let's see the cases
* **Case 1:-** If water from smaller tank is poured to larger tank (int to long typecasting).
  * In this case the larger tank hold all the water or we can say int can be typecasted to long.
 ![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/022/original/p47.png?1695053732)

* **Case 2:-** If larger tank has water <= 50 ml and water from larger tank is poured to smaller tank.
  * Since the water in larger tank is equal to smaller tanks capacity the operation can be done.
  * We can say that long can be typecasted to int, if the data is within constraints of int datatype value range.
  ![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/023/original/p48.png?1695053757)

* **Case 3:-** If larger tank has water > 50 ml and water from larger tank is poured to smaller tank.
  * In this case, water will OVERFLOW.
  ![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/024/original/p49.png?1695053775)
  * When long is typecasted to int for data not within constraints of int datatype, the result would be **garbage value**.

#### Using variables
```cpp
String name = "arnav"
System.out.print("My name is " + name)
```

* We can declare variables as follows:-
```cpp
int i  = 5;
long p = 1000000000l;
float f = 3.14f;
double d = 1.141516171819;
```

* By default integers are considered int
* By default decimal values are considered double
* Convention of putting l ,f before long and float is only in coding area, not in input

#### Typecasting example 1
```cpp
// small --> large
int i = 5,
long I = i;
System.out.println(I); // will give 5 as output
```

#### Typecasting example 2
```cpp
// large —-> small
long l = 100000000000l
int i = l
System.out.print(i); 
```
* Above conversion will give an error:-Datatypes incompatible possible lossy conversion.
* This type of typecasting is **implicit typecasting**.

#### Typecasting example 3
```cpp
// large —> small
long l = 1000l;
int i = l;
System.out.print(i); 
```
* For safety, above conversion will give an error:- Datatypes incompatible possible lossy conversion.
* We can force the conversion by using **explicit typecasting**
```cpp
long l = 1000l;
int i = (int)l; // forcing to convert; explicit typecasting
System.out.print(i);// 1000 as output
```
* If we force the same typecasting with data out of int value range 
* In above case we would get garbage value.
```cpp
long l = 10000000000l;
int i = (int)l;
// forcing to convert
// explicit typecasting
System.out.print(i);// garbage value as output
```

---
### Input in  java


* Scanner class is used to take inputs in java.
* Following are the methods to take number inputs in java:-
```cpp
scn = new Scanner(System.in);
int i = scn.nextInt();
long t = scn.nextLong();
float f = scn.nextFloat( ) ;
double d = scn.nextDouble();

```
* Following are methods to take string input in java.
```cpp
//scn. next ( ) —> Reads only 1 word from input
String s = scn.next();
System. out. print(s);

//scn.nextLine() —> Reads entire line from input
String s1 = scn.nextLine();
System.out.print(s1);
``` 

---
## Question 1

### Question
Take 2 names X and Y as input and print X loves Y.
### Testcase

```java
X  = Ram
Y  = Shyam
```
### Solution

`Output : Ram loves Shyam`

#### Code
```java
String x = scn.next();
String y = scn.next();
System.out.print(x + " loves " + y);
```

---
## Question 2


### Question
Take name X and age Y as input and print X age is Y.
### Testcase

```cpp
X = Aarnav
Y = 25
```
### Solution
`Output : Aarnav age is 25`
#### Code
```java
String x = scn.next();
int y = scn.nextInt();
System.out.print(x + " age is " + y);
```
