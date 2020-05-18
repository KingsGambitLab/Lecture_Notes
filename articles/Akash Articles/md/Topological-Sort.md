Suppose, you want to enter into a well-known computer science university, but they always test students before giving admission. Now it is your turn, they give you a long list of pairs of courses. Each pair $(\text{course}A,\text{courseB})$ is representing that, completing the $\text{courseA}$ is a prerequisite for the $\text{courseB}$.

Now the challenge is that, they will give you two courses, $\text{courseX}$ and $\text{courseY}$. And you have to find out whether $\text{courseX}$ can be done before $\text{courseY}$. 

For example, You are given a list: $(A,B), (B,C), (D,A), (C,E), (F,A)$, what will be the answer for two courses, D and C? 

Yes, you can do $\text{course}D$ before $\text{course}C$. But...

The main twist is, the list is very large, so you can not remember everything. They are smart, so they have given you course names which are not computer science courses.

How will you tackle this test? If you are allowed to use some resources like computer, then?

Well, this problem can be solved by converting it to a graph where vertices are courses and directed edges representing prerequisites. Then find out the topological sort of the graph and you are done!!

But what is Topological Sort? Let's see.

## Topological Sort

Topological Sort is the sorting of the vertices in such a way that, for any two vertices $a$ and $b$, if there is a directed edge from $a \to b$ then $a$ must appear before $b$ in the topological ordering.

$a,b,c,d,e$ is the topologically ordering for the graph below.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Topological%20Sort/1.jpg)

## Quiz Time

$Q.1$ Is it always possible to find out the topological sort?

No. Whenever there is a cycle in a graph we can not find it. See the image below: 

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Topological%20Sort/2.jpg)

We can not find proper dependency between any two vertices, becuase each of them are interdependent.

So the condition for the topological sort is, the graph must be a DAG - Directed Acyclic Graph.

$Q.2$ Does topological sort give a unique ordering of the vertices?

No, it is not unique in every case, because we can find many orderings which satisfies the condition of the topological sort.
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Topological%20Sort/3.jpg)

In the graph shown in the image above, $b,a,c,d,e$ and $a,b,c,d,e$ both are valid topological sorts.

But how to find a topological ordering for a given DAG?

**Notes:** 
- Assuming that the graph is **DAG**, becuase you can not find topological sort in case of cycle (as shown above).
- **Indegree** for a vertex is count of the number of incoming directed edges.

We have two standard techniques for graph traversal: DFS and BFS. Can we use any of them to find out topological ordering?

Let's see, how modified BFS can be used to find it, which is known as **Kahn's Algorithm**.

## Kahn's Algorithm for Topological Sort

We will use the indegree of vertices to find the topological ordering. How? Let's observe:

In the image below, the number in the square bracket represents indegree for a vertex near to it.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Topological%20Sort/4.jpg)

As we have seen the topological ordering for the above graph is $a,b,c,d,e$. Now, what is your observation?

See that the vertices having indegree $0$ are appearing first in the ordering. But what next? What if we remove both the vertices and all the edges coming out from it?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Topological%20Sort/5.jpg)

See now, $c$ is the vertex having $0$ indegree, which is appearning next in the ordering. 

And what if we remove $c$ and all the edges coming out from it. The next $0$ indegree vertices are $d$ and $e$, which are the next vertices in the ordering.

Done, right? Let's see the final algorithm.

## Algorithm

 1. First of all, count the indegrees of all the vertices.
 2. Add all the vertices whose indegrees are zero to the queue.
 3. Start the loops like BFS.
 4. Dequeue a vertex from the queue, say $V$ and append it to the sorting order.
 5. Visit all the adjacent vertices of $V$ and decrease the indegrees of all of them by $1$.
 6. Enqueue all the adjacent vertices whose indegrees become zero.
 7. If the queue is empty, then stop the algorithm otherwise continue from the step $4$.

**Visualization**


```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000


void Topological_sort(int no_vertices, vector<vector<int> > &graph)
{
	list<int> topological_order;
	
	vector<int> indegrees(no_vertices + 1);
	
	for(int i = 1; i < graph.size(); i++)
		for(int j = 0; j < graph[i].size(); j++)
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
Now, we have seen the approach using modified BFS. Can we use DFS as well?

Yes, we can use DFS with some modification. 

Here, we will start DFS from an arbitrary vertex-$U$ and first visit all the adjacent vertices by recursively calling DFS on all of them and then at the end, add U at the front of the topological order. 

What does it do?

This thing makes sure that all the vertices which are dependent on U will appear after U, because we are adding U at the front of the ordering.

## Algorithm using DFS

 1. Mark all the vertices as unvisited.
 2. Choose any unvisited vertex and start a DFS start from it (say $V$).
 3. Inside DFS, Mark $V$ as visited and loop over the adjacent vertices of $V$.
 4. Recursivly call DFS on all the unvisited adjacent vertices.
 5. As all the DFS calls completes, add $V$ at the front(head) of the topological order.
 6. If there is an unvisited vertex then go to the step 2, else stop.
**Note:** You can take linked list to store the topological order, which is empty at the starting of the algorithm.

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

### Time Complexity:
It has the same time complexity as DFS and BFS: $\mathcal{O}(|V|+|E|)$

## Applications of Topological Ordering

 1. It is used in the process to find out the shortest distance paths efficiently.
 2. Scheduling of tasks according to their dependencies on each other, where dependencies are represented by the directed edges.
