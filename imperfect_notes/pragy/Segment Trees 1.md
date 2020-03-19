Segment Trees
-------------

Have ever used segment tree? Implemented?

Rarely asked in interviews, but good to know from a competitive programming perspective.

We will cover basics today, and delve into more complex stuff later on.

Has range queries and update queries.
-- --

> Given array  (has -ve, has duplicates, unsorted)
> 1 2 -3 3 4 7 4 6
> Given multiple queries that ask the sum from $a_i$ to $a_j$

Brute Force: O(n) per query

Solve using prefix sum. Preprocessing: O(n), query: O(1)

> Now, we also have update queries like - change $a_4$ to 7

- Prefix sum:
    + Query: O(1)
    + Update: O(n) because we gotta change entire prefix sum
- Normal:
    + Query: O(n)
    + Update: O(1)

- Can we do it in $O(\log n)$ time for each query?
    What comes to your mind when we talk about $O(\log n)$ time?
    ![8fd0176c.png](:storage/d9e5e2af-8dad-435c-b0f0-729fca3448fd/31b63f54.png)
- Discarding part of the search space

![45bdcdc1.png](:storage/d9e5e2af-8dad-435c-b0f0-729fca3448fd/45bdcdc1.png)

-- --

Segment Tree
------------

- ![e3eb808f.png](:storage/d9e5e2af-8dad-435c-b0f0-729fca3448fd/e3eb808f.png)
- ![8598c257.png](:storage/d9e5e2af-8dad-435c-b0f0-729fca3448fd/8598c257.png)
    + Update: $O(\log n)$
        + ![27ac5aa0.png](:storage/d9e5e2af-8dad-435c-b0f0-729fca3448fd/27ac5aa0.png)
    + Query: $O(\log n)$
        + if query completely overlaps node range: return entire node value
        + if no overlap at all: return null
        + if some overlap: recurse on both children and apply operation

- worst case: 4 * n because left and right and attached right and left
- Operation must be Associative

-- --


Build Segment Tree
------------------

```python
data = [...]  # N
tree = [...]  # 4N # 2N-1      - N leaves and N-1 elems in parents

left  = lambda n: 2 * n + 1
right = lambda n: 2 * n + 2

def build(start, end, pos):
    if start == end:
        tree[pos] = data[start]
        return
    # post order traversal
    mid = (start + end) // 2
    build(start, mid, left(pos))
    build(mid+1, end, right(pos))
    tree[pos] = tree[left(pos)] + tree[right(pos)]

build(0, N-1, 0)
```

Note: Always implement it as a class. Do NOT couple your algorithm with your DS.

Okay for Competitive Coding. Reject in interviews.

O(n), because you visit each node only once.

Query
--------------------------

```python
def query(q_start, q_end, r_start, r_end, pos):
    if q_start <=r_start <= r_end <= q_end:
        return tree[pos]
    if r_end < q_start or r_start > q_end:
        return 0
    
    mid = (r_start + r_end) // 2
    
    left  = query(q_start, q_end, r_start, mid,  left(pos))
    right = query(q_start, q_end, mid+1, r_end, right(pos))
    
    return left + right
```


Updating
--------

Simple - just change the values from node up to the root - recursive,y come down to the node, update and update each sum



Complexity for query and update: $O(\log n)$, because height of tree is $O(\log n)$
-- --

