
## Disjoint Set Union

Disjoint Set Union is one of the simplest and easy to implement data structure, which is used to keep track of disjoint(Non-overlapping) dynamic sets.

![enter image description here](https://lh3.googleusercontent.com/IhDMlNBw6t1hp2gmRfpGYKGqioeFLRNLEwb3yrnsaLCl_-N5IKv1m2GfTev5-eVMYOk_Or54kyyW "DSUs")

In the image above, $\{a,b,c,d\}$ and $\{e,f\}$ are two non-overlapping sets. Dynamic here says that we can combine any two sets and still keep track of elements of it.

There are three main operations of this data structure: Make-set, Find and Union

 1. **Make-Set**: This operation creates a disjoint set each one having a single element.

 2. **Find**: This operation finds a unique set to which a particular element belongs.

 3. **Union**: This operation unifies two disjoint sets.

There are many ways we can represent this data structure: Linked list, Array, Trees. But here we will discuss its representation using array and visualize using tree.

**Some Terminologies**

 - **Parent** is a main attribute of an element which represents an element by which a particular element is connected with some disjoint set.
	
![enter image description here](https://lh3.googleusercontent.com/IhDMlNBw6t1hp2gmRfpGYKGqioeFLRNLEwb3yrnsaLCl_-N5IKv1m2GfTev5-eVMYOk_Or54kyyW)


In the image, $c$ is parent of $d$ and $a$ is parent of $c$.
	
 - **Root** is an element of a set whose parent is itself. It is unique per set. $a$ is the root element for the left disjoint set.



## Operation Make-Set

Make-Set operation creates a new set having a single element (means $size=1$) which is having a unique id.

```	
MAKE-SET(x)
{
	x.parent = x;
	x.size = 1;
}
```
Here X is the only element in the set so it is parent of itself.

We are working with arrays, so the code to make $n$ sets is as below:

```c++
vector<int> parent,size;
void Make_sets(int n)
{
	parent.resize(n);
	size.resize(n);
	for(int i = 0; i < n; i++)
	{
		parent[i] = i;
		size[i] = 1;
	}
}
```

**Time Complexity:** Make-Set operation take $O(1)$ time. So creating $N$ sets it will take $O(N)$ time.

## Operation Find

$Find(X)$ basically finds the root element of the disjoint set to which $X$ belongs. 

IMAGE

Here the thing to note is that, the root element of a root element of any disjoint set is itself i.e., $root.parent = root$

**Algorithm**

Until you reach at the root element, traverse the tree of the disjoint set upwards.

```
FIND(X)
	while x != x.parent
		x = x.parent
		
	return x;
```
**Visualization**

---------------
### Quiz Time

Can you find the recursive implementation of the above function?

Answer:
```
FIND(x)
	if x == x.parent
		return x
	else
		return FIND(x.parent) 
```
------------------

**Implementation in C++**
```c++
// Iterative implementation
int Find(x)
{
	while(x != parent[x])
		x = parent[x];
	return x;
}

// Recursive implementation
int Find(x)
{
	if(x == parent[x])
		return x;
	else
		return Find(parent[x]);
}
```
**Time Complexity:** This operation can take $O(N)$ in worst case where N is the size of the set-which can be number of total elements at maximum.

This is too much. Right? What can we do?

We have a technique named **"Path compression"**, which burns this time to $O(logN)$ on average. Note the term **on average**. 

The idea of the Path compression is: **It re-connects every vertex to the root vertex directly rather than by a path**.

Image

How can we do it? It is easy, we just need a little modification in $Find(X)$.
```
FIND(x)
	if x == x.parent
		return x
	else 
		x.parent = FIND(x.parent);
		return x.parent
```
So every time we run this function, it will re-connect every vertex on the path to the root, directly to root.

---
### Quiz Time

Can you write the iterative version of the above $FIND(X)$ function with path compression?

Answer:
```
FIND(x)
	y = x

	while y != y.parent
		y = y.parent
	
	while x != x.parent
		z = x.parent;
		x.parent = y
		x = z
		
```
----

**Implementation in C++**
```c++
// Iterative Implementation
int Find(x)
{
	int y = x;
	while(y != parent[y])
		y = parent[y];
	
	int parent;
	
	while(x != parent[x])
	{
		parent = parent[x];
		parent[x] = y;
		x = parent;
	}
	
	return x;
}

// Recursive implementation
int Find(x)
{
	if(x == parent[x])
		return x;
	else
		return parent[x] = Find(parent[x]);
}
```

## Operation Union
$Union(X,Y)$ operation first of all finds root element of both the disjoint sets containing X and Y respectively. Then it connects the root element of one of the disjoint set to the another.

Well, how do we decide which root will connet to which? If we do it randomly then it may increase the tree height up to O(N), which means that the next $Find(x)$ operation will take O(N) time. Can we do better?

Yes, we have two standard techniques: **By size and By rank**.

### By Size
Union by size technique decides it based on the sizes of the sets. Everytime, the smaller size set is attatched to the larger size set.

```
UNION(X,Y)
	Rx = FIND(X), Ry = FIND(Y)

	if Rx == Ry
		return
	if Rx.size > Ry.size
		Ry.parent = Rx
		Rx.size = Rx.size + Ry.size
	else 
		Rx.parent = Ry
		Ry.size = Ry.size + Rx.size
```

### By Rank
In Union by rank technique, shorter tree is attatched to taller tree. Initally rank of each disjoint set is zero. 

If both sets have same rank, then the resulting rank will be one greater. Otherwise the resulting rank will be larger of the two.

```
UNION(X,Y)
	Rx = FIND(X), Ry = FIND(Y)

	if Rx == Ry
		return
	if Rx.rank > Ry.rank
		Ry.parent = Rx
		if Rx.rank == Ry.rank
			Rx.rank = Rx.rank + 1
	else 
		Rx.parent = Ry
		if Rx.rank == Ry.rank
			Ry.rank = Ry.rank + 1
```

**Implementation in c++**
```c++
// By size
void union(int x,int y)
{
	int Rx = find(x), Ry = find(y);
	
	if(Rx == Ry)
		return;
		
	if(size[Ry] > size[Rx])
		swap(Rx,Ry);
	
	parent[Ry] = Rx;
	size[Rx] += size[Ry];
		
}

// By Rank
void union(int x,int y)
{
	int Rx = find(x), Ry = find(y);
	
	if(Rx == Ry)
		return;
		
	if(rank[Ry] > rank[Rx])
		swap(Rx,Ry);
	
	parent[Ry] = Rx;
	
	if(rank[Rx] == rank[Ry])
		rank[Rx] += 1;

}
```

**Time Complexity of Union**

 1. Without path compression: $O(N)$
 2. With path compression: $O(logN)$ on an average

## Applications of DSU

 1. To keep track of connected components in an undirected graph.
 2. In Kruskal's and Boruvka's algorithm to find minimum spanning tree.
