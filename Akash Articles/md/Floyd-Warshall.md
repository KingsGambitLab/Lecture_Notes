## All Pair Shortest Path Problem

Statement: Given a graph, Find out the shortest distance paths between every pair of vertices.

## Brute Force

We have seen Dijkstra's algorithm and Bellman-Ford algorithm, which solves the SSSP problem. 

We can run these algorithms for every vertex one by one, which solves the given problem.

This will give the complexity of $\mathcal{O}( (|V| + |E|) \cdot |V| \cdot log|V|)$ in the case of Dijkstra's algorithm and $\mathcal{O} (|V|^2 \cdot |E|)$ in the case of Bellman-Ford Algorithm.

**Floyd-Warshall Algorithm** solves all pair shortest path problem in an efficient manner.

## Floyd-Warshall Algorithm

This algorithm is an example of Dynamic Programming. We split the process of finding the shortest paths in several phases.

-- --

### Quiz Time

You are given that the shortest path between two vertices $A$ and $B$ passes through $C$, i.e. $C$ is the intermediate vertex in the shortest path from $A$ to $B$. What can you conclude from it? 

Answer: $SD(A, B) = SD(A,C) + SD(C,B)$

$SD$ stands for Shortest Distance.

-- --

The above answer can be proved using contradiction.

The Floyd-Warshall algorithm works based on the above answer. 

Before the $i^{th}$ phase of the algorithm, it finds out the shortest distance path between every pair of vertices which uses intermediate vertices only from the set $\{1,2,..,i-1\}$. In every phase of the algorithm, we add one more vertex in the set.

In the $i^{th}$ phase, we update the $distance$ matrix considering the two cases below:

For an entry $distance[a][b]$,

 1. If the shortest path between $a$ and $b$ which uses intermediate vertices from the set $\{1,2,...i-1\}$ is longer than the one that uses $\{1,2,...,i\}$, then update the shortest distance path as below:

	$distance[a][b] = distance[a][i]+distance[i][b]$

	Where $distance[a][b]$ is the shortest distance between $a$ and $b$ which uses intermediate vertices from the set $\{1,2,..,i-1\}$.

 2. Otherwise, $distance[a][b]$ will remain unchanged.

### Algorithm

 1. Initialize $N \times N$ distance matrix with infinity.
  2. Assign every element representing distance between vertex to itself to zero - assign every diagonal element of distance matrix to zero.
  3. For all pair of vertices, If there is an edge between $A$ and $B$, then update $distance[A][B]$ to $Edge Weight(A,B)$.
  4. Start from the first vertex, say phase $i=1$.
  5.  For all pairs of the vertices, update the new shortest distance between them using the condition below,
	$distance[a][b] > distance[a][i]+distance[i][b]$
 6. If $i$ is equal to the number of vertices, then stop otherwise increment $i$ and repeat step $5$.

```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000


void Floyd_Warshall(int no_vertices, vector<vector<int> > & distances)
{
	// i shows the phase
	for(int i = 1; i <= no_vertices; i++)
	{
		// Update distance matrix for all pairs
		for(int a = 1; a <= no_vertices; a++)
		{
			for(int b = 1; b <= no_vertices; b++)
			{
				if(distances[a][i] < MAX_DIST && distances[i][b] < MAX_DIST)
					distances[a][b]	= min(distances[a][b], distances[a][i]+distances[i][b]);
			}
		}
	}
}


int main()
{
	
	int no_vertices=5;
	
	// N*N array to store the distances between every pair
	vector<vector<int> > distances(no_vertices+1, vector<int> (no_vertices+1, MAX_DIST));
	
	// Adding the edges virtually by
	// updating distance matrix
	distances[1][2]=1;
	distances[1][3]=-3;
	distances[2][4]=2;
	distances[2][5]=1;
	distances[3][4]=-1;
	distances[3][5]=2;
	distances[4][5]=1;
	
	for(int i = 1; i <= no_vertices; i++)
		distances[i][i] = 0;
	
	Floyd_Warshall(no_vertices, distances);
	
	// Printing the distance matrix
	for(int i=1;i<=no_vertices;i++)
	{
		for(int j=1;j<=no_vertices;j++)
		{
			if(distances[i][j]!=MAX_DIST)
				cout << setw(5) << right << distances[i][j] << "  ";
			else
				cout << setw(5) << right << "INF" << "  ";
		}
		cout << endl;
	}
	
	return 0;
}
```

### Time Complexity
As there are three loops, each running number of vertices time, the complexity will be $\mathcal{O}(|V|^3)$.

In worst case, this is better than the brute force approach.

### Path Reconstruction

To reconstruct the path, we have to store the next vertex for each pair and whenever we update the shortest distance we have to update the next vertex as well.

```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000


void Floyd_Warshall(int no_vertices, vector<vector<int> > & distances, vector<vector<int> > & next)
{
	// i shows the phase
	for(int i = 1; i <= no_vertices; i++)
	{
		// Update distance matrix for all pairs
		for(int a = 1; a <= no_vertices; a++)
			for(int b = 1; b <= no_vertices; b++)				
				if( distances[a][b] > distances[a][i]+distances[i][b] && 
				distances[a][i] < MAX_DIST && distances[i][b] < MAX_DIST )
				{
					distances[a][b]	= distances[a][i]+distances[i][b];
					next[a][b] = next[a][i];
				}
	}
}


int main()
{
	
	int no_vertices=5;
	
	// N*N array to store the distances between every pair
	vector<vector<int> > distances(no_vertices+1, vector<int> (no_vertices+1, MAX_DIST));
	
	
	// N*N array to store the next vertex for every pair
	vector<vector<int> > next(no_vertices+1, vector<int> (no_vertices+1, -1));
	
	
	// Adding the edges virtually by
	// updating distance matrix and
	// next vertex matrix
	distances[1][2]=1, next[1][2] = 2;
	distances[1][3]=-3, next[1][3] = 3;
	distances[2][4]=2, next[2][4] = 4;
	distances[2][5]=1, next[2][5] = 5;
	distances[3][4]=-1, next[3][4] = 4;
	distances[3][5]=2, next[3][5] = 5;
	distances[4][5]=1, next[4][5] = 5;
	
	// Update all the diagonal elements
	for(int i = 1; i <= no_vertices; i++)
	{
		distances[i][i] = 0;
		next[i][i] = i;
	}
	
	Floyd_Warshall(no_vertices, distances, next);
	
	// Example of path reconstruction
	int source = 1, destination = 5;
	
	while(source != destination)
	{
		cout << source << " "; 
		source = next[source][destination];
	}
	
	cout << destination << endl;
	
	return 0;
}
```

### Negative Cycle Case

We can use the Floyd-Warshall algorithm to detect the negative cycle and to find the pair of vertices affected by it.

Initially, the distance between the vertex to itself was zero, but if it turns out to be negative at the end of the algorithm, then there is a negative cycle.

```c++
#include <bits/stdc++.h>
using namespace std;
#define MAX_DIST 100000000


void Floyd_Warshall_with_NC(int no_vertices, vector<vector<int> > & distances)
{
	// i shows the phase
	for(int i = 1; i <= no_vertices; i++)
		for(int a = 1; a <= no_vertices; a++)
			for(int b = 1; b <= no_vertices; b++)
				if( distances[a][b] > distances[a][i]+distances[i][b] && 
				distances[a][i] < MAX_DIST && distances[i][b] < MAX_DIST )
					distances[a][b]	= distances[a][i]+distances[i][b];
					
	
	bool is_negative_cycle = false;
	
	// Check for negative cycle
	for (int i = 1; i <= no_vertices; ++i) 
	    for (int a = 1; a <= no_vertices; ++a) 
	        for (int b = 1; b <= no_vertices; ++b) 
	        {
	        	// If there is a negative cycle, then update the distance to -Infinity
	            if (distances[a][i] < MAX_DIST && distances[i][i] < 0
	            						&& distances[i][b] < MAX_DIST)
	            {
	            	distances[a][b] = -MAX_DIST;
	            	is_negative_cycle = true;
	            }
	        }
	}
	
	if(is_negative_cycle)
	{
		cout << "The following pairs are affected by the negative cycle:" << endl;
		for (int a = 1; a <= no_vertices; ++a)
		    for (int b = 1; b <= no_vertices; ++b)
		        if (distances[a][b] = -MAX_DIST)
		        	cout << a << "--" << b << endl;
	}
	
}


int main()
{	
	int no_vertices=5;
	
	// N*N array to store the distances between every pair
	vector<vector<int> > distances(no_vertices+1, vector<int> (no_vertices+1, MAX_DIST));
	
	
	// Adding the edges virtually by
	// updating distance matrix
	distances[1][2]=1;
	distances[1][3]=-3;
	distances[2][4]=2;
	distances[4][1]=1;
	distances[3][4]=-2;
	
	for(int i = 1; i <= no_vertices; i++)
		distances[i][i] = 0;
	
	Floyd_Warshall_with_NC(no_vertices, distances);
	
	return 0;
}
```

### Application of Floyd-Warshall Algorithm

 1. "Widest Path Finding Algorithm", which is an algorithm to finding a path between two vertices of the graph **maximizing the weight of the minimum-weight edge in the path**, can be solved using this algorithm.
 2. To do optimal routing.
 3. In Gauss-Jordan Algorithm, to find reduced form of matrix and inversion matrix.

## Other Shortest Path Finding Algorithms:

 1. Using Dynamic Programming
 2. Dijkstra's Algorithm
 3. Bellman-Ford Algorithm
