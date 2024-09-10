# Bit Manipulation 2

## Revision Quizzes

### Question
If the last bit(**0<sup>th</sup> bit**) of a number is 1     (rest can be anything), then the number is?

### Choices

- [ ] Even
- [x] Odd
- [ ] Cannot be determined
- [ ] 1

---


### Question
What is the time complexity of the operation to check whether the i-th bit of a number with $N$ bits is set or not?


### Choices
- [ ] O(N^2^)
- [ ] O(log^2^(N))
- [x] O(1)
- [ ] O(N)

---
### Question
What is the time complexity to count the total number of set bits of an integer with $N$ bits ?

### Choices
- [ ] O(1)
- [x] O(N)
- [ ] O(log(N))
- [ ] O(sqrt(N))


---
## Problem 1 Every element appear thrice except one


### Problem Statement
Given an integer array, all the elements will occur thrice but one. Find the unique element.

### Example
**Input:** [4, 5, 5, 4, 1, 6, 6, 4, 5, 6]
**Output:** 1

`Only 1 occurs a single time`

## Approach 1: Brute Force
Using two for loops and counting the occurence of each number.

### Complexity
**Time Complexity:** O(N^2)
**Space Complexity:** O(1)


## Approach 2: Best Approach
**Interesting Solution!**
Bitwise operators work on bit level, so let's see how XOR was working on bits.
For that, let's write binary representation of every number.

### Observations:
For every bit position, if we count the number of 1s the count should be even because numbers appear in pairs, but it can be odd if the bit in a single number is set for that position.


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/237/original/upload_0afb41111a02da1bd77c0005ef443a69.png?1696401793)" width=500/>

* Iterate on every bit.
* If the count of numbers in which ith bit is set is a multiple of 3, then in answer ith bit is NOT SET.
* If the count of numbers in which ith bit is of the form (3 * x) + 1, then in answer ith bit is SET.

### Pseudocode
```cpp=
ans = 0;
    
for(i -> 0 to 31) { // go to every bit one by one  
    cnt = 0;
    
    for(j -> 0 to arr.size - 1) { // iterate on array
   
       // check if ith bit is set
       if((arr[j] & (1<<i))cnt++;
    }
          
    if(cnt % 3 == 1) // If the count is not the multiple of 3
        ans = ans | 1 << i; // set ith bit in ans
}
  
print(ans);
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(1)

---
## Problem 2 Every element appear twice except two


### Problem Statement
Given an integer array, all the elements will occur twice except two. Find those two elements.

**Input:** [4, 5, 4, 1, 6, 6, 5, 2]

**Output:** 1, 2

### Hint:
* Will finding XOR help ? May be!
* What do we get if we XOR all numbers ? XOR of the two unique numbers!
* From that can we identify/separate the two numbers ? Not Really! Why?
    * Example: If XOR is 7, we aren't sure which 2 numbers are they. (2, 5), (1, 6), (3, 4), ... have xor = 7, so we won't be able to identify!


***Is there any way in which we can identify the two numbers from their XOR ?***

Suppose if two unique numbers are **a** and **b**. Their XOR is **c**.
In **c** if say 0th bit is set, what does that tell about a and b ?
In one of the numbers the bit is set and in other the bit is unset! So, can we identify the numbers based on that ?

### Idea:

* We will find the position of any set bit in XOR c, it will denote that this bit is different in a and b.
* Now, we divide the entire array in two groups, based upon whether that particular bit is set or not.
* This way a and b will fall into different groups.
* Now since every number repeats twice, they will cancel out when we take XOR of the two groups individually leaving a and b.


### Pseudocode
```cpp=
    xorAll = 0;

    // XOR of all numbers in the array
    for (i -> 0 to N - 1) {
        xorAll ^= A[i];
    }

    // Find the rightmost set bit position
    // Note: Any other bit can be used as well
    declare pos 
    
    for(pos = 0; pos < 32; pos++)
    {
        if(checkbit(xorAll,pos))
            break;
    }

    num1 = 0;
    num2 = 0;

    // Divide the array into two groups based on the rightmost set bit
    for (i -> 0 to N - 1) {
        if (checkbit(A[i], pos)) {
            num1 ^= A[i];
        } else {
            num2 ^= A[i];
        }
    }

   print(num1);
   print(num2);
```

---

### Question
What is the time complexity to find two unique elements where every element is present 2 times except for two unique elements?

### Choices
- [ ] O(1)
- [ ] O(log(N))
- [x] O(N)
- [ ] O(32 * N)

