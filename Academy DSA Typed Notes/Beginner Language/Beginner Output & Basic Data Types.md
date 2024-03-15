# Output and Basic Data Types

---

## Agenda

- Revise Initial Rules
- Evaluating Expression
- Quizzes
- Concatenation
- Intro to variable

---
# Section 2.1 (Revision)



1. end statements with a **semicolon ( ; )**
2. JAVA is **case sensitive.** -> System, system are considered different
3. In order to print text, we use **double quotes ( " " )**
4. {}, (), " " --> All of these are in pairs.
5. Comments → 
    * **Single-line comments** start with two forward slashes ( // ). Any text between // and the end of the line is ignored by Java (will not be executed).
    * **Multi-line comments** start with /* and ends with \*/. Any text between /* and */ will be ignored by Java.
6. **System.out.print(); →** Just type the output
7. **System.out.println(); →** Just type the output and press Enter [cursor moves to the next line]


Now, let's check how much they remember from the last class with the help of quizzes.


---


# Question

What will be output for this ?
```
System.out.print("Welcome in playground")
```
# Choices

- [ ] Welcome Home
- [ ] Welcome in playground
- [x] Error
- [ ] All the options are correct


---


# Question 

What will be output for this ?
```
system.out.print("Hi Everyone");
```

# Choices

- [ ] Hi Everyone
- [ ] Bye Everyone
- [x] Error
- [ ] Welcome Everyone


---


# Question 
What will be output for this ?
```
System.ouT.print("Hi Guys");
```

# Choices
- [ ] Hi Guys
- [ ] Bye Guys
- [x] Error
- [ ] Welcome Guys


---


# Question 
What will be output for this ?
```
System.out.print(Good Morning Everyone);
```

# Choices

- [ ] Good Morning Everyone
- [ ] Good Afternoon Everyone
- [x] Error
- [ ] Good Night Everyone



---


# Question

What will be output for this ?
```
System.out.print('Happy Thursday');
```

# Choices

- [ ] Happy Thursday
- [ ] Sad Thursday
- [x] Error
- [ ] All the options are correct



---


# Question 
What will be output for this ?

```
System.out.print(10 + 20); 
```


# Choices

- [x] 30
- [ ] 10+20
- [ ] Error


---


# Question 

What will be output for this ?
```
System.out.print(10 - 25);
```

# Choices
- [x] -15
- [ ] 15
- [ ] 10
- [ ] Error

---


# Question 

What will be output for this ?
```
System.out.println("Hello");
System.out.print("World);
```

# Choices

- [ ] Hello<br>World
- [ ] HelloWorld
- [x] Error
- [ ] inky pinky po



---


# Question 
What will be output for this ?
```
System.out.print("Hello");
System.out.println("World");
```

# Choices
- [ ] Hello<br>World
- [x] HelloWorld
- [ ] Error
- [ ] inky pinky po

---


# Question 
What will be output for this ?
```
System.out.println("Hello");
System.out.print("World");
System.out.println("Welcome")
```

# Choices

- [ ] Hello<br>World<br>Welcome
- [ ] HelloWorldWelcome
- [x] Error
- [ ] Hello<br>WorldWelcome



---


# Question 

What will be output for this ?
```
System.out.printLN("Hello");
System.out.println("World);
```

# Choices
- [ ] Hello<br>World
- [ ] HelloWorld
- [x] Error
- [ ] inky-pinky-po



---


# Question 
What will be output for this ?
```
Which of the follwing are operators?
```

# Choices
- [ ] ( + )
- [ ] ( - )
- [ ] ( * )
- [ ] ( / )
- [x] All of them


---


# Question 

```
10+30
In the given expression choose the operands.
```

# Choices
- [ ] (+)
- [ ] 10
- [ ] 30
- [x] Both 10 and 30
---

**Explanation of Quiz :** 
Operator : + 
Operands : 10 and 30

Explain using one more example if needed.

Numbers -> 2 types
1. Decimal -> Numbers that have Decimal point
Ex. 4.67, 0.986, 20.73, 2.0
2. Non Decimal / Integer -> Any +ve, -ve or 0
Ex. 7, -30, 0, -7
		
- Note: In today's class, we will only discuss Integers.


Very Basic expression on simple maths. Time of the quiz is 20sec. 


---


# Question 
What will be output for this ?
```
System.out.print(5 + 8);
```

# Choices
- [ ] 11
- [ ] 12
- [x] 13
- [ ] 14

---


# Question 
What will be output for this ?
```
System.out.print(5 - 8);
```

# Choices
- [ ] -1
- [ ] -2
- [x] -3
- [ ] -4

---


# Question 
What will be output for this ?
```
System.out.print(5 * 8);
```

# Choices

- [ ] 30
- [ ] 32
- [x] 40
- [ ] 42

---


# Question 
What will be output for this ?
```
System.out.print(8 / 2);
```

# Choices
- [ ] 3
- [x] 4
- [ ] 5
- [ ] 6


---


# Question 

What will be output for this ?
```
System.out.print(10 / 3);
```

# Choices

- [ ] 3.3333
- [x] 3
- [ ] Error
- [ ] None of them
---

**Explanation :**
In calculator, 10 / 3 = 3.33333
But in JAVA, we get 3


**Rule :**  In JAVA, when you divide (/) integers we only get quotient.

---


# Question 

What will be output for this ?
```
System.out.print(24 / 9);
```

# Choices

- [ ] 1
- [ ] 2.54
- [x] 2
- [ ] 3

---


# Question 

What will be output for this ?
```
System.out.print(3 / 6);
```

# Choices
- [ ] 1
- [x] 0
- [ ] Error

---


# Question 
What will be output for this ?
```
System.out.print(24 / 0);
```

# Choices
- [ ] Infinite
- [ ] 24
- [ ] 0
- [x] Error

---


## **Rule:** 
Division of integers by zero is not possible in JAVA

---


# Question 
What will be output for this ?
```
System.out.print(6 * 7 / 6);
```

# Choices
- [x] 7
- [ ] 6
- [ ] None of them
- [ ] All of them

---


**Explanation:**
<img 
src= "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/233/original/upload_62530fdedbeb3e0a6c288afc122c7b4b.png?1695416761" 
alt = "" width ="700" height = "350">

But we cannot have two answers for the same expression.
So, there must be some rules in place to get the output.

---


## Priority in Operators:

   1. Rank 1 :  **()**
   2. Rank 2 : __*__ , __/__
   3. Rank 3 : __+__ , __-__ 

### Few important rules of doing operations 
 
* **Rule 1 :**<br> If we have same priority operators, whichever comes first from left to right that will be evaluated first.
* **Rule 2 :**<br> If we have different priority operators, whichever has highest priority that will be evaluated first.

**Explanation:**
Here, * and / have same priority. Because * comes first we will evaluate 6 * 7 will be evaluated first.
=> 6 * 7 / 6 
=> 42 / 6 
=> 7

---


# Question 

What will be output for this ?
```
System.out.print(4 + 3 * 6 - 7 / 2);
```

# Choices
- [ ] 16
- [ ] 17
- [ ] 18
- [x] 19
---
**Explanation:**
Between * and / we will be evaluating multiply first and then divide. 
=> 4 + 3 * 6 - 7 / 2 
=> 4 + 18 - 7 / 2 
=> 4 + 18 - 3 
=> 22 - 3 
=> 19

---

# Question 
What will be output for this ?

```
System.out.print(5 + 2 * 3);
```

# Choices
- [ ] 21
- [ ] 17
- [x] 11
- [ ] Error
---
**Explanation:**
Here, * has higher priority.
=> 5 + 2 * 3 
=> 5 + 6 
=> 11

---

# Question 
What will be output for this ?
```
System.out.print(5 + 15 / 5 + 6 * 3);
```

# Choices
- [ ] 30
- [x] 26
- [ ] 11
- [ ] Error
---
**Explanation:**
=> 5 + 15 / 5 + 6 * 3
=> 5 + 3 + 6 * 3 
=> 5 + 3 + 18
=> 8 + 18
=> 26

---

# Question 

What will be output for this ?
```
System.out.print(7 - 2 * 4 + 18 / 3);
```

# Choices
- [ ] 15
- [x] 5
- [ ] 30
- [ ] Error
---
**Explanation:**
=> 7 - 2 * 4 + 18 / 3
=> 7 - 8 + 18 / 3
=> 7 - 8 + 6
=> -1 + 6
=> 5

---

# Question 
What will be output for this ?
```
System.out.print(3 * 4 / 2 + 7 + 3 - 4 / 2);
```

# Choices
- [ ] 21
- [x] 14
- [ ] 11
- [ ] Error
---
**Explanation:**
=> 3 * 4 / 2 + 7 + 3 - 4 / 2
=> 12 / 2 + 7 + 3 - 4 / 2
=> 6 + 7 + 3 - 4 / 2
=> 6 + 7 + 3 - 2
=> 13 + 3 - 2
=> 16 - 2
=> 14

---

# Question 
What will be output for this ?
```
System.out.print(5 + 2 * 4 + 8 - 6 + 12 / 4);
```

# Choices
- [ ] 25
- [x] 18
- [ ] 16
- [ ] Error
---
**Explanation:**
=> 5 + 2 * 4 + 8 - 6 + 12 / 4
=> 5 + 8 + 8 - 6 + 12 / 4
=> 5 + 8 + 8 - 6 + 3
=> 13 + 8 - 6 + 3
=> 21 - 6 + 3
=> 15 + 3
=> 18

---

# Question 
What will be output for this ?
```
System.out.print( (5 + 2) * 3 );
```

# Choices
- [x] 21
- [ ] 17
- [ ] 11
- [ ] Error
---
**Explanation:**
=> (5 + 2) * 3) 
=> 7 * 3
=> 21

---

# Question 
What will be output for this ?
```java
System.out.print("Hello" + "World");
```
# Choices
- [ ] Hello<br>World
- [x] HelloWorld
- [ ] Error
- [ ] I'm sleeping, Don't Disturb
---
**Explanation:** 

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/234/original/upload_9d8f2e7e5fa8e1f3b5bdd0b1c4c521c9.png?1695417058"
width = "700" height = "450">

**Rule:** With + operator, If one Operand is text then we concatenate both Operands 

---

# Question 
What will be output for this ?
```
System.out.print("Hi" + "Students" + "Namaste");
```

# Choices
- [x] HiStudentsNamaste
- [ ] HelloEveryone
- [ ] Error
- [ ] I'm Angry :(
---
**Explanation:**
=> "Hi" + "Students" + "Namaste"
=> "HiStudents" + "Namaste"
=> "HiStudentsNamaste"

---

# Question 
What will be output for this ?
```
System.out.print("Hi" + " " + "Namaste");
```

# Choices
- [x] Hi Namaste
- [ ] HiNamaste
- [ ] Error
- [ ] Namaste Hi
---
**Explanation:**
=> "Hi" + " " + "Namaste"
=> "Hi " + "Namaste"
=> "Hi Namaste" 

---

# Question 
What will be output for this ?
```
System.out.print("Hi" * "Guys");
```

# Choices
- [ ] HiGuys HiGuys HiGuys
- [x] Error
- [ ] abcdefghijklmnopqrstuvwxyz
- [ ] Hi Guys
---
**Explanation:**
We cannot use * with text operand.


## **Rule:**
With text operand, only + operator can be used. Any other operator gives error.

---

# Question 
What will be output for this ?
```
System.out.print("WelcomeHome" - "Home");
```

# Choices
- [ ] Welcome
- [ ] WelcomeHome-Home
- [ ] Home
- [x] Error
---
**Explanation:**
We cannot use - with text operand.

---

# Question 
What will be output for this ?
```
System.out.print("Hello" + 3);
```

# Choices
- [ ] Hello
- [x] Hello3
- [ ] Error
- [ ] HelloHelloHello
---
**Explanation:**
Operator: +
Operands:
"Hello" -> text
3  -> number
 Since, one operand is text, we concatenate both operands.

---

# Question 
What will be output for this ?
```
System.out.print("Hello" + 3 + 4);
```

# Choices
- [ ] Hello
- [x] Hello34
- [ ] Hello7
- [ ] Error
---
**Explanation:** 
Since, both operators are + and have same priority we will evaluate from left to right
=> "Hello" + 3 + 4
=> "Hello3" + 4
=> "Hello34"

---

# Question 
What will be output for this ?
```
System.out.print("Hello" + 10 + "World");
```

# Choices
- [ ] HelloWorld
- [x] Hello10World
- [ ] Hello10
- [ ] Error
---
**Explanation:** 
=> "Hello" + 10 + "World"
=> "Hello10" + "World"
=> "Hello10World"

---

# Question 
What will be output for this ?
```
System.out.print(10 + "Welcome");
```
# Choices
- [ ] Welcome10
- [x] 10Welcome
- [ ] Welcome 10 times
- [ ] inky pinky po
---
**Explanation:** 
=> 10 + "Welcome"
=> "10Welcome" 

---

# Question 
What will be output for this ?
```
System.out.print(10 + 20 + "WakeUp" + 3 + 2);
```

# Choices
- [ ] 1020WakeUp32
- [ ] 1020WakeUp5
- [ ] 30WakeUp5
- [x] 30WakeUp32
---
**Explanation:**
=> 10 + 20 + "WakeUp" + 3 + 2
=> 30 + "WakeUp" + 3 + 2
=> "30WakeUp" + 3 + 2
=> "30WakeUp3" + 2
=> "30WakeUp32" 

---

# Question 
What will be output for this ?
```
System.out.print("HiGuys" * 2);
```

# Choices
- [ ] HiGuys*2
- [ ] HiGuys2
- [ ] HiGuysHiGuys
- [x] Error
---
**Explanation:**
We cannot use * operator with text operand

---

# Question 
What will be output for this ?
```
System.out.print(10 + 20 + "WakeUp" + 3 * 2);
```

# Choices
- [ ] 1020WakeUp32
- [ ] 30WakeUp32
- [ ] Error
- [x] 30WakeUp6
---
**Explanation:**

=> 10 + 20 + "WakeUp" + 3 * 2
=> 10 + 20 + "WakeUp" + 6
=> 30 + "WakeUp" + 6
=> "30WakeUp" + 6
=> "30WakeUp6"

---

# Question 
What will be output for this ?
```
System.out.print(10 + "Hello" * "World" + 3);
```

# Choices
- [ ] 10HelloWorld3
- [ ] 10HelloWorldWorldWorld3
- [x] Error
- [ ] Good Morning :)
---
**Explanation:**
We cannot use * operator with text operand

---

# Question 
What will be output for this ?
```
System.out.print(10 + "WelcomeHome" - "Home" + 3);
```
# Choices
- [ ] 10Welcome3
- [ ] 10WelcomeHomeHome3
- [x] Error
- [ ] Good Morning :)
---
**Explanation:** 
We cannot use - operator with text operand


---

# Question
Predict the output for the following code:
```
System.out.println(10 + 20 + "Hello");
```

# Choices
- [ ] 1020Hello
- [x] 30Hello
- [ ] Hello1020
- [ ] Hello Hello Hello
---
**Explanation**
10 + 20 = 30, 
 Now when string is concatenated then 30 becomes as string "30" so the answer is "30Hello".
 

---
# Section 2.3 (Introduction to Variables)

> Start with that numbers are of two types:
1. **Non-Decimal / Integers** 
2. Decimals

**Story :** Assume we have a container storing water in it. And then explain the three factors of container that are : Type, Name and Value

After that take a container to store integers and explain the same three factors.


<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/235/original/upload_23ef2438b9c3b2043ca7f53fffb61f9d.png?1695417557" width = "750" height = "350">

In programming, containers are known as variables.

## Creating a variable:

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/236/original/upload_4734a0a6fd149a8b7767b1498637f82a.png?1695417585"
width = "750" height = "250">

---

# Question 
What will be output for this ?
```java
Create a variable of type int and give name as num and assign 34 in it.
```

# Choices
- [ ] num = 34
- [x] int num = 34;
- [ ] int 34 num
- [ ] num int = 34



---

# Question 
What will be output for this ?
```
int val = 30;
System.out.println(val);
```

# Choices
- [ ] val
- [x] 30
- [ ] Error
- [ ] Don't Select me, I'm wrong option
---
**Explanation:**
The value of variable val is 30.

**Rule :** Whenever we use variable name, the value of that variable is used.

---

# Question 
What will be output for this ?
```
int a = 10;
int b = 20;
System.out.println(a + b);
```

# Choices
- [ ] ab
- [x] 30
- [ ] Error
- [ ] Keep focus on the above option, I am wrong




---

# Question 
What will be output for this ?
```
int a = 10;
int b = 20;
System.out.println("Sum of Number is " + a + b);
 ```
 
# Choices
- [ ] Sum of Number is 30
- [x] Sum of Number is 1020
- [ ] Error
- [ ] Above Options, Not me :)
---
**Explanation:**

Here, both operators are + and have same priority. Hence, the exppression will be evaluated from left to right.
=> "Sum of Number is " + a + b
=> "Sum of Number is " + 10 + 20
=> "Sum of Number is 10" + 20
=> "Sum of Number is 1020"


---

# Question 
What will be output for this ?
```
int a = 10;
int b = 20;
System.out.println("Product of Number is " + a * b);
```

# Choices
- [ ] Product of Number is 1020
- [x] Product of Number is 200
- [ ] Error
- [ ] Again Above Options, Not me :)
---
**Explanation:**
Here, * has highest priority. So, a * b will be evaluated first.
=> "Product of Number is " + a * b
=> "Product of Number is " + 10 * 20
=> "Product of Number is " + 200
=> "Product of Number is 200"

---
# Section 2.4 (Summary)
1. In Java, when we divide ( / ) integers we only get quotient.
2. We cannot divide integers by 0, we get error.
3. Priority of Operators : 
   * Rank 1 :  **()**
   * Rank 2 : __*__ , __/__
   * Rank 3 : __+__ , __-__ 
4. When two operators of different priority are there, we evaluate the one with higher priority first.
5. When two operators of same priority are there, we evaluate the one which comes first from left to right.
6. With + operator, if one of the operand is text then we concatenate both the operands.
7. Creating a variable:
    * type name = value;
    * Way 1 : 
        * int x = 30;
    * Way 2 : 
        * int y;
            y = 40;
8. When we use variable name, we use its value.








