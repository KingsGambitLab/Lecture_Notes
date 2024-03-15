# Loops 2

---

> Quick revision

**Step 1:** Initialization of a loop variable.
**Step 2:** Write while with condition.
**Step 3:** Write the task you want to repeat.
**Step 4:** Updation of loop variable.

## Syntax of while loop

```
initialize
while(condition){ // loop stops when the condition fails
    // task to be repeated
    // updation
}
```

**Flow chart of while loop:**
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/748/original/beginner-iterations-loop-2-image-1.png?1693749426" height = "350" width = "350">


**Question:** 

How to find the last digit of a number N?

**Answer:** Use the modulus operator as `N%10`.

> Give an example

**Question:** How to delete the last digit of N?

**Answer:**
```
N = N / 10;
SOP(N);
```

---
title: Printing all digits
description: Print all the digits of that number from right to left
duration: 480
card_type: cue_card
---

**Ques:** Given a integer number, print all the digits of that number from right to left.

Example, if `n = 6397` the correct output should be `7 9 3 6`

> Give the students, an intuition to solve the problem as follows:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/746/original/upload_c997251ad272ffb9708ce7c8a5bf1411.png?1693748957" alt= “” width ="450" height="350">


:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

**Approach:**
* Find the last digit.
* Print the digit.
* Remove last digit.

**Code:**
```
int n = scn.nextInt();
while(n > 0){
    int digit = n % 10;
    SOPln(digit);
    n = n / 10;
}
```

> To figure out the condition in the while loop expression (i.e., `n > 0`), give the students an intuition as follows:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/747/original/upload_a7b3a344d33b1e78a66ba64c1ae9b4a0.png?1693748996" alt= “” width ="400" height="450">

**How to handle negative numbers?**
**Ans:** Convert negative numbers to positive numbers.

> Take an example of a negative number, dry run the code. Tell the students that the code exits from the while loop condition since `n < 0`. Then give the solution.

**The updated code is as follows:**
```
int n = scn.nextInt();
if(n < 0){
    n = n * -1;
}
while(n > 0){
    int digit = n % 10;
    SOPln(digit);
    n = n / 10;
}
```

**Next corner test case:** What if `n == 0`?
In this case, the output should be $0$, but according to the code this will print nothing. So we need to handle this case as well.

**The updated code is as follows:**
```
int n = scn.nextInt();
if(n < 0){
    n = n * -1;
    return;
}
else if(n == 0){
    SOPln(0);
    return;
}
while(n > 0){
    int digit = n % 10;
    SOPln(digit);
    n = n / 10;
}
```


**Dry Run:**

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/749/original/beginner-iterations-loop-2-image-2.png?1693749460" height = "450" width = "450">


---
title: Find sum of digits of a given number
description: Take examples to explain how to use while loops
duration: 900
card_type: cue_card
---

## Find Sum of Digits of A Given Number
**Question:** 

Find the sum of digits of a given number.

Give examples -> 1274, 1004, -512

```
1274 -> 1 + 2 + 7 + 4 = 14
1004 -> 1 + 0 + 0 + 4 = 5
-512 -> 5 + 1 + 2 = 8
```


Note: Negative sign (**-**) is not a digit.

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

**Approach:**
To discuss the approach take an example.

```
// Initialization
n = 2748
s = 0
```

|  n   | n > 0 | d = n % 10 | s = s + d | n = n / 10 |
|:----:|:-----:|:----------:|:---------:|:----------:|
| 2748 | true  |     8      |     8     |    274     |
| 274  | true  |     4      |    12     |     27     |
|  27  | true  |     7      |    19     |     2      |
|  2   | true  |     2      |    21     |     0      |
|  0   | false |     -      |     -     |     -      |

```
int n = scn.nextInt();

if (n < 0) {
    n = n * - 1;
}

int s = 0;
while (n > 0) {
    int d = n % 10;
    s = s + d;
    n = n / 10;
}

SOPln(s);
```

---
title: Add a given digit to the back of a given number N.
description: Take examples to explain how to use while loops
duration: 800
card_type: cue_card
---

### Example 1
**Question:**

Given a positive integer N and a single digit d, add d to the back of N.

**Example:**
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/751/original/beginner-iterations-loop-2-image-3.png?1693749757" height = "350" width = "500">

Formula to add d to the back of N:

```
n = n * 10 + d;
```

---
title: Find the reverse of a given number
description: Take examples to explain how to use while loops
duration: 1100
card_type: cue_card
---

### Example 2
**Question:**

Given a number N, store it's reverse in another variable and print it.

**Examples:**
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/752/original/beginner-iterations-loop-2-image-4.png?1693749809" height = "350" width = "220">

**Idea/Approach:**
Initialize a variable rev = 0 and one by one take the last digit of N and add it to rev as shown below.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/754/original/beginner-iterations-loop-2-image-5.png?1693749853" height = "350" width = "350">

**Steps:**
* Get last digit
* Add last digit to the back of rev
* Remove last digit
* Repeat the above three steps till the number is greater than zero

**Dry run:**
|  n   | n > 0 | d = n % 10 | rev = rev * 10 + d | n = n / 10 |
|:----:|:-----:|:----------:|:------------------:|:----------:|
| 1456 | true  |     6      |         6          |    145     |
| 145  | true  |     5      |         65         |     14     |
|  14  | true  |     4      |        654         |     1      |
|  1   | true  |     1      |        6541        |     0      |
|  0   | false |     -      |         -          |     -      |

```
int n = scn.nextInt();
int copy = n;

if (n < 0) {
    n = n * - 1;
}

int rev = 0;
while (n > 0) {
    int d = n % 10;
    rev = rev * 10 + d;
    n = n / 10;
}

if (copy < 0) {
    rev = rev * - 1;
}

SOPln(s);
```

> Dry run with n = 2400 and show that the output will be 42 and not 0042.

Tell them that if you want to print 0042, print the digits of n from right to left. It is not possible for an integer variable to store 0042.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/755/original/beginner-iterations-loop-2-image-6.png?1693750025" height = "350" width = "650">

> Show dry run with - 417 as n.

---
title: Check if a given number is palindrome or not
description: Take examples to explain how to use while loops
duration: 720
card_type: cue_card
---

### Example 3
**Question:** 

Given a number N, check if number if palindrome or not.
A number is said to a palindrome if it remains the same when its digits are reversed. Ex- 1221, 1551, 131, etc.

**Exercise for students:**
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/756/original/beginner-iterations-loop-2-image-7.png?1693750061" height = "400" width = "430">

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

**Approach:**
Find the reverse of the number using what we discussed in the last quiz and compare it with the original number. It it is the same, then the number is palindromic, otherwise not.

```
int n = scn.nextInt();
int copy = n;

if (n < 0) {
    n = n * - 1;
}

int rev = 0;
while (n > 0) {
    int d = n % 10;
    rev = rev * 10 + d;
    n = n / 10;
}

if (copy < 0) {
    rev = rev * - 1;
}

if (rev == copy) {
    SOPln("PALINDROME");
}
else {
    SOPln("NOT PALINDROME")
}
```

---
title: For loop basics
description: Quick recap of the syntax and flow of for loops
duration: 120
card_type: cue_card
---

## For loop Basics

Every for loop question can be done using a while loop. The difference lies in the syntax.

**Syntax:**
```
for(Initialization; Condition; update) {
    // Statements to be executed
}
```

> Explain the syntax.


**Flow:**
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/757/original/beginner-iterations-loop-2-image-8.png?1693750115" height = "400" width = "380">

---
title: Print numbers from 1 to 5 using for loops
description: Take examples to explain how to use for loops
duration: 180
card_type: cue_card
---
### Example 4
**Question:**

Print all numbers from 1 to 5.

```
for(int i = 1; i <= 5; i ++ ) {
    SOPln(i);
}
```

> Explain the logic behind initialization, condition and update statements.

**Dry Run:**
|  i  | i <= 5 | print(i) | i++ |
|:---:|:------:|:--------:|:---:|
|  1  |  true  |    1     |  2  |
|  2  |  true  |    2     |  3  |
|  3  |  true  |    3     |  4  |
|  4  |  true  |    4     |  5  |
|  5  |  true  |    5     |  6  |
|  6  | false  |    -     |  -  |

---
title: Quiz 1
description: Quiz 1
duration: 60
card_type: quiz_card
---

# Question
Expected output for following code :

```
for(int i = 1; i <= 10; i = i + 2) {
    System.out.println(i);
}
```

# Choices
- [ ] All Numbers from 1 to 10
- [ ] All Even Numbers from 1 to 10
- [x] All Odd Numbers from 1 to 10
- [ ] All Numbers from 1 to 9

---
title: Explain the quiz answer
description: Perform a dry run to explain the quiz question
duration: 240
card_type: cue_card
---

### Explaination

**Dry Run:**
|  i  | i <= 10 | print(i) | i += 2 |
|:---:|:-------:|:--------:|:------:|
|  1  |  true   |    1     |   3    |
|  3  |  true   |    3     |   5    |
|  5  |  true   |    5     |   7    |
|  7  |  true   |    7     |   9    |
|  9  |  true   |    9     |   11   |
| 11  |  false  |    -     |   -    |

---
title: Print the count of digits of a number
description: Take examples to explain how to use for loops
duration: 600
card_type: cue_card
---

### Example 5
**Question:**

Given a positive number, print the count of digits.

> Give examples such as 5164, 121700, 9, etc.

**Approach/Intuition:**
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/767/original/beginner-iterations-loop-2-image-9.png?1693751819" height = "400" width = "380">

```
int count = 0;
for(int i = n; i > 0; i = i / 10) {
    count += 1;
}

SOPln(count);
```

> Show that the above code does not work for n = 0 and make the following change.

```
int count = 0;
if (n == 0) count = 1;

for(int i = n; i > 0; i = i / 10) {
    count += 1;
}

SOPln(count);
```

---
title: Read 5 numbers and for every number print last digit of the number.
description: Explain the need of for loops
duration: 780
card_type: cue_card
---
### Example 6

**Question:**

Read 5 numbers and for every number print last digit of the number.

**Example:**
Input:
34
45
378
980
456

**Output:**
4
5
8
0
6

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

**Approach 1:**

```
int a = scn.nextInt();
int b = scn.nextInt();
int c = scn.nextInt();
int d = scn.nextInt();
int e = scn.nextInt();

SOPln(a % 10);
SOPln(b % 10);
SOPln(c % 10);
SOPln(d % 10);
SOPln(e % 10);
```

**Approach 2:**
```
for(int i = 0; i < 5; i ++ ) {
    int n = scn.nextInt();
    SOPln(n % 10);
}
```

---
title: Read T numbers and for every number print last digit of the number.
description: Show examples to explain how to use for loops
duration: 360
card_type: cue_card
---
### Example 7

**Question:**

Read T numbers and for every number print the last digit.

**Input Format:**
1st Line: Contains T
Followed by T lines containing the T numbers

```
int T = scn.nextInt();

for(int i = 0; i < T; i ++ ) {
    int n = scn.nextInt();
    SOPln(n % 10);
}
```

---
title: Read T numbers and for every number print the sum of digits of the number.
description: Show examples to explain how to use for loops
duration: 420
card_type: cue_card
---
### Example 8
**Question:**

Read T numbers and for each number, print the sum of digits of the number.

**Input:**
3
566
4130
162

**Output:**
17
8
9

```
int T = scn.nextInt();

for(int i = 0; i < T; i ++ ) {
    int n = scn.nextInt();

    if (n < 0) {
        n = n * - 1;
    }

    int s = 0;
    while (n > 0) {
        int d = n % 10;
        s = s + d;
        n = n / 10;
    }

    SOPln(s);
}
```

> Show dry run for the example above.

Same question using for loop - 
```
int T = scn.nextInt();

for(int i = 0; i < T; i ++ ) {
    int n = scn.nextInt();

    if (n < 0) {
        n = n * -1;
    }

    int s = 0;
    for(int x = n; x > 0; x ++ ) {
        int d = x % 10;
        s = s + d;
    }

    SOPln(s);
}
```

