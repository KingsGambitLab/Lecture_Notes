Maths 1 - GCD
-------------

Tushar - fast batch


Kshitij, Sept EliteX

-- --

Some basic Maths - concepts that are used in coding questions and interviews

GCD / HCF
---------

1. gcd(a) = largest $x$, such that $a|x$ and $b|x$
1. GCD examples
    - 5, 15 = 5
    - 12, 8 = 4
    - 8, 16 = 8
    - 16, 8 = 8
    - 17, 1 = 1
    - 12, 1 = 1
    - 17, 0 = 17
    - 12, 0 = 12
    - -5, 0 = 5
1. GCD Properties
    - gcd(x, 0) = |x|
    - gcd(x, 1) = 1
    - does the order matter?
        - No
    - gcd(x, y) = gcd(y, x)  (commutative)
    - gcd(x, y, z) = gcd(gcd(x, y), z) = gcd(x, gcd(y, z)) (associative)
        - Analogy with
            - longest common prefix  aac, aabc, aabcd
            - Set intersection
        - Whenever we're finding common things, usually order doesn't matter
    - max possible value of $gcd(a, b) = min(a, b)$  if both a, b are +ve

1. GCD of complete array
    - if gcd(x, y) function is given
    - simply do pairwise

-- --

Computing GCD
-------------

**Brute Force**

```python
def gcd(a, b):
    for i <- 2 .. min(a, b)
        if a % i == 0 and b % i == 0:
            return i
```

Complexity: $O(\min(a, b))$
-- --

Substraction Approach
---------------------

1. $GCD(a, b) = GCD(a-b, b), \text{if } a > b$
    > $GCD(20, 6) = GCD(14, 6)$

**Proof**

1. $a = b + c$
    > $20 = 14 + 6$
1. $GCD(a, b) = g$
    > $GCD(20, 6) = 2$
1. Thus, $(b+c) | g$ and $b | g$
    > $(6+14)|2, 6|2$
1. Thus, $c | g$
    > $14|2$
1. Thus, $g = GCD(c, b)$
    > $2 = GCD(14, 6)$
1. Hence, $GCD(a, b) = GCD(a-b, b), \text{if } a > b$

So, we can calculate GCD recursively
(Chinese Mathematician)

```python
def gcd(a, b):
    if a < b:
        a, b = b, a # swap
    if b == 0:
        return a
    return gcd(a-b, b)
```

Time complexity - Worst case linear
but usually much faster

-- --

Euclid Approach
---------------

1. $GCD(a, b) = GCD(b, a\%b), \text{if } a > b$
    > $GCD(20, 6) = GCD(2, 6)$

**Proof**

1. $a = k \cdot b + c$
    > $20 = 3 \cdot 6 + 2$
1. $GCD(a, b) = g$
    > $GCD(20, 6) = 2$
1. Thus, $(k \cdot b + c) | g$ and $b | g$
    > $(3 \cdot 6 + 2)|2, 6|2$
1. Thus, $c | g$
    > $2|2$
1. Thus, $g = GCD(c, b)$
    > $2 = GCD(2, 6)
1. Hence, $GCD(a, b) = GCD(a\%b, b), \text{if } a > b$

So, we can calculate GCD recursively

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
```

**Explain how the numbers are automatically swapped**


![5b3ffff4.png](/users/pragyagarwal/Boostnote/attachments/3312dcc9-9a3d-4d0f-88b3-fa96f86e5a83/772e17f0.png)

![5b85a308.png](/users/pragyagarwal/Boostnote/attachments/3312dcc9-9a3d-4d0f-88b3-fa96f86e5a83/4808ccaa.png)

![55070460.png](/users/pragyagarwal/Boostnote/attachments/3312dcc9-9a3d-4d0f-88b3-fa96f86e5a83/e0af41cd.png)

![95ddd25e.png](/users/pragyagarwal/Boostnote/attachments/3312dcc9-9a3d-4d0f-88b3-fa96f86e5a83/cf4b9112.png)

Stop if divisor is 1 or remainder is 0


Complexity: $O(\log_2\max(a, b))$

Why: after one step, max possible value of remainder is $< a/2$

Cases
- $b < a/2$ - remainder $< b$, so remainder $< a/2$
- $b > a/2$ - division eats up more than half, and remainder is less than half
![69762a56.png](/users/pragyagarwal/Boostnote/attachments/3312dcc9-9a3d-4d0f-88b3-fa96f86e5a83/3bb53b9e.png)

-- --

Array Factorial GCD
-------------------

> Given Array A[N], find the GCD of factorials of elements of array
> 
Naive: factorial and then gcd

Solution: min and then factorial
![6f8d9921.png](/users/pragyagarwal/Boostnote/attachments/3312dcc9-9a3d-4d0f-88b3-fa96f86e5a83/6f8d9921.png)

-- --
Array Susequence GCD
--------------------

> Given A[N]
> Return 1 if there is any subsequence with gcd = 1, else return 0
> 

Explain subsequence (can skip) vs subarray (contiguous)

> Example:
> A = 4 6 3 8
> return 1, because 4 3 has gcd 1
> So does 3 8
> and 4 3 8
> 

**Brute Force**

Consider all subsequences - $O(2^n)$

**Simple Approach:**
Simply take gcd of the whole array

Why?

If there is any subsequence whose gcd is 1, the gcd of the entire array must also be 1
If the gcd of entire array is 1, then there's some subsequence which causes it.

$GCD(\text{array}) = GCD(GCD(A, B, C), GCD(D, E, F, G))$
$= GCD(1, GCD(D, E, F, G))$
$= 1$

Complexity: $O(n \log \max)$

-- --

Delete Elements
---------------

> Given A[N]
> Give me the minimum number of element that you need to delete such that the GCD of the resulting array becomes 1
> If can't, return -1

Same as previous. If 1, then delete nothing.
Else, return -1, because deleting won't help

Side Note: GCD will be 0 only if all the elements are 0
-- --

Delete one
----------

> Given A[N]
> Delete one element, and make the GCD maximum
> 12, 15, 18
> delete 15 to get GCD = 6
> 

Naive: $O(n^2)$

Note: deleting min element is not correct

Optimized:
Prefix and postfix GCD
> 12 3 3
> 3 3 18
> 

Intuition: Prefix-Sum, postfix-sum to get sum of elements except A[i]
> pre[i-1] + post[i+1] = Sum(A) - A[i]
> 

What property enables this? Association & commutative


-- --

Pubg
----

> Given A[N] with healths, minimize the health of the last player
> When a attacks b, we have a, (b-a)
> If health becomes 0, the person dies
> 

> 14 2 28 56
> 12 2 28 56
> 12 2 16 56
> 12 0 16 56
> 


Note: min is not the answer. Example, 4, 6 An is 2

Observation 1: smaller should attack larger, example 12, 8

So, smallest should attack the rest
untill all become 1 or 0

same as finding the gcd of entire array


-- --

Closed Differences
------------------

> Given A[N], consider any pair $A[i], A[j]$, if the difference $|A[i] - A[j]| \notin A$, append it.
> If no more moves can be made, stop.
> Find the size of the final array
> 

$$\frac{\max A}{\rm{gcd} A} + \begin{cases}1 & \text{if } 0 \in A \\ 0 & \text{otherwise} \end{cases}$$

Note: $\max A$ is always divisible by GCD (duh)
