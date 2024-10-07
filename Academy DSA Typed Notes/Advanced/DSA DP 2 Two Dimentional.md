# DP 2: Two Dimensional

## Problem 1 House Robber
### Problem Statement:
Given an integer array nums, where each element represents the amount of money in a house, determine the maximum amount of money you can rob without triggering an alarm. The constraint is that you cannot rob two adjacent houses (i.e., you cannot rob house i and house i+1 together).

**Example 1**:
Input: nums = [1, 2, 3, 1]
Output: 4
**Explanation**:
- Rob house 1 (money = 1) and house 3 (money = 3).
- Total amount = 1 + 3 = 4.

**Example 2**:
Input: nums = [2, 7, 9, 3, 1]
Output: 12
**Explanation**:

- Rob house 1 (money = 2), house 3 (money = 9), and house 5 (money = 1).
- Total amount = 2 + 9 + 1 = 12.

**Step-by-Step Breakdown**:
### Brute Force Approach (Inefficient):

**Idea**: Recursively explore all subsets of houses by either robbing or skipping each house, and calculate the maximum amount you can rob.
**Steps**:
- For each house, you can choose to:
1.Rob the house and skip the next one.
2.Skip the house and move to the next one.
- Recursively compute the maximum amount of money that can be robbed.
**Complexity**:  O(2^n)
 
**Flaws**:
 - The brute force approach becomes extremely slow as the number of houses increases due to redundant calculations.
 
## Problem 1 House Robber Optimised Approach
###  Optimized Approach Using Dynamic Programming (DP):

**Key Insight**: 
For each house, you can either:
1. Rob it and add its value to the total amount robbed from all non-adjacent previous houses.
2. Skip it and take the maximum amount robbed from the previous house.

**State Transition**:
- Let dp[i] represent the maximum amount of money that can be robbed from the first i houses.
- **For each house i**:
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
- This means: either take the maximum amount up to the previous house dp[i-1], or rob the current house nums[i] and add the value from the non-adjacent house dp[i-2].


**Optimized Solution Pseudocode (Dynamic Programming Approach):**

``` cpp function rob(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    # Initialize base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Fill the dp array for each house
    for i from 2 to len(nums) - 1:
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

    # Return the maximum amount possible, which is dp[n-1]
    return dp[len(nums) - 1]
```
    
### Complexity Analysis:
**Time Complexity**: O(n)
**Space Complexity**:
- The DP approach uses O(n) space to store the dp array.
- The space-optimized version uses O(1) space, as it only maintains two variables.

---
## Problem 2 Count Unique Paths

### Problem Statement
Given mat[n][m], find total number of ways from (0,0) to (n - 1, m - 1). We can move 1 step in horizontal direction or 1 step in vertical direction.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/332/original/upload_cb3858a3235bba18e6037c9699d300f3.png?1695530323a" width=400 />


### Example

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/333/original/upload_44295f53f281281555a9264d2acee1d4.png?1695530363" width=400 />


> `h` represents movement in horizontal direction and `v` represents movement in vertical direction

**Ans:** 6 



---


### Question
Find the total number of ways to go from (0, 0) to (1, 2)

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/087/788/original/a.png?1724856036" width=400/>



### Choices
- [ ] 1
- [ ] 2
- [x] 3
- [ ] 4


### Explanation:

The 2D matrix dp is

|   | 0 | 1 | 2 |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 1 | 1 | 2 | 3 |

From here, the number of ways to go from (0, 0) to (1, 2) is 3.


---
## Count Unique Paths Brute Force Approach

### Brute Force Appoarch
**Backtracking**, i.e., start from (0, 0) and try all possible scenarios to reach (n - 1, m - 1)

### Observation
Can we break it into subproblems?
- We can reach (n - 1, m - 1) in one step (by moving vertically) from (n - 2, m - 1)
- We can reach (n - 1, m - 1) in one step (by moving horizontally) (n - 1, m - 2)

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/334/original/upload_3fc7c3e0b6a26618888979ff3b4bfa4a.png?1695530388" width=500 />



### Recursive Relation

**ways(i, j) = ways(i - 1, j) + ways(i, j - 1)**

### Base Condition
- When i == 0, we have only one path to reach at the end, i.e., by moving vertically.
- Similary, when j == 0,  we have only one path to reach at the end, i.e., by moving horizontally.

Therefore, **ways(0, j) = ways(i, 0) = 1**

### Pseudocode:
```java
function ways(i, j) {
    if (i == 0 || j == 0) {
        return 1;
    }
    return ways(i - 1, j) + ways(i, j - 1);
}
```

Time Complexity: O(2 ^ (N * M)), as at every step we have two options, and there are total of N * M cells.


## Count Unique Paths Optimization

### Optimization using DP

We can see the **optimal substructure** in this problem as it can be defined in terms of smaller subproblems.

**Are there overlapping subproblems as well?**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/335/original/upload_6c4137711a6c49b0ed6def7c230fc475.png?1695530519" width=400 />


We can see that, `(i - 1, j - 1)` are the overlapping subproblems.

***Since there is optimal substructure and overlapping subproblems, DP can be easily applied.***

*Which type of array should be used?*
Since two args (i and j) are varying in above method, 2-d storage is needed of size N x M.

### Top Down Approach

**`dp[i][j] = It is defined as the total ways to reach from 0,0 to i,j`**

### Pseudocode
```java
dp[N][M]; // initialized with -1
function ways(i, j) {
    if (i == 0 || j == 0) {
        return 1;
    }
    
    if (dp[i][j] != -1) {
        return dp[i][j];
    }
    ans = ways(i - 1, j, dp) + ways(i, j - 1, dp);
    dp[i][j] = ans;
    return ans;
}
```
### Complexity
**Time Complexity:** O(N * M), as we are filling a matrix of size N * M.
**Space Complexity:** O(N * M), as we have used dp matrix of size N * M.

> *In how many ways can we reach (0, 0) starting from (0, 0)?*
> 
> If you say 0, that means there is no way to reach (0, 0) or (0, 0) is unreachable. Hence, to reach (0, 0) from (0, 0), there is 1 way and not 0.

### Bottom Up Approach:
Consider a 2D matrix `dp` of size N * M.
`dp[i][j] = It is defined as the total ways to reach from 0,0 to i,j`

In bottom up approach, we start from the smallest problem which is (0, 0) in this case.
- No. of ways to move (0, 0) from (0, 0) = ways(0, 0) = 1
- Similarly, ways(0, 1) = ways(0, 2) = . . . = 1
- Also, ways(1, 0) = ways(2, 0) = . . . = 1
- Now, ways(1, 1) = ways(1, 0) + ways(0, 1) = 2
- Similarly, ways(1, 2) = ways(1, 1) + ways(0, 2) = 3, and so on.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/336/original/upload_91d6c51f6c8e74ac6934f9096ed1e7d2.png?1695530605" width=500 />

### Pseudocode
```java
dp[N][M];
// Initialize `dp` row - 0 and col - 0 with 1.
for (i = 1; i <= N; i++) {
    for (j = 1; j <= M; j++) {
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
}
return dp[N - 1][M - 1];
```

Time Complexity: O(N * M)
Space Complexity: O(N * M)


### Can we further optimize the space complexity?

- The answer of every row is dependent upon its previous row.
- So, essentially, we require two rows at a time - (1) current row (2) previous row. Thus, the space can be optimized to use just two 1-D arrays.


---
## Problem 3 N digit numbers
### Problem Statement:
You are tasked with finding how many A-digit positive numbers exist, such that the sum of their digits equals B. A valid number does not contain leading zeros (i.e., the first digit must be between 1 and 9). Since the answer can be large, return the result modulo 10^9+7 (1000000007).

**Example 1**:
Input: A = 2, B = 4
Output: 4
**Explanation**:

- Valid numbers with 2 digits whose sum is 4 are: {22, 31, 13, 40}.
- Hence, the output is 4.

**Example 2**:
Input: A = 1, B = 3
Output: 1
**Explanation**:

- The only valid 1-digit number whose sum is 3 is 3.

**Step-by-Step Breakdown**:
### Brute Force Approach (Inefficient):

**Idea**: Generate all possible A-digit numbers, check each number to see if the sum of its digits equals B.
**Steps**:
- Iterate through all possible A-digit numbers.
- For each number, calculate the sum of its digits and check if it equals B.
- Count all valid numbers.
**Time Complexity**: O(9^A)

**Flaws**:

- This approach is inefficient for larger values of A since it involves generating many numbers and checking each one.



## Problem 3 N digit numbers Optimized Approach

### Optimized Approach Using Dynamic Programming (DP):
**Key Insight**: Instead of generating all numbers, we can use dynamic programming to efficiently count valid numbers. We can build the solution step by step by keeping track of the sum of digits at each step.

**State Definition**:

- Let dp[i][j] represent the number of valid i-digit numbers whose digit sum equals j.
Our goal is to calculate dp[A][B].

**State Transition**:

- For each i (number of digits so far) and each j (current sum of digits), we add a new digit d (ranging from 0 to 9) and update the state:
dp[i][j] += dp[i-1][j-d]
- This means: for each number with i-1 digits whose sum is j-d, we can form a new number by adding a digit d to it, resulting in an i-digit number whose sum is j.

**Base Case**:

- dp[1][sum] = 1 for all valid sums where 1 ≤ sum ≤ 9, because there is exactly one 1-digit number for each sum.

**Optimized Solution Pseudocode (DP Approach)**:

``` cpp function countValidNumbers(A, B):
    MOD = 1000000007
    
    # Initialize dp array: dp[i][j] represents the number of valid i-digit numbers with digit sum j
    dp = array of size [A + 1][B + 1] initialized to 0
    
    # Base case: For 1-digit numbers
    for d from 1 to 9:
        if d <= B:
            dp[1][d] = 1  # There's exactly one way to get a sum of d with one digit

    # Fill dp array
    for i from 2 to A:  # Iterate through digit counts
        for j from 0 to B:  # Iterate through sums
            for d from 0 to 9:  # Try adding each digit d
                if j - d >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-d]) % MOD

    # Return the result for A digits and sum B
    return dp[A][B]
    
```
**Explanation:**
**Base Case**:

- For i = 1 (1-digit numbers), dp[1][d] = 1 for all d from 1 to 9. This initializes the base case where there is exactly one way to form a 1-digit number for each sum d.

**Transition**:

- For each digit count i (from 2 to A), and each sum j (from 0 to B), we check all possible new digits d (from 0 to 9).
- If adding digit d to a number whose sum was j-d forms a valid i-digit number, we update the count of valid numbers for i digits and sum j.

**Result**:

- The final answer is stored in dp[A][B], which gives the number of valid A-digit numbers with a digit sum of B.

### Time Complexity Analysis:
**Time Complexity**: O(A×B×10).
**Space Complexity**: O(A×B).

### Catalan Numbers

The Catalan numbers form a sequence of natural numbers that have numerous applications in combinatorial mathematics. Each number in the sequence is a solution to a variety of counting problems. The Nth Catalan number, denoted as Cn, can be used to determine:

* The number of correct combinations of N pairs of parentheses.
* The number of distinct binary search trees with N nodes, etc.

Here is the sequence, 
```
C0 = 1
C1 = 1
C2 = C0 * C1 + C1 * C0 = 2
C3 = C0 * C2 + C1 * C1 + C2 * C0 = 5
C4 = C0 * C3 + C1 * C2 + C2 * C1 + C3 * C0 = 14
C5 = C0 * C4 + C1 * C3 + C2 * C2 + C3 * C1 + C4 * C0 = 42
```

### Formula

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/800/original/catalan-formula.jpg?1706639109" width = 500 />

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/799/original/catalan.jpg?1706639038" width = 500 />


### Psuedo Code

```cpp
declare array C[N + 1];

C[0] = 1;
C[1] = 1;

for(i -> 2 to N)
{
    for(j -> 0 to i - 1)
    {
        C[i] += C[j] * C[N - 1 - j];
    }
}
```

### Complexity

**Time Complexity:** O(N^2^)
**Space Complexity:** O(N) 

Now, Let's look into a problem, which can be solved by finding the **Nth catalan number**.


---
## Problem 4 Total Number of Unique BSTs

### Problem Statement

You are given a number N, Count Total number of Unique Binary Search Trees, that can be formed using N distinct numbers.

### Example

**Input:**
N = 3

**Output:**
5

**Explanation:**

The Unique binary Search Trees are
```
      30      10           30     10          20
     /         \          /        \         /  \ 
   10           20       20        30       10  30
    \            \       /         /
    20           30     10        20
```

---


### Question
Count Total number of Unique Binary Search Trees, that can be formed using 2 distinct numbers

### Choices
- [ ] 1
- [x] 2
- [ ] 5
- [ ] 4


### Explanation:

Let's take 2 distinct numbers as [10, 20]

The possible BSTs are
```
    20       10 
   /          \
  10           20 
```
---

### Total Number of Unique BSTs Dryrun
Let's take N = 5, the numbers are [10, 20, 30, 40, 50].

Let's keep each number as the root! one by one.

**10 as root**
```
        10
          \
           \
            \
          20, 30, 40, 50
```

Here we notice that, 20, 30, 40 and 50 will be present on right side of 10. With these 4 nodes, we can create further BSTs, let's denote by C4

Also on the right side, there is no elements. So denoting by C0.

With `10 as root, the total number of BSTs => C0 * C1`


**20 as root**
```
        20
      /   \
     /     \
    /       \
  10      30, 40, 50
```

There are 1 element on the left side and 3 elements on the right side.

`20 as root => C1 * C3`


**30 as root**
```
        30
       /  \
      /    \
     /      \
  10, 20    40, 50
```


There are 2 element on the left side and 2 elements on the right side.


`30 as root => C2 * C2`


**40 as root**
```
             40
            / \
           /   \
          /     \
   10, 20, 30    50
```


There are 3 element on the left side and 1 elements on the right side.


`40 as root => C0 * C1`

**50 as root**
```
             50
            / 
           /   
          /    
  10, 20, 30, 40
```

There are 4 element on the left side and 1 elements on the right side.


`10 as root => C4 * C0`

C5 = C0 * C4 + C1 * C3 + C2 * C2 + C3 * C1 + C4 * C0

which is 42.

### Solution

The Solution for finding the total number of Unique BSTs is the **Nth Catalan Number**.


## Total Number of Unique BSTs Pseudo Code

### Psuedo Code

The pseudo code is same as the Catalan Number Psuedo code.

```cpp
function findTotalUniqueBSTs(N){
    declare array C[N + 1];

    C[0] = 1;
    C[1] = 1;

    for(i -> 2 to N)
    {
        for(j -> 0 to i - 1)
        {
            C[i] += C[j] * C[N - 1 - j];
        }
    }

    return C[N];
}    
```

### Complexity

**Time Complexity:** O(N^2^)
**Space Complexity:** O(N) 

---
