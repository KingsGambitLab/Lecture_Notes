Recursion & Backtracking
------------------------

Recursion - function calling itself

- initial call from some external function
- recursive calls
- base case

```python
def fib(n):
    if n <= 1 : return n  # base case
    return fub(n-1) + fib(n-2) # recursive calls
    
fib(10)  # initial call
```

-- --

Power
-----

> Given n, k, find $n^k$
> 

```python
def pow(n, k):
    if k == 0: return 1
    
	nk = pow(n, k//2)
	if k % 2 == 0:
		return nk * nk
	else:
		return nk * nk * n
```

why not f(n, k//2) * f(n, k//2+1) in the else condition? To allow reuse of answers


```
19 -> 9 -> 4 -> 2 -> 1 -> 0

19 ->  9 -> 4 -> 2 -> 1
         -> 5 -|2
              -> 3 -|1
                   -|2
   -> 10 -|5
```

Complexity (assuming all multiplications are O(1))? $O(\log_2 k)$


Break it into 3 parts? k//3 and take care of mod1 and mod2

Binary is still better, just like in binary search
-- --

All Subsets
-----------

> Given A[N], print all subsets
> 

Number of subsets? $2^n$
Two choices for each element

One of them is the empty set

Explain that we want combinations, and not permutations. [1, 4] = [4, 1]

Number of permutations will be much larger

```python
def subsets(A, i, aux):
    if i == len(A):
        print(aux)
        return
    take = subsets(A, i+1, aux + [A[i]])
    no_take = subsets(A, i+1, aux)
```

Draw recursion Tree

How many leaves? $2^n$ - one for each subset
How many total nodes? $2^{n+1} - 1$

Complexity? $O(2^n)$

-- -- 

Subsets using Iteration
-----------------------

Look at recursion Tree. Going left = 0
Going right = 1

Basically, for each element, choose = 1, skip = 0


So, generate numbers from 0 to $2^n-1$ and look at the bits of the numbers. Each subset is formed using each number

-- --

Lexicographic subsets
---------------------

Explain lexicographic order

```
[]
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 3]
[0, 2]
[0, 2, 3]
[0, 3]
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
```

Basically, we're doing DFS. Print when encountering node
But don't print when going left - because already printed in parent

```python
def subsets(A, i, aux, p):
    if p: print(aux)
    if i == len(A):
        return
    take = subsets(A, i+1, aux + [A[i]], True)
    no_take = subsets(A, i+1, aux, False)
```

time: $O(2^n)$
Space: $O(n^2)$, because we're creating new aux arrays

-- --

Backtracking
------------

- do
- recurse
- undo


Can help reduce the space complexity, because we're reusing the same storage

-- --

Deduplicated subsets
--------------------

> A = [1, 1, 2, 3, 4, 5, 5]
> find all distinct subsets
> 

- create multiset
- if A[i] occurs k times, we have (k+1) choices. 0 times, 1 times, 2 times, ... k times
- move on to A[i+1]


-- --

Number of subsets with given sum
--------------------------------

> Given A[N], k find number of subsets with sum k
> 

```python
def knapsack(A, k, i, total):
    if i == len(A):
        if total == k: return 1
        else: return 0

    take = knapsack(A, k, i+1, total + A[i])
    skip = knapsack(A, k, i+1, total)
    return  take + skip
```

Why can't terminate earlier whne total is good? Because can have -ves and don't consider future sums

k = 6
1, 2, 3 is good, but
1, 2, 3, -1, 1 is also good

-- --

Subsets with sum k (repetitions allowed)
----------------------------------------

> Given A[n]. Only +ves
> Given k
> allowed repetitions
> Find number of subsets with repitions with sum k
> 

Solution:

```python

def foo(A, k, i, total):
    if i == len(A):
        if total == k:
            return 1
        else:
        return 0
    if total > k:
        return 0
        
    no_take = foo(A, k, i+1, total)
    take = foo(A, k, i, total+a[i])  # don't change index
```

Take care of base cases
No negatives allowed, so can check on both array length and total


-- --

following May EliteX by Vivek

3rd October - remedial class - june+may - elite+super
