## Topological Sort of Graph

Topological Sort is the sorting of the vertices in such a way that, for any two vertices $a$ and $b$, if there is a directed edge from $a \to b$ then $a$ must appear before $b$ in the topological ordering.

$a,b,c,d,e$ is the topologically sorted order for the graph below.

![enter image description here](https://lh3.googleusercontent.com/zOBG-tWmznt9QeFbW-SopxIpvyDSH7RgpmYKL9fIgth_TkRQ3sfuxXsDw7iWgmmyGdqip4cay_WS)

## Quiz Time

Is it always possible to find out the topological sort?

No. Whenever there is a cycle in a graph we can not find it.

To find out the topological sort, we will use the standard graph traversal technique DFS with some modification.

## Algorithm

 1. Mark all the vertices as unvisited.
 2. If there is a unvisited vertex, then run the DFS starting from that vertex. Otherwise stop.
 3. Inside DFS, If all the adjacent vertices of the start vertex are visited, then prepend this vertex at the head of the linked list.
 4. Go to the step 2.

Starting from the head, the linked list shows the topological sort of the given graph.

**Visualization:**


```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000

void dfs(vector<vector<int> > &graph, int start, list<int> &linked_list, vector<bool>& visited)
{
	visited[start] = true;
	
	for(auto i: graph[start])
		if(!visited[i])
			dfs(graph, i, linked_list, visited);
	
	linked_list.push_front(start);
	
}

void Topological_sort(int no_vertices, vector<vector<int> > &graph)
{
	vector<bool> visited(no_vertices + 1);
	
	list<int> linked_list;
	
	for(int i = 1; i <= no_vertices; i++)
		if(!visited[i])
			dfs(graph, i, linked_list, visited);
	
	for(auto vertex: linked_list)
		cout << vertex << " ";
	
}

int main()
{
	
	int no_vertices = 5;
	
	vector<vector<int> > graph(no_vertices+1, vector<int>());
	
	graph[1].push_back(3);
	graph[2].push_back(3);
	graph[3].push_back(4);
	graph[3].push_back(5);
	
	Topological_sort(no_vertices, graph);
	
	return 0;
}
```

## Quiz Time

Does topological sort give a unique ordering of the vertices?

No, it is not unique in every case, because we can find many orderings which satisfies the condition of topological sort.

In the graph shown in the image above, $b,a,c,d,e$ and $a,b,c,d,e$ both are valid topological sorts.

## Application

 1. It is used to find out the shortest distance path efficiently.
 2. Scheduling of tasks according to their dependencies on each other, where dependencies are represented by the directed edges.


## Kahn's Algorithm for Topological Sort

We have seen how to find the topological sort using modified DFS. Now, we will see Kahn's algorithm, which is modified BFS.

We will use the indegree of vertices to find the next vertex of the topological ordering. How?

**The main concept**: If the indegree of the vertex is zero, then it must appear before the vertices whose indegrees are greater than zero.

## Algorithm

 1. First of all, count the indegrees of all the vertices.
 2. Add all the vertices whose indegrees are zero to the queue.
 3. Start the loops like BFS.
 4. Dequeue a vertex from the queue, say V and append it to the sorting order.
 5. Visit all the adjacent vertices of V and decrease the indegrees of all of them by 1.
 6. Enqueue all the adjacent vertices whose indegrees become zero.
 7. If the queue is empty, then stop the algorithm otherwise continue from the step 4.

**Visualization**

```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000


void Topological_sort(int no_vertices, vector<vector<int> > &graph)
{
	list<int> topological_order;
	
	vector<int> indegrees(no_vertices + 1);
	
	for(int i = 1; i <= graph.size(); i++)
		for(int j = 0; j < graph[j].size(); j++)
			indegrees[graph[i][j]]++;
	
	
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
			--indegrees[i];
			if(indegrees[i] == 0)
				que.push(i);
		}
		
	}
	
	for(auto i: topological_order)
		cout << i << " ";
	
}

int main()
{
	
	int no_vertices = 5;
	
	vector<vector<int> > graph(no_vertices+1, vector<int>());
	
	graph[1].push_back(3);
	graph[2].push_back(3);
	graph[3].push_back(4);
	graph[3].push_back(5);
	
	Topological_sort(no_vertices, graph);
	
	return 0;
}
```
**Variant:** We can use the priority queue in the place of queue if we want smaller indexed vertices to appear first.
