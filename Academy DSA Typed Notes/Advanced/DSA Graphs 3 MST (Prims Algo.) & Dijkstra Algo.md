# Graphs 3: MST & Dijkstra



### Agenda of the lecture:

* Challenges in Flipkart's Logistics and Delivery Operations
* Prim's Algorithm
* Djikstra's Algorithm

### Challenges in Flipkarts Logistics and Delivery 

**Scenario:**
Suppose Flipkart has N local distribution centers spread across a large metropolitan city. These centers need to be interconnected for efficient movement of goods. However, building and maintaining roads between these centers is costly. Flipkart's goal is to minimize these costs while ensuring every center is connected and operational.

**Goal:** You are given number of centers and possible connections that can be made with their cost. Find minimum cost of constructing roads between centers such that it is possible to travel from one center to any other via roads.



### Explanation

**Example:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/126/original/upload_b27e5dc6056098a838971ceb1ddf7aab.png?1696921885" width=300 />



**Output:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/127/original/upload_f8296197fcf4b61f3d2531921d4c9a43.png?1696921923" width=500 />


### Idea:

To achieve the lowest cost in our scenario, consider these key points:

1. **Aim for Fewer roads:** Minimizing the number of roads directly leads to reduced costs.

2. **Opt for a Tree Structure:** Why a tree? Well, in the world of data structures, a tree uniquely stands out when it comes to minimal connections. For any given N nodes, a tree is the only structure that connects all nodes with exactly N - 1 edges. This is precisely what we need - the bare minimum of edges to connect all points, ensuring the lowest possible number of roads.


**Another Example:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/846/original/Screenshot_2024-01-31_at_4.11.16_PM.png?1706697687" width=500 />

The end goal is that all centers should be connected.

**Possible Solutions -**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/847/original/Screenshot_2024-01-31_at_4.13.05_PM.png?1706697792" width=300 />

Here first is better because the sum of all edge weights is minimum.

The tree which spans (covers) all the vertices with the minimum number of edges needed to connect them is known as **Spanning Tree**.

### Minimum Spanning Tree

The minimum spanning tree has all the properties of a spanning tree with an added constraint of having the minimum possible weights among all possible spanning trees.

**Uniqueness of MST:** If all edge weights are unique, there's only one MST. If some weights are the same, multiple MSTs can exist.

**Algorithms for MST:** Kruskal's and Prim's algorithms are used to find MSTs. The MST found can vary based on the choices made for edges with equal weights. Both algorithms solve for same problem having same time and space complexities.

*Note: We'll cover Prim's in today's session, Kruskal shall be covered in DSA 4.2*

### Solution to Flipkart's problem

**Application of MST:**
* **Identify All Possible Connections:** First, identify all the possible routes that can connect these N centers. Imagine this as a network where each center is a node, and each possible road between two centers is an edge.

* **Assign Costs:** Assign a cost to each potential road, based on factors like distance, traffic, or construction expenses. In real-life terms, shorter and more straightforward routes would generally cost less.

* **Create the MST:** Now, apply the MST algorithm (like Kruskal's or Prim's). The algorithm will select routes that connect all the centers with the least total cost, without forming any loops or cycles.

* **Outcome:** The result is a network of roads connecting all centers with the shortest total length or the lowest cost.

### Prims Algorithm

Let's consider the below **Graph:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/855/original/Screenshot_2024-01-31_at_4.34.43_PM.png?1706699091" width=350 />

Say we start with **vertex 5**, now we can choose an edge originating out of 5.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/856/original/Screenshot_2024-01-31_at_4.37.30_PM.png?1706699339" width=350 />

*Which one should we choose?*
The one with minimum weight.

We choose 5 ---- 3 with weight 2

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/857/original/Screenshot_2024-01-31_at_4.41.06_PM.png?1706699512" width=350 />

Now, after this, since 5 and 3 are part of the MST, we shall choose a min weighted edge originated from either 3 or 5. That edge should connect to a vertex which hasn't been visited yet. 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/858/original/Screenshot_2024-01-31_at_4.41.23_PM.png?1706699636" width=350 />

We choose 5 ---- 4 with weight 3

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/859/original/Screenshot_2024-01-31_at_4.44.49_PM.png?1706699696" width=350 />

---

### Question
What is the next node, we need to visit ? 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/859/original/Screenshot_2024-01-31_at_4.44.49_PM.png?1706699696" width=350 />


### Choices
- [ ] 3
- [x] 2
- [ ] 1
- [ ] 6




### Explanation:

The next we need to visit is **2**.

We choose 4 ----> 2 with weight 3, This is the smallest weight node among all possible edges of 3, 4, and 5.

---
###  Prims Algorithm Continued

Now, same process follows i.e, we can select a min weighted edge originating from 3, 4, or 5 such that it should connect to a vertex that hasn't been visited yet.


**After completing the entire process, we shall have below MST.**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/860/original/Screenshot_2024-01-31_at_4.47.55_PM.png?1706699884" width=350 />


---


### Question
What is the most suitable data structure for implementing Prim's algorithm?

### Choices
- [ ] Linked List 
- [ ] Array
- [x] Heap
- [ ] Stack


### Explanation:

Prim's algorithm typically uses a Heap (min-heap) to efficiently select the minimum-weight edge at each step of the algorithm. Min Heaps allow for constant time access to the minimum element, making them well-suited for this purpose.

---
## Prims Algorithm Execution


### Execution

Say we have a black box(we'll name it later) 

Now, say we start with 5. From 5, via weight 3 we can visit 4, via weight 5 we can visit 6, via weight 2 we can visit 3.

We'll information as - (weight, vertex)

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/861/original/Screenshot_2024-01-31_at_4.51.52_PM.png?1706700121" width=350 />

From this, we'll get vertex reachable via min weight, which data structure can be helpful ?
**MIN HEAPS**

Now, we remove (2, 3) from heaps and connect 3 to 5.

From 3, the nodes that are reachable will be pushed to the heap.
*We'll insert only those vertices which haven't been visited yet.*

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/862/original/Screenshot_2024-01-31_at_4.56.18_PM.png?1706700386" width=350 />

Select the minimum weighted -> (3, 4)

Now, this shall continue.


### Pseudocode

```java 
while (no heap.isEmpty()) {
    
    p = heap.getMin();

    if (vis[v] == true)
        continue;

    // Add the vertex to the MST and accumulate the weight
    vis[v] = true;
    ans += p.first

    // Now, you can optionally iterate through the adjacent vertices of 'v' and update the heap with new edges
    for ((u, w) in adj[v]) {
        
        if (!vis[u]) {
            // Add the unvisited neighbor edges to the heap
            heap.add({w, u});
        }
    }
}
```

### Complexity
**Time Complexity:** O(E * logE)
**Space Complexity:** O(V + E)

## Dijkstras Algorithm

### Question

There are N cities in a country, you are living in city-1. Find minimum distance to reach every other city from city-1.

We need to return the answer in the form of array

### Example

**Input Graph:**
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/064/422/original/graph.jpg?1707336223" width=500/>

**Output:**

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | 7 | 8 | 12 | 11 | 15 | 13 |


### Result Array

Lets say d is the Resultant Array,

`d[i] says that the minimum distance from the source node to the ith vertex`

### Dry Run
Lets take the above example and Dry Run it.


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/064/422/original/graph.jpg?1707336223" width=500/>

Lets set the starting point as **1**.  So we need to find the Shortest to all the other vertexes from 1.


Initally the distance array, d will be set to ∞.


|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |

We know that, from 1 -> 1 is always 0.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |

Lets add the adjacent vertexes of 1 into the min-heap, which is used to pick the minimum weighted node.

The elements of the min heap is in the form **(weight, vertex)**.

min heap = `[ (7,2) (8, 3) ]`

**(7, 2) Picked**

Pick the minimum weighted one, which is **(7, 2)**. So we can say that, from **1 -> 2**, the minimum path is 7. Updating in the distance array as well.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | 7 | ∞ | ∞ | ∞ | ∞ | ∞ |

Lets add the adjacent vertexes of 2 into the min-heap, by adding the current weight + adjacent weight.
i.e., (cost_to_reachfrom_1_to_2 + cost_to_reachfrom_2_to_3)
(cost_to_reachfrom_1_to_2 + cost_to_reachfrom_2_to_4)

Before adding the adjacent vertex in the min heap, check whether it is good enought to add it.

Here the adjacent elements of 2 is 1, 3, 4.  We notice that, there is no point in visiting 1, by **1 -> 2 -> 1** for the cost of **14**.  Already we know that, 1 can be visited in **0 cost** by checking on the d (distance array).  So in this case, we **dont insert in our min heap**.



Adding the remaining two pairs in the min heap.

min heap = `[ (8, 3) (10, 3) (13, 4)]`


**(8, 3) Picked**
Picking the minimum (8, 3) and updating the distance array.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | 7 | 8 | ∞ | ∞ | ∞ | ∞ |

After adding the adjacent vertexes of 3,

(16, 1) is not inserted, Since there is already a cost exist. 

min heap = `[ (10, 3) (13, 4) (11, 5) (12, 4)]`



---

### Question

The current states are,

Given Graph
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/064/422/original/graph.jpg?1707336223" width=500/>

min heap = `[ (10, 3) (13, 4) (11, 5) (12, 4)]`


|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| distance array (d) | 0 | 7 | 8 | ∞ | ∞ | ∞ | ∞ |

What would be the next step, which is going to take place?

### Choices
- [ ] Pick (10, 3) and Update the distance array at 3rd vertex as 10
- [x] Pick (10, 3) and Dont update the distance array
- [ ] Pick (13, 4) and Update the distance array at 4th vertex as 13
- [ ] Pick (12, 4) and Dont update the distance array




### Explanation:

The current step is to **Pick (10, 3) and Dont update the distance array**.  Since we have noticed that, On the distance array, vertex 3 can be visited at cost 8, which is obviously lesser than 10.  So no need to update the array.

After Picking (10, 3), the further steps are processed.

---
## Dijkstras Algorithm Dry Run continued

**(10, 3) is Picked**

But 3 can be visited by 8 cost already. So, No changes.

min heap = `[ (13, 4) (11, 5) (12, 4)]`

**(11, 5) is Picked**

Updating the distance array

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | 7 | 8 | ∞ | 11 | ∞ | ∞ |

Inserting the adjacent vertexes of 5,

min heap = `[ (13, 4) (12, 4) (13, 4) (16, 6) (13, 7)]`

The pairs, (14, 3) is not inserted, since there is already minimum cost exist in the distance array.

**(12, 4) is Picked**

Updating the distance array
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | 7 | 8 | 12 | 11 | ∞ | ∞ |

Inserting adjacent of 4,

min heap = `[ (13, 4) (13, 4) (16, 6) (13, 7) (17, 6)]`

The other possible pairs are not inserted, since it has the minimum cost already.

**(13, 4) is Picked**

4 is on Already minimum cost

min heap = `[ (13, 4) (16, 6) (13, 7) (17, 6)]`

**(13, 4) is Picked**

4 is on Already minimum cost

min heap = `[ (16, 6) (13, 7) (17, 6)]`

**(13, 7) is Picked**

Updaing the distance array,

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | 7 | 8 | 12 | 11 | ∞ | 13 |


min heap = `[(16, 6) (17, 6) (18, 7) (15, 6)]`

**(15, 6) is Picked**

Updaing the distance array,

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | 7 | 8 | 12 | 11 | 15 | 13 |


min heap = `[(16, 6) (17, 6) (18, 7)]`


**(16, 6) is Picked**

No changes

min heap = `[(17, 6) (18, 7)]`

**(17, 6) is Picked**

No changes

min heap = `[(18, 7)]`

**(18, 6) is Picked**

No changes

min heap = `[]`

Thus the min heap is Emptied. 

The distance array is,

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| d | 0 | 7 | 8 | 12 | 11 | 15 | 13 |



### Pseudo code
```java 
 while (not hp.isEmpty()) {
            rp = hp.pop();  // Extract the minimum element

            d = rp.first;  // Distance
            u = rp.second; // City

            // Skip if this distance is greater than the known distance
            if (d > dist[u]) {
                continue;
            }

            // Explore neighbors of u and update distances
            for (/* Loop through neighbors */) {
                v = /* Neighbor city */;
                w = /* Weight to reach v from u */;

                // Calculate the new distance via u
                new_dist = dist[u] + w;

                // If the new distance is shorter, update dist and add to heap
                if (new_dist < dist[v]) {
                    dist[v] = new_dist;
                    hp.add(Pair(new_dist, v));
                }
            }
        }
    }
```

* The time complexity of the Dijkstra's algorithm implementation with a min-heap of pairs is $O((E + V) * log(V))$, where E is the number of edges, V is the number of vertices (cities), and log(V) represents the complexity of heap operations.
* The space complexity of this implementation is O(V + E), where V is the space used to store the dist array (minimum distances) for all cities, and E is the space used to represent the graph (adjacency list).
                    
### Can Dijkstra's algorithm work on negative wieghts?

Dijkstra's algorithm is not suitable for graphs with negative edge weights as it assumes non-negative weights to guarantee correct results. Negative weights can lead to unexpected behavior and incorrect shortest path calculations.

---


### Question
Is Dijkstra's algorithm is commonly used for finding the Minimum Spanning Tree ? 

### Choices
- [ ] Yes
- [x] No


### Explanation:

Dijkstra's Algorithms is for finding the Single source shortest path algorithm

---
