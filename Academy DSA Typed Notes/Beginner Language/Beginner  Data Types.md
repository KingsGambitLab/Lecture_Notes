# Beginner: Data Types

---

# Agenda

* Quizes to revise the previous session
* Rules of Naming a variable
* Different categories of Data
  * Why we need multiple datatype under one category
  * Int Vs Long
* TypeCasting

:::success
There are a lot of quizzes in this session, please take some time to think about the solution on your own before reading further.....
:::

---

# Question 

What will be output for this ?
```
System.out.print(12 + 4 + "try" + 3 * 4);
```
# Choices
- [ ] Error
- [ ] 124try34
- [ ] 16try34
- [x] 16try12


---

# Question

```
Declare a int variable with name x and intialize with value 10
```

# Choices
- [ ] x int = 10;
- [ ] int x = 20
- [x] int x = 10;
- [ ] None of them

---


# Question
```
int x = 10;
int y = 20;
System.out.print(x + y);
```

# Choices
- [ ] Error
- [ ] x + y
- [x] 30
- [ ] 1020


---


# Question
```
int x = 10;
int y = 20;
System.out.print(x + " " + y);
```

# Choices

- [ ] 1020
- [ ] Error
- [x] 10 20
- [ ] 30


---

# Question
```
int try = 10;
System.out.print(Try);
```
# Choices

- [ ] 10
- [ ] Try
- [x] Error

---


# Question
```
System.out.print(x);
int x = 10;
```
# Choices
- [ ] x
- [ ] 10
- [x] Error
- [ ] None of the above

---


**Rule:** In order to use a variable we need to declare and initialise it first.

---


# Question
```
int x = 10;
System.out.print(x + y);
int y = 20;
```
# Choices
- [ ] 30
- [ ] 10y
- [x] Error
- [ ] None of them


---


# Question
```
int x = 10;
int x = 20;
System.out.print(x);
```
# Choices
- [ ] 10
- [ ] 20
- [x] Error
- [ ] None of them

---


**Explanation:**
Here, when we write `int x = 10;`, we are declaring and initialising a variable "x". 
Now when we write this statement, `int x = 20;`, again a variable is created of type int, and name x with value 20.
But this is not possible, we cannot have 2 variables with same name.


## **Rule:** We cannot have 2 variables with same name.

---


# Question
```
int x = 20;
System.out.println(x);
x = 40;
System.out.print(x);
```
# Choices
- [ ] 2040
- [ ] Error
- [x] 20 40

---

**Explanation:**
Here, when we write `int x = 20;` , a variable is created of type int and name x. 
But `x= 40` means we are not creating the variable, instead changing the value of the variable. This line will change the value of x to 40. 


---


# Question
```
int x = 20;
int y  = 40;
x = y + 10;
System.out.print(x);
```

# Choices

- [ ] 70
- [ ] 60
- [x] 50

---


**Explanation:**

With very first line, <img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/248/original/Screenshot_2023-09-23_104216.png?1695445969" height = "40" width = "120"> ;, we are creating a variable of type int and name x. Again <img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/249/original/Screenshot_2023-09-23_104341.png?1695446029" height = "25" width = "120">; another variable is created of type int and name y. Then <img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/250/original/Screenshot_2023-09-23_104437.png?1695446089" height = "25" width = "120">; means update the value of x to 50. 

---


# Question
```
int x = 20,y = 40;
System.out.print(x + y);
```
# Choices
- [ ] Error
- [ ] x + y
- [x] 60

---



**Explanation:**
Everytime in Java a statement ends with semicolon. 
In this line there is a comma so we are trying to create a variable x and y of type int. 

**Rule:** We can create two multiple variables of same type in a single line seperated by comma. 

---


# Question
```
int x = 20;y = 40;
System.out.print(x + y);
```
# Choices
- [x] Error
- [ ] x + y
- [ ] 60

---



**Explanation:**
Here semicolon is present after 20. That means with <img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/251/original/Screenshot_2023-09-23_104216.png?1695446171" height = "45" width = "120"  style="margin: -10px 0px 0px 0px;" >; we are creating a variable and <img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/252/original/Screenshot_2023-09-23_104656.png?1695446243" height = "25" width = "70"  style="margin: 0px 0px 0px 0px;" >; we are not declaring a variable. 


---


# Question
```
int x = 20,y = 40,z = 80;
System.out.print(x + y + z);
```
# Choices
- [ ] Error
- [ ] 150
- [x] 140
- [ ] None of them

---



**Explanation:**
Here we are creating 3 variables which are seperated by commas which is possible. 

---



## Rules of Naming a variable:
1.  Name can only contain lowercase[a - z], uppercase alphabets[A - Z], digits(0 - 9), '\$'{Dollar} or '_' {Underscore}, nothing else
2. 	Name cannot start with a digit
3. 	Cannot use reserve keywords as variable name : 
Reserve keywords : Words which already have a predefined 
meaning in java, they have a predefined use for them
Ex : public, static, void, int, etc : 
4. Variable name is also case senstive. 

---


# Question
```
How many of them are correct variable names?
int x = 10;
int 1y = 20;
int x@a = 20;
```
# Choices
- [x] 1
- [ ] 2
- [ ] 3
- [ ] 0

---


**Explanation:**
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/253/original/Screenshot_2023-09-23_104835.png?1695446325" height = "25" width = "120"  style="margin: 0px 0px 0px 0px;" >; here second rule is not followed, we are starting a variable name with a digit. This is a invalid variable name. 
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/254/original/Screenshot_2023-09-23_105017.png?1695446427" height = "30" width = "130"  style="margin: 0px 0px 0px 0px;" >; this is also invalid because here we are having @ in variable name which is not allowed.

---


# Question
```
How many of them are correct variable names?
int _y = 10;
int xxy = 20;
int x a = 20;
int y$z = 45;
```

# Choices
- [ ] 1
- [ ] 2
- [x] 3
- [ ] 4
- [ ] 0

---


**Explanation:**
_y -> valid, 
xxy -> valid
x a -> cannot have space in name, therefore invalid. 
y\$z -> valid.

---


# Question
```
int n = 20;
int N = 30;
System.out.print(n + N);
```

# Choices
- [x] 50
- [ ] 2030
- [ ] Error

---


**Explanation:**
Variables 'n' and 'N' are completely different, Java is case sensitive. 

---

# Question

```
int static = 40;
System.out.print(static);
```

# Choices
- [ ] 40
- [ ] static
- [x] Error

---


**Explanation:**
"static" is reserve keyword. 


---


## Different categories of Data:
There are 3 categories of Data:
1. Text:
      * String: words/sentences. 
      * char: 1 character
2. Numbers:
   a. Decimal:
      * float
      * double
     
   b. Non-Decimal(Integers):
      * byte: almost never used. 
      * short: almost never used. 
      * int 
      * long
3. Boolean:
   *  boolean
    * True/False

### Why We Need Multiple Datatype Under One Category:


<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/244/original/upload_bdc30e4d28acbd24dcec0e8e57749503.png?1695445499"
     height = "350" width = "700" >

All of them store water. 
Difference lies in their storage capacity. 



| category |   small    | medium | large |
|:--------:|:----------:|:------:|:-----:|
|  500ml   | yes [ideal] |  yes   | yes  |
|   15L    |     no     |   no   |  yes  |


---

### Int Vs Long:
They both have different range. 

**int:** <img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/245/original/Screenshot_2023-09-23_103645.png?1695445684"
              height = "50" width = "200">

**approx:** <img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/246/original/Screenshot_2023-09-23_103749.png?1695445719"
                 height = "55" width = "200">


**long:**<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/247/original/Screenshot_2023-09-23_104014.png?1695445828" 
              height = "60" width = "200">


**approx:** <img src ="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/255/original/Screenshot_2023-09-23_105318.png?1695446607"
                 height = "30" width = "200">

---

# Question
Predict the output:
```
int num = 100000; // 10^5
System.out.print(num);
```
# Choices
- [x] 100000
- [ ] Error
- [ ] No clue!

---


**Explanation:**
Here we are creating a variable of type int, name num and value: 100000. 
It is in the range if int. 
Ans = 100000. 

---

# Question

What will be the output?
```
int x = 10000000000; //10^10
System.out.print(x); 
```
# Choices
- [ ] 10000000000
- [x] Error
- [ ] Too many zeroes!

---

**Explanation:**
Error, Integer number too large. 
Because 10^10 is out of range of int.

---

# Question
Predict the output:
```
long n = 10000000000; // 10^10
System.out.print(n);
```
# Choices
- [x] Error
- [ ] 10000000000
- [ ] Choose me. I am best!

---

**Explanation:**
Error: Integer number too large. 

**Rule:** whenever the compiler see a non decimal number it considers it as int.

Now here, We are storing the value 10000000000 into long, But as soon as compiler see the non decimal digit it consider it as int and which is out of range of int. Therefore we get error. 

---

# Question
Predict the output:
```
long a = 10000000000L; //10^10
System.out.print(a);
```

# Choices
- [ ] Error
- [ ] a
- [x] 10000000000
- [ ] 10000000000L

---

**Explanation:**
When we write "L" in front of the number it is telling the compiler that consider this number as long, not int. 

---

# Question
Predict the output:
```
long a = 10000000000l; //10^10
System.out.print(a);
```

# Choices
- [ ] Error
- [ ] 10000000000l
- [x] 10000000000
- [ ] Too tired to count zeroes!

---

**Explanation:** 
Either use "L" or "l", both will work. 


----

## TypeCasting:
Typecasting means converting one datatype to another. 
Basically, Tranfering data from one container to another. 

**Anology:**

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/256/original/upload_c9d475a202262c1a5c542216c6589737.png?1695446752" height = "280" width = "700" >

1. We can easily transfer water from 5L bucket to 20; bucket. 
From smaller storage to higher storage, we can easily do it. 

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/257/original/upload_56a679ca68e84294e7fa9897f30e6f94.png?1695446782" height = "280" width = "700" >

2. We can again transfer water from 20L bucket to 5L bucket, if the water level is less than 5L. 

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/258/original/upload_6a3bb23eb0715c66bbe4ea20ebe87e2c.png?1695446814" height = "280" width = "700" >

3. We have 8L of water in 20l bucket, now this time when we try to transfer it to 5L bucket, overflow will happen. Water will flow outside of the bucket as well. It will spill. 

**Replicate the example with data types:**
5L bucket: int
20L bucket: long. 

4. Easily transfer data from int(smaller) to long(bigger). 

---

# Question
```
int a = 1000;
long b = a;
System.out.print(b);
```
# Choices
- [x] 1000
- [ ] Error

---

**Explanation:**
Here,`int a = 1000;` we are trying to create a int type variable of name a, value 1000. 
Now `long b = a;` with this we create a long type variable, name b.
b = 1000.
And we can easily store 1000 in long. 

**It is Implicit/Widening TypeCasting(automatic).**

---

# Question
```
long x = 10000;
System.out.print(x);
```

# Choices
- [x] 1000
- [ ] Error

---

**Explanation:**
Java considers non decimal number as int. 
Therefore, the value 10000 is considered as int and we are trying to store int value into long which is possible. 
Int to Long is implicit typecasting. 

---

# Question

```
long x = 10000;
int y = x;
System.out.print(y);
```

# Choices
- [ ] 1000
- [x] Error

---

**Explanation:**
`long x = 10000` It is implicit typecasting. 
But, `int y = x;` Here we are trying to store long value into int container.
Error: Possible lossy conversion. 

---

# Question
```
long x = 1000;
int y = (int)x;
System.out.print(y); 
```

# Choices
- [x] 1000
- [ ] Error

---

**Explanation:**

Here we are doing Explicit/Narrowing Typecasting from long to int. 


---

# Question

```
long a = 10^10;
int  b = (int)a;
System.out.print(b);
```

# Choices
- [ ] 10^10
- [ ] 10^10L
- [x] Error
- [ ] Some random value

---

**Explanation:**

Here, value 10^10 is too large for int. 
Ans = Error, Integer number too large. 


---

# Question
```
long a = 10^10L;
int  b = (int)a;
System.out.print(b);
```


# Choices
- [ ] 10^10
- [ ] 10^10L
- [ ] Error
- [x] Some random value

---
**Explanation:**

Here, We are specifying L so compiler considers 10^10 as long only and then we are trying to store in a long container only which is possible. 
After that in next line we are doing explicit typecasting, but then also we know that this number is out of range of int. 
We are actually forcing the compiler to do it, data loss will happen.
 
---
Some quizzes to revise

---

# Question

```
int a = (int)10000000000L;
System.out.print(a);
```

# Choices
- [x] Some Random Value
- [ ] Error
- [ ] Very Complicated

---


# Question

```
int a = (int)10000000000;
System.out.print(a);
```

# Choices
- [ ] Some Random Value
- [x] Error
- [ ] 10000000000

