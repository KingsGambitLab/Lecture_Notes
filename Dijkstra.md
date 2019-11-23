Problem Statement
--




Dijkstra Algorithm
--

**Dijkstra’s algorithm**  is an  **algorithm**  that maps the shortest path between two nodes on a graph.

The best example to depict the application of Dijkstra’s algorithm is *Google Maps*. It gives you number of ways from one destination to the other. But, it primarily focuses on the shortest path between the 2 places.

**_Dijkstra’s algorithm_** can be used to determine the shortest path from one node in a graph to _every other node_ within the same graph data structure, provided that the nodes are reachable from the starting node.!

Intuition
--
We want to find the shortest path in between a source node and all other nodes (or a destination node), but we don’t want to have to check EVERY single possible source-to-destination combination to do this, because that would take a really long time for a large graph, and we would be checking a lot of paths which we should know aren’t correct! So we decide to take a _greedy_ approach!

*more to be added*

Algorithm
--
Here are some of the steps that are involved:

1.  Set the distance to the source to 0 and the distance to the remaining vertices to infinity.
2.  Set the  **current**  vertex to the source.
3.  Flag the  **current**  vertex as visited.
4.  For all vertices adjacent to the  **current**  vertex, set the distance from the source to the  **adjacent**  vertex equal to the minimum of its present distance and the  **sum**  of the  **weight of the edge**  from the current vertex to the adjacent vertex and the distance from the source to the  **current**  vertex.
5.  From the set of  **unvisited vertices**, arbitrarily set one as the new  **current**  vertex, provided that there exists an edge to it such that it is the minimum of all edges from a vertex in the set of  **visited vertices**  to a vertex in the set of  **unvisited vertices**. To reiterate: The new current vertex must be unvisited and have a minimum weight edges from a visited vertex to it. This can be done trivially by looping through all visited vertices and all adjacent unvisited vertices to those visited vertices, keeping the vertex with the minimum weight edge connecting it.
6.  Repeat steps 3-5 until all vertices are flagged as visited. 

Dry Run
--



Pseudocode
--
```
function Dijkstra(Graph, source):
       dist[source]  := 0                     // Distance from source to source is set to 0
       for each vertex v in Graph:            // Initializations
           if v ≠ source
               dist[v]  := infinity           // Unknown distance function from source to each node set to infinity
           add v to Q                         // All nodes initially in Q

      while Q is not empty:                  // The main loop
          v := vertex in Q with min dist[v]  // In the first run-through, this vertex is the source node
          remove v from Q 

          for each neighbor u of v:           // where neighbor u has not yet been removed from Q.
              alt := dist[v] + length(v, u)
              if alt < dist[u]:               // A shorter path to u has been found
                  dist[u]  := alt            // Update distance of u 

      return dist[]
  end function
```

Time Complexity
--
The bottleneck of Dijkstra's algorithm is finding the next closest, unvisited node/vertex. Using  *LinkedList*  this has a complexity of  _O(numberOfEdges)_, since in the worst case scenario we need to go through all the edges of the node to find the one with the smallest weight.

To make this better, we can use Java's heap data structure -  *PriorityQueue*. Using a  *PriorityQueue*  guarantees us that the next closest, unvisited node (if there is one) will be the first element of the  *PriorityQueue*. So  now finding the next closest node is done in constant (_O(1)_) time, however, keeping the  *PriorityQueue*  sorted (removing used edges and adding new ones) takes  _O(log(numberOfEdges))_  time. This is still much better than  _O(numberOfEdges)_.

Further, we have  _O(numberOfNodes)_  iterations and therefore as many deletions from the  *PriorityQueue* (that take  _O(log(numberOfEdges))_  time), and adding all of our edges also takes  _O(log(numberOfEdges))_  time. This gives us a total of  _O((numberOfEdges + numberOfNodes) * log(numberOfEdges))_  complexity when using  *PriorityQueue*.



Correctness of Dijkstra Algorithm
--

