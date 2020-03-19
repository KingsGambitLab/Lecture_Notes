Binary Trees 2
--------------

Lowest Common Ancestor
---------------------
> LCA(n1, n2) is the node which is accessible from both n1, n2 (while going up), and is farthest from the root
> Given a Tree and 2 nodes, find LCA
> k-ary tree


**Approach 1:**
- traverse from each node to root - bottom up
- compare the two paths from left to right
- O(n^2) time, O(n) space

**Approach 2:**
- traverse from each node to root - bottom up
- compare from root to node - top down
- O(n) time, O(n) space

**Approach 3:**
- don't store all parents. Use linked list intersection technique
- count the height of each path.
- traverse the longer path so height is same
- move up together
- stop when same node
- O(1) space



> Can't go from child to parent?
> Don't have pointers to nodee we have values which must be searched
> Distinct values

```python
def lca(key1, key2, node):
    if node.value in [key1, key2]:
        return node
    left = lca(key1, key2, node.left)
    right = lca(key1, key2, node.right)
    if left is not None and right is not None:
        return node
    if left is not None:
        return left
    if right is not None:
        return right
    return None
    
lca(key1, key2, root)
```


-- --

Isomorphism
-----------

> Rotate tree to reach another row


```python
def isomorphic(node1, node2):
    if node1 != node2:
        return False
        
    # binary
    if isomorphic(node1.left, node2.left) and isomorphic(node1.right, node2.right):
        return True
    if isomorphic(node1.left, node2.right) and isomorphic(node1.right, node2.left):
        return True
    return False
    # O(n). Each node visited at most twice
    
    # k-ary
    for children1 in permute(node1.children):
        for children2 in permute(node2.children):
            passed = True
            for c1, c2 in zip(children1, children2):
                if not isomorphic(c1, c2):
                    passed = False
                    break
            if passed:
                return True
    return False
    
    # sort tree in level order recursively first, then compare
```

-- --

Longest Increasing Consequtive Sequence
--------------------------------------------------

> has to be top-down
> has to be connected
> has to be continuous (1-2-3 is okay, 1-3-5 is not)
> 

- recursive
- func returns length of the LICS at node
- find LICS of left and right
- if left = node + 1, then LICS+1
- max of left, right

-- --


Create Next Pointers with O(1) space
------------------------------------

- Simple using O(n) space. Just do level order traversal
- can't use recursion either, because have to maintain call stack, which is O(h)
- todo


```python
level_start = root

while level_start:
    cur = level_start
    while cur is not None:
        if cur.left:
            if cur.right:
                cur.left.next = cur.right
            else:
                cur.left.next = get_next_child(cur)
        if cur.right:
            cur.right.next = get_next_child(cur)
            
        cur = cur.next
    if level_start.left:
        level_start = level_start.left
    elif level_start.right:
        level_start = level_start.right
    else:
        level_start = None

def get_next_child(node):
    iterate to get the child, till children exist
    if not, then move to node.next
    guaranteed to have precomputed the next

```

-- --

Boundary of tree
----------------


Tree of same sum
----------------

-- --

> Why cant decide tree using pre+post order? why need inorder?

inorder:    lst root  rst
preorder:  root  lst  rst
postorder:  lst  rst root

if just have preorder+postorder, can't separate lst-rst

