# Calculating ${n \choose r} \% m$ like a pro

Let's begin with some prerequisites.

## Modular arithmetic

$(a \bmod m)$, also represented as $a \% m =$ remainder left when $a$ is divided by $m$.
Example: $10 \% 7 = 3$

### Properties of $\%$
#### Distritbutive over addition & substraction $(\pm)$
   $$(a\pm b) \% m = \Bigl[ (a \% m ) \pm (b \% m) \Bigr] \% m$$
   $(8+13)\%7 = \Bigl[(8 \% 7) + (13 \% 7)\Bigr]\%7$
$21\%7 = [1 + 6]\%7$
   $0 = 7 \% 7$
   $0 = 0$
#### Distritbutive over multiplication $(\times)$
   $$(a \times b) \% m = \Bigl[ (a \% m ) \times (b \% m) \Bigr] \% m$$
   $(8 \times 13)\%7 = \Bigl[(8 \% 7) \times (13 \% 7)\Bigr]\%7$
   $104 \% 7 = [1 \times 6]\%7$
   $6 = 6 \% 7$
   $6 = 6$
    
- **NOT distributive over $\div$**
    Unlike $+, -, \times$, the modulo operator does not distribute over division.
    So, $\left (\dfrac ab \right )\%m \;\;\red \neq\;\; \left[\dfrac{a\%m}{b\%m}\right] \% m$.
    However, the concept of **Modular Inverse** (discussed later) helps us simplify these calculations.

## Calculating $(n! \bmod m)$ in $\mathcal O(n)$ time

Since $\%$ distributes over $\times$, we can say that

$$(n!) \% m = \Bigl[n (n-1)(n-2) \cdots 1\Bigr] \% m \\[.5em]
=\overbrace{\underbrace{{\underbrace{\overbrace{n \cdot (n-1)}^{\%m} \cdot (n-2)}_{\%m} \cdots} \cdot 2}_{\% m} \cdot 1}^{\%m}$$

So, we can simply calculate factorial, by taking $\%$  after every multiplication.
```python
def fact_mod(n, mod):
    ans = 1
    for i in [1 .. n]
        ans = (ans * i) % mod
    return ans
```

## Binary Exponentiation: calculating $(n^p \bmod m)$ in $\mathcal O(\log_2 p)$ time
```python
def binary_exponentiation(n, p, mod):
    if n == 0: return 0
    if p == 0: return 1
    ans = binary_exponentiation(n, p//2, mod) # note: integer division
    ans = ans * ans
    if p is even:
        return ans
    else:
        return ans * n
```



## Fermat's Little Theorem
If $p$ is prime, then
$$a^p \equiv a \pmod p$$

## Euler's generalization to Fermat's Little theorem

Iff $a$ and $m$ are co-prime, then
$$\boxed{a^{\phi(m)} \equiv 1 \pmod m}$$

**Let's break it down:**
- $a$ is coprime with $m$ iff $gcd(a, m) = 1$, that is, $a$ and $m$ do not have any common factor.
- If $a \bmod m = b \bmod m$, we say that $a \equiv b \pmod m$
- $\phi(m)$ is the Euler's Totient Function for $m$

## Euler's Totient Function $\phi(m)$
The Euler's Totient Function $\phi(m)$ counts the number whole numbers smaller than $m$ which are coprime with $m$

For example, if $m = 30$, then what numbers are coprime with $m$?
```
 1  2  3  4  5  6  7  8  9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
-----------------------------
 1                 7
11    13          17    19
      23                29
-----------------------------
count = 8
```

1. If $m$ is prime,
    $$\boxed{\phi(m) = m - 1}$$
2. If $m$ is not prime, then let us factorize $m$
    Let $m = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot p_3^{\alpha_3} \ldots$
    Then,
    $$\boxed{\phi(m) = m \left (1 - \dfrac1 p_1 \right )\left (1 - \dfrac1 p_2 \right )\left (1 - \dfrac1 p_3 \right ) \cdots}$$

Example,
- if $m = 17$, $\phi(17) = 16$
- if $m = 30 = 2^1 \cdot 3^1 \cdot 5^1$, then
    $\phi(30) = 30 \left( 1 - \dfrac 1 2 \right )\left( 1 - \dfrac 1 3 \right )\left( 1 - \dfrac 1 5 \right )$
    $= 30 \cdot \dfrac12 \cdot \dfrac23 \cdot \dfrac45 = 8$
