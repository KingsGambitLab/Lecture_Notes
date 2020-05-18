## Prim's Algorithm

Like Kruskal's algorithm, Prim's algorithm is another algorithm to find the minimum spanning tree for the given undirected weighted graph.

Prim's algorithm is also a greedy algorithm, which is quite similar to Dijkstra's algorithm. If you are familar with Dijkstra's algorithm then you know that, we need to find a minimum distance vertex at each step, however in Prim's algorithm we need to find a minimum weight edge. Let's see the actual algorithm.

**Notes:** 
- Here the term **tree** stands for an intermediate tree in the formation of the whole MST.
- **Explored edges** means the edges which are already found in the run of the algorithm.
- Here, we are assuming that the given undireted graph is connected.

## Algorithm

 1. Select an arbitrary vertex say $V$ from the graph and start the algorithm from that vertex.
 2. Add vertex $V$ in the tree.
 3. Explore all the edges connected to vertex $V$.
 4. Find the minimum weight edge from all the explored edges, which connects the tree to a vertex $U$ which is not yet added in the tree.
 5. Set $V$ to $U$ and continue from step 2 until all $|V|$ vertices are in the tree.

**Visualization**
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/1.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/2.jpg)
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/3.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/4.jpg)
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/5.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/6.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/7.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/8.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/9.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/10.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/11.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/12.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Prim's%20Algo/13.jpg)

We will discuss two different approaches:
 1. Adjacency List representation of graph
 2. Adjacency Matrix representation of graph

Generally, we use Adjacency Matrix representation in case of Dense graph because it uses lesser space than the list representation, whereas we use Adjacency List representation in the case of sparse graph.

**Note:** **Minimum weight** represents the weight of a minimum weight edge observed so far in the algorithm, which is connected to a particular vertex.

## Sparse Graphs - Adjacency list representation

Here we are representing the graph using Adjacency list representation.

**Implementation Algorithm**

 1. Initialize a boolean array which keeps track of, whether a vertex is added in the tree.
 2. Initialize an array of integers say $\text{Minweight[]}$, where each entry of it shows the minimum weight, by $\infty$.
 3. Start from any vertex say $A$. Mark the weight of the minimum weight edge to reach it as $0$.
 4. Explore all of the edges connected with $A$ and update the minimum weights to reach the adjacent vertices, if the below condition is satisfied,
For an edge $A\to B$,
$\text{Minweight}[B] < \text{EdgeWeight}(A,B)$
	Note that we are only looking for those adjacent vertices which are not already in the tree.
 5. Find the minimum weight edge from all the explored edges and repeat from step $4$. Say that edge is $a - b$, then take $V$ as $b$ and repeat from step $4$.
 6. If all the $|V|$ vertices are added in the tree, then stop the algorithm.

Can you tell, how we will do the step 5, which is to find the minimum weight edge from all the exlpored edges?

Here, we need to use some data structure which finds out the minimum weight edge from all the explored edges efficiently.

Do you know any of them?

We can use anyone of priority queue, fibonacci heap, binomial heap, balanced binary tree, etc.

**Note:** Below in the code, the parent array is used to retrieve the formed MST and **set** (STL container) is a kind of balanced binary search tree.


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
	
	vector<int> minWeight(no_vertices+1, MAX_Weight),
				parent(no_vertices+1);
	
	// Minimum finding(logN) DS
	set<pair<int,int>> Explored_edges;
	
	Explored_edges.insert({0,1});
	
	for(int i=2;i<no_vertices+1;i++)
		Explored_edges.insert({MAX_Weight,i});
	
	int VertinMST = 0, MSTcost = 0;
	
	minWeight[1] = 0;
	parent[1] = -1;
	
	while(VertinMST < no_vertices)
	{		
		// Vertex connected by Minimum weight edge
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
				// Previous larger weighted edge
				Explored_edges.erase({minWeight[i.first],i.first});
				
				minWeight[i.first] = i.second;
				parent[i.first] = vertex;
				
				// New smaller weighted edge
				Explored_edges.insert({minWeight[i.first],i.first});
			}
		}
		
	}
	
	cout << MSTcost << endl;
	
	cout << "Edges in MST:" << endl;
	for(int i = 1; i <= no_vertices; i++)
	{
		if(parent[i] != -1)
		cout << parent[i] << " " << i << endl;
	}
	
	return 0;
}
```

**Time Complexity**

 1. We need $\mathcal{O}(log|V|)$ time to find the minimum weight edge.
 2. We are doing the above step $\mathcal{O}(|E|+|V|)$ times, which is similar to BFS.

	Overall time complexity: $\mathcal{O}((|E|+|V|)log|V|)$

## Dense Graphs - Adjacency matrix representation

Here, to loop over the adjacent vertices, we have to loop over all |V| entries of the adjacency matrix.

So, basically to update minimum weights we have to spend $O(|V|)$ time. And also to find the minimum weight edge we have to spend $O(|V|)$ time.

The implementation is much simpler than the previous one.

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
	
	vector<int> minWeight(no_vertices + 1, MAX_Weight),
				parent(no_vertices + 1);
				
	minWeight[1] = 0;
	parent[1] = -1;
	
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
			{
				minWeight[j] = graph[minvertex][j];
				parent[j] = minvertex;
			}
		
	}
	
	cout << MSTcost << endl;
	
	cout << "Edges in MST:" << endl;
	for(int i = 1; i <= no_vertices; i++)
	{
		if(parent[i] != -1)
		cout << parent[i] << " " << i << endl;
	}	
	
	return 0;
}

```
### Time Complexity

 1. It takes $\mathcal{O}(|V|)$ time to find the minimum weight edge and also to update the minimum weights.
 2. The outer loop runs $|V|$ times.

	Overall time complexity: $\mathcal{O}(|V|^2)$

### Other algorithms to find MST

 1. Kruskal's Algorithm
 2. Boruvka's Algorithm

 
