Binary Search
-------------
- needs ordering (not necessarily sorting, since orderings can be of more than one type)
    - basically, some proposition which makes
    ```
    N N N N N N Y Y Y Y Y Y Y
    ```
- ask about how many people are encountering Binary Search for the first time
- quickly explain Binary Search. Ask if everyone can implement it
- Recurrennce implementation

 
Implementation of Binary Search
-------------------------------
- loop till low <= high
- Computing mid:
    ```
    m = (l+h) / 2
    ```
    vs
    ```
    m = l + (h-l)/2
    ```
    
Time complexity
---------------
- Recurrence for time complexity: $T(n) = T(n/2) + O(1)$
- Solve this recurrence to show complexity is $O(\log_2 n)$


Ternary Search
--------------
- Ternary Search: $T(n) = T(n/3) + O(1)$
- Ternary Search isn't really faster. Since $O(1)$ of binary search is less than $O(2)$ of ternary search. $1 \times \log_2 n < k \times \log_k n$. Extreme Case: $k=n$, n-ary search, which is same as linear search


Eventual value of low and high if element is not present?
---------------------------------------------------------
- if searching for $x$, after termination, $A_l >= x$ while $A_h <= x$
- Note that the roles are reversed


Repeated elements, Find first occurance of element
-------------------------------
- when `array[mid] == x`, either we've hit the first occurance or hit the not-first occurance.
- if `array[mid] == x` then check if `array[mid - 1] == x`. If yes, do `high = mid - 1` and continue, since this is not the first occurance.
- edge case: if `mid = 0`, then make sure that you don't check `array[-1]`

-- --

Rotated array:
--------------
- if shifted to the right
    - `6 7 8 9 0 1 2 3 4 5`
    - `A[0] >= A[-1]`. If this is not true, there was no rotation
    - Now, we have mid, let's say 2
    - Now, if 2 is in the first half, then it must be greater than last element
    - Else it should be smaller than last element.
    - So search for rotation point based on this


Find any peak element in _unsorted_ array
------------------------------------------
- Peak element is one that is not smaller than its neighbors
- 1, **5**, 3, 2, 1, **6**, 5
- $\log n$ time using binary search
- if sorted ascending, peak is last
- if sorted descending, first element is peak
- algo:
    - check mid.
    - 1 6 5
        - if `a[m-1] <= a[m] >= a[m+1]`, then peak
    - 7 6 5
        - if `a[m-1] > a[m] >= a[m+1]`, then move left
        - theorem: one peak exists to the left
        - 90 80 70 60 50
        - ofcourse, there could be a peak to the right, but we can safely go left
    - 7 6 8
        - move in either of the parts, since peaks exist on both sides


All but one element comes twice, find this element. Sorted array
----------------------------------------------------------------
- 0 0 4 4 **5** 7 7 8 8
- get mid. find its first occurance in log n time.
- check if number of elements from mid to last is even or odd.
    - odd: singular exists in latter part
    - even: singular exists in former part

Family of strings
-----------------
- $s_0 = 0$
- $s_i = s_{i-1} \cdot 0 \cdot (s_{i-1})'$

```
s0 =        0            1
s1 =       001           3
s2 =     0010110         7
s3 = 001011001101001    15
```
- Given N, k, find kth character of $S_n$.
- Length of string: $|S_n| = 2^{n+1} - 1$
- Draw tree. Show toggling of bits



Staircase
---------
```
          __
       __|__|
    __|__|__|
 __|__|__|__|
|__|__|__|__|
```
- heights: 1, 2, ... h
- Given $n$ bricks, find the max height of staircase that can be built
- Let ans be $h$. Then number of bricks needed = $h(h+1) / 2$
- Now, binary search on h. Min = 0, max = n. 
- if f(h) > n, go left
- if f(h) < n and f(h+1) >= n. Stop
- if f(h) < n and f(h+1) < n, go right
- 


MxN Matrix. Each row sorted. MxN is odd. Find overall median
------------------------------------
$M \times N$ matrix. Note: $M \times N$ is odd.
```
        4 6 7
        1 7 9
        2 2 3
```
actual answer: 4
1 2 2 3 **4** 6 7 7 9

- Vanilla - concat and sort arrays. $O(mn \log{mn})$
- Median of Medians doesn't work, 7 is not the correct answer
- Note: lowest element is from 1st col, and largest is from last col (since rows are sorted)
- M rows. Find low and high in O(m) time
- Now, if x is median, then 1/2 elements should be smaller, 1/2 should be bigger
- more correctly, if x is repeated, then if first occurance of x is l, last occurance is r, then if l <= n/2 <= r, then x is median
- now, in each row, find how many >x and <x.
- if l <= n/2 <= r - stop
- if r < n/2, increase low
- if l > n/2, decrease high
- Time complexity: $O(m \log n \log{(\max - \min)})$
- why odd? 1 4 6 9, and searching for 5. both side are n/2 so we don't know what to increase/decrease

Any doubts, will you be able to code it?
----------------------------------------


-- --






- 4 things
    - lecture 1 hour
    - assignment (4 questions) same which were discussed in class
    - standup session (homework problem / doubts)
    - homework problem
- 2 links generated - standup lecture and lecture
- operations guy will help setting up of lectures
- TAs will take a standup session, not me
- share questions and homeworks
