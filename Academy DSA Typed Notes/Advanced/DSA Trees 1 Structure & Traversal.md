# Trees 1: Structure & Traversal

## Revision Quizzes

### Question
Which of the following scenarios is an example of a queue?


### Choices

- [ ] A stack of books
- [ ] Undo operation in a text editor
- [x] People standing in line at a ticket counter
- [ ] A recursive function call stack
 
---


### Question
Which of the following is a more efficient strategy for implementing a queue using a linked list?

### Choices
- [ ] Insert at head and delete at head.
- [ ] Insert at head and delete at tail.
- [ ] Insert and delete at tail.
- [x] Insert at tail and delete at head.

---

## What is a tree?

Till now, we have seen data structures such as Arrays, Linked Lists, Stacks, Queues... They are **Linear Data Structure** which means we can access them in sequencial order.

The other category is **Non Linear Data Structure** 

At a lot of places, you must have seen hierarchy - Family, Office, Computer File System, etc. Therefore, there arise a need to be able to store such type of data and process it.

**Tree is an example of a non/linear or hierarchical data structure.**


### Example 
Let us see the **hierachy of people in an organization**:
```sql
CEO (Chief Executive Officer)
├── CTO (Chief Technology Officer)
│   ├── Engineering Manager
│   │   ├── Software Development Team Lead
│   │   │   ├── Software Engineer
│   │   │   └── Software Engineer
│   │   └── QA Team Lead
│   │       ├── QA Engineer
│   │       └── QA Engineer
│   └── IT Manager
│       ├── IT Specialist
│       └── IT Specialist
├── CFO (Chief Financial Officer)
│   ├── Finance Manager
│   │   ├── Accountant
│   │   └── Accountant
│   └── Procurement Manager
│       ├── Procurement Officer
│       └── Procurement Officer
└── CMO (Chief Marketing Officer)
    ├── Marketing Manager
    │   ├── Marketing Specialist
    │   └── Marketing Specialist
    └── Sales Manager
        ├── Sales Representative
        └── Sales Representative
```

As we know that every tree has roots which are below the leaves but in the computer science the case is different the roots are at the top and leaves below it. 

---
### Tree naming

### Example
```sql
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
             /
            8
```
* **Node**: An element in a tree that contains data and may have child nodes connected to it. 1, 2, 3, 4, 5, 6, 7, 8.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/525/original/gHw4HO4.png?1697188175)" width=500/>


* **Root**:<br> The topmost node in a tree from which all other nodes descend. It has no parent. Node 1 is the root.
* **Parent**:<br> A node that has child nodes connected to it.  Nodes 1, 2, 3 and 7.. 
* **Child**:<br> A node that has a parent node connected to it. Nodes 2, 3, 4, 5, 6, and 7 are children.
* **Leaf**:<br> A node that has no child nodes. It's a terminal node. Nodes 4, 5, 6, and 8 are leaves.
* **Depth:**<br> The level at which a node resides in the tree. The root is at depth 0. Depth of node 1 is 0, 2 and 3 are at depth 1, 4, 5, 6, and 7 are at depth 2, and 8 is at depth 3.
* **Height:**<br> The length of the longest path from a node to a leaf. The height of the tree is the height of the root node. Height of the tree is 3, which is the number of edges from the root to a farthest leaf (8).
* **Subtree**:<br> A tree structure that is part of a larger tree. Subtree rooted at node 2 consists of nodes 2, 4, and 5.
* **Siblings**:<br> Nodes that share the same parent node. Nodes 2 and 3 are siblings.
* **Ancestor:**<br> All nodes from parent to the root node upwards are the ancestors of a node. Nodes 1, 3, 7 are ancestors of node 8.
* **Descendant**:<br> All nodes from child to the leaf node along that path. Nodes 4 and 5 are descendants of node 2.


---


### Question
Can a leaf node also be a subtree?

### Choices
- [x] YES
- [ ] NO
- [ ] Can't say


### Explanation:

Yes, a leaf node can also be considered a subtree. A subtree is a portion of a tree structure that is itself a tree.

---


### Question
Do all nodes have a parent node?

### Choices
- [ ] YES
- [x] NO
- [ ] Can't say



### Explanation:

In a tree data structure, all nodes except for the root node have a parent node.

---


### Levels of a Tree

```sql
    1            Level 0
   / \
  2   3          Level 1
 / \
4   5            Level 2
```
In this example:

* **Level 0:** Node 1 is at level 0 (root level).
* **Level 1:** Nodes 2 and 3 are at level 1.
* **Level 2:** Nodes 4 and 5 are at level 2.

---


### Question
What is the height of the leaf node in any tree?


### Choices
- [x] 0
- [ ] 1
- [ ] 2
- [ ] 3


### Explanation 

The height of a leaf node in any tree, including a binary tree, is 0. This is because the height of a node is defined as the length of the longest path from that node to a leaf node, and a leaf node is a node that doesn't have any children. Since there are no edges to traverse from a leaf node to a leaf node, the length of the path is 0.

---

### Binary Tree

A type of tree in which each node can have at most two children i.e, either 0, 1 or 2, referred to as the left child and the right child.

**Example of a binary tree:**
```sql
         10
       /    \
      5     15
     / \    / \
    3   8  12  18
```

---
## Traversals in a Tree



### How can we traverse a Tree ?

There are many ways to traverse the tree. 

**L:** Left Subtree, **R:** Right Subtree, **N:** Root Node

|   L N R   |   L R N   |   R N L   |
|:---------:|:---------:|:---------:|
| **R L N** | **N L R** | **N R L** |

Having so many traversals can be confusing and are unnecessary. Threfore, a standard has been set where first we'll always consider the Left Subtree and then the Right Subtree.
Therefore, we boil down to 3 traverals.



|   L N R   |  **Named as Inorder**  |
|:---------:|:----------------------:|
| **N L R** | **Named as Preorder**  |
| **L R N** | **Named as Postorder** |

Names are given w.r.t the position of the root node.

> There are more techniques for traversing a tree that'll be covered in next set of sessions.

### Pre-order
Pre-order traversal is a depth-first traversal technique used to visit all nodes of a binary tree in a specific order. In pre-order traversal, you start from the root node and follow these steps for each node:
1. Visit the current node.
2. Traverse the left subtree (recursively).
3. Traverse the right subtree (recursively).

**This traversal order ensures that the root node is visited before its children and the left subtree is explored before the right subtree.**

### Example:
```sql
         10
       /    \
      5     15
     / \    / \
    3   8  12  18
```
Pre-order traversal sequence: 10, 5, 3, 8, 15, 12, 18

### Pseudocode
```cpp
function preorder(root)
{
    if(root == null)
        return;
    
    print(root.data);//node
    preorder(root.left);//left
    preorder(root.right)//right
}
```
### In-order traversal
In-order traversal is another depth-first traversal technique used to visit all nodes of a binary tree, but in a specific order. In in-order traversal, you follow these steps for each node:

1. Traverse the left subtree (recursively).
2. Visit the current node.
3. Traverse the right subtree (recursively).

**This traversal order ensures that nodes are visited in ascending order if the binary tree represents a search tree.**

Here's an example of in-order traversal on a binary tree:
```cpp
         10
       /    \
      5     15
     / \    / \
    3   8  12  18
```
In-order traversal sequence: 3, 5, 8, 10, 12, 15, 18

### Pseudocode
```cpp
function inorder(root)
{
    if(root == null)
        return;
    
    inorder(root.left);//left
    print(root.data);//node
    inorder(root.right)//right
}
```
### Post-order Traversal
Post-order traversal is another depth-first traversal technique used to visit all nodes of a binary tree, but in a specific order. In post-order traversal, you follow these steps for each node:

1. Traverse the left subtree (recursively).
2. Traverse the right subtree (recursively).
3. Visit the current node.

**This traversal order ensures that nodes are visited from the bottom up, starting from the leaf nodes and moving towards the root node.**

### Example
```cpp
         10
       /    \
      5     15
     / \    / \
    3   8  12  18
```
Post-order traversal sequence: 3, 8, 5, 12, 18, 15, 10

### Pseudocode:
```cpp
function postorder(root)
{
    if(root = null ) return;
    postorder(root.left) left
    postorder(root.right) right
    print(root.data) Node
}
```

---


### Question
What is the inorder traversal sequence of the below tree?
```cpp
         1
       /    \
      2      4
     /      / \
    3      5   6
```
### Choices
- [ ] [1, 2, 3, 4, 5, 6]
- [x] [3, 2, 1, 5, 4, 6]
- [ ] [3, 2, 1, 4, 5, 6]
- [ ] [4, 5, 6, 1, 2, 3]


### Explanation 

The inorder traversal sequence is [3, 2, 1, 5, 4, 6].



---
## Iterative Inorder traversal



### Approach:
* Iterative Inorder traversal is a method to visit all the nodes in a binary tree in a specific order without using recursion. 
* In the case of Inorder traversal, you visit the nodes in the following order: left subtree, current node, right subtree. 
* Here's how you can perform an iterative Inorder traversal using a stack data structure, along with an example:

Let's say we have the following binary tree as an example:
```cpp
       1
      / \
     2   3
    / \
   4   5
```
### Dry-Run:
* Start at the root node (1).
* Push 1 onto the stack and move left to node 2.
* Push 2 onto the stack and move left to node 4.
* Push 4 onto the stack and move left; there are no left children, so pop 4, visit it, and move right (which is null).
* Pop 2, visit it, and move to its right child, node 5.
* Push 5 onto the stack and move left; there are no left children, so pop 5, visit it, and move right (which is null).
* Pop 1, visit it, and move to its right child, node 3.
* Push 3 onto the stack and move left; there are no left children, so pop 3, visit it, and move right (which is null).
* The stack is empty, and all nodes have been visited.
* So, the iterative Inorder traversal of the tree is 4, 2, 5, 1, 3.

### Need of recursion/stack:
In inorder traversal of a binary tree, you need a data structure like a stack or recursion because you need to keep track of the order in which you visit the nodes of the tree. The reason for using these techniques is to handle the backtracking that's inherent in traversing a binary tree in inorder fashion. In a binary tree's inorder traversal, you visit nodes in a specific order: left, current, right. You use a stack or recursion to remember where you left off in the tree when moving between nodes, ensuring you visit nodes in the correct order and navigate through the tree efficiently. This backtracking is essential for proper traversal.

### Pseudocode:
```cpp
cur = root;
while(cur != null || st.isempty())
{
    if(cur != null)
    {
        st.push(curr)
        cur = cur.left;
    }
    else{
        cur = st.pop();
        print(cur.data)
        cur = cur.right
    }
}
```
* **TC -** O(N)
* **SC -** O(N)


---
## Equal Tree Partition

### Problem Statement : 
Given the root of a binary tree, return ***true*** if the tree can be split into two non-empty subtrees with equal sums, or ***false*** otherwise.

### Example 1
```cpp
Input:
         5
       /   \
      3     7
     / \   / \
    4   2 6   1

Output: True                
```
### Explanation:

```cpp 
Part 1 :- 
    
    5
   / 
  3   
 / \
4   2   

Sum: 14
```

```cpp 
Part 2 :- 

   7
  /  \
 6    1

Sum: 14
```
### Example 2
```cpp
Input:
      5
     / \
    8   9
       / \
      2   3
          
Output: false                        
```
### Explanation:
There is no way to split the course into two parts with equal sums.


---


### Question
Check whether the given tree can be split into two non-empty subtrees with equal sums or not.

```cpp
       5
      / \
     10  10
    /     \
  20      3
  /
 8
```

### Choices
- [x] Yes, It is possible.
- [ ] It is impossible. 


### Explanation:

Yes It is possible to split the tree into two non-empty subtrees with sum 28.

Sub-Tree 1:
```cpp
       5
      / \
     10  10
          \
          3

```

Sub-Tree 2:
```cpp
     20
     /
    8
```


---
## Equal Tree Partition Solution


### Solution

1. **Total Sum Check**:
If the total sum of all nodes in the binary tree is odd, it is impossible to divide the tree into two subtrees with equal sums. This is because the sum of two equal values is always even, and if the total sum is odd, it cannot be divided equally into two parts.
2. **Subtree Sum Check**:
If we can find a subtree in the binary tree with a sum equal to half of the total sum, we can split the tree into two equal partitions by removing the edge leading to the root of that subtree. This means that we don't necessarily need to compare sums of all possible subtrees, but we can look for a single subtree that meets the subtree sum check condition.

### Pseudocode
```cpp
function sum(TreeNode root) {
    if (!root) {
        return 0;
    }
    return sum(root.left) + sum(root.right) + root.val;
}

function hasSubtreeWithHalfSum(TreeNode root, int totalSum) {
    if (!root) {
        return false;
    }
    
    int leftSum = sum(root.left);
    int rightSum = sum(root.right);

    if ((leftSum == totalSum / 2 || rightSum == totalSum / 2) || hasSubtreeWithHalfSum(root.left, totalSum) || hasSubtreeWithHalfSum(root.right, totalSum)) {
        return true;
    }

    return false;
}

function isEqualTreePartition(TreeNode root) {
    if (!root) {
        return false; // An empty tree cannot be partitioned
    }

    int totalSum = sum(root);

    if (totalSum % 2 == 1) {
        return false; // If the total sum is odd, partition is not possible
    }

    return hasSubtreeWithHalfSum(root, totalSum);
}
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(H)

---
## Path Sum

### Problem Statement
Given a binary tree and an integer k, determine if there exists a root-to-leaf path in the tree such that adding up all the node values along the path equals k.

Example:
```cpp 

Input:
                Binary Tree:
                       5
                      / \
                     4   8
                    /   / \
                   11  13  4
                  /  \      \
                 7    2      1

                k = 22
                           
Output: true
```
Explanation:

In the given binary tree, there exists a root-to-leaf path 5 -> 4 -> 11 -> 2 with a sum of 5 + 4 + 11 + 2 = 22, which equals k. Therefore, the function should return true.

### Solution:
* To solve this problem,we first check if the current node is a leaf node (having no left and right children) and if the current value equals k. If both conditions are met, it returns true, indicating that a valid path is found.
* If not, it recursively checks the left and right subtrees with a reduced sum (k - root->val).
* It returns true if there's a path in either the left or right subtree, indicating that a valid path is found.


### Pseudocode
```cpp 
function hasPathSum(Node root, k) {
    if (!root) {
        return false; // No path if the tree is empty
    }

    if (!root.left and !root.right) {
        return (k == root.val);
    }

    return hasPathSum(root.left, k - root.val) || hasPathSum(root.right, k - root.val);
}

```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(H)
