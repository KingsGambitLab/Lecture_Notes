Binary Search 2
---------------

Median of two sorted arrays
---------------------------
- merge: O(n). Search O(log n) 
- binary search: O(log n)
- pick the smaller array
- low = 0, high = length of smaller array
- partition the other array so that number of elements in first of both = number of elements in last of both
- now check if this partition is valid by cross comparison
- change high and low accordingly
- append -inf and +inf to start and ends of arrays

Special Integer
-------------------------------------
> Unsorted array of size N.
> +ve numbers.
> Given X, find max value of K such that no subarray of length k has sum > x
- binary search over k in 0..N
- if any sum > X, k is not the answer
- if sum <= x, k might be the answer if k+1 is not allowed
- finding max sum for a given k takes O(n) time
- todo: change to m and not m-1/m+1 loop till h-l>1
-- --

Sorted array of length N.
-------------------------------------
> numbers are from 1..N-1 (so contiguous).
> One of the numbers is repeated.
> Find it

- 1 2 3 4 4 5 6 7 8  (number)
- 0 1 2 3 4 5 6 7 8  (index)
- N N N N Y Y Y Y Y  (proposition)

Agressive Cows
--------------

> N stalls, n >= 2
> C cows, c >= 2
> locations of stalls, let's say 1, 2, 5, 7, 8
> Maximize the minimum distance between any two cows

- low = 1
- high = N
- calculate mid = distance, and check

Smallest Good Base
------------------
> $N \in \{3, 10^{18}\}$
> k >= 2
> $(N)_k = 1111111\ldots$
> Find smallest k

- example: N = 7
    - k = 2, $(7)_2 = 111$
- finding the largest good base is trivial - N-1
- low = 2, high = n-1
- If $m$ is the answer, then $\exists i: 1 + m + m^2 + \cdots + m^i = N$
- But we still can't binary search since we don't know $i$. $i$ will change for different numbers
- Also, say we found a working or non working m. How do we change the low and high? Multiple possible answers, which one to chose?
- Let's look at it from searching on i
- We need to maximize i (thereby minimize k)
- $(7)_6 = 11, (7)_2 = 111$, we need to output 2.
- So, linear search over all possible number of bits from 63 to 2
    - Then for a fixed (i), binary search for the value of m (or use formula of geometric series)
- low, high for number of bits will be $1, \log_2 N$ (because smallest k is 2)
- $2^{63} \approx 10^{18}$


Smallest subarray
-----------------

> Array of length N
> Not sorted
> +ve numbers
> Find length of smallest subarray such that sum >= k
- calculate prefix sum (prefix sum is sorted)
- can you calculate sum a[i] .. a[j]?
    - a[i] .. a[j] = P[j] - P[i] + a[i]
- now, let's say the answer starts from S and ends at E
    - loop over all possible S
        - binary search for E
    - return S, E that has min distance

Election
--------

> N People
> influence[1..n]: 1 2 2 3 1    (+ve)
> Voting: ith person votes for jth person if sum(influence[i+1:j-1]) <= influence[i]
> Note: j can lie on the left side as well
> Print the array of votes each person got

- So, in 1 2 2 3 1, the number of people who can vote for a[i] are 2 3 2 3 3
- now, if we try to find how many people vote for i, it is linear search, so total $O(n^2)$
- instead, we can calculate prefix sum, and for each person, see what range of people it can vote for using binary search. So O(n \log n)
- Now that we have ranges, we need to find the final array
- O(n) algo to convert ranges to array by doing +1 on start, -1 on end, and then taking prefix sum

