
# DSA: Topological Sort & Interview Problems

##  Possibility of finishing the courses

Given N courses with pre-requisites, we have to check if it is possible to finish all the course ?

### Example:

N = 5

**Pre-requisites**
1 ---> 2 & 3 [1 is pre-req for 2 and 3]
2 ---> 3 & 5
3 ---> 4
4 ---> 2

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/951/original/Screenshot_2024-02-01_at_6.42.52_PM.png?1706793211" width=300  />
     
The pre-req information is represented in above directed graph.


### Explanantion:

**Que:** Which course shall we complete first?
The one having no pre-requisites. (say 1)

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/952/original/Screenshot_2024-02-01_at_6.48.07_PM.png?1706793500" width=300 />

Next, which one shall we pick ?

We can't pick any course because of the dependencies. Hence, it means we can't finish courses in above example.

The reason is there's a cycle!
Have you heard of the term deadlock ? [*For experience we need job, for job we need experience like scenario :p* ]

**Conclusion:** If it's a cyclic graph, answer will always be false, else true.

**Observation:** To solve the problem, we need directed acyclic graph!

### Possibility of finishing courses approach

**Example:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/953/original/Screenshot_2024-02-01_at_6.53.36_PM.png?1706793868" width=320 />

Pick ? 1 [not dependant on any other course]
Next Pick ? 2
Next Pick ? 3
Next Pick ? 4
Next Pick ? 5

**Order:**
1 2 3 4 5

The above order is known as topological sort/ topological order.

**Que:** For one graph, can we have only one topological order?

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/955/original/Screenshot_2024-02-01_at_6.57.14_PM.png?1706794109" width=300 />

Is the order 1 2 3 4 5 valid ? YES!
What about 1 3 2 4 5 ? YES!
What about 1 3 4 2 5 ? YES!

Hence, it is possible that we have multiple topological order for a given graph.

### Definition

**Topological sort** is a linear ordering of the vertices (nodes) in a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u comes before vertex v in the ordering. In other words, it arranges the nodes in such a way that if there is a directed edge from node A to node B, then node A comes before node B in the sorted order.

### Topological Sort

Let's find topological ordering of below graph!

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/956/original/Screenshot_2024-02-01_at_7.04.26_PM.png?1706794475" width=350 />

**Indegree:** The count of incoming nodes is known as indegree of a node.

For above graph, the indegrees will be as follows -

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/957/original/Screenshot_2024-02-01_at_7.08.52_PM.png?1706794742" width = 350 />

### Next Steps
* Insert all the nodes with indegree=0 in a queue
* Dequeue an element from the queue and update the indegree for all the neighbours, if the indegree for any nbr becomes 0 add that node in the queue.



### Approach:
* Create an array to store indegrees, initially set all values to zero.
* Iterate through each node in the graph using a loop.
* For each node, traverse its outgoing edges by iterating through its adjacency list.
* For each neighboring node in the adjacency list, increment its indegree count by one.
* Continue the loop until you've processed all nodes in the graph.
* The array now contains the indegree of each node, where the value at index i represents the indegree of node i.

### Example:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/522/original/upload_8ed904670ed12810074a3d07c9d7ea10.png?1697742167" width=400/>

In the above photo we can refer the indegree of each of the nodes is written in green. 

### Pseudocode:

```java
in_degree[N], i,
for(i -> 0 to n - 1)	
    in_degree[i] = 0;

for(i -> 0 to n - 1)
{
    for(each neighbour in adj[i])
    {
        in_degree[i] += 1;
    }
}
```
### Complexity
**Time Complexity:** O(N + E)
**Space Complexity:** O(N)

## Topological Sort (Right to Left)
### Topological Sort

In a right-to-left topological order, you start from the "rightmost" vertex (i.e., a vertex with no outgoing edges) and proceed leftward. This approach can be useful in certain situations and can be thought of as a reverse topological ordering. 

Here's how you can approach it:

### Approach:
* Identify a vertex with no outgoing edges (in-degree = 0). If there are multiple such vertices, you can choose any of them.
* Remove that vertex from the graph along with all its outgoing edges. This removal may affect the in-degrees of other vertices.
* Repeat steps 1 and 2 until all vertices are removed from the graph. The order in which you remove the vertices constitutes the right-to-left topological order.

### Example/Dry-Run:
```java
A -> B -> C
|    |
v    v
D    E
```
To find the right-to-left topological order:

* Start with a vertex with no outgoing edges. In this case, you can start with vertex C.
* Remove vertex C and its outgoing edge. The graph becomes:
```java
A -> B
|    
v    
D    E
```
Now, you can choose either B or E, both of which have no outgoing edges. Let's choose B and remove it:
```java
A
|    
v    
D    E
```
* Continue with the remaining vertices. Choose A next:
```java
|
v    
D    E
```
* Finally, remove D and E:
```java
|
v    
|    |
```
The order in which you removed the vertices is a right-to-left topological order: C, B, A, D, E.

### Pseudocode
```java
function topologicalSortRightToLeft(graph):
    // Function to perform DFS and record nodes in the order they are finished
    function dfs(node):
        mark node as visited
        for each neighbor in graph[node]:
            if neighbor is not visited:
                dfs(neighbor)
        append node to order list

    create an empty order list
    initialize a visited array with False for all nodes

    for each node in the graph:
        if node is not visited:
            dfs(node)

    reverse the order list

    return the reversed order list as the topological order (right-to-left)
```

### Complexity
**Time Complexity:** O(V+E)
**Space Complexity:** O(V)

---


### Question
Which of the following is correct topological order for this graph?

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/881/original/1.png?1706710397" width=300/>

### Choices
- [x] TD,TA,TC,TB
- [ ] TA,TD,TC,TB
- [ ] TC,TA,TD,TB

---
 
to add

---
title: In-Degree of Node
description:
duration: 900
card_type: cue_card
---

## Problem 2 Minimum Jumps to Reach End
### Description:
You are given a 0-indexed array of integers arr of length n. You are initially positioned at arr[0].

Each element arr[i] represents the maximum length of a forward jump from index i. In other words, if you are at arr[i], you can jump to any arr[i + j] where:
* 0 <= j <= arr[i]
* i + j < n

Return the minimum number of jumps to reach arr[n - 1]. The test cases are generated such that you can reach arr[n - 1].

### Example
#### Example 1
**Input**: arr = [2,3,1,1,4]
**Output**: 2
**Explanation**: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

#### Example 2
**Input**: arr = [2,3,0,1,4]
**Output**: 2


### Slower Approach

- Initialize an array to store the minimum number of jumps required to reach each index in the input array.
- Start with the assumption that the minimum number of jumps required to reach the first index is 0.
- Iterate through each index of the array.
- For each index i, iterate through all the indices before i.
- Check if it's possible to reach index i from index j (where j < i) by ensuring the current index is within the reachable range of j.
    - If it's possible to reach index i from index j, update the minimum number of jumps required to reach index i.
- Once all indices are processed, the last element of the jumps array will hold the minimum number of jumps required to reach the end of the array.

### Code
```java

function minJumps(arr[], n) { 
    // jumps[n-1] will hold the result 
    jumps[] = integer array of size n; 

    // if first element is 0, end cannot be reached 
    if (n == 0 || arr[0] == 0) 
        return infinity; 

    jumps[0] = 0; 

    // Find the minimum number of jumps to reach arr[i] 
    // from arr[0], and assign this value to jumps[i] 
    for (i -> 1 to n - 1) { 
        jumps[i] = infinity; 
        for (j -> 0 to i - 1) { 
            if (i <= j + arr[j] && jumps[j] != infinity) { 
                jumps[i] = min(jumps[i], jumps[j] + 1); 
                break; 
            } 
        } 
    } 
    return jumps[n - 1]; 
}

```

### Complexity Analysis
**Time complexity**: O(N$^2$)

**Space complexity**: O(N$^2$)

## Optimised Approach Minimum jumps to reach end 

### Observation
How can we calculate for each index what's the farthest index we can jump to ? And can we do it in O(N) ?

The answer is Yes !!

### Optimized Approach
1. **Preprocess the Array:** 
* We iterate through the array starting from the second element.
* For each element $arr[i]$, we update it to be the maximum value between $arr[i] + i$ and $arr[i - 1]$.
* $arr[i] + i$ represents the farthest index we can reach from index i using the value at $arr[i]$.
* $arr[i - 1]$ represents the farthest index reachable from any of the previous indices.
* This preprocessing step ensures that $arr[i]$ holds the farthest reachable index from the start up to the current index **i**.

2. **Calculate the Minimum Jumps:**
While currentIndex is not at the last index (n - 1), we perform the following:
* Increment the jumps counter as we are making a jump.
* Update currentIndex to the value of $arr[currentIndex]$, which represents the farthest index we can reach from currentIndex.
* This loop continues until we reach or pass the last index of the array.

### Pseudocode
```java
function jump(arr, n) {
    if (n <= 1) return 0;

    for (i -> 1 to n - 1) {
        arr[i] = max(arr[i] + i, arr[i - 1]);
    }

    currentIndex = 0;
    jumps = 0;

    while (currentIndex < n) {
        ++jumps;
        currentIndex = arr[currentIndex];
    }

    return jumps;
}

```

### Complexity Analysis
**Time complexity**: O(N)

**Space complexity**: O(1)


---
## Problem 4 Maximum Profit from Stock Prices

### Problem Statement
Given an array A where the i-th element represents the price of a stock on day i, the objective is to find the maximum profit. We're allowed to complete as many transactions as desired, but engaging in multiple transactions simultaneously is not allowed.

### Approach
Let's start with some key observations:

**Note 1**: It's never beneficial to buy a stock and sell it at a loss. This intuitive insight guides our decision-making process.

**Note 2**: If the stock price on day i is less than the price on day i+1, it's always advantageous to buy on day i and sell on day i+1.

Now, let's delve into the rationale behind Note 2:

**Proof**: If the price on day i+1 is higher than the price on day i, buying on day i and selling on day i+1 ensures a profit. If we didn't sell on day i+1 and waited for day i+2 to sell, the profit would still be the same. Thus, it's optimal to sell whenever there's a price increase.

### DP-Based Solution
Now, let's transition to a dynamic programming solution based on the following recurrence relation:

Let Dp[i] represent the maximum profit you can gain in the region (i, i+1, ..., n).

**Recurrence Relation**: `Dp[i] = max(Dp[i+1], -A[i] + max(A[j] + Dp[j] for j > i))`

Here, Dp[i] considers either continuing with the profit from the next day (Dp[i+1]) or selling on day i and adding the profit from subsequent days.

#### Base Cases

When i is the last day (i == n-1), Dp[i] = 0 since there are no more future days.
When i is not the last day, Dp[i] needs to be computed using the recurrence relation.

#### Direction of Computation

We start computing Dp[i] from the last day and move towards the first day.

#### Code
```cpp
function max_profit(list A) {
    n = A.size;
    declare dp array of size n filled with 0;

    for (i -> n - 2 down to 0) {
        dp[i] = dp[i + 1];

        for (j -> i + 1 to n - 1) {
            if (j + 1 < n) {
                dp[i] = max(dp[i], -A[i] + A[j] +  dp[j + 1]);
            } else {
                dp[i] = max(dp[i], -A[i] + A[j]);
            }
        }
    }

    return dp[0];
}
```


### Optimized Code
The provided code snippet in C++ contains this observation-based solution. It iterates through the array, checks for price increases, and accumulates the profits accordingly.
```cpp
function maxProfit(list A) {
    total = 0, sz = A.size;
    
    for (i -> 0 to sz - 2) {
        if (A[i + 1] > A[i]) 
            total += A[i + 1] - A[i];
    }
    return total;
}
```

**Time Complexity** : O(|A|)
**Space Complexity** : O(1)


---
