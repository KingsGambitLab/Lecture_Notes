# Maths 3: Prime Numbers

## Agenda

* Introduction to Prime Numbers
* Get all primes from 1 to N
* Print smallest prime factor for 2 to N
* Prime Factorization
* Get the number of factors/divisors

---
## Introduction to Prime Numbers


### What are Prime Numbers?

Numbers having only 2 factors i.e, 1 and the number itself are known as Prime Numbers 

**Example:** 2, 5, 7, 11

---
## Problem 1 Check if a number is prime or not


### Problem Description

Given a number, we need to check wheather its a prime number or not

### Example
**Input:**
```
n = 3

n = 4
```

**Output:**
```
true

false
```

---


### Question
Check whether 11 is a prime number or not!

### Choices
- [x] true, 11 is a prime number
- [ ] false, 11 is not a prime number


---
## Check if a number is prime or not Approach



### Approach

* We need to count the number of factors:
    * if factors = 2, then it is prime
    * otherwise if factors >2, then it is non prime


### Code snippet

```java 
function checkPrime(function n){
    count=0;
    for(i -> 1 to sqrt(n)){
        if(n % i == 0){
            if(i == n / i) {
                count++;
            }
            else {
                count += 2;
            }
        }
    }
    if(count == 2) {
        print("prime");
    }
    else {
        print("Not Prime");
   }
}
```

---
## Problem 2 SecurePrime's Encryption Strategy

### Scenerio
**SecurePrime Inc.** a renowned cybersecurity firm, is on a mission to upgrade its **encryption** techniques to outsmart potential attackers. Their strategy involves utilizing **prime numbers**, known for their pivotal role in strengthening cryptographic systems

### Problem Statement
**SecurePrime Inc.** plans to enhance its **encryption keys** by incorporating **random prime numbers** from the **1 to A** into their algorithms. This approach significantly complicates any brute force attempts by attackers, making the encryption much more robust and reliable.

### Task
As the requirement , you need to generate prime numbers** from the **1 to A**

### Example
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/372/original/upload_ca624d99d0511b1d5e5bfea2d1f07826.png?1697652469" width="500"/>

---

### Question
Find all the prime numbers from 1 to N

### Choices
- [ ] 1, 2, 3, 5, 7
- [ ] 2, 3, 5, 7, 8
- [x] 2, 3, 5, 7
- [ ] 2, 5 ,7



---
## SecurePrime's Encryption Strategy Solution


### Solution
**Brute Force:** Iterate from 1 to N, and check if a number is prime or not.

```java 
function printAllPrime(n) {
    for (i -> 2 to n) {
        if(checkPrime(i) == true) {
            print(i + " ");
        }
    }
}
```

* **Time Complexity (TC):** The time complexity of the given function is $O(n√n)$, as it iterates through numbers from 2 to N and for each number, it checks divisibility up to the square root of that number.
* **Space Complexity (SC):** The space complexity is O(1), as the function uses a constant amount of extra space regardless of the input size.

---
## Sieve of Eratosthenes


### Optimized approach for counting number of primes between 1 to N

### Approach

* **Assumption:** Begin by assuming that all numbers from 2 to N are prime numbers.
* **Marking Non-Primes:** Start with the first prime number, which is 2. Since 2 is a prime number, mark all its multiples as non-prime. These multiples are 4, 6, 8, and so on.
* **Move to Next Unmarked Number:** Move to the next unmarked number, which is 3. Since 3 is a prime number, mark all its multiples as non-prime. These multiples are 6, 9, 12, and so on. Notice that we skip numbers that have already been marked as non-prime in previous steps. Unmarked numbers are prime as they do not have any number less then themselves a factor of the number except 1. Which means they are prime
* **Repeat for Remaining Unmarked Numbers:** Continue this process for the remaining unmarked numbers, each time marking all their multiples as non-prime.
* **Completion:** After going through all numbers up to the square root of N, the remaining unmarked numbers are prime numbers. This is because their multiples have been marked as non-prime in previous steps.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/373/original/upload_b442db3bcc3a4185648ef1d3ecca0ea5.png?1697652539" width="500"/>

### Code Snippet

```java 
function printAllPrime(n) {
    isPrime = new array of size [n + 1]; // Initialize a boolean array to track prime numbers
    fill all values of isPrime from 2 to n with true     // Assume all numbers from 2 to n are prime
    
    for (i -> 2 to sqrt(n)) {
        if (isPrime[i]) {
            j = i * i ;
            while(j <= n) {
                isPrime[j] = false; // Mark multiples of the current prime as non-prime
                j = j + i ;
            }
        }
    }
}
```

### Optimization in Sieve of Eratosthenes

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/374/original/upload_b73738ff854848f11bb17d23ea42e4f3.png?1697652577)" width="500"/>

Starting from the square of each prime number, mark all its multiples as non-prime in the sieve. This is efficient because smaller multiples of the prime would have already been marked by smaller primes. By avoiding redundant marking, we optimize the Sieve of Eratosthenes algorithm.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/375/original/upload_a4554ab46a486e271d5e7e6415c6c634.png?1697653082" width="500"/>

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/376/original/upload_7360b60910237c0941d76a96b6bd05d4.png?1697653111" width="500"/>

* **Time Complexity (TC):** The optimized Sieve of Eratosthenes has a time complexity of O(n log log n), which means it grows very slowly. This is because the algorithm only visits and marks numbers up to the square root of N, and the number of non-prime numbers marked is logarithmic with respect to N.
* **Space Complexity (SC):** The space complexity is O(n), which is used to store the boolean array indicating whether each number is prime or not. The space used is directly proportional to the input size N.


---
## Count of Divisors


### Problem Statement
Given a number n, you need to find the count of divisors for every integer from 1 to n. The task is to efficiently calculate the number of divisors for all numbers in the range using a modified prime sieve technique.

### Examples
Input: n=6
Output: [1,2,2,3,2,4]
This means:
1 has 1 divisor.
2 has 2 divisors: 1,2
3 has 2 divisors: 1,3
4 has 3 divisors: 1,2,4
5 has 2 divisors: 1,5
6 has 4 divisors: 1,2,3,6

### Observation
The number of divisors for a number k can be calculated by counting how many integers between 1 and k divide k exactly. 
### For example:
4 is divisible by 1,2 and 4, so it has 3 divisors.
6 is divisible by 1,2,3 and 6, so it has 4 divisors.

---
## Count of Divisors using Sieve

We can use a modified sieve approach to calculate the number of divisors for each number up to n. 

The idea is to iterate over each number i and increment the divisor count for all multiples of i. **Here's how it works:**
1. Initialize an array divisor_count of size n+1 with all elements set to zero. This array will hold the number of divisors for each number.
2. Iterate through each number i from 1 to n. **For each i:**
    - Increment the divisor count for all multiples of i (i.e., divisor_count[j]++ where j is a multiple of i).
3. Return the divisor_count array (ignoring the 0th index as it is unused).

### Find divisors

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/382/original/upload_8268cdcd52dde872eff270cd07fe0723_%281%29.png?1697655012" width="500"/>


---
## Sorted Permutation Rank


### Problem Description
You are given a string AAA containing distinct characters (no characters are repeated). The task is to find the rank of this string among all its permutations when sorted in lexicographical (dictionary) order.

### Explanation in Simple Steps
Lexicographical order is the order in which words are arranged in a dictionary. For example, for the string "ABC":
The permutations in order are: "ABC", "ACB", "BAC", "BCA", "CAB", "CBA".
The rank of "ACB" is 2, because it is the second permutation in this list.

### How to Find the Rank of the String:
* To determine the rank of the string AAA, we need to count how many permutations would appear before it in lexicographical order.
* For each character in the string, you compare it with the characters that come after it and count how many characters are smaller than it. These smaller characters could have appeared in the earlier permutations.

---
## Sorted Permutation Rank Solution


### Step-by-Step Process:
* Start with the first character of the string.
* For each character, calculate how many permutations can be formed with the smaller characters to the right of it.
* Add up these counts to get the total number of permutations that come before the string.
* The rank is 1 plus this total count (since rank starts at 1).

### Modulo Operation:
Since the rank might be a large number, return the answer modulo 100000310000031000003 (a large prime number) to ensure it fits within standard data types.

### Example Walkthrough
Consider the string A="BAC":
**Step 1:** Look at the first character, "B".
Characters that could come before "B" in sorted order are "A".
There are 2 remaining characters ("AC"), which can be arranged in 2!=2 ways.
So, 2 permutations start with "A", which would come before any permutation starting with "B".
**Step 2:** Move to the next character, "A".
There are no characters smaller than "A" after it, so no new permutations can be formed that would come before "BAC".
**Step 3:** Finally, count the total permutations before "BAC":
There are 2 permutations before "BAC", so the rank of "BAC" is 2+1=32 + 1 = 32+1=3.
Thus, the rank of "BAC" is 3.

### Pseudocode
```javascript
function find_rank(A):
    rank = 1
    n = len(A)
    factorials[0] = 1
    FOR i FROM 1 TO n:
        factorials[i] = (factorials[i-1] * i) % 1000003
    
    FOR i FROM 0 TO n-1:
        COUNT smaller characters on the right of A[i]
        rank += COUNT * factorials[n-i-1]
        rank %= 1000003
        
    RETURN rank
```

### Key Points:
- **Counting:** For each character, count the number of smaller characters to its right and calculate the permutations.
- **Result:** Add up these permutation counts, add 1 for the current string, and return the result modulo 1000003.
- This approach efficiently calculates the rank in O(n^2^) time complexity, which is feasible for strings of moderate length.
