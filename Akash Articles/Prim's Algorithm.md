## Prim's Algorithm

Like Kruskal's algorithm, Prim's algorithm is an another algorithm to find the minimum spanning tree for the given undirected weighted graph.

Prim's algorithm is also a greedy algorithm, which is quite similar to Dijkstra's algorithm. In Dijkstra's algorithm, we find the minimum distance vertex at each step, however in Prim's algorithm we find minimum weighted edge.

At each step of the algorithm we add the least cost edge to the tree.

**Algorithm**

 1. Select an arbitrary vertex say $V$ from the graph and start the algorithm from that vertex.
 2. Add vertex $V$ in the tree.
 3. Explore all the edges connected to vertex $V$.
 4. Find the minimum weighted edge from all the explored edges, which connects the tree to a vertex $U$ which is not yet added in the tree.
 5. Set $V$ to $U$ and continue step 3 until all $|V|$ vertices are in the tree.

**Note:** Here **tree** is an intermediate tree in the formation of the whole MST.

**Visualization**


We will discuss different approaches:

 1. Adjacency List representation of graph
 2. Adjacency Matrix representation of graph

Generally, we use Adjacency Matrix representation in case of Dense graph because it uses lesser space than the list representation, whereas we use Adjacency List representation in case of sparse graph.


### Sparse Graphs - Adjacency list representation

Here we need to use some data structure which finds us the minimum weighted edge from the explored edges. Do you know any of them?

We can use priority queue, red-black trees, fibonacci heaps, binomial heap, etc. These are the data structures which can do this operation efficiently.

```c++
#include <bits/stdc++.h>
#define MAX_Weight 1000000000
using namespace std;

int main() 
{
	int no_vertices = 4;
	
	vector<vector<pair<int,int>> > graph(no_vertices+1, vector<pair<int,int>>());
	
	graph[1].push_back({2,6});	// A-B
	graph[2].push_back({1,6});
	graph[1].push_back({4,5});	// A-D
	graph[4].push_back({1,5});
	graph[2].push_back({3,3});	// B-C
	graph[3].push_back({2,3});
	graph[2].push_back({4,4});	// B-D
	graph[4].push_back({2,4});
	graph[3].push_back({4,2});	// C-D
	graph[4].push_back({3,2});
	
	// To track if the vertex is added in MST
	vector<bool> inMST(no_vertices+1);
	
	vector<int> minWeight(no_vertices+1, MAX_Weight);
	
	// Minimum finding(logN) DS
	set<pair<int,int>> Explored_edges;
	
	Explored_edges.insert({0,1});
	
	for(int i=2;i<no_vertices+1;i++)
		Explored_edges.insert({MAX_Weight,i});
	
	int VertinMST = 0, MSTcost = 0;
	
	minWeight[1] = 0;
	
	while(VertinMST < no_vertices)
	{
		if(Explored_edges.empty())
		{
			cout << "There is no MST" << endl;
			break;
		}
		
		// vertex connected by Minimum weighted edge
		int vertex = Explored_edges.begin()->second;
		
		MSTcost += minWeight[vertex];
		
		inMST[vertex] = true;
		VertinMST++;
		
		Explored_edges.erase(Explored_edges.begin());
		
		// Exploring the adjacent edges
		for(auto i:graph[vertex])
		{
			// If we reach by lesser weighted edge then update
			if(!inMST[i.first] && minWeight[i.first] > i.second)
			{
				// Previous more weighted edge
				Explored_edges.erase({minWeight[i.first],i.first});
				
				minWeight[i.first] = i.second;
				
				// New min. weighted edge
				Explored_edges.insert({minWeight[i.first],i.first});
			}
		}
		
	}
	
	cout << MSTcost << endl;
	
	return 0;
}
```

**Time Complexity**

 1. We need $\mathcal{O}(log|V|)$ time to find minimum weighted edge and we are doing this step $\mathcal{O}(|E|)$ times.

	Overall time complexity: $\mathcal{O}(|E|log|V|)$

### Dense Graphs - Adjacency matrix representation

In adjacency matrix representation, we have to traverse all $|V|$ entries to find and update the minimum weights.

The implementation is much simpler then the previous one.

```c++
#include <bits/stdc++.h>
#define MAX_Weight 1000000000
using namespace std;

int main() 
{
	int no_vertices = 4;
	
	int graph[no_vertices+1][no_vertices+1];
	
	graph[1][2]=6;	// A-B
	graph[2][1]=6;
	graph[1][4]=5;	// A-D
	graph[4][1]=5;
	graph[2][3]=3;	// B-C
	graph[3][2]=3;
	graph[2][4]=4;	// B-D
	graph[4][2]=4;
	graph[3][4]=2;	// C-D
	graph[4][3]=2;
	
	// To track if the vertex is added in MST
	vector<bool> inMST(no_vertices + 1);
	
	int VertinMST = 0, MSTcost = 0;
	
	vector<int> minWeight(no_vertices + 1, MAX_Weight);
	minWeight[1] = 0;
	
	for(int i=1; i<=no_vertices; i++)
	{
		int minvertex = 0, weight = MAX_Weight;
		
		// Find the minimum weighted edge
		for(int j=1; j<=no_vertices; j++)
			if(!inMST[j] && (minvertex==0 || minWeight[j] < minWeight[minvertex]))
			{
				minvertex = j;
				weight = minWeight[j];
			}
		
		inMST[minvertex] = true;
		MSTcost += weight;
		
		// Update the min weights
		for(int j=1;j<=no_vertices;j++)
			if(!inMST[j] && graph[minvertex][j] < minWeight[j])
				minWeight[j] = graph[minvertex][j];
		
	}
	
	cout << MSTcost << endl;
	
	return 0;
}
```
**Time Complexity**

 1. It takes $\mathcal{O}(|V|)$ time to find the minimum weighted edge connected vertex.
 2. $\mathcal{O}(|V|)$ time to update the minimum weights.

	Overall time complexity: $\mathcal{O}(|V|^2)$

**Other algorithms to find MST**

 1. Kruskal's Algorithm
 2. Boruvka's Algorithm

 
