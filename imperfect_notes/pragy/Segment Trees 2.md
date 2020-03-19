Segment Trees 2
---------------

Max and 2nd Max
---------------

store both.
to combine, find max and 2nd max of 4 number

-- --

> n processes start, end
> 1 processor
> find out if a new process can be added
sort and binary search



> n processes start, end
> 4 processors
> find out if a new process can be added

allocate processes to processors and then previous approach

> n processes start, end
> k processors
> find out if a new process can be added

+1 -1 trick
prefix sum

max range query segment tree over the prefix sum

-- --

Flip Bits
---------

> Given series of coin flips
> 0 1 0 1 1 0 0 1
> Given a range, find the number of heads
> Also, given a index, flip the coin at that index
> 

Simple, just use Segment Tree


-- --

Bob and Queries
--------

> start A[n] = [0, 0, 0, ...]
> 3 types of queries
> 1. a[i] = 2 * a[i] + 1
> 2. a[i] = a[i] // 2
> 3. sum of counts of set bits in the range s, e
> 

observation: numbers will always be 0, 1, 11, 111, ... in binary

can never reach a non-0 even number

so can just keep count of set bits

1. increase a leaf value
2. decrease a leaf value
3. normal seg tree range query

-- --

Powers of 3
-----------

> binary string
> 1. l, r: print value of binary string l to r mod 3
> 2. i: flip the bit at index i

- store the bit in leaf
- combine two nodes $= (2^x\cdot l + r) \mod 3$

![aa19c149.png](:storage/142c3fe6-1d20-4d84-8ee9-51c8f2751685/aa19c149.png)

![21e3e2c1.png](:storage/142c3fe6-1d20-4d84-8ee9-51c8f2751685/21e3e2c1.png)

-- --



> Given ranges in hours from 0 - 24, mark then in your schedule
> For every marker you place, also output how many overlapping tasks
> 

todo

- build a tree from 0 - 24
- for each query, update each count 


-- --

lazy prop

![ce7714d2.png](:storage/142c3fe6-1d20-4d84-8ee9-51c8f2751685/ce7714d2.png)

lazy tree

- update self. add lazy to children
- always update self from lazy first
- 

-- --

~~Optimzed LCA~~
------------

$O(h)$ when we have pointers to nodes
But takes $O(n)$ when we have to search for the nodes

> Binary Tree, No duplicates
> Given multiple keys of type (a, b), find LCAs
> $O(\log n)$ for each query

- Build Euler Path
- Assign index to each node
- Build Min segment Tree
- Keep index of first occurance in a hashmap


todo


- if no duplicates, just store pointers to each node in a hashmap. Then earlier approach (linked list) is still simpler cause no segment tree

