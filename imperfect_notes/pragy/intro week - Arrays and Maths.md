Intro Week - 2 - Arrays and Math
--------------------------------

**PRIVATE**

- Explain that we're just giving a trailer for the first week. Will dive into much more detail later on. HLD tomorrow, LLD day after, special talk on Friday/Saturday.
- will cover DS/Algo, advanced problems, advanced topics like Segment Trees, lazy propagation, Fenwick Trees, Bitmask DP, Network Flow (Mincut-Maxflow)

**PUBLIC**

- We're assuming that you know what arrays are, basic loops, if else
- Anyone who doesn't understand arrays?
- Array is a collection of homogeneous data


C++ Vector vs Array
-------------------

- how do arrays work?
    - allocate space of fixed size
- how are vectors different?
    - Vectors are dynamic. Arrays are not
- How are vectors allocated?
    - when space is full, how do we push_back?
        - double the space
        - Copy the current elements
        - Free previous array
    - what is the time complexity of inserting elements?
        - Time complexity - worst case - O(n)
        - Amortized - O(1)
    - Explain what "amortized" means
    - Actually have growth factor - 1.7, and not 2 to scale the array by
    - Overall, not a big overhead


Passing arrays by value / reference
-----------------------------------

```c++
int run() {
    int n;
    cin >> n;
    vector<int> v;
    for(int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    return find_middle(v);
}


int find_middle(vector<int> v) {
    return v[v.size() / 2];
}

```

C++

- Time complexity overall? O(n)
- For find_middle? O(n)
    - Note that here the passing is by value - the entire array is being copied
    - No changes will reflect if we make changes in the function

So, if you use pass by reference

```c++
int find_middle(vector<int> & v) {
    ...
}
```

- now it is being passed by reference
- Java has objects. Objects are passed. So, by reference. O(1), and mutable
- important because
    - passing by value can slow down the code
    - passing by reference can cause side effects

-- --


Absolute Values
---------------

> 
> A: 1 5 13 8
> can have -ves
> Find i, j so that i != j and
> $\Bigl | A[i] - A[j] \Bigr | + \Bigl | i - j \Bigr |$ is maximized

```python
def abs(x):
    if x < 0: return -x
    else: return x
```

1. Ask clarifying questions
    - can we have -ve elements?
    - What happens when the array has size 1?
        - return -1
2. Think of the brute force appraoch
3. Optimize


**Brute Force**

$O(n^2)$ - all combinations of i, j
Get max


**Optimized**

Expand the expression if you don't see any patterns
Expand the abs()

- enforce i > j
- Two cases:
    - A[i] > A[j]
        - $= (A[i] + i) - (A[j] + j)$
    - A[i] < A[j]
        - $= (A[j] - j) - (A[i] - i)$
- So, calculate (A[i] + i) as X and A([i] - i) as Y
- Find maxX, minX, maxY, minY
- return max((maxX-minX), (maxY-minY))

- How does this take care of i = j case?
    - $i = j$ gives answer of 0
    - we know that since $|i-j| > 0$ for some $(i, j)$, no matter what $|A[i] - A[j]|$ is, our answer will at least be greater than 0

-- --

Trapping Rain
-------------

> Buildings
> Rain from top.
> Find the area of the rain trapped.

![059e3810.png](:storage/45f4ad51-49ea-4265-bb5b-39516f1b6b05/059e3810.png)


Approach:

Look at a building.
Amount of water that I can store is the min height of the tallest building on left and right

$O(n^2)$

- how can we calculate max and min efficiently?
    - Prefix and suffix max

```c++
prefix_max[0] = A[0];
for(int i = 1; i < N; i++)
    prefix_max[i] = max(prefix_max[i-1], A[i]);

suffix_max[N-1] = A[N-1];
for(int i = N-2; i >= 0; i--)
    suffix_max[i] = max(suffix_max[i-1], A[i]);

```

Now, for every element i, look at the prefix_max[i-1] and suffix_max[i+1] and take min-height

-- --

Max Gap
-------

> A = 2 5 13 8 7 6
> unsorted array, duplicates possible
> if A as sorted, then find max(A[i+1] - A[i])
> don't sort, use linear space


Make sure that everyone knows what sorting is


Approach:
What is the max possible difference? max - min   (min min min max max max)
What is the min possible difference? (max-min) / (N-1)   (min min+d min+2d .. max)


Now, create buckets with the size of gap

gap = (max - min) / (N-1)

Create buckets of size of gap
![7495d1f7.png](:storage/45f4ad51-49ea-4265-bb5b-39516f1b6b05/7495d1f7.png)

- can the two elements from the same bucket have the max-gap? No, because bucket size = min gap possible
- so, elements from different buckets must give us the answer
- all buckets have 1 exactly element  - answer is gap
- Otherwise, atleast 1 bucket will be empty  - answer is more than gap

20 8 15 12
min = 8
max = 20

max_gap = 20 - 8 = 12
min_gap = (20 - 8) / (4-1) = 4

now, create buckets of size 4 from min and max

-- --

comunicate with each other

ping the TA on flock

ping us

-- --

TA session tomorrow

1st week - just introductory stuff
recording of this video will be up
share notes