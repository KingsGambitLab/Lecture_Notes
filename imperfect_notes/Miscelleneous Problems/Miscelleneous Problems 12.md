# Miscelleneous Problems 12

## 423 Good Graph

### Problem Statement

Given a directed graph of N nodes where each node is pointing to any one of the N nodes (can possibly point to itself). Ishu, the coder, is bored and he has discovered a problem out of it to keep himself busy. Problem is as follows:

A node is ```'good' ```if it satisfies one of the following:

```
1. It is the special node (marked as node 1)
2. It is pointing to the special node (node 1)
3. It is pointing to a good node.
```

Ishu is going to change pointers of some nodes to make them all 'good'. You have to find the min. number of pointers to change in order to
make all the nodes good (Thus, a Good Graph).

Note: Resultant Graph should hold the property that all nodes are good and each node must point to exactly one node.

**Constraints:**

```
1 <= N <= 100,000
```

**Input:** 

```
A vector of N integers containing N numbers 
all between 1 to N, where i-th number is 
the number of node that i-th node is pointing to.
```
 
**Output:**

```
An Integer denoting min. number of pointer changes.
```

**Example:**

```C++
input: [1, 2, 1, 2]
output: 1 (Pointer of node 2 is made to point to node 1)

input: [3, 1, 3, 1]
output: 1 (Pointer of node 3 is made to point to node 1)
```

### Wrong Approach
- Initialize count = 0.
- From every point do a BFS/DFS. If you can't reach any special node, increase count by 1.
- This approach will tell us the total number of non-good nodes.
- We can change the pointer in every good node. Thus we can say after count number of pointer changes we will have a good graph.
- This approach is wrong. Because there might a case like following:
```C++
input: [1,2,1,2]
```
- Here if we change the pointer of second element, we do not need to change the pointer of forth element. Thus we can say the minimum pointer change is 1. Here, the count of non-good nodes is two.
- How can we improve this approach?
### Brute Force
- For every node find the top most node that can reached from it.
- Save that node in a set.
- Return set.size()
### Hints
- We can see that if there is path from a node to a good node then it is a good node. 
- If we can reach a good node from a given node we can mark it as good node.
- If we can not reach a good node from a given node, we will need at least one pointer change to make it good.
- If there is a chain like $5->4->3->2->4$. Now, if we change pointer of 4 to 1, all the nodes will become good.
- So, we can see again we just one pointer change to make the whole chain good.
- Let's color all the chains one by one. 
- Since every node is only connected to at maximum one other node. BFS and DFS are same. It is similar to linked list traversal.

```C++
input: [1,2,2,3,4,5,7,7,8,9]

Linked list representation: 
1 
2<-2<-3<-4<-5<-6 
7<-7<-8<-9<-10
```

### Code
```C++
int Solution::solve(vector<int> &A) {
    
    int n = A.size();
    bool good[n];
    good[0] = true;
    for(int i = 1; i < n; i += 1){
        good[i] = false;
    }
    bool visited[n];
    for(int i = 0; i < n; i += 1){
        visited[i] = false;
    }
    int curr, next;
    int ans = 0, c = 0;
    int color[n];
    for(int i = 0; i < n; i += 1) {
        if(visited[i] == false){
            curr = i;
            visited[i] = true;
            next = A[curr] - 1;
            color[curr] = c;
            while(visited[next] == false){
                good[curr] = true;
                visited[next] = true;
                color[next] = c;
                curr = next;
                next = A[curr] - 1;
            }
            if(color[next] == c && next != 0 ){
                ans += 1;
            }
            c += 1;
        }
    }
    return ans;
}
```
### Time Complexity
Since every node will be visited at max twice, the time complexity will be $O(n)$.

### Dry Run
|Visited|Color|Good|i|A|count|
|:--|:--|:--|:--|:--|:--|
|[f,f,f,f,f,f]|[]|[t,f,f,f,f,f]|0|[1,2,2,5,6,3]|0|
|[t,f,f,f,f,f]|[0,]|[t,f,f,f,f,f]|1|[1,2,2,5,6,3]|0|
|[t,t,f,f,f,f]|[0,1]|[t,t,f,f,f,f]|2|[1,2,2,5,6,3]|1|
|[t,t,t,f,f,f]|[0,1,2]|[t,t,t,f,f,f]|3|[1,2,2,5,6,3]|1|
|[t,t,t,t,t,t]|[0,1,2,3,3,3]|[t,t,t,t,t,t]|4|[1,2,2,5,6,3]|1|
|All visited||||||


[Good Graph](https://www.interviewbit.com/hire/test/problem/423/)

## 438 King Graph

### Problem
Kingdom JenaRajya is a well planned kingdom. They have N houses numbered [0,1,..,N-1] in the city and some  bidirectional roads connecting the houses. King Jena has decided to meet his people and so he will visit one of the house in the kingdom where others can gather and meet him. King Jena is very kind and do not want anyone to travel far to meet him. So, he has come up with the following criteria to decide the house he will be visiting:

Assuming that the people from other houses will take the shortest possible path to reach the house the king is visiting, King Jena wants to minimize the maximum distance one has to travel to meet him. In other words, he will choose the house where the shortest distance to the farthest house is minimum possible.

Output the house number which King Jena will visit. 

**Note:**
1. In case there is a tie, he will visit the house with minimum house number.
2. You can assume that the graph is connected and so everyone will be able to visit.

**Constraints:**
1 <= N <= 500
1 <= Length of road <= 1000000

**Input format:**
Adjacency matrix representation of the graph. 
A[i][j] = distance between house i and j. (A[i][i] = 0 and A[i][j] = -1, if house i and house j have no road between them)
As the roads are bidirectional, A[i][j] = A[j][i]

**Example:**

```C++
Input:
A = [[0, 6, 8, -1],
     [6, 0, 9, -1], 
     [8, 9, 0, 4],
     [-1, -1, 4, 0]]

Output:
2
```
### Brute Force
- We can run Dijkstra from each house to find the distance of every other house to this house.
- We can get a distance matrix for each node.
- Then we can find for every house the distance of the furtherest house from that house.
- Find the house which has minimum such distance.
- Time Complexity $O(V* ElogV)$

### Hint
- $E$ can be as big as $V^2$. The above brute force can take $O(V^3logV)$.
- We can reduce the time complexity by using Floyd Warsal all pair shortest path algorithm.
- Floyd Warsal will take only $O(V^3)$ time. This is not much better. However, the implementation is much simpler.
- Inductive Hypothesis
  - Suppose that prior to the kth iteration it holds that for $i, j \in V$, $d_{ij}$ contains the length of the shortest path Q from i to j in G containing only vertices in the set ${1, 2, ..., k − 1}$
  - We can prove floyd warsal using this hypothesis.

### Code
```C++

#define INF 1000000000

int Solution::solve(vector<vector<int> >& A){
	//No. of places
	int n = A.size();
	
	//Floyd-Warshall Algorithm implementation to find all pairs shortest paths
	
	vector<vector<int> > d(n,vector<int>(n,INF));
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			if(A[i][j] != -1) d[i][j] = A[i][j];
		}
	}
	
	for(int i=0; i<n; i++)	d[i][i]=0;
	
	for(int k=0; k<n; k++)
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				if(d[i][j] > d[i][k]+d[k][j])
					d[i][j] = d[i][k]+d[k][j];
					
 	
 	//Find the required answer
	int maxDist = -1, ans = -1, temp = INF;
	for(int i=0; i<n; i++){
		maxDist = -1;
		for(int j=0; j<n; j++) maxDist = max(d[i][j], maxDist);
		
		if(maxDist < temp){
			temp = maxDist;	ans = i;
		}
	}
	return ans;
}

```
### Time Complexity
- $O(V^3)$

### Dry Run
- Adjacency Matrix : $\begin{bmatrix}
    0&3&6\\
    3&0&2\\
    6&2&0
    \end{bmatrix}$
- Distance Matrix :$\begin{bmatrix}
    0&3&5\\
    3&0&2\\
    5&2&0
    \end{bmatrix}$
- We can see that the answer will be node at index 1. As the distances are ${3,0,2}$ for it.
    

[King Graph](https://www.interviewbit.com/admin/new_problems/438/#/hints)

## 441 Snake And Ladder Game

### Problem Statement
Given a `snake and ladder` board.
You have to find the ```minimum number of dice throws``` required to reach the last cell(Nth cell) from first cell(1st cell).

For example:
![before](https://images8.alphacoders.com/448/448009.jpg)

```
Here N is 30 and you have to reach 30 from 1.
Here minimum number of dice throws are 3 
In first dice throw you will get a 2
In second dice throw you will get a 6
And in third dice throw you will get a 2
```
For snake and ladders there are two arrays A and B of same size.
Ladder or a Snake at position A[i] will take you to a position B[i].

[Snake And Ladder](https://www.interviewbit.com/hire/test/problem/441/)

### Easier Problem
- If there were no snakes and ladders, the problem will become simpler. We can visit 6th node after the given node in one roll. So, for n we will need to do ceiling of $n/6$ rolls. 
### Hint
- Having snakes and ladders changes the problem. Jumping to the 6th node might not be optimal. 
- Here we can replace every node i that has a ladder to j or snake to j with j. 
- Now, we can do a bfs to find the shortest path.


### Code
```C++
int solve(int N, vector<int> &A, vector<int> &B)
{
	vector<int> moves(N+1, -1);
	vector<bool> visited(N+1, false);
	for(int i=0;i<A.size();i++){
		moves[A[i]] = B[i];
	}
	queue<pair<int,int> > que;
	que.push(make_pair(1,0));
	pair<int,int> entryExtracted ;
	visited[1]=true;
	while(!que.empty())
	{
		entryExtracted = que.front();
		
		if(entryExtracted.first==N)
			break;
		que.pop();
		for(int i=entryExtracted.first+1;i<=entryExtracted.first+6 && i<=N;i++)
		{
			pair<int,int> entry;
			if(!visited[i])
			{
				entry.second = entryExtracted.second+1;
				visited[i]=true;
				if(moves[i]!=-1)
				{
					entry.first = moves[i];
				}else
				entry.first =i;
				
				que.push(entry);
			}
		}
	}
	return entryExtracted.second;
}
```