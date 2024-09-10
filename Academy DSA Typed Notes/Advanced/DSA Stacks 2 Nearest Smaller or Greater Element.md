# Stacks 2: Nearest Smaller/Greater Element

## Problem 1 Nearest smallest element on left

### Problem Statement
Given an integer array A, find the index of nearest smallest element on left for all i index in A[].
Formally , for all i find j such that `A[j] < A[i]`, `j < i` and j is maximum.

### Example:

A[] = [8, 2, 4, 9, 7, 5, 3, 10]
Answer = [-1, -1, 1, 2, 2, 2, 1, 6]

For each element in the input array, the output indicates the index of the nearest smaller element on the left side of that element. If there's no smaller element on the left, it's represented by -1.

| Element | Nearest Smaller Element | Index of Nearest Smaller Element |
|:-------:|:-----------------------:|:--------------------------------:|
|    8    |           NA            |                -1                |
|    2    |           NA            |                -1                |
|    4    |            2            |                1                 |
|    9    |            4            |                2                 |
|    7    |            4            |                2                 |
|    5    |            4            |                2                 |
|    3    |            2            |                1                 |
|   10    |            3            |                6                 |

---


### Question

Given N array elements, find the **index** of the nearest smaller element on the left side for all the elements. If there is NO smaller element on left side, ans is -1.

A = [4, 6, 10, 11, 7, 8, 3, 5]

### Choices

- [ ] [-1, 0, 1, 2, 0, 4, -1, 6]
- [ ] [-1, 0, 1, 2, 1, 1, -1, 6]
- [x] [-1, 0, 1, 2, 1, 4, -1, 6]


---


### Question

Given N array elements, find the **index** of the nearest smaller element on the left side for all the elements. If there is NO smaller element on left side, ans is -1.

A = [4, 5, 2, 10, 8, 2]

### Choices

- [ ] [0, 0, -1, 2, 2, -1]
- [x] [-1, 0, -1, 2, 2, -1]
- [ ] [-1, 0, 0, 2, 2, -1]
- [ ] [-1, 0, 2, 2, 2, 2]

---
## Nearest smallest element on left Brute Force


For each element in the array, iterate through all the elements to its left.

Note: We want the indices in answer array.

### Pseudocode
```java 
result[n];
for (i -> 0 to n - 1) {
    nearestSmaller = -1;

    for (j -> i - 1 down to 0) {
        if (arr[j] < arr[i]) {
            nearestSmaller = j;
            break;
        }
    }

    result[i] = nearestSmaller;
}
return result;
```

### Time Complexity

This approach has a time complexity of $O(n^2)$ because for each element, it requires checking all elements to its left. It is inefficient for large input arrays.

---


### Question

If A = [8, x, x, x, x, 5, x, x, x, x...]
For any element present after 5, can the element 8 become nearest smaller element on left?

### Choices

- [ ] Yes
- [x] No

### Explanation

Not really since 5 will be the answer for them.

---
## Nearest Smallest Element Optimized Approach


### Observation/Intuition:

To efficiently find the nearest smaller element to the left of each element in an array, you can use a stack. Here’s a simplified explanation:

1. **Use a Stack:** As you move from left to right through the array, use a stack to keep track of element indices that haven't yet found their nearest smaller element.

2. **Compare with Stack's Top:** For each new element, compare it with the element at the top of the stack. If the new element is smaller, it means it's the nearest smaller element for the future elements, making the stack's top element no longer valid.

3. **Pop the Stack:** Continue popping the stack until you find an element smaller than the current one or the stack is empty. This way, the popped elements are marked as having their nearest smaller element found.

4. **Linear Time Complexity:** This method avoids nested loops and extensive comparisons, allowing you to find each element's nearest smaller neighbor with a linear time complexity, 𝑂(𝑛)

By continuously updating the stack and assigning nearest smaller elements efficiently, this approach streamlines the process, ensuring each element's comparison is handled as you iterate through the array.


---
## Nearest Smallest Element Optimized Approach Dry Run


* Initialize an empty stack and an empty result array of the same length as A filled with -1s.
* Start iterating through the array from left to right:
   
|  i  | Element | Pop index | Stack | Nearest Smaller Element | Push index |
|:---:|:-------:|:---------:|:-----:|:-----------------------:|:----------:|
|  0  |    8    |    NIL    | EMPTY |           NA            |     0      |
|  1  |    2    |     0     | EMPTY |           NA            |     1      |
|  2  |    4    |    NIL    |   1   |            2            |     2      |
|  3  |    9    |    NIL    | 1, 2  |            4            |     3      |
|  4  |    7    |     3     | 1, 2  |            4            |     4      |
|  5  |    5    |     4     | 1, 2  |            4            |     5      |
|  6  |    3    |   5, 2    |   1   |            2            |     6      |
|  7  |   10    |    NIL    | 1, 6  |            3            |     7      |


**PseudoCode:**

```java
for (i -> 0 to n - 1) {
        // While the stack is not empty and the element at the current index is less than or
        // equal to the element at the index stored at the top of the stack, pop elements from
        // the stack and update the result array.
        while (not Empty(stack) and arr[i] <= arr[stack.top()]) {
            stack.pop();
        }

        // If the stack is not empty, the top element's index is the nearest smaller element on the left.
        if (not Empty(stack)) {
            result[i] = stack.top();
        }

        // Push the current index onto the stack.
        stack.push(i);
    }

    return result;
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)

---
## Variation Question 2 Restraunt Hunt


A person uses **Google Maps** to find the nearest restaurants and picks one based on its proximity. Unfortunately, after visiting, they realized that the restaurant didn't meet their expectations. 

**Task**
Let's break it down with a simple example. You have a list of restaurants and their **ratings**. For each restaurant, we're going to find the next restaurant to the **right** on the list that's not just close but also has a **higher rating** than the **current** one. If there's no better option on the list, we'll say there's **none** available.

**Problem** 
Given a sequence of restaurants listed on Google Maps with their ratings, create a tool that helps users discover the rating of the next higher-rated restaurant to the right for each listed establishment. 

#### Example Input

Ratings[] =


| 0 | 1 | 2 | 3 | 4 | 5 |  6 |
| -| -| -| -| -| -|-|
| 3 | 2 | 6 | 5 | 8 | 7 |9 |

Output -
Next greater elements' indices are mentioned for each element.
| 3 | 2 | 6 | 5 | 8 | 7 |9 |
| -| -| -| -| -| -|-|
| 2 | 2 | 4 | 4 | 6 | 6 |  -1 |

### Approach

In this problem, **we have to find greater element on right.**
This is also a variation of above problem only.
* For this question, we need to iterate from right to left.
* For an element A[i], while A[i] >= element at top of stack, then keep removing.
* If at the end stack is not empty, the element at top will be answer for A[i].

### Code

```java 
for (i -> n - 1 down to 0) {
    // While the stack is not empty and the current element is greater than or
    // equal to the element at top, pop and update the result array.
    while (not stack.isEmpty() and arr[i] >= arr[stack.to()]) {
        stack.pop();
    }

    // If the stack is not empty, the top element is the nearest greater element on the right.
    if (not stack.isEmpty()) {
        result[i] = stack.top();
    }

    // Push the current index onto the stack.
    stack.push(i);
}

return result;
```

---
## Variations of the problem


## Try the below problems by yourselves

### Question 3: For all `i`, find nearest greater element on left

### Question 4: For all `i`, find nearest smaller element on right.

---
## Problem 2 Largest Rectangle in histogram


### Problem Statement

Given an integer array A, where
A[i] = height of i-th bar.
Width of each bar is = 1.

Find the area of the largest rectangle formed by continious bars.


**Given Array (heights):** [8, 6, 2, 5, 6, 5, 7, 4]

The goal is to find the largest rectangle that can be formed using continuous bars from this array. In this example, the largest rectangle is formed by bars with heights 5, 6, 5, and 7. The width of each bar is 1, so the area of this rectangle is 5 (height) * 4 (width) = 20.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/493/original/upload_1a381873534ce89cd41fd72c9f479c12.png?1697181086" width=600/>


Sure, here is a brief MCQ based on finding the largest rectangle formed by continuous bars in an integer array representing bar heights:

---


### Question
Find the area of the largest rectangle formed by continious bars.

bars = [1, 2, 3, 2, 1]

### Choices
- [ ] 5
- [ ] 9
- [ ] 7
- [x] 6
- [ ] 3

### Explanation:

The largest rectangle is formed from [2, 3, 2] whose contribution is [2, 2, 2] thus the area of the largest rectangle is 6. 


---
## Largest rectangle Approach


### Largest Rectangle Brute Force

**Brute - Force Approach Pseudo Code:**

```cpp
function findMaxRectangleArea(hist):
    maxArea = 0

    for i from 0 to len(hist) - 1:
        // Consider each bar as a potential starting point
        minHeight = hist[i]

        for j from i to len(hist) - 1:
            // Iterate through bars to the right
            minHeight = min(minHeight, hist[j])
            width = j - i + 1
            area = minHeight * width
            maxArea = max(maxArea, area)

    return maxArea
```

The brute-force approach involves nested loops and has a time complexity of O(n^2) because it considers all possible combinations of starting and ending points for rectangles.


### Optimized Approch

**Mathematical Representation:**

* Let a[i] represent the height of the bar at index i.
* We use j to represent the index of the nearest smaller bar to the left of i.
* Similarly, we use k to represent the index of the nearest smaller bar to the right of i.
* The area of the rectangle that can be formed with the bar at index i as its base is given by `a[i] * (k - j - 1)`.

**Observation/Intuition:**

* The key insight here is that for each potential base (represented by indices in the stack), we can efficiently calculate the area of the rectangle by finding the width between the current index and the index at the top of the stack.
* By using a stack, we maintain a list of potential bases and calculate the area of rectangles as we encounter new heights, ensuring we consider all possible rectangles efficiently.

**Optimized Approach Pseudo Code:**

```cpp
function findMaxRectangleArea(hist):
    stack = []  // Initialize an empty stack to store indices of bars.
    maxArea = 0

    for i from 0 to len(hist) - 1:
        while (stack is not empty and hist[i] < hist[stack.top()]):
            // Pop elements from the stack and calculate areas
            // with their heights as the potential bases.
            height = hist[stack.pop()]
            width = (i - stack.top() - 1) if stack is not empty else i
            area = height * width
            maxArea = max(maxArea, area)

        stack.push(i)  // Push the current index onto the stack.

    while (stack is not empty):
        // Process the remaining elements in the stack.
        height = hist[stack.pop()]
        width = (len(hist) - stack.top() - 1) if stack is not empty else len(hist)
        area = height * width
        maxArea = max(maxArea, area)

    return maxArea
```


**Mathematical Representation of the Answer:**

* The answer (maximum area) is given by the formula:
* $ans ~=~ max(a[i] * (nearest~smaller~right[i] * nearest~smaller~left[i] - 1))$
* Where a[i] is the height of the bar at index i.
* `nearest_smaller_right[i]` is the index of the nearest smaller bar to the right of i.
* `nearest_smaller_left[i]` is the index of the nearest smaller bar to the left of i.
* We subtract 1 from the product of `nearest_smaller_right[i]` and `nearest_smaller_left[i]` to account for the width of the rectangle.

---
## Problem 3 Sum of (Max-Min) of all subarrays


### Question

Giver an integer array with distinct integers, for all subarrays find (max-min) and return its sum as the answer.

**Example:**

Given Array: [2, 5, 3]

The goal is to find the sum of the differences between the maximum and minimum elements for all possible subarrays.

* Subarray [2]: Max = 2, Min = 2, Difference = 0
* Subarray [5]: Max = 5, Min = 5, Difference = 0
* Subarray [3]: Max = 3, Min = 3, Difference = 0
* Subarrays of length 2:
   * [2, 5]: Max = 5, Min = 2, Difference = 3
   * [5, 3]: Max = 5, Min = 3, Difference = 2
* Subarray [2, 5, 3]: Max = 5, Min = 2, Difference = 3


The sum of all differences is 0 + 0 + 0 + 3 + 2 + 3 = 8.


### Sum of (Max-Min) of all subarrays Brute force approach
**Brute-Force Approach Pseudo Code:**

```cpp
function sumOfDifferences(arr):
    result = 0

    for start from 0 to len(arr) - 1:
        for end from start to len(arr) - 1:
            // Find the maximum and minimum elements within the subarray
            maxElement = arr[start]
            minElement = arr[start]

            for i from start to end:
                maxElement = max(maxElement, arr[i])
                minElement = min(minElement, arr[i])

            // Calculate the difference between the maximum and minimum elements
            difference = maxElement - minElement

            // Add this difference to the result
            result += difference

    return result
```

### Complexity
**Time Complexity:** O(N^3^)
**Space Complexity:** O(1)

---


### Question
Giver an integer array, A with distinct integers, for all subarrays find (max-min) and return its sum as the answer.

A = [1, 2, 3]

### Choices
- [x] 4
- [ ] 6
- [ ] 5
- [ ] 0


### Explanation:

The goal is to find the sum of the differences between the maximum and minimum elements for all possible subarrays.

Subarrays of length 1:
* [1]: Max = 1, Min = 1, Difference = 0
* [2]: Max = 2, Min = 2, Difference = 0
* [3]: Max = 3, Min = 3, Difference = 0

Subarrays of length 2:
* [1, 2]: Max = 2, Min = 1, Difference = 1
* [2, 3]: Max = 3, Min = 1, Difference = 1

Subarrays of length 3:
* [1, 2, 3]: Max = 3, Min = 1, Difference = 2

The sum of all differences is 0 + 0 + 0 + 1 + 1 + 2 = 4. 


---
## Sum of (Max-Min) of all subarrays Optimized approach


### Optimized Approach

**Intuition:**

1. Calculate the contribution of each element being the maximum
2. Calculate the contribution of each element being the minimum
3. Calculate the total contribution : contribution = element × (count as max − count as min)

### Contribution idea
Let's take example  **A** = $[1, 2, 3]$

Now compute the 4 things for each element:
1. Previous Greater element's index (default value -1)
2. Next Greater element's index (default value n)
3. Previous Smaller element's index (default value -1)
4. Next Smaller element's index (default value n)

| index | prvGreater | nxtGreater | prvSmaller | nxtSmaller |
|:-----:|:----------:|:----------:|:----------:|:----------:|
|   0   |     -1     |     1      |     -1     |     3      |
|   1   |     -1     |     2      |     0      |     3      |
|   2   |     -1     |     3      |     1      |     3      |


**Contributions :**

1. Contribution as Min = $(nxtSmaller - i) * (i - prvSmaller)$
2. Similarly Contribution as Max = $(nxtGreater - i) * (i - prvGreater)$
3. Total contribution = (contribution as max - contribution as min)

| index | contribution as Min | contribution as Max | Total Contribution |
|:-----:|:-------------------:|:-------------------:| ------------------ |
|   0   |          3          |          1          | -2                 |
|   1   |          2          |          2          | 0                  |
|   2   |          1          |          3          | 2                  |

Hence Total Contribution = $A[0] * (-2) + A[1] * (0) + A[2] * (2)$ 
= $-2 + 0 + 6$ = $4$

**Optimized Approach Pseudo code:**

```cpp
function subarrayRanges(A):
    n = size(A)
    nextGreater = array of size n, initialized to n
    prevGreater = array of size n, initialized to -1
    nextSmaller = array of size n, initialized to n
    prevSmaller = array of size n, initialized to -1

    stack = empty stack

    // Find next greater elements
    for i from 0 to n-1:
        while stack is not empty and A[stack.top()] < A[i]:
            nextGreater[stack.top()] = i
            stack.pop()
        stack.push(i)

    clear stack

    // Find previous greater elements
    for i from n-1 to 0:
        while stack is not empty and A[stack.top()] <= A[i]:
            prevGreater[stack.top()] = i
            stack.pop()
        stack.push(i)

    clear stack

    // Find next smaller elements
    for i from 0 to n-1:
        while stack is not empty and A[stack.top()] > A[i]:
            nextSmaller[stack.top()] = i
            stack.pop()
        stack.push(i)

    clear stack

    // Find previous smaller elements
    for i from n-1 to 0:
        while stack is not empty and A[stack.top()] >= A[i]:
            prevSmaller[stack.top()] = i
            stack.pop()
        stack.push(i)

    result = 0

    // Calculate the result based on the contributions
    for i from 0 to n-1:
        maxContribution = (i - prevGreater[i]) * (nextGreater[i] - i)
        minContribution = (i - prevSmaller[i]) * (nextSmaller[i] - i)
        result += A[i] * (maxContribution - minContribution)

    return result
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)
