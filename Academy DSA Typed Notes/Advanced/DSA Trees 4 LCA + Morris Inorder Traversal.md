# Advanced DSA : Trees 4: LCA


## Agenda

1. Kth smallest element in BST
2. Node to Root Path in a given Tree
3. LCA in Binary Tree
4. LCA in Binary Search Tree


---
## Problem 1 Finding the kth Smallest Element in a Binary Search Tree


### Problem Statement

Given a Binary Search Tree and a positive integer k, find the kth smallest element in the BST.

### Approach 1

We can use inorder traversal and store elements in an array, then return (k-1)th element.
**T.C:** O(N)
**S.C:** O(N)

### Approach 2
The **`Inorder Traversal`** of a BST visits the nodes in ascending order. Therefore, by performing an inorder traversal and keeping track of the count of visited nodes, we can identify the kth smallest element when the count matches k. Basically instead of storing elements, we can just keep the track of count.
**T.C:** O(N)
**S.C:** O(Height)

```cpp
count = 0;
result = -infinity;
function inorderTraversal(Node node, k) {
    if (node == null) {
        return;
    }

    // Traverse the left subtree
    inorderTraversal(node.left, k);

    // Increment count for each node visited
    count++;

    // If count equals k, we've found the kth smallest element
    if (count == k) {
        result = node.val;
        return; // Stop the traversal
    }

    // Only proceed to the right subtree if we haven't found the kth smallest element
    if (result == -infinity) {
        inorderTraversal(node.right, k);
    }
}

//Once "inorderTraversal" function completes, "result" variable shall hold the answer. 
```

---
## Problem 2 Morris Traversal


### Introduction:
Morris Traversal is a clever method used to walk through binary trees without needing extra memory structures like stacks or queues. This technique not only saves memory but also provides an interesting way to explore trees.

### Idea:

Morris Traversal works by making use of the empty spaces in the tree's structure to create temporary links between nodes. This process threads the tree, allowing traversal without relying on recursion or additional memory.


### In-Order Morris Traversal Dry Run:

Lets take an Example and understand the traversal better.

To Perform Inorder traversal,  We need to visit **Left-Data-Right**

![image](https://hackmd.io/_uploads/ryRVTEKmA.png)

The root 6 has no left child, So `print 6`, then move towards the right child.

From node 8, it has no left child, So `print 8`, then move to the right child.

On 29, there is a left child. So the left subtree needs to be visited before 29.

> The Problem here is "If we go to the left node, do we have a way to come to 29 ?"

                > During recursion, we recusively call the function, once the function call is over, then we will move back to the root, using the stack memory.
> While print 6 and moving to 8,  We know that, we dont need to visit 6 again, But on 29, we need to come back.

So we need to secure a way to come back.

Now focus on this particular tree alone, and find the last node to be visited during the In-order traversal.

![image](https://hackmd.io/_uploads/By4alrKQA.png)


That is 25.  So, Before moving to 20, we will secure a way, from 25 to the current node 29, like the below.

![image](https://hackmd.io/_uploads/By6ZWrYQA.png)

After making the connecting, move to 20.

Now, 20 has a left child.  So before printing 20, need to visit the left node. 

![image](https://hackmd.io/_uploads/HkXAWSFX0.png)


> Lets ask the same question here as well, "If we go to the left node, do we have a way to come to 20 ?"
> No, So lets do the same process, Connect the Last node of the inorder traversal to the current node like the below

![image](https://hackmd.io/_uploads/HyHnWBt7R.png)


The same process for the node 5 as well.
![image](https://hackmd.io/_uploads/Sy_QzrFmR.png)


On node 9, there is no left child,  `print 9` then move to right child.

On node 10, there is no left child,  `print 10` then move to right child.

On node 13, there is no left child,  `print 13` then move to right child.

> Here is the main catch, Visually we can see that we are visiting 5 for the second time, But how do we realise programically ? 

lets do the same process, and see how it works,

> 5 has left child, so need to visit its left child, before printing 5. need to secure a path from the last node of the inorder traversal of the left subtree. 
> Here is the main thing we can notice, when trying to make a connection, there is connection which is already established.  

`This is how, we can figure out the left subtree is already visited`

> After this, we will break the connection which we used to come back.

![image](https://hackmd.io/_uploads/rkWKarYQA.png)


The same process goes for the rest of the nodes as well!

![image](https://hackmd.io/_uploads/Sk4j-LYm0.png)


### Pseudocode:

```java
function morrisInOrderTraversal(root):
    current = root
    while current is not null:
        if current.left is null:
            print current.value
            current = current.right
        else:
            pre = current.left
            while pre.right is not null and pre.right != current:
                pre = pre.right
            if pre.right is null:
                pre.right = current
                current = current.left
            else:
                pre.right = null
                print current.value
                current = current.right
```


### Analysis:
Morris Traversal eliminates the need for an explicit stack, leading to a constant space complexity of $O(1)$. The time complexity for traversing the entire tree remains $O(n)$, where n is the number of nodes.

---


###  Question
What is the primary advantage of Morris Traversal for binary trees?
### Choices
- [ ] It uses an auxiliary stack to save memory.
- [ ] It allows for traversal in reverse order (right-to-left).
- [x] It achieves memory-efficient traversal without using additional data structures.



---
## We are all connected


### Problem Statement
It is said that we all **humans** are related through some **common ancestor** at some point of time. Assume that a person can have **0, 1 or 2** **children** **only**. 

Given the Binary tree **A** representing the family tree, discover the earliest common family member who connects two given people **B and C** in a family tree.

### Example
```java
       Ram
      /   \
  Shyam    Bob
   /   \      \
Dholu  Bholu   Satish

-> Find LCA of Dholu and Bob
-> Answer = Ram
```

### Simplified Problem
Let's simplify the problem where we are only working with numbers and let's formally define the problem statement.

---
## Problem 3 LCA 


The LCA is a crucial concept with applications in genealogy research, network routing, and more. Let's explore the intricacies of finding the LCA in a binary tree.

### Approach:
To find the LCA of two nodes in a binary tree, we'll utilize a recursive approach that capitalizes on the tree's structure. The LCA is the deepest node that has one of the nodes in its left subtree and the other node in its right subtree.

### Recursive Algorithm for LCA:

* Start at the root of the binary tree.
* If the root is null or matches either of the target nodes, return the root as the LCA.
* Recursively search for the target nodes in the left and right subtrees of the current root.
* If both target nodes are found in different subtrees, the current root is the LCA.
* If only one target node is found, return that node as the LCA.
* If both target nodes are found in the same subtree, continue the search in that subtree.


### Example:
```java
         1
        / \
       2   3
      / \
     4   5
    / \
   6   7
  ```
**LCA of nodes 6 and 3 is node 1.**
1. Start at the root (1).
2. Check for nodes 6 and 3 in the subtree rooted at 1.
3. Recursively search the left subtree (2).
4. Continue searching left (4).
5. Continue searching left (6).
6. Found node 6, but not node 3 in the left subtree.
7. Go back to node 4 and check the right subtree (null).
8. Go back to node 2 and check the right subtree (5).
9. Continue searching right (5).
10. Not found node 6 in the right subtree.
11. Go back to node 2 and check for nodes 6 and 3.
12. Found node 6 in the left subtree.
13. Return node 2 as the Lowest Common Ancestor (LCA).


### Pseudocode Example:

```java
function findLCA(root, node1, node2):
    # Base case: if root is null or matches either of the nodes, return root
    if root is null or root == node1 or root == node2:
        return root
    
    # Recursively search for the target nodes in the left and right subtrees
    left_lca = findLCA(root.left, node1, node2)
    right_lca = findLCA(root.right, node1, node2)
    
    # Determine the LCA based on the search results
    if left_lca and right_lca:
        return root  # Current root is the LCA
    if left_lca:
        return left_lca  # LCA found in the left subtree
    return right_lca  # LCA found in the right subtree
```

### Analysis:
The time complexity of finding the LCA in a binary tree using this recursive approach is O(n), where n is the number of nodes in the tree. The space complexity is determined by the depth of the recursion stack.

---
## Problem 4 Lowest Common Ancestor (LCA) in a Binary Search Tree (BST)


### Introduction:
Hello, everyone! Today, we're going to explore a specialized case of finding the Lowest Common Ancestor (LCA) in a data structure known as a Binary Search Tree (BST). The LCA operation is essential for understanding relationships between nodes in a tree, and in a BST, it becomes even more efficient due to the inherent properties of the structure. Let's dive into the process of finding the LCA in a BST.

### Approach:
To find the LCA of two nodes in a Binary Search Tree, we'll utilize the properties of BSTs that make traversal and comparison more efficient.

### Algorithm for Finding LCA in a BST:

* Start at the root of the BST.
* Compare the values of the root node, node1, and node2.
* If both nodes are smaller than the root's value, move to the left subtree.
* If both nodes are larger than the root's value, move to the right subtree.
* If one node is smaller and the other is larger than the root's value, or if either node matches the root's value, the root is the LCA.
* Repeat steps 2-5 in the chosen subtree until the LCA is found.

### Example: Finding LCA in a Binary Search Tree

**BST:**
```java
       8
        / \
       3   10
      / \    \
     1   6    14
        / \   /
       4   7  13
```
Let's find the LCA of nodes 4 and 7 in this BST:

- **Step 1:**
    1. Start at the root, which is node 8.
    2. Compare node 4 and node 7 with the current node's value (8).
    3. Both are smaller, so move to the left subtree (node 3).

- **Step 2:**
    1. Move to node 3.
    2. Compare node 4 and node 7 with the current node's value (3).
    3. Both are larger, so move to the right subtree (node 6).

- **Step 3:**
    1. Move to node 6.
    2. Compare node 4 and node 7 with the current node's value (6).
    3. Node 4 is smaller, and node 7 is larger.
    4. The current node (6) is the LCA of nodes 4 and 7.
    5. So, in this example, the LCA of nodes 4 and 7 in the BST is node 6.

### Pseudocode Example:

```java
function findLCA(root, node1, node2):
    if root is null:
        return null  // If the tree is empty, there's no LCA

    while root is not null:
        // If both nodes are smaller than the current node, go left
        if node1.value < root.value and node2.value < root.value:
            root = root.left
        // If both nodes are larger than the current node, go right
        else if node1.value > root.value and node2.value > root.value:
            root = root.right
        // If one node is smaller and the other is larger, or if one matches, this is the LCA
        else:
            return root

    return null  // If no LCA is found (unlikely in a valid BST)

```
### Analysis:
The time complexity of finding the LCA in a BST is O(h), where h is the height of the BST. In a balanced BST, the height is log(n), making the LCA operation highly efficient. The space complexity is determined by the depth of the recursion stack.
