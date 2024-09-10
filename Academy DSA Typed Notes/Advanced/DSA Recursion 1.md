# Recursion 1


## Introduction to Recursion


### Definition
1. Watch this video - [LINK](https://www.youtube.com/watch?v=-xMYvVr9fd4)
2. Function calling itself.
3. A problem is broke into smaller problem(subproblem) and the solution is generated using the subproblems.


### Example
Here's an example of how recursion can be used to calculate the sum of the first **N** natural numbers:
```cpp
sum(N) = 1 + 2 + 3 + 4 + ..... + N-1 + N
sum(N) = sum(N-1) + N
```
Here, **sum(N-1)** is smaller instance of same problem that is **sum(N)**.
sum(N-1) is known as a subproblem.

### How to write a recursive code?
We can solve any recursive problem using below magic steps:

1. **Assumptions:** Decide what the function does for the given problem.
2. **Main logic:** Break the problem down into smaller subproblems to solve the assumption.
3.  **Base case:** Identify the inputs for which we need to stop the recursion.

### Sum of N
```
//Assumption: function sum(N) will return sum of numbers from 1 to N

function sum(N) {
    //Base Case
    if(N==0) {
        return 0;
    }
    
    //Main Logic
    return N + sum(N-1); //sum(N-1) will return sum of numbers from 1 to N-1
}
```

---
## Function Call Tracing


* Function call tracing involves tracing the sequence of function calls that are made when a program is executed. 
* It involves keeping track of the function calls, their arguments, and the return values in order to understand the flow of the program and how the functions are interacting with each other.

### Example:
We have the following code:
```cpp
function add(x, y) {
    return x + y;
}

function mul(x, y, z) {
    return x * y * z;
}

function sub( x, y) {
    return x - y;
}

function ( x) {
    cout << x << endl;
}

function main() {
    x = 10, y = 20;
    print(sub(mul(add(x, y), 30), 75));
}
```
Here are the steps involved in function call tracing of the above code:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/034/896/original/Screenshot_2023-05-22_at_9.21.01_PM.png?1684771032" alt= “” width="350" height="400">

* We start with the call to **sub(mul(add(10, 20), 30), 75)**.
* That called: **mul(add(10, 20), 30)**.
* That called: **add(10, 20)**.
* add will return **10+20 = 30** to **mul** function.
* mul will return **30*30 = 900** to **sub** function.
* sub will return **900-75 = 825** to print function.

### Data structure involved in function calls
* We need to store calling function so that we can come back to it once answer of the called function has been evaluated.
* **Stack Data Structure** is used to store function calls, their arguments, and return values. 
* In recursion, stack is called "call stack" and is used by the program to keep track of function calls in progress.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/033/383/original/Screenshot_2023-05-02_at_3.13.05_PM.png?1683043955" alt= “” width="600" >

---
## Problem 1 Factorial of N

### Problem Statement
Given a positive integer N, find the factorial of N.

---

### Question
If N = 5, find the factorial of N.
### Choices
- [ ] 100
- [x] 120
- [ ] 150
- [ ] 125


---
### Factorial of N Solution

**Assumptions:** Create a function which - 
* takes an integer value `N` as parameter. 
* calculates and returns N!.
* return type should be integer.

**Main logic:** 
* The factorial of N is equal to N times the factorial of (N-1)
* We made assumption that sum(N) calculates and return sum of N natural number. Similarly, sum(N-1) shall calculate and return the factorial of N-1 natural number.
`factorial(N) = N * factorial(N-1)`

**Base case:** The base case is when N equals 0, i.e., `0! = 1`

For example,
When we perform, `factorial(N) = N * factorial(N-1)`, value of N keeps on decreasing by 1. 
`N -> (N-1) -> (N-2) ........ 2 -> 1` 
for N = 1 as well as 0, the factorial is 1.
So, we can write base case for N = 0 which will also cover for N = 1.

### Pseudocode
```cpp
factorial(N) {
    // base case
    if (N == 0) { 
        return 1;
    } 
    // recursive case
    return N * factorial(N-1);
}
```

### Dry Run

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/805/original/Screenshot_2023-10-08_at_6.50.26_PM.png?1696771237" width="350" />

---
## Problem 2 Printing numbers in increasing order


### Problem Statement
Given N, print all numbers from 1 to N in increasing order.

Inc(5)= 1 2 3 4 5
Inc(5) = Inc(4) + 5
Subproblem: Inc(4)

---
### Question

Which of the following correctly represents the N Increasing numbers in form of subproblems?

### Choices
- [x] Inc(N - 1) 
- [ ] Inc(N + 1) 
- [ ] Inc(N) 

---
### Solution 

```javascript
// Assumption - Given N, print all numbers from 1 to N

function increasing(N) {
    //Base Condition
    if(N == 1) {
        print(N)
        return
    }
    
    //Main Logic
    increasing(N-1) //subproblem
    print(N) //first we call for recursion and then print
}
```

**Dry Run**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/164/original/upload_ad93d552333c416bad2a243d135af117.png?1695877458" width=700 />

**Note:** 
* If the return type is void we can still write **return statement** to exit the function.
* When the function ends {last line executed} or when we execute a return, it will go back to where it was called.

---
## Problem 3 Whirlpool's countdown timer


### Problem 
**Whirlpool** wants to design a timer for their **washing machines**. This feature is a simple countdown timer. When a user sets a time, for example, 10 minutes, the washing machine needs to show each minute passing, counting down until it reaches 0.

Your task is to write a program that takes an integer **A** (the time in minutes set by the user) and then prints out each minute as it counts down to **0**.The requirement is that after a user set a timer for the washing machine for some time say **A** , the washing machine should display each minute after that decremented one by one till the time becomes **0**.


### Simplified Problem statement 
Given **N**, print all numbers from **1 to N** in decreasing order.

### Approach

- `decreasing(5) = 5 4 3 2 1`
- `decreasing(5) = print(5) decreasing(4)`
- `decreasing(N) = N N - 1 N - 2 ... 2 1` 
- `decreasing(N) = print(N) decreasing(N - 1)`

### Pseudocode
```java
// Assumption - Given N, print all numbers from N to 1

function decreasing(N) {
    //Base Condition
    if(N == 1) {
        print(N)
        return
    }
    
    //Main Logic
    print(N) //first we print and then we call for recursion
    decreasing(N-1) //subproblem
}   
```

### Time and Space Complexity of Recursion


**Time Complexity = O(Number of function calls * Time per function call)**

**Space Complexity = O(Maximum depth of recursion tree/stack space + Space per function call)**

The space complexity of recursion refers to the amount of memory required by a recursive algorithm as it executes. It is determined by the maximum amount of memory needed on the call stack at any given point during the recursion(stack space can be measured from height of the tree).

## Factorial(N)

#### Pseudocode
```cpp
function factorial(N) {
    // base case
    if (N == 0) { 
        return 1;
    } 
    // recursive case
    return N * factorial(N-1);
}
```

#### Recursive Tree for Factorial

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/065/181/original/Screenshot_2024-02-15_at_11.51.09_AM.png?1707978082" width=200 />



### Time Complexity

For finding number of function calls, we can see the above recursive tree.
If N=5, number of function calls = 5
If N=6, number of function calls = 6
Hence for N, number of function calls = N
Time take per call = O(1)

Hence, for factorial, overall time complexity = O(N)

### Space Complexity
Total N call will be stored in the stack.
```
factorial(1)
factorial(2)
---------------
---------------
---------------
factorial(N-1)
factorial(N)
```
The height of recursive tree = N, hence stack space is O(N) and no extra space is used in calls, hence total space complexity O(N)

## increasing(N) /decreasing(N)

### Time Complexity
Number of function calls are N
Time per call is O(1)
Total T.C = O(N)

### Space Complexity
Since height of recursive tree is N, and no extra space is used otherwise, the S.C = O(N)


---
## Problem 4 Nth number in the Fibonacci Series

### Problem Statement
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers.


The sequence goes like this:
| N | 0 | 1 | 2 | 3 | 4 | 5 |....|
|---|---|---|---|---|---|---|---|
| Fibonacci(N) | 0 | 1 | 1 | 2 | 3 | 5 |....|


Given a positive integer N, write a function to compute the Nth number in the Fibonacci sequence using recursion.

### Example
```cpp
Input = 6
Output = 8
```
**Explanation:** 
| N | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Fibonacci(N) | 0 | 1 | 1 | 2 | 3 | 5 | 8 |

Fibonacci(6) = Fibonacci(5) + Fibonacci(4) = 3 + 5 = 8.

---

### Question
If N = 7, find the Nth number in the fibonacci sequence.
### Choices
- [ ] 8
- [ ] 5
- [x] 13
- [ ] 10

---
## Nth number in the Fibonacci sequence Solution


### Solution
**Assumptions:** Create a function which - 
* takes an integer value `N` as parameter. 
* calculates and returns Nth number in the fibonacci sequence.
* return type should be integer.

**Main logic:**  Recursively compute the (N-1)th and (N-2)th numbers in the sequence and add them together to get the nth number.
`fibonacci(N) = fibonacci(N - 1) + fibonacci(N - 2)`

**Base case:** If N is 0 or 1, return the corresponding value in the Fibonacci sequence.

* Since, according to the definition of fibonacci sequence, the smallest two possible values of N are `N = 1` & `N = 2`, therefore, stop recursion as soon as N becomes 0 or 1.

### Pseudocode
```cpp
function fibonacci(N) {
    // base case
    if (N == 0 || N == 1) {
        return N;
    }
    
    // recursive case
    return fibonacci(N - 1) + fibonacci(N - 2);
}

```
### Function Call Tracing
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/034/890/original/Screenshot_2023-05-22_at_8.05.10_PM_%281%29.png?1684766319" alt= “” width="500" height="500">

**HW:** Do the above function call tracing with stack.

---
## Time and Space for Fibonacci


#### Pseudocode
```c++
Function fibonacci(n){
    if(n == 0 || n == 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
} 
```
#### Recursive Tree for Fibonacci

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/163/original/fibonacci.png?1706036608" width=500/>

### T.C 

In above tree, how many function calls are there ?
In level 1 => 2^0^
In level 2 => 2^1^
In level 3 => 2^2^
.
.
.
In level x => 2^x-1^

The last is Nth level, hence x = N.

Total function calls are -
2^0^ + 2^1^ + 2^2^ + 2^3^ + ....... + 2^N-1^
This is sum of GP, a=1, r=2, #terms = N

Formula = a(r^#terms^ - 1) / (r-1)
        = 1(2^N^ - 1) / (2-1)
        = O(2^N^)



### S.C

Space complexity is the maximum amount of stack space used by the algorithm.

When a function is called, it is added to the stack.
When a function returns, it is popped off the stack.

We’re not adding all of the function calls to the stack at once.
We only make n calls at any given time as we move up and down branches.

We proceed branch by branch, making our function calls until our base case is met, then we return and make our calls down to the next branch.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/164/original/fibnocci_compexity.png?1706036686" width=500/>

Hence, at a time at max calls = height of the tree, will be present in stack, hence space complexity is O(N) for fibonacci.

#### Emulation of space for Fibonacci(3) using stack

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/065/197/original/Screenshot_2024-02-15_at_1.05.24_PM.png?1707982536" width=500 />


