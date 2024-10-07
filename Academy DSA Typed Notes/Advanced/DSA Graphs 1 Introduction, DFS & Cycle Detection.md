# Graphs 1: Introduction, DFS & Cycle Detection

## Graphs Introduction

### Introduction

**Graph**: It is a collection of nodes and edges.

Some real life examples of Graph -
1. Network of computers
2. A Website
3. Google Maps
4. Social Media

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/778/original/Screenshot_2024-01-30_at_6.59.51_PM.png?1706621403" width="400" />

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/779/original/Screenshot_2024-01-30_at_6.58.46_PM.png?1706621438" width="400" />

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/780/original/Screenshot_2024-01-30_at_6.56.17_PM.png?1706621456" width="400" />


## Types of Graph

### Cyclic Graph

A cyclic graph contains at least one cycle, which is a closed path that returns to the same vertex.
Diagram:
```javascript
A -- B
|    |
|    |
D -- C
```

### Acyclic Graph
An acyclic graph has no cycles, meaning there are no closed paths in the graph.
Diagram:
```javascript
A -- B
|    |
D    C
```

### Directed Graph (Digraph)
In a directed graph, edges have a direction, indicating one-way relationships between vertices.
Diagram:
```javascript
A --> B
|     |
v     v
D --> C
```

### Undirected Graph
In an undirected graph, edges have no direction, representing symmetric relationships between vertices.
Diagram:
```javascript
A -- B
|    |
|    |
D -- C
```

### Connected Graph
A connected graph has a path between every pair of vertices, ensuring no isolated vertices.
Diagram
```javascript
A -- B
|     
D -- C
```

### Disconnected Graph
A disconnected graph has at least two disconnected components, meaning there is no path between them.
Diagram:
```javascript
A -- B    C -- D
|              |
E -- F    G -- H
```

### Weighted Graph
In a weighted graph, edges have associated weights or costs, often used to represent distances, costs, or other metrics.
Diagram (Undirected with Weights):
```javascript
A -2- B
|     |
1     3
|     |
D -4- C
```

### Unweighted Graph
An unweighted graph has no associated weights on its edges.
Diagram (Undirected Unweighted):
```javascript
A -- B
|     
D -- C
```

### Degree of a Vertex
The degree of a vertex is the number of edges incident to it.
Diagram:
```javascript
   B
   |
A--C--D
```

### Outdegree of a Vertex
The outdegree of a vertex in a directed graph is the number of edges leaving that vertex.
Diagram:
```javascript
A --> B
|     |
v     v
D --> C
```

### Simple Graph
A simple graph has no self-loops or multiple edges between the same pair of vertices.
Diagram:
```javascript
A -- B
|     
D -- C
```

## How to store a graph

### Graph:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/759/original/Screenshot_2024-01-30_at_3.01.38_PM.png?1706607105" width=400/>

### Adjacency Matrix:
All the edges in above graph has equal weights.
In adjacency matrix, `mat[i][j] = 1`, if there is an edge between them else it will be 0. 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/760/original/Screenshot_2024-01-30_at_3.02.55_PM.png?1706607186" width=400/>



#### Pseudocode:

```cpp
declare N, M 
declare 2D matrix with all values 0 -> mat[N+1][M+1] 

for(i -> 0 to A.size - 1) {
    u = A[i][0];
    v = A[i][1];
    
    mat[u][v] = 1
    mat[v][u] = 1
}
```

Note: In case of weighted graph, we store weights in the matrix.

**Advantage:** Easy to update new edges.

**Disadvantage:** Space wastage because of also leaving space for non-exitent edges.
Moreover,
If N<=10^5, it won't be possible to create matrix of size 10^10.
It is possible only if N <= 10^3


**Space Complexity:** O(N^2^)

### 2. Adjacency List:

An adjacency list is a common way to represent a graph in computer science. It's used to describe which nodes (or vertices) in the graph are connected to each other. Here's how it works:

#### Graph:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/759/original/Screenshot_2024-01-30_at_3.01.38_PM.png?1706607105" width=400/>

#### Adjacency List:

Stores the list of nodes connected corresponding to every node.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/761/original/Screenshot_2024-01-30_at_3.08.41_PM.png?1706607566" width=200/>

We can create map of <int, list> or an array of lists
```
map<integer, list<integer>> graph;

OR

list<integer> graph[]
```

#### Pseudocode:
```javascript
list<integer> graph[N+1]
for(i -> 0 to A.size - 1) {
    u = A[i][0]
    v = A[i][1]
    
    graph[u].add(v)
    graph[v].add(u)
}
```

* We refer the adjacent nodes as **neighbours**.

---


### Question

Consider a graph contains V vertices and E edges.  What is the **Space Complexity** of adjacency list?

### Choices

- [ ] O(V^2)
- [ ] O(E^2)
- [x] O(V + E)
- [ ] O(V*E)

### Explanation


Space is defined by the edges we store. An Edge e comprise of two nodes, a & b. For a, we store b and for b, we store a. Hence, 2 * E.

Now, we are doing this for every node, hence +V.

Space Complexity: O(V+E)


---
### Graph traversal algorithm - DFS

There are two traversal algorithms - DFS (Depth First Search) and BFS(Breadth First Search).

In this session, we shall learn DFS and in next, BFS.

### DFS
Depth-First Search (DFS) is a graph traversal algorithm used to explore all the vertices and edges of a graph systematically. It dives deep into a graph as far as possible before backtracking, hence the name "Depth-First." Here's a basic explanation of the DFS process with an example:

### Process of DFS:
1. **Start at a Vertex:** Choose a starting vertex (Any).
2. **Visit and Mark:** Visit the starting vertex and mark it as visited.
3. **Explore Unvisited Neighbors:** From the current vertex, choose an unvisited adjacent vertex, visit, and mark it.
4. **Recursion:** Repeat step 3 recursively for each adjacent vertex.
5. **Backtrack:** If no unvisited adjacent vertices are found, backtrack to the previous vertex and repeat.
6. **Complete When All Visited:** The process ends when all vertices reachable from the starting vertex have been visited.



### Example/Dry-run:

Consider a graph with vertices A, B, C, D, E connected as follows:

```
A ------ B
|        |
|        |
|        |
C        D
\
 \
  \
   \
    E
```

**DFS Traversal:**

* Start at A: Visit A.
* Visit Unvisited Neighbors of A:
    * Go to B (unvisited neighbor of A).
    * Visit B.
* Visit Unvisited Neighbors of B:
    * Go to D (unvisited neighbor of B).
    * Visit D.
* Backtrack to B: Since no more unvisited neighbors of D.
* Backtrack to A: Since no more unvisited neighbors of B.
* Visit Unvisited Neighbors of A:
    * Go to C (unvisited neighbor of A).
    * Visit C.
* Visit Unvisited Neighbors of C:
    * Go to E (unvisited neighbor of C).
    * Visit E.
* End of DFS: All vertices reachable from A have been visited.

**DFS Order:**
The order of traversal would be: **A → B → D → C → E**.
    

### Pseudocode:

We'll take a visited array to mark the visited nodes.

```javascript
// Depth-First Search function
maxN = 10^5 + 1
list<integer> graph[maxN];
visited[maxN];

function dfs( currentNode) {
    // Mark the current node as visited
    visited[currentNode] = true;

    // Iterate through the neighbors of the current node
    for (i -> 0 to graph[currentNode].size - 1) {
        neighbor = graph[u][i];
        // If the neighbor is not visited, recursively visit it
        
        if (not visited[neighbor]) {
            dfs(neighbor);
        }
    }
}
```


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/784/original/IMG_1C2FED3C35EF-1.jpeg?1706628598" width="500" />

---


### Question
Time Complexity for DFS?

### Choices
- [x] O(V + E) 
- [ ] O(V)
- [ ] O(2E)



### Explanation:

The time complexity of the DFS algorithm is O(V + E), where V is the number of vertices (nodes) in the graph, and E is the number of edges. This is because, in the worst case, the algorithm visits each vertex once and each edge once.

**Space Complexity:** O(V)


---
## Problem 1 Detecting Cycles in a Directed Graph

### Problem Statement
Check if given graph has a cycle?

### Examples

1)
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/787/original/Screenshot_2024-01-30_at_9.16.41_PM.png?1706629671" width="250"/>

2) 
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/786/original/Screenshot_2024-01-30_at_9.17.06_PM.png?1706629663" width="300"/>




**Counter Example:** It is not true, because we can come to a visited node via some other path
For eg, in Example 2, start at 0 -> 1 -> 3, now we can't go anywhere, backtrack to 1->2, then via 2 we'll find 3 which is already visited but there's no cycle in the graph.


### Approach

Apply DFS, if a node in current path is encountered again, it means cycle is present!
With this, we will have to keep track of the path.

Example 1:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/786/original/Screenshot_2024-01-30_at_9.17.06_PM.png?1706629663" width="300"/>

>Say we start at 0 -> 1 -> 3
path[] = {0, 1, 3}
Now, while coming back from 3, we can remove the 3 from path array.
path[] = {0, 1}
Now, 0 -> 1 -> 2 -> 3
path[] = {0, 1, 2, 3} ***[Here, we came back to 3, but via different path, which is not an issue for us]***

Example 2:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/787/original/Screenshot_2024-01-30_at_9.16.41_PM.png?1706629671" width="250"/>

> Say we start at 0 -> 1 -> 2 -> 3 
path[] = {0, 1, 2, 3}
Now, from 3, we come back to 1. 
path[] = {0, 1, 2, 3, 1} ***[But 1 is already a part of that path, which means cycle is present]***

### Pseudocode

```javascript
list<integer> graph[] //filled
visited[] = {0}
path[N] = {0}

function dfs( u) {
    visited[u] = true
    path[u] = 1
    
    for(i -> 0 to graph[u].size - 1) {
        v = graph[u][i]
        if(path[v] == 1) return true
        else if(not visited[v] and dfs(v)) {
            return true
        }
    }
    path[u]=0;
    return false;
}
```

### Complexity
**Time Complexity:** O(V + E)
**Space Complexity:** O(V)

---
