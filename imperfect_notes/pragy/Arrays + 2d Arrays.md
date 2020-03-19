Arrays + 2d Arrays
------------------

anish - disruptor


Vivek - May EliteX

-- --
pragy@interviewbit.com


Sum of all Submatrices
----------------------
> Given matrix $M_{n \times n}$, find the sum of all submatrices of M
> 
> Example:
> 
> 1 1
> 1 1
> 
> sum = 1 + 1 + 1 + 1 + 2 + 2 + 2 + 2 + 4
> = 16
> 

![10417df8.png](/users/pragyagarwal/Boostnote/attachments/58e5d3fa-9fb3-4fac-8589-df43c99e4851/10417df8.png =250x)


**Brute Force**
Go over each submatrix, and add

- Submatrix is a rectangle - topleft and bottomright points
- So, four for loops to decide a submatrix (two for topleft, 2 for bottomright)
- then, two for loops to go over each element in the submatrix

Complexity: $O(n^6)$

```python
total = 0

top <- 0 .. n
    left <- 0 .. n
        bottom <- top .. n
            right <- left .. n
                i <- top .. bottom
                    j <- left .. right
                        total += M[i][j]
```


**Optimized**

![50177743.png](/users/pragyagarwal/Boostnote/attachments/58e5d3fa-9fb3-4fac-8589-df43c99e4851/50177743.png =150x)

- Element i, j appears in multiple submatrices
- If a[i][j] occurs in $k$ submatrices, its contribution to the total is $k \times a[i][j]$
- So, we need to count the number of occurances of each i, j

![f9420692.png](/users/pragyagarwal/Boostnote/attachments/58e5d3fa-9fb3-4fac-8589-df43c99e4851/f9420692.png =400x)

Just count the number of submatrices that contain $i, j$ - choose any top right from allowed, choose any bottom right from allowed

For top-right: $(i+1)(j+1)$
For bottom-left: $(n-i) (n-j)$

Total for $i, j = (i+1)(j+1)(n-i)(n-j)$

So, contribution = $a[i][j] \times (i+1)(j+1)(n-i)(n-j)$



$O(n^2)$

-- --

This is called reverse lookup
(not to be confused with inverting the problem)

-- --

Any Submatrix Sum
------------------

> Given $M_{m \times n}$
> $q$ queries, $q$ is large, of the form (top-left, bottom-right)
> Find the sum of the submatrix specified by each query
> 

**Naive**

$O(qmn)$

**Optimized**
Calculate Prefix Sums
- explain for 1d array
- extend to 2d array

![b3741590.png](/users/pragyagarwal/Boostnote/attachments/58e5d3fa-9fb3-4fac-8589-df43c99e4851/b3741590.png)

First by rows, then by columns (or vice versa)

Now, add and substract sum to get the desired sums
![89352278.png](/users/pragyagarwal/Boostnote/attachments/58e5d3fa-9fb3-4fac-8589-df43c99e4851/89352278.png)

Prefix Sum matrix = P

$sum(top, left, bottom, right) = P(bottom, right) - P(bottom, left - 1) - P(top-1, right) + P(top-1, left-1)$


**Corner cases**

-- --


Max Submatrix Sum
------------------

> Given Matrix
> All rows are sorted
> All columns are sorted
> Find the max sum submatrix
> 

![cf7e8a03.png](/users/pragyagarwal/Boostnote/attachments/58e5d3fa-9fb3-4fac-8589-df43c99e4851/cf7e8a03.png =300x)

**Brute force** $O(n^6)$
**All submatrices using prefix sum** $O(n^4)$

**Optimal**
Create suffix sums of matrix
find max value

$O(n^2)$


-- --

Find number ZigZag
------------------


> Given matrix
> Each row and column is sorted
> Find a given number $k$
> 

**Approach 1**

Binary search each row/column

$O(n \log n)$

**Optimal**
![237e989f.png](/users/pragyagarwal/Boostnote/attachments/58e5d3fa-9fb3-4fac-8589-df43c99e4851/237e989f.png =300x)
Start from top right of the remaining matrix

If $k$ is larger, scrape off the row
If $k$ is smaller, scrape off the column

In every iteration, we scrape off one row or column

Complexity: $O(m+n)$

-- --

Chunks
------

> Given Array
> A[N]
> $A[i] \in \{0 .. N-1\}$
> All elements are distinct
> 
The array is a permutation

> 1. Split the array into chunks $C_1, C_2, C_3 \ldots$
> 2. Sort individual chunks
> 3. Concatenate
> 
> The array after these operatio0ns should be sorted
> Find the max number of chunks that the array can be split into
> 

minimizing? ans: 1

sorted array (max)? ans: |A|
reverse sorted? 1



**Observation**

For $i$ to $j$ to be a valid chunk, it has to contain all the numbers $i$ to $j$


**Approach**

Compute max from left to right. If at any point, max == i, we have a chunk
So, do a chunk++



If max > i, can we jump to i? No. because there might be something even greater on the way
Can max < i? No




--- ---

--- ---

Lecture bookmarks

mine -
00:04:00     Lecture Start
00:04:29     Q1 - Find sum of all submatrices of given Matrix
00:05:28     Q1 - Example
00:08:00     Q1 - Brute Force Approach
00:15:30     Q1 - Optimized (Intuition)
00:19:28     Q1 - Optimized (Approach)
00:24:56     Q1 - Optimized - Formula re-explanation
00:27:30     Pattern: Reverse lookup
00:28:16     Q2 - Answer many submatrix sum Queries
00:30:30     Q2 - Brute Force Approach
00:31:20     Q2 - 1D Array Prefix Sum
00:35:20     Q2 - Extending prefix-sum to Matrices
00:46:25     Q2 - Corner Cases
00:48:07     Q3 - Given Matrix with rows & columns sorted, find Largest sum submatrix
00:49:42     Q3 - Brute Force Approach
00:50:47     Q3 - Optimization 1
00:52:38     Q3 - Optimization 2
01:00:07     Q4 - Given Matrix with rows & columns sorted, search for some key k
01:00:47     Q4 - Binary Search Approach
01:03:27     Q4 - ZigZag approach
01:15:22     Q5 - Max number of chunks
01:18:18     Q5 - Example
01:20:18     Q5 - Special Cases
01:22:47     Q5 - Observations
01:25:20     Q5 - Optimized
01:29:15     Q5 - Example Run
01:30:15     Q5 - Pseudo Code
01:32:20     Doubt Clearing
