# Sorting

- define sorting: permuting the sequence to enforce order. todo
- brute force: $O(n! \times n)$


Stability
---------
- definition: if two objects have the same value, they must retain their original order after sort
- importance:
    - preserving order - values could be orders and chronological order may be important
    - sorting tuples - sort on first column, then on second column

-- --

Insertion Sort
--------------
- explain: 
    - 1st element is sorted
    - invariant: for i, the array uptil i-1 is sorted
    - take the element at index i, and insert it at correct position
- pseudo code:
  ```c++
  void insertionSort(int arr[], int length) {
      int i, j, key;
      for (i = 1; i < length; i++) {
          key = arr[i];
          j = i-1;
          while (j >= 0 && arr[j] > key) {
              arr[j+1] = arr[j];
              j--;
          }
          arr[j + 1] = key;
      }
  }
  ```
- **Stablility:** Stable, because swap only when strictly >. Had it been >=, it would be unstable
- **Complexity:** $O(n^2)$

-- --


Bubble Sort
-----------
- explain:
    - invariant: last i elements are the largest one and are in correct place.
- why "bubble": largest unsorted element bubbles up - just like bubbles
- pseudo code:
  ```c++
  void bubbleSort(int arr[], int n) {  
      for (int i = 0; i < n-1; i++)
      for (int j = 0; j < n-i-1; j++)  
          if (arr[j] > arr[j+1])  
              swap(&arr[j], &arr[j+1]);  
  }
  ```
- **Stability:** Stable
- **Complexity:** $O(n^2)$

-- --


Bubble Sort with window of size 3
---------------------------------
- explain bubble sort as window of size 2
- propose window of size 3
- does this work?
- no - even and odd elements are never compared

 
-- --


Counting Sort
-------------
- explain:
    - given array, first find min and max in O(n) time
    - create space of O(max-min)
    - count the number of elements
    - take prefix sum
- constraint: can only be used when the numbers are bounded.
- pseudo code:
  ```c++
  void counting_sort(char arr[]) { 
      // find min, max
      // create output space
      // count elements
      // take prefix sum
      // To make it stable we are operating in reverse order. 
      for (int i = n-1; i >= 0; i--) {
          output[count[arr[i]] - 1] = arr[i]; 
          -- count[arr[i]]; 
      }
  }
  ```
- **Stability:** Stable, if imlpemented correctly
- **Complexity**: $O(n + \max(a[i]))$
- why not just put the element there? if numbers/value, can do. Else, could be objects

-- --


Radix Sort
----------
- sort elements from lowest significant to most significant values
- explain: basically counting sort on each bit / digit
- **Stability:** inherently stable - won't work if unstable
- **complexity:** $O(n \log\max a[i])$

-- --



Partition Array
---------------
> Array of size $n$
> Given $k$, $k <= n$
> Partition array into two parts $A, ||A|| = k$ and $B, ||B|| = n-k$ elements, such that $|\sum A - \sum B|$ is maximized

- Sort and choose smallest k?
- Counterexample
```
1 2 3 4 5
k = 3

bad: {1, 2, 3}, {4, 5}
good: {1, 2}, {3, 4, 5}
```
- choose based on n/2 - because we want the small sum to be smaller, so choose less elements, and the larger sum to be larger, so choose more elements

-- --


Sex-Tuples
----------
> Given A[n], all distinct
> find the count of sex-tuples such that
> $$\frac{a b + c}{d} - e = f$$
> Note: numbers can repeat in the sextuple

- Naive: ${n \choose 6} = O(n^6)$
- Optimization. Rewrite the equation as $ab + c = d(e + f)$
    - Now, we only need ${n \choose 3} = O(n^3)$
    - Caution: $d \neq 0$
    - Once you have array of RHS, sort it in $O(\log n^3)$ time.
    - Then for each value of LHS, count using binary search in the sorted array in $\log n$ time.
    - Total: $O(n^3 \log n)$

-- --

Anagrams
--------
