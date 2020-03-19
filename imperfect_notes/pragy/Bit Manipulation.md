Bit Manipulation
----------------


Bitwise AND &
-------------
3 & 5
011 & 101
= 001
= 1


Bitwise OR |
------------

3 | 5
011 | 101
= 111
= 7

XOR ^
-----

Exclusive OR. Either this, or that
That is, both bits are different.
For more than 2 bits, True when number of on bits is odd

-- --

```
a & 0 = 0     a & 1 = a     a & a = a
a | 0 = a     a | 1 = 1     a | a = a
a ^ 0 = a     a ^ 1 = ~a    a ^ a = 0
```


For all these 3 operations, associativity is followed

so, $a \odot b \odot c = (a \odot b) \odot c = a \odot (b \odot c)$

-- --

Masking property of XOR
-----------------------

b = (a^b) ^ a
= (a^b) ^ a
= b ^ (a^a)
= b^ 0
= b

-- --

Shifts
------

`<< k` - shift left by k. Insert 0 on right
`>> k` - shift right by k.

`<< k` = multiply by $2^k$
`>> k` = integer divide by $2^k$

show with example, say 22 = 10110

-- --

find first set bit
------------------

simply loop from i = 1 to 64.
check if x & (1<<i) is non-zero

-- --

Pair with XOR
-------------

> Given A[N], find any pair of elements whose XOR is k
> 

**Brute Force:**
Consider all pairs. $O(n^2)$


If a[i] ^ a[j] = k, then a[j] = k ^ a[i]

So, for each a[i]. I need to find if k^a[i] also exists in the array.

Use a hashmap - O(n)


**Corner Case**

if k = 0, we need to search for repeated elements.
So, make sure that you handle it separately.
If we don't handle separately, we might have to store a list of values for each number, which will be bad.

-- --

Single Out
----------

> Given A[N] in which each number appears twice, except for one number. Find this number
> 

**Naive:**
Hashmap. O(n) space

**Optimized:**

Masking property of xor - each repeated number will unmask itself.

So, simply xor the entire array.
Space complexity: O(1)

a^a = 0, a^0 = a
Order doesn't matter, so
a ^ b ^ a ^ c ^ b

a's will cancel out, b's will cancel out. Left with c

-- --

Double Out
----------


> Given A[N] in which each number appears twice, except for two numbers. Find these numbers
> 1 2 2 1 3 8 6 3
> Return 6, 8
> 

**Naive:** Counter. O(n) space

**Optimized:**
- x = xor of entire array. You get xor of the tw oneeded elements
- find out any bit where the xor is set. We know that for this bit, our needed elements differ. So, partition by this bit
- Since all other numbers come in pairs, each partition will also have the numbers in pairs
- calculate the xor of individual partitions

![3e86c025.png](:storage/e8857c4d-a2f9-4142-91cb-4eb909379fd2/3e86c025.png =400x)


O(1) space

-- --


Tripled
-------

> Given A[N]. All elements occur thrice, exceopt one which occurs once. Find the single one.
> 

**Naive:** Counter. O(n) space

**Optimized:**

 Since numbers occurs thrice, for each bit, the count of 1s for that bit must be a multiple of 3. If it is not, then the single number must have that bit set.
 
 So, construct that single number
 
 ![f51be358.png](:storage/e8857c4d-a2f9-4142-91cb-4eb909379fd2/f51be358.png =400x)
 
 Complexity: $O(n \log \max)$
 
 If max integer is 32 bits, then O(32n)
 
 -- --
 
 > Given A[N], find the pair with minimum xor
 > 

**Brute Force:** All pairs. Keep min. $O(n^2)$

**Optimized:**

Given a[i], best possibility is to find another a[i]
If not, then we can find a[i]-1 or a[i]+1

We basically want the numbers to be different as right as possible

![7ddd6b6e.png](:storage/e8857c4d-a2f9-4142-91cb-4eb909379fd2/7ddd6b6e.png)

Intuition: Sort the numbers. Lower the difference, lower the XOR.

**Proof:**

Consider A < B < C

suppose A, C differ in ith bit. Bits 0 to i-1 are same (from MSB)

Then, A must have a 0 there, while C must have a 1.

If B is b/w A, C, then B can have a 0 or a 1 there.

![4cded4eb.png](:storage/e8857c4d-a2f9-4142-91cb-4eb909379fd2/4cded4eb.png =300x)


- 0:
    - A^B < A^C
    - A^B < B^C 
    - (both conditions are important)
- 1:
    - B^C < A^B
    - B^C < A^C

In both cases, the min xor is b/w consecutive elements, and not b/w extremes.


Solution: Sort. Find xor of consecutive pairs. Return min.
O(n log n)

-- --
Google Code Jam '19
-------------------

> Given master server with N slaves.
> user inputs binary string of length N
> send each bit to one server
> to read back, master asks slaves
> slaves are faulty, can go down, and don't return anything
> 
> ![56cbd86d.png](:storage/e8857c4d-a2f9-4142-91cb-4eb909379fd2/56cbd86d.png =300x)
> 
> input: 1010.
> slaves 2, 4 go down
> read: 11
> 
> input: 1111
> slaves 2, 4 go down
> read: 11
> 
> Find out all faulty slaves by minimizing number of input queries
> 


**Brute Force:** O(n). Check each slave one by one by setting just one bit each time

**Optimized:**

- we send several strings. Represented as matrix
- If ith slave is faulty, then ith column is dropped off.
- Say 2, 3 are faulty
- ![47132572.png](:storage/e8857c4d-a2f9-4142-91cb-4eb909379fd2/47132572.png =300x)
- simply encode each slave number in each column and send
- ![5c782630.png](:storage/e8857c4d-a2f9-4142-91cb-4eb909379fd2/5c782630.png =200x)
- whatever comes back are columnwise numbers of active slaves
- ![9e762159.png](:storage/e8857c4d-a2f9-4142-91cb-4eb909379fd2/9e762159.png =400x)

Instead of sending N strings, we send strings of length N
We only need $\log_2 N$ strings


So, for $10^9$ slaves, I only need 32 queries!
-- --


Sum of Hamming Distances
------------------------

> Given A[N], find sum of Hamming distance b/w each pair of elements.
> x = 0110
> y = 1001
> d = 1111
> 

**Brute Force:** All pairs $O(n^2)$

**Optimized:**
For each bit:
    count with bit set = x
    count with bit not set = y
    contribution of bit = 2^bit * x * y

sum up

**O(32 * n)**


Remember the pattern? Instead of summing up all submatrix, we counted contribution of each cell. Reverse Lookup

-- --

following Kshitij's lecture
