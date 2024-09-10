# Hashing 2: Problems


## Problem 1 First non repeating element

### Problem Statement

Given N elements, find the first non-repeating element. 

### Example

Input 1:
```
N = 6
```
|  1  |  2  |  3  |  1  |  2  |  5  |
|:---:|:---:|:---:|:---:|:---:|:---:|

Output1 :
```plaintext
ans = 3
```

|  1  |  2  |  3  |  1  |  2  |  5  |
|:---:|:---:|:---:|:---:|:---:|:---:|

Input 2:
```
N = 8
```

|  4  |  3  |  3  |  2  |  5  |  6  |  4  |  5  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

Output 2:
```plaintext
ans = 2
```
Input 3:
```
N = 7
```

|  2  |  6  |  8  |  4  |  7  |  2  |  9  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

Output 3:
```plaintext
ans = 6
```

## Solution
### Idea 1

* Use Hashmap to store the frequency of each element. Store <**key**:element, **value**:frequency>.
* Iterate over the Hashmap and find the element with frequency 1.

### Flaw in Idea 1

* When we store in Hashmap, the order of elements is lost; therefore, we cannot decide if the element with frequency 1 is first non-repeating in the order described in the Array.

### Idea 2

* Use Hashmap to store the frequency of each element. Store `<key:element, value:frequency>`.
* Instead of Hashmap, iterate over the Array from the start. If some element has a frequency equal to one, then return that element as answer.


### Pseudeocode
```cpp
Function firstNonRepeating(A[])
{
   Hashmap<integer,integer> mp;
   n = A.length
   
   for(i -> 0 to n - 1)
   {
      if(mp.Search(A[i]) == true)
      {
         mp[A[i]] ++
      }
      else{
        mp.Insert(A[i],1)
      }
   }
   for(i -> 0 to n - 1)
   {
       if(mp[A[i]] == 1)
       {
          return A[i]
       }
   }
   return - 1
}
```

Time Complexity : **O(N)**
Space Complexity : **O(N)**


---
## Problem 2 Pair Sum K


### Problem Statement
Given arr[N] and K, check if there exists a pair(i, j) such that,
```kotlin
arr[i] + arr[j] == K && i != j
```

### Example
Let's say we have an array of 9 elements and K, where K is our target sum, 

| Index |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
|:-----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Array |  8  |  9  |  1  | -2  |  4  |  5  | 11  | -6  |  4  |

K = 6: arr[2] + arr[5] : such a pair exists
K = 22: does not exist
K = 8: arr[4] + arr[8]: such a pair exists

Hence if K = `6` or `8` the answer is `true`, for K = `22`, it will be `false`.

---

### Question
Check if there exists a pair(i, j) such that, arr[i] + arr[j] == K && i != j in the given array A = [3, 5, 1, 2, 1, 2] and K = 7.


### Choices 
- [x] true
- [ ] false

---


### Question
Check if there exists a pair(i, j) such that, arr[i] + arr[j] == K && i != j in the given array A = [3, 5, 1, 2, 1, 2] and K = 10.


### Choices 
- [ ] true
- [x] false

---
## Pair Sum K Brute Force

### Idea 1: 
Iterate on all pairs(i, j) check if their sum == k

### Example 2:
Take another example of arr[5] 
| Index  |  0  |  1  |  2  |  3  |  4  |
|:------:|:---:|:---:|:---:|:---:|:---:|
| arr[5] |  3  |  2  |  6  |  8  |  4  |

We can have following cases of pairs from an array of size 5



<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/583/original/upload_3a54ba208d44d76c7063510180eb6da1.png?1695221986" alt= “” width ="500" height="400">

* Here, since we are not allowed to consider pairs where i == j these diagonal elements (marked in red) will not be considered. 
* Now, as you can see the upper (blue) and lower (yellow) triangles represent the same pairs (order of pair doesn't matter here) our program would work with either one of these triangular parts.  

*Now, considering upper triangle -*
### Observation:

|  i  | j loops from [i...(N - 1)] |
|:---:|:------------------------:|
|  0  |          [0..N-1]           |
|  1  |          [1..N-1]          |
|  2  |          [2..N-1]          |
|  3  |          [3..N-1]          |
|  4  |          -          |

Here for every index of i, j loops from i to N - 1

For an `arr[i]`, the target will be `K-arr[i]`

### Pseudocode:
```kotlin
function checkPair(arr[], K){
    
    N = arr.length
    for(i -> 0 to N - 1){
        //target: K-arr[i]
        for(j -> i to N - 1){
            if(arr[j] == K - arr[i]){ // arr[i] + arr[j] == K
                return true;
            }
        }    
    }
    return false;
}

```

### Complexity
**Time Complexity:** O(N^2)
**Space Complexity:** O(1)


---
## Pair Sum K Optimization with HashSet(Doesn't Work)

* We can insert all elements in the set initially.
* Now, iterate over every arr[i] and check if K-arr[i] is present in the set. If yes, return tue, else false.


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/055/050/original/Screenshot_2023-10-27_at_4.11.32_PM.png?1698403308" alt= “” width ="600" height="200">


--- 
**ISSUE: (Edge Case)**

* For even K value, say arr[i] is K/2 and only one occurrence of it is present. 
* Eg: A[] = {8, 9, 2, -1, 4, 5, 11, -6, 4}; K=4, we will end up considering 2(present at index 2) two times.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/055/051/original/Screenshot_2023-10-27_at_4.11.39_PM.png?1698403359" alt= “” width ="600" height="200">


We can see the above logic isn't working

### Resolution:
We need not insert all elements into set at once. Rather only insert from [0, i - 1].


---
## Pair Sum K Optimization with HashSet(Works)


At ith index: Hashset should contain all the elements:[0...i - 1]

Let's take an example,

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/585/original/upload_a4b1e5d20d55238fbec1e78884238f96.png?1695222089" alt= “” width ="600" height="200">



* Initially set is empty.
* For every element at ith index, search for target (arr[i] - K) in set.
* If found, it means it must have been previously inserted. If not, we'll insert arr[i], because in future if we'll find a pair, we'll be able to get the current element. 

Let's take another example,


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/586/original/upload_68f2bd2ab73bc0bb5384b5b758375222.png?1695222113" alt= “” width ="600" height="200">



### Pseudocode:
```kotlin
function targetSum(arr[], K){
    N = arr.length;
    Hashset<integer> bs;
    
    for(i -> 0 to N - 1){
        //target = K - arr[i]
        if(bs.contains(K - arr[i])){
            return true;
        }
        else {         
            bs.add(arr[i]);
        }
    }
    return false;
}
```
---

### Question
Count pairs(i, j) such that, arr[i] + arr[j] == K && i != j in the given array.
A = [3, 5, 1, 2, 1, 2] and K = 3.

Note that (i, j) and (j, i) considered as same.

### Choices 
- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4

### Explanation


In the given array A = [3, 5, 1, 2, 1, 2], pairs with sum = 3 are:

| Pairs(i, j)  | arr[i] | arr[j] |
| ------ | ------ | ------ |
| {2, 3} |   1    |   2    |
| {2, 5} |   1    |   2    |
| {3, 4} |   2    |   1    |
| {4, 5} |   1    |   2    |


---
## Problem 3 Count no. of pairs with sum K


### Problem Statement
Given an `arr[n]`, count number of pairs such that 
```kotlin
arr[i] + arr[j] = K && i != j
```
Note that (i, j) and (j, i) considered as same.

### Example

Provided we have an arr[8] and K = 10, we have 
| Index  |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |
|:------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| arr[8] |  2  |  5  |  2  |  5  |  8  |  5  |  2  |  8  |

**Pairs:**

| Pairs: 9 |
|:--------:|
|  {0, 4}  |
|  {0, 7}  |
|  {1, 5}  |
|  {1, 3}  |
|  {2, 4}  |
|  {2, 7}  |
|  {3, 5}  |
|  {4, 6}  |
|  {6, 7}  |

Here (i, j) and (j, i) considered as same. 

### Optimised Approach(Same as in previous question)
* Similar to our previous problem, we'll be searching for our target. 
* This time we also need to consider the frequency of how many times a particular element appeared, so we shall be maintianing a map.



<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/587/original/upload_9aa1cbc2130f91fa21781e92fe645f64.png?1695222159" alt= “” width ="500" height="200">



### Pseudocode:
```kotlin
function countTargetSum(arr[], K){
    N = arr.length;
    Hashmap<integer, integer> hm;
    
    c = 0;
    
    for(i -> 0 to n - 1){
        //target = K-arr[i]
        if(hm.contains(K - arr[i])){
            c = c + hm[K - arr[i]] //freq of target = pairs
        }
        
        //insert arr[i]
        if(hm.contains(arr[i])){
            hm[arr[i]]++;
        }
        else{
            hm[arr[i]] = 1;
        }
    }
    return c;
}

```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)


---
## Problem 4 Subarray sum 0


### Problem Statement

Given an array of N elements, check if there exists a subarray with a sum equal to 0.

### Example
**Input:**

N = 10


|  2  |  2  |  1  | -3  |  4  |  3  |  1  | -2  | -3  |  2  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

**Output:**
if we add elements from index 1 to 3, we get 0; therefore, the answer is **true**.

### Solution
* Traverse for each subarray check if sum == 0.
   * Brute Force: Create all Subarrays, Time complexity: **O(n<sup>3</sup>)**.
   * We can optimize further by using **Prefix Sum** or **Carry Forward** method and can do it in Time Complexity: **O(n<sup>2</sup>)**.
   * How can we further optimize it?

### Observations

* Since we have to find sum of a subarrays(range), we shall think towards **Prefix Sum**.

Initial Array: -


|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  2  |  2  |  1  | -3  |  4  |  3  |  1  | -2  | -3  |  2  |

Prefix sum array: -

|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  2  |  4  |  5  |  2  |  6  |  9  | 10  |  8  |  5  |  7  |

We need a subarray with **sum(i to j) = 0**
Using Prefix Sum Array,
**PrefixSum[j] - PrefixSum[i-1] = 0
PrefixSum[j] = PrefixSum[i-1]**

It implies, if there exist duplicate values in Prefix Sum Array, then the sum of a subarray is 0.

Example,

```cpp
PrefixSum[2] = 5
PrefixSum[8] = 5
sum of elements in intial array from index 3 to 8 = 0
```

**Summary**
* If numbers are repeating in Prefix Sum Array, then there exists a subarray with sum 0.
* Also, if the Prefix Sum Array element is 0, then there exists a subarray with sum 0.
    * Example: 
        * A[] = {-2, -1, 3, 5}
        * PrefixSum[] = {-2, -3, 0, 5}
        * Here, 0 in PrefixSum Array implies that there exist a subarray with sum 0 starting at index 0.
          

### Approach

* Calculate prefix sum array.
* Traverse over elements of prefix sum array.
  * If the element is equal to 0, return true.
  * Else, insert it to HashSet.
* If the size of the prefix array is not equal to the size of the hash set, return true.
* Else return false.

### Pseudeocode
```cpp
// 1. todo calculate prefix sum array

// 2.
Function checkSubArraySumZero(PrefixSumArray[])
{
  Hashset<integer> s
  for(i -> 0 to PrefixSumArray.length - 1 )
  { 
    if(PrefixSumArray[i] == 0)
    {
       return true
    }
    s.insert(PrefixSumArray[i])
  }
  if (s.size != PrefixSumArray.size) 
      return true
  return false
}
```
Time Complexity : **O(N)**
Space Complexity : **O(N)**


---
## Problem 5 Subarray with Sum K

### Problem Statement
Given an array arr[n] check if there exists a subarray with sum = K

### Example: 
We have the following array

| Index  |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
|:------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| arr[7] |  2  |  3  |  9  | -4  |  1  |  5  |  6  |  2  |  5  |

Possible subarrays for the following values of K are, 
* k = 11: {2 3 9 -4 1}, {5, 6}
* k = 10: {2 3 9 -4}
* k = 15: {-4, 1, 5, 6, 2, 5}

---


### Question
Check if there exist a subarray with sum = 110 in the given array?
A = [ 5, 10, 20, 100, 105 ]
 

### Choices 
- [x] No
- [ ] YES


---
## Subarray with Sum K Approach


To get subarray sum for any subarray in constant time, we can create a prefix sum array.

Now, a subarray sum `PF[i] - PF[j]` should be equal to `K`

OR
**a - b = K**

We can fix `a` and get the corresponding pair for it, given by `a - K`

> We can create a HashSet at the time of traversal simultaneously 
> Here, instead of creating prefix sum initially, we are calculating it while iterating through the array.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/589/original/upload_6ecbb00a34003fd352ffa8d7a52cd79c.png?1695222337" alt= “” width ="600" height="200">


 
**Edge case:**
If subarray from index 0 has sum = K.
Say, K = 10
a = 10, b = 10-10=0, now 0 won't be present in the array.
Please take below example:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/590/original/upload_0ceb31b4f16f07cfda3dc4f4283b8135.png?1695222358" alt= “” width ="600" height="200">


**To resolve this, take 0 in the set initially.**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/591/original/upload_0efad47d63c86de9d905ecc34a17410f.png?1695222380" alt= “” width ="600" height="200">


### Pseudocode:
```kotlin
function targetSubarray(arr[], K){
    N = arr.length;
    a = 0;
    
    //cumulative sum, long -> to avoid overflow
    HashSet<long integer> hs;
    hs.add(0);
    for(i -> 0 to N - 1){
        a = a + arr[i];
        
        //cumulative sum = target = a - k
        if(hs.contains(a - K)){
            //subarray exists
            return true;
        } else {
            hs.add(a);
            
        }
     
    }
    return false;
}

```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)


