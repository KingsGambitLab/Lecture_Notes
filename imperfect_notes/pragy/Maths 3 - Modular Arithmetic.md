Maths 3 - Modular Arithmetic
----------------------------



Arithmetic of Remainders

$x % m$ gives a value $\in [0, m-1]$


Say m = 4

**Property 1 - Modulus repeats**
![97402b22.png](/users/pragyagarwal/Boostnote/attachments/b40d7037-2666-4b31-b623-936a12cc4244/b445a06d.png)

Since 1, 5, 10 have the same modulus, they can be said to be "modular equivalent wrt 5"

$0 \equiv 5 \equiv 10 \mod 5$
$1 \equiv 6 \equiv 11 \mod 5$
-- --

Linearity of remainders
-----------------------

Remainder of sums is the sum of remainders (modular-sum)

**Incorrect:** $(a+b) \% m = a \% m + b \% m$

This is wrong, because (m-1) + (m-1) = (2m-2) can be >= m

**Correct:** $(a+b) \% m = \Bigl ( a \% m + b \% m \Bigr ) \% m$

**Linearity works for both +ve and negative.**
But, we need numbers to be $\in [0, m-1]$

So, negative modulus values can be fixed by simply adding $m$

$(10 - 4) \% 7$
$= (10 \% 7 - 4 \% 7) \% 7$
$= (3 - 4) \% 7$
$= -1 \% 7$
$= -1 + 7$
$= 6$

**Distributive over multiplication, addition, substraction but not division.**

-- --

Count Pairs
-----------


> Given A[N]. non-negative integers.
> Given m
> Count number of pairs (i, j), such that a[i] + a[j] is divisible by m
> 


**Brute Force:** $O(n^2)$

Example:
> A = [2 2 1 7 5 3], m = 4
> answer = 5
> (2,2), (1, 7), (1, 3), (7, 5), (5, 3)

**Optimized:**
Instead of thinking of remainders of sum, think of sum of remainders.

That is, if I've an element which gives remainder $x$, then it can be paired with an element which gives remainder $m-x$
![5dd03bec.png](/users/pragyagarwal/Boostnote/attachments/b40d7037-2666-4b31-b623-936a12cc4244/bf41b9e2.png =300x)
Keep counts for each remainder. Finally, count the number of pairs

> 0 - 0
> 1 - 2
> 2 - 2
> 3 - 2
> So, $\dfrac{c_0 (c_0-1)}2 + (c_1 \times c_3) + \dfrac{c_2 (c_2-1)}2$
> $= 0 + 4 + 2 = 6$
> 

Special cases for remainders is 0, n/2
Note: loop till m/2 so that you don't double count

```python
total = count[0] choose 2
if m % 2 ==0:
    total += count[m/2] choose 2
else:
    total += count[m//2] + count[m//2 + 1]

for i <- 1 .. m/2-1:
    total += count[i] * count[m-i]
```


Complexity: Time: $O(n + m)$ Space: $O(m)$
-- --

Count Triplets
--------------

> Given A[N] with non-negative integers
> Given m, find the number of triplets such that sum is divisible by m
> 

Think in terms of the last question

**Brute Force**: $O(n^3)$

**With last approach:** $O(n + m^2)$

1. Bucket
2. Choose 2 mods: a, b. Third mod c = m - (a+b)
3. Count total
4. All 3 from same bucket - for 0 and m//3
5. 2 from same bucket, one from other bucket
6. all 3 from different buckets

![bb5890c2.png](/users/pragyagarwal/Boostnote/attachments/b40d7037-2666-4b31-b623-936a12cc4244/bb5890c2.png =400x)

So, fix two buckets, so 3rd can be chosen

Enforce two things:
1. i <= j <= k   otherwise, repetitions can happen
2. i + j + k = 0 or i + j + k = m


```python
total = 0

for i <- 0 .. m-1:
    for j <- i .. m-1:
        k = (m - i + j) % m # explain the case when i, j are 0
        # explain that this mod should handle -ve
        # python. for c++/java, do it yourself
        if i == j == k:
            total += count[i] choose 3
        elif i == j:
            total += count[i] choose 2 * count[k]
        elif i == k:
            total += count[i] choose 2 * count[j]
        elif j == k:
            total += count[j] choose 2 * count[i]
        else:
            total += count[i] * count [j] * count[k]

```

Time: $O(n + m^2)$, Space: $O(m)$


-- --

Balanced Paranthesis Count
--------------------------

> Given N pairs of paranthesis
> Find number of distinct balanced paranthesis
> 
> meaning of balanced: for every prefix, number of opening braces should be >= number of closing braces
> 

Example
> 0 pairs
> 0
> 
> 1 pair: ()
> 1
> 
> 2 pairs: ()(), (())
> 2
> 
> 3 pairs: ()()(), ()(()), (())(), (()()), ((()))
> 5

Say we want to construct for n = 3
Choose how many pairs must go inside

![33f72a14.png](/users/pragyagarwal/Boostnote/attachments/b40d7037-2666-4b31-b623-936a12cc4244/33f72a14.png =400x)

![962dd530.png](/users/pragyagarwal/Boostnote/attachments/b40d7037-2666-4b31-b623-936a12cc4244/962dd530.png =300x)


$C_0 = 1$

$C_n = C_0 C_{n-1} + C_1 C_{n-2} + \cdots C_{n-1}C_0$

$\displaystyle C_n = \sum\limits_{i=0}^{n-1} C_i C_{n-i-1}$

-- --

Catalan numbers
---------------


Same as above

Time to find nth catlan number = $O(n^2)$ (because we need to compute numbers before it)

-- --


Number of Paths
---------------

> Given $m \times n$ grid, find the number of paths from (0,0) to (m-1, n-1)
> Can only move right and down.


Approach:
- Every path will have exactly (n-1) right steps, and (m-1) down steps.
- Only the order differs

So, $\dfrac{(n+m-2)!}{(n-1)! \cdot (m-1)!}$

Complexity? O(n+m)

-- --

Number of lower triangle paths in Square Matrix
-----------------------------------------------


> Given $n \times n$ (square) grid, find the number of paths from (0,0) to (m-1, n-1)
> Can only move right and down.
> Exists only in teh lower triangle
> 

- First move must be down
- Number of Rs < Number of Ds at every step

Same as balanced parans
![7c611269.png](/users/pragyagarwal/Boostnote/attachments/b40d7037-2666-4b31-b623-936a12cc4244/7c611269.png)

$C_{n-1}$, because n-1 pairs of moves for $n \times n$ matrix

