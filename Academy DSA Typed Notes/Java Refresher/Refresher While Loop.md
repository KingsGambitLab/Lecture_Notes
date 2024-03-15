# Refresher : While Loop
## While Loop


### Example
* Say we need to print "Hello" 5 times.
* We can do it as :-
```cpp
System.out.print("Hello");
System.out.print("Hello");
System.out.print("Hello");
System.out.print("Hello");
System.out.print("Hello");    
```
* But what if we have to do the same 100 times or 1000 times ?
* It would be not feasible.
* Solution to above is to use **while loop** :-
```cpp
int count = 0 ;
    
while(count < 5)
{
  System.out.print("Hello");
  count ++ ;   
}
```

#### Syntax
```cpp
intialization

while(Condition)
{
    // loop work
    updation
}
```


---
### Question

```
int i = 1;
i = i + 1;
```

What is the new value of i ?

**Choices**

- [x] 2
- [ ] 1
- [ ] 0
- [ ] 3

**Solution**

```plaintext
i = 1
i = i + 1 => i = 1 + 1 = 2
```

---
## Question 1


### Question
Given an integer N as input. Print from 1 to N ?

#### Testcase 1

```plaintext
Input :
N = 4
```

#### Solution 1
`Output : 1 2 3 4`

#### Approach 
* Intialize the count with 1.
* While loop will execute till count <= N.
* Print count.
* In loop update the count by increamenting 1.

#### Code
```cpp
public static void main(){

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    int count = 1;
    while (count <= N) {
        System.out.printLn(count + " ");
        count++ ;    
    }
}
```

---
## Question 2

### Question
Given an integer N as input. Print from N to 1 ?

#### Testcase 1

```plaintext
Input :
N = 4
```
#### Solution 1
`Output : 4 3 2 1`

#### Approach 
* Intialize the count with N.
* While loop will execute till count >= 1.
* Print count.
* In loop update the count by decreamenting it by 1.

#### Code
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    int count = N;
    while (count >= 1) {
        System.out.print(count + " ");
        count--;
    }
}
```

---
## Question 3

### Question
Given an integer N as input. Print odd values from 1 to N ?
#### Testcase 1

```plaintext
Input : N = 8
```
#### Solution 1
```plaintext
Output : 1 3 5 7
```
#### Approach 
* Since odd numbers start from 1, intialize the count with 1.
* While loop will execute till count <= N.
* print count.
* In loop update the count by increamenting it by 2 since adding 2 to previous odd will yeild next odd number.

#### Code
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    int count = 1;
    while (count <= N) {
        System.out.print(count + " ");
        count += 2;
    }
}
```



---
## Question 4


### Question
Given an integer N as input. Print odd values from 1 to N ?


#### Testcase 1

```plaintext
Input :
N = 8
```
#### Solution 1
`Output : 1 3 5 7`

#### Approach 
* Since odd numbers start from 1, intialize the count with 1.
* While loop will execute till count <= N.
* print count.
* In loop update the count by increamenting it by 2 since adding 2 to previous odd will yeild next odd number.

#### Code
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    int count = 1;
    while (count <= N) {
        System.out.print(count + " ");
        count += 2;
    }
}
```

---
## Question 5


### Question
Given an integer N as input, print multiples Of 4 till N ?

#### Testcase 1
```plaintext
Input : N = 18
```

#### Solution 1
```plaintext
Output : 4 8 12 16
```

#### Approach 
* Since multiple of 4 numbers start from 4, intialize the count with 4.
* While loop will execute till count <= N.
* Print count.
* In loop update the count by increamenting it by 4 since adding 4 to previous multiple will yeild the next multiple.

#### Code
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    int count = 4;
    while (count <= N) {
        System.out.print(count + " ");
        count += 4;
    }
}
```

---


### Question
```cpp
int i = 1;
while (i <= 10) {
    i = i * i;
    System.out.print(i + " ");
    i++;
}
```
What will be the output ?

**Choices**

- [x] 1 4 25
- [ ] Error
- [ ] Infinite loop
- [ ] 100 12 34

**Solution**

```plaintext
|i = 1  | i <= 10 | i * i = 1 | i++ = 2 |---> iteration 1
|i = 2  | i <= 10 | i * i = 4 | i++ = 5 |---> iteration 2
|i = 5  | i <= 10 | i * i = 25 | i++ = 26 |---> iteration 3
```

---
### Question

```java
public static void main() {
    int i = 0;
    while (i <= 10) {
        System.out.print(i + " ");
        i = i * i;
    }
}
```

What will be the output ?

**Choices**

- [x] Loop will never end 
- [ ] 1 4 9 16 25 36 49 64 81 100
- [ ] 1 2 3 4
- [ ] 0 0 0 0

**Solution**

```plaintext
Since i would always be less than 10 hence infinite loop
```

---
## Question 6


### Question
Q5 : Given an integer N as input, print perfect squares till N ?
> Perfect square —> An integer whose square root is an integer

#### Testcase 1

```plaintext
Input : N = 30
```
#### Solution 1
```plaintext
Output : 1 4 9 16 25
```

#### Approach 
* Intialize count = 1
* While loop will execute till count * count <= N.
* Print count * count.
* In loop update the count by increamenting it by 1.

#### Code
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    int count = 1;
    while (count * count <= N) {
        System.out.print(count * count + " ");
        count += 1;
    }
}
```

---
## Question 7

### Question
Given an integer N as input, print it's digits ?

#### Testcase 1

```plaintext
Input : N = 6531
```
#### Solution 1
```plaintext
Output : 1 3 5 6
```
#### Observations 


|  N   | N % 10 |
|:----:|:----:|
| 6531 |  1   |
| 653  |  3   |
|  65  |  5   |
|  6   |  6   |

* We can see that answer to % 10 of numbers present in the table coincide with the answer.
* We need to find a way to arrive at these numbers while iterating.
* We can do this by dividing number in each iteration by 10.

|  N   | N/10 |
|:----:|:----:|
| 6531 | 653  |
| 653  |  65  |
|  65  |  6   |
|  6   |  0   |


#### Approach 
* Input N.
* While loop will execute till N > 0.
* Print N % 10.
* In loop update the N by dividing it by 10.

#### Code 
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    while (N > 0) {
        System.out.print(N + " ");
        N /= 10;
    }
}
```

### Edge Cases
**TestCase 1**
```plaintext
Input :-
N = 0
```
**Solution 1**
```plaintext
Output = 0
```
**Approach** to handle edge case -
* Input N.
* While loop will execute till N >= 0.
* Print N % 10.
* In loop update the N by dividing it by 10.

**Code 1**
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    while (N >= 0) {
        System.out.print(N + " ");
        N /= 10;
    }
}
```
* The above approach leads to **infinite loop**.
* We need to handle above case seperately in if else.


**TestCase 2**
```plaintext
Input :-
N = - 6351 (i.e N < 0)
```
**Solution 2**
```plaintext
Output : 1 3 5 6 
```

* Since answer of N < 0 would be same as that of N > 0.
* So we just multiple N with -1 in order to convert it to +ve number .

#### Code final
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    if (N == 0) {
        System.out.print(0);
    } else {

        if (N < 0) {
            N *= -1;
        }
        while (N > 0) {
            print(N + " ")
            N /= 10;
        }
    }
}
```

---
## Question 8


### Question
Given an integer N as input, print sum of it's digits ?
> N > 0

#### Testcase 1

```plaintext
Input : N = 6531
```
#### Solution 1
```plaintext
Output : 15
```

#### Approach 

* Input N & Intialize sum = 0
* While loop will execute till N > 0.
* Add N % 10 to sum.
* In loop update the N by dividing it by 10.

#### Pseudeocode 
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    int Sum = 0;
    while (N > 0) {
        Sum += (N % 10);
        N /= 10;
    }
    System.out.print(Sum);
}
```

---

### Question
Which of the following will add the digit `d` to the back of a number `r`

**Choices**

- [x] r * 10 + d 
- [ ] d * r
- [ ] d + r
- [ ] d * 10 + r

**Solution**

```plaintext
Let r = 13 & d = 4
We want to add d behind r i.e we need number 134
So r * 10 = 130
r * 10 + d => 130 + 4 = 134
```

---
## Question 9


### Question
Given an integer N as input, Reverse it ?
> N > 0

#### Testcase 1

```plaintext
Input :
N = 6531
```
#### Solution 1
`Output : 1356`

#### Approach 
* Input N & Intialize reverse = 0
* While loop will execute till N > 0.
* Set reverse = reverse * 10 + N % 10.
* In loop update the N by dividing it by 10.

#### Code 
```cpp
public static void main() {

    Scanner scn = new Scanner(System.in);
    int N = scn.nextInt();
    int reverse = 0;
    while (N > 0) {
        d = N % 10;
        reverse = reverse * 10 + d;
        N /= 10;
    }
    System.out.print(reverse);
}
```
