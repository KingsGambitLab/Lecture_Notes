# Beginner: Operators
---
## Agenda

* Typecasting Revision
* Rules doing basic operations
* Integer Overflow
* Operators (Logical, Unary)

:::success
There are a lot of quizzes in this session, please take some time to think about the solution on your own before reading further.....
:::

---

## Rules
1. While type casting, if no chance of data loss, then we get no error -> Implicit / Widening Typecasting (Happens automatically).
2. If there may be a data loss, then we will get some error. If we still want to typecast, we forcefully have to do it -> Explicit / Narrowing (forcefully).

**Note:** If students are not able to understand, run the corresponding quiz code in IDE, and then clarify any questions.


---


# Question
Predict the output:
```
int abc = 400;
long x = abc;
System.out.print(x); 
```

# Choices
- [x] 400
- [ ] Error
- [ ] Random Value
- [ ] Good Morning!

---


# Explanation
When we store int into long, there is no data loss, hence 400 is the answer. Explain more if necessary.



---


# Question

Predict the output:
```
long a = 100000; // 10^5
System.out.print(a);
```

# Choices
- [ ] Error
- [x] 100000
- [ ] a

---


# Explanation
**Mistake:** Some students may think that we need a L after the number but its not necessary. Because implicity typecasting is going on. Explain more, if needed.


---


# Question

Predict the output:
```
long x = 500000;
int y = x;
System.out.print(y);
```

# Choices
- [x] Error
- [ ] 500000
- [ ] Some random value
---


# Explanation

```
long x = 500000; // This line is correct (Implcity typecasting)
int y = x; // Possible data loss.
System.out.print(y);
```
We cannot store a long into int, because of possible data loss. Hence, the error.

**Q.** Ask students on how to correct this?
**A.** Explicit typecasting

Move on to the next quiz which is based on this.



---


# Question
Predict the output:
```
long n = 60000;
int a = (int)n;
System.out.print(a); 
```

# Choices
- [ ] Random Value
- [ ] Error
- [x] 60000
- [ ] How would I know?

---


# Explanation
The 2nd line is forcing the compiler to change the long to int which is correct.

**Mistake:** Some students may ask why we won't get any random value. Because, 60000 is within the range of int data type, and hence no loss.

Range of int  -> -2 * 10^9 to 2 * 10^9

Give the following example:
long x = 100000000000 // 10^11
This number is too large and so we need to mention explicity that:
long x = 100000000000L.


---


# Question
Predict the output:
```
long a = 100000000000L; // 10^11
int b = (int)a;
System.out.println(b);
```

# Choices
- [ ] 100000000000
- [ ] Error
- [x] Random Value
- [ ] Too many zeroes

---


# Explanation

Since 10^11 cannot be stored in int, and we are forcing. So, data loss (Overflow) is happening, and some value is getting lost, we are getting random value.


---
title: Quiz 6
description: Quiz 6
duration: 30
card_type: quiz_card
---

# Question
Predict the output:
```
double x = 7.89; 
System.out.print(x);
```

# Choices
- [ ] 7
- [x] 7.89
- [ ] Error
- [ ] Ex is not texting back.

---

# Explanation

Since the right value is of type double. We can store double into double without any issues.


---

# Question
Predict the output:
```
float val = 10.78; 
System.out.print(val); 
```

# Choices
- [ ] 10.78
- [ ] 10
- [x] Error
- [ ] I am sleeping

---

# Explanation

Any decimal number is of double type, while the type of val is float. 
**Q.** Can we store double into float type?
**A.** No, as there can be possible data loss.

Hence, we get an error.
**Q.** Ask students into how to fix this?
**A.** Explicit typecasting to float.


---

# Question

Predict the output:
```
float x = 15.88f;
System.out.print(x);
```

# Choices
- [x] 15.88
- [ ] 15
- [ ] Error

---

# Explanation
Since, we explicitly typecasted to float, hence we will not get any error.

---

# Question

Predict the output:
```java
double y = 4.78;
float a = y;
System.out.println(a);
```

# Choices
- [ ] 4.78
- [x] Error
- [ ] Missed the lectures

---

# Explanation

Since, we are storing a double type into float, we have possible data loss. Hence, we get an error.


---
## Rules doing Basic Operations


## Rule 1 
When we do operation between a decimal and a non-decimal number, the output is always decimal.

* int op double --> double
* long op float --> float

**Note:** Run each of the following example codes in the compiler, and show the output to students.

## Example 1

### Incorrect Code
Don't let the students know that the code is incorrect. Ask them if it's correct and if not, how is it violating the Rule 1.

```
class Scaler {
    public static void main(String[] args) {
        int x = 10;
        double y = 10.25;
        int z = x + y;
        System.out.println(z);
    }
}
```

### Output
```
error: incompatible types: possible lossy conversion from double to int
        int z = x + y;
                  ^
1 error
```

Explain why their is a possible lossy conversion if we store the sum in an integer.
A. (x + y) is of double type.

Ask students on how to remove the error?

### Correct Code
```
class Scaler {
    public static void main(String[] args) {
        int x = 10;
        double y = 10.25;
        double z = x + y;
        System.out.println(z);
    }
}
```

### Output
```
20.25
```

Q. Ask students on how to store the result into an integer i.e, we don't want to store into a double.

A. Typecasting

### Correct Code
```
class Scaler {
    public static void main(String[] args) {
        int x = 10;
        double y = 10.25;
        int z = (int)(x + y);
        System.out.println(z);
    }
}
```



## Rule 2 
When we do operation between two operands of same category, the result is of bigger type.

* int op long --> long
* float op double --> double
* int op int --> int
* long op long --> long

**Note:** Run each of the following example codes in the compiler, and show the output to students.

## Example 1

### Incorrect Code
Don't let the students know that the code is incorrect. Ask them if it's correct and if not, how is it violating the Rule 2.

```
class Scaler {
    public static void main(String[] args) {
        int x = 20;
        long y = 150L;
        int z = x + y;
        System.out.println(z);
    }
}
```

### Output
```
/tmp/thqSRPUchr/Scaler.java:6: error: incompatible types: possible lossy conversion from long to int
int z = x + y;
^
1 error
```

Explain why their is a possible lossy conversion if we store the sum in an integer.
A. (x + y) is of long type.

Ask students on how to remove the error?

### Correct Code

```
class Scaler {
    public static void main(String[] args) {
        int x = 20;
        long y = 150L;
        long z = x + y;
        System.out.println(z);
    }
}
```

### Output
```
170
```

---
## Integer Overflow


**Note:** For better clarity of quizzes, please run the codes in the compiler as well.
Explain the integer overflow concept after giving the following quiz.


---


# Question

Predict the output:
```
int a = 100000;
int b = 400000;
int c = a * b;
System.out.print(c);
```

# Choices
- [ ] 40000000000
- [x] Some random Value
- [ ] Error


---
## CPU and its components


Before explaining the quiz's answer, we need to understand some more information.

**Q.** Where are these variables stored and where are these operations carried out?

We have two major components:
* Central Processing Unit (CPU)
    * ALU - Arithmetic Logic Unit
    * Control Unit
    * Registers
* Random Access Memory (RAM)

Look at the following diagram.
<img src ="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/048/460/original/upload_d26c363818f0ecae906193eac45751b9.png?1694708166"
     width = "600" height = "300">

Explain the use of the two components using the code for the quiz.

int a = 100000;
int b = 400000;
Populate the RAM with these two variables.
int c = a * b;
We want to store c into RAM. But we need to compute a * b first.

**Q.** Where will the computation happen?
**A.** ALU 
Values will be transferred to CPU's registers via buses, and then computation will be performed. The values are then written back to c's location in RAM.

The result would look something like this:
<img src ="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/048/461/original/upload_84a6994f462551877ec0827f0a75b961.png?1694708288"
     width = "700" height = "300">


If the inputs are integers, the ALU will assume that the output is also integer, which cannot be stored. 
**Note:** The compiler has no control over this.

So, the output will be some random value.

Now, formally define what is **Integer Overflow**?
* When we attempt to store a value that cannot be represented correctly by a data type, an Integer Overflow. 
* Integer Overflow occurs when the value is more than the maximum representable value



---


# Question

Predict the output:
```
int a = 100000;
int b = 400000;
long c = a * b;
System.out.print(c);
```

# Choices
- [ ] 40000000000
- [ ] 2147483647
- [x] Some random Value
- [ ] Error: product of integers can't be stored in long

# Explanation

Explain why this is the correct answer. If we store an integer in a long, we don't have any issues. So, according to the compiler, there's nothing wrong.

Explain it in the following way:


<img src ="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/048/462/original/upload_6ee7d0a207336c303f89d6aab64cbaaa.png?1694708350"
     width = "700" height = "250">


---


# Question

Predict the output:
```
long a = 100000;
long b = 400000;
int c = a * b;
System.out.print(c);
```

# Choices
- [ ] 40000000000
- [ ] Some random Value
- [x] Error

---


# Explanation
Explain why we are getting error in this case.
long * long --> long
Q. Can we store long into an integer? 
A. No, we can't. So, there is a possible lossy conversion.

**Reminder:** Remind the students to focus on the two rules, and all the questions would be easy.


---


# Question
Predict the output:
```
long a = 100000;
int b = 400000;
long c = a * b;
System.out.print(c);
```

# Choices
- [x] 40000000000
- [ ] Compilation Error
- [ ] Some random Value

---

# Explanation
long * int --> long
Q. Can we store long into a long type? 
A. Yes.

Explain this again in RAM and ALU in the following way:
<img src ="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/048/463/original/upload_7581c0b9de5fd1dad5e7fc79cea74dd8.png?1694708442"
     width = "700" height = "250">


---


# Question

Predict the output:
```
int a = 100000;
int b = 400000;
long c = (long)(a * b);
System.out.println(c);
```

# Choices
- [ ] 40000000000
- [ ] Compilation Error
- [x] Some random Value

---


# Explanation

int * int --> int
Q. Ask if we are typecasting individual variables or (a * b)?
A. We are typecasting (a * b) which is a random value to long.

Explain this again in RAM and ALU in the following way:
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/048/464/original/upload_aa2768e0525d6a8622f5133220bdcee4.png?1694708474" width = "700" height = "300">

Let the students know that this is not the correct way to multiply two integers.


---


# Question
What will be the output?
```
int a = 100000;
int b = 400000;
long c = (long)a * b;
System.out.println(c);
```

# Choices
- [x] 40000000000
- [ ] Compilation Error
- [ ] Some random Value

---


# Explanation

Typecast the value of a to long, and then multiply it with the integer b. 
Q. What will be the output of the multiplication of a long and an integer?
A. According to Rule 2, it will be long.

We can store a long into a long variable.
Explain this again in RAM and ALU in the following way:
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/048/465/original/upload_ff5e95b19bb73ea5f469d0c89ba91411.png?1694708553" height = "250" width = "600">


**Clarification:**

Some students get confused between the following 2 things:
* long c = (long) (a * b)
* long c = (long)a * b

Explain that in the 1st case, we are typecasting the product of two integers to a long, and in the 2nd case, we are first typecasting a into long, and then multiplying it with an integer.

---

In this section, we will study different types of operators namely:
* Arithmetic Operators
* Relational Operators
* Logical Operators
* Unary Operators
* Assignment Operators

---


**Q.** What are Logical Operators?
**A.** Logical operators can be defined as a type of operators that help us to combine multiple conditional statements. There are three types of logical operators: **AND (&&), OR (||) and Logical NOT (!) operators**.

To better understand AND(&&) operator, give the students the following analogy.

1. Driver's License
    * age >= 18
    * Know how to drive

In which of the following 4 scenarios the person should get their driver's license.



$\begin{array}{|c:c:c:c:c:c|}
  \hline
age >= 18 & Know\ how\ to\ drive & Driver's\ License\ received \\ \hline 
True & True  & True  \\ \hline
True & False & False \\ \hline
False & True  & False  \\ \hline
False & False & False \\ \hline
\end{array}$


So, we get the drivers's license when both the conditions are true.
AND [&&] -> Both conditions need to be true to get true as answer.

To better understand Logical OR (||) operator, give the students the following analogy.

2. Eligibility Criterion for Exam
    * Should have a diploma
    * Should have a degree

If they have either diploma or degree, they will be allowed to sit in the exam.

In which of the following 4 scenarios the person should be allowed to sit in the exam.



$\begin{array}{|c:c:c:c:c:c|}
  \hline
Have\ a\ diploma? & Have\ a\ degree? &Allowed\ to\ sit\ in\ exam      \\ \hline 
True & True  & True  \\ \hline
True & False & True \\ \hline
False & True  & True  \\ \hline
False & False & False \\ \hline
\end{array}$





OR [||] -> Even if one of the conditions is true, we get true as an answer.

### Important Observation of AND and OR Operator

* In case of AND, if the 1st condition is false, does the 2nd value have any effect? No, so the compiler would skip the 2nd check if the 1st condition is false.
* Similarly, if the 1st condition is true, does the 2nd value have any effect? No, so the compiler would skip the 2nd check if the 1st condition is true.


To better understand Logical Not (!) operator, let us look into following analogy.

3. To purchase milk, it shouldn't be raining outside. How to check for this condition?

If it's not raining outside, purchase milk.



$\begin{array}{|c:c:c:c:c:c|}
  \hline
Raining\ outside &   Can\ purchase\ Milk?     \\ \hline 
True  & False  \\ \hline
False & True \\ \hline
\end{array}$


Meaning, whatever is the case, just invert it.

### Examples

Discuss the following examples related to both arithmetic and logical operators.
1. Given two scores, check if they made a 50 partnership i.e, their combined score is 50 or not.
    * a = 15, b = 30 -> False
    * a = 25, b = 25 -> True
    * a = 10, b = 60 -> False
How to write the code for it in java?
```
a + b == 50
```

Q. What type of operator are we using here?
A. Relational Operator

2. Read 2 scores, check if both of them passes. The passing score is 35.
    * a = 35, b = 40 -> True
    * a = 34, b = 40 -> False
    * a = 50, b = 14 -> False

Q. How to check if a score is passed?
A. Use the >= operator.

Q. How to check if both the scores are passed?
A. Use the AND (&&) operator.

How to write the code for it in java?
```
a >= 35 && b >= 35
```

3. Read 2 scores and check if atleast one of them passed. The passing score is 35.

Ask students to do it themselves.
**Answer:** 
```
a >= 35 || b >= 35
```

**Note:** If students ask about the Logical NOT (!) operator, let them know that this will be discussed in unary operators section.

---


# Assignment Operators

It is used to assign value. 
They are : =, +=, -=, * =, /= etc.

```java 
int a = 10;
a = a+5; 
System.out.println(a);
```
>Explanation: This will increase the value of a by 5.

Same thing can be done using "+=".
```java 
int b = 10;
b += 5; // increment the value of b by 5
System.out.println(b);
```

```java 
int c = 20;
c -= 4; // decrement the value of c by 4
System.out.println(b);
```
Similarly, /= and * = works



---


Q. What are unary operators?
A. Unary operators work on a single operand only.

Give them a little bit idea of the following:
* What are Pre operators -> ++a, --a
* What are Post operators -> a++, a--

Run the following codes on IDE:
```
int a = 10;
a ++ ;
System.out.println(a);
```

```
int b = 10;
++ b;
System.out.println(b);
```

Both the codes give 11 as output.
Ask the students what is happening here, and why are we getting the same result.

Now, to show the difference, use the following codes.

```
int a = 10;
System.out.println(a ++ );
```

```
int b = 10;
System.out.println( ++ b);
```

The first code will give 10 as output, while the 2nd code gives 11 as output.
To explain the reason for this behaviour, show them the following table and ask them to focus on the first 4 rows.


$\begin{array}{|c:c:c:c:c:c|}
  \hline
Operator &   Name     \\ \hline 
a++  & Post-Increment\ Operator  \\ \hline
++a & Pre-Increment\ Operator \\ \hline
a-- & Post-Decrement\ Operator \\ \hline
--a & Pre-Decrement\ Operator \\ \hline
! & Logical\ Not\ Operator \\ \hline
\end{array}$








Coming back to the original question,

**Post-Increment**
```
int a = 10;
System.out.println(a ++ );
```

The last line is broken down into the following two lines.
```
System.out.println(a);
a ++ ;
```

**Pre-Increment**
```
int a = 10;
System.out.println(++ a);
```

The last line is broken down into the following two lines.
```
++a;
System.out.println(a);
```

Now, ask students if they can figure out the reason why the 1st code is printing 10, while the 2nd code is printing 11.


Mention that similar is the case with pre-decrement and post-decrement operators.

# Examples

## Example 1
```
int a = 10;
int b = 20;
int c = a ++ + b ++ ;
System.out.println(a + b + c);
```

Ask the following questions along with explanation, wherever necessary.
**Q.** What is the value of c?
**A.** 30

**Q.** What is the current value of a after 3rd line?
**A.** 11

**Q.** What is the current value of b after 3rd line?
**A.** 21

**Q.** What will be the output?
**A.** 62


## Example 2
```
int a = 10;
int b = a ++ + a ++ ;
System.out.println(a);
System.out.println(b);
```

**Output:**
```
12
21
```

Explanation: First we will solve left "a++", that will give b = 10 + a++, and now a will be 11.
Then again, we solve 2nd "a++", b = 10 + 11, and now a will be 12 after this. 
So, finally a = 12, b = 21.

Q. Suppose, we add the following statement in the above code, what would be the value of c?

```
int c = b ++ ;
```

A. There are 2 things happening -> Assignment and Post-Increment.
But since its post-increment, we will use the value of b first, and then increment the value of b.
So, value of c = 21.

Q. What if we add the following statement instead?

```
int c = ++ b;
```
A. There are 2 things happening -> Assignment and Pre-Increment.
But since its pre-increment, we will increment the value of b and then use the value of b.
So, value of c = 22.


## Example 3
```
int a = 10;
int b = a-- ;
System.out.println(a);
System.out.println(b);
```

**Output:**
```plaintext
9
10
```

Explain the reason for the above output accordingly if the students understood or not.

