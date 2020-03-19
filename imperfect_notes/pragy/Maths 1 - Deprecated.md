Maths 1
-------

Vivek, July EliteX

-- --

pragy@interviewbit.com

Some basic Maths - concepts that are used in coding questions and interviews

Random Functions
----------------

> Given function rand5() defined as follows

```c++
int rand5() {
  // return random number from [1..5] with equal probability
}
```

> The implementation of the function is not provided - black box
> Given rand5, implement a `rand7()` that returns a random number from [1..7] with equal probability
> 

Try using rand5 to create rand7, and try minimizing the number of calls to rand5


Wrong Approach: call rand5 7 times, add and divide by 5

Why wrong:
```
to get 7, we need 7 5's, so prob = $(1/5)^7$
1 0
2 0.0051
3 0.1523
4 0.5044
5 0.3088
6 0.0294
7 0.0001
```

**1 call:**
- Mapping {1..5} to {1..7}.
- Can't map single number to multiple outputs.
- So, not possible

**2 calls:**
- Mapping {(1,1)..(5,5)} to {1..7}.
- So, we need to map 25 outputs having equal prob, to 7 outputs
- Challenges:
    - Map 2d to 1d
    - Maintain equal prob
- Instead, think rand6() and rand9()
- now, we have matrix of 6x6. Total 36 possibilities.
- Map to 9 values by making 4 buckets
- ![52f49e08.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/52f49e08.png)
- First buckets contains numbers from 1..9
- Second bucket contains numbers from 10..18
- So, `1 + (x%9)` would work
- Now, how to transform $(x, y)$ to numbers by doing $(x-1) * 6 + y$

```python
def rand9():
    x = rand6()
    y = rand6()
    val = (x - 1) * 6 + y
    return 1 + val % 9
    
def rand9():
    return 1 + ((rand6() - 1) * 6 + rand6()) % 9
```


Now, this worked because 36 is divisible by 9

So, for rand7 using rand5, if we make
- 2 calls, make 3 buckets, use 1-21, waste 4
![6270c29c.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/6270c29c.png =300x)
- When discarded, call rand5 again

```python
def rand7():
    val = (rand5() - 1) * 5 + rand6()
    if val > 21:  # discard and redo
        return rand7()
    return 1 + (val % 7)
```


-- --

GCD
---

gcd(a) = largest $x$, such that $a|x$ and $b|x$

max possible value of $gcd(a, b) = min(a, b)$

**Brute Force**

```
def gcd(a, b):
    for i <- 1 .. min(a, b)
        if a % i == 0 and b % i == 0:
            return i
```

Complexity: $O(\min(a, b))$

**Euclidean algo**
![5b3ffff4.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/5b3ffff4.png)

![5b85a308.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/5b85a308.png)

![55070460.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/55070460.png)

![95ddd25e.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/95ddd25e.png)

Stop if divisor is 1 or remainder is 0


```python
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
```

Complexity: $O(\log_2\max(a, b))$

Why: after one step, max possible value of remainder is $< b/2$

Cases
- $a < b/2$ - remainder $< a$, so remainder $< b/2$
- $a > b/2$ - division eats up more than half, and remainder is less than half
![69762a56.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/69762a56.png)


-- --

GCD of multiple numbers
-----------------------

$gcd(a, b, c) = gcd(c, gcd(a, b))$

Does order matter? No.

Analogy with
- longest common prefix  aac, aabc, aabcd
- Set intersection

Whenever we're finding common things, usually order doesn't matter


-- --

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
If the gcd of entire array is 1, then there's some subsequence which causes it


Complexity: $O(n \log \max)$

-- --

> Given number n, find all factors of n
> 

Observations:
- largest factor is n itself
- all other factors are $\leq n/2$

So, loop from 1..n/2

Time complexity: $O(n)$


But what about not just factors, what about pairs of factors?
(1,n), (2, n/2), (x, n/x) .. 

```python
for(i = 1; i < sqrt(n); i++)
    if( n%i == 0 ):
        factors.append(i)
        factors.append(n/i)
```

Why sqrt? if x = n/x, then $x = \sqrt n$

Complexity: $O(\sqrt n)$

-- --

Even factors?
-------------

**Brute Force**: Loop and count

**Simple:** Check if perfect square. If perfect suqre - odd, else even.
Binary search / newton raphson


-- --

Check Prime
-----------

**Brute Force** Loop from 1 to $\sqrt n$ and check
$O(\sqrt n)$

-- --

Generate all primes till n
--------------------------

Using last approach: $O(n \times \sqrt n)$

**Sieve of Eratosthenes**  (era - tos - thenis)

- Assume all prime
- cut 1
- next uncut is prime
- cut all multiples - because can't be prime
- go only till sqrt

![3fa0e7ff.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/3fa0e7ff.png =400x)

Optimizatiopn
- start cutting from $i\times i$, because $i \times (i-1,2..)$ is alreayd cut

```python
primes[N] = {1}
primes[0] <- 0
primes[1] <- 0
for(i = 2; i * i <= N; i++)
    if(primes[i] == 1)
        for(j = i; i * j <= N; j++)
            primes[i*j] = 0
```

Complexity:

2 -> N/2
3 -> N/3
...
$\sqrt N$ -> 1

total = $N (1/1 + 1/2 + ...)$
= $O(n \log n)$

Memory = $O(n)$


Caution: Don't build a sieve if you just want to check one number. $O(\sqrt n)$ vs $O(n \log n)$

Note: better algos exist for primality testing

-- --

Prime Factorization
-------------------

> $24 = 2^3 \cdot 3$
> Factorize N

```python
p_factors = []
for f <- 1.. sqrt(n)
    while n % f == 0
        p_factors.append(f)
        n /= f
```

Issue:
> 404 = 2 * 2 * 101
> our algo gives only 2, 2
> i.e., if a prime factorization contains a prime number that is greater than the sqrt of n. we have an issue

Fixed:

```python
p_factors = []
for f <- 1.. sqrt(n)
    while n % f == 0
        p_factors.append(f)
        n /= f
if n != 1
    p_factors.append(n)
```

Time complexity: $O(\log n)$
Inner loop doesn't matter since n is getting decreased

Note: log $O(\log n)$

**Optimization:**

We're going over composite numbers as well. Go over primes only.

But sieve is costly. Ignoring sieve, we will take
O(number of primes < N) time

**Optimization:**

If we can get SmallestPrimeFactor(n) in O(1) time, we can solve in logn time.

Because,

6060 - 2
3030 - 2
1515 - 3
505 - 5
101

Everytime, number if being reduced by atleast half

In sieve itself, we can find the SPF of each number - the first prime to cut that number

Helpful when doing multiple queries


-- --


Number of factors
-----------------

If $\large n = p_1 ^ a p_2 ^ b p_3 ^ c \cdots$

Then number of factors = $(1+p_1)(1+p_2)(1+p_3)\cdots$

-- --

Lecture Bookmarks

```
Lecture Start - 00:23:54

```


