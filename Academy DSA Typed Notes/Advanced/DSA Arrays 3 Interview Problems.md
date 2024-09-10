# Lecture | Advanced DSA: Arrays 3 - Interview Problems

## Revision Quizzes

### Question
Which starting point would you choose as the most efficient to find whether element k is present in a row-wise and column-wise sorted matrix?

### Choices
- [ ] Top left
- [x] Top right
- [ ] Bottom right
- [ ] None


---

### Question
In the optimized approach for finding an element in a row-wise and column-wise sorted matrix of size NxM, what is the time complexity?

### Choices
- [ ] O(N^2^)
- [ ] O(log(N))
- [x] O(M + N)
- [ ] O(N)

---

### Question
In a matrix, what is a submatrix?

### Choices
- [ ] a matrix with all elements zero
- [ ] a matrix with all elements one
- [x] a continuous part of original matrix
- [ ] a matrix with only diagonal elements

---

### Question
How can a submatrix be uniquely identified ?

### Choices
- [ ] Using one corner coordinates
- [ ] Using two corner coordinates
- [x] Using two diagonal coordinates
- [ ] All of above

---

### Question
In the optimized approach for finding the sum of all submatrices of a Matrix of size NxN, what is the time complexity?

### Choices
- [ ] O(1)
- [ ] O(N)
- [x] O(N<sup>2</sup>)
- [ ] O(N log (N))

---

## Merge Intervals

An Interval is defined by start and end time, where start <= end.

Say we are given a list of Intervals, we will have to merge them if they overlap.

Let's look at them below -

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/054/original/Screenshot.png?1696314602)" width=700 />

### Non-Overlapping Condition

Say there are two Intervals, I1 {s1 e1} & I2 {s2 e2}
Then the condition for them to not overlap is -


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/055/original/Screenshot_2023-09-27_at_1.25.30_PM.png?1696314640)" width=500 />

```javascript
if(s2 > e1 || s1 > e2)
```

So, if above condition is not followed, it says that Intervals are overlapping!


### How to merge overlapping Intervals ?


**[I1.start , I1.end] & [I2.start , I2.end]**
After merging -
**[min(I1.start, I2.start) , max(I1.end, I2.end)]**


---

### Question
If the intervals [3, 8] and [5, 12] are given, do they overlap?

### Choices
- [x] Yes
- [ ] No




### Explanation:

Answer: Yes

The intervals [3, 8] and [5, 12] overlap because 8 is greater than 5. The overlapping area is [5, 8]

---

### Question
What is the correct way to represent the merged result of intervals [6, 10] and [8, 15]?

### Choices
- [x] [6, 15]
- [ ] [6, 8, 10, 15]
- [ ] [6, 10] and [8, 15]
- [ ] [8, 10]



### Explanation:

[6, 15]

This is because the merging of intervals involves combining overlapping intervals into a single, continuous interval


---
## Problem 1 Merge sorted Overlapping Intervals


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

Overlapping Condition - 
**If start of B <= end of A**


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

## Problem 1 Approach

* Create an array to store the merged intervals.
* If the current and ith intervals overlaps, merge them. In this case update the current interval with the merged interval.
* Else, insert the current interval to answer array since it doesn't overlap with any other interval and update the current Interval to ith Interval.

### Dry Run

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
## Real life application - Website Maintenance - follow up to first problem


### Background
**Scaler Academy**, a leading ed-tech platform known for its comprehensive learning programs, is planning to conduct maintenance on its website to enhance user experience and introduce new features. 

To ensure the maintenance work does not disrupt the learning process for its students, Scaler Academy aims to schedule this maintenance during the period of **no user activity**.

### Problem Statement

Given sorted data on the active hours of multiple learners on the platform, your task is to analyze this data and identify the longest continuous period when no learners are active. This identified time slot is crucial as it represents the best opportunity to perform website maintenance with the least disruption to learners' activities.

### Example Input : 
DATA =  [(9, 11), (14, 16), (15, 20)]
### Output :
Maximum time = **8**
### Explanation

After merging the data, we get the following intervals -
[(9, 11), (14, 20)]

There are three time intervals during which there is no user online for the day:- 
- First is (0, 9) => 9 hrs
- Second is (11, 14) => 3 hrs
- Third is (20, 24 (00)) => 4 hrs

**Here the our answer is the longest time interval which is (0, 9) for 9 hours**


### How does this question use the same concept?
- Once intervals are **merged** as per problem 1, identifying **gaps** becomes straightforward. 
- Each gap between consecutive intervals represents a potential maintenance window. 
- The longest of these gaps is then an optimal time for maintenance.

This is just a real life situation for above problem.


---
## Problem 2 Find First Missing Natural Number

### Problem Statement
Given an unsorted array of integers, Find first missing Natural Number.

### Examples
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/058/original/Screenshot_2023-09-27_at_2.42.15_PM.png?1696314889" width=500 />


---

### Question
In the array [5, 3, 1, -1, -2, -4, 7, 2], what is the first missing natural number?

### Choices
- [x] 4
- [ ] 6
- [ ] -3
- [ ] 8


w## Find First Missing Natural Number Solution Approach


### Approach 1: Brute Force
Check for all the numbers from 1 till we get the answer
**T.C -** O(N * ans)

Here, in the worst case answer can go uptil N+1, in case if all numbers from 1 to N are present in the array.

**Example -** {4, 1, 3, 2}
Here we will have to iterate till 5, ie. N+1.


## First Missing Natural Number Optimised Approach

### Idea
**Can we utilise the fact that answer can be out of 1 to N+1?**
If any number other than 1 to N is present, then missing is out of 1 to N only.
If all elements from 1 to N are present, then it will be N+1.

Say we start checking if 1 is present or not, we somehow want to mark the presence of 1.
Now, since we can't use extra space, so we can use indices to mark the presence of a number.

Index 0 can be used to mark presence of 1.
Index 1 can be used to mark presence of 2.
Index 2 can be used to mark presence of 3.
so on....

**Now how do we mark the presence ?**

**One Solution:**
```plaintext
We can set element at that index as negative. 
```

*But what if negative number is part of the input?*

### Let's assume only positive numbers are present
We can use indices to mark the presence of a number.
We can set element at that index as negative.

**A[ ] = {8, 1, 4, 2, 6, 3}**

```plaintext
N = 6
Answer can be from [1 7]
So, if any number is beyond this range, we don't care!
```

| index | element |       presence marked at index        |   state of the array    |
|:-----:|:-------:|:-------------------------------------:|:-----------------------:|
|   0   |    8    | don't care, since out of answer range |                         |
|   1   |    1    |                   0                   |   {-8, 1, 4, 2, 6, 3}   |
|   2   |    4    |                   3                   |  {-8, 1, 4, -2, 6, 3}   |
|   3   |    2    |                   1                   |  {-8, -1, 4, -2, 6, 3}  |
|   4   |    6    |                   5                   | {-8, -1, 4, -2, 6, -3}  |
|   5   |    3    |                   2                   | {-8, -1, -4, -2, 6, -3} |

Now, we can just iterate from left to right and whichever element is not ve-, we can return i+1 as the answer.
**Example: {-8, -1, -4, -2, 6, -3}**
Here, index: 4 is +ve, hence 5 is the answer.

**NOTE:** Since we are marking elements as negative, so when checking presence of a certain number, we'll have to consider the absolute value of it.

### Pseudocode
```cpp
for(i -> 0 to N - 1) {
    ele = absolute(A[i]);
    
    if(ele >= 1 and ele <= N) {
        int idx = ele - 1;
        A[idx] = -1 * absolute(A[i]);
    }
}
```

---
## First missing natural number if negative numbers are present


### How to resolve for negative numbers ?

Will negatives ever be our answer?
**NO!**
So, we don't have to care about them!

Should we change them to ve+ ?
**NO!** They may fall in our answer range.

Should we mark them 0?
**NO!** Then we will not be able to mark the presence of a number!

***We can just change negative number to a number that is out of our answer range. **It can be N+2**.***

```cpp
for(i -> 0 to N - 1) {
    if(A[i] <= 0) {
        A[i] = N + 2;
    }
}

for(i -> 0 to N - 1) {
    ele = abs(A[i]);
    
    if(ele >= 1 && ele <= N) {
        idx = ele - 1;
        A[idx] = -1 * abs(A[i]);
    }
}

for(i -> 0 to N - 1) {
    if(A[i] > 0) return i + 1;
}
return N + 1;
```
>Please show a dry run on - {4, 0, 1, -5, -10, 8, 2, 6}

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(1)

