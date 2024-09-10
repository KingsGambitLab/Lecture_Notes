# Sorting 1: Count Sort & Merge Sort


## Count Sort

### Problem Statement

Find the smallest number that can be formed by rearranging the digits of the given number in an array. Return the smallest number in the form an array.

**Example:** 
A[ ] = `{6, 3, 4, 2, 7, 2, 1}`
Answer: `{1, 2, 2, 3, 4, 6, 7}`

A[ ] = `{4, 2, 7, 3, 9, 0}`
Answer: `{0, 2, 3, 4, 7, 9}`

### Observation/Hint
The digits in a number can only `range from 0 to 9`, thus instead of sorting the number which takes `O(N log N)` time, one can leverage this fixed range to derive a faster solution.

### Approach

* **Frequency Count:** Create an `array of size 10` to count the frequency of each digit in the given number.
* Using the frequency array, reconstruct the original array in ascending order.
* This method of sorting based on frequency counting is often called "**`Count Sort`**".

### Pseudocode

```cpp
Frequency Array of size 10
F = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i -> 0 to (N - 1) {
   F[A[i]] ++
}

k = 0

for d -> 0 to 9 {   // For each digit
   for i -> 1 to F[d] {
      A[k] = d
      k++
   }
}

return A
```

### Dry Run

* A = `[1, 3, 8, 2, 3, 5, 3, 8, 5, 2, 2, 3]` (Given Array)
* F = `[0, 1, 3, 4, 0, 2, 0, 0, 2, 0]` (Frequency Array)
* Reconstructing A using F:
1 (once), 2 (three times), 3 (four times), 5 (two times), 8 (two times)
* Resulting A = `[1, 2, 2, 2, 3, 3, 3, 3, 5, 5, 8, 8]`

### TC and SC
* **Time Complexity:** O(N)
* **Space Complexity:** O(1) (Since the size of the frequency array is constant, regardless of the size of N).

---
## Count Sort on large values


### Will Count Sort work if the range of A[i] is more than $10^9$?

* Count Sort isn't suitable for a range of $10^9$ because a frequency array of this size would demand too much memory.
* Count Sort works well when the range of A[i] is ~ $10^6$.

Each integer typically occupies `4 Bytes`.

Storing $10^9$ integers requires 4GB, which is often impractical. An array up to $10^6$ in length is more manageable, needing 4MB.

---
## Count Sort on Negative Numbers


### Problem Statement

Implement Count Sort for an array containing negative numbers.

### Observation/Hint
Unlike conventional **Count Sort**, which operates on non-negative integers, this variation needs to account for negative numbers. The method involves adjusting indices in the frequency array based on the smallest element in the original array.

### Approach

* **Find Range:** Determine the smallest and largest elements in the array to ascertain the range.
* **Adjust for Negative Numbers:** By adjusting indices in the frequency array based on the smallest element, negative numbers can be accounted for.

### Example

* Given A = [-2, 3, 8, 3, -2, 3]
* Smallest = -2, Largest = 8
* Range = 11 (8 - (-2) + 1)
* Frequency array F = [2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1]
* 0th index frequency is mapped with -2, 1st index with -1, and so on.
* Reconstructed A using F: -2, -2, 3, 3, 3, 8 

### Pseudocode

```cpp
//Find smallest and largest elements in A
//Create a frequency array F of size (largest - smallest + 1)

for i -> 0 to (N - 1) {
   F[A[i] - smallest_element] ++
}

//Reconstruct array A using F

for each index i in F {
   while F[i] > 0 {
      Append (i + smallest_element) to A
      F[i]--
   }
}
```

### TC and SC
* **Time Complexity (TC):** O(N)
* **Space Complexity (SC):** O(N + Range)

---
## Gmail's All Inboxes Feature

### Scenerio
**Google's Gmail** offers an "***All Inboxes***" feature that allows users to view emails from **multiple email accounts** in one seamless interface. This is particularly useful for users managing personal and professional communications through separate accounts. 

The feature ensures that emails from all accounts are merged into a single feed sorted by date and time, facilitating better email management and access.

### Problem 
Develop a function to emulate the "**All Inboxes**" feature of **Gmail**. 
- You are given **two sorted arrays** that represent **timestamps** of emails from two different email accounts. Each element in the array is an email object. 
- Your task is to merge these two arrays into a single list, ensuring that the resulting list is sorted by the **timestamp**, allowing the user to view emails in a **chronological order** from both accounts combined.

### Example
**Input**:  

| ACCOUNT| Email Times | 
| -------- | -------- | 
| A | $[1, 5, 6, 9]$    | 
|  B   | $[2, 4, 8]$|

**OUTPUT** : $[1, 2, 4, 5, 6, 8, 9]$

### Approach : 
- This is a direct application of **Merge two sorted arrays**.
- Let's have a deep look into the concept now.

---
## Merge two sorted arrays


Giver an integer array where all odd elements are sorted and all even elements are sorted. Sort the entire array.

A[] = {`2, 5, 4, 8, 11, 13, 10, 15, 21`}

### Approach
We can take two separate arrays to keep even(EVEN[]) and odd(ODD[]) elements. Then we can merge them in the original array.

We will keep three pointers here: `a(for original array)`, `e(for even array)` and `o(for odd array)`, all starting at index 0.

If A[a] is odd, ODD[o]=A[a], o++, a++
If A[a] is even, EVEN[e]=A[a], e++, a++

---
## Pseudocode


```java
function merge( A[]) {
    N = A.length();

    //n1: count of even elements
    //n2: count of odd elements
    n1 = 0, n2 = 0;

    // Count the number of even and odd elements
    for (i -> 0 to N - 1) {
        if (A[i] % 2 == 0)
            n1++;
        else
            n2++;
    }

    EVEN[n1], ODD[n2];
    a = 0; // moves over A
    e = 0; // moves over EVEN
    o = 0; // moves over ODD
    
    for(i -> 0 to N - 1) {
        if(A[a] % 2 == 0) {
            EVEN[e] = A[a];
            e++;
        }
        else {
            ODD[o] = A[a];
            o++;
        }
        a++;
    }
    
    a = 0; // moves over A
    e = 0; // moves over EVEN
    o = 0; // moves over ODD
    
    // perform actual logic of merging of two sorted arrays
    
    while (e < n1 && o < n2) {
        if (EVEN[e] < ODD[o]) {
            A[a] = EVEN[e];
            e++;
        } else {
            A[a] = ODD[o];
            o++;
        }
        a++;
    }
    
    while (e < n1) {
        A[a] = EVEN[e];
        e++;
        a++;
    }
    
    while (o < n2) {
        A[a] = ODD[o];
        a++;
        o++;
    }
}
```

---


### Question
Iteration of merging 2 Arrays?

### Choices
- [ ] N ^ 3
- [ ] N ^ 2
- [x] 2 * N
- [ ] Constant


---
## Merge Sort


### Example: Sorting Examination Sheets
>A teacher collected the examination sheets of students randomly. Now, she needs to sort those sheets as per roll number of students. As she is smart, instead of sorting it by herself, she divided the sheets into two halves and gave each half to Kishore and Suraj for sorting.

>Once she has the sorted halves, she just need to merge two sorted halves, which is significantly easier.

>Kishore and Suraj also decided to repeat this and divided the sheets in two halves and gave them to their friends for sorting.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/864/original/upload_40b520e7af8dd0f922e1d9c2d89636cf.png?1697472522" width="500" />

>In this way, the last students will have one sheet only. They can directly gave that sheet to the students before them whose job will be to arrange those two sheets and pass it above.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/865/original/upload_adb5507f2cfca8b1765468ce198b10b1.png?1697472567" width="500" />


>In this way, the sheets are finally sorted.

## Example: Sorting Numbers
Sort the array, A = {3, 10, 6, 8, 15, 2, 12, 18, 17}

### Divide

* The idea is to divide the numbers in two halves and then start merging the sorted arrays from bottom and pass above.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/866/original/upload_7e5df36dc120d7420e309c41164356a3.png?1697472603" width="500" />


### Merge
- Merging [3] and [10] as [3, 10] 
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/869/original/upload_6ec547929c68fa72ea4313246feda12f.png?1697472658" width="500" />

- Merging [3, 10] and [6] as [3, 6, 10]
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/870/original/upload_c4ab90c586f56f05b3251e0e9e156f56.png?1697472722" width="500" />

- Merging [8] and [15] as [8, 15]
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/871/original/upload_1cba3e08b9c70b828a83a2dd3918efe9.png?1697472758" width="500" />

- Merging [3, 6, 10] and [8, 15] as [3, 6, 8, 10, 15]
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/872/original/upload_611d5e13b458afb7740064b342a6b033.png?1697472843" width="500" />

- Merging [2] and [12] as [2, 12]
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/874/original/upload_ed17cfb54776ca14d04018b75f249a3d.png?1697472907" width="500" />

- Merging [18] and [17] as [17, 18]
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/877/original/upload_75715655b476438b9f8b89bbc7897a01.png?1697472953" width="500" />

- Merging [2, 12] and [17, 18] as [2, 12, 17, 18]
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/878/original/upload_888c80aade9ad006676f296b54a593f7.png?1697472999" width="500" />

- Merging [3, 6, 8, 10, 15] and [2, 12, 17, 18] as [2, 3, 6, 8, 10, 12, 15, 17, 18]
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/879/original/upload_0ef9c62a941f2bff356661587a27008a.png?1697473037" width="500" />

In this way, we have finally sorted the array.

***This algorithm of dividing the array into multiple subproblems and merging them one by one is called Merge Sort.***

*Since we are breaking down the array into multiple subproblems and applying the same idea to merge them, we are using the technique of Recursion.*


## Psuedocode
```java 
function merge(A[], l, mid, r) {
    N = A.length();
    n1 = mid-l+1;
    n2 = r-mid;
    
    B[n1], C[n2];
    
    idx=0;
    for(i -> l to mid){
        B[idx] = A[i];
        idx++;
    }
    
    idx=0;
    for(i -> mid+1 to r){
        C[idx] = A[i];
        idx++;
    }
    
    idx = l;
    i = 0; // moves over A
    j = 0; // moves over B
    
    while (i < n1 && j < n2) {
        if (B[i] <= C[j]) {
            A[idx] = B[i];
            i++;
        } else {
            A[idx] = C[j];
            j++;
        }
        idx++;
    }
    
    while (i < n1) {
        A[idx] = B[i];
        idx++;
        i++;
    }
    
    while (j < n2) {
        A[idx] = C[j];
        idx++;
        j++;
    }
}

function mergeSort(A[], l, r){
    if(l == r) return; // base case
    
    mid = (l + r) / 2;
    mergeSort (A, l, mid);
    mergeSort (A, mid + 1, r);
    merge(A, l, mid, r);
}
```

### Complexity Analysis:
If we divide the arrays in two halves, we will have a tree structure as:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/903/original/Screenshot_2023-10-25_at_4.22.50_PM.png?1698231187" width=400/>
<br/><br/>
The time taken at every level is the time taken by merging the arrays which will be O(N).

Height of Tree / Number of Levels - O(log N)
At each level, work done is O(N)

**Hence, Time Complexity:** O(N * log(N))

**Space Complexity:** O(N)
For recursive stack, we require O(logN) space. And at every level, we are using O(N) space for merging but since we are freeing that as well. We are utilizing O(N) in total merging. Thus, space complexity is O(N) 

> Merge sort is stable as arrangement of elements is taking place at merge step which is essentially maintaining the relative order of elements.



## Stable Sort

### Definition:
Relative order of equal elements should not change while sorting w.r.t a parameter.

### Examples

A[ ] = {6, 5, 3, 5}
After Sorting
A[ ] = {3, 5, 5, 6}

In this case, which 5 comes first, which later, doesn't matter since it is just a singular data.

But in actually scenario the objects to be sorted is collection of data.

> Scenario: Let's talk about an Airport checkin line!
> It should be First Come first serve, whoever comes first should be allowed first to checkin. 
> But according to airline, all the members are not same. Some would be economic, business class, priveledged/ priorty...
> Say Anand(economic class) is standing and Amir(economic class) comes and tries to move ahead Anand, will Anand be okay with it? Not Really!
> Say Anupriya(Business Class), now Anand would be okay!
> The above example explains why stable sorting is important.

**Another Example:**

| Name | Marks |
| -------- | -------- |
| A     | 8     | 
| B     | 5     | 
| C     | 8     | 
| D     | 4     |
| E     | 8     | 

Sort acc to marks. In which case, if this is stable sort, A,C,E should appear in the same order.

After Sorting

| Name | Marks |
| -------- | -------- |
| D     | 4     |
| B     | 5     | 
| A     | 8     | 
| C     | 8     | 
| E     | 8     | 

## Inplace

- No extra space
- Space complexity: O(1)


## Sort Colors

### Problem Statement
Given an array with N objects colored red, white, or blue, represented by the integers:

Red -> 0
White -> 1
Blue -> 2

The task is to sort the array so that all the red objects come first, followed by white objects, and then blue objects.
    
    
## Steps for the Brute Force Approach:

**1. Count the Occurrences:**
    - Traverse the array to count the number of occurrences of each color (0s, 1s, and 2s). This requires one pass through the array.

**2. Rebuild the Array:**
    - Once you know how many 0s, 1s, and 2s are present, rebuild the array by placing the appropriate number of 0s, followed by 1s, and then 2s.
    
### Pseudocode
    
```javascript
FUNCTION sort_colors(arr):
    # Step 1: Initialize counters
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Step 2: Count occurrences of 0s, 1s, and 2s
    FOR EACH num IN arr:
        IF num == 0:
            count_0++
        ELSE IF num == 1:
            count_1++
        ELSE IF num == 2:
            count_2++

    # Step 3: Rebuild the array
    index = 0

    # Place all 0s
    FOR i --> 1 to count_0:
        arr[index] = 0
        index++

    # Place all 1s
    FOR i --> 1 to count_1:
        arr[index] = 1
        index++

    # Place all 2s
    FOR i --> 1 to count_2:
        arr[index] = 2
        index++

    RETURN arr 
```
    
## Optimisation
    
### Initialization:
We will use three pointers to solve this problem:
1. low will track the boundary between red and white objects.
2. mid will traverse the array.
3. high will track the boundary between blue and white objects.

Initially, set low = 0, mid = 0, and high = N-1.

### Traversal:
**Traverse the array using the mid pointer.**
- Depending on the value at arr[mid], perform the following actions:
    - If arr[mid] == 0 (Red): Swap arr[mid] and arr[low], increment both low and mid. This ensures that red objects are placed in the correct region.
    - If arr[mid] == 1 (White): Simply increment mid. White objects are already in the correct region.
    - If arr[mid] == 2 (Blue): Swap arr[mid] and arr[high], and decrement high. The mid pointer is not incremented in this case because the swapped element from the high position needs to be processed.

### Termination:
The process continues until mid surpasses high. At this point, all objects are sorted in the correct order.

### Example Walkthrough
Let's consider an example array:
arr=[2, 0, 2, 1, 1, 0]

**Initial State:**
low = 0, mid = 0, high = 5

**Array: 2, 0, 2, 1, 1, 0**

### Iteration 1:
> arr[mid] = 2: Swap mid & high, high- -
> **New State:** low = 0, mid = 0, high = 4
> **Array: 0, 0, 2, 1, 1, 2**

### Iteration 2:
> arr[mid] = 0: Swap mid & low, low++, mid++
> **New State:** low = 1, mid = 1, high = 4
> **Array: 0, 0, 2, 1, 1, 2**

### Iteration 3:
> arr[mid] = 0: Swap mid & low, low++, mid++
> **New State:** low = 2, mid = 2, high = 4
> **Array: 0, 0, 2, 1, 1, 2**

### Iteration 4:
> arr[mid] = 2: Swap mid & high, high- -
> **New State:** low = 2, mid = 2, high = 3
> **Array: 0, 0, 1, 1, 2, 2**

### Iteration 5:
> arr[mid] = 1: Increment mid.
> **New State:** low = 2, mid = 3, high = 3
> **Array: 0, 0, 1, 1, 2, 2**

### Iteration 6:
> arr[mid] = 1: Increment mid.
> **New State:** low = 2, mid = 4, high = 3
> **Array: 0, 0, 1, 1, 2, 2**

Termination:
mid = 4 is now greater than high = 3. The loop terminates.
Final sorted array: 0, 0, 1, 1, 2, 2
    
### Pseudocode
```javascript
function dutch_national_flag(arr) {
    low=0, mid=0, high=len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    
    return arr
}
```
    
### Complexity
    T.C = O(N)
    S.C = O(1)
