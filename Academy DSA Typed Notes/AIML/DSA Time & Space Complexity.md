# DSA: Time & Space Complexity


## Problem 1 Count of factors

Q. What is a factor?
A. We say i is a factor of N if i divides N completely, i.e the remainder is 0.

How to programmatically check if i is a factor of N ?
We can use % operator which gives us the remainder.
=> **N % i == 0**

### Problem Statement:
Given N, we have to count the factors of N.
**Note:** N > 0


---

### Question
Number of factors of the number 24.

### Choices
- [ ] 4
- [ ] 6
- [x] 8
- [ ] 10


### Explanation
1, 2, 3, 4, 6, 8, 12, and 24 are the factors.

---

### Question
Number of factors of the number 10.

### Choices
- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4



### Explanation

1, 2, 5, and 10 are the factors.

---

### Brute Force Solution


What is the minimum factor of a number ?
=> 1

What is the maximum factor of a number ?
=> The number itself

So, we can find all factors of N from 1 to N.


### Pseudocode
```cpp=
function countfactors (N){
    fac_count = 0
    for(i -> 1 to N) {
        if (N % i == 0)
            fac = fac + 1
    }
    return fac
}  
```

> NOTE: Now that you all are well aware of language basics of your language, like writing basic for loop, while, loop, if else, array declaration, etc.. the codes will be writing as pseudocodes. What are they? => please explain by writing below code.

### Observations for Optimised Solution

* Now, your code runs on servers. 
* When you submit your code, do you expect some time within which it should return the Output ?
* You wouldn't want to wait when you even don't know how long to wait for ?
* Just like that one friend who says, 'Just a little more time, almost there.' And you feel annoyed, not knowing how much longer you'll have to wait.

Servers have the capability of running ~10^8 Iterations in 1 sec. 
Please note that this is a standard assumption accross all platforms.

> Note: We shall be learning more about it in next session

Explain the time taken by above code for below values of N and need for Optimisation.

|N|		Iterations| Execution Time|
|-|----------|---------- |
|10^8| 	10^8 iterations| 1 sec |
|10^9| 	10^9 iterations| 10 sec |
|10^18| 	10^18 iterations| 317 years |

So, for N = 10^18, to just get the number of factors, we need around 317 years.

*Would you be alive to watch the O/P ?
Your children ?
3rd Gen ?
4th Gen ?
............. too long to wait.*


#### Optimisation for Counting Factors 


i * j = N     -> {i and j are factors of N}

=> j = N / i  -> {i and N / i are factors of N}

For example, N = 24

|i|		N / i| 
|-|----------|
|1| 	24|
|2| 	12|
|3| 	8|
|4| 	6|
|6| 	4|
|8| 	3|
|12| 	2|
|24| 	1|

Q. Can we relate these values?
A. We are repeating numbers after a particular point. Here, that point is from 5th row.

Now, repeat the above process again for N = 100.

|i|		N / i| 
|-|----------|
|1| 	100|
|2| 	50|
|4| 	25|
|5| 	20|
|10| 	10|
|20| 	5|
|25| 	4|
|50| 	2|
|100| 	1|

The factors are repeating from 6th row. After a certain point factors start repeating, so we need to find a point till we have to iterate.

We need to only iterate till -

**`i <= N/i`**
**`i * i <= N`**

### Pseudocode

```cpp=
function countfactors(N){
    fac_count = 0
    for(i -> 1  till i*i <= N) {
        if (N % i == 0)
            fac = fac + 2
    }
    return fac
}
```

Q. Will the above work in all the cases?
A. No, not for perfect squares. Explain this for N = 100, what mistake we are doing. We will count 10 twice.

**Observation:** Using the above example, we need to modify the code for perfect squares.


### Pseudocode with Edge Case Covered

```cpp=
function countfactors(N){
    fac_count = 0
    for(i -> 1  till i*i <= N) {
        if (N % i == 0){
            if(i == N / i){
                fac = fac + 1
            }
            else {
                fac = fac + 2
            }
        }
    }
    return fac
}
```

Dry run the above code for below examples,
N = 24, 100, 1.

### What's the number of iterations now ?

We are running loop till i * i <= N
Let's evaluate it -
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/846/original/upload_b7d89a4e3534f96005e65eaec0681e2a.png?1692787858)


|N|		Iterations| Execution Time|
|-|----------|---------- |
|10^18| 	10^9 iterations| 10 secs |

**Conclusion:** Most important skill for problem solving is observation.

>How beautifully we have been able to reduce the Iterations just by making some Observations!

### Follow Up Question
Given N, You need to check if it is prime or not.

---
### Question
How many prime numbers are there?
10, 11, 23, 2, 25, 27, 31

### Choices
- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4



### Explanation
Q. What is a prime Number?
A. Number which has only 2 factors, 1 and N itself.

So, 11, 23, 2, and 31 are the only prime numbers since they all have exactly 2 factors.

---

## Some Basic Math Properties

1. `[a,b]` - This type of range means that a and b are both inclusive.
2. `(a,b)` - This type of range means that a and b are both excluded.



---
### Question
How many numbers are there in the range [3,10]?

### Choices
- [ ] 7
- [ ] 6
- [x] 8
- [ ] 10

### Explanation

The range [3,10] includes all numbers from 3 to 10, inclusive. Inclusive means that both the lower bound (3) and the upper bound (10) are included in the range. Thus the numbers that are included are 3 4 5 6 7 8 9 10.

--- 

### Question
How many numbers are there in the range [a,b]?

### Choices
- [ ] b - a
- [x] b - a + 1
- [ ] b - a - 1
- [ ] Ahhh.. too tricky to calculate

### Explanation

To find the number of numbers in a given range, we can subtract the lower bound from the upper bound and then add 1. Mathematically, this can be expressed as:
```
Number of numbers in the range 
= Upper bound - Lower bound + 1
```

---

### Question
1 + 2 + 3 + 4 + 5 + 6 + ... + 100 = ?

### Choices
- [ ] 1010
- [x] 5050
- [ ] 5100
- [ ] 1009

### Explanation

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/034/347/original/ytbMtMR.png?1684220222" width=500/>

Generalize this for the first N natural numbers.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/034/348/original/iqYoobK.png?1684220244" width=500 />

---

## Geometric Progression

> **Example for intution:**
```
5 10 20 40 80 ..
```
In these type of series, the common ratio is same. In the given example the common ratio r is
= 10/5
= 20/10
= 40/20
= 80/40
= 2

**Generic Notation:**
a, a * r, a * r^2^, a * r^3^ ........a * r^n-1^

### Sum of first N terms of a GP


**Sum of first N terms of GP:**
= <img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/847/original/upload_7d7368fe780e904c2836a90ed74e5b1e.png?1692787881" width=400/>


r cannot be equal to 1 because the denominator cannot be zero.

**Note:** 
When r is equal to 1, the sum is given by a * n.

## Real Life Examples of GP


### **Spreading of news**
Suppose one person spreads a news to 4 different people. Each one of those, spreads to 4 others, and so on..

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/086/636/original/Screenshot_2024-08-19_at_2.51.07_PM.png?1724059285" width=500 />

This can be denoted in form of GP which looks as follows-
1, 4, 16, 64, .....

### Number of people at 8th level
Now, if we want to figure out that at 8th level, how many people will know about this news, we can use formula for getting 8th term.

Formula for nth term = a * r^n-1^
a = 1, r = 4, n = 8

8th term = 1 * (4)^8-1^ = 16384

### Sum till 8th level
GP = 1, 4, 16, 64, 256, 1024, 4096, 16384

sum = a * ( r^#terms^ - 1)/ (r - 1)

= 1 * (4^8^ - 1)/(4 - 1)
= (65536-1)/3 = 65535/3 = 21845

> **`Likewise, there can be multiple examples related to calculation of simple interest, spreading of a disease, growing population, depreciating value of car, etc...`**


### What do we mean by Iteration?

The number of times a loop runs, is known as Iteration.

---
### Question
How many times will the below loop run ?

```
for(i -> 1 to N)
{
    if(i == N) break; 
}
```

### Choices
- [ ] N - 1
- [x] N
- [ ] N + 1
- [ ] log(N)

---

### Question
How many iterations will be there in this loop ?

```
for(i -> 0 to 100){
    s = s + i + i^2;
}
```

### Choices
- [ ] 100 - 1
- [ ] 100
- [x] 101
- [ ] 0

---

### Question
How many iterations will be there in this loop?
```
func(){
    for(i -> 1 to N){
        if(i % 2 == 0){
            print(i);
        }
    }
    for(j -> 1 to M){
        if(j % 2 == 0){
            print(j);
        }
    }
}
```

### Choices
- [ ] N
- [ ] M
- [ ] N * M
- [x] N + M



### Explanation

We are executing loops one after the other. Let's say we buy first 5 apples and then we buy 7 apples, the total apples will be 12, so correct ans is N + M

---

> How to compare two algorithms?

### Story
There was a contest going on to SORT the array and 2 people took part in it (say Gaurav and Shila).

They had to sort the array in ascending order.

arr[5] = {3, 2, 6, 8, 1} -> {1, 2, 3, 6, 8}

Both of them submitted their algorithms and they are being run on the same input.

See this image to understand one important aspect of comparing two algorithms.

## Discussion

Can we use execution time to compare two algorithms?

Say initially **Algo1** took **15 sec** and **Algo2** took **10sec**. 

This implies that **Shila's Algo 1** performed better, but then Gaurav pointed out that he was using **Windows XP** whereas Shila was using **MAC**, hence both were given the same laptops.........

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/034/050/original/time-complexity-2-image-1.png?1683815146" width=500 />

## Conclusion
We can't evaluate algorithm's performance using **execution time** as it depends on a lot of factors like operating system, place of execution, language, etc.

### Question
How can we compare two algorithms?
Which measure doesn't depend on any factor? 

**Answer:** Number of Iterations

**Why?**
* The number of iterations of an algorithm remains the same irrespective of Operating System, place of execution, language, etc.


---

## Asymptotic Analysis of Algorithms

**Asymptotic Analysis** OR **Big(O)** simply means analysing perfomance of algorithms for **larger inputs**.

### Calculation of Big(O)
**Steps** for **Big O** calculation are as follows:

* Calculate **Iterations** based on **Input Size**
* Ignore **Lower Order Terms**
* Ignore **Constant Coefficients**

**Example-**
Kushal's algo took **100 * log<sub>2</sub>N** iterations: Big O is **O(log<sub>2</sub>N)**
Ishani's algo took **N / 10** iterations: Big O is **O(N)**

### Examples to calculate the Big O from the number of Iterations

**For example**, 
1. Iterations: 4N^2 + 3N  + 1
2. Neglect lower order term: 3N  + 1; Remaining Term: 4N^2
3. Neglect constant 4

Big O is O(N^2)

### Comparsion Order:

log(N) < sqrt(N) < N < N log(N) < N sqrt(N) < N^2 <  N^3 < 2^(N) < N! < N^N

**Using an example**
N = 36
5 < 6 < 36 < 36\*5 < 36\*6 < 36<sup>2</sup> < 36<sup>3</sup> < 2<sup>36</sup> < 36! < 36<sup>36</sup>

**Ques:** What is the big notation time complexity of the following expression?
4N^2 + 3N + 6 sqrt(N) + 9 log_2(N) + 10
Ans = O(N^2)

> **IMPORTANT:** For every QUIZ in the lecture, please tell their Big O Notation to Students.


---
### Question
F(N) = 4N + 3N * log(N) + 1
O(F(N)) = ?

### Choices
- [ ] N
- [x] N * log(N)
- [ ] Constant
- [ ] N<sup>2</sup>

---

### Question
F(N) = 4Nlog(N) + 3N * Sqrt(N) + 10<sup>6</sup>
O(F(N)) = ?

### Choices
- [ ] N
- [ ] N * logN
- [ ] N<sup>2</sup>
- [x] N * Sqrt(N)

---

## Why do we neglect Lower Order Terms


Let's say the number of Iterations of an Algorithm are: N<sup>2</sup>+10N

N|Total Iterations = N<sup>2</sup>+10N|Lower Order Term = 10N|% of 10N in total iterations = 10N/(N<sup>2</sup>+10N)*100
-|-|-|-
10|200|100|50%
100|10<sup>4</sup>+10<sup>3</sup>|10<sup>3</sup>|Close to 9%
10000|10<sup>8</sup>+10<sup>5</sup>|10<sup>5</sup>|0.1%

## Conclusion
We can say that, as the **Input Size** increases, the contribution of **Lower Order Terms** decreases.

## Why do we neglect Constant Coefficients


When the comparison is on very larger input sizes, the constants do not matter after a certain point. For example,

> In the below scenario, ask the students one by one which algo is better based on their Big O.

| Algo 1(Nikhil)|Algo 2(Pooja)|Winner for Larger Input| 
| -------- | -------- | -------- |
| 10 * log<sub>2</sub> N    | N     | Nikhil     |
| 100 * log<sub>2</sub> N    | N     | Nikhil     |
| 9 * N   | N<sup>2</sup>     | Nikhil     |
| 10 *  N    | N<sup>2</sup> / 10| Nikhil     |
| N * log<sub>2</sub> N    | 100 * N     | Pooja     |

> A question can come that what if the constant is so big?
> We will then talk about Issues with Big O.

---

## Issues with Big(O)


### Issue 1

**We cannot always say that one algorithm will always be better than the other algorithm.**

**Example:**
* Algo1 (Iterations: 10<sup>3</sup> N) -> Big O: O(N)
* Algo2 (Iterations: N<sup>2</sup>) -> Big O: O(N<sup>2</sup>)
* Algo 1 is better than Algo 2 but only for large inputs, not for small input sizes.



|Input Size (N)| Algo 1 (10<sup>3</sup>* N) | Algo 2 (N<sup>2</sup>) | Optimised|
| --| --| --| --|
|N = 10| 10<sup>4</sup>| 10<sup>2</sup>|Algo 2|
|N = 100| 10<sup>5</sup>| 10<sup>4</sup>|Algo 2|
|N = 10<sup>3</sup>| 10<sup>6</sup>| 10<sup>6</sup>|Both are same|
|N = 10<sup>3</sup> + 1| (10<sup>3</sup>)*(10<sup>3</sup> + 1)| (10<sup>3</sup> + 1)*(10<sup>3</sup> + 1)|Algo 1|
|N = 10<sup>4</sup>| 10<sup>7</sup>| 10<sup>8</sup>|Algo 1|

**Claim:** For all large inputs >= 1000, Algo 1 will perform better than Algo 2.

### Issue 2
If 2 algorithms have same higher order terms, then Big O is not capable to identify algorithm with higher iterations.

Consider the following questions -
Count the number of odd elements from 1 to N

Code 1: Iterations: N
```
for(i -> 1 to N) {
    if(i%2 != 0) {
     c = c+1;
    }
}
```

Code 2: Iterations: N/2
```
for(i goes from 1 to N and get incremented by 2 in every iteration) {
    c = c+1;
}
```

In both, Big O is O(N) but we know second code is better.

---

## Importance of Constraints

### Question

If 1 <= N <= 10<sup>5</sup>,
then which of the following Big O will work ?

| Complexity | Iterations | Works ? |
| -------- | -------- | -------- |
| O(N<sup>3</sup>)     | (10<sup>5</sup>)<sup>3</sup>     | No     |
| O(N<sup>2</sup>) log N    | (10<sup>10</sup>)*log 10<sup>5</sup>     | No     |
| O(N<sup>2</sup>)     | (10<sup>5</sup>)<sup>2</sup>     | No     |
| O(N * log N)     | (10<sup>5</sup>)*log 10<sup>5</sup>    | Yes     |


### Question
If 1 <= N <= 10<sup>6</sup>,
then which of the following Big O will work ?

| Complexity | Iterations | Works ? |
| -------- | -------- | -------- |
| O(N<sup>3</sup>)     | (10<sup>6</sup>)<sup>3</sup>     | No     |
| O(N<sup>2</sup>) log N    | (10<sup>12</sup>)*log 10<sup>6</sup>     | No     |
| O(N<sup>2</sup>)    | (10<sup>12</sup>)  | No |
| O(N * log N)     | (10<sup>6</sup>)*log 10<sup>6</sup> ~ 10<sup>7</sup>    | May Be     |
| O(N)     | (10<sup>6</sup>)   | Yes     |


#### Question
If constraints are 
1 <= N <= 100, N<sup>3</sup> will also pass.

If constraints are 
1 <= N <= 20, 2<sup>N</sup> will also pass.

**Note:**
In Online Assessments, if we are not getting any other approach to a problem, try out the code; it may pass some test cases, which is better than nothing.

---

## How to approach a problem?

* Read the **Question** and **Constraints** carefully.
* Formulate an **Idea** or **Logic**.
* Verify the **Correctness** of the Logic.
* Mentally develop a **Pseudocode** or rough **Idea of Loops**.
* Determine the **Time Complexity** based on the Pseudocode.
* Assess if the time complexity is feasible and won't result in **Time Limit Exceeded (TLE)** errors.
    * Note: In worst case we can only have **10^7 or 10^8 iterations**.
* **Re-evaluate** the **Idea/Logic** if the time constraints are not met; otherwise, proceed.
* **Code** the idea if it is deemed feasible.

### Space Complexity


* Space complexity is the max space(worst case) that is utilised at any point in time during running the algorithm.
* We also determine Space Complexity using **Big O**.

Consider the following example:

NOTE: **`Please mention that for Python, we don't have to explicitly mention the data types while declaring array, hence it'll be an additional information for them, but good to know`**.

```
func(int N) { // 4 bytes
    int x; // 4 bytes
    int y; // 4 bytes
    long z; // 8 bytes
}
```

* We only consider the space utilised by our program and not the Input Space since it is not in our control, hence we'll ignore space taken by "int N".
* The above code takes total **16B** of memory.
* Hence, we say the **Space Complexity** of the above code is **O(1)** (1 resembles constant).



---

### Question
Find the Space Complexity [Big(O)] of the below program.
```
func(int N) {    // 4 bytes
    int arr[10]; // 40 Bytes
    int x;       // 4 bytes
    int y;       // 4 bytes
    long z;      // 8 bytes
    int arr[N];  // 4 * N bytes
}
```
### Choices
- [x] N
- [ ] 4N + 60
- [ ] Constant
- [ ] N^2

---

### Question
Find the Space Complexity [Big(O)] of the below program.

```javascript
func(int N) {       // 4 bytes
    int x = N;      // 4 bytes
    int y = x * x;  // 4 bytes
    long z = x + y; // 8 bytes
    int arr[N];     // 4 * N bytes
    long l[N][N];   // 8 * N * N bytes
}
```
### Choices
- [ ] N
- [ ] 4N + 60
- [ ] Constant
- [x] N<sup>2</sup>

---

### Question on Space Complexity

Find the Space Complexity [Big(O)] of the below program.

```
function maxArr(int arr[], int N) {
    int ans = arr[0];
    for(i -> 1 to N-1) {
        ans = max(ans, arr[i]);
    }
    return ans;
}
```

### Space complexity: O(1)

* Don't consider the space acquired by the input size. Space complexity is the order of extra space used by the algorithm.
* **arr[]** is already given to us, we didn't create it, hence it'll not be counted in the Space Complexity.
* **int N** will also not be counted in space but since it is contant hence doesn't matter.
* Additional space is also called **computational or auxiliary space.**
* The above code finds the max element of the Array.
