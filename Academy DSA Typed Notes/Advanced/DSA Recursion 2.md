# Recursion 2

## Revision Quizzes

### Question
What is recursion ?

### Choices

- [ ] A function that calls itself
- [ ] A function that calls another function
- [ ] A loop that repeats until a condition is met
- [x] A function that solves a problem by breaking it into smaller subproblems and calling itself

---



### Question
What data structure is used for function call tracing in recursion?

### Choices
- [ ] Queue
- [ ] Linked List
- [x] Stack
- [ ] Array

---

### Question
 Which of the following is the base case for calculating the factorial of a number using recursion?


### Choices
- [ ] N == 2
- [x] N == 0
- [ ] N == 1
- [ ] N == -1

---


### Question
What is the time and space complexity for calculating factorial using recurion ?


### Choices
- [x] O(N), O(N)
- [ ] O(N), O(1)
- [ ] O(1), O(N)
- [ ] O(N), O(log(N))

---


### Question
To compute Fibonacci(N) you need answers of ?


### Choices

- [ ] fibonacci(N - 1)
- [ ] Fibonacci(N - 2)
- [x] Fibonacci(N - 1) and Fibonacci(N - 2)
- [ ] none


---
## Agenda

* Power Function
* Print array
* Indices of an Array
* Check palindrome

---
## Problem 1 Power Function


### Problem Statement

Given two integers **a** and **n**, find **a<sup>n</sup>** using recursion.

### Input
```
a = 2
n = 3
```
### Output
```
8
```
### Explanation
2<sup>3</sup> i.e, 2 * 2 * 2 = 8.


### Brute Force Approach
The above problem can be redefined as:
```
a ^ n = a * a * a......* a (n times).
```
The problem can be broken into subproblem as:
```
a ^ n = a ^ (n-1) * a
```
So we can say that pow(a,n) is equivalent to
```
pow(a,n) = pow(a,n-1) * a
```
Here, pow(a,n) is the defined as `a^n`.
We have seen how the problem is broken into subproblems. Hence, it can be solved using recursion.
Below is the algorithm:
* Assumption step:
    * Define a recursive function pow(a,n). 
* Main Logic:
    * Define a recursive case: if **n** > 0, then calculate the pow(a,n-1).
    * Return a * pow(a,n-1).
* Base Case:
    * Base condition: if **n** = 0, then return 1.
### Pseudocode
```
function pow(int a, int n){
    if(n == 0) return 1;
    return a * pow(a,n-1);
}
```

### Complexity

Recursive Tree for 5^3^
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/065/205/original/Screenshot_2024-02-15_at_2.56.26_PM.png?1707989370" width=500 />

#### T.C

Number of calls = N+1
Work done in each call = O(1)
Total T.C = O(N)

#### S.C

The height of the tree is N, hence the S.C = O(N)

---
## Power Function Another Approach

### Optimized Approach 1
We can also divide pow(a, n) as follows:
if **n** is even:
```
pow(a,n) = pow(a,n/2) * pow(a,n/2)
```
if **n** is odd:
```
pow(a,n) = pow(a,n/2) * pow(a,n/2) * a
```
### Recursion Steps:
* Assumption Step:
    * Define a recursive function pow(a,n).
* Main Logic:
    * if n is odd, then return pow(a,n/2) * pow(a,n/2) * a.
    * else return pow(a,n/2) * p(a,n/2).
* Base Condition:
    *  if **n** is equal to 0, then return 1.

### Pseudocode
```
Function pow(int a, int n){
    if(n == 0) return 1;
    
    if(n % 2 == 0) {
        return pow(a,n/2) * pow(a,n/2);
    }
    else {
        return pow(a,n/2) * pow(a,n/2) * a;
    }
}
```
The above function will have more time complexity due to calling the same function twice. We will see it while calculating Time Compleixity.

### Complexity

Recursive Tree -

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/065/206/original/Screenshot_2024-02-15_at_2.59.03_PM.png?1707989421" width=250 />

#### T.C

At level 1, the number of nodes are 2^0^
At level 2, the number of nodes are 2^1^
At level 3, the number of nodes are 2^2^
.
.
.
At level x, the number of nodes are 2^x-1^

Here, if we see one path from root to leaf, then reduction happens as n -> n/2 -> n/4 -> ... 1 which means height of the tree is log N.
x = log N **or** N = 2^x^

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/065/207/original/Screenshot_2024-02-15_at_2.59.13_PM.png?1707989428" width=450 />

Total calls are - 
2^0^ + 2^1^ + 2^2^ + ...... + 2^x-1^
This is sum of GP, a=1, r=2, #terms = x

Formula = a(r^#terms^ - 1) / (r-1)
        = 1(2^x^ - 1) / (2-1)
        = 2^x^ = N 

Time taken by each call = O(1)
Total Time Complexity = O(N)

#### S.C

The height = S.C is O(log N)

---
## Power Function Optimized Approach - Fast Power


In above approach, we are calling function **pow(a, n/2)** twice. Rather, we can just call it once and use the result twice. 
Below is the algorithm:
* Assumption Step:
    * Define a recursive function **pow(a,n)**.
* Main Logic:
    * Calculate **pow(a,n/2)** and store it in a variable **p**.
    * if n is odd, then return **p * p * a**.
    * else return **p * p**.
* Base Condition:
    *  if **n = 0**, then return **1**.

### Pseudocode
```
Function pow(int a, int n){
    if(n == 0) return 1;
    
    int p = pow(a, n/2);
    
    if(n % 2 == 0) {
        return p * p;
    }
    else {
        return p * p * a;
    }
}
```
> Note: The above function is known as Fast Power or Fast Exponentiation.

### Complexity

Recursive Tree -

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/065/208/original/Screenshot_2024-02-15_at_3.04.25_PM.png?1707989674" width=400 />

#### T.C
The number of calls are log N
Time taken by each call is O(1)
Total T.C = O(log N)

#### S.C
The height = S.C is O(log N)

---
## Problem 2 Print array using recursion


### Problem Statement

Given an array of integers, write a recursive function to print all the elements of the array.

Example

Input:
`A = [1, 2, 3, 4, 5]`

Output:
`1 2 3 4 5`

### Approach
To print an array using recursion:

- Base Case: If the index is equal to the size of the array, then return.
- Print the element corresponding to the index.
- Recursively call the function by incrementing the index by 1.


### Pseudocode

```python
function printArray(arr, index):
    if n == arr.size():
        return
    print arr[index]
    printArray(arr, index + 1)
```


### Complexity Analysis
Time Complexity: O(n), where n is the size of the array.

---

### Question

To find the **sum of the array** using recursion, what is the Recursive state to be used ?
**Tip:** We have used `max(arr[index], findMax(arr, index + 1))` to find the maximum of the array.

### Choices
- [x] arr[index] + findSum(arr, index + 1)
- [ ] max(arr[index], findSum(arr, index + 1))
- [ ] arr[index] + max(arr[index], findSum(arr, index + 1))
- [ ] arr[index] - findSum(arr, index + 1)


### Explanation:

For finding the maximum of the array, our goal on each step is to compare two elements, one is the current element and another one is the maximum of the remaining array.

The same idea goes for sum of the array also,  here our goal on each step is to return the sum of two numbers, one is the current number and another one is the sum of the remaining array.

The entire pseudo code will look as follows,

```javascript
function findSum(arr, index):
    if index == arr.size() - 1: 
        return arr[index]
    return arr[index] + findSum(arr, index + 1))
```

---
## Problem 3 All Indices Of Array


### Problem Statement

Given an array of integers A with N elements and a target integer B, the task is to find all the indices at which B occurs in the array.

It is guaranteed that the target B, exist atleast once in the Array A.

### Example

Input : 
```
A = [4, 5, 3, 1, 5, 4, 5]
B = 5
```

Output : 
```
[1, 4, 6]
```


---


### Question
Find all the Indices at which B occurs in the given array, A:

```
A = [1, 2, 3, 1, 1]
B = 1
```
### Choices
- [ ] [1, 2, 4] 
- [ ] [0, 1, 2, 3, 4]
- [ ] [1, 5]
- [x] [0, 3, 4]

---
## All Indices Of Array Observation


### Observation

Here we don't know about size of the array beforehand. So, in our function, we shall be taking a variable "cnt", to track the number of B found so far so that we can create a new array(with cnt size) in base case and return it.

Now, on our way back from recursion, we can keep filling the elements in array.

Hence, to solve this problem using recursion, we will include two additional variables in the recursive call: 
* one to track the **index of the current element** and 
* another to **count the occurrences** of the target integer.

**Recursive Function**:
**`recur(A, B, index, cnt)`**

### Steps

1. **Assumption:** **`recur(A, B, index, cnt)`** return an array with indices where B is found from index till end.
2. **Main Logic:** We can break the problem for 2 different cases -
    *  When B is present at index
        *   **`recur(A, B, index+1, cnt+1)`**
    *  When B is not present
        *   **`recur(A, B, index+1, cnt)`**
3. **Base Case:**
```
if(index == N) {
    return new ans[cnt]
}
```

### Dryrun

Input: 
```
A = [1, 2, 3, 2, 4, 4, 2]
B = 2
```

Initial Call -> (A, B, 0, 0)

|call no. | A | B | A[index] | recurive call |
|--|---|---|--| --|
|1 | A | B | A[0] = 1 | (A, B, index=1, count=0) |
|2 | A | B | A[1] = **2**(found)|(A, B, index=2, count=1) |
|3 | A | B | A[2] = 3|(A, B, index=3, count=1) |
|4 | A | B | A[3] = **2**(found)|(A, B, index=4, count=2) |
|5 | A | B | A[4] = 4|(A, B, index=5, count=2) |
|6 | A | B | A[5] = 4|(A, B, index=6, count=2) |
|7 | A | B | A[6] = **2**(found)|(A, B, index=7, count=3) 

When **`index reaches 7`**, we **`create array of size=3(count)`**, and **`return ans[3]`**
`ans = [0, 0, 0]`

While coming back from recursion, in call number 2, 4, 7, the ans array will get updated
1. Call Number 2, update ans[0] = 1
2. Call Number 4, update ans[1] = 3
3. Call Number 7, update ans[2] = 6

---
## All Indices Of Array Pseudo code


### Pseudo code

```java
int[] recur(int[] A, int B, int index, int count) {
    if (index == A.length)
        return new int[count];

    if (A[index] == B){
        int[] ans = recur(A, B, index + 1, count + 1);
        ans[count] = idx;
    }
    else {
        int[] ans = recur(A, B, index + 1, count);
    }
    
    return ans;
}
```

---
## Problem 4 Check palindrome using recursion


### Problem Statement
Given a string, write a recursive function to check if it is a palindrome.

### Example

Input:
str = "radar"

Output:
True

Input:
str = "area"

Output:
False


### Observation

To ensure a string is a palindrome, each pair of characters symmetrically positioned around the center must match.


Lets keep to pointers, one on the left and another on the right.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/075/822/original/Screenshot_2024-06-01_at_8.40.24_PM.png?1717254638" width="200"/>

Here the last checking can be ignored by using (left_pointer < right_pointer).


### Dry Run

Lets breakdown the problem into smaller subproblem.

To ensure a string is palindrome,  the first and the last character has to be same and the remainging string also has to be palindrome.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/075/824/original/Screenshot_2024-06-01_at_8.39.38_PM.png?1717254679" width=300 />

Here pali(str, left + 1, right - 1) is the recursive step.

We check the characters recursiving by incrementing the left pointer and decrementing the right pointer.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/075/823/original/Screenshot_2024-06-01_at_8.39.47_PM.png?1717254671" width=400 />


When the left and right pointers meets the center, then the recusion has to stop and return True.  

Since all the characters around the center has a match.

The base case will be

```python 
if left >= right:
    return True
```


### Approach (in short)
To check if a string is a palindrome using recursion:

- Base Case: If left >= right then return True.
- Compare the left and right characters of the string.
- Recursively check if the substring excluding the first and last characters is a palindrome

---
## Check Palindrome Using Recursion Pseudo Code


### Pseudocode

```python
function isPalindrome(str, left, right):
    if left >= right:
        return True
    if str[left] != str[right]:
        return False
    return isPalindrome(str, left+1, right-1)
```

### Complexity Analysis
Time Complexity: O(n), where n is the length of the string.

---


### Question
What is the output of the following code for N = 3?
```cpp
void solve(int N){
    if(N == 0)
        return;
    print(N);
    solve(N-1);
    print(N);
}
```

### Choices

- [x] 3 2 1 1 2 3
- [ ] 3 2 1 0
- [ ] 1 2 3 3 2 1
- [ ] 1 2 3


### Explanation

First we start at N=3, print(3)
go to N=2, print(2) 
go to N=1, print(1)
go to N=0, return
come back to N=1, print(1)
come back to N=2, print(2)
come back to N=3, print(3)

Hence the output is 3 2 1 1 2 3

---


### Question
What is the output of the following code for N = -3?
```cpp
void solve(int N){
    if(N == 0)
        return;
    print(N);
    solve(N-1);
}
```

### Choices

- [ ] -3 -2 -1
- [ ] 3 2 1
- [x] Error; Stack Overflow
- [ ] 1 2 3


### Explanation

In this question we will never reach 0, and get stack overflow.
At first solve(-3) is called, then it will print -3 
call for solve(-4), then it will print -4 
call for solve(-5), in this way, it will keep making calls infinitely, as we will not reach zero, hence stack overflow error occurs.

