	# Refresher : Introduction to Java : If-Else

## If-Else

#### Example
Let's start with real world example of ordering coffee from a cafe :-

* The customer might ask the receptionist ***If* you have coffee then provide coffee.**
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/036/013/original/p50.png?1685876618)
* Or ***If* you have coffee then provide coffee, *else* provide tea**
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/036/015/original/p51.png?1685876698)

* In programming we have to tackle real world situations.
* **How can we tackle the situation described above in the example using programming ?**
* If we pay attention to questions asked in the example we find the following keywords ***If*** & ***Else***.
* We can code the above situations using if else conditions.


#### If-Else Syntax
```cpp
if(is coffee available ? ){
 //   serve coffee
}
else{
 // serve tea
}
```
 
* **Is coffee available ?** is the **Condition**.
* **The condition is statement which can have only true/false as answers** or we say it's of **boolean** type



---
## Question 1


### Question
Given an integer age as input, print whether the person is eligible to vote or not ? 
> A person is eleigible if the person's age >= 18

#### Testcase 1

```plaintext
Input :
20
```
#### Solution 1

`Output : Eligible`
#### Testcase 2

```plaintext
Input :
14
```
#### Solution 2
`Output : Not Eligible`

#### Approach 
* Using conditional statements we check:
  * If age is >= 18 print Eligible.
  * Else print Not Eligible
#### Pseudeocode
```cpp
public static void main() {

    if (age >= 18) {
        System.out.print("Eligible");
    } else {
        System.out.print("Not Eligible");
    }
}
```

---
## Question 2

### Question
Given two integers A and B as input, print the larger
> A will not be equal to B
#### Testcase 1

```plaintext
Input :
A = 4, B = 6
```
#### Solution 1
`Output : 6 is bigger`

#### Testcase 2

```plaintext
Input :
A = 9, B = 6
```
#### Solution 2
`Output : 9 is bigger`

#### Approach

* Using conditional statements we check:
  * If A > B print **A is bigger**.
  * Else print **B is bigger**.

#### Pseudeocode
```java
public static void main() {

    scn = new Scanner(System.in);

    int A = scn.nextInt();
    int B = scn.nextInt();

    if (A > B) {
        System.out.print(A + "is bigger");
    } else {
        System.out.print(B + "is bigger");
    }
}
```
---
## Question 2 part 2


### Question
Given two integers A and B as input, print the large

#### Testcase 1

```plaintext
Input :
A = 4, B = 6
```
#### Solution 1
`Output : 6 is bigger`
#### Testcase 2

```plaintext
Input :
A = 9, B = 6
```
#### Solution 2
`Output : 9 is bigger`

#### Testcase 2

```plaintext
Input :
A = 6, B = 6
```
#### Solution 2
`Output : Both are equal`

#### Approach 
* Using conditional statements we check:
  * If A > B print **A is bigger**.
  * Else if A < B print **B is bigger**.
  * Else  print **Both are equal**.

#### Pseudeocode
```java
public static void main() {

    scn = new Scanner(System.in);

    int A = scn.nextInt();
    int B = scn.nextInt();

    if (A > B) {
        System.out.print(A + "is bigger");
    } else if (B > A) {
        System.out.print(B + "is bigger");
    } else {
        System.out.print("Both are equal");
    }
}

```

---
## Question 3


### Question
Given temperature of patient in farenheit as input,
print whether the temperature is low, normal, high
>normal from 98.2 till 98.8

#### Testcase 1

```plaintext
Input :
98.1
```
#### Solution 1
`Output : Low`
#### Testcase 2

```plaintext
Input :
98.5
```
#### Solution 2
`Output : normal`

#### Testcase 3

```plaintext
Input :
99.3
```
#### Solution 3
`Output : high`

---


### Question
Which data type should be used to store temperature of a patient ?


**Choices**

- [x] Double
- [ ] Int
- [ ] String
- [ ] long

**Solution**

```plaintext
Double is used to store the numbers with decimals.
```

#### Approach 
* Using conditional statements we check:
  * If temperature is < 98.2 print low.
  * Else if temperature > 98.5 print high**.
  * Else print normal

#### Pseudeocode
```java
public static void main() {
    scn = new Scanner(System.in);

    double temperature = scn.nextDouble();

    if (temperature < 98.2) {
        System.out.print("low");
    } else if (temperature > 98.8) {
        System.out.print("high");
    } else {
        System.out.print("normal");
    }
}  
```

---
## Operators


### Division
*  Division is denoted by **/**  operator.
* Provided below is the output datatype based on dividend and divisor datatype.

  * int / int ---> int
  * float / int ---> float
  * int / float ---> float
  * float / float ---> float
  * long / int ---> long 
  * double / float ---> double
  * int / long are replacable
  * float / double are replacable

* To convert a number to float put a f in the ending of it.
* To convert a number to double we can write it with .0 in the end.

#### Example
```cpp
System.out.println(9 / 3) ; // int / int ---> int output would be 3
System.out.println(11 / 3); // int / int ---> int output would be 3
System.out.println(11f / 3) ; // float / int ---> float output would be 3.6666 
``` 
### Multiplication

* Multiplication is denoted by <b>*</b> operator.
* Provided below is the output datatype based on  multiplicand and multiplier datatype.
  * int * int ---> int
  * int * long ---> long
  * long * int ---> long
  * long * long --->long
  * int / float are replacable
  * long / double are replacable

#### Example 1
```java
int x = 100000;
int y = 100000;
int z = x * y
System.out.println(z); // prints garbage value
```
* The above code gives garbage value as output but **why ?**
* We can see that when we multiply x and y i.e 100000 * 100000 then output would be 10<sup>10</sup>. 
* Since the range of integer datatype is roughly 10<sup>9</sup> we would get garbage value due to overflow as we store it in z (int). 

#### Example 2
```java
int x = 100000;
int y = 100000;
long z = x * y
System.out.println(z); // prints garbage value
```
* The above code gives garbage value as output but **why ?** **even though we have changed the datatype of z from int ---> long.**
* We have changed the datatype of z but the according to rules above :-
  * int * int ---> int 
* Therefore we need to explicitly change datatype of the multiplicand or the multiplier to long so that :-
  * long * int ---> long
* Therefore :-
```java
int x = 100000;
int y = 100000;
long z = (long)x * y;
System.out.println(z); // prints 10000000000
```

---

### Question
What will be the output according to Java :
```java
int a = 100000;
int b = 400000;
long c = (long)(a * b);
System.out.println(c);
```

**Choices**

- [x] Some random number
- [ ] 40000000000
- [ ] Compilation error
- [ ] No Output

**Solution**

* First we are doing a * b i.e int * int therefore the output will be int. 
* Overflow would have already occured before typecasting to long.
* Hence the random value is printed.  

---
### Operators Continued


### Modulo
* Modulo is denoted by **%**  operator.
* Gives us the remainder when a is divided by b i.e. a % b = remainder when a is divided by b.

#### Examples 
* 7 % 3  ---> 1
* 8 % 5  ---> 3
* 10 % 1 ---> 0
* 5 % 12 ---> ?
  * Answer is 5 by **why ?**.
  * Because 5 % 12 = 12 * 0 + 5 where 5 is dividend, 12 is divisor , 0 is  quotient & 5 is remainder.

---


### Question
What is the result? 
System.out.print(17 % 4);

**Choices**

- [x] 1
- [ ] 4
- [ ] 16
- [ ] 5

**Solution**

```plaintext
dividend = divisor* quotient + remainder 
=> 17 = 4 * 4 + 1 
```

---

### Question
What will be the result of a % b, when b perfectly divides a with no remainder ?

**Choices**

- [x] 0
- [ ] b -1
- [ ] b
- [ ] a

**Solution**
```plaintext
dividend = divisor * quotient + remainder 
if dividend is divided perfectly by divisor then the remainder is 0
```

---
## Question 4


### Question
Given an integer as input, print whether it is even or Odd

#### Testcase 1

```plaintext
Input :
3
```

#### Solution 1
`Output : odd`

#### Testcase 2

```plaintext
Input :
6
```
#### Solution 2
`Output : even`

---


### Question

If a % 2 == 0, what can we say about a ?

**Choices**

- [x] even
- [ ] odd
- [ ] prime
- [ ] remainder

---
### Approach 
* Using conditional statements we check:
  * If A % 2 == 0 print **even**.
  * Else print **odd**.

#### Pseudeocode
```cpp
public static void main() {
    scn = new Scanner(System.in);

    int A = scn.nextInt();
    int B = scn.nextInt();

    if (A % 2 == 0) {
        System.out.print("even");
    } else {
        System.out.print("odd");
    }
}
```


---
## Question 5


### Question
Q5 : Given an integer as input, print its last digit

#### Testcase 1

```plaintext
Input :
73
```
#### Solution 1
`Output : 3`
#### Testcase 2

```plaintext
Input :
651
```
#### Solution 2
`Output : 1`

#### Approach 

* Print A % 10

#### Pseudeocode
```cpp
scn = new Scanner(System.in);

int A = scn.nextInt();
    
System.out.print(A % 10);
```


---
### Operators Continued


### Relational Operators
* **A > B** ---> Checks weather A is greater than B.
* **A < B** ---> Checks weather A is less than B.
* **A >= B** ---> Checks weather A is greater than or equalt to B.
* **A <= B** ---> Checks weather A is less than or equal to B.
* **A == B** ---> Checks weather A is equals B.
* **A != B** ---> Checks weather A is not equal to B.

### Logical Operators
* AND operator is denoted  by  **&&**
* Truth table is provided below.

|  A  |  B  | A && B |
|:---:|:---:|:------:|
|  T  |  F  |   F    |
|  F  |  T  |   F    |
|  F  |  F  |   F    |
|  T  |  T  |   T    |

* OR operator is denoted  by  **||**
* Truth table is provided below.

|  A  |  B  | A && B |
|:---:|:---:|:------:|
|  T  |  F  |   T    |
|  F  |  T  |   T    |
|  F  |  F  |   F    |
|  T  |  T  |   T    |



---
## Question 6


### Question

Q6 : Given units of electricity consumed as an integer input A, print the bill amount. Provided below is the range of electricity consumed and rate at which it is charged:-
[1-50] ---> ₹1
[51-100] ---> ₹2
[101 and beyond] ---> ₹4

#### Testcase 1

```plaintext
Input :
20
```
#### Solution 1
`Output : 20 * 1 = 20`

#### Testcase 2

```plaintext
Input :
80
```
#### Solution 2
`Output : 50 * 1 + 30 * 2 = 110`

#### Testcase 3

```plaintext
Input :
120
```
#### Solution 3
`Output : 50 * 1 + 50 * 2 + 20 * 4= 230`

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


#### Pseudeocode
```java
public static void main() {

    scn = new Scanner(System.in);
    int A = scn.nextInt();

    if (A >= 1 && A <= 50) {
        System.out.print(A * 1);
    } else if (A >= 51 && A <= 100) {
        System.out.print(50 + (A - 50) * 2);
    } else {
        System.out.print(50 + (50 * 2) + ((A - 100) * 4));
    }
}    
```

---
### Question 7

### Question
Q7 : Given an integer A as input
* If it is a multiple of 3, print Fizz
* If it is a multiple of 5, print Buzz
* If it is a multiple of 3 and 5, print Fizz-Buzz

#### Testcase 1

```plaintext
Input :
5
```

#### Solution 1
`Output : Buzz`

#### Testcase 2

```plaintext
Input :
3
```

#### Solution 2
`Output : Fizz`

#### Testcase 3

```plaintext
Input :
30
```

#### Solution 3
`Output : Fizz-Buzz`

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


#### Approach 1
```java
public static void main() {

    scn = new Scanner(System.in);
    int A = scn.nextInt();

    if (A % 3 == 0) {
        System.out.print("Fizz");
    } else if (A % 5 == 0) {
        System.out.print("Buzz");
    } else if (A % 3 == 0 && A % 5 == 0) {
        System.out.print("Fizz-Buzz");
    }
} 
```
* When we test the above approach on A = 30, we get output as "Fizz" 
* But correct output would be "Fizz-Buzz", so **why the wrong answer ?**
* Since if-else work in a chained manner the condition A % 3 == 0 is checked first.
* Therefore "Fizz" is printed
* Correct approach would be to check condition ( A % 3  == 0 &&  A % 5 == 0 ) first.

#### Pseudeocode
```java
public static void main() {

    scn = new Scanner(System.in);
    int A = scn.nextInt();

    if (A % 3 == 0 && A % 5 == 0) {
        System.out.print("Fizz-Buzz");
    } else if (A % 5 == 0) {
        System.out.print("Buzz");
    } else if (A % 3 == 0) {
        System.out.print("Fizz");
    }
}   
```