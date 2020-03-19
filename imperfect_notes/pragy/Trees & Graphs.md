Trees and Graphs
----------------

**Graph:**
- nodes
- edges: pairs of nodes that are connected
- directed/undirected
- weighted/unweighted

**Trees:**
- graphs with constraints
- connected
- acyclic
- rooted - contrast with graph
- node has 0 or more children
- node with 0 children is leaf
- node with 1 or more children is non-leaf
- each node has a parent - except for the root
- so, n-1 edges
- since we can make levels, it is a hierarchical DS


**K-ary Tree:**
- node can have at most k children


-- --


Binary Trees
------------

```
    o
   / \
  o   o
   \  |\
    o o o
```

- Each node has exactly 1 parent (except root)
- Each node has at most 2 children

```python
Node:
    value
    Node left_child
    Node right_child
    # typically, we also keep track of parent
    Node parent
```

- Full BT - $2^{l+1} - 1$ nodes, if $l$ levels
- Complete BT - full on penultimate level. Nodes in last level fill from the left
- BST
- Balanced Tree
- ...


-- --


Traversals
---------
- DFS:
    ```
          o
       /     \
    [LST]   [RST]
    Left and Right subtrees
    ```
    - preorder: whatever operation, do on the node first, then LST, then RST
    - inorder: LST, Node, RST
    - postorder: LST, RST, Node
    - Recursive:
        ```python
        def preorder(node):
            if node is null:
                return
            func(node)  # print
            preorder(node.left)
            preorder(node.right)
        ```
    - Iterative:
        - show how the recursion works using a call stack
        - so, use a stack - just remember the order to push nodes in


- level-order / bfs



-- --



Zig Zag traversal
-----------------
```
   4
 6   8
1 3 2 5
========
4 | 8 6 | 1 3 2 5
```

```python
def zigzag(A):
    queue = [A]
    result = []
    level = 0
    while queue:
        n = len(queue)
        vals = [x.val for x in queue]
        if level % 2 == 1:
            vals = vals[::-1]
        result.append(vals)
        for i in range(n):
            item = queue.pop()
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        level += 1
    return result
```


-- --


Vertical traversal
------------------
```
  4
 6 8
1 3 5
=====
1 | 6 | 4 3 | 8 | 5 

If two children, put them in any order
```

store dict of lists of distance from mid
move left = distance - 1
move left = distance + 1


-- --


Tree from Inorder + Preorder
----------------------------

> Given Preporder and Inorder traversals of a Binary Tree, create the tree 

- first element of preorder is the Root
- Find root in In-order traversal. Everything on left is in the LST and everything to the right is in the RST
- Recurse

```python
def build(inorder, preorder, in_start, in_end):
    if in_start > in_end:
        return None
    node = Node(preorder[pre_index])
    pre_index += 1
    if in_start == in_end :
        return node

    inIndex = search(inorder, in_start, in_end, node.data)
    node.left = build(inorder, preorder, in_start, inIndex-1)
    node.right = build(inorder, preorder, inIndex + 1, in_end)
    return node

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i

inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
pre_index = 0
root = build(inorder, preorder, 0, len(inorder) - 1)

```

- search can be made $O(1)$ or $O(\log n)$ by storing in hashmap

-- --



Check Valid Traversals
----------------------

> Given Preorder, Inorder and Postorder, check if they represent the same tree

- Use any pair with inorder to create the tree. Then check the remaining order by traversing the tree



-- --



Check Balanced
----------------

> Given Tree, check if balanced
> $$\Bigl | h(\text{left}) - h(\text{right}) \Bigr | \leq c$$
> Holds true for all nodes

```python
def check(node):
    if node is null:
        return 0
    left_height, left_balanced = check(node.left)
    right_height, right_balanced = check(node.right)
    height = 1 + max(left_height, right_height)
    balanced = abs(left_height - right_height) < 1
                and left_balanced
                and right_balanced
    return height, balanced
```
