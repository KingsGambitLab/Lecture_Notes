# DSA: Graphs 2: BFS, Matrix Questions & Topological Sort

---
title: BFS
description:
duration: 900
card_type: cue_card
---

### BFS
Breadth-First Search (BFS) is another graph traversal algorithm used to explore and navigate graphs or trees. It starts at a source node and explores all its neighbors at the current depth level before moving on to the next level. BFS uses a queue data structure to maintain the order of nodes to be visited.

### Approach:
* We use a queue to maintain the order of nodes to visit in a breadth-first manner.
* We start with a vector visited to keep track of whether each node has been visited. Initially, all nodes are marked as unvisited (false).
* We enqueue the startNode into the queue and mark it as visited.
* We enter a loop that continues until the queue is empty.
* In each iteration, we dequeue the front element (the current node) from the queue and process it. Processing can include printing the node or performing any other desired operation.
* We then iterate through the neighbors of the current node. For each neighbor that hasn't been visited, we enqueue it into the queue and mark it as visited.
* The BFS traversal continues until the queue is empty, visiting nodes level by level.


### Example/Dry-Run
```javascript
   A --- B --- C
   |         |
   +---------+
       |
       D
```
Suppose in this if we want to perform BFS then:

* Start from the source node (City A).
* Explore neighboring nodes level by level.
* Use a queue to maintain the order.
* Mark visited nodes (using adjaency list) to avoid repetition.
* Stop when the target node (City D) is reached.
* This guarantees the shortest path in unweighted graphs.


### Pseudocode:
```javascript
void bfs(int startNode) {
    vector<bool> visited(MAX_NODES, false); // Initialize all nodes as unvisited
    queue<int> q;

    q.push(startNode); // Enqueue the start node
    visited[startNode] = true; // Mark the start node as visited

    while (!q.empty()) {
        int currentNode = q.front();
        q.pop();

        // Process the current node (e.g., print or perform an operation)

        for (int neighbor : graph[currentNode]) {
            if (!visited[neighbor]) {
                q.push(neighbor); // Enqueue unvisited neighbors
                visited[neighbor] = true; // Mark neighbor as visited
            }
        }
    }
```

### Compexity
**Time Complexity:** O(V + E)
**Space Complexity:** O(V)


---
title: Quiz 1
description: 
duration: 30
card_type: quiz_card
---

# Question

Consider a graph with the following adjacency matrix:

```
[0, 1, 1, 0]
[1, 0, 0, 0]
[1, 0, 0, 1]
[0, 0, 1, 0]
```

What is the order in which the nodes will be visited when performing a breadth-first search (BFS) starting from node 0?

# Choices
- [x] 0, 1, 2, 3
- [ ] 0, 1, 3, 2
- [ ] 0, 2, 3, 1
- [ ] 0, 1, 3, 1

---
title: Quiz Explanation
description: 
duration: 30
card_type: cue_card
---
The correct answer is (a) 0, 1, 2, 3.

BFS (Breadth-First Search) explores neighbor nodes first before moving to the next level. Starting from node 0, BFS visits its neighbors 1 and 2. It then moves to the next level and visits 1's neighbor 3. Finally, it moves to the next level but finds no more unvisited nodes. Therefore, the order of BFS traversal is 0, 1, 2, 3.

---
title: Multisource BFS
description:
duration: 2000
card_type: cue_card
---

#### Problem
There are N number of nodes and multisource(S1,S2,S3), we need to find the length of shortest path for given destination node to any one of the source node{S1,S2,S3}.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/088/original/upload_5bc332d89630700685c6151288b14228.png?1696918618" width=500 />


#### Solution
Length = 2
In the beginning, we need to push all source node at once and apply exact BFS,then return the distance of destination node.
#### Time and Space Complexity
* **TC -** O(N+E)
* **SC -** O(N+E)

---
title: Rotten Oranges
description:
duration: 2000
card_type: cue_card
---

#### Problem
There is given a matrix and there are 3 values where 0 means empty cell, 1 means fresh orange present and 2 means rotten orange prsent, we need to find the time when all oranges will become rotten.
**Note:** If not possible, return - 1.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/090/original/upload_3461de9fe730f97814a45fd8d8c6eb74.png?1696918669" width=300 />



#### Solution

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/091/original/upload_d8bb39bbd8d744419836f41e3bd6c606.png?1696918713" width=500 />



**Answer:** after 3 minutes all oranges will get rotten.
* Initially, We need to insert all rotten oranges in Queue (where each element in queue is in a pair), 
* Then check if any fresh oranges has become rotten and if they did, return the time otherwise return -1.

#### Pseudocode
```java
public class RottingOranges {
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    public int orangesRotting(int[][] grid) {
        int rowCount = grid.length;
        int colCount = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int freshOranges = 0;
        int minutes = 0;

        // Count fresh oranges and add rotten oranges to the queue
        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < colCount; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j, minutes});
                } else if (grid[i][j] == 1) {
                    freshOranges++;
                }
            }
        }
        if (freshOranges == 0) {
            // If there are no fresh oranges initially, they are already rotten.
            return 0;
        }

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int x = cell[0];
            int y = cell[1];
            minutes = cell[2];

            for (int i = 0; i < 4; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];

                if (isValid(grid, newX, newY) && grid[newX][newY] == 1) {
                    grid[newX][newY] = 2;
                    freshOranges--;
                    queue.offer(new int[]{newX, newY, minutes + 1});
                }
            }
        }

        return (freshOranges == 0) ? minutes : -1;
    }
    private boolean isValid(int[][] grid, int x, int y) {
        int rowCount = grid.length;
        int colCount = grid[0].length;
        return x >= 0 && x < rowCount && y >= 0 && y < colCount;
    }
    
        
```  

---
title: Flipkart's Delivery Optimization
description:
duration: 2000
card_type: cue_card
---

## Problem : 
**Flipkart** Grocery has several warehouses spread across the country and in order to minimize the delivery cost, whenever an order is placed we try to deliver the order from the nearest warehouse. 

Therefore, each Warehouse is responsible for a certain number of localities which are closest to it for deliveries, this **minimizes the overall cost for deliveries**, effectively managing the distribution workload and minimizing the overall delivery expenses.

### Problem statement:- 
You are given a 2D matrix **A** of size **NxM** representing the map, where each cell is marked with either a **0 or a 1**. Here, a **0** denotes a locality, and a **1** signifies a warehouse. The objective is to calculate a new **2D matrix** of the same dimensions as **A**.

In this new matrix, the value of each cell will represent the minimum distance to the nearest warehouse. For the purpose of distance calculation, you are allowed to move to any of the **eight adjacent cells** directly surrounding a given cell.

### Example TC :- 
**Map =** 
0 0 0 0 1 0 0 1 0
0 0 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 

**Answer** 
2 2 2 1 0 1 1 0 1
1 1 1 1 1 1 1 1 1 
1 0 1 2 2 2 2 2 2
1 1 1 2 3 3 2 1 1
2 2 2 2 3 3 2 1 0

**NOTE:** This is same rotten oranges.

---
title: Possibility of finishing the courses
description:
duration: 900
card_type: cue_card
---

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

---
title: Possibility of finishing courses approach
description:
duration: 900
card_type: cue_card
---

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

---
title: Topological Sort
description:
duration: 900
card_type: cue_card
---

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
for(i = 0; i < n; i++)	
    in_degree[i] = 0;

for(i = 0; i < n; i++)
{
    for(neighbour : adj[i])
    {
        in_degree[i] += 1;
    }
}
```
### Complexity
**Time Complexity:** O(N + E)
**Space Complexity:** 0(N)

---
title: Topological Sort (Right to Left)
description:
duration: 900
card_type: cue_card
---

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
title: Quiz 2
description:
duration: 90
card_type: quiz_card
---

# Question
Which of the following is correct topological order for this graph?

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/881/original/1.png?1706710397" width=300/>

# Choices
- [x] TD,TA,TC,TB
- [ ] TA,TD,TC,TB
- [ ] TC,TA,TD,TB

---
title: Why BFS leads to shortest path
description: 
duration: 900
card_type: cue_card
---

### Question

Find the minimum number of edges to reach v starting from u in undirected simple graph.

**Graph:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/132/original/upload_25a85963d2c4d1d4dc148c24f6295ddd.png?1696922220)" width=550 />


### Approach

Imagine you're playing a game where you have to find the quickest way from point A (vertex u) to point B (vertex v) in a giant maze. This is similar to using Breadth-First Search (BFS) in a graph.

**Think of BFS as your strategy for exploring the maze:**

**Start at Point A:** You're at the entrance of the maze (vertex u), ready to find the shortest path to the treasure (vertex v).

**Explore Closest Paths First:** Just like deciding which paths to take in the maze, BFS first checks all the paths that are one step away from your current position, then moves to paths two steps away, and so on.

**Layer by Layer:** It's like a ripple effect in a pond. You throw a stone (start at vertex u), and the ripples (paths) expand outward, reaching further away points one layer at a time.

**Reaching Point B:** As you follow this method, the moment you step on point B (vertex v) in the maze, you know you've found the shortest route. In BFS, when you first reach vertex v, it guarantees the minimum steps taken, just like finding the quickest path out of the maze.

So, by using BFS in our maze game (or graph), we ensure we're taking the most efficient route possible, avoiding any long detours or dead-ends. It's a smart and systematic way to reach our goal with the least amount of hassle!
