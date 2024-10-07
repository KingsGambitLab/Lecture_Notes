# Interview Problems 2

## Problem 1 Meeting Rooms
### Problem Statement:
You are given an array of meeting time intervals where each interval is represented as [start, end] (start time is less than the end time). Your task is to find the minimum number of conference rooms required to schedule all meetings without overlap.


### Example 1:

Input: [[0, 30], [5, 10], [15, 20]]
Output: 2

**Explanation**:

- The first meeting (0, 30) starts at 0 and ends at 30.
- The second meeting (5, 10) overlaps with the first meeting, so a second room is required.
- The third meeting (15, 20) can reuse a room after the second meeting ends, resulting in a total of 2 rooms.
### Example 2:

Input: [[7, 10], [2, 4]]
Output: 1
**Explanation**:

The two meetings don’t overlap. The second room finishes at time 4, and the first one starts at time 7. Hence, only 1 room is required.


### Brute Force Approach (Inefficient)

**Idea**: For each meeting, check whether it overlaps with any other meeting and keep count of rooms.

 **Explanation**:
- Sort all meetings by start time.
- Iterate through the meetings and compare the current meeting with all previous meetings to find overlaps.
- Keep track of the maximum number of overlapping meetings (i.e., required rooms).

**Complexity**:

**Time Complexity**: O(N^2)

## Meeting Rooms Optimised Approach

### Optimized Approach Using Time Points (Sweep Line Algorithm)

**Key Insight**: 
Instead of comparing every meeting to every other meeting, we can treat the problem as a series of time points where meetings start and end. We can then track how many rooms are being used at any given time.

**Steps**:

- Record every meeting's start time as an event where a room is needed.
- Record every meeting's end time as an event where a room is freed.
- Count the rooms used at each time point and return the maximum number of rooms required.
### Pseudo code
```cpp 
function minMeetingRooms(intervals):
    n = 1000010
    // For room allocation 
    delta = array of size n initialized to 0
    
    // Step 1: Update room allocation at each time point
    for each interval in intervals:
        start_time = interval[0]
        end_time = interval[1]
        
        // A room is needed when a meeting starts
        delta[start_time] += 1
        
        // A room is freed when a meeting ends
        delta[end_time]-= 1
    
    // Step 2: Calculate the prefix sum to determine how many rooms are needed over time
    for i from 0 to n - 2:
        delta[i + 1] += delta[i]  // Accumulate the room changes over time
    
    // Step 3: Return the maximum number of rooms needed at any point in time
    return max value in delta array
```

### Compexity
**Time Complexity:** O(K + N.logK)
**Space Complexity:** O(K)

---

## Problem 3 Merge K sorted arrays
### Merge K-sorted arrays
a - [2, 3, 11, 15, 20]
b - [1, 5, 7, 9]
c - [0, 2, 4]
d - [3, 4, 5, 6, 7, 8]
e - [-2, 5, 10, 20]

We have to merge these sorted arrays.
 
### Idea
- If we want to merge two sorted arrays then we need two pointers. 
- If we want to merge three sorted arrays then we need three pointers. 
- If we want to merge K sorted arrays then we need K pointers, in which complexity becomes very high and we need to keep track of K pointers.

---


### Question
For merging K sorted arrays, which data structure would be the most efficient for this task ?

### Choices
- [ ] Linked List
- [ ] Array
- [x] Min-Heap
- [ ] Hash Table




### Explanation:

A Min-Heap is an efficient data structure choice. The Min-Heap ensures that the smallest element among all the elements in the arrays is always at the front. This allows for constant-time access to the minimum element, making it efficient to extract and merge elements in sorted order.

---

## Merge K sorted arrays Solution

### Optimized Solution
- First, we need to compare the 0th index element of every array.
- Now we use heap here.
- We will add an index 0 element of every array in the heap, in the form of element value, array number and Index of the element in particular.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/061/239/original/11.png?1704815927" width=250/>

Now take the minimum element and insert it in the resultant array,

- Now insert the next element of the list for which the minimum element is selected, like first, we have taken the fourth list element, so now insert the next element of the fourth list.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/061/240/original/22.png?1704815937" width=250/>

- Now again extract-min() from the heap and insert the next element of that list to which the minimum element belongs.
- And keep repeating this until we have done with all the elements.

### Time Complexity
**Time Complexity:** (XlogK)
Here X is a total number of elements of all arrays.


---

## Problem 4 Minimum Distance Equal Pair

### Problem Statement:
Given an array A, find a pair of indices (i, j) such that A[i] = A[j] and the absolute difference |i - j| is minimized. In simpler terms, you need to find two equal elements in the array that are the closest to each other and return the minimum distance between them.

**Example 1:**

Input: A = [7, 1, 3, 4, 1, 7]
Output: 3

**Explanation**:

- Two options exist:
a.Elements at indices 1 and 4 are both 1, so |1 - 4| = 3.
b.Elements at indices 0 and 5 are both 7, so |0 - 5| = 5.
- The minimum distance is 3.
**Example 2**:

Input: A = [1, 1]
Output: 1
**Explanation**:

The only pair of equal elements are at indices 0 and 1, so |0 - 1| = 1.

### Brute Force Approach (Inefficient):

**Idea**: 
Compare every element with every other element to find pairs of equal values and compute the difference in their indices.

**Explanation:**
For every element A[i], check all subsequent elements A[j] to see if they are equal.
Track the minimum difference between the indices of any matching pair.

**Time Complexity**: O(N^2)

**Flaws**:

The brute force method becomes inefficient as the size of the array increases due to the quadratic time complexity.

## Minimum Distance Equal Pair Optimised Approach
### Optimized Approach Using Hash Map:
**Key Insight**: Instead of comparing every element with every other element, use a hash map to store the last seen index of each element.
**Steps**:
As you traverse the array, if an element has been seen before, calculate the distance between the current index and the last seen index from the hash map.
Keep track of the minimum distance found so far.


### Dry Run:
- Consider A = [7, 1, 3, 4, 1, 7].
- Initialize an empty hash map: lastSeen = {}.
- Initialize minDistance = ∞.


 | Index (i) 	| Element(A[i]) 	| lastSeen Map             	| Distance Calculation 	| minDistance 	|
|-----------	|---------------	|--------------------------	|----------------------	|-------------	|
| 0         	| 7             	| {7: 0}                   	| -                    	| ∞          	|
| 1         	| 1             	| {7: 0, 1: 1}             	| -                    	| ∞          	|
| 2         	| 3             	| {7: 0, 1: 1, 3: 2}       	| -                    	| ∞          	|
| 3         	| 4             	| {7: 0, 1: 1, 3: 2, 4: 3} 	| -                    	| ∞          	|
| 4         	| 1             	| {7: 0, 1: 1, 3: 2, 4: 3} 	| 4-1                  	| 3           	|
| 5         	| 7             	| {7: 0, 1: 4, 3: 2, 4: 3} 	| 5-0                  	| 3           	|
### Pseudo code

```cpp
function findMinDistance(A):
    Create hash map 'lastSeen'
    Set 'minDistance' to infinity

    for i from 0 to len(A):
        if A[i] in 'lastSeen':
            distance = abs(i - lastSeen[A[i]])
            minDistance = min(minDistance, distance)
        
        lastSeen[A[i]] = i

    if minDistance < infinity:
        return minDistance
    return -1  # No pair found
```
    


### Complexity Analysis:
**Time Complexity**: O(n)
**Space Complexity**: O(n) 


---

## Problem 5 Minimum Window Substring 

### Problem Statement:
Given two strings s and t, find the minimum window in s which contains all characters of t (including duplicates). If no such window exists, return an empty string "".

**Example 1**:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
**Explanation**:

- The substring "BANC" in s contains all characters 'A', 'B', and 'C' from string t in the minimum length.

**Example 2**:
Input: s = "a", t = "a"
Output: "a"
**Explanation**: 
- The entire string s contains the only character 'a' from string t.

**Example 3**:
Input: s = "a", t = "aa"
Output: ""
**Explanation**: 
- The string s only contains one 'a', but t requires two 'a's. Thus, no valid window exists, and the output is "".


### Brute Force Approach (Inefficient):

**Idea**: Check every possible substring of s, and for each substring, verify if it contains all characters of t.
**Steps**:
- For every substring of s, check if it includes all characters of t by counting the occurrences of each character.
- Track the smallest valid substring.

**Complexity**: O(m^2⋅n)


## Minimum Window Substring Optimised Approach

### Optimized Approach Using Sliding Window:
**Key Insight**: Use a sliding window to progressively expand and contract the substring of s while keeping track of the characters required from t.
**Steps**:
- Maintain a window using two pointers (left and right), expanding the window by moving the right pointer, and shrinking it by moving the left pointer.
- Use a hash map or frequency counter to track how many of each character from t are still needed within the current window.
- Whenever the window contains all characters from t, attempt to shrink the window from the left to minimize its size.
- Continue until the entire string s is processed.

### Pseudocode

``` cpp 
function minWindow(s, t):
    if len(t) > len(s):
        return ""  # Impossible case

    Create hash map 'targetCount' to store frequency of chars in t
    Create hash map 'windowCount' to store frequency of chars in current window

    Initialize variables:
        left = 0
        right = 0
        required = number of unique characters in t
        formed = 0  # Tracks how many unique chars in the current window match t's requirements
        minWindow = (infinity, 0, 0)  # Format: (window length, left index, right index)

    while right < len(s):
        # Add character from s[right] to windowCount
        char = s[right]
        Increase windowCount[char]

        # If the current char in the window matches targetCount, increment 'formed'
        if windowCount[char] == targetCount[char]:
            formed += 1

        # Try shrinking the window from left if it's valid (i.e., all characters are formed)
        while left <= right and formed == required:
            # Update minWindow if the current window is smaller
            if (right - left + 1) < minWindow[0]:
                minWindow = (right - left + 1, left, right)

            # Remove char at s[left] from windowCount and shrink window
            char = s[left]
            Decrease windowCount[char]

            if windowCount[char] < targetCount[char]:
                formed -= 1

            left += 1  # Shrink the window

        right += 1  # Expand the window

    if minWindow[0] == infinity:
        return ""
    
    return s[minWindow[1]:minWindow[2] + 1]
```

### Complexity Analysis:
**Time Complexity**: O(m+n)

---

