# DSA: Graphs 2: BFS & Matrix Questions



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
   |           |
   +-----------+
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
function bfs(startNode) {
    declare visited array of size MAX_NODES with all values initially false); // Initialize all nodes as unvisited
    
    declare queue<integer> q;

    q.push(startNode); // Enqueue the start node
    visited[startNode] = true; // Mark the start node as visited

    while (!q.empty()) {
        currentNode = q.front();
        q.pop();

        // Process the current node (e.g., print or perform an operation)

        for (each neighbor in graph[currentNode]) {
            if (not visited[neighbor]) {
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


### Question

Consider a graph with the following adjacency matrix:

```
[0, 1, 1, 0]
[1, 0, 0, 0]
[1, 0, 0, 1]
[0, 0, 1, 0]
```

What is the order in which the nodes will be visited when performing a breadth-first search (BFS) starting from node 0?

### Choices
- [x] 0, 1, 2, 3
- [ ] 0, 1, 3, 2
- [ ] 0, 2, 3, 1
- [ ] 0, 1, 3, 1

### Explanation

The correct answer is (a) 0, 1, 2, 3.

The given adjacency matrix is for the below graph.

---

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/074/455/original/graph.png?1716283696" width=200/>



BFS (Breadth-First Search) explores neighbor nodes first before moving to the next level. Starting from node 0, BFS visits its neighbors 1 and 2. It then moves to the next level and visits 1's neighbor 3. Finally, it moves to the next level but finds no more unvisited nodes. Therefore, the order of BFS traversal is 0, 1, 2, 3.

## Multisource BFS

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

## Rotten Oranges

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
dx[] = {-1, 1, 0, 0};
dy[] = {0, 0, -1, 1};

function orangesRotting(grid[][]) {
    rowCount = grid.length;
    colCount = grid[0].length;
    declare Queue of integer array named queue;
    
    freshOranges = 0;
    minutes = 0;

    // Count fresh oranges and add rotten oranges to the queue
    for (i -> 0 to rowCount - 1) {
        for (j -> 0 to colCount - 1) {
            if (grid[i][j] == 2) {
                queue.push({i, j, minutes});
            } else if (grid[i][j] == 1) {
                freshOranges++;
            }
        }
    }
    if (freshOranges == 0) {
        // If there are no fresh oranges initially, they are already rotten.
        return 0;
    }

    while (not queue.isEmpty()) {
        cell = queue.pop();
        x = cell[0];
        y = cell[1];
        minutes = cell[2];

        for (i -> 0 to 3 ) {
            newX = x + dx[i];
            newY = y + dy[i];

            if (isValid(grid, newX, newY) and grid[newX][newY] == 1) {
                grid[newX][newY] = 2;
                freshOranges--;
                queue.push({newX, newY, minutes + 1});
            }
        }
    }

    return (freshOranges == 0) ? minutes : -1;
}
function isValid(grid[][], x, y) {
    rowCount = grid.length;
    colCount = grid[0].length;
    return x >= 0 and x < rowCount and y >= 0 and y < colCount;
}        
```  

---

##  Problem 2 Number of Islands
### Problem Statement

You are given a 2D grid of '1's (land) and '0's (water). Your task is to determine the number of islands in the grid. An island is formed by connecting adjacent (horizontally or vertically) land cells. Diagonal connections are not considered.

Given here if the cell values has 1 then there is land and 0 if it is water,  and you may assume all four edges of the grid are all surrounded by water.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/523/original/upload_a58eb3b65d084e2319c537762414bba7.jpeg?1697742306" width=400/>

In this case we can see that our answer is 5. 

**Que: Do we need adjacency list ?**
Ans: No, since the information is already present in form of matrix which can be utilised as it is. 

### Approach:

**Set a Counter:** Start with a counter at zero for tracking island count.

**Scan the Grid:** Go through each cell in the grid.

**Search for Islands:** When you find a land cell ('1'), use either BFS or DFS to explore all connected land cells.

**Mark Visited Cells:** Change each visited '1' to '0' during the search to avoid recounting.

**Count Each Island:** Increase the counter by 1 for every complete search that identifies a new island.

**Finish the Search:** Continue until all grid cells are checked.

**Result:** The counter will indicate the total number of islands.


## Number of Islands Dry Run and Pseudocode

### Dry-Run:
```java
[
 ['1', '1', '0', '0', '0'],
 ['1', '1', '0', '0', '0'],
 ['0', '0', '0', '0', '0'],
 ['0', '0', '0', '1', '1']
]
```

* Initialize variable islands = 0.
* Start iterating through the grid:
* At grid[0][0], we find '1'. Increment islands to 1 and call visitIsland(grid, 0, 0).
* visitIsland will mark all connected land cells as '0', and we explore the neighboring cells recursively. After this, the grid becomes:


```cpp-
[ 
 ['0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0'],
 ['0', '0', '1', '0', '0'],
 ['0', '0', '0', '1', '1']
]
```
* Continue iterating through the grid:
* At grid[2][2], we find '1'. Increment islands to 2 and call visitIsland(grid, 2, 2).
* visitIsland will mark connected land cells as '0', and we explore the neighboring cells recursively. After this, the grid becomes:
```java
[ 
 ['0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0'],
 ['0', '0', '0', '1', '1']
]
```
* Continue the iteration.
* At grid[3][3], we find '1'. Increment islands to 3 and call visitIsland(grid, 3, 3).

We can visit only 4 coordinates, considering them to be i, j; it means we can visit **(i,j-1), (i-1, j), (i, j+1), (i+1, j)**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/792/original/Screenshot_2024-01-30_at_9.58.09_PM.png?1706632097" width=500 />

### Pseudocode

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/796/original/Screenshot_2024-01-30_at_10.04.29_PM.png?1706632480" width=400 />

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/794/original/Screenshot_2024-01-30_at_10.03.04_PM.png?1706632395" width=400 />

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/793/original/Screenshot_2024-01-30_at_10.02.10_PM.png?1706632342" width=400 />

## Take the next question if time permits, or just explain the problem statement to students.

---
## Problem 3 Shortest Distance in a maze

### Problem Statement:
Given an n x n binary matrix grid, return the length of the shortest clear path from the top-left corner (0, 0) to the bottom-right corner (n - 1, n - 1). A clear path is defined as one where:

- All cells visited on the path are 0.
- The path is connected in 8 directions (adjacent cells share an edge or a corner).
If there is no clear path, return -1.

**Example 1**:
Input: grid = [[0, 1], [1, 0]]
Output: 2
**Explanation**:
The path is from the top-left corner to the bottom-right corner. The minimum path length is 2 (cells (0,0) -> (1,1)).

**Example 2**:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
**Explanation**:
The shortest path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2).
The minimum path length is 4.

**Example 3**:
Input: grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
Output: -1
**Explanation**:
Since the top-left corner contains a 1, there is no clear path, so the output is -1.


### Breadth-First Search (BFS) Approach:

The problem is a shortest path search on a grid, where all moves have equal weight. This makes it ideal for a Breadth-First Search (BFS), which explores the shortest path in unweighted graphs.
BFS explores level by level, guaranteeing that when we reach the destination, the number of steps is minimal.

**8-Directional Movement**:

- We are allowed to move in 8 directions (up, down, left, right, and diagonally). Hence, from each cell (x, y), we can move to any of its 8 neighboring cells.
- The valid neighbors are those within the bounds of the grid and whose values are 0 (i.e., walkable).

**Early Termination**:

- If the start cell (0, 0) or the end cell (n-1, n-1) is blocked (i.e., contains 1), return -1 immediately, as no path is possible.
Optimized Solution Using BFS
Approach:

**BFS Initialization**:

- Start BFS from the top-left corner (0, 0), and add it to the queue.
- Maintain a visited set or mark cells as visited in the grid itself to avoid revisiting the same cell.

**BFS Process**:

- For each cell (x, y) dequeued, check its 8 possible neighboring cells.
If a neighboring cell is walkable (i.e., 0), mark it as visited, add it to the queue, and increment the path length.
If you reach the bottom-right corner, return the path length.

**Edge Cases**:

- If the start or end is blocked (i.e., contains a 1), return -1.
If the grid has only one cell, check whether it’s walkable (0).

### Optimized Solution Pseudocode:

``` cpp 
function shortestPathBinaryMatrix(grid):
    n = length of grid
    
    # Edge case: If the start or end cell is blocked, return -1
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    # Directions for 8 possible moves (horizontal, vertical, and diagonal)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    # BFS initialization
    queue = [(0, 0, 1)]  # (row, col, path_length)
    grid[0][0] = 1  # Mark as visited

    while queue is not empty:
        (x, y, path_length) = dequeue

        # If we reached the bottom-right corner, return the path length
        if x == n - 1 and y == n - 1:
            return path_length

        # Explore all 8 neighbors
        for direction in directions:
            newX, newY = x + direction[0], y + direction[1]
            
            if 0 <= newX < n and 0 <= newY < n and grid[newX][newY] == 0:
                queue.append((newX, newY, path_length + 1))
                grid[newX][newY] = 1  # Mark as visited

    # If no path found, return -1
    return -1
                
```
**Explanation**:
**Base Case Check**:

- If the starting cell (0, 0) or the ending cell (n-1, n-1) is blocked (i.e., contains a 1), return -1 immediately because no path is possible.

**BFS Queue**:
- Initialize a queue with the starting cell (0, 0) and the initial path length of 1. Each item in the queue is a tuple (x, y, path_length), where x and y represent the cell coordinates, and path_length represents the length of the path from the start to this cell.
- 
**8-Directional Movement**:
- From each cell (x, y), attempt to move to all 8 possible neighboring cells. If a neighbor is within bounds and walkable (0), mark it as visited (set its value to 1), and add it to the queue with an incremented path length.
- 
**Termination**:

- If we reach the destination cell (n-1, n-1), return the current path length.
If the queue is empty and the destination was not reached, return -1 to indicate that no path exists.

### Complexity Analysis**:
**Time Complexity**: O(n^2)
**Space Complexity**: O(n^2)

---
