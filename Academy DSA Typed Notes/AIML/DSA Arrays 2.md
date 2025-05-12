# DSA: Arrays 2

## Problem 1 Count of Pairs ag

Given a string **s** of lowercase characters, return the **count of pairs (i,j)** such that **i < j** and **s[ i ] is 'a'** and **s[ j ] is 'g'**.

### Example 1

```plaintext
String s = "abegag"
Ans = 3
```

### Explanation:
Here, [i,j] such that i<j and s[i] is 'a' and s[j] is 'g' are [0,3], [0,5] and [4,5]. So ans would be 3

---

### Question

What is the count of **a,g** pairs in the array:-
`s = "acgdgag"`

### Choices
- [x] 4
- [ ] 3
- [ ] 5
- [ ] 2


### Explanation
Here, [i,j] such that i<j and s[i] is 'a' and s[j] is 'g' are [0,2], [0,4], [0,6] and [5,6]. So ans would be 4.

---
### Question
How many **ag** pairs are in this string?
`s = "bcaggaag"`

### Choices
- [x] 5
- [ ] 4
- [ ] 3
- [ ] 6



### Explanation
Here, [i,j] such that i<j and s[i] is 'a' and s[j] is 'g' are [2,3], [2,4], [2,7], [5,7] and [6,7]. So ans would be 5.

---

## Brute Force Solution

For every **'a'**, we need to find the count of **g's** on the right side of **a**. So, we need to have nested loops.

### Pseudocode
```cpp
function count_ag(str) {
    result = 0;
    for (i -> 0 to n-1) {
        if(str[i] == 'a'){
            for (j -> i+1 to N-1){
                if(str[j] == 'g') {
                    result++;
                }               
            }
        }
    }
    return result;
}
```

### Time and Space Complexity
-- TC - $O(n^2)$
-- SC - $O(1)$


##  Optimised solution


### Observation: 
* For every **'g'**, we need to know the count of **'a'** on left side of **'g'**. 

* We will store the count of **'a'** and whenever **'g'** is encountered, we will add the count of **'a'** to the result.
 
### Dry Run
Example: **"acbagkagg"** 

![reference link](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/032/986/original/dry.jpeg?1682663462)

### Pseudocode
```cpp
function count_ag(str) {
    result = 0;
    count_a = 0;
    for(i -> 0 to n-1) {
        if(str[i] == 'a') {     
            count_a++;          
        }
        else if(str[i] == 'g') {
            result += count_a;
        }
    }
    return result;
}
```
#### Time and Space Complexity

What will be T.C and S.C for this approach?
-- TC - $O(n)$
-- SC - $O(1)$


---
## Introduction to Subarrays


### Definition
A subarray is a contiguous part of an array. It is formed by selecting a range of elements from the array. A subarray can have one or more elements and must be a contiguous part of the original array.

### Example
Consider the following array of integers:

| 4 | 1 | 2 | 3 | -1 | 6 | 9 | 8 | 12 |
| - | - | - | - | - | - | - | - | - |

* `2, 3, -1, 6` is a subarray of length 4.
* `9` is a subarray of single element.
* `4, 1, 2, 3, -1, 6, 9, 8, 12` is a subarray consisting of all the array elements.
* `4, 12` is **not** a subarray because loop does not count as subarray.
* `1, 2, 6` is **not** a subarray beacuse the array elements must be contiguous.
* `3, 2, 1, 4` is **not** a subarray because order of the elements in a subarray should be same as in the array.


---
### Question
A[] = { 2, 4, 1, 6, -3, 7, 8, 4}
Which of the following is a valid subarray?

### Choices
- [ ] {1, 6, 8}
- [ ] {1, 4}
- [ ] {6, 1, 4, 2}
- [x] {7, 8, 4}


### Explanation

{1, 6, 8} & {1, 4} are not contiguous parts of array. {6, 1, 4, 2} is not in the same order as in original array. Only {7, 8, 4} is a valid subarray.

---

## Representation of a Subarray

### Representation of a Subarray
A Subarray can be uniquely represented in following ways:
1. By specifying the `start` and `end` index of the subarray.
2. By specifying the `start` index and `length` of the subarray.

If we consider the same array from the above example, 
| 4 | 1 | 2 | 3 | -1 | 6 | 9 | 8 | 12 |
| - | - | - | - | - | - | - | - | - |

The subarray `2, 3, -1, 6` can be represented as 
* the range of elements starting at index `2` and ending at index `5` (0-based indexing).
* the range of elements having length of `4` with start index as `2`.

---
### Question

How many subarrays of the following array start from index 0
[4, 2, 10, 3, 12, -2, 15]

### Choices
- [ ] 6
- [x] 7
- [ ] 21
- [ ] 36


### Explanation

[4] (starting from index 0)
[4, 2] 
[4, 2, 10]
[4, 2, 10, 3]
[4, 2, 10, 3, 12]
[4, 2, 10, 3, 12, -2]
[4, 2, 10, 3, 12, -2, 15]
Therefore, there are a total of 7 subarrays that start from index 0.

---

### Question
How many subarrays of the following array start from index 1
[4, 2, 10, 3, 12, -2, 15]

### Choices
- [x] 6
- [ ] 7
- [ ] 21
- [ ] 36

### Explanation

[2] (starting from index 1)
[2, 10]
[2, 10, 3]
[2, 10, 3, 12]
[2, 10, 3, 12, -2]
[2, 10, 3, 12, -2, 15]

Therefore, there are a total of 6 subarrays that start from index 1.

---

## Problem 2 Find sum of all Subarrays sums 

### Problem Statement
Given an array of integers, find the total sum of all possible subarrays.
**#Note:** This question has been previously asked in *Google* and *Facebook*.

### Example
```cpp
Input: [3, 2, 5]
Output: 20
Explanation:

[3] = 3
[3, 2] = 5
[3, 2, 5] = 10
[2] = 2
[2, 5] = 7
[5] = 5
    
Thus total sum of all subarrays is 3 + 5 + 10 + 2 + 7 + 5 = 32
```

### Brute Force Solution
To solve this problem, we can use three nested loops. Two loops will generate all possible subarrays and third will be used to calculate sum of the subarray.

### Pseudocode
```cpp
function subArraysSumBruteForce(arr[], n) {
    
    total = 0;
        
    // Generate all possible subarrays and calculate their sum
    for (i -> 0 to n - 1) {
        for (j -> i to n - 1) {
            
            subarray_sum = 0;
            
            for (k -> i to j) {
                subarray_sum += arr[k];
            }
            
            total += subarray_sum;
        }
    }
    print(total)
}
```
### Time and Space Complexity
* TC - O(n^3)
* SC - O(1)


### Subarrays Sums - Prefix Sum


We can optimize the solution using the **Prefix Sum** technique. 
* First, calculate the Prefix Sum array of the Input Array. 
* Then, use two nested loops to iterate over all possible subarrays. At each iteration, calculate the sum of the subarray using the **Prefix Sum** array. 
* Add the subarray sum to the total.


### Pseudocode
```cpp
function totalSubArraySum(arr[], n) {
    // Calculate the prefix sum of the array
    prefix[n];
    prefix[0] = arr[0];
    for (i -> 1 to n - 1) {
        prefix[i] = prefix[i-1] + arr[i];
    }
    
    total = 0

    // Print the sum of all possible subarrays using the prefix sum
    for (i -> 0 to n - 1) {
        for (j -> i to n - 1) {
            if (i == 0) {
                sum = prefix[j]
            } else {
                sum = prefix[j] - prefix[i-1];
            }
            
            total += sum
        }
    }
    
    print(total);
}
```
### Time and Space Complexity
* TC - O(n^2)
* SC - O(n)

### Subarrays Sums - Carry Forward


### More optimized Solution - Observation
In the Brute force approach, with the first for loop, we have fixed i and with the second loop, we are moving j from i to n-1 and then using k we are calculating the sum from i to j.

```plaintext
A[ ] = {-4, 1, 3, 2}
i = 0
j = 0
k: sum = A[0]
j = 1
k: sum = A[0] + A[1]  —------------------- (a)
j = 2
k: sum = A[0] + A[1] + A[2]  —------------------- (b)
j = 2
k: sum = A[0] + A[1] + A[2]
j = 3
k: sum = A[0] + A[1] + A[2] + A[3]
```

### Hint 1:
Are we doing some redundant calculations? 
How can we avoid it?
If (a) has already been calculated, how can we calculate (b) using it?

### Expected: 
If sum = A[0] + A[1], we can just add A[2] to it to get the sum from index 0 to 2.

### Observation:
Everytime j is moving, we can add A[j] to the previous sum value and obtain the next sum value.

### Dry Run
```
A[ ] = {-4, 1, 3, 2}
```

i = 0
currSum = 0
|j|	subarray index|		currSum|	value|		total|
|-|----------|-------------|---------|------------|
|0| 	[0 0]|		+=A[0] |-4	       |	-4    | 
|1|		[0 1]|		+=A[1] |-4+1 = -3  |    -7    |
|2|		[0 2]|		+=A[2] |-4+1+3 = 0 |	-7     |
|3|		[0 3]|		+=A[3] |-4+1+3+2 = 2 |	-5     |

i = 1
currSum = 0
|j|		subarray index|		currSum|	value |		total|
|-|----------|-------------|----------|-----------|
|1|		[1 1]|		+=A[1] |	1 |		-4     |
|2|		[1 2]|		+=A[2] |	1+3	= 4  |	  0       |
|3|		[1 3]|		+=A[3] |	1+3+2 = 6 |		6     |

i = 2
currSum = 0
|j|		subarray index|		currSum|	value	|	total|
|-|----------|-------------|------------|---------|
|2|		[2 2]|		+=A[2] |		3	|	9     |
|3|		[2 3]|		+=A[3] |		3+2	= 5|	14     |

i = 3
currSum = 0
|j|		subarray index|		currSum|	value |		total|
|-|----------|-------------|----------|-----------|
|3|		[3 3]|		+=A[3] |		2 |		16     |


### Pseudocode
```cpp
function totalSubarraySum(arr[], n) {
    total = 0

    for (i -> 0 to n - 1) {
        currSum = 0;
        for (j -> i to n - 1) {
            currSum = currSum + arr[j]
                
            // add to the total
            total += currSum
        }
    }
    print(total);
}
```
The above technique is Carry Forward.
### Time and Space Complexity
* TC - O(n^2)
* SC - O(1)
### Subarrays Sums - Contribution Technique


### Contribution Technique

We can optimize the above solution further by observing a pattern in the subarray sums.
Let's take the example array ``[1, 2, 3]``. The subarrays and their sums are:

```
[1] -> 1
[1, 2] -> 3
[1, 2, 3] -> 6
[2] -> 2
[2, 3] -> 5
[3] -> 3
Total Sum = 1+3+6+2+5+3 = 20
```

Instead of generating all subarrays, we can check that a particular element appears in how many subarrays and add its contribution that many times to the answer.

* the first element 1 appears in 3 subarrays: [1], [1, 2], and [1, 2, 3]. 
* the second element 2 appears in 4 subarrays: [2], [1, 2], [2, 3], and [1, 2, 3]. 
* the third element 3 appears in 3 subarrays: [3], [2, 3], and [1, 2, 3].

Total = $(1*3) + (2*4) + (3*3) = 20$

### How to calculate the number of subarrays in which A[i] appears? 


### Question
In how many subarrays, the element at index 1 will be present?
A: [3, -2, 4, -1, 2, 6 ]

### Choices
- [ ] 6
- [ ] 3
- [x] 10
- [ ] 8



**Explanation:** The subarrays in which the element at index 1 is present are - 
[3, -2], [3, -2, 4], [3, -2, 4, -1], [3, -2, 4, -1, 2], [3, -2, 4, -1, 2, 6], [-2], [-2, 4], [-2, 4, -1], [-2, 4, -1, 2], [-2, 4, -1, 2, 6 ]. There are total 10 such subarrays.




### Question
In how many subarrays, the element at index 2 will be present?
A: [3, -2, 4, -1, 2, 6 ]

### Choices
- [ ] 6
- [x] 12
- [ ] 10
- [ ] 8


**Explanation:** The subarrays in which the element at index 1 is present are - 
[3, -2, 4], [3, -2, 4, -1], [3, -2, 4, -1, 2], [3, -2, 4, -1, 2, 6], [-2, 4], [-2, 4, -1], [-2, 4, -1, 2], [-2, 4, -1, 2, 6], [4], [4, -1], [4, -1, 2], [4, -1, 2, 6 ]. There are total 12 such subarrays.

### Subarrays Sums continued

### Generalized Calculation -
The start of such subarrays can be $0, 1, ..i$
The end of such subarrays can be $i, i+1, i+2, ...n-1$

Elements in range [0 i] = $i+1$
Elements in range [i n-1] = $n-1-i+1 = n-i$
Thus, the total number of subarrays containing arr[i] is i+1 multiplied by n-i. 

This gives us the expression `(i+1) * (n-i)`.

We can use this pattern to compute the total sum of all subarrays in O(n) time complexity. The steps are as follows:
* Initialize a variable total_sum to zero.
* Iterate over all elements of the input array arr. For each element arr[i], compute `arr[i] * (i+1) * (n-i)` and add it to total_sum.
* Return total_sum as the output of the function.

### Pseudocode
```cpp
function sumOfAllSubarraySums(arr[]) {
    n = arr.size();
    total_sum = 0;

    // Iterate over all elements of the array and compute the sum of all subarrays containing that element
    for (i -> 0 to n - 1) {
        total_sum += arr[i] * (i+1) * (n-i);
    }

    return total_sum;
}
```
### Time and Space Complexity
* TC - O(n)
* SC - O(1)


### Count subarrays of length K


Number of subarrays of length K = Total number of start indices of subarrays of length K.

All start positions for length K, will be within range **[0 N-K]**. Therefore total is N-K+1.

Hence, total number of subarrays of length K = **N-K+1**.


### Question

Given N=7, K=4, What will be the total number of subarrays of length K? 

### Choices
- [ ] 3
- [x] 4
- [ ] 5
- [ ] 6

### Problem 3 Max subarray sum with length K 


Given an array of N elements. Print maximum subarray sum for subarrays with length = K.

### Example
```
N=10 K=5
```

| -3  | 4   | -2  | 5   | 3   | -2  | 8   | 2   | -1  |  4  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |:---:|

### Explanation



| s | e | sum |
| -------- | -------- | -------- |
| 0     | 4     | 7     |
| 1     | 5     | 8     |
| 2     | 6     | 12     |
| 3     | 7     | 16     |
| 4     | 8     | 10     |
| 5     | 9     | 11     |

Maximum: **16**

### Max subarray sum with length K - Bruteforce Approach


We have to calculate the sum of all subarrays of size k and find the maximum out of them

### Pseudeocode

```cpp
function maxSubarrayOfLengthK(A[],N,K)
{
     ans = -infinity
         
     //first window
     i = 0 
     j = k-1
     
     while(j < N)
     {  
        sum = 0
        for(idx -> i to j)
        {
           sum += A[idx]
        }
        ans = max(sum, ans)
        
        //going to next subarray of length k
        i++
        j++
     }
     print(ans)
     
}
```

### Complexity

For what value of k will the iterations be highest ?

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/031/030/original/1.png?1681232198)

### Max subarray sum with length K - Sliding Window


We want to reduce the space complexity without modifying the given array, but how?

### Observations
* We can get sum of next subarray using current subarray sum as follows:-
  * By adding a new element to current sum.
  * By subtracting the first element of current subarray.
  
Given array :-
| -3  | 4   | -2  | 5   | 3   | -2  | 8   | 2   | -1  |  4  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |:---:|
 
First subarray from 0 to 4:-
| -3  | 4   | -2  | 5   | 3   |
| --- | --- | --- | --- | --- |

Converting first to second subarray :-

| <span style="color:red"> ~~-3~~ </span>   | 4   | -2  | 5   | 3   | <span style="color:green"> -2 </span>   |
| --- | --- | --- | --- | --- | --- |

Based upon above observation can we say:-
<div class="alert alert-block alert-warning">
sum of all elements of next subarray = sum of elements of current subarray - first element of current subarray + new element
</div>

This approach is known as  **Sliding window approach**. 

### Dry Run

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/031/066/original/Screenshot_%286%29.png?1681239141)

**We can clearly observe the window sliding in above run.**

### Pseudeocode

```cpp
function maxSubarrayOfLengthK(A[],N,K)
{
     ans = -infinity
     i = 0 
     j = K-1
         
     sum = 0         // here k iterations
     for(idx -> i to j)
     {
        sum += A[idx]           
     }
     ans = max(sum,ans)
         
     j++ 
     i++
       
     while(j<N)
     {                      
        sum = sum + A[j] - A[i-1]
        
        ans = max(sum,ans)
                                    // here N-k iterations
        i++
        j++
     }
     print(ans)
}

```
***Time Complexity  : O(N)**
**Space Complexity  : O(1)***
