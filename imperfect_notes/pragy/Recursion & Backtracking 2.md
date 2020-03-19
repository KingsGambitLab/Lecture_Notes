Recursion and Backtracking 2
----------------------------

```
https://www.interviewbit.com/problems/kth-permutation-sequence/
https://www.interviewbit.com/problems/number-of-squareful-arrays/
https://www.interviewbit.com/problems/gray-code/
https://www.interviewbit.com/problems/combination-sum-ii/
https://www.interviewbit.com/problems/nqueens/
https://www.interviewbit.com/problems/all-unique-permutations/
https://www.interviewbit.com/problems/sorted-permutation-rank/
https://www.interviewbit.com/problems/word-break-ii/



https://www.interviewbit.com/problems/palindrome-partitioning/
https://www.interviewbit.com/problems/unique-paths-iii/
```


Permutations
------------

> Given String containing distinct characters. Print all permutations of the string
> 

Approach:

Fix the first char

![e777e692.png](:storage/b3ce81fe-2514-47db-9c8f-6e5d3b0dd2aa/e777e692.png =350x)

Can essentially be achieved by swapping

![14bdca46.png](:storage/1d31a4b8-2ef8-4299-8673-f3b477ed5dec/812b8234.png)

```python
def permute(S, i):
    if i == len(S):
        print(S)
    for j in range(i, len(S)):
        S[i], S[j] = S[j], S[i]
        permute(S, i+1)
        S[i], S[j] = S[j], S[i]  # backtrack
```

-- --

Lexicographic permutations
--------------------------

asked in Amazon

- start with sorted elements
- instead of swap, do right rotation(i to j). Undo = left rotate
- swap was O(1), whereas rotation is O(n)

-- --


Unique Permutations, when string has duplicates
-----------------------------------------------

![255b5284.png](:storage/b3ce81fe-2514-47db-9c8f-6e5d3b0dd2aa/255b5284.png =400x)

Basically, if we're swapping S[i] with S[j], but S[j] already occured earlier from S[i] .. S[j-1], then swapping will result in repetition

```python
def permute_distinct(S, i):
    if i == len(S):
        print(S)

    for j in range(i, len(S)):
        if S[j] in S[i:j]:
            continue
        S[i], S[j] = S[j], S[i]
        permute_distinct(S, i+1)
        S[i], S[j] = S[j], S[i]  # backtrack
```

-- --

Kth Permutation Sequence
------------------------
> Given A[N] and k,
> find the kth permutation
> 

[Kth Permutation Sequence - InterviewBit](https://www.interviewbit.com/problems/kth-permutation-sequence/)

$\dfrac{k}{(n-1)!}$ will give us the index of the first digit. Remove that digit, and continue


```python
def get_perm(A, k):
    perm = []
    while A:
        # get the index of current digit
        div = factorial(len(A)-1)
        i, k = divmod(k, div)
        perm.append(A[i])
        # remove handled number
        del A[index]
    return perm
```

-- --

Sorted Permutation Rank
-----------------------
> Given S, find the rank of the string amongst its permutations sorted lexicographically.
> Assume that no characters are repeated.
> 
```
Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
```

**Hint:**
If the first character is X, all permutations which had the first character less than X would come before this permutation when sorted lexicographically.

Number of permutation with a character C as the first character = number of permutation possible with remaining $N-1$ character = $(N-1)!$

**Approach:**

rank = number of characters less than first character * (N-1)! + rank of permutation of string with the first character removed

```
Lets say out string is “VIEW”.

Character 1 : 'V'
All permutations which start with 'I', 'E' would come before 'VIEW'.
Number of such permutations = 3! * 2 = 12

Lets now remove ‘V’ and look at the rank of the permutation ‘IEW’.

Character 2 : ‘I’
All permutations which start with ‘E’ will come before ‘IEW’
Number of such permutation = 2! = 2.

Now, we will limit ourself to the rank of ‘EW’.

Character 3:
‘EW’ is the first permutation when the 2 permutations are arranged.

So, we see that there are 12 + 2 = 14 permutations that would come before "VIEW".
Hence, rank of permutation = 15.
```


[Sorted Permutation Rank - InterviewBit](https://www.interviewbit.com/problems/sorted-permutation-rank/)


-- --

Number of Squareful Arrays
--------------------------

> Given A[N]
> array is squareful if for every pair of adjacent elements, their sum is a perfect square
>
> Find and return the number of permutations of A that are squareful
> 


> Example:
> A = [2, 2, 2]
> output: 1
> 
> A = [1, 17, 8]
> output: 2
> [1, 8, 17], [17, 8, 1]
> 


```python
def check(a, b):
    sq = int((a + b) ** 0.5)
    return (sq * sq) == (a + b)

if len(A) == 1:  # corner case
    return int(check(A[0], 0))
    
count = 0
def permute_distinct(S, i):
    global count
    if i == len(S):
        count += 1

    for j in range(i, len(S)):
        if S[j] in S[i:j]:  # prevent duplicates
            continue
        if i > 0 and (not check(S[j], S[i-1])):  # invalid solution - branch and bound
            continue
        S[i], S[j] = S[j], S[i]
        permute_distinct(S, i+1)
        S[i], S[j] = S[j], S[i]  # backtrack
        
permute_distinct(A, 0)
return count
```

-- --

Gray Code
---------
> Given a non-negative integer N representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
> The gray code is a binary numeral system where two successive values differ in only one bit.


G(n+1) can be constructed as:
0 G(n)
1 R(n)

```
Example G(2) to G(3):

0 00
0 01
0 11
0 10
----
1 10
1 11
1 01
1 00
```

```python
def gray(self, n):
    codes = [0, 1]   # length 1
    for i in range(1, n):
        new_codes = [s | (1 << i) for s in reversed(codes)]
        codes += new_codes
    
    return codes
```



-- --

Combination Sum II
------------------

[Combination Sum II - InterviewBit](https://www.interviewbit.com/problems/combination-sum-ii/)


We already did this. Why couldn't you solve it!?

-- --

N Queens
--------

[NQueens - InterviewBit](https://www.interviewbit.com/problems/nqueens/)

Backtracking

- Place one queen per row
- backtrack if failed


-- --

Word Break II
-------------

> Given a string A and a dictionary of words B, add spaces in A to construct a sentence where each word is a valid dictionary word.
> 

```
Input 1:
    A = "catsanddog",
    B = ["cat", "cats", "and", "sand", "dog"]

Output 1:
    ["cat sand dog", "cats and dog"]
```

```python

def wordBreak(A, B):
    B = set(B)
    sents = []
    
    def foo(i, start, sent):
        word = A[start:i+1]
        
        if i == len(A):
            if word in B:
                sents.append((sent + ' ' + word).strip())
            return
        
        if word in B:
            foo(i+1, i+1, sent + ' ' + word)
        foo(i+1, start, sent)
    
    foo(0, 0, '')
```