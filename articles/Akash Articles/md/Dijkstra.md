<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>


## Dijkstra's Algorithm

Have you ever used Google Maps?

Ever wondered how it works? How does it tell you the shortest path from point A to B? 

At the backside of it, they are using something known as "Shortest Path Finding algorithm". Well, what does the shortest path actually mean?

The **dark** line represents the shortest path from the home to the office, in the diagram below
![Example for shortest path](https://lh3.googleusercontent.com/GaOV_vdJ-V1G3t27g7bHQzeSbBwdl38bjsTp5xdxgFvrfTU5PAB92FDY7y7zzuPA1rT86N9eaQV6)

Do you know how to represent the roads between different places? This is **Weighted Directed Graph** - a directed graph with edges having weights.

## Quiz Time:

Now can you find the shortest path from the source vertex to the target vertex in the image below?

![Quiz](https://lh3.googleusercontent.com/M4ye9O11B0X1C6qp-Ox-m87G0TJpIn_qOmzi8lEwnV_AYPYoDLK3lG528zElEgEVIMADutFRvbEl "Quiz")

Answer: The dark line shows the answer.

![Answer to the quiz problem](https://lh3.googleusercontent.com/nopAw8ZspVs0cI4YPuu4duBbdRRgoaju3mSSCNb_tVuc9jPSyHsflWQOKhpbLt164llxGQ0rZVEh "Answer to the quiz problem")

-- --
Single Source Shortest Path problem (SSSP)
-----------------------------
**Statement**: Given a graph find out the shortest path from a given point to all other points.

### How to solve this problem?
When we talk about the graph we have two standard techniques to traverse: DFS and BFS.

Can you solve this problem using these standard algorithms? 

Certainly. We will see how to find the shortest path from the source to the destination using DFS.

Let's look at how can we solve it using DFS.


### Solution using DFS:                                                                                                              

**Algorithm:**  DFS approach is very simple.

 - Start from the source vertex
 - Explore all the vertices adjacent to the source vertex
 - For each adjacent vertex, If it satisfies the relaxation condition then update the new distance and parent vertex
 - Then recurse on it, by considering itself as the new source.

**Relaxation** means if you reach the vertex with less distance than encountered before, then update the data. **Parent vertex** means the vertex by which the particular vertex is reached.

This way DFS will explore all the possible paths from the source vertex to the destination vertex and will find out the shortest path.

Here in the code, we will represent the graph using adjacency list representation:

```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000

// Function to print the required path 
void printpath(vector<int>& parent, int vertex, int source, int destination) 
{ 
	if(vertex == source)
	{
		cout << source << "-->";
		return;
	}
    printpath(parent, parent[vertex], source, destination);
    cout << vertex << (vertex==destination ? "\n" : "-->");
}

void DFS(int source, int destination, vector<vector<pair<int,int> > > &graph, vector<int> &distances, vector<int> &parent)
{
	// When we reach at the destination just return
	if(source == destination)
		return;
	
	// Do DFS over all the vertices connected
	// with the source vertex
	for(auto vertex: graph[source])
	{
		// Relaxation of edge:
		// If the distance is less than what we 
		// have encountered uptil now then update
		// Distance and Parent vertex
		if(distances[vertex.second] > distances[source] + vertex.first)
		{
			distances[vertex.second] = distances[source] + vertex.first;
			parent[vertex.second] = source;
		}
		
		// Do DFS over all the vertices connected 
		// with the source vertex
		DFS(vertex.second, destination, graph, distances, parent);
	}
}

int main()
{
	// Number of vertices in graph
	int n = 6;
	
	// Adjacency list representation of the 
	// Directed Graph
	vector<vector<pair<int, int> > > graph; 
  
    graph.assign(n + 1, vector<pair<int, int> >()); 

	// Now make the Directed Graph
	// Note that edges are
	// in the form (weight, vertex ID)
	graph[1].push_back( make_pair(1, 2) );
	graph[1].push_back( make_pair(6, 2) );
	graph[2].push_back( make_pair(1, 4) );
	graph[4].push_back( make_pair(1, 3) );
	graph[3].push_back( make_pair(1, 5) );
	graph[2].push_back( make_pair(7, 5) );
	graph[4].push_back( make_pair(3, 6) );
	
	// Array to store the distances
	vector<int> distances(n+1, MAX_DIST);
	
	// Array to store the parent vertices
	vector<int> parent(n+1, -1);
	
	int source = 1, destination = 5;
	
	distances[source] = 0;
	
	// Do DFS
	DFS(source, destination, graph, distances, parent);
	
	int shortest_distance = distances[destination];
	
	// To print shortest_distance
	cout << shortest_distance << endl;
	
	// To print the path of the shortest_distance
	printpath(parent, destination, source, destination);
	
	return 0;
}
```

### Time Complexity of DFS
As DFS explores all possible paths from the given source vertex to the destination vertex, this may lead to exponential time complexity in a very dense graph.

So, our DFS approach is not efficient. What next?

We have a very interesting and elegant algorithm to solve the problem named " **Dijkstra's Algorithm**".  This is the algorithm whose variants are used by most of the path finding applications.

## Dijkstra's Algorithm: 

Dijkstra's Algorithm solves SSSP.

Dijkstra's Algorithm is an iterative algorithm similar to **BFS**, but here we have a little twist.

**Algorithm:** 

 1. Mark the distance between the source and all other vertices to $\infty$ and assign all the parent vertices to some sentinel (not used value). 
 2. The set is a collection of vertices which is empty at the start of the algorithm.
 3. Set the distance between source to source as 0 and add the source vertex to the set.
 4. Find the minimum distance vertex from the set and erase it from the set. Mark it as processed. let this vertex be $A$.
 5. Explore all the edges connected to $A$.
 6. If the edge is connected to the unprocessed vertex and it satisfies the relaxation condition below, then relax that edge and insert the vertex into the set.
**Relaxation Condition:**  Let the edge be $A-u$,
$$\text{Distance}[u] < \text{Distance}[A] + \text{EdgeWeight}(A,u)$$
 4. If the set is empty, then stop the algorithm.
 5. Otherwise, repeat from step 3.
 
In Dijkstra's Algorithm, we explore the vertices in the way BFS does, however here we have to find the minimum distance vertex from the set.

Which data structure can help us find the minimum distance vertex from the set?

**Priority Queue** is the data structure which achieves this goal in an efficient manner $\mathcal{O}(\log n)$. 

**Visualization:** 

 - Here cloud represents the processed nodes - the nodes whose final shortest distance is found.
 - Solid lines represent the edges that are discovered. 
 - Numbers in square brackets represent the current distance of that vertex from the source vertex.


 1. Start from the source vertex 1. ![enter image description here](https://lh3.googleusercontent.com/FjtCUJsZLrgfR91fhg9SnWq6mZ6huoVoP32ps_Z6V1N1saPJNb_BBCIRB_IlilwuPIK87WPul3u7)
 2. Vertex 1 discovers vertices 2 and 3. It consequently does the relaxation and adds vertices 2 and 3 in the set.
![enter image description here](https://lh3.googleusercontent.com/2jJ_CHiOTouAQxCrgpeJ6qK25_ZZuFgh-kI1B19Fsl0NoB9m3rtmtupPUJv4ttC2YSg3X-LD5nnq)
 3. The minimum distance vertex in the set is vertex 2. So vertex 2 will be the next source vertex.

	It will discover vertices 5 and 4. 

	Now vertex 2 is added to the cloud as it is processed.
![enter image description here](https://lh3.googleusercontent.com/Gjkc7w3DJKA0k9McJPpSk1HOG9nENp15oWoqcQoreTxS1VGCBdgUP2qdzDDE5KFSHc90p6rNDeI6)
 4. The next minimum distance vertex is vertex 4.
	 It relaxes both 3 and 6. Then vertex 4 will be added to the cloud.
![enter image description here](https://lh3.googleusercontent.com/M_6-KvDeY2V3dkJGfwPKwSDqe6crTNIc9S3N-2e6Zel8pTGTnMQEKp4T4O6pSAj3Ss2aNLxYSMkK)
 5. Next vertex will be 3. It relaxes 5.
![enter image description here](https://lh3.googleusercontent.com/rQFxj-uiNigNUNA19aiMtd9eqv1hbIzTtv80UFgB3ij7iJchfZnWiFLuxRDM1AQ4uQMHM8ZOWaP7)
 6. Now there will not be any more relaxations.
	 All the vertices in the priority queue will dequeue without adding any new vertex to the set.
![enter image description here](https://lh3.googleusercontent.com/Hnf3MyVP3V6jAck4trl8mWltMwfMRiP7u0NLYgtX99aQ7T5r4MzNFR3_IyHDjQi4K95kI5FC0ZO-)

Now we have found the shortest distances to all the vertices from the given source vertex. 

We can use parent array to store parent of the given vertex, and then we can find out the shortest path for any vertex. 

```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000

// Function to print the required path 
void printpath(vector<int>& parent, int vertex, int source, int destination) 
{ 
	if(vertex == source)
	{
		cout << source << "-->";
		return;
	}
    printpath(parent, parent[vertex], source, destination);
    
   	cout << vertex << (vertex==destination ? "\n" : "-->");
}


// Dijkstra's Algorithm
int Dijkstra_Algo(vector<vector<pair<int, int> > >& Graph, 
                int src, int target, vector<int> & distances, vector<int> & parent)
{ 
	
	// Minimum Priority Queue to keep track of the discovered
	// vertex which has the minimum distance
	priority_queue<pair<int, int>, vector<pair<int, int> >, 
                   greater<pair<int, int> > > container; 
                   
    // To check whether vertex is in the cloud
    vector<bool> processed(Graph.size());
  
	// Start with source vertex
	// Push the source vertex in the
	// Priority Queue
   	container.push(make_pair(0, src)); 
	
	// Assign distance to source as 0
    distances[src] = 0; 
  
	
    while (!container.empty()) { 
       	
       	// Pop the least distance vertex from the Priority Queue
       	pair<int, int> temp = container.top(); 
        int current_src = temp.second; 
  
		// Pop the minimum distance vertex
        container.pop(); 
        	
        processed[current_src] = true;
		// current source vertex
        for (auto vertex : Graph[current_src]) {
  
			// Distance of the vertex from its 
			// temporary source vertex
			int distance = distances[current_src] + vertex.first;

			// Relaxation of edge
			if (!processed[vertex.second] && distance < distances[vertex.second]) { 

				// Updating the distance
				distances[vertex.second] = distance; 

				// Updating the parent vertex
				parent[vertex.second] = current_src; 
				
				// Adding the relaxed edge in the prority queue 
				container.push(make_pair(distance, vertex.second)); 
			}
       	}
    }
  
	// return the shortest distance
    return distances[target]; 
} 
int main()
{
	// Number of vertices in graph
	int n = 6;
	
	// Adjacency list representation of the 
	// Directed Graph
	vector<vector<pair<int, int> > > graph;  
  
	graph.assign(n + 1, vector<pair<int, int> >()); 

	// Now make the Directed Graph
	// Note that edges are
	// in the form (weight, vertex ID)
	graph[1].push_back( make_pair(1, 2) );
	graph[1].push_back( make_pair(6, 2) );
	graph[2].push_back( make_pair(1, 4) );
	graph[4].push_back( make_pair(1, 3) );
	graph[3].push_back( make_pair(1, 5) );
	graph[2].push_back( make_pair(7, 5) );
	graph[4].push_back( make_pair(3, 6) );
	
	// Array to store the distances
	vector<int> distances(n+1, MAX_DIST);
	
	// Array to store the parent vertices
	vector<int> parent(n+1, -1);
	
	// For example destination is taken as 5
	int source = 1, destination = 5;
	
	distances[source] = 0;
	
	// Dijkstra's algorithm
	int shortest_distance = Dijkstra_Algo(graph, source, destination, distances, parent);
	
	// To print shortest_distance
	cout << shortest_distance << endl;
	
	// To print the path of the shortest_distance
	printpath(parent, destination, source, destination);
	
	return 0;

}
```

## Time Complexity of Dijkstra's Algorithm:

 1. $\mathcal{O}(|E|)$ time to make the Weighted Directed Graph.
 2. $\mathcal{O}(|E| + |V|)$ can be taken by the while loop which is similar to BFS time complexity.
 3. $\mathcal{O}(\log |V|)$ time to insert the relaxed vertex in the priority queue.

So the overall complexity of the Dijkstra's Algorithm will be 
$$\mathcal{O}((|E| + |V|) \times \log(|V|))$$

Here $|E|$ represents the number of edges in the graph and $|V|$  represents the number of vertices in the graph.


## Limitation of Dijkstra's Algorithm:

When there are negative weight edges in the graph, then Dijkstra's algorithm does not work.

Example: 
![Negative Edge Problem in Dijkstra](https://picasaweb.google.com/110514411166133524120/6771365618877108449#6771365621395377650 "negative_edges")

It will find the path from $a$ to $c$ incorrectly.

What if there is a negative cycle in the graph?

**Negative Cycle:** Cycle in which sum of the weights of the edges is negative.

When there is any negative cycle in the graph then Dijkstra's algorithm will run forever, because then we can reach the affected vertices in negative infinite cost.

Note that the graph, we have used, is connected. If you have a vertex which is not connected, then you cannot find the shortest distance to it!

## **Applications of Dijkstra's algorithm:**


 1. One very famous variant is the "Widest Path Finding Algorithm", which is an algorithm to finding a path between two vertices of the graph **maximizing the weight of the minimum-weight edge in the path**. 

     In the practical application, this problem can be seen as a graph with routers as its vertices and edges representing bandwidth between two vertices. Now if we want to find the maximum bandwidth path between two places in the internet connection, then this algorithm is useful which is highly based on Dijkstra's Algorithm.

 2.  A widely used application of the shortest path algorithm is in network routing protocols "Routing protocol".

## Other Shortest Path Finding Algorithms:

 1 Bellman-Ford Algorithm
 2. Using Dynamic Programming
 3. All Pair Shortest Path Algorithm - **Floyd-Warshall Algorithm**, which finds the shortest path between every pair of vertices.

