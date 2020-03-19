Problem Statement
--

Recently, Riya won the scholarship to attend the Linux Open Source Conference in Paris. She was very excited to be a part of it. On the day of the conference, she got late and now she wants to quickly know what's the shortest path she needs to follow in order to reach the conference venue as early as possible. She used google maps and luckily reached the venue on time. She was quite impressed by this app and wanted to build something like that herself but she wasn't sure how to find the shortes path from a source to destination in the most efficient way possible.
Let's help Riya in finding this. 


Brute Force Solution
--
Ideally, the brute force solution to find the shortest path from a source node to the destination node can be to explore all possible paths and choose the one with the least node. But that will lead to exponential time complexity.


Dijkstra Algorithm
--

Specifically, given a graph G with non-negative weights, one can easily construct a new unweighted graph H (with the same vertices in G and some additional ones), by replacing each weighted edge with the number of edges equivalent to its weight. 
So, for example, if you have an edge (u,v) with weight 10 in G, we can replace this edge by a series of 10 edges between u and v (with new intermediate vertices ofcourse) in H. Now, the distances between the vertices that were originally from G is still preserved, and we've essentially converted the weighted graph into an unweighted graph that we can run BFS on.

 At this point, one  might realize that we don't really care about the distances to these new intermediate vertices, and you'd only want to enqueue/visit the vertices that were originally from G, which gets us to the idea of a priority queue.

So basically, we want to find the shortest path in between a source node and all other nodes (or a destination node), but we don’t want to have to check EVERY single possible source-to-destination combination to do this, because that would take a really long time for a large graph, and we would be checking a lot of paths which we should know aren’t correct! So we decide to take a _greedy_ approach!

Here when Dijkstra Algorithm come to our rescue!

**Dijkstra’s algorithm** is an **algorithm** that maps the shortest path between two nodes on a graph.

The best example to depict the application of Dijkstra’s algorithm is *Google Maps*. It gives you number of ways from one destination to the other. But, it primarily focuses on the shortest path between the 2 places.
 
**_Dijkstra’s algorithm_** can be used to determine the shortest path from one node in a graph to _every other node_ within the same graph data structure, provided that the nodes are reachable from the starting node.!


**NOT SURE TO INCLUDE IT OR NOT**
*Dijkstra’s algorithm follows somehow the principle of Dynamic Programming as well. Consider the shortest path from s to some vertex w. It traverses a sequence of vertices, with a final vertex v that then connects to w to finish the shortest path to w. The key observation is that the path up to v must be a shortest path to v. Because if it weren't, we could replace that path to v with a shorter path, which would also shorten the path to w, which would contradict the claim that we have a shortest path to w. Dijkstra's algorithm was that it is basically an efficient version of breadth-first search on a different graph.*


Algorithm
--
Let's take a quick look at the steps and rules for running Dijkstra Algorithm.


-   We have a weighted graph  `G`  with a set of vertices (nodes)  `V`  and a set of edges  `E`
-   We also have a starting node called  `s`, and we set the distance between  `s`  and  `s`  to 0
-   Mark the distance between  `s`  and every other node as infinite, i.e. start the algorithm as if no node was reachable from node  `s`
-   Mark all nodes (other than  `s`) as unvisited, or mark  `s`  as visited if all other nodes are already marked as unvisited (which is the approach we'll use)
-   As long as there is an unvisited node, do the following:
    -   Find the node  `n`  that has the shortest distance from the starting node  `s`
    -   Mark  `n`  as visited
    -   For every edge between  `n`  and  `m`, where  `m`  is unvisited:
        -   If  `smallestPath(s,n)`  +  `smallestPath(n,m)`  <  `smallestPath(s,m)`, update the cheapest path between  `s`  and  `m`  to equal  `smallestPath(s,n)`  +  `smallestPath(n,m)`
        - 
These instructions are our golden rules that we will always follow, until our algorithm is done running. So, let’s get to it!

This might seem complicated but let's go through an **example** that makes this a bit more intuitive:: 

![IMG_0033](https://user-images.githubusercontent.com/35702912/69817977-ca91e080-1221-11ea-9e42-08635dfbfd33.jpg)
Consider the weighted and undirected graph above. 
We're looking for the shortest path from node `a` to node `e`. 


![IMG_0036](https://user-images.githubusercontent.com/35702912/69823217-41cd7180-122e-11ea-8012-5bc761ad28be.jpg)

We'll be using a table to better represent the algorithm and understand what is going on. 
- In the beginning, we'll determine the edge weights of `a` from its adjacent nodes. The rest of the distances are denoted as positive infinity, i.e. they are not reachable from any of the nodes we've processed so far. 
- The next step is to find the closest node that hasn't been visited yet that we can actually reach from one of the nodes we've processed. In our case, this is node `c`  [shortest distance] and we'll mark node `a` as visited. 
- We see that from node `c` we can reach nodes `b` and `d`.
	- node `b` -> to get from `c` to `b` costs 1 units, given that the shortest path from `a` to `c` costs 3 units, 3 + 1 is less than 7 (the shortest path between `a` and `b`). This means we have  found a better path from `a` to `b` through the node `c`, so we update that cell in the table.
	- node `d` -> to get from `c` to `d` costs 2 units, and since `d` was previously unreachable, 3 + 2 is definitely better than infinity so we update that particular cell in the table.

- We  now have choose between node `b` and node `d`, since node `b` has shortest distance between the both of them, we choose node `b`. 
- Unvisited, reachable nodes from node `b` are nodes `d` and `e`:
	- node `d` -> it costs 2 units to get from node `b` to node `d`, and 4 + 2 isn't better than the previous 5 unit value we found, so there's no need to update.
	- node `e` -> to get from `b` to `e` costs 6 units, and since `e` was previously unreachable, 4 + 6 is definitely better than infinity so we update that particular cell in the table.
	- Mark node `b` as visited.

- The next node to be considered is node `d`. 
- Unvisited, reachable nodes from node `d` is node `e`:	
	- node `e` ->  to get from `d` to `e` costs 4 units, given that the shortest path from `a` to `d` costs 5 units, 5 + 4 is less than 10. This means we have  found a better path from `a` to `e` through the node `d`, so we update that cell in the table.


- Since the next closest, reachable, unvisited node is our end node - the algorithm is over and we have our result - the value of the shortest path between `a` and `e` is 9.

Pseudocode
--

```
def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn't exist'

        # 1. Mark all nodes unvisited and store them.
        # 2. Set the distance to zero for our initial node 
        # and to infinity for other nodes.
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            # 3. Select the unvisited node with the smallest distance, 
            # it's current node now.
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])

            # 6. Stop, if the smallest distance 
            # among the unvisited nodes is infinity.
            if distances[current_vertex] == inf:
                break

            # 4. Find unvisited neighbors for the current node 
            # and calculate their distances through the current node.
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost

                # Compare the newly calculated distance to the assigned 
                # and save the smaller one.
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

            # 5. Mark the current node as visited 
            # and remove it from the unvisited set.
            vertices.remove(current_vertex)


        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path
```

Time Complexity
--

Now let's calculate the running time of Dijkstra's algorithm using a min-heap priority queue. 

- It takes O(|V|) time to construct the initial priority queue of |V| vertices . 
- Each of the subsequent priority queue operations takes time O(log q) where q is the current size of the queue.
- Each vertex u is deleted from the queue exactly once, after it has obtained its least cost path from the source vertex. 
- After u is deleted from the queue, each neighbor v of vertex u is tested to see if the path from the source to v through u has a lower cost than the current path from the source to v. 
- If a lower cost path is obtained through u, then the path cost for v is decreased, and the vertex priority changed in the queue. 
- So, the test for improving a path is performed a total of O(|E|) times with a worst-case time of O(log |V|) to update the vertex priority for each test. 

Consequently, the algorithm runs in time **O(|E| log |V|)**.


Problems with Dijkstra
--
DjkstraDijkstra algorithm does not work with graphs having negative weight edges.  The graph shown below is a good example to understand this. 


![IMG_0032](https://user-images.githubusercontent.com/35702912/69810118-2ef87400-1211-11ea-94f4-67421d7827d4.jpg)

Dijkstra follows a simple rule that if all edges have non negative weights, adding an edge will never make the path smaller. That's why it follows the greedy strategy and picks up the shortest path to find the optimal solution. 

If we ran the algorithm, looking for the least expensive path between **a** and **c**, the algorithm would return 0 even though that's not correct (the least expensive cost is -200).
Let's start with the node **a**.
- The path from **a** to **a** (a -> a) will be marked 0 and everything else will be marked infinity. 
- In the next turn
		- **a** -> **b** will be 1.
		- **a** -> **d** will be 99.
		- **a** -> **c** will be 0.

Note that,  there will be no changes if you expand vertices **b** and **c**.
When you expand **d**,  the path from **a** to **b** will be changed to -201. 
Notice that  **a** -> **c** is still 0, when there is a shorter path  **a** -> **d** -> **b** -> **c** costing -200. 

But, Dijsktra will not be able to find out this and will subsequently fails in this case.
