# While Loop


---

## Agenda
- Intro of Loops
- Print numbers from 1 to 5
- Structure and Syntax of while loop
- Even numbers from 1 to n
- Print multiples of 4
- Print numbers from n to 1 
- Find last digit
- Remove last digit 


:::success
There are a lot of quizzes in this session, please take some time to think about the solution on your own before reading further.....
:::

---

**Ques:** Print natural numbers from 1 to 5.

**Method 1:**
```
System.out.println(1);
System.out.println(2);
System.out.println(3);
System.out.println(4);
System.out.println(5);
```

**Method 2:**
```
int i = 1;
System.out.println(i);
i ++ ;
System.out.println(i);
i ++ ;
System.out.println(i);
i ++ ;
System.out.println(i);
i ++ ;
System.out.println(i);
```

**Comparison of Method 1 and Method 2:**
Both **Method 1** and **Method 2** output the numbers 1, 2, 3, 4, and 5 in order. The only difference between the two methods is the way the code is written.
* Issues In **Method 1** : Since we are updating the values as well along with copy pasting the lines.
Possibility of Human Error
* Issues In **Method 2** : We are repeating the same lines again and again.

## Loops 
Repeat a task multiple times

- For Loop
- While Loop
- Do while Loop

**Method 3:**
```
int i = 1;
while(i <= 5){
    SOPln(i);
    i = i + 1;
}
```

|  i  | i<=5  | Output |   i + 1   |
|:---:|:-----:|:------:|:---------:|
|  1  | true  |   1    |     2     |
|  2  | true  |   2    |     3     |
|  3  | true  |   3    |     4     |
|  4  | true  |   4    |     5     |
|  5  | true  |   5    |     6     |
|  6  | false |        | **Break** |


---

## Structure of While loop

**Step 1:** Initialization of a loop variable.
**Step 2:** Write while with condition.
**Step 3:** Write the task you want to repeat.
**Step 4:** Updation of loop variable.

## Syntax of while loop

```
initialize
while(condition){
    // task to be repeated
    // updation
}
```

**Flow chart of while loop:**


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/265/original/Screenshot_2023-10-04_at_3.00.22_PM.png?1696411919" alt= “” width ="400" height="300">

---

# Question
What is the output of the following code?
```
int i = 5;
while(i <= 10){
    System.out.println(i);
    i = i * 2;
}
```

# Choices
- [x] 5<br>10
- [ ] 0
- [ ] Error




---

# Question
What is the output of the following code?
```
int i = 1;
while(i < 5){
    System.out.print(i + " ");
    i = i + 1;
}
```

# Choices
- [ ] 1 2 3 4 5
- [x] 1 2 3 4 
- [ ] 5 4 3 2 1



---


# Question
What is the output of the following code?
```
int i = 0;
while(i <= 10){
    System.out.print(i + " ");
    i++;
}
```

# Choices
- [x] 0 1 2 3 4 5 6 7 8 9 10
- [ ] 1 2 3 4 5 6 7 8 9 10
- [ ] Error




---

# Question
What is the output of the following code?

```
int i = 1;
while(i >= 10){
    System.out.print(i + " ");
    i = i + 1;
}
```

# Choices
- [ ] Error
- [ ] 1 2 3 4 5 6 7 8 9 10
- [x] Nothing will get printed
- [ ] 10 9 8 7 6 5 4 3 2 1


---


# Question
What is the output of the following code?

```
int i = 1;
while(i <= 10){
    System.out.print(i + " ");
}
```

# Choices
- [ ] 1 2 3 4 5 6 7 8 9 10
- [x] 1 1 1 1 1 1 ... Infinite times



---


# Question
What is the output of the following code?

```
int i = 0;
while(i <= 10){
    System.out.print(i + " ");
    i = i * 2;
}
```

# Choices
- [ ] 5 10
- [ ] 0
- [x] Infinite loop
- [ ] 0 2 4



---


# Question
What is the output of the following code?

```
int i = 1;
while(i <= 5){
    System.out.print(i + " ");
    i = i - 1;
}
```

# Choices
- [ ] 1 2 3 4 5
- [ ] 5 4 3 2 1
- [x] Infinite loop
- [ ] Inki pinky ponky


---


# Question
How many times `Hi` will be printed in the output?

```
int i = 0;
while(i <= 5){
    System.out.println("Hi");
    i = i + 1;
}
```

# Choices
- [ ] 5
- [x] 6
- [ ] 4
- [ ] Infinite times

---


# Question
How many times `Inki Pinki Ponki` will be printed in the output?

```
int i = 1;
while(i <= n){
    System.out.println("Inki Pinki Ponki");
    i = i + 1;
}
```

# Choices
- [x] n
- [ ] (n+1)
- [ ] Only once
- [ ] Too many times



---


**Ques:** Print even numbers from 1 to n

```
int n = scn.nextInt();
int i = 1;
while(i <= n){
    if(i % 2 == 0){
        System.out.println(i);
    }
    i = i + 1;
}
```

> Explain dry run of the above code for more clarity
> Example of how to dry run the above code:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/266/original/Screenshot_2023-10-04_at_3.26.15_PM.png?1696413386" alt= “” width ="500" height="300">



Another way to implement the above task is as follows:

```
int i = 2;
while(i <= n){
    System.out.println(i);
    i = i + 2;
}
```

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/267/original/Screenshot_2023-10-04_at_3.27.52_PM.png?1696413482
" alt= “” width ="500" height="300">


Note that the number of iterations are reduced from 6 to 3.

Let us take some test cases to test our code.
Consider `n = 17`
The output should be `2 4 6 8 10 12 14 16`
> **Instruction for Instructor:** Run the code on editor to verify the same and show to the students.


In the range 1 - 17, the total number of even numbers are 8.

In the range 1 - 10, the total number of even numbers are 5.

> Based on the above observation, ask the following question to the students?
**How to calculate the total number of multiples of x between 1 and n?**
**Ans:** `n/x`

Total number of multiples of 2 from 1 to 40 is = ![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/048/485/original/Screenshot_2023-09-14_232954.png?1694714463)

Total number of multiples of 2 from 1 to 51 is = ![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/048/486/original/Screenshot_2023-09-14_233032.png?1694714627)

---





# Question
What will be the total number of iterations in the following code?

```
int i = 1;
while(i <= 20){
    System.out.println(i);
    i = i + 1;
}
```

# Choices
- [x] 20
- [ ] 10
- [ ] 15
- [ ] No clue


---


# Question
What will be the total number of iterations in the following code?

```
int i = 2;
while(i <= n){
    System.out.println(i);
    i = i + 2;
}
```

# Choices
- [ ] n
- [x] n/2
- [ ] n+1
- [ ] Infinite


---


# Question
What will be the total number of iterations in the following code?

```
int i = 3;
while(i <= n){
    System.out.println(i);
    i = i + 3;
}
```

# Choices
- [x] n / 3
- [ ] 3 * n
- [ ] n+3
- [ ] n

---


# Question
What are all the multiples of 4 between 1 to 18 ?

# Choices
- [ ] 4 8 12 16 20 24
- [ ] 4 6 8 10 12 14
- [x] 4 8 12 16
- [ ] 1 4 8 12 16


---

**Ques:** Print multiples of 4 till n.

**Approach 1:**
In this approach, the code takes an input from the user and stores it in the variable n. Then, it uses a `while` loop to iterate from 1 to n. During each iteration, if the value of i is divisible by 4, it prints the value of i using `System.out.println()`.

```
int n = scn.nextInt();
int i = 1;
while(i <= n){
    if(i % 4 == 0){
        System.out.println(i);
    }
    i++;
}
```

If n is taken as 10, the output of the above code would be: `4 8`


**Approach 2:** **Number of instructions executed are reduced**
In this approach, the code initializes the variable $i$ to $4$ and then uses a `while` loop to print the value of $i$ in each iteration. The value of $i$ is incremented by $4$ during each iteration until it becomes greater than $n$.

**Code:**
```
int i = 4;
while(i <= n){
    System.out.println(i);
    i = i + 4;
}
```

> Explain using dry run as follows:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/733/original/upload_908acb233760adf812b6c04b41b24ff1.png?1693736372" alt= “” width ="500" height="200">


> Contrast both the dry runs and stress on the fact that the number of iterations are reduced from 10 to 2.


---


# Question
What are the total number of iterations of the following code?
```
int i = 4;
while(i <= n){
    System.out.println(i);
    i = i + 4;
}
```

# Choices
- [ ] n
- [ ] n + 4
- [x] n / 4
- [ ] Easy Peesy

---


**Ques:** Print numbers from n to 1.

```
int n = 5;
while(i >= 1){
    System.out.println(i);
    i--;
}
```

> Explain using dry run as follows:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/734/original/upload_f0f8b93644bb7df8f81fe127ed7302cd.png?1693736416" alt= “” width ="600" height="300">



---


# Question
Predict the output:

```
int i = 10;
while(i >= 0){
   System.out.print(i + " ");
   i = i - 2;
}
```

# Choices
- [ ] 10 9 8 7 6 5 4 3 2 1 0
- [ ] 10 8 6 4 2
- [x] 10 8 6 4 2 0
- [ ] 0 2 4 6 8 10

---

**Dry Run:**
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/735/original/upload_41d0c4493836a10e847050314b6fa548.png?1693736449" alt= “” width ="450" height="400">


---


## Modulus operator (%)
It is used to find the remainder. When we take modulus by 10, we get the last digit of that number.


---


# Question
Predict the output of the following code:

```
int x = 7185;
System.out.println(x % 10);
```

# Choices
- [ ] 8
- [ ] 578
- [ ] 718.5
- [x] 5

---


# Question
Predict the output of the following code:

```
int x = 4578;
System.out.println(x % 10);
```

# Choices
- [x] 8
- [ ] 578
- [ ] 78
- [ ] None


---


# Question
Predict the output of the following code:

```
int x = 99576;
System.out.println(x % 10);
```

# Choices
- [x] 6
- [ ] 576
- [ ] 995
- [ ] None


---


# Question
Predict the output of the following code:

```
int x = 7248;
System.out.println(x / 10);
```

# Choices
- [ ] 724.8
- [ ] 725
- [x] 724
- [ ] Inky pinky ponky

---


**Ques:** Given a positive integer, write code to find it's last digit.

**Code:**
```
int n = scn.nextInt();
System.out.println(n % 10);
```

---


**Ques:** Given a positive integer, write code to remove it's last digit.

**Code:**
```
int n = scn.nextInt();
n = n / 10;
System.out.println(n);
```
---

