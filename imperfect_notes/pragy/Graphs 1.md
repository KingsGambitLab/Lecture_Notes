Graphs 1
--------


G = (V, E)

- directed / undirected
- edge describes some relationship
- edge can have value - which can be some property of that relationship
- edit distance of pan --- pen is 1
- bi-directional: a->b implies b->a
- weighted/unweighted - when 1 property associated with edge - some number
- when all weights are same, we don't represent the weights
- ask students for examples of undirected graphs (fb friends) and directed (twitter follows / company hierarchy) and weighted graphs (city distances)

Trees vs graphs
- exactly 1 path b/w any pair of nodes in a tree
- because acyclic. If 2 paths, cycle occurs A-B-A or A-x-B-x

Simple graph
- no self loops
- no multiple edges b/w any 2 nodes
- max edges = $n \choose 2$
- such is a clique $K_{n}$


Disconnected vs Connected
connected = can go from any node to any node

a b c
a-b c

a-b-c
a-b
\c/

Connected Components
largest subgraphs which are connected

connected graph has exactly 1 connected component

directed needs strong connections to be connected
a->b is not connected
-- --

Representations
---------------

Adjacency Matrix
----------------
does path exist?

for undirected, $A$ is symmetric across the major diagonal.
Diagonal is 0 for a simple graph

Space: $O(n^2)$
Checking edge: $O(1)$

Can puts weights/cost/distance as well.

$A^n_{ij} =$ number of $k$ length walks b/w $i, j$

Adjacency List
--------------

List of lists

Space: efficient for sparse graphs
Time: $O(n)$ lookup in the worst case
$O(1)$ degree count in worst case
better if we only want to list down the neighbors

-- --

Traversals
----------

- same as for trees, just remember visited to prevent infinite loops
- start from any node - because no root
- tree defined using graph - rooted, unrooted
- BFS - $O(|V| + |E|)$


DFS using stack
- remember to keep the count of children explored and the parent, so that we can resume exploring from the next child


Check Connected
---------------

undirected - just run DFS from 1. If all visited, connected

DFS over disconnected graph - must start from all nodes one by one

BFS - 

![dc2d0b12.png](:storage/30547dac-c72e-46b3-86e3-479b31df3a42/dc2d0b12.png)

start from some node.
levels, min distance from that node

BFS for single source shortest path, when edge weights are EQUAL

Doesn't work when a-b-c < a-c

-- --

Undirected graph with weights 1 or 2
Can still NOT apply BFS

-- --

pseudo/dummy nodes
- can't always create if weights are large
- how to add them virtually? counter - inefficient
- heap - efficient

-- --

![93c9f38f.png](:storage/30547dac-c72e-46b3-86e3-479b31df3a42/93c9f38f.png)

1 = land, 0 = water
find the number of islands
diagonals allowed

find the number of connected components via DFS

![5c8b1184.png](:storage/30547dac-c72e-46b3-86e3-479b31df3a42/5c8b1184.png)
-- --

grid with 0s and 1s

capture all 0s surrounded by 1s on all 4 sides

![6f39934a.png](:storage/30547dac-c72e-46b3-86e3-479b31df3a42/6f39934a.png)

apply DFS to find components of 0s

if reaches boundary, don't capture
if not, we've surrounded, capture all

-- --

reach from source to destination

![151b8e6a.png](:storage/30547dac-c72e-46b3-86e3-479b31df3a42/151b8e6a.png)

-- --

shortest distance of all 0s from any 1

![f8a8702a.png](:storage/30547dac-c72e-46b3-86e3-479b31df3a42/f8a8702a.png)

BFS from all 1s

inspire from 1 and 2 bombs
![ad3d4993.png](:storage/30547dac-c72e-46b3-86e3-479b31df3a42/ad3d4993.png)


-- --

any shortest distance?

BFS from all 0s
or prev and find min

