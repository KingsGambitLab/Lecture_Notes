# Patterns Introduction
---

## Agenda

**Some abbreviations that will be used in this class:**
* System.out.print - SOP
* System.out.println - SOPln



We will work with patterns today. After this class, the students will feel very comfortable with loops.
1. Print stars in a single row
2. Print a square
3. Print a rectangle
4. Print staircase
5. Print reverse staircase
6. Print special pattern



---

# Question
Loop to print " * " N times in a single row?
Ex: N = 5, print *****
N = 9, print *********

# Choices
- [x] for(int i = 1; i <= N; i++) {
SOP(" * ");
}
- [ ] for(int i = 1; i < N; i++) {
SOP(" * ");
}
- [ ] for(int i = 0; i <= N; i++) {
SOP(" * ");
}



---

## Explanation

```java
for(int i = 1; i <= N; i++) {
    SOP(" * ");
}
```
This choice is correct. The code uses a loop to iterate from `i = 1` to `i = N` (both inclusive). In each iteration, it prints the "*" character using the `SOP("*");` statement. This loop will print "*" N times in a single row, as desired.


Certainly, let's take a look at why the other two choices are incorrect:

1. **Incorrect Choice 2:**
   ```java
   for (int i = 1; i < N; i++) {
       SOP(" * ");
   }
   ```
   **Explanation:** This code uses a loop that starts from `i = 1` and continues until `i` is less than `N`. In each iteration, it prints an asterisk. However, this loop only iterates `N - 1` times, which means it will print one less asterisk than the desired value. For example, if `N` is 5, this loop will print `****` (4 asterisks) instead of `*****`.

2. **Incorrect Choice 3:**
   ```java
   for (int i = 0; i <= N; i++) {
       SOP(" * ");
   }
   ```
   **Explanation:** This code uses a loop that starts from `i = 0` and continues until `i` is less than or equal to `N`. In each iteration, it prints an asterisk. However, this loop iterates `N + 1` times, which means it will print one more asterisk than the desired value. For example, if `N` is 5, this loop will print `******` (6 asterisks) instead of `*****`.


---


### Example 1

This is the quiz question.
Print N starts " * " in  a single row.
N = 5, *****
N = 4, ****
N = 2, **

**Q.** What should be the number of iterations?
**A.** "N"


**Code:**

```
 public static void main() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            System.out.print(" * ");
        }
    }
```
Dry run the codes and justify why Option 1 is correct for some values of N.

---

### Example 2
Print a square (N * N) of stars.

For example, 

N = 4
```plaintext
****
****
****
****
```

N = 5
```plaintext
*****
*****
*****
*****
*****
```

**Q.** If you have to repeat a single task N number of tasks, how to do that?
**A.** We can write a loop.


Now, this questions is similar to repeating 1st task N number of times.
So, the code can be:

```
for (int i = 1; i <= N; i++) {
    for (int i = 1; i <= N; i++) {
        SOP(" * ");
    }
    SOPln();
}
```

Ask students if this code is correct. It's not, because we cannot repeat variable 'i' in java.
So, the final correct code is:

```
for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
        SOP(" * ");
    }
    SOPln();
}
```

Explain why we need `SOPln()` after the 2nd for loop.

**Explanation:**
Without the `SOPln()` statement after the inner loop, all the asterisks would be printed in a single continuous line, and the pattern would not be formed with rows and columns. The `SOPln()` call ensures that each row of asterisks is printed on a new line, creating the desired pattern.

Dry run the above code for N = 3.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/810/original/upload_f645c770eeb92640a9f8cc6db03c3cc4.png?1693755503" 
     height = "350" width = "450">



---

### Example 3
Print rectangle of N * M having stars.
N rows having M stars in each row.

For example,

N = 4, M = 3
```plaintext
***
***
***
***
```
N = 2, M = 4
```plaintext
****
****
```

Outer loop -> N times
Inner loop -> M times

The correct code is:
```
for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
        SOP(" * ");
    }
    SOPln();
}
```

**Note:** Mention that the starting values does not matter. Just that the number of iterations should be N.

Dry run for N = 2, M = 3.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/812/original/upload_a445fa2609ea3cf56e1734ba8f432818.png?1693755542" 
     height = "300" width = "6000">


**Observation Table:**

| Row | Stars |
|:---:|:-----:|
|  1  |   3   |
|  2  |   3   |


ith row => M stars
and a total N rows


---

### Example 4
Print staircase pattern.
For example, 

N = 4
```plaintext
*
**
***
****
```

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

Observe for each row number i, we have i stars in that row.

Outer Loop -> N times
Inner Loop -> i times
Inner loop does not work for constant number of times.

**Observation Table:**

| Row | Stars |
|:---:|:-----:|
|  1  |   1   |
|  2  |   2   |
|  3  |   3   |
|  4  |   4   |
|  5  |   5   |


ith row => i stars


The correct code is:
```
for (int i = 1; i <= N; i++) {
    
    // Loop to print i stars.
    for (int j = 1; j <= i; j++) {
        SOP(" * ");
    }
    SOPln();
}
```

Dry run this code for N = 4 (Given image is incomplete).
You may complete the dry run or stop in-between according to the batch.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/813/original/upload_210e5f09585ebf945b8091effbbc4957.png?1693755626" 
     height = "350" width = "600">


---


### Example 5

> **Note for instructor:** Give some context of why we are learning this approach. Like, as similar approach will work in majority of pattern questions

Print reverse staircase pattern.
For example,
N = 4
```plaintext
****
***
**
*
```

N = 5
```plaintext
*****
****
***
**
*
```

For N = 5, we are printing stars in the following manner.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/814/original/upload_603a3fffb7a60cb436ec6c3f9cd701d8.png?1693755658" 
     height = "300" width = "450">

Row + star = N + 1
So, star = N + 1 - Row
Observe for each row number i, we have N - i + 1 stars in that row.

Outer Loop -> N times
Inner Loop -> N - i + 1 times
Inner loop does not work for constant number of times.

The correct code is:
```java
for (int i = 1; i <= N; i++) {
    
    // Loop to print N - i + 1 stars.
    for (int j = 1; j <= N - i + 1; j++) {
        SOP(" * ");
    }
    SOPln();
}
```

Dry run the code for N = 3.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/815/original/upload_36fc6fad1038306dbbea3e096487fb78.png?1693755708" 
     height = "300" width = "500">

---


#### Another Approach

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/816/original/upload_9e6e30919023e0f930c7d6a77dbfc12d.png?1693756190" 
     height = "250" width = "500">

In this approach, we will change the starting value of i itself.

The correct code is:
```
for (int i = N; i >= 1; i--) {
    
    // Loop to print i stars.
    for (int j = 1; j <= i; j++) {
        SOP(" * ");
    }
    SOPln();
}
```


---

### Example 6
Print the diamond pattern.

For example,
N = 5

```plaintext
**********
****--****
***----***
**------**
*--------*
*--------*
**------**
***----***
****--****
**********
```

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/817/original/upload_52ad209dbb64e8caaea062a196388d88.png?1693756234" 
     height = "300" width = "550">

You are only supposed to print star " * ", but not underscores (they should be spaces).

If N = 5, so 10 rows are needed.

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

The pattern can be broken into two halves.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/820/original/upload_308e046a7c9a3d5a090c91f4bdbeb45c.png?1693756293" 
     height = "400" width = "250">

Again, we can break this pattern into halves again.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/821/original/upload_7f1f949912f01d8526b41b664739fcbe.png?1693756327" 
     height = "200" width = "550">

For the right quarter, we need to print some spaces first and then stars.
The table shows for each row, how many spaces and stars need to be printed.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/822/original/upload_f12e19981999da489adddc4e0116fb84.png?1693756365" 
     height = "300" width = "500">

Combining everything for the first half, we have the following table.

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/823/original/upload_2eab4eb6d8be0559bd3c33a7aaa316c3.png?1693756386" 
     height = "300" width = "500">

In one single row,

print (N + 1 - i) stars + (i - 1) spaces + (i - 1) spaces + (N + 1 - i) stars

So, print (N + 1 - i) stars + 2 * (i - 1) spaces + (N + 1 - i) stars
So, let's write the code for the upper half using the above facts.

```
for (int i = 1; i <= N; i++) {
    
    // In each row, print N + 1 - i stars.
    for (int j = 1; j <= N + 1 - i; j++) {
        SOP(" * ");
    }
    
    // In each row, (i - 1) spaces.
    for (int j = 1; j <= 2 * (i - 1); j++) {
        SOP(" _ ");
    }
    
    // In each row, print N + 1 - i stars.
    for (int j = 1; j <= N + 1 - i; j++) {
        SOP(" * ");
    }
    SOPln();
}
```

**Lower Half:**

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/824/original/upload_de9788a8310b94486706ebd6b69671bb.png?1693756417" 
     height = "200" width = "300">

For lower part, we can directly write the following table:

<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/045/825/original/upload_17ef3ebc6ea5203765bad9eca9915b17.png?1693756437" 
     height = "310" width = "700">


In one single row,
print i stars + print (N - i) spaces + print (N - i) spaces + i stars

So, print i stars + print 2 * (N - i) spaces + i stars
So, let's write the code for the upper half using the above facts.

```
for (int i = 1; i <= N; i++) {
    
    // In each row, print N + 1 - i stars.
    for (int j = 1; j <= i; j++) {
        SOP(" * ");
    }
    
    // In each row, (i - 1) spaces.
    for (int j = 1; j <= 2 * (N - i); j++) {
        SOP(" _ ");
    }
    
    // In each row, print N + 1 - i stars.
    for (int j = 1; j <= i; j++) {
        SOP(" * ");
    }
    SOPln();
}
```

Combining these 2 codes we get, the diamond pattern.


---


### Example 7
Print the following pattern:

For example, 

N = 5
```plaintext
1
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
```

N = 4
```plaintext
1
2 3 
4 5 6
7 8 9 10
```

We will create a variable and print that variable. After printing, we increment it.

```
int val = 1;
for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= i; j++) {
        SOP(val);
        val++;
    }
    SOPln();
}
```


**Explanation:**

In the given approach we have initialized a variable `val` to 1. It employs an outer loop that iterates from 1 to N, governing the rows. Within this loop, an inner loop runs from 1 to the current value of the outer loop index, controlling the values within each row. It prints the value of `val`, increments it, and then proceeds with the next iteration of the inner loop. This structure creates a pattern where each row holds an increasing sequence of numbers. The `SOPln()` statement at the end of the outer loop iteration ensures a new line for the subsequent row. By iteratively printing values and managing rows through nested loops, the code systematically generates the desired pattern of numbers.


---


### Example 8
Print the following pattern:
For example, 

N = 5
```plaintext
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

**Approach 1:**
```
for (int i = 1; i <= N; i++) {
    
    int val = 1;
    for (int j = 1; j <= i; j++) {
        SOP(val);
        val++;
    }
    SOPln();
}
```

**Approach 2:**
In this approach instead of taking an extra variable we can directly print j.
```
for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= i; j++) {
        SOP(j);
    }
    SOPln();
}
```

---


### Example 9

Print the following pattern.
For example,

N = 5
```plaintext
1
2 3 
3 4 5
4 5 6 7
5 6 7 8 9 
```

The pattern now starts at each row with that row number. So, only 1 change is required i.e, in the initial value of val.

The correct code for this pattern is:
```
for (int i = 1; i <= N; i++) {
    
    int val = i;
    for (int j = 1; j <= i; j++) {
        SOP(val);
        val++;
    }
    SOPln();
}
```

---