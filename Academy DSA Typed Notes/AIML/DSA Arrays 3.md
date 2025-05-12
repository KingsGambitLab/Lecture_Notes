# DSA: Arrays 3

## Problem 1 Find Maximum Subarray Sum

### Problem Statement

As a cryptocurrency trader, you have a unique advantage: access to predicted data that outlines the daily price changes of a specific cryptocurrency for the next **N** days. Your goal is to maximize your profit based on these predictions. 

You are provided with an array **A** consisting of **N** integers, where each integer represents the predicted change in the crypto's price for that day. A positive value indicates a profit (the price goes up), while a negative value indicates a loss (the price goes down). The total profit or loss you can make is determined by the sum of the daily price changes for the period you choose to hold onto the crypto.

Your goal is to Determine the maximum profit you can achieve, under the condition that you must buy before you can sell. 

**Example**:
For the given array A with length N,  

| Index |  0  |  1  |  2  |  3  |  4  |  5  |  6  |
|:-----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Profit/Loss array **A** | -20  |  30  |  40  | -10  |  50  | -100 |  70  |

**Output:** 
```plaintext
Max Profit: 110
Hold on to the crypto for profits : 30 40 -10 50
```

**Explanation**
If you buy the stock just before day 1 (index 1) and hold on to the stock for day 4 (index 4), you will see that the sum of total profit / loss = 30 + 40 + (-10) + 50 = 110. 


### Short conclusive Problem Statement
Given an integer array A, find the maximum subarray sum out of all the subarrays.

### How is it the same problem ?
Both problems revolve around finding the maximum sum of a contiguous subarray within an array. In the context of cryptocurrency trading, this corresponds to finding the sum of elements (profits/losses) incurred by cryptocurrency at different prices over consecutive days.

### Examples
**Example 1**:
For the given array A with length N,

| Index |  0  |  1  |  2  |  3  |  4  |  5  |  6  |
|:-----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Array | -2  |  3  |  4  | -1  |  5  | -10 |  7  |

**Output:** 
```plaintext
Max Sum: 11
Subarray: 3 4 -1 5
```


**Example 2:**
For the given array A with it's length as N we have,

| Index |  0  |  1  |  2  |  3  |  4  |  5  |  6  |
|:-----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Array | -3  |  4  |  6  |  8  | -10 |  2  |  7  |

**Output:**
```plaintext
Max Sum: 18
Subarray: 4 6 8
```

---
### Question
For the given array A, what is the maximum subarray sum ? 
A[ ] = { 4,  5,  2,  1,  6  }

### Choices
- [ ] 6
- [x] 18
- [ ] No Idea
- [ ] 10

### Explanation

```plaintext
Max Sum: 18
Subarray: 4 5 2 1 6
```

---
### Question

For the given array A, what is the maximum subarray sum ? 
A[ ] = { -4, -3, -6, -9, -2 }

### Choices
- [ ] -9
- [ ] 18
- [x] -2
- [ ] -24

### Explanation

```plaintext
Max Sum: -2
Subarray: -2
```
---

## Brute Force
No of possible subarrays: `N * (N + 1) / 2`

Iterate over all subarrays, calculate sum and maintain the maximum sum.

### Psuedocode:
```java
ans = A[0];
for (i -> 0 to N - 1) { // start to N
    for (j -> i to N - 1) { // end
        for (k -> i to j) {
            sum += A[k];
        }
        ans = Math.max(ans, sum);
        sum = 0; // Reset sum for the next iteration
    }
}
return ans;
```

### Complexity
**Time Complexity:** `O(N^2 * N) = O(N^3)`
**Space Complexity:** `O(1)`


## Find Maximum Subarray Sum using Carry Forward

### Optimized Solution using Carry Forward
We don't really need the third loop present in brute force, we can optimise it further using Carry Forward technique.

### Psuedocode
```java
ans = A[0]
for(i = 0 to N - 1){ //start to N
    sum = 0
    for(j = i to N - 1){ //end
        sum += A[k]
        ans = max(ans, sum)
    }
}
return ans;
```

### Complexity
**Time Complexity:**  O(N^2)
**Space Complexity:** O(1)

## Find Maximum Subarray Sum using Kadanes Algorithm

### Observation:

**Case 1:**
If all the elements in the array are positive
Arr[] = `[4, 2, 1, 6, 7]`

**Answer:**
To find the maximum subarray we will now add all the positive elements
Ans: `(4 + 2 + 1 + 6 + 7) = 20`


**Case 2:**

If all the elements in the array are negative 
Arr[] = `[-4, -8, -9, -3, -5]`

**Answer:**
Here, since a subarray should contain at least one element, the max subarray would be the element with the max value
Ans: `-3`


**Case 3:**

If positives are present in between
Arr[] = [-ve -ve -ve `+ve +ve +ve +ve` -ve -ve -ve]

**Answer:**
Here max sum would be the sum of all positive numbers 


**Case 4:** 
If all negatives are present either on left side or right side.
Arr[ ] = [-ve -ve -ve `+ve +ve +ve +ve`]
OR
Arr[ ] = [`+ve +ve +ve +ve` -ve -ve -ve -ve]

**Answer:**
All postives on sides



Case 5 :
### Hint:
What if it's some ve+ followed by some ve- and then again some more positives...

```plaintext
+ve +ve +ve -ve -ve -ve +ve +ve +ve +ve +ve
```

### Solution:
We will take all positives, then we consider negatives only if the overall sum is positive because in the future if positives come, they may further increase this positivity(sum).



**Scenario:**
Say you recently got committed. Your partner did something wonderful for you and you are so happy about it.

The other day, they kept your message on seen and didn’t reply. What will happen to your happiness level?
It’ll reduce a bit or you will start hating that person? Happiness level ve - ? 
It will reduce a bit, some positivity in relationships still exists.*


*The other day, they showered you with flowers and quality time, so now can we say that your bond is even stronger and happiness level is even higher than the first day ?*



**Example** -
```plaintext
A[ ] = { -2, 3, 4, -1, 5, -10, 7 }
```
Answer array: 3, 4, -1, 5


**Explanation**:
3+4 = 7
7 + (-1) = 6 (still positive)
6+5 = 11 (higher than 7)

### Dry Run
```plaintext
    0   1    2    3  4  5   6  7   8
{ -20, 10, -20, -12, 6, 5, -3, 8, -2 }
```

|  i  | currSum | maxSum |                                                                                                                                                              |
|:---:|:-------:|:------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|  0  |   -20   |  -20   | reset the currSum to 0 and do not propagate since adding a negative will make it more negative and adding a positive will reduce positivity of that element. |

currSum = 0

|  i  |    currSum    | maxSum |                    |
|:---:|:-------------:|:------:|:------------------:|
|  1  |      10       |   10   |                    |
|  2  | 10 + (-20)= -10 |   10   | reset currSum to 0 |



currSum = 0

|  i  | currSum | maxSum |                    |
|:---:|:-------:|:------:|:------------------:|
|  3  |   -12   |   10   | reset currSum to 0 |



currSum = 0

|  i  |  currSum  | maxSum |                                                                             |
|:---:|:---------:|:------:|:---------------------------------------------------------------------------:|
|  4  |     6     |   10   |                                                                             |
|  5  |    6 + 5    |   11   |                                                                             |
|  6  | 6 + 5 - 3 = 8 |   11   | Keep currSum as 8 only since if we find a positive, it can increase the sum |

|  i  | currSum | maxSum |                                                                             |
|:---:|:-------:|:------:| --------------------------------------------------------------------------- |
|  7  | 8 + 8 = 16  |   16   |                                                                             |
|  8  | 16 - 2 = 14 |   16   | Keep currSum as 8 only since if we find a positive, it can increase the sum |

Final maxSum = 16

---
### Question
Tell the output of the below example after running the Kadane's Algorithm on that example
A[ ] = { -2, 3, 4, -1, 5, -10, 7 }

### Choices
- [ ] 9
- [ ] 7
- [x] 11
- [ ] 0

---

### Pseudocode

```cpp
function maximumSubarraySum(arr[], n) {
       maxSum = -infinity;
       currSum = 0;

       for (i -> 0 to n - 1) {
           currSum += arr[i];

           if (currSum > maxSum) {
           maxSum = currSum;
           }

           if (currSum < 0) {
           currSum = 0;
           }
       }

       return maxSum;
   }
```

### Complexity
**Time Complexity:**  O(n)
**Space Complexity:** O(1)

The optimized method that we just discussed comes under **Kadane's Algorithm** for solving maximum subarray problem


---
## Problem 2 Find in rowwise and colwise sorted matrix

### Problem Statement
Given a row wise and column wise sorted matrix, find out whether element **k** is present or not.

### Example
Observe that rows and columns are both sorted.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/573/original/Screenshot_2023-09-25_at_3.51.10_PM.png?1695652091" width=300 />

### Test Case 1
13 => Present (true)

### Test Case 2
2 => Present (true)

### Test Case 2
15 => Not Present (false)

---
### Question
What is the brute force approach and the time complexity of it?

### Choices
- [ ] Iterate over first row; T.C - O(M)
- [ ] Iterate over last col; T.C - O(N)
- [x] Iterate over all rows & cols; T.C - O(N * M)
- [ ] Iterate over first col; T.C - O(N)

---
## Find in rowwise and colwise sorted matrix Optimised Approach

### Idea
* We shall exploit the property of the matrix being sorted.
* Start with the cell from where we can decide the next step.
**Example:** 
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/662/original/Screenshot_2023-09-25_at_8.07.35_PM.png?1695706871" width=250 />
Search for: 0

Say we stand at **top left cell i.e, -5**.
Now, **-5 < 0**, can we determined the direction to search based on this?
No, because on rightside as well as downwards, the elements are in increasing order, so 0 can be present anywhere.

Now, say we stand at **top right cell i.e, 13**.
Now,**13 > 0**, should we go left or down ? Can we decide ?
Yes, if we move down the elements are > 13, but we are looking for an element < 13, so we should move left.

It means, all elements below 13, can be neglected.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/664/original/Screenshot_2023-09-25_at_8.08.43_PM.png?1695707082" width=50 />

**Move Left**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/665/original/Screenshot_2023-09-26_at_11.14.03_AM.png?1695707132" width=150 />

Now, where shall we move ?

---
### Question
Say we are at 1 and want to find 0, where should we move ?

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/662/original/Screenshot_2023-09-25_at_8.07.35_PM.png?1695706871" width=250 />

### Choices
- [x] left
- [ ] bottom
- [ ] let's move in both the directions
- [ ] let's move everywhere

---
## Optimised Approach (Continued)

Since, **1 > 0**, again all elements below 1 are greater than 1, hence can be neglected.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/667/original/Screenshot_2023-09-25_at_8.09.08_PM.png?1695707195" width=150 />

**Move Left**
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/670/original/Screenshot_2023-09-26_at_11.17.20_AM.png?1695707280)" width=250 />

Now, **-2 < 0**, all elements on left of -2 are lesser than -2, hence can be neglected.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/672/original/Screenshot_2023-09-25_at_8.09.29_PM.png?1695707327" width=300 />

**Move Down**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/674/original/Screenshot_2023-09-25_at_8.09.51_PM.png?1695707362" width=300 />
### Approach

* We can start at top right cell.
* If A[i][j] < K, move down, else move left.
* Repeat until the element is found, our the search space is exhausted.

**NOTE:** We could have also started at bottom left cell.

### Pseudocode

```cpp
i = 0, j = M - 1
while(i < N && j>= 0){
    if(arr[i][j] == K){
        return true;
    } else if(arr[i][j] < K){
        i++; //move down; next row
    } else{
        j--; //move left; previous column
    }
}
return false;
```

### Time & Space Complexity
**Time Complexity:** O(M+N) since at every step, we are either discarding a row or a column. Since total rows+columns are N+M, hence Iterations will be N+M.
**Space Complexity:** O(1)


---
## Problem 3 Merge sorted Overlapping Intervals

### Problem Statement
You are given a collection of intervals A in a 2-D array format, where each interval is represented by a pair of integers `[start, end]`. The intervals are sorted based on their start values.

Your task is to merge all overlapping intervals and return the resulting set of non-overlapping intervals.

### Input:
Interval[] = {(0,2), (1,4), (5,6), (6,8), (7,10), (8,9), (12,14)}

### Output:

{(0,4), (5,10), (12,14)}

### Explanation:


| Interval 1 | Interval 2 |                 | Answer Interval List |
|:----------:|:----------:|:---------------:|:--------------------:|
|    0-2     |    1-4     |   Overlapping   |         0-4          |
|    0-4     |    5-6     | Not Overlapping |       0-4, 5-6       |
|    5-6     |    6-8     |   Overlapping   |       0-4, 5-8       |
|    5-8     |    7-10    |   Overlapping   |      0-4, 5-10       |
|    5-10    |    8-9     |   Overlapping   |      0-4, 5-10       |
|    5-10    |   12-14    | Not Overlapping |   0-4, 5-10, 12-14   |


### The Array Is Sorted Based on Start Time. What Is the Overlapping Condition?

Say start time of A < start time of B

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/056/original/Screenshot_2023-09-27_at_1.55.29_PM.png?1696314693)" width=300 />

Overlapping Condition - **If start of B <= end of A**

---

### Question

Given a sorted list of overlapping intervals, sorted based on start time, merge all overlapping intervals and return sorted list. Select output for following input.
Input:
Interval[] = { (1,10), (2, 3), (4, 5), (9, 12) }

### Choices
- [x] (1, 12)
- [ ] (1, 10), (9, 12)
- [ ] (1, 9), (9, 12)
- [ ] No Change


---

## Approach

* Create an array to store the merged intervals.
* If the current and ith intervals overlaps, merge them. In this case update the current interval with the merged interval.
* Else, insert the current interval to answer array since it doesn't overlap with any other interval and update the current Interval to ith Interval.

## Dry Run

### Input:
Interval[] = {(0,2), (1,4), (5,6), (6,8), (7,10), (8,9), (12,14)}

### Explanation:


| current |  ith  |                 | After merging | answer list |
|:-------:|:-----:|:---------------:|:-------------:|:-----------:|
|   0-2   |  1-4  |   Overlapping   |      0-4      |             |
|   0-4   |  5-6  | Not Overlapping |  Not needed   |     0-4     |
|   5-6   |  6-8  |   Overlapping   |      5-8      |     0-4     |
|   5-8   | 7-10  |   Overlapping   |     5-10      |     0-4     |
|  5-10   |  8-9  |   Overlapping   |     5-10      |     0-4     |
|  5-10   | 12-14 | Not Overlapping |  Not needed   |  0-4, 5-10  |
|  12-14  |  end  |                 |               |             |

At the end, we are left with the last interval, so add it to the list.

### Pseudocode
```cpp
currS = A[0][0], currE = A[0][1];

for (i -> 1 to N - 1) {
    if (A[i][0] <= currE) {
        currE = max(currE, A[i][1]);
    } else {
        ans.insert({currS, currE});
        currS = A[i][0];
        currE = A[i][1];
    }
}
ans.insert({currS, currE});

return ans;
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(1)


---
## Problem 4 Transpose of a square matrix

### Problem Statement
Given a square 2D matrix mat[N][N], find transpose.

### Transpose of matrix
The transpose of a matrix is a new matrix obtained by interchanging the rows and columns of the original matrix. 


### TestCase

```
mat[3][3] = {
    {1,2,3},
    {5,6,7},
    {9,10,11}
}
```

**Output:** 

```
{
{1,5,9},
{2,6,10},
{3,7,11}
}
```

### Observation
* After performing the transpose, what is same in the original matix and its transpose ?
The diagonal that starts from (0,0) is same.
![](https://i.imgur.com/9Xu3SYE.png)
* Along the diagonals, the elements have swapped their positions with corresponding elements.

### PseudoCode
```
function find_transpose(matrix[N][N]){
    for(i -> 0 to N - 1){
        for(j -> i + 1 to N - 1){
            swap(matrix[i][j],matrix[j][i]);
        }
    }
}
```
#### Note: If we start j at 0, the matrix will come back to its original position.

---
### Question

What is the time and space complexity to find transpose of a square matrix?

### Choices
- [ ] TC: O(N), SC: O(N)
- [ ] TC: O(N<sup>2</sup>), SC: O(N)
- [x] TC: O(N<sup>2</sup>), SC: O(1)
- [ ] O(N), SC: O(1)

---

### Complexity

Time Complexity: **O(N<sup>2</sup>)**.
Space Complextiy: **O(1)**


---
## Problem 5 Rotate a matrix to 90 degree clockwise

### Problem Statement
Given a matrix mat[N][N], rotate it to 90 degree clockwise.

### TestCase
```
{ {1,2,3},
  {4,5,6},
  {7,8,9} }
```
**Output:** 
```
{ {7,4,1},
  {8,5,2},
  {9,6,3} }
```

### Hint:
* What if we first find the transpose of the matrix?
* Is there any relation between rotated matrix and transposed matrix ?

### Observation:
Yes, if we reverse all the rows, then it will become rotated matrix.
The rotated matrix looks like:
![](https://i.imgur.com/B4p4avm.png)

**Transpose and rotated matrix:**
![](https://i.imgur.com/ZfdZaor.png)

### PseudoCode
```
Function rotate(mat[N][N]){
    mat = transpose(mat);
    for(i -> 0 to N - 1){
        reverse(mat[i]);
    }
    return mat;
}
```
### Complexity
Time Complexity: **O(N*N)**.
Space Complextiy: **O(1)**.
