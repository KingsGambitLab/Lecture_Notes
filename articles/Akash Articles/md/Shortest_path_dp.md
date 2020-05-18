## Single source shortest path using Dynamic Programming for Directed Acyclic Graph(DAG)

We can solve the single source shortest path problem using dynamic programming. How?

First of all, we will see how to solve this problem using recursion with memoization(top-down approach) followed by bottom-up dynamic programming approach.

## Quiz Time

You are given that the shortest path between two vertices $A$ and $B$ passes through $C$. What can you conclude from it?

Answer: $SD(A, B) = SD(A,C) + SD(C,B)$

$SD$ stands for Shortest Distance.

-- --

The above answer can be proved using contradiction. Suppose that shortest path between $A$ and $B$ passes through $C$ and the path from $A$ to $C$ is not shortest, then we can replace it with some other vertex $D$ such that the shortest path becomes $A \to D \to B$ which is better than $A \to C \to B$, but it is a contradiction becuase we have asssumed that $A \to C \to B$ is the shortest path between $A$ and $B$.

We will use the above property together with memoization to solve the problem. How?

Suppose that we are searching a shortest path between $u$(source) and $v$. Then we know that the shortest path between $u$ and $v$ must be passing through one of the vertices which are putting a directed edge on $v$ (incoming edges for $v$).

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/1.jpg)

So, first of all we will find a shortest path between source and $x$, $y$, $z$ one by one. Then we can see that the shortest path between $u$ to v will be either $\text{SP}(x) \to v$ or $\text{SP}(y) \to v$ or $\text{SP}(z) \to v$ depending on which one is minimum from $\text{SD}(x)+w1$, $\text{SD}(y)+w2$, $\text{SD}(z)+w3$, respectively.

**Note:** $\text{SP}$ stands for shortest path upto the given vertex and $\text{SD}$ stands for shortest distance.

Done? Let's see proper algorithm.

## Recursive Memoization Approach

Now, if we want to find out the shortest path from source $u$ to vertex $v$, then start the recursion from the vertex $v$. 

Move in the reverse direction of the directed edges connected with $v$ and recurse on each of the (reverse)adjacent vertex(i.e. $x,y,z$) until you reach at the source u.

Meanwhile update the shortest distances accordingly. 

**Note:** **Memoization** is just the memorization of the obtained results, which can be used again and again to obtain new results.

One thing to notice is that, once the shortest distance for a vertex is found, we can do memoization and use it again to block unnecessary recursive calls.

### Algorithm
 1. Assign all the distances to $\infty$.
 2. Now, assign source to source distance to $0$ and start the algorithm.
 3. Loop through all the vertices, if the distance to a vertex is not found yet then start the recursion over that vertex.

 4. In the recursive function, suppose you are starting from a vertex $v$, then move backward over the incoming edges to the vertex $v$.
	![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/2.jpg)
	
	In the image above $x$,$y$,$z$ are these vertices, we can reached by moving backward over the incoming edges to the vertex $v$. 
	
 5. Now, we will do recursive call over all these vertices and find out the shortest distance to all of them first and update $distance[v]$ as below:
	Say $u_1, u_2, \ldots , u_n$ are the vertices we reached by moving backward over the edges.
$distance[v] = min(distance[v], ShortestDistance(u_i) + EdgeWeight(u_i,v) )$  $\forall i<=n$. 

	**Note:** Stop the recursion at the source vertex, which is a base case.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/3.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/4.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/5.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/6.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/7.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/8.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/9.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/10.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/11.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/12.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/13.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/14.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/15.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/16.jpg)
	
```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000


struct edge {
	int from, to, weight;
	
	edge(int a,int b,int w)
	{
		from = a;
		to = b;
		weight = w;
	}
	
};


int Shortest_Path(vector<vector<edge> > &graph, int source, int vertex,
								vector<int> &distances, vector<int> &parent)
{
	if(vertex == source)
		return 0;
	
	if(distances[vertex] != MAX_DIST)
		return distances[vertex];
	
	for(auto vedge: graph[vertex])
	{
		int new_distance = Shortest_Path(graph, source, vedge.from, 
										distances, parent) + vedge.weight;
		if(new_distance < distances[vertex])
		{
			distances[vertex] = new_distance;
			parent[vertex] = vedge.from;
		}
	}
	
	return distances[vertex];
	
}

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


int main()
{
	
	int no_vertices = 6;
	
	vector<vector<edge> > graph(no_vertices+1, vector<edge>());
	
	// Making the graph using
	// Reverse edges
	graph[2].push_back(edge(1,2,1));
	graph[2].push_back(edge(1,2,6));
	graph[4].push_back(edge(2,4,1));
	graph[3].push_back(edge(4,3,1));
	graph[5].push_back(edge(3,5,1));
	graph[5].push_back(edge(2,5,7));
	graph[6].push_back(edge(4,6,3));
	
	
	vector<int> distances(no_vertices + 1, MAX_DIST), parent(no_vertices +1, -1);
	
	int source = 1, destination = 5;
	
	distances[source] = 0;
	
	for(int i = 1; i <= no_vertices; i++)
		if(distances[i] == MAX_DIST)
			Shortest_Path(graph, source, i, distances, parent);
			
	for(int i = 1; i <= no_vertices; i++)
		cout << distances[i] << " ";
	
	
	return 0;
}
```

## Bottom-Up Dynamic Programming Approach

How can we do bottom-up dynamic programming to solve the SSSP problem?

Where to start the bottom-up dp? Can we start it at any random vertex? No, We cannot. Right? Now the thing is that, we have to order the vertices in some order, such that before reaching to a particular vertex(say $v$), we must have found the shortest distances to all the vertices, which are putting an incoming edge over $v$.

Are you familiar with this kind of ordering of vertices? It is **"Topological ordering"**. Topological ordering ensures that we will process vertices in the required manner.

Let's see the algorithm.

### Algorithm

 1. First of all, find the topological sort of the vertices.
 2. Assign all the distances to $\infty$.
 3. Start the algorithm by assigning the distance from source to source as zero.
 4. Loop over the vertices in the order generated by the topological sort and update the shortest distances to all the adjacent vertices of all of them, one by one in the order.

**Visualization**
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/17.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/18.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/19.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/20.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/21.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/22.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/23.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/24.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/25.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/26.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/27.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/ShortestPath_DP/28.jpg)
```c++

#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000


struct edge {
	int from, to, weight;
	
	edge(int a,int b,int w)
	{
		from = a;
		to = b;
		weight = w;
	}
	
};


// Kahn's Algorithm for Topological Sort
list<int> Topological_Sort(vector<vector<edge> > &graph, int no_vertices)
{
	list<int> topological_order;
	
	vector<int> indegrees(no_vertices + 1);
	
	for(int i = 1; i <= graph.size(); i++)
		for(int j = 0; j < graph[j].size(); j++)
			indegrees[graph[i][j].to]++;
	
	
	queue<int> que;
	
	for(int i = 1; i <= no_vertices; i++)
		if(indegrees[i] == 0)
			que.push(i);
	
	
	while(!que.empty())
	{
		int V = que.front();
		que.pop();
		
		topological_order.push_back(V);
		
		for(auto i: graph[V])
		{
			--indegrees[i.to];
			if(indegrees[i.to] == 0)
				que.push(i.to);
		}
	}
	
	return topological_order;
	
}

void shortest_path_dp(vector<vector<edge> > &graph, vector<int> &distances, int source)
{
	distances[source] = 0;
	
	list<int> topological_order = Topological_Sort(graph, no_vertices);
	
	for(auto i: topological_order)
		for(auto edgev: graph[i])
			if(distances[edgev.to] > distances[edgev.from] + edgev.weight)
				distances[edgev.to] = distances[edgev.from] + edgev.weight;
}

int main()
{
	
	int no_vertices = 6;
	
	vector<vector<edge> > graph(no_vertices+1, vector<edge>());
	
	graph[1].push_back(edge(1,2,1));
	graph[1].push_back(edge(1,3,6));
	graph[2].push_back(edge(2,4,1));
	graph[4].push_back(edge(4,3,1));
	graph[3].push_back(edge(3,5,1));
	graph[2].push_back(edge(2,5,7));
	graph[4].push_back(edge(4,6,3));
		
	vector<int> distances(no_vertices + 1, MAX_DIST);
	
	int source = 1;
	
	shortest_path_dp(graph, distances, source);
	
	for(int i = 1; i <= no_vertices; i++)
		cout << distances[i] << " ";
	
	return 0;
}

```

### Time Complexity

There are total $|V|$ subproblems and eachone takes $\Theta (Indegree(v) +1)$ time. So the total time complexity will be $\sum_{\forall v \in V}  (Indegree(v) +1)$, which is equal to $\mathcal{O}(|V|+|E|)$.

Where $V$ is the set of vertices.

**Note**: Handshaking lemma for directed graph: $\sum_{\forall v \in V}Indegree(v) = E = \sum_{\forall v \in V} Outdegree(v)$
