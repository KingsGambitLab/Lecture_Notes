# Linked List 1: Introduction


## Check for value X (searching)
We can simply iterate and check if value X exists of not.
```java
temp = Head
while (temp != null){
    if(temp.data == X)
    return true
    temp = temp.next
}
return false
```
> Here if the Linked List is empty i.e if `Head = NULL`, if we try to access head.next it will give null pointer expection error.

Time Complexity for searching in Linked list is O(N).

> In linked list we cannot perform binary search because we have to travel to the middle element. We cannot jump to the middle element unlike array.

---


### Question
What is the time complexity to search any node in the linked list?

### Choices
- [ ] O(1)
- [ ] O(log(N))
- [x] O(N)
- [ ] O(N ^2)


---


### Question
What is the time complexity to access the Kth element of the linked list? [index K is valid]


### Choices
- [ ] O(1)
- [ ] O(log(N))
- [ ] O(N)
- [x] O(K)


---
## Problem 1 Insert a New Node with Data

### Insert a New Node with Data

Insert a new node with data **v** at index **p** in the linked list
>Though indexing doesn't exist is LL, but for our understanding, let's say Node 1 is at index 0, Node 2 at index 1, etc.

### Testcase 1
v = 60 and p = 3

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/031/738/original/p2t1.png?1681756504" width=600 />



### Solution to Testcase 1
* Iterate to the node having index p-1 where p-1>=0 from start of linked list. Here p is 3 so we iterate till 2
* On reaching index 2 we create a new node riz with data v i.e. 60
* Set **riz.next = t.next** and set **t.next = riz**
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/031/746/original/s2dr3.png?1681759945" width=600/>


### Testcase 2
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/031/748/original/s2rt1.png?1681760633" width=700/>

### Solution to Testcase 2
**We can do the dry run similar to testcase 1 here is the final result**
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/031/749/original/s2rt.png?1681760713" width=700/>

---


### Question
Insert a new node with data **10** at index **2** in the Given linked list.

Head -> 1 -> 6 -> 7 -> 9 -> Null

Choose the correct LinkedList after insertion.

### Choices
- [ ] Head -> 1 -> 6 -> 7 -> 9 -> **10** -> Null
- [x] Head -> 1 -> 6 ->  **10** -> 7 -> 9 -> Null
- [ ] Head -> 1 -> **10** -> 6 -> 7 -> 9 -> Null
- [ ] Head -> 10 -> 1 -> 6 -> 7 -> 9 -> Null


---
## Insert a New Node with Data Approach


### Approach

* Traverse till **(p - 1)th** node. Let's call it **t**.
* Create a new node **newNode**, with data **v**.
* Set **newNode.next** equals to **t.next**.
* Set **t.next** to reference of **newNode**.


### Pseudocode 1
```cpp
Function insertAtIndex(p,v,Node head)
{
   Node t = head
   for(i -> 1 to p - 1) // iterating updating t, p-1 times
   {
     t = t.next
   }
   
   // create a new node
   Node newNode = Node(v)
   
   // Inserting the Node
   newNode.next = t.next
   t.next = newNode
}
```
>Again there is an edge case to above solution can anyone figure it out ?

### Edge Case

If p = 0 then where to insert the node ?
=> At head of the list.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/031/753/original/sdrt3.png?1681762396" width=700/>

### Pseudocode 2

```cpp
Function insertAtIndex(p,v,Node head){
   // create a new node
   Node newNode = Node(v)
   
   Node t = head
   
   if(p == 0){    // edge case
     newNode.next = head
     head = newNode
   }
  
   for(i -> 1  to p - 1){    // iterating updating t p-1 times
     t = t.next
   }
   
   // Inserting the Node
   newNode.next = t.next
   t.next = newNode
}
```


### Time Complexity for Insertion 
O(K)


---
## Problem 2 Deletion in Linked List


### Deletion in Linked List

*Delete the first occurrence of value X in the given linked list. If element is not present, leave as is.*

### Examples
**Example 1:**
```java
List: 1 -> 8 -> 4 -> -2 -> 12
X = -2

Ans:
List: 1 -> 8 -> 4 -> 12
-2 has been deleted from the list.
```

**Example 2:**
```java
List: 1 -> 8 -> 4 -> -2 -> 4 -> 12
X = 4

Ans:
List: 1 -> 8 -> -2 -> 4 -> 12
The first occurrence of 4 has been deleted from the list.
```

### Cases: 
1. **Empty list i.e., head = null**

```java
List: null
X = 4

Ans:
List: null
```
2. **head.data = X i.e., delete head**

```java
List: 4
X = 4

Ans:
List: null
```

3. **X is somewhere in between the list, find and delete node with value X**
```java
List: 1 -> 8 -> 4 -> -2 -> 4 -> 12
X = 4

Ans:
List: 1 -> 8 -> -2 -> 4 -> 12 (removed first occurrence)
```
4. **X is not in the list, simply return**
```java
List: 1 -> 8 -> -2 -> 7 -> 12
X = 4

Ans:
List: 1 -> 8 -> -2 -> 7 -> 12
```

---


### Question
Delete the first occurrence of value **X** in the given linked list. If element is not present, leave as is.

Linked List : ```5 -> 4 -> 7 -> 1 -> NULL```
X (to Delete) : 1
### Choices
- [ ] 5 -> 4 -> 7 -> 1 -> NULL
- [x] 5 -> 4 -> 7 -> NULL
- [ ] 4 -> 7 -> 1 -> NULL
- [ ] 5 -> 7 -> NULL

---


### Explanation:

The Value 1 is present  at 4th index in the Linked List.  So if we remove it.The final Linked List will look something like this `5 -> 4 -> 7 -> -1 -> NULL`

---
## Deletion in Linked List Approach and Pseudocode

### Approach

- Check if the list is empty; if so, return it as is.
- If the target value X is at the head, update the head to the next node.
- Otherwise, iterate through the list while looking for X.
- When X is found, skip the node containing it by updating the next reference of the previous node.
- Return the modified head (which may or may not have changed during the operation).

### Pseudocode

```java
if (head == null) return head
if(head.data == X){
    tmp = head
    free(tmp) //automatically done in java, whereas have to do manually for c++ and other languages.
    head = Head.next
    return head
}
temp = head
while(temp.next != null) {
    if(temp.next.data == X){
        tmp = temp.next
        temp.next = temp.next.next
        free(tmp)
        return head
    }
    temp = temp.next
}
return head  
```
### Time complexity for Deletion
**O(N)**

> It can be seen that every operation in linked list takes linear time complexity unlike arrays.



---
## OnePlus removes Defects

### Scenerio
**OnePlus** has a lineup of **N** mobile phones ready in their manufacturing line. It has detected a defect in one of their phone models during production. 

They have decided to recall all phones of the defective model from their manufacturing line. Your task is to help **OnePlus** remove all defective phones from their production lineup efficiently.

### Problem 
You are given a **linked list A of N** nodes where each node represents a specific **model type of a OnePlus mobile phone** in the manufacturing line. Each node contains an integer representing the model number of the phone. You will also be given an integer **B** which represents the model number of the defective phone that needs to be removed.

Your goal is to remove all **nodes** (phones) from the linked list that have the model number **B** and return the modified linked list representing the updated manufacturing line.

### Approach

- We need to first check for all occurrences at the head node and change the head node appropriately.
- Then we need to check for all occurrences inside a loop and delete them one by one. 
- This problem very similar to the above problem, the only difference is that we need to remove all occurences in this problem.

### PseudoCode
```java=
Functin remove(Node A, B) {
    // Remove nodes from the beginning if they match B
    while (A != null and A.val == B) {
        A = A.next;
    }

    // Now, handle the rest of the list
    Node current = A;
    while (current != null and current.next != null) {
        if (current.next.val == B) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }
    return A;
}
```


---
## Problem 3 Reverse the linked list


### Linked List

**Note:** We can't use extra space. Manipulate the pointers only.

### Example
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/214/original/upload_b1b57d6a7f3fa84de5c43c4e52abacbb.png?1696393145" width=600/>

### Approach:
- Check for Empty List:
    - If head is null, return it as is.
- Handle Single Node List:
    - If head.next is null, return head. (This line is optional and can be omitted without affecting the core functionality.)
- Reverse the Linked List:
    - Initialize cur as head, pre as null, and a temporary variable nxt.
    - While cur is not null, do the following:
        - Store the next node in nxt.
        - Reverse the next pointer of cur to point to pre.
        - Update pre to cur.
        - Move cur to the next node (nxt).
- Update head:
    - After the loop, set head to pre, making the reversed list the new head.

### Dry Run
**Initialize the pointers**

prev = null
curr = 2 -> 5 -> 8 -> 7 -> 3 -> null
nxt = null

### Iteration 1:
**Store the next node in nxt**
```java
nxt = curr.next; nxt = 5 -> 8 -> 7 -> 3 -> null
```
**Reverse the next pointer of the current node**
```java
curr.next = prev
```
**Update the previous and current pointers**
```java
prev = curr
curr = nxt
prev = 2 -> null
curr = 5 -> 8 -> 7 -> 3 -> null
```
### Iteration 2:
**Store the next node in nxt**
```java
nxt = curr.next; nxt = 8 -> 7 -> 3 -> null
```
**Reverse the next pointer of the current node**
```java
curr.next = prev
```
**Update the previous and current pointers**
```java
prev = curr
curr = nxt
prev = 5 -> 2 -> null
curr = 8 -> 7 -> 3 -> null
```

### Iteration 3:
**Store the next node in nxt**
```java
nxt = curr.next; nxt = 7 -> 3 -> null
```
**Reverse the next pointer of the current node**
```java
curr.next = prev
```
**Update the previous and current pointers**
```javascript
prev = curr
curr = nxt
prev = 8 -> 5 -> 2 -> null
curr = 7 -> 3 -> null
```

### Iteration 4:
**Store the next node in nxt**
```java
nxt = curr.next; nxt = 3->null
```
**Reverse the next pointer of the current node**
```java
curr.next = prev
```
**Update the previous and current pointers**
```java
prev = curr
curr = nxt
prev = 7 -> 8 -> 5 -> 2 -> null
curr = 3 -> null
```
**Iteration 5**:

**Store the next node in nxt**
```java
nxt = curr.next; nxt = null
```
**Reverse the next pointer of the current node**
```java
curr.next = prev
```
**Update the previous and current pointers**
```java
prev = curr
curr = nxt
prev = 3 -> 7 -> 8 -> 5 -> 2 -> null
curr = null
```

The **loop terminates** because **curr is now null**

Final state of the linked list:
```java
prev = 3 -> 7 -> 8 -> 5 -> 2 -> null
curr = null
The head of the linked list is now prev, which is the reversed linked list:

3 7 8 5 2
```

---

### Question
Reverse the given Linked List.

Linked List :  5 -> 6 -> 7 -> 8 -> 9 

### Choices
- [ ] 5 -> 6 -> 7 -> 8 -> 9
- [x] 5 <- 6 <- 7 <- 8 <- 9
- [ ] 9 -> 6 -> 7 -> 8 -> 5
- [ ] 5 <- 6 -> 7 <- 8 <- 9


---
## Reverse the LinkedList Psuedo code and Time Complexity


### Psuedocode
```java 
cur = head;
pre = null;

while (cur != null) {
    next = cur.next;
    cur.next = pre;
    pre = cur;
    cur = next;
}

head = pre;
```
### TC & SC
**Time complexity -** O(N) 
**Space complexity -** O(1)


---
## Deep copy of a doubly linked list


### Problem Statement

We have to create a deep copy of the Doubly Linked list with random pointers. Here there is no certain next and previous pointer, a node can point to some other node.

The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding **original** node. 

Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 

**Note:** None of the pointers in the new list should point to nodes in the **original list**.

## Example

**Input:**
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/162/original/upload_d7f3137fb5df7939b219fa8bafd5e6f3.png?1692856000)

**Explanation:**
- Here black line representing `next` of the node and dotted line representing `rand` of node.
    - If we see node `a1`
        - `a1.next = a2`
        - `a1.rand = a5`
    - If we see node `a2`
        - `a2.next = a3`
        - `a2.rand = a2`
    - If we see node `a3`
        - `a3.next = a4`
        - `a3.rand = a1`
    - If we see node `a4`
        - `a4.next = a5`
        - `a4.rand = a3`
    - If we see node `a5`
        - `a5.next = null`
        - `a5.rand = a3`
- Now we need to create the copy of input linked list, in which `data` should be same and `next` and `rand` linking should also be same, but addresses of nodes should be different.


**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/163/original/upload_2eacbcfaed23c170185f545bfee191c5.png?1692856037)


**NOTE :** No **next or random** pointer can point to any of the node in original linked list.

**Another example of how the final Structure Looks like :**
<img src = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/078/922/original/Screenshot_from_2024-06-20_18-34-03.png?1718888673" >


---
## Deep Copy Solution flow

### Obvious Idea : 
Use a **HashMap** to take care of **Random Pointers.** Simple, right ?

Yes, this takes $O(N)$ space, but can we do better ? Can we save space and solve this problem in $O(1)$ extra space ? 

## Space Optimisation Idea

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/164/original/upload_47e4166f5214582aaa7f81ef2640dfba.png?1692856079)

- Take a temp node `t`.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/166/original/upload_0f0154cce487db04b97c8127151fedf2.png?1692856108)

- Create a new node with data `8` with the name `nn`.

```cpp
Node nn = new Node(t.data);
```
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/168/original/upload_e82a795a92a2d1dec7dccbd1c48c0e63.png?1692856183)

- Insert this new node `nn` between `8` and `9` of original list.
```cpp
nn.next = t.next;
t.next = nn;
t = nn.next; // t 9 in original list
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/169/original/upload_62bbb652f463d794befb1a79f69fbb6b.png?1692856213)


- Again create a new node with data `9` and insert it in between `9` and `2` in original list.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/170/original/upload_e3994f14162286393812b9d424c756ce.png?1692856238)

- In this way create new node for all the nodes of linked list till `t!=null` and insert it in between.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/171/original/upload_d6e93ee40f751725063b04dfdee2a425.png?1692856262)


The **Pseudocode** for this part is as follows:
```cpp
Node t = h;
while(t!-NULL){
Node nn = new Node(t.data);
nn.next = t.next;
t.next = nn;
t = nn.next;
}
```

**By doing this we have made our task of handling random pointers a lot easier :**
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/173/original/upload_a4edec33b8dc097ee8d3811a044af554.png?1692856491)


- Now `a1.rand=a5`, so `b1.rand` should also equal to `b5`, but how can we get `b5`, here `b5=a5.next`.
- Take two nodes `t1` and `t2`, `t1` at `h` node and `t2` at `h.next`.
```cpp
Node t1 = h;
Node t2 = h.next;
```
 
 
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/174/original/upload_fc1445c42c4b6c9ebce5c1e4c541f267.png?1692856516)

- Now `t2.rand = t1.rand.next`.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/175/original/upload_e9254fcee6b6ce27e726a8543d7beda8.png?1692856546)

- Now `t1 = t2.next` and `t2 = t1.next`, to move `t1` and `t2` forward.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/176/original/upload_c16ce3b1f9d7b16ac1d14161cde6abcd.png?1692856574)

- Now again `t2.rand = t1.rand.next` and `t1 = t2.next` and `t2 = t1.next` to move `t1` and `t2` forward.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/178/original/upload_ebef92fef6ea6ff8f0fed3ca7c4ca458.png?1692856649)

- In this way do it until, `t1!=NULL`. So that every new node points to their `rand` node.

- While updating `t2.next = t1.next`, we need to check `t1!=NULL`, otherwise it will give an `nullpointerexception` in last iteration when `t1` becomes `NULL`.


Here is how the **Pseudocode** looks like:
```cpp
Node t1 = h;
Node t2 = h.next;
while(t1 != NULL){
t2.rand = t1.rand.next;
t1 = t2.next;
if(t1 != NULL){
t2 = t1.next;
}
}
```

- Now random links are also arranged in purple list.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/182/original/upload_752e297c2b16dad058707d1c09c0f038.png?1692857118)

- Now again take two nodes `t1` and `t2`, `t1` at `h` node and `t2` at `h.next`.
```cpp
Node t1 = h;
Node t2 = h.next;
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/183/original/upload_4471af8b32e5130a0d3b729a65812167.png?1692857142)

- `t1.next` is actually `a2` in original list, so `t1.next = t2.next`.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/184/original/upload_2cab8e5334a75b7fff438cfdebb536d3.png?1692857184)

- Now update `t1 = t1.next`.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/185/original/upload_ba45d76070b6c72cb7c112ebb6f15d7e.png?1692857206)

- `t2.next = t1.next`.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/186/original/upload_ddb1c2321df12a49b13f7ddb705166ad.png?1692857230)

- Now we will update `t2`, `t2 = t2.next`.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/187/original/upload_6270d7f01206e71bcf7d4f97384308c3.png?1692857266)

- In this way do this, until `t1!=NULL`.

```cpp
Node dh =  h.next;
Node t1 = h;
Node t2 = h.next;
while(t1 != NULL){
    t1.next = t2.next;
    t1 = t1.next;
    if(t1 != NULL){
        t2.next = t1.next;
    }
    t2 = t2.next;
}
```

- Now final list becomes, and we will return `dh` which we have initialized by `h.next`.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/188/original/upload_cb98cb80fece534e53f5eb24c901a92f.png?1692857320)


## PseudoCode
```cpp
Node Clone(Node h) {
    Node t = h;
    while (t != NULL) {
        Node nn = new Node(t.data);
        nn.next = t.next;
        t.next = nn;
        t = nn.next;
    }
    
    Node t1 = h;
    Node t2 = h.next;
    while (t1 != NULL) {
        t2.rand = t1.rand.next;
        t1 = t2.next;
        if (t1 != NULL) {
            t2 = t1.next;
        }
    }
    
    Node dh = h.next;
    t1 = h;
    t2 = h.next;
    while (t1 != NULL) {
        t1.next = t2.next;
        t1 = t1.next;
        if (t1 != NULL) {
            t2.next = t1.next;
        }
        t2 = t2.next;
    }
    
    return dh;
}

```

## Complexity
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$ because we are **not** using extra memory like **Hashmap**.

---

### Question
What is the time complexity of creating a deep copy of a Doubly Linked List consists of N nodes with random pointers using extra space?

### Choices
- [x] O(N)
- [ ] O(N * N)
- [ ] O(1)
- [ ] O(log(N))

---

