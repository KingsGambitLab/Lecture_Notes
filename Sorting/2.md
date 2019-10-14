
# Sorting 2
-- --

Merge Sort
----------
- Divide and Conquer
    - didive into 2
    - sort individually
    - combine the solution
- Merging takes $O(n+m)$ time.
    - needs extra space
- code for merging:
  ```c++
  // arr1[n1]
  // arr2[n2]
  int i = 0, j = 0, k = 0;
  
  // output[n1+n2]
  
  while (i<n1 && j <n2) {
      if (arr1[i] <= arr2[j])  // if <, then unstable
          output[k++] = arr1[i++];
      else
          output[k++] = arr2[j++];
  }
  // only one array can be non-empty
  while (i < n1)
      output[k++] = arr1[i++];
  
  while (j < n2)
      output[k++] = arr2[j++];
  ```
- stable? Yes
- in-place? No
- Time complexity recurrence: $T(n) = 2T(n/2) + O(n)$
- Solve by Master Theorem.
- Solve by algebra
- Solve by Tree height ($\log n$) * level complexity ($O(n)$)


-- --


Intersection of sorted arrays
-----------------------------
> 2 sorted arrays
> ```
> 1 2 2 3 4 9
> 2 3 3 9 9
> 
> intersection: 2 3 9
> ```
- calculate intersection. Report an element only once
- Naive:
    - Search each element in the other array. $O(n \log m)$
- Optimied:
    - Use merge.
    - Ignore unequal.
    - Add equal.
    - Move pointer ahead till next element


-- --


Merging without extra space
---------------------------
- can use extra time
- if a[i] < b[j], i++
- else: swap put b[i] in place of a[i]. Sorted insert a[i] in b array
- so, $O(n^2)$ time


-- --


Count inversions
---------------
> inversion:
> i < j, but a[i] > a[j]  (strict inequalities)
- naive: $O(n^2)$
- Split array into 2.
- Number of inversions = number of inversions in A + B + cross terms
- count the cross inversions by example
- does number of cross inversions change when sub-arrays are permuted?
- no
- can we permute so that it becomes easier to count cross inversions?
- sort both subarrays and count inversions in A, B recursively
- then, merge A and B and during the merge count the number of inversions
- A_i B_j
- if A[i] > B[j], then there are inversions
- num inversions for A[i], B[j] = |A| - i
- intra array inversions? Counted in recursive case.


-- --


Find doubled-inversions
-----------------------
> same as inversion
> just i < j, a[i] > 2 * a[j]

- same as previous. Split and recursilvely count
- while merging, for some b[j], I need to find how many elements in A are greater than 2 * b[j]
- linear search for that, but keep index
- linear search is better than binary search


-- --

Sort n strings of length n each
    - $T(n) = 2T(n/2) + O(n^2) = O(n^2)$ is wrong
    - $T(n) = 2T(n/2) + O(n) * O(m) = O(nm\log n)$ is correct. Here m = the initial value of n


-- --
> .
>
> I G N O R E
>
> .


Bounded Subarray Sum Count
--------------------------
> given A[N]
> can have -ve
> given lower <= upper
> find numbe of subarrays such that lower <= sum <= upper

- naive: $O(n^2)$  (keep prefix sum to calculate sum in O(1), n^2 loop)
- if only +ve, $O(n\log n)$ using prefix sum
- but what if -ve?
- 


-- --
