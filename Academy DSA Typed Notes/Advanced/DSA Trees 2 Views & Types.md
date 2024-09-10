# Advanced DSA : Trees 2: Views & Types


## Problem 1 Level order traversal

### Level Order Traversal
Input: 1, 2, 3, 5, 8, 10, 13, 6, 9, 7, 4, 12, 11.

The diagram for the following nodes will be:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/528/original/EBDvTnv.jpg?1697189390" width=300 />


```cpp
1
2  3
5  8  10  13
6  9  7  4
12  11
```


---



### Question
Will the last level node always be a leaf node?

### Choices
- [x] YES
- [ ] NO
- [ ] Cant say


### Explanation

In a binary tree, the last level nodes are typically the leaf nodes. A leaf node is defined as a node that does not have any children. Since the last level of a binary tree is the lowest level, the nodes at this level do not have any child nodes, making them leaf nodes.

Thus, the correct answer is "YES" because in a well-formed binary tree, the nodes at the last level will always be leaf nodes, as they cannot have any children further down the tree. 


---



### Question
Which traversal is best to print the nodes from top to bottom?

### Choices
- [x] Level order traversal
- [ ] Pre order 
- [ ] post order



### Explanation:

When you want to print nodes from top to bottom, the level-order traversal, also known as Breadth-First Search (BFS), is the best choice. Level-order traversal ensures that nodes at the same level are processed before moving to the next level. This results in a top-to-bottom exploration of the tree.

---
## Level order traversal Observations


### Observations:
* Level order traversal visits nodes level by level, starting from the root.
* It uses a queue to keep track of the nodes to be processed.
* Nodes at the same level are processed before moving on to the next level.
* This traversal ensures that nodes at higher levels are visited before nodes at lower levels.

Since this will be done level by level hence we will be requiring a queue data structure to solve this problem:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/529/original/Wf3Hhch.png?1697189478" width=400/>

After the whole process the queue data strucutre will look somewhat like this:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/530/original/8VJIelj.png?1697189508" width=400/>

Like this(in theabove example) it will be done for all of the nodes. 
Let us see the pseudocde to solve the problem in printing in one line only:

### Pseudocode:

```cpp
q.enqueue(root)
{
    while(not q.empty())
    {
        x = q.dequeue()
        print(x.data)
        if(x.left != null) q.enqueue(x.left)
        if(x.right != null) q.enqueue(x.right)
    }
}
```
Each level will be printed in seperate line:
```cpp
1
2  3
5  8  10  13
6  9  7  4
12  11
```


### Observations:

* Level order traversal prints nodes at the same depth before moving to the next level, ensuring that nodes on the same level are printed on separate lines.

### Approach:
1. Start with the root node and enqueue it.
2.  Initialize last as the root.
3.  While the queue is not empty:
    * Dequeue a node, print its data.
    * Enqueue its children (if any).
    * If the dequeued node is the same as last, print a newline and update last.

### Dry-Run:
```cpp
        1
       / \
      2   3
     / \
    4   5
```
* Enqueue root node 1 and initialize last as 1.
* Dequeue 1 and print it. Enqueue its children 2 and 3.
* Dequeue 2 and print it. Enqueue its children 4 and 5.
* Dequeue 3 and print it. Since 3 is the last node in the current level, print a newline.
* Dequeue 4 and print it. There are no children to enqueue for 4.
* Dequeue 5 and print it. There are no children to enqueue for 5.

**Final Output:**
```plaintext
1
2
3
4
5
```



Let us see the pseudocode to solve the problem in printing in **seperate** line only:

### Pseudocode:

```cpp
q.enqueue(root)
{
    last = root;
    while(!q.empty())
    {
        x.dequeue()
        print(x.data)
        if(x.left != null) q.enqueue(x.left)
        if(x.right != null) q.enqueue(x.right)
        if(x == last && !q.empty())
        {
            print("\n");
            last = q.rear();
        }
    }
}
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)

---
## Problem 2 Right and left view 


### Print right view of a binary tree:

### Example:
Let us see an example below: 
```cpp
        1
       / \
      2   3
     / \   \
    4   5   6
             \
              7
```
The right view of this tree would be [1, 3, 6, 7] when viewed from the right side.

To solve this we need to print last node of every level.


---
### Question
Print right view of the given binary tree,

```cpp
        1
       / \
      2   3
       \   \
        5   6
           / \
          8   7
         / \ 
        9   10
```

### Choices
- [ ] [1, 3, 6, 7]
- [ ] [1, 3, 6, 8, 9]
- [ ] [1, 3, 6, 7, 8, 9, 10]
- [x] [1, 3, 6, 7, 10]
- [ ] [1, 2, 5]


---
## Right view  Observations


### Observations/Idea

* The idea behind obtaining the right view of a binary tree is to perform a level-order traversal, and for each level, identify and print the rightmost node. This process ensures that we capture the rightmost nodes at each level, giving us the right view of the binary tree. We can obtain the right-view of the tree using a breadth-first level-order traversal with a queue and a loop. 


### Approach:
1. Initialize an empty queue for level order traversal and enqueue the root node.
2. While the queue is not empty, do the following:
    * Get the number of nodes at the current level (levelSize) by checking the queue's size.
    * Iterate through the nodes at the current level.
    * If the current node is the rightmost node at the current level, print its value.
    * Enqueue the left and right children of the current node if they exist.
    * Repeat this process until the queue is empty.

Let us see the pseudocode to solve the problem:

### Pseudocode:
```cpp
q.enqueue(root)
last = root;
while(!q.empty(1))
{
    x = q.dequeue()
    if(x.left != null) q.enqueue(x.left)
    if(x.right != null) q.enqueue(x.right)
    if(x == last) { 
        print(x.data)
        if(!q.empty())
        {
            print("\n");
            last = q.rear();
        }

    }
}
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(M)

---
## Types of binary tree



1. **Proper Binary Tree (Strict Binary Tree):**
Every node has either 0 or 2 children (never 1 child).
Diagram:
```cpp
    A
  /   \
 B     C
/ \   / \
```
2. **Complete Binary Tree:**
All levels are filled except possibly the last level, which is filled left to right.
Diagram:
```cpp
    A
  /   \
 B     C
/ \   /
```
3. **Perfect Binary Tree:**
All internal nodes have exactly two children, and all leaf nodes are at the same level.
Diagram:
```cpp
    A
  /   \
 B     C
/ \   / \
```


---



### Question
Perfect Binary Trees are also:

### Choices
- [ ] Proper binary tree
- [ ] Complete binary tree
- [x] both
- [ ] none

### Explanation:

A perfect binary tree is a specialized case of both a proper binary tree and a complete binary tree, where all internal nodes have two children, all leaf nodes are at the same level, and all levels are completely filled.

---
## Problem 3 Check height balanced tree


### Definition
For all nodes if(`height_ofleftchild-height_ofrightchild`) <= 1

### Example:
```cpp
        1
       / \
      2   3
     / \
    4   5
   /
  6
```
This tree is not height-balanced because the left subtree of node 2 has a height of 3, while the right subtree of node 2 has a height of 0, and the difference is greater than 1.

### Brute Force
### Approach
* For each node in the binary tree, calculate the height of its left and right subtrees.
* Check if the absolute difference between the heights of the left and right subtrees for each node is less than or equal to 1.
* If step 2 is true for all nodes in the tree, the tree is height-balanced.


### Pseudocode:
```cpp
// Helper function to calculate the height of a tree
function calculateHeight(root):
    if root is null:
        return -1
    return 1 + max(calculateHeight(root.left), calculateHeight(root.right))

function isHeightBalanced(node):
    if node is null:
        return true  // An empty tree is height-balanced

    // Check if the current node's subtrees are height-balanced
    leftHeight = calculateHeight(node.left)
    rightHeight = calculateHeight(node.right)

    // Check if the current node is height-balanced
    if abs(leftHeight - rightHeight) > 1:
        return false

    // Recursively check the left and right subtrees
    return isHeightBalanced(node.left) && isHeightBalanced(node.right)

// Example usage:
root = buildTree()  // Build your binary tree
result = isHeightBalanced(root)
```

> NOTE: For a null node: **height = -1**


### Complexity
**Time Complexity:** $O(N^2)$
**Space Complexity:** O(N)

---


### Question
Which traversal is best to use when finding the height of the tree?

### Choices
- [ ] Level order
- [ ] Inorder
- [x] postorder
- [ ] preorder


### Explanation: 

Postorder traversal works best for calculating the height of a tree because it considers the height of subtrees before calculating the height of parent nodes, which mirrors the hierarchical nature of tree height calculation.

---
## Check height balanced tree Optimised Approach


### Observation/Idea:
* To solve the problem of determining whether a binary tree is height-balanced we can consider using a recursive approach where you calculate the height of left and right subtrees and check their balance condition at each step. Keep track of a boolean flag to indicate whether the tree is still balanced.

### Approach:
* We use a helper function height(root) to calculate the height of each subtree starting from the root.
* In the height function:
* If the root is null (i.e., an empty subtree), we return -1 to indicate a height of -1.
* We recursively calculate the heights of the left and right subtrees using the height function.
* We check if the absolute difference between the left and right subtree heights is greater than 1. If it is, we set the ishb flag to false, indicating that the tree is not height-balanced.
* We return the maximum of the left and right subtree heights plus 1, which represents the height of the current subtree.
* The ishb flag is initially set to true, and we start the height calculation from the root of the tree.
* If, at any point, the ishb flag becomes false, we know that the tree is not height-balanced, and we can stop further calculations.
* After the traversal is complete, if the ishb flag is still true, the tree is height-balanced.

### Example:
```cpp
        1
       / \
      2   3
     / \
    4   5
```
This tree is height-balanced because the height of the left and right subtrees of every node differs by at most 1.

### Pseudocode
```cpp
function height(root, ishb)
{
    if(root == null) return -1;
    l = height(root.left)
    r = height(root.right)
    if( absolute(l - r) > 1) ishb = false;
    return max(l, r) + 1
}
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(log N)

---
## Problem 4 Construct binary tree


### Construct binary tree from inorder and post order

Constructing a binary tree from its inorder and postorder traversals involves a recursive process. Here's a brief explanation with an example:

### Brute-Force Approach

### Approach:

* Generate all possible permutations of the given inorder traversal.
* For each permutation, check if it forms a valid binary tree when combined with the given postorder traversal.
* Return the first valid binary tree found.

### Example:
Inorder: [4, 2, 7, 5, 1, 3, 6]
Postorder: [4, 7, 5, 2, 6, 3, 1]

### Dry-Run:
* Identify the root: In the postorder traversal, the last element is 1, which is the root of the binary tree.
* Split into left and right subtrees: In the inorder traversal, find the position of the root element (1). Elements to the left of this position represent the left subtree, and elements to the right represent the right subtree.
* Recurse on left subtree: For the left subtree, the root is 2 (found in postorder traversal). Split the left subtree's inorder and postorder traversals, and repeat the process.
* Recurse on right subtree: For the right subtree, the root is 3 (found in postorder traversal). Split the right subtree's inorder and postorder traversals, and repeat the process.
* Continue the recursion: Repeat steps 3 and 4 for each subtree until the entire binary tree is constructed.


### Pseudocode:
```cpp
function buildTreeBruteForce(inorder, postorder):
    for each permutation of inorder:
        if formsValidBinaryTree(permutation, postorder):
            return constructBinaryTree(permutation, postorder)
    return null
```
* **TC-** O(N! * N)
* **SC-** O(N)

---
## Construct binary tree Most Optimised Approach

### Most-Optimised Approach:

* The last element in the postorder traversal is the root of the binary tree.
* Find the root element in the inorder traversal to determine the left and right subtrees.
* Recursively repeat the process for the left and right subtrees.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/527/original/M1IKDA8.png?1697188735"/>

Now as we can see in the above image let us understand this with the help of a dry/run:
### Dry-Run/Example:
inorder={4,2,7,5,1,3,6} and postorder={4,7,5,2,6,3,1} 

1. The last element in the postorder traversal is 1, which is the root of the binary tree.

Binary Tree:
```plaintext
1
```
2. Find 1 in the inorder traversal to split it into left and right subtrees. The elements to the left are the left subtree, and the elements to the right are the right subtree.

```cpp
Inorder: [4,2,7,5,1,3,6]
Postorder: [4,7,5,2,6,3,1]
```

Left Subtree (Inorder: [4,2,7,5], Postorder: [4,7,5,2]):

```cpp
  1
 /
2
 \
  5
 / \
4   7
```
Right Subtree (Inorder: [3,6], Postorder: [6,3]):

```cpp
6
 \
  3
```
3. Repeat the process for the left and right subtrees:

For the left subtree:
* The last element in the postorder traversal is 2, which is the root of the left subtree.
* Find 2 in the inorder traversal to split it into left and right subtrees.
* Left Subtree (Inorder: [4], Postorder: [4]):
```cpp
  2
 /
4
```
Right Subtree (Inorder: [7,5], Postorder: [7,5]):
```cpp
  5
 /
7
```
For the right subtree:

* The last element in the postorder traversal is 3, which is the root of the right subtree.
* Find 3 in the inorder traversal to split it into left and right subtrees.
* Left Subtree (Inorder: [6], Postorder: [6]):
```cpp
  3
   \
    6
```

The final binary tree would look like this:
```cpp
         1
        / \
       2   3
      / \   \
     4   5   6
        /
       7
```

---

### Question
The inorder traversal sequence `[4, 2, 5, 1, 6, 3]` and the postorder traversal sequence `[4, 5, 2, 6, 3, 1]`. What is the root of the binary tree?

### Choices
- [x] 1
- [ ] 2
- [ ] 3
- [ ] 4

### Explanation:

In postorder traversal, the last element is always the root of the tree, so here, 1 is the root. 

---
## Construct binary tree Pseudocode

### Pseudocode:
* rootIndex is the index of the root value in the inorder array.
* rootIndex + 1 represents the start of the right subtree in the arrays.
* end represents the end of the right subtree in the arrays.
* start represents the start of the left subtree in the arrays.
* rootIndex - 1 represents the end of the left subtree in the arrays.
```cpp
function buildTree(inorder, postorder):
    if postorder is empty:
        return null

    // The last element in postorder is the root of the current subtree
    rootValue = postorder.last
    root = new TreeNode(rootValue)

    // Find the index of the rootValue in inorder to split it into left and right subtrees
    rootIndex = indexOf(inorder, rootValue)

    // Recursive call for right subtree
    root.right = buildTree(subarray(inorder, rootIndex + 1, end), subarray(postorder, rootIndex, end - 1))
    
    // Recursive call for left subtree
    root.left = buildTree(subarray(inorder, start, rootIndex - 1), subarray(postorder, start, rootIndex - 1))

    return root
```

**TC-O(N)
SC-O(N)**
