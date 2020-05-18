## Kruskal's Algorithm

Suppose, You are running a company with several offices in different cities. Now, you want to connect all the offices by phone lines. Different networking companies are asking for different amount of money to connect different pairs of offices.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/1.jpg)
***Comp** is an abbreviation of Company.

Now, how will you figure out the way with minimum cost?

Well, this problem can be solved by using classical algorithms to find the minimum spanning tree for the given graph.

What is the "**Minimum Spanning Tree**" ? and even before that, what is a "**Spanning Tree**"?

### Spanning Tree (ST)

Spanning Tree for a given undirected graph is a subgraph, which is a tree that includes every vertex of a graph with minimum possible number of edges.

### Quiz Time

$Q.1$ What is the minimum possible number of edges that can connect all the vertices of the undirected graph having $|V|$ vertices?

Answer: $|V|-1$

$Q.2$ Find one ST for the following graph.![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/2.jpg)
**Answer:** Dark lines represents the spanning tree which is not unique.
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/3.jpg)

### Minimum Spanning Tree (MST)
Minimum Spanning Tree is the Spanning Tree with minimum cost. 

Here the cost has different meanings for different kinds of problem. For example, In the above stated problem, cost is the money asked by different companies.

### Quiz Time
Find the MST for the given graph.
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/4.jpg)

**Answer:** 
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/5.jpg)


**Note**: Here we are talking about an undirected graph because directed graph may or may not have ST. See the image below:

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/6.jpg)

For a directed graph to have a ST, there must be a vertex (say "$root$") from which we can reach to every other vetex by directed paths.

How can you find a MST for an undirected graph?

## Brute Force

One basic idea is to find all the paths which are using exactly $|V| - 1$ edges and including all $|V|$ vertices - find all ST of a graph. 

Take the minimum cost path(ST) which will be the MST for a given graph.

This process can lead to exponential time complexity, because in order to find all possible paths we have to spend exponential time in a very dense graph.

We have an elegant algorithm to solve MST finding problem very efficiently.

**Terminologies and notes:**

1. **Connected component** is a subgraph of a graph, which has a path between every pair of vertices in it. And each of the path uses no additional vertices outside of this subgraph.
2. At the start of the algorithm, each vertex is representing different component on their own.
3. Unifying two connected components results into one connected component, having all the vertices of both components.

## Kruskal's Algorithm

Kruskal's Algorithm is a **greedy algorithm**, which chooses the least weighted edge from the remaining edges at each step of the algorithm, to find the overall minimum weighted spanning tree.

### Algorithm

 1. Sort the array of the edges, by the weights of the edges.
 2. Now, loop over this sorted array. 

	If the edge is connecting two vertices which are not already in the same connected component, then add that edge in the list of MST edges. And also unify both of the components.

 3. When all $|V|$ vertices are added in the tree, then stop the algorithm. Now this tree represents MST for a given graph.

At the end of the algorithm there will be only one connected component, which includes each vertex of the graph.

**Visualization**
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/7.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/8.jpg)
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/9.jpg)

![same Connected component thing](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/10.jpg)
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Kruskal's%20Algo/11.jpg)

Are you wondering how we will do the step $2$ of the algorithm? Which is to find whether two vertices are already connected.

There are two different ways to do it.

 1. Use an array to track the indices of the vertices. If both of the vertices are having same index, then they are already connected. Otherwise update the new indices accordingly and add that edge in ST.
 2. Use **Disjoint Set Union** Data Structure, which does this operation very efficiently.

### Approach without DSU

This is very simple. We will check whether the edge is connecting the vertices are having different IDs. Here we are using IDs to represent the connected components.

If they have different IDs, which means that they belong to different connected components. So we will join both of them by just changing the IDs of the vertices of these components.

```c++
#include <bits/stdc++.h>
using namespace std;

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

bool comparator(edge& a, edge& b)
{
	return a.weight < b.weight;
}

signed main() {
	
	int no_vertices = 4, no_edges = 5;
	
	vector<edge> graph;
	
	// Edges of graph
	graph.push_back(edge(1,2,2));
	graph.push_back(edge(1,4,5));
	graph.push_back(edge(2,3,3));
	graph.push_back(edge(1,3,4));
	graph.push_back(edge(3,4,6));
	
	// sorting the edges
	sort(graph.begin(), graph.end(), comparator);
	
	// To remember the edges in ST
	vector<bool> is_in_ST(no_edges);
	
	// Array to maintain the IDs of 
	// vertices
	vector<int> ID(no_vertices+1);
	
	int min_cost = 0;
	
	for(int i = 0; i < no_vertices+1; i++)
		ID[i] = i;
	
	for(int i = 0; i < no_edges; i++)
	{
		int ida = ID[graph[i].from], idb = ID[graph[i].to];
		
		// Connecting two set of vertices
		if(ida != idb)
		{	
			for(int j=1; j<=no_vertices; j++)
				if(ID[j] == ida)
					ID[j] = idb;
			
			is_in_ST[i] = true;
			min_cost += graph[i].weight;
		}
		
	}
	
	// Cost to make MST
	cout << min_cost << endl;
	
	for(int i=0; i<no_edges; i++)
		if(is_in_ST[i])
			cout << graph[i].from << "---" << graph[i].to << endl;

	return 0;
}

```
**Time Complexity**

 1. To sort the edges: $\mathcal{O}(|E|log{|E|})$
 2. To Update the IDs at each step takes $\mathcal{O}(|V|)$.
 3. The outer most loop can run at most $|E|$ times.

Overall time complexity: $\mathcal{O}(|E|log|E| + |V|*|E|)$

### Approach with DSU

DSU burns down the time complexity of step-2 from $\mathcal{O}(V)$ to $\mathcal{O}(log|V|)$.

Here we will use DSU to find whether two vertices are already connected. If they are not connected, then we will use the union operation to connect them.

It is much simpler and efficient than the previous one.

```c++
#include <bits/stdc++.h>
using namespace std;

// Disjoint Set Union Structure
class Dsu
{
    int size;
    int numberofcomponents;
    
    public:
    
    int *IDs;
    vector<int> sizes;
    
    // Constructor
    Dsu(int size)
    {
        numberofcomponents = size;
        IDs = new int[size+1];
        sizes.push_back(0);
        
        for(int i=1; i <= size; i++)
        {
            IDs[i] = i;
            sizes.push_back(1);
        }
    }
    
    // Find the ID of the component
    int find(int p)
    {
        int root = p;
        
        while(p != IDs[p])
            p = IDs[p];
        
        //path compression
        while(p != root)
        {
            int temp = root;
            root = IDs[temp];
            IDs[temp] = p;
        }
        
        return p;
    }
    
    
    // Join two components
    void unify(int a, int b)
    {
        int ida = find(a);
        int idb = find(b);
        
        if(ida == idb) return;
        
        //smaller will unify with bigger set
        if(sizes[ida] > sizes[idb])
        {
            IDs[idb] = IDs[ida];
            sizes[ida] += sizes[idb];
        }
        else
        {
            IDs[ida] = IDs[idb];
            sizes[idb] += sizes[ida];
        }
        
        numberofcomponents--;
    }
};

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

bool comparator(edge& a, edge& b)
{
	return a.weight < b.weight;
}

signed main() {
	
	int no_vertices = 4, no_edges = 5;
	
	vector<edge> graph;
	
	// Edges of graph
	graph.push_back(edge(1,2,2));
	graph.push_back(edge(1,4,5));
	graph.push_back(edge(2,3,3));
	graph.push_back(edge(1,3,4));
	graph.push_back(edge(3,4,6));
	
	// sorting the edges
	sort(graph.begin(), graph.end(), comparator);
	
	// To remember the edges in ST
	vector<bool> is_in_ST(no_edges);
	
	// Array to maintain the IDs of 
	// vertices
	
	int min_cost = 0;
	
	Dsu unionfind(no_vertices);
	
	for(int i = 0; i < no_edges; i++)
	{
		int ida = unionfind.find(graph[i].from);
		int idb = unionfind.find(graph[i].to);
		
		// Connecting two set of vertices
		if(ida != idb)
		{	
			unionfind.unify(ida,idb);
			is_in_ST[i] = true;
			min_cost += graph[i].weight;
		}
		
	}
	
	// Cost to make MST
	cout << min_cost << endl;
	
	for(int i=0; i<no_edges; i++)
		if(is_in_ST[i])
			cout << graph[i].from << "---" << graph[i].to << endl;

	return 0;
}
```

**Time Complexity**
 1. To sort the edges: $\mathcal{O}(|E|log{|E|})$
 2.  To Update the IDs at each step takes $\mathcal{O}(log|V|)$.
 3. The main loop can run at most $|E|$ times.

Overall time complexity: $\mathcal{O}(|E|log|E|+|E|log|V|)$

## Applications of MST

 1. In Network Designs: Pipelining, Roads & Transportation, Telephone or Electric cable network, etc.
 2. In Image recognization of handwritten expressions

## Other Algorithms to find MST

 1. Prim's Algorithm
 2. Boruvka's Algorithm
