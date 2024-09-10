# Advanced DSA : Trees 5: Problems on Trees

## Problem 1 Next Pointer in Binary Tree

### Problem Statement
Given a perfect binary tree initially with all next pointers set to nullptr, modify the tree in-place to connect each node's next pointer to the next node in the same level from left to right, following an in-order traversal.


### Example
```cpp 
Input:
                        1
                       / \
                      2   3
                     / \ / \
                    4  5 6  7

Output :  
                        1 -> nullptr
                       / \
                      2 -> 3 -> nullptr
                     / \ / \
                    4 -> 5 -> 6 -> 7 -> nullptr

```



### Brute force solution 
**Level order Traversal** : 
1. We check if the binary tree is empty; if so, we return the root since there's nothing to connect. 
2. A queue is created for level order traversal, initialized with the root node. 
3. In the main loop, we process nodes at the current level. 
4. At the start of each level, we determine the number of nodes at the current level (levelSize).
5. In the inner loop, we process each node at the current level:
    *  We dequeue the current node from the front of the queue.
    *  If the current node is not the last node in the level (i.e., i < levelSize - 1), we update its next pointer to point to the front of the queue, which connects nodes from left to right within the same level.
    *  We enqueue the left and right children of the current node (if they exist) into the queue for the next level.
6. The loop continues until all levels are processed.
7. Finally, the function returns the modified root of the binary tree, which now has next pointers connecting nodes at the same level, except for the last node in each level, whose next pointer remains nullptr.


### Pseudocode : 
```cpp 
function connect(Node root) {
    // Check if the tree is empty
    if (root is null) {
        return null;
    }

    // Create a queue and enqueue the root
    queue<Node> q;
    q.push(root);

    // Traverse the tree level by level
    while (!q.empty()) {
        int levelSize = q.size();

        // Process nodes at the current level
        for (int i = 0; i < levelSize; ++i) {
            Node node = q.front();
            q.pop();

            // Connect the current node to the next node in the same level
            if (i < levelSize - 1) {
                node.next = q.front();
            }

            // Enqueue the left and right children (if they exist) for the next level
            if (node has a left child) {
                q.push(node's left child);
            }
            if (node has a right child) {
                q.push(node's right child);
            }
        }
    }

    // Return the modified root
    return root;
}
```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(N)

### Optimized Solution:
1. We create a dummy node and a temp pointer initially pointing to it.
2. We traverse the tree level by level from left to right.
3. For each node:
* If it has a left child, we connect the temp node's next pointer to the left child and update temp.
* If it has a right child, we connect the temp node's next pointer to the right child and update temp.
4. Level Completion:
5. When the current level is done, we move to the next level by updating root to the dummy node's next. We reset dummy's next and reset temp to the dummy node.
6. We repeat these steps until all levels are traversed.
7. The loop ends when there are no more levels to traverse.


### Pseudocode 
```cpp 
function populateNextPointers(Node root) {
    if (!root) {
        return;
    }

    Node dummy = new Node(-1);
    Node temp = dummy;

    while (root != nullptr) {
        if (root.left != nullptr) {
            temp.next = root.left;
            temp = temp.next;
        }
        if (root.right != nullptr) {
            temp.next = root.right;
            temp = temp.next;
        }
        root = root.next;
        if (root == nullptr) {
            root = dummy.next;
            dummy.next = nullptr;
            temp = dummy;
        }
    }
```

### Complexity
Time Complexity:** O(N)
**Space Complexity:** O(1)



---
## Problem 2 Diameter of Binary Tree


### Problem Statement

Given a binary tree, find the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

**Definition of Diameter**: The diameter of a binary tree is defined as the number of edges along the longest path between any two leaf nodes in the tree. This path may or may not pass through the root.

---


### Question
How would you find the diameter of a binary tree?

### Choices
- [ ] Add the height of the left and right subtrees.
- [ ] Count the number of nodes in the tree.
- [x] The maximum of the following three: Diameter of the left subtree, Diameter of the right subtree, Sum of the heights of the left and right subtrees plus one
- [ ] Divide the height of the tree by 2.


---
## Diameter of Binary Tree Examples

**Example**:
Example that illustrates that the diameter of the tree can pass through a root node.
```cpp
Input:

                        1
                       / \
                      2   3
                     / \
                    4   5
Output: 3
```
**Explanation**:
The diameter of the binary tree shown above is the path 4 -> 2 -> 1 -> 3, which contains 3 edges.


**Example:**
Example that illustrates that the diameter of the tree can pass through a non-root node:
```cpp
Input:
                        1
                       / 
                      2   
                     / \
                    4   5
                   / \   \
                  6   7   3
                  
Output: 4            
```
**Explanation:**
The diameter of the binary tree shown above is the path 6 - 4 - 2 - 5 - 3, which includes 4 edges.


---


### Question
What is the diameter of the Given Binary Tree.

```cpp
                        1
                       / 
                      2   
                     / \
                    4   5
                   / \   \
                  6   7   9
                       \
                        8
                         \
                         10
```

### Choices
- [x] 6
- [ ] 5
- [ ] 7
- [ ] 4

### Explanation:

The path 9 -> 5 -> 2 -> 4 -> 7 -> 8 -> 10 has 6 edges, which is the diameter of the given tree. 


---
## Diameter of Binary Tree Solution


### Solution:
1. To solve this problem,we initialize a diameter variable to 0 to track the maximum diameter.
2. Define a helper function that recursively computes both the height of the tree and the diameter
3.  In the helper function:
    * If the node is null, we return -1 to signify no height.
    * We recursively find left and right subtree heights.
    * We update diameter with the maximum diameter found, including the current node and connecting path (2 units).
    * The height of the current node is the max of left and right subtree heights, plus 1.
    * Call the helper function with the root of the binary tree from the main function or method.
4. Retrieve and use the maximum diameter found during traversal as the result.

### Pseudocode:
```cpp
function diameterOfBinaryTree(Node root) {
    diameter = 0;

    // Helper function to calculate height and update diameter
    function calculateHeight(node) {
        if (!node) {
            return -1; // Height of a null node is -1
        }

        leftHeight = calculateHeight(node.left);
        rightHeight = calculateHeight(node.right);

        // Update diameter with the current node's diameter
        diameter = max(diameter, leftHeight + rightHeight + 2);

        // Return the height of the current node
        return max(leftHeight, rightHeight) + 1;
    };

    calculateHeight(root); // Start the recursive calculation

    return diameter;
}

```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(H)


---
## Problem 3 Vertical Order traversal


### Print vertical order traversal

### Examples:
Consider the following binary tree:
```cpp
        1
       / \
      2   3
     / \ / \
    4  5 6  7
       / \
      8   9
```
Vertical order traversal of this tree would yield the following output:
```cpp
Vertical Line 1: 4
Vertical Line 2: 2, 8
Vertical Line 3: 1, 5, 6
Vertical Line 4: 3, 9
Vertical Line 5: 7
```

We need to print the vertical lines from top to bottom. 


----

### Question
Consider the following binary tree:
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

Pick the vertical order traversal of the given Binary Tree.

### Choices
- [x] [2, 1, 5, 9, 3, 8, 6, 10, 7]
- [ ] [1, 2, 5, 3, 6, 8 ,9, 10, 7]
- [ ] [2, 1, 3, 5, 6, 8, 7, 9, 10]
- [ ] [1, 5, 2, 3, 6, 10, 8, 7, 9]


### Explanation:

Vertical order traversal of this tree would yield the following output:
```cpp
Vertical Line 1: 2
Vertical Line 2: 1, 5, 9
Vertical Line 3: 3, 8
Vertical Line 4: 6, 10
Vertical Line 5: 7
``` 


---
## Vertical Order traversal Observations



### Observation:
* Vertical order traversal of a binary tree prints nodes column by column, with nodes in the same column printed together.

These are the steps to Print vertical order traversal:
### Approach:
* Assign horizontal distances to nodes (root gets distance 0, left decreases by 1, right increases by 1).
* Create a map/hash table where keys are distances and values are lists of node values.
* Update the map while traversing: append node values to corresponding distance lists.
* After traversal, print the values from the map in ascending order of distances.


---
## Vertical Order traversal Pseudocode


### Pseudocode

Let us see the pseudocode to solve this:
```cpp
procedure verticalOrderTraversal(root)
    if root is null
        return an empty list
    
    Create a dictionary to store nodes at each vertical level: vertical_levels
    Create a queue for level order traversal: queue
    Enqueue a tuple (root, 0) into the queue  // Tuple: (Node, Vertical Level)
    
    while queue is not empty
        node, level = dequeue a tuple from the queue
        Append node's value to vertical_levels[level]
        
        if node has left child
            Enqueue a tuple (left child, level - 1) into the queue
        
        if node has right child
            Enqueue a tuple (right child, level + 1) into the queue
    
    Sort the keys of vertical_levels to maintain vertical order
    
    Initialize an empty list: vertical_traversal
    
    for each key, level, in sorted vertical_levels
        Append all values in vertical_levels[level] to vertical_traversal
    
    return vertical_traversal
end procedure

```


---
## Problem 4 Top View 


### Example:
Consider the following binary tree:
```cpp
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```
The top view of this tree would be [4, 2, 1, 3, 7].


---

### Question
Consider the following binary tree:
```cpp
        1
       / \
      2   3
       \   \
        5   6
           / \
          8   9          
```

What is the top view of the given binary tree.

### Choices
- [ ] [5, 2, 1, 3, 6, 9]
- [ ] [8, 5, 2, 1, 3, 6, 9]
- [ ] [2, 1, 5, 3, 8, 6, 9]
- [x] [2, 1, 3, 6, 9]

---

### Explanation:

The Top view of the Given Binary tree is [2, 1, 3, 6, 9].


---
## Top View Observations


### Observations:
* Assign Horizontal Distances: Nodes are assigned horizontal distances, with the root at distance 0, left children decreasing by 1, and right children increasing by 1. This helps identify the nodes in the top view efficiently.

### Approach:
For this we need to follow these steps:
* Traverse the binary tree.
* Maintain a map of horizontal distances and corresponding nodes.
* Only store the first node encountered at each unique distance.
* Print the stored nodes in ascending order of distances to get the top view.

### Pseudocode:
```cpp
procedure topView(root)
    if root is null
        return
    
    Create an empty map
    
    Queue: enqueue (root, horizontal distance 0)
    
    while queue is not empty
        (currentNode, currentDistance) = dequeue a node
        
        if currentDistance is not in the map
            add currentDistance and currentNode's value to map
        
        enqueue (currentNode's left child, currentDistance - 1) if left child exists
        enqueue (currentNode's right child, currentDistance + 1) if right child exists
    
    Print values in map sorted by keys
end procedure

```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(W)


## Invert Binary Tree -  Problem Statement
Given the root node of a binary tree, write a function to invert the tree.

### Example 
Original Binary Tree : 
```plaintext
                    1
                   / \
                  2   3
                 / \
                4   5
```
After Inverting the Binary Tree : 
```plaintext
                    1
                   / \
                  3   2
                     / \
                    5   4
```

### Solution
To solve this problem,we can recursively invert the binary tree by swapping the left and right subtrees for each node.

```cpp
function invertTree(Node root) {
    if (root == nullptr) {
        return; // Return if the root is null
    }

    // Use a temporary variable to swap left and right subtrees
    Node temp = root.left;
    root.left = root.right;
    root.right = temp;

    // Recursively invert the left and right subtrees
    invertTree(root.left);
    invertTree(root.right);
}

```

### Complexity
**Time Complexity:** O(N)
**Space Complexity:** O(H)
