# DSA: Arrays 1

## Introduction To Arrays

### Definition

Array is the collection of same types of data. The datatype can be of any type i.e, int, float, char, etc. Below is the declaration of the array:
```
int arr[n];
```
Here, ‘int’ is the datatype, ‘arr’ is the name of the array and ‘n’ is the size of an array. 
We can access all the elements of the array as arr[0], arr[1] ….. arr[n-1]. 

**Note:** Array indexing starts with 0.

> Why indexing starts at 0 ? (Optional, discuss only if asked by someone)

An array arr[i] is interpreted as *(arr+i). Here, arr denotes the address of the first array element or the 0 index element. So *(arr+i) means the element at i distance from the first element of the array.

---

### Question
What will be the indices of the first and last elements of an array of size **N**?

### Choices
- [ ] 1,N
- [x] 0,N-1
- [ ] 1,N-1
- [ ] 0,N

---

### Print all elements of the array

The elements of arrays can be printed by simply traversing all the elements. Below is the pseudocode to print all elements of array.

```
function print_array(arr[], n){
    for(i -> 0 to n-1){
        print(arr[i]);
    }
}
```


---
### Question

What is the time complexity of accessing element at the ith index in an array of size **N**?

### Choices
- [ ] O(N)
- [x] O(1)
- [ ] O(N*N)
- [ ] O(log(N)).

---


### Question
```
int arr[5] = {5,-4,8,9,10};
```
Which of the following statements correctly prints the sum of the 1st and 5th elements of the array?

### Choices
- [ ] print(arr[0] + arr[5])
- [x] print(arr[0] + arr[4])
- [ ] print(arr[1] + arr[5])
- [ ] print(arr[1] + arr[4])

---

## Problem 1 Reverse the array


### Problem Statement

Given an array arr of size 'N'. Reverse the entire array.

### TestCase:

#### Input:
```
N = 5
arr = {1,2,3,4,5}
```

#### Output:

```
arr = {5,4,3,2,1}
```

### Approach

The simplest approach to solve the problem is to keep two pointers at the end, traverse the array till middle element and swap first element with last element, second with second last, third with third last and so on.
![](https://i.imgur.com/xUDocWR.png)

**What should be the stopping condition?**
Say N = 6

| i     | j      | swap            |
| -------- | -------- |  -------- |
| 0     | 5     | A[0] & A[5]     |
| 1     | 4     | A[1] & A[4]     |
| 2     | 3     | A[2] & A[3]     | 
| 3     | 2     | STOP   | 

Say N = 5

| i     | j      | swap            |
| -------- | -------- |  -------- |
| 0     | 4     | A[0] & A[4]     |
| 1     | 3     | A[1] & A[3]     |
| 2     | 2     | STOP     |

We can stop as soon as $i>=j$


### Pseudocode

```
Function reverse(arr[], N, start, end){
    int i = start;
    int j = end;
    while(i < j) {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++;
        j--;
    }
}

Function solve(arr[], int N) {
    return reverse(arr, N, 0, N-1);
}
```

### Complexity:
**Time Complexity - O(N).
Space Complexity - O(1).**

---
## Problem 2 Rotate K times


Given an array 'arr' of size 'N'. Rotate the array from right to left 'K' times. (i.e, if K = 1, last element will come at first position,...)

### TestCase:

#### Input:
```
N = 5
arr = {1,2,3,4,5}
k = 2

```

#### Output:

```
arr = {4,5,1,2,3}
```

### Explanation:

Initially the array is:

| 1   | 2   | 3   | 4   | 5   |

After 1st rotation:

| 5   | 1   | 2   | 3   | 4   |

After 2nd rotation:

| 4   | 5   | 1   | 2   | 3   |


## BruteForce Approach

Simple approach is to rotate the array one element at a time.

### Pseudocode

```
Function rotateK(arr[], N, K){
    for(i -> 0 to K-1){
        temp = arr[N-1];
        for(j -> N-1 to 1){
            arr[j] = arr[j-1];
        }
        arr[0] = temp;
    }
}
```

### Complexity:
**Time Complexity - O(N*k).
Space Complexity - O(1).**


## Optimized Appraoch Observations

* After K rotations, last K elements become 1st K elements and rest elements will go at back.
    For example - Suppose we have an array arr as shown below and k = 3.
    `1 2 3 4 5 6 7`
    After 1st rotation, k=1:
    `7 1 2 3 4 5 6`
    After 2nd rotation, k=2:
    `6 7 1 2 3 4 5`
    After 3rd rotation, k=3:
    `5 6 7 1 2 3 4`
So, we have observed that last 3(K=3) elements i.e, `5 6 7` comes in front and rest elements appear at the end.
    
Therefore, we will first reverse the entire array, then reverse first K elements individually and then next N-K elements individually.
```   
1 2 3 4 5 6 7    //Given Array, K=3

7 6 5 4 3 2 1    //Reversed Entire Array
    
5 6 7 4 3 2 1    //Reversed first K elements

5 6 7 1 2 3 4    //Reversed last N-K elements    
```


## For reversing part of an array
To our function for reversing array, we can simply pass the start and end index of the part of the array we want to reverse.


### Pseudocode
```
Function countgreater(arr[], N, k){
    reverse(arr, N, 0, N-1); 
    reverse(arr, N, 0, K-1);
    reverse(arr, N, K, N-1);
}
```
    
### Edge Case

K might be very large but if we observe carefully then after N rotations the array comes to its initial state.
Hence, K rotation is equivalent to K%N rotations.

    
Suppose we have an array:
    `1 2 3 4`
After 1st rotation, the array becomes:
    `2 3 4 1`
After 2nd rotation, the array becomes:
    `3 4 1 2`
After 3rd rotation, the array becomes:
    `4 1 2 3`
Afer 4th rotation, the array becomes:
    `1 2 3 4`
Hence, we have concluded that after **N** rotations, the array become same as before 1st rotation.

### Final Pseudocode
```
Function countgreater(arr[], N,  K){
    K = k % N;
    reverse(arr, N, 0, N-1);
    reverse(arr, N, 0, K-1);
    reverse(arr, N, K, N-1);
}
```
    
### Complexity:
**Time Complexity - O(N).
Space Complexity - O(1).**


---
## Dynamic Arrays


### Question:
What is the drawback of normal arrays?

### Issue:
The size has to be declared before hand.


## Dynamic Arrays
* A dynamic array is an array with a big improvement: automatic resizing. 
* It expands as you add more elements. So you don't need to determine the size ahead of time.

### Strengths:
**Fast lookups:** Just like arrays, retrieving the element at a given index takes 
O(1) time.
**Variable size:** You can add as many items as you want, and the dynamic array will expand to hold them.

### Weaknesses:
> Note: We'll study more about it later, below is just an overview.

**Slow worst-case appends:** 
* Usually, adding a new element at the end of the dynamic array takes O(1) time. 
* But if the dynamic array doesn't have any room for the new item, it'll need to expand, which takes O(n) time.
    * It is because we have to take a new array of bigger size and copy all the elements to a new array and then add a new element. 
    * So, Time Complexity to add a new element to Dynamic array is **O(1) amortised**.
* Amortised means when most operations take **O(1)** but some operations take **O(N)**.


### Dynamic Arrays in Different Languages

### Java
```
ArrayList<String> al = new ArrayList<>(); //Arraylist is created
```

```
al.add("50"); //50 is inserted at the end
```

```
al.clear(); // al={} 
```

```
for (int i = 0; i < al.size(); i++) {
    System.out.print(al.get(i) + " ");
}                                        //iterating the Arraylist
```

### C++
```
vector<int> a; //vector is created
```
```
a.push_back(60); 
//a = {10, 20, 30, 40, 50, 60} after insertion at end
```

```
a.clear(); // a={} 
```
```
for(int i=0; i<a.size(); i++) {
    cout<<a[i];
}                             //iterating the vector
```

### Python

```
thislist = [] //created list
```

```
thislist.append("orange") //added orange at end
```

```
thislist.clear()    //cleared the list
```

```
for i in range(len(thislist)):
  print(thislist[i])  //iterating on the list
```


---
## Problem 3 Stock Portfolio Performance Tracking 


## Problem 
Tracking the performance of stocks over time is crucial for making informed decisions. You want to develop a feature for a banking app that allows users to quickly assess their stock portfolio's profit or loss over specified periods. To efficiently calculate the total profit or loss over any given range of time, you decide to implement this feature using the prefix sums technique. 

## Problem Statement
Given an array representing the daily profit or loss from a particular stock over a period of days, write a function that calculates the total profit or loss over a given range of days. The function should efficiently handle multiple queries for different ranges without recalculating the sum for each query.

### Example

Stock_Prices[ ] = [-5, 10, 20, 40, 50, -10, 80, -90, -20, -10]

Queries (Q) 

| Start Day | End day | Net Stock Price |
| -------- | -------- | -------- |
| 0   | 9     | 65    |
| 1    | 4     | 120   |
| 0    | 0     | -5   |
| 7    | 9     | -120   |
| 2    | 7     | 90   |

The problem is same as calculating sum of elements within a given range. Let's explore it further.

### Simplified Problem Statement

Given N elements and Q queries. For each query, calculate sum of all elements from L to R [0 based index].

### Example:

A[ ] = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]

Queries (Q) 

| L | R | Solution |
| -------- | -------- | -------- |
| 4    | 8     | 9    |
| 3    | 7     | 10   |
| 1    | 3     | 12   |
| 0    | 4     | 14   |
| 7    | 7     | -9   |

## Brute Force Approach

For each query Q, we iterate and calculate the sum of elements from index L to R

### Pseudocode

```cpp
Function querySum(Queries[][], Array[], querySize, size){
     for(i -> 0 to Queries.length-1){
        L  = Queries[i][0]
        R = Queries[i][1]
        
        sum = 0
        for( j -> L to R){
           sum += Array[j]
        }
        print(sum)
     }
}
```
***Time Complexity  : O(N * Q)**
**Space Complexity : O(1)***

>Since Time complexity of this approach is O(N * Q) then in a case where there are 10^5 elements & 10^5 queries where each query is (L=0 and R=10^5-1) we would encounter **TLE** hence this approach is Inefficient

---
### Question
Given the scores of the 10 overs of a cricket match
2, 8, 14, 29, 31, 49, 65, 79, 88, 97
How many runs were scored in just 7th over?

### Choices
- [x] 16
- [ ] 20
- [ ] 18
- [ ] 17


### Explanation
Total runs scored in over 7th  : 65 - 49 = 16 
(score[7]-score[6])

---

### Question
Given the scores of the 10 overs of a cricket match
2, 8, 14, 29, 31, 49, 65, 79, 88, 97
How many runs were scored from 6th to 10th over(both included)?

### Choices
- [x] 66
- [ ] 72
- [ ] 68
- [ ] 90

### Explanation
Total runs scored in over 6th to 10th : 97 - 31 = 66 
(score[10]-score[5])

---

### Question
Given the scores of the 10 overs of a cricket match
2, 8, 14, 29, 31, 49, 65, 79, 88, 97
How many runs were scored in just 10th over?


### Choices

- [ ] 7
- [ ] 8
- [x] 9
- [ ] 10

### Explanation
Total runs scored in over 6th to 10th : 97 - 88 = 9 
(score[10]-score[9])

---

### Question
Given the scores of the 10 overs of a cricket match
2, 8, 14, 29, 31, 49, 65, 79, 88, 97
How many runs were scored from 3rd to 6th over(both included)?

### Choices

- [ ] 70
- [ ] 40
- [ ] 9
- [x] 41

### Explanation
Total runs scored in over 3rd to 6th : 49-8 = 41 
(score[6]-score[2])

---

### Question
Given the scores of the 10 overs of a cricket match
2, 8, 14, 29, 31, 49, 65, 79, 88, 97
How many runs were scored from 4th to 9th over(both included)?

### Choices

- [ ] 75
- [ ] 80
- [x] 74
- [ ] 10

### Explanation
Total runs scored in over 4th to 9th : 88 - 14 = 74 
(score[9]-score[3])

---

## Observation for Optimised Solution

* On observing cricket board score, we can say that queries can be answered in just constant time since we have cummulative scores.

* In the similar manner, if we have cummulative sum array for the above problem, we should be able to answer it in just constant time.

* We need to create cumulative sum or <B>prefix sum array</B> for above problem.

</div>

### How to create Prefix Sum Array ?


pf[i] = sum of all elements from 0 till ith index.

<!-- </div>  -->

### Example
Step1:-
Provided the intial array:-
| 2   | 5   | -1   | 7   | 1   |
| --- | --- | --- | --- | --- |

We'll create prefix sum array of size 5 i.e. size equal to intial array. 
`Initialise pf[0] = initialArray[0]`

|  2  | -  | -  |  -  |  -   |
| --- | --- | --- | --- | --- |

|  2  | 7  | -  |  -  |  -   |
| --- | --- | --- | --- | --- |

|  2  | 7  | 6 |  -  |  -   |
| --- | --- | --- | --- | --- |

|  2  | 7  | 6 |  13  |  -   |
| --- | --- | --- | --- | --- |

|  2  | 7  | 6 |  13  |  14  |
| --- | --- | --- | --- | --- |


Finally we have the prefix sum array :-

|  2  | 7  | 6 |  13  |  14  |
| --- | --- | --- | --- | --- |

---

### Question
Calculate the prefix sum array for following array:-

| 10  | 32  | 6   | 12  | 20  |  1  |
| --- | --- | --- | --- | --- |:---:|

### Choices
- [x] `[10,42,48,60,80,81]`
- [ ] `[10,42,49,60,79,81]`
- [ ] `[42,48,60,80,81,10]`
- [ ]  `[15,43,58,61,70,82]`

---

### Brute Force 

Below is the Brute Force Code to create Prefix Sum Array

```cpp=
pf[N]
for(i -> 0 to N-1){

    sum = 0;
    
    for(j -> 0 to i) {
        sum = sum + A[j]
    }
    
    pf[i] = sum;
} 
```


                
## Observation for Optimising Prefix Sum array calculations

pf[0] = A[0]
pf[1] = A[0] + A[1]
pf[2] = A[0] + A[1] + A[2]
pf[3] = A[0] + A[1] + A[2] + A[3]
pf[4] = A[0] + A[1] + A[2] + A[3] + A[4]

* Can we observe that we are making redundant calculations?

* We could utilise the previous sum value.
    * pf[0] = A[0]
    * pf[1] = pf[0] + A[1]
    * pf[2] = pf[1] + A[2]
    * pf[3] = pf[2] + A[3]
    * pf[4] = pf[3] + A[4]

* **Generalised Equation is:** ```pf[i] = pf[i-1] + A[i]```

## Optimised Code:

```cpp=
pf[N]
pf[0] = A[0];
for(i -> 1 to N-1){
    pf[i] = pf[i-1] + A[i];  
} 
```
* Time Complexity: O(N)

### How to answer the Queries ?


A[ ]  = [-3, 6, 2, 4,  5,  2,  8, -9,  3,  1]

pf[ ] =[-3, 3, 5, 9, 14, 16, 24, 15, 18, 19]

| L | R | Solution | |
| -------- | -------- | -------- | -------- |
| 4    | 8     | pf[8] - pf[3]   | 18 - 9 = 9 |
| 3    | 7     | pf[7] - pf[2]   |15 - 5 = 10   |  
| 1    | 3     | pf[3] - pf[0]   |9 - (-3) = 12   | 
| 0    | 4     | pf[4]           |14   |  
| 7    | 7     | pf[7] - pf[6]   |15 - 24 = -9   |  



## Generalised Equation to find Sum:

sum[L R] = pf[R] - pf[L-1]

Note: if L==0, then sum[L R] = pf[R]


### Complete code for finding sum of queries using Prefix Sum array:

```cpp =
Function querySum(Queries[][], Array[], querySize, size){  
    //calculate pf array
    pf[N]
    pf[0] = A[0];
    for(i -> 1 to N-1){
        pf[i] = pf[i-1] + A[i];  
    } 
    
    //answer queries
    for( i -> 0 to Queries.length-1){
        L  = Queries[i][0];
        R = Queries[i][1];

        if(L == 0) {
            sum = pf[R]
        }
        else {
            sum = pf[R] - pf[L - 1];
        }
        
        print(sum);
    }
}
```
***Time Complexity  : O(N+Q)**
**Space Complexity : O(N)***



### Space Complexity can be further optimised if you modify the given array.

```cpp
Function prefixSumArrayInplace(Array[], size){
    for(i -> 1 to size-1){
        Array[i] = Array[i-1] + Array[i];
    }
}
```
***Time Complexity  : O(N)**
**Space Complexity  : O(1)***


---
## Problem 4 Sum of even indexed elements


Given an array of size N and Q queries with start (s) and end (e) index. For every query, return the sum of all **even indexed elements** from **s to e**.

### Example

```plaintext
A[ ] = { 2, 3, 1, 6, 4, 5 }
Query :
 1 3
 2 5
 0 4
 3 3
 
Ans:
 1
 5
 7
 0
```
### Explanation:
* From index 1 to 3, sum: A[2] = 1
* From index 2 to 5, sum: A[2]+A[4] = 5
* From index 0 to 4, sum: A[0]+A[2]+A[4] = 7
* From index 3 to 3, sum: 0

### Brute Force
How many of you can solve it in $O(N*Q)$ complexity?
**Idea:** For every query, Iterate over the array and generate the answer.

### Sum of even indexed elements Observation for Optimisation


Whenever range sum query is present, we should think in direction of **Prefix Sum**.

**Hint 1:** Should we find prefix sum of entire array?
**Expected:** No, it should be only for even indexed elements.

**We can assume that elements at odd indices are 0 and then create the prefix sum array.**


Consider this example:-

```
  A[] = 2  3  1  6  4  5
PSe[] = 2  2  3  3  7  7
```

> Note: PSe[i] denotes sum of all even indexed elements from 0 to i<sup>th</sup> index.


If **i is even** we will use the following equation :- 
<div class="alert alert-block alert-warning">
PSe[i] = PSe[i-1] + A[i]
</div> 

If **i is odd** we will use the following equation :-
<div class="alert alert-block alert-warning">
PSe[i] = PSe[i-1]
</div> 


---
### Question
Construct the Prefix Sum for even indexed elements for the given array
[2, 4, 3, 1, 5]

### Choices
- [ ] 1, 6, 9, 10, 15
- [x] 2, 2, 5, 5, 10
- [ ] 0, 4, 4, 5, 5
- [ ] 0, 4, 7, 8, 8
 
 
### Explanation

We will assume elements at odd indices to be 0 and create a prefix sum array taking this assumption.
So ```2 2 5 5 10``` will be the answer.

---

### Pseudocode


```cpp
Function sumOfEvenIndexed(Array[], Queries[][], N){
    // prefix sum for even indexed elements
    PSe[N]; 
    
    PSe[0] = Array[0]
    
    for(i -> 1 to N-1){
        if(i % 2 == 0){
            PSe[i] = PSe[i-1] + Array[i];
        }
        else {
            PSe[i] = PSe[i-1]; 
        }
    }
    for(i -> 0 to Queries.length-1) {
        s = Queries[i][0]  
        e = Queries[i][1]
        if(s == 0){
            print(PSe[e])
        }
        else {
            print(PSe[e]-PSe[s-1])
        }         
            
    }
 
}
```
### Complexity
-- TC - $O(n)$
-- SC - $O(n)$

