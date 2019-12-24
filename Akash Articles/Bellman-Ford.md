<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>

## Bellman-Ford Algorithm

Dijkstra's algorithm solves the problem of finding single source shortest paths, but it does not work in the case if there are negative edges or negative cycles in the graph. 

How do we solve the SSSP problem when the given graph has negative weighted edges?

We have a new algorithm named "**Bellman-Ford algorithm**" which achieves this goal.

## Quiz Time
You are given a directed graph, how many edges can be there on the path between any two nodes at maximum?

Answer: $|V|-1$

## Brute Force

DFS finds out the correct shortest path whether the edge weights are positive or negative, because it searches all the possible paths from the source to the destination.
**Note:** If there is a negative cycle, then it is not possible to find the shortest distance to affected vertices.

## Bellman-Ford algorithm

Bellman-Ford algorithm works on the principal that the path between any two vertices can contain at most $|V|$ vertices or $|V|-1$ edges. 

In Bellman-Ford Algorithm, the main step is the relaxation of the edges.
 
 The algorithm relaxes all the outgoing directed edges $|V| - 1$ times.

### Algorithm

 1. Same as Dijkstra's Algorithm, mark all the distances to $\infty$ and assign all the parent vertices to some sentinel value (not used before).
 2. Assign source to source distance as $0$ and start the algorithm.
 3. Loop over all the directed edges.
 4. If the relaxation condition below is satisfied, then relax those edges.
**Relaxation Condition:** For an edge from $A \to B$,
$$\text{Distance}[B] < \text{Distance}[A] + \text{EdgeWeight}[A, B]$$
 5. Repeat the step 3, $|V|-1$ times.

This is a kind of bottom-up **Dynamic Programming**. After the $k$-th iteration of the outer loop the shortest paths having at most $k$ edges are found.

### Visualization



After the first iteration of the outer loop there will not be any more relaxations.

### Code

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

// Object - Edge
struct edge{
	
	// Edge from -> to
	// having some weight
	int from, to, weight;
	
	edge(int a, int b, int w)
	{
		from = a;
		to = b;
		weight = w;
	}
	
};

int main()
{
	
	int no_vertices=5;
	
	// Array of edges
	vector<edge> edges;
	
	// Distance and Parent vertex storing arrays
	vector<int> distance(no_vertices+1, MAX_DIST), parent(no_vertices+1,-1);
	
	// Edges
	edges.push_back(edge(1,2,1));
	edges.push_back(edge(2,3,1));
	edges.push_back(edge(1,3,2));
	edges.push_back(edge(2,4,-10));
	edges.push_back(edge(4,3,4));
	edges.push_back(edge(3,5,1));
	
	// For the shake of example
	int source = 1, destination = 5;
	
	distance[1] = 0;
	
	// Bellman-Ford Algorithm
	for (int i = 0; i < no_vertices - 1; i++)
	{
		// Loop over all the edges
		for(int j = 0; j < edges.size() ; j++)
		{
			if(distance[edges[j].from] != MAX_DIST) {
				
				// Check for the Relaxation Condition
				if(distance[edges[j].to] > distance[edges[j].from] + edges[j].weight )
				{
					distance[edges[j].to] = distance[edges[j].from] + edges[j].weight;
					parent[edges[j].to] = edges[j].from; 
				}
			}
		}
	}
	
	// Shortest distance from source to destination
	cout << distance[5] << endl;
	
	// Shortest path
	printpath(parent, 5, 1, 5);
	
	return 0;
}

```
### Time Complexity

 - $\mathcal{O}(|V| )$ time is taken by outer loop as it runs $|V|-1$ times.
 - $\mathcal{O}(|E|)$ time to loop over all the edges in the inner loop.
 
	 So the total time complexity will be: $\mathcal{O}(| V | \cdot | E |)$

If there is a negative cycle in the graph, then certainly we can not find the shortest paths. But how to detect the negative cycles? 

We can use Bellman-Ford algorithm to detect negative cycles in the graph. How?

## Detection of Negative Cycle

In the algorithm, we are running the outer loop $|V| - 1$times, as there can be at most $|V| - 1$ relaxations on a path between any two vertices.

Now, if there are any more relaxations possible, then there is a negative cycle in the graph. This is how we detect the negative cycle.

So, we will run the outer loop one more time to detect the negative cycle.

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

// Object of Edge
struct edge{
	
	// Edge from -> to
	// having some weight
	int from, to, weight;
	
	edge(int a, int b, int w)
	{
		from = a;
		to = b;
		weight = w;
	}
	
};

// Bellman-Ford Algorithm for Negative Cycle
bool Bellman_Ford_NC(vector<edge> & edges, vector<int> & distance, vector<int> & parent)
{
	int no_vertices = 5;
	
	for (int i = 0; i < no_vertices - 1; i++)
	{
		// Loop over all the edges
		for(int j = 0; j < edges.size() ; j++)
		{
			if(distance[edges[j].from] != MAX_DIST) 
			{				
				// Check for the Relaxation Condition
				if(distance[edges[j].to] > distance[edges[j].from] + edges[j].weight )
				{
					distance[edges[j].to] = distance[edges[j].from] + edges[j].weight;
					parent[edges[j].to] = edges[j].from; 
				}
			}
		}
	}
	
	bool is_negative_cycle = false;
	
	// Running the outer loop one more time
	for(int j = 0; j < edges.size() ; j++)
	{
		// Check for the Relaxation Condition
		if(distance[edges[j].to] > distance[edges[j].from] + edges[j].weight )
		{
			// Used when finding vertices in NC
			distance[edges[j].to] = distance[edges[j].from] + edges[j].weight;
			parent[edges[j].to] = edges[j].from;
			// There is a negative cycle 
			is_negative_cycle = true;
		}
		
	}
	
	if(is_negative_cycle)
	{
		cout << "There is a negative cycle in the graph." << endl;
		return false;
	}
	
	return true;
}
	

int main()
{
	
	int no_vertices=5;
	
	// Array of edges
	vector<edge> edges;
	
	// Distance and Parent vertex storing arrays
	vector<int> distance(no_vertices+1, MAX_DIST), parent(no_vertices+1,-1);
	
	// Edges
	edges.push_back(edge(1,2,1));
	edges.push_back(edge(2,3,5));
	edges.push_back(edge(3,1,2));
	edges.push_back(edge(2,4,-10));
	edges.push_back(edge(4,3,4));
	edges.push_back(edge(3,5,1));
	
	// For the shake of example
	int source = 1, destination = 5;
	
	distance[1] = 0;
	
	if(Bellman_Ford(edges, distance, parent))
	{
		// Shortest distance from source to destination
		cout << distance[5] << endl;
		
		// Shortest path
		printpath(parent, 5, 1, 5);
	}
	
	return 0;
}

```
Is it possible to find the vertices involved in the negative cycle? Yes.

## Finding the Negative Cycle

If there is a unique negative cycle, then we can find out the vertices involved in the cycle using the data of the last relaxation edge and parent vertices.

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

// Function to print the required path 
void printcycle(vector<int>& parent, int vertex, int source, int destination) 
{ 
	if(vertex == source)
	{
		cout << source << "-->";
		return;
	}
    printcycle(parent, parent[vertex], source, destination);
    
    if(vertex == destination)
   		cout << vertex << "-->" << source << endl;
   	else
   		cout << vertex << "-->";
}

// Object - Edge
struct edge{
	
	// Edge from -> to
	// having some weight
	int from, to, weight;
	
	edge(int a, int b, int w)
	{
		from = a;
		to = b;
		weight = w;
	}
	
};

// Bellman-Ford Algorithm
bool Bellman_Ford(vector<edge> & edges, vector<int> & distance, vector<int> & parent)
{
	int no_vertices = 5;
	for (int i = 0; i < no_vertices - 1; i++)
	{
		// Loop over all the edges
		for(int j = 0; j < edges.size() ; j++)
		{
			if(distance[edges[j].from] != MAX_DIST) 
			{
				
				// Check for the Relaxation Condition
				if(distance[edges[j].to] > distance[edges[j].from] + edges[j].weight )
				{
					distance[edges[j].to] = distance[edges[j].from] + edges[j].weight;
					parent[edges[j].to] = edges[j].from; 
				}
			}
		}
	}
	
	bool is_negative_cycle = false;
	
	int last_relaxation = 0;
	
	// Running the outer loop one more time
	for(int j = 0; j < edges.size() ; j++)
	{
		// Check for the Relaxation Condition
		if(distance[edges[j].to] > distance[edges[j].from] + edges[j].weight )
		{
			distance[edges[j].to] = distance[edges[j].from] + edges[j].weight;
			parent[edges[j].to] = edges[j].from;
			last_relaxation = edges[j].to;
			is_negative_cycle = true;
		}
		
	}
	
	if(is_negative_cycle)
	{
		cout << "There is a negative cycle in the graph." << endl;
		return last_relaxation;
	}
	
	return 0;
}
	

int main()
{
	
	int no_vertices=5;
	
	// Array of edges
	vector<edge> edges;
	
	// Distance and Parent vertex storing arrays
	vector<int> distance(no_vertices+1, MAX_DIST), parent(no_vertices+1,-1);
	
	// Edges
	edges.push_back(edge(1,2,1));
	edges.push_back(edge(2,3,5));
	edges.push_back(edge(3,1,2));
	edges.push_back(edge(2,4,-10));
	edges.push_back(edge(4,3,4));
	edges.push_back(edge(3,5,1));
	
	// For the shake of example
	int source = 1, destination = 5;
	
	distance[1] = 0;
	
	int last_relaxation = Bellman_Ford(edges, distance, parent);
	
	if(!last_relaxation)
	{
		// Shortest distance from source to destination
		cout << distance[5] << endl;
		
		// Shortest path
		printpath(parent, 5, 1, 5);
	}
	else
	{
		int trapped = last_relaxation;
		
		// To find the negative_cycle, we can
		// use the last relaxation data
		// and loop back over parent vertices
		// for over no_vertices time, so that 
		// we get trapped in the negative cycle
		for(int i = 0; i < no_vertices; i++)
		{
			trapped = parent[trapped];
		}
		
		// Printing negative_cycle
		printcycle(parent, parent[trapped], trapped, parent[trapped]);
		
	}
	
	return 0;
}
```

## Other Shortest Path finding Algorithms

 1. All pair shortest path algorithm - **Floyd Warshall Algorithm**.
 2. SSSP using Dynamic Programming.
 3. Dijkstra's Algorithm
