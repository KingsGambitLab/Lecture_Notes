Greedy
------

$k$ negations
-------------

> Given A[N]
> can have -ve can have 0s
> k negations
> can choose same element multiple times
> find the maximum sum that you can achieve

always find the smallest and negate it

Sort: $O(n \log n + k)$
Min Heap: $O(n+k \log n)$

Note: 1 2 will have -1 2 or 1 2 as the final answer
can keep toggling the smallest element
-- --

What is Greedy
--------------

Greedy - when optimal solution to a local problem is also the optimal solution to the global problem

That is, if you can act greedily at every step, and still reach the optimal.
If you don't have to think long term to achieve the optimal

-- --

Where will greedy not work?
---------------------------

![65112ffa.png](:storage/8d511c68-5ee9-423f-b945-bf7407cdb509/65112ffa.png)

Local solution is not contributing to the global solution

Whenever greedy works, it will be based on observations and intuition

But have to be careful because can be subtle-non-greedy case

-- --

Max Sum Subset
--------------

> Given A[N] with -ves
> Find the subset of size k with maximum sum
> 

Sort and take top k values

$O(n \log n)$

-- --

Amazon - Min Subset Product
----------------------------

> Given A[N]
> min possible subset product
> 

Examples

> -1 -1 -2 4 5  = -24
> -1 0 2  = -2
> 0 1  = 0
> 

1. If no -ve, then choose min $\geq 0$
2. If k -ve, then choose all $> 0$. don't choose 0
    - if odd -ve, choose all
    - if even -ve, choose the smallest odd -ves

$O(n)$

-- --


Activity Selection
------------------

Multiple companies. Very important

> ![96706e2d.png](:storage/8d511c68-5ee9-423f-b945-bf7407cdb509/96706e2d.png)
> max no of activity that can be performed without overlapps

**Incorrect:** min sized?
```
=============    ===============
           ========
```               

**Incorrect:** start time

**Correct:** least overlaps?

**but easier:** first one to end

sort by end time and execute

**Proof:**

Assume there exists a solution that doesn't include the min end time job.

Add this job. Either it overlaps with 1, or with 0.
Optimal in both cases

So, for every optimal solution without the min end job, we also have an optimal solution with the min end job.

So, optimal to always choose the min end job

![8d6e9fbb.png](:storage/8d511c68-5ee9-423f-b945-bf7407cdb509/8d6e9fbb.png)
-- --

Flights
-------

> start, end time of flights
> num of platforms
> 

+1 -1, prefix sum max

![03c1d903.png](:storage/8d511c68-5ee9-423f-b945-bf7407cdb509/03c1d903.png)

-- --

Job Scheduling + Profit
-----------------------

> day deadlines for jobs
> can perform only 1 job per day

delay the job

$O(n \log n + n^2)$

$n \log n$ to sort by profit
$n^2$ because start at end time and move left to find an empty slot

Can reduce to n log n using BBST

we want the highest number in the set which is less than x
we also want to remove any given number from set

set - upperbound - google

-- --


Rats and Holes
--------------


> Rats
> Holes
> equal count
> locations given for each
> ech rat runs together
> each must reach a hole
> max time so that all reach hole
> 

sort, all go left or all go right

cant cross because that will increase time

```

-------          ----------

vs

       ----------
---------------------------

```