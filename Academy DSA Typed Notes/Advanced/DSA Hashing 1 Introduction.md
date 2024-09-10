# Hashing 1: Introduction


## Hashmap and HashSet Introduction

### HashMap

Let's take an example:-

* Imagine we have a hotel called Reddison, which has 5 rooms.
* How can we maintain information on the status of rooms provided the hotel is old and hasn't adapted to technology yet?

Solution: The hotel may maintain a manual register for five rooms like:-

| Room no | occupied |
|:-------:|:--------:|
|    1    |   Yes    |
|    2    |    No    |
|    3    |   Yes    |
|    4    |    No    |
|    5    |    No    |


* After a few years, the hotel became a success, and the rooms increased to 1000. 
* Provided the hotel decided to adapt to technology, what is the programmatically most straightforward approach to maintain the status of rooms?
  * An array can be maintained where the index can denote the room number. 
  * If there are N rooms, we'll create an array of size + 1 where true denotes that room is occupied, and false denotes unoccupied.

* Pandemic hit, due to which footfall reduced significantly. Owner visits Numerologist who asks them to change room numbers to some random lucky numbers from [1-10<sup>9</sup>]. How can we maintain the status of the rooms now?
  * Maintain boolean array of length 10<sup>9</sup> + 1 `bool arr[10^9 + 1]`.
  * **ISSUE:** Status can be checked in O(1), but just for 1000 rooms, we require an array of size 10<sup>9</sup>.

* **Solution:** HashMaps
    * HashMap is a data structure that stores <key, value> pair.

        |  Key   |  value   |
        |:------:|:--------:|
        | 100003 | occupied |
        |   3    | occupied |
        | 10007  | occupied |


    
* **In HashMap, T.C of search is O(1) time and S.C is O(N)**   
* Key must be unique 
* Value can be anything
* **Note:** We'll discuss the internal working of Map in Advanced classes.

**In hashmap approach we can search in O(1) time and can have a space complexity of O(N)**

Let's see some questions based on Hashmap.

---

### Question

Which of the following HashMap will you use to store the population of every country?

### Choices

- [ ] HashMap<String, Float>
- [ ] HashMap<String, Double>
- [ ] HashMap<String, String>
- [x] HashMap<String, Long>

### Explanation


* Key must be unique in Hashmap, so for that reason :
  * We use the country name as the key. 
  * Since the country name is a `string`, the key would be of type `string`.
* In this case, value is a population that can be stored in `int` or `long` datatype.
* Solution:- 
`hashmap<String,long> populationByCountry`.

---


### Question

Which of the following HashMap will you use to store the no of states of every country?

### Choices

- [ ] HashMap<String, Float>
- [ ] HashMap<String, Double>
- [x] HashMap<String, INT>
- [ ] HashMap<String, String>

### Explanation

* Key must be unique in Hashmap, so for that reason :
  * We use the country name as the key. 
  * Since the country name is a `string`, the key would be of type `string`.
* We know that value can be anything. In this case : 
  * Value is the number of states stored in `int` or `long` datatype.
* Solution:- 
`hashmap<String,int> numberOfStatesByCountry`

---

### Question

Which of the following HashMap will you use to store the name of all states of every country?

### Choices

- [ ] HashMap<String, List < Float > >
- [x] HashMap<String, List < String > >
- [ ] HashMap<String, String>
- [ ] HashMap<String, Long>

### Explanation


* Key must be unique in Hashmap, so for that reason :
  * We use the country name as the key. 
  * Since the country name is a `string`, the key would be of type `string`.
* Value can be anything. In this case:
  * Value is the name of states.
  * To store them, we would require a list of strings, i.e., `vector<string>` in C++ or `ArrayList<Sting>` in Java, etc., to store the name of states.


* Solution:-
`hashmap<String,list<String>> nameOfStatesByCountry`



---



### Question

Which of the following HashMap will you use to store the population of each state in every country?

### Choices

- [ ] HashMap<String, Int>
- [ ] HashMap<String, List < Int > >
- [x] HashMap<String,HM < String , Int > >
- [ ] HashMap<String, Long>

### Explanation

* Key must be unique in Hashmap, so for that reason :
  * We use the country name as the key.
  * Since the country name is a `string`, the key would be of type `string`.
* Value can be anything. In this case :
  * We need to store the name of states with its population. 
  * We will create another hashmap with the state name as key and population as value.
* Solution:-
`hashmap<String,hashmap<String,Long>> populationOfStatesByCountry`

We can observe that:-
* **Value can be anything.**    
* **Key can only be a primitive datatype.**   


---
## HashSet

Sometimes we only want to store keys and do not want to associate any values with them, in such a case; we use HashSet.

`Hashset<Key Type>`


* **Key must be unique** 
* **Like HashMap, we can search in O(1) time in Set**

---
## HashMap and HashSet Functionalities


### HashMap
* **INSERT(Key,Value):** new key-value pair is inserted. If the key already exists, it does no change.
* **SIZE:** returns the number of keys.
* **DELETE(Key):** delete the key-value pair for given key.
* **UPDATE(Key,Value):** previous value associated with the key is **overridden** by the new value.
* **SEARCH(Key):** searches for the specified key.

### HashSet

* **INSERT(Key):** inserts a new key. If key already exists, it does no change.
* **SIZE:** returns number of keys.
* **DELETE(Key):** deletes the given key.
* **SEARCH(Key):** searches for the specified key.

**Time Complexity** of **all the operations** in both Hashmap and Hashset is **O(1)**.

Therefore, if we insert N key-value pairs in HashMap, then time complexity would be O(N) and space complexity would be O(N).

### Hashing Library Names in Different Languages



|         |  Java   |      C++      |   Python   | Js  |     C#     |
|:-------:|:-------:|:-------------:|:----------:|:---:|:----------:|
| Hashmap | Hashmap | unordered_map | dictionary | map | dictionary |
| Hashset | Hashset | unordered_set |    set     | set |  Hashset   |

## Implementations :


## Problem 1 Frequency of given elements


### Problem Statement
 Given N elements and Q queries, find the frequency of the elements provided in a query.
 
### Example

N = 10

|  2  |  6  |  3  |  8  |  2  |  8  |  2  |  3  |  8  | 10  |  6  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

Q = 4

|  2  |  8  |  3  |  5  |
|:---:|:---:|:---:|:---:|


### Solution


| Element | Frequency |
|:-------:|:---------:|
|    2    |     3     |
|    8    |     3     |
|    3    |     2     |
|    5    |     0     |

### Idea 1

* For each query, find the frequency of the element in the Array.
* TC - **O(Q*N)** and SC - **O(1)**.
>How can we improve TC?

### Approach

* First, search for the element in the Hashmap.
  * If the element does not exist, then insert the element as key and value as 1.
  * If an element already exists, then increase its value by one.
 
### Pseudeocode
```cpp
Function frequencyQuery(Q[], A[])
{
   Hashmap<integer,integer> mp;
   q = Q.length
   n = A.length
   
   for(i -> 0 to n - 1 )
   {
      if(mp.Search(A[i]) == true)
      {
         mp[Array[i]] ++
      }
      else{
        mp.Insert(A[i],1)
      }
   }
   
   for(i -> 0 to q - 1 )
   { 
        if(mp.Search(Q[i]) == true)
      {
         print(mp[Q[i]])
      }
      else{
        print("0")
      }
   }
}
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)



---
## Problem 2 Count of Distinct Elements


### Problem Statement

Given an array of N elements, find the count of distinct elements.

### Example
**Input:** 

N = 5

|  3  |  5  |  6  |  5  |  4  |
|:---:|:---:|:---:|:---:|:---:|

**Output:**

```plaintext
ans = 4
```
**Explanation:** We have to return different elements present. If some element repeats, we will count it only once. 


**Input:** 
N = 3


|  3  |  3  |  3  |
|:---:|:---:|:---:|

**Output:**
```plaintext
ans = 1
```
**Input:** 

N = 5

|  1  |  1  |  1  |  2  |  2  |
|:---:|:---:|:---:|:---:|:---:|


**Output:**
```plaintext
ans = 2
```
### Solution 

* Insert element in Hashset and return the size of HashSet.

> In Hashset, if a single key is inserted multiple times, still, its occurrence remains one.


### Pseudeocode
```cpp
Function distinctCount(Array[])
{
  hashset<integer>set;
  for(i -> 0 to Array.length - 1 )
  {
    set.insert(Array[i])
  }
  return set.size
}
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)

---
## Problem 3 Longest Substring Without Repeating Characters


### Problem Statement
Given a string s, find the length of the longest substring without repeating characters.

### Examples

**Example 1:**
Input: "abcabcbb"
Output: **3**
Explanation: The longest substring without repeating characters is "abc", which has a length of 3.


**Example 2:**
Input: "bbbbb"
Output: 1
Explanation: The longest substring without repeating characters is "b", which has a length of 1.

**Example 3:**
Input: "pwwkew"
Output: 3
Explanation: The longest substring without repeating characters is "wke", which has a length of 3.

### Brute Force Approach

**To solve this problem using a brute force approach, follow these steps:**
* Generate all possible substrings of the given string.
* For each substring, check if all characters are unique.
* Keep track of the length of the longest substring that contains unique characters.

**Example:**
For string "abcabcbb":
Generate substrings: "a", "ab", "abc", "b", "bc", "bca", ...
Check each substring for uniqueness.
The longest substring with unique characters is "abc".

### Complexity analysis of brute force approach
- Time Complexity: **O(n^3)** — Generating all substrings takes O(n^2), and checking uniqueness takes O(n).
- Space Complexity: **O(1)** — No extra space is used.


---
## Longest Substring Without Repeating Characters optimised approach


### Observations for Optimization

1) *Sliding Window Technique*: The brute force method is inefficient for larger strings. We can use a sliding window approach to optimize the solution.
2) *HashSet for Uniqueness*: Use a data structure like HashSet to keep track of characters in the current window and efficiently check for duplicates.
3) *Two-pointer Technique*: Use two pointers to represent the start and end of the current substring window.

**Optimized Approach**

We use the sliding window technique with two pointers and a hash set to solve the problem in linear time.

*Steps:*
* Initialize two pointers start and end to represent the current window.
* Use a hash set to keep track of characters in the current window.
* Move the end pointer to expand the window and include new characters.
* If a duplicate character is encountered, move the start pointer to reduce the window until the duplicate is removed.
* Update the maximum length of substrings without repeating characters as you expand the window.

**Pseudocode**
```cpp
function lengthOfLongestSubstring(s):
    initialize start = 0
    initialize maxLength = 0
    initialize hashSet = empty set

    for end = 0 to length of s - 1:
        while s[end] in hashSet:
            remove s[start] from hashSet
            increment start by 1
        add s[end] to hashSet
        maxLength = max(maxLength, end - start + 1)

    return maxLength
```

**Complexity Analysis of Optimized Approach**

* Time Complexity: **O(n)** — Each character is processed at most twice (once added and once removed).
* Space Complexity: **O(min(n,m))** — n is the length of the string, and m is the size of the character set (e.g., 128 for ASCII).


