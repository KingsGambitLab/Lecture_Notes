# Advanced DSA : Trees 3: BST



## Binary Search Tree

Binary search tree is searching data in an organized dataset using divide and conquer. 

For a node X in a binary search tree everything on the left has data less than x and on the right greater than x.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/535/original/6mtWOem.png?1697191199" width=500/>

Example of a binary search tree:

```cpp
        5
       / \
      3   8
     /\   /\
    1  4  6 9
```

---



### Question
What is a Binary Search Tree (BST)?


### Choices
- [ ] A tree with only two nodes
- [ ] A tree where the left child of a node has a value <= the node, and the right child has a value > the node
- [x] A tree where for a node x, everything on the left has data <= x and on the right > x.
- [ ] A tree that has height log N.

---
## Problem 1 Searching in Binary Search Tree

### Searching
Searching in a Binary Search Tree (BST) involves utilizing the property that values in the left subtree are smaller and values in the right subtree are larger than the current node's value. This property allows for efficient search operations.
Here's an example using the BST diagram from earlier:
```cpp
        5
       / \
      3   8
     /\   /\
    1  4  6 9
```
**Suppose you're searching for the value 6:**

* Start at the root (value 5).
* Compare 6 with 5. Since 6 is greater, move to the right child (value 8).
* Compare 6 with 8. Since 6 is smaller, move to the left child (value 6).
* The value 6 matches the current node's value, so the search is successful.

---


### Question
What is the number of nodes you need to visit to find the number `1` in the following BST?

```cpp
        5
       / \
      3   8
     /\   /\
    1  4  6 9 
```

### Choices
- [ ] 2
- [x] 3
- [ ] 4
- [ ] 1


### Explanation
First node: 5. From 5 you move left.
Second node: 3. From 3 you move left, again.
Third node: 1. You finally get 1. 

---
## Searching in Binary Search Tree Pseudo Code

### Pseudo Code
```cpp
function search(root, target):
    if root is None:
        return None

    if root.value == target:
        return root

    if target < root.value:
        return search(root.left, target)

    if target > root.value:
        return search(root.right, target)
```


---
## Problem 2 Insertion in Binary Search Tree

### Insertion in BST:
Inserting a new value into a Binary Search Tree (BST) involves maintaining the property that values in the left subtree are smaller and values in the right subtree are larger than the current node's value.

Here's an example using the BST diagram from earlier:
```cpp
        5
       / \
      3   8
     /\   /\
    1  4  6 9 
```
**Suppose you want to insert the value 7:**

* Start at the root (value 5).
* Compare 7 with 5. Since 7 is greater, move to the right child (value 8).
* Compare 7 with 8. Since 7 is smaller, move to the left child (value 6).
* Compare 7 with 6. Since 7 is greater, move to the right child (null).
* Insert the value 7 as the right child of the node with value 6.

The updated tree after insertion:
```cpp
        5
       / \
      3   8
     /\   /\
    1  4  6 9 
           \
            7
```

### Pseudocode:
```cpp
function insert(root, value):
    if root is null:
        return createNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root
```

---


### Question
Where does the node with the smallest value resides in a BST?

### Choices
- [x] We keep on going left and we get the smallest one.
- [ ] Depends on the tree.
- [ ] We keep on going right and we get the smallest one.
- [ ] The root node.


For every node, we need to go to its left, that's the only way we can reach the smallest one.

---
## Problem 3 Find smallest in Binary Search Tree

### Problem Statement
Find smallest in Binary Search Tree

### Approach

The left most node in the tree, will be the smallest.

### Example:
Suppose we have the following BST:
```cpp
       5
      / \
     3   8
    / \   \
   2   4   9
```
To find the smallest element:

* Start at the root node (5).
* Move to the left child (3).
* Continue moving to the left child until you reach a node with no left child.
* The node with no left child is the smallest element in the BST. In this case, it's the node with the value 2.
* So, in this example, the smallest element in the BST is 2.
### Pseudocode

```cpp
temp = root// not null
while(temp.left != null)
{
    temp = temp.left
}
return temp.data;
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(1)

---
## Problem 4 Find largest in Binary Search Tree

### Approach

The right most node in the tree, will be the largest.

### Example:
Suppose we have the following BST:
```cpp
       5
      / \
     3   8
    / \   \
   2   4   9
```
* To find the largest element:
* Start at the root node (5).
* Move to the right child (8).
* Continue moving to the right child until you reach a node with no right child.
* The node with no right child is the largest element in the BST. In this case, it's the node with the value 9.
* So, in this example, the largest element in the BST is 9.

### Pseudocode

```cpp
temp = root// not null
while(temp.right != null)
{
    temp = temp.right
}
return temp.data;
```

---
## Problem 5 Deletion in Binary Search Tree


### Deletion in Binary Search Tree
Deleting a node from a Binary Search Tree (BST) involves maintaining the BST property while handling various cases depending on the node's structure. Here's how the deletion process works:

* Find the Node to Delete: Start at the root and traverse the tree to find the node you want to delete. Remember to keep track of the parent node as well.

### Case 1: Node with No Children (Leaf Node)
In this case, we have a node with no children (a leaf node). Deleting it is straightforward; we simply remove it from the tree.

**Example:**
Suppose we have the following BST, and we want to delete the node with the value 7.
```cpp
        10
       /  \
      5    15
     / \   / \
    3   7 12  18
```
After deleting the node with the value 7, the tree becomes:
```cpp
        10
       /  \
      5    15
     /    /  \
    3    12  18
```
### Case 2: Node with One Child
In this case, the node to be deleted has only one child. To delete it, we replace the node with its child.

**Example:**
Suppose we have the following BST, and we want to delete the node with the value 5.
```cpp
        10
       /  \
      5    15
     /    / \
    3    12  18
```
After deleting the node with the value 5, we replace it with its child (3):
```cpp
        10
       /  \
      3    15
          / \
        12  18
```


### Case 3: Node with Two Children
In this case, the node to be deleted has two children. To delete it, we find either the in-order predecessor or successor and replace the node's value with the value of the predecessor or successor. Then, we recursively delete the predecessor or successor.

**Example:**
Suppose we have the following BST, and we want to delete the node with the value 10 (which has two children).
```cpp
        10
       /  \
      5    15
     / \  / \
    3   9 12  18
```
To delete the node with value 10, we can either choose its in-order predecessor (9) or in-order successor (12). Let's choose the in-order predecessor (9):

* Find the in-order predecessor (the largest value in the left subtree). In this case, it's 9.
* Replace the value of the node to be deleted (10) with the value of the in-order predecessor (9).
* Recursively delete the in-order predecessor (9), which falls into either Case 1 (no children) or Case 2 (one child).
* After deleting the node with the value 10, the tree becomes:
```cpp
        9
       / \
      5   15
     /   / \
    3   12  18
```
These are the three main cases for deleting a node in a Binary Search Tree (BST). 

### Pseudo Code
Here's the pseudo code with each of the cases mentioned.


```cpp 
Node delete(Node root, int K){
    if(root == NULL) return NULL;
    
    if(root.data == K){
        if(root.left == NULL && root.right == NULL)
            return NULL;
        if(root.left || root.right){
            if(root.left == NULL) return root.right;
            if(root.right == NULL) return root.left;
        }
        
        Node temp = root.left;
        while(temp.right != NULL){
            temp = temp.right;
        }
        root.data = temp.data;
        root.left = delete(root.left, temp.data);
        return root;
    }
    else if(root.left > K){
        root.left = delete(root.left, K);
    }
    else{
        root.right = delete(root.right, K);
    }
}
```

---


### Question
What is the purpose of balancing a Binary Search Tree?
### Choices
- [ ] To make it visually appealing
- [ ] To ensure all nodes have the same value
- [x] To maintain efficient search, insert, and delete operations
- [ ] Balancing is not necessary in a Binary Search Tree

---
## Problem 6  Construct a binary search tree


### Construct BST from sorted array of unique elements:

### Approach:
* Find the middle element of the sorted array.
* Create a new node with this middle element as the root of the tree.
* Recursively repeat steps 1 and 2 for the left and right halves of the array, making the middle element of each subarray the root of its respective subtree.
* Continue this process until all elements are processed.
* The final tree will be a valid BST with the given sorted array as its inorder traversal.
* Here's an example construction of a BST using the values 8, 3, 10, 1, 6, 14, 4, 7, and 13:

### Example:
* Sorted Array - 1, 3, 4, 6, 7, 8, 10, 13, 14
* Create the root node with value 8.
* Insert 3: Move to the left child of the root (value 3).
* Insert 10: Move to the right child of the root (value 10).
* Insert 1: Move to the left child of the node with value 3 (value 1).
* Insert 6: Move to the right child of the node with value 3 (value 6).
* Insert 14: Move to the right child of the root (value 14).
* Insert 4: Move to the left child of the node with value 6 (value 4).
* Insert 7: Move to the right child of the node with value 6 (value 7).
* Insert 13: Move to the left child of the node with value 14 (value 13).
The constructed BST:
```cpp
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```


### Pseudocode:

```cpp
function insert(root, value):
    if root is null:
        return [value, null, null]
    
    if value < root[0]:
        root[1] = insert(root[1], value)
    else:
        root[2] = insert(root[2], value)
    
    return root

// Construct a BST by inserting values
root = null
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for each value in values:
    root = insert(root, value)
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(logn)

---
## Problem 7 Check if a binary tree is a binary search tree


### Check if a binary tree is a binary search tree

To check if a binary tree is a binary search tree (BST), you can perform an inorder traversal of the tree and ensure that the values encountered during the traversal are in ascending order. Here's how you can do it:

**Conditions are:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/537/original/yd0ry4C.png?1697191775" width=500/>


### Approach:
* Perform an inorder traversal of the binary tree.
* During the traversal, keep track of the previously visited node's value.
* At each step, compare the current node's value with the previously visited node's value.
* If the current node's value is less than or equal to the previously visited node's value, the tree is not a BST.
* If you complete the entire traversal without encountering any violations of the BST property, the tree is a BST.



### Example:
Suppose we have the following binary tree:
```cpp
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```
* Initialize prevValue as -∞ (negative infinity).
* Begin the inorder traversal:
* Start at the root node (4).
* Recursively traverse the left subtree (node 2).
* Check 2 > -∞, so it's okay.
* Update prevValue to 2.
* Recursively traverse the left subtree (node 1).
* Check 1 > 2. This is a violation.
* Since there's a violation, the tree is not a BST.

---


### Question
Check where the given binary tree is a Binary Search Tree.

```cpp
        5
       / \
      2   6
     / \ / \
    1  3 4  7
```

### Choices
- [ ] Yes, It is a Binary Search Tree
- [x] No, It is not a Binary Search Tree
- [ ] May be
- [ ] Not sure


---

### Explanation:

No, It is not a Binary Search Tree.

The node with the value 4 should not be on the right sub of the root node, since the root is 5, the node has to be placed on left subtree.

### Pseudocode:
```cpp
function isBST(root):
    // Initialize a variable to keep track of the previously visited node's value
    prevValue = -infinity  // A small negative value

    // Helper function for the inorder traversal
    function inorderTraversal(node):
        if node is null:
            return true  // Reached the end of the subtree, no violations

        // Recursively traverse the left subtree
        if not inorderTraversal(node.left):
            return false

        // Check if the current node's value violates the BST property
        if node.value <= prevValue:
            return false

        // Update the previously visited node's value
        prevValue = node.value

        // Recursively traverse the right subtree
        return inorderTraversal(node.right)

    // Start the inorder traversal from the root
    return inorderTraversal(root)
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)
