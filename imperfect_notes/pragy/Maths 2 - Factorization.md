Maths 2 - Factorization
-----------------------

All Factors
-----------

> Given number n, find all factors of n
> 

**Observations:**
1. largest factor is n itself
1. all other factors are $\leq n/2$

**Brute Force:**
So, loop from $1 \ldots \frac n 2$

**Time complexity:** $O(n)$


**Observation 3**
Factors come in pairs
(1,n), (2, n/2), (x, n/x) .. 
Need to go only till $\sqrt n$
Why sqrt? if x = n/x, then $x = \sqrt n$

```python
for(i = 1; i < sqrt(n); i++)
    if( n%i == 0 ):
        factors.append(i)
        factors.append(n/i)
if( n % i == 0)
    factors.append(i) # because i = n/i = sqrt(n)
```

Complexity: $O(\sqrt n)$

-- --

Open Door question
------------------

100 doors, all are closed.
1. Open all doors
2. Close every 2nd door
3. Open every 3rd door
4. Close every 4th door

100. Close every 100th door.

Find the number of doors that are left open.

Approach: Door is toggled by each factor.
Find the number of factors for each 0 <= i <= 100

Check if the number of factors is even or odd.

**How to find if the number of factors is even or odd?**


**Brute Force**: Loop and count

**Observation:** Factors come in pairs. Except for $\sqrt n$

Check if perfect square. If perfect suqre - odd, else even.

Finding $\sqrt n$: Binary search / Newton Raphson


-- --

Check Prime
-----------

**Brute Force** Loop from 1 to $\sqrt n$ and check if the count is 1
$O(\sqrt n)$

-- --

Generate all primes till n
--------------------------

Brute force using $\sqrt n$ check prime: $O(n \times \sqrt n)$

**Sieve of Eratosthenes**  (era - tos - thenis)

- Assume all prime
- cut 1
- next uncut is prime
- cut all multiples - because can't be prime
- go only till sqrt

![3fa0e7ff.png](:storage/3d9f53c5-6f21-4ce2-b310-40e38a17113c/3fa0e7ff.png =400x)

Optimizatiopn
- start cutting from $i\times i$, because $i \times (i-1,2..)$ is already cut
- $i$ needs to go only till $sqrt n$

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
4 -> O(1)
5 -> N/5
6 -> O(1)
7 -> N/7
8 -> O(1)
9 -> O(1)
...
$\sqrt N$ -> 1 or O(1)

total = $N (1/1 + 1/2 + 1/3 + 1/5 + 1/7...)$

$\Large N \sum_p \frac 1 p$

= $O(n \log \log n)$ ([Mertens' theorems - Wikipedia](https://en.wikipedia.org/wiki/Mertens%27_theorems))

Memory = $O(n)$

Simple Upperbound can be $n \log n$ because $\sum_i \frac 1 i = \Theta(\log n)$ (proof by integration)


Note: better algos exist for primality testing, as well as sieve.

-- --

Caution: Don't build a sieve if you just want to check one number. $O(\sqrt n)$ vs $O(n \log n)$


-- --

Prime Factorization
-------------------

1. find all factors and check if prime


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

Time complexity: $O(\sqrt n)$
Inner loop doesn't matter since n is getting decreased


**Optimization 1:**

We're going over composite numbers as well. Go over primes only.

But sieve is costly. Ignoring sieve, we will take
O(number of primes < N) time

**Optimization 2:**

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

If $\Large n = p_1 ^ a p_2 ^ b p_3 ^ c \cdots$

Then number of factors $= \phi(n) = (1+p_1)(1+p_2)(1+p_3)\cdots$
Sum of factors
$= (1 + p_1 + p_1^2 + \cdots + p_1^a) \cdot (1 + p_2 + p_2^2 + \cdots + p_2^b) \cdots$

$= \Large \frac{p_1^{a+1} - 1}{p_1 - 1} \cdot \frac{p_2^{b+1} - 1}{p_2 - 1} \cdots$
can be found using mod-exponentiation

Product of factors = $n^{\phi(n)}$ where $\phi(n)$ is the number of factors

-- --


https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n