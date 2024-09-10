# Linked List 3: Problems & Doubly Linked List

## Revision Quizzes

### Question
What is the time complexity to merge two sorted linked lists into a single sorted linked list?

### Choices
- [x] O(n + m)
- [ ] O(n log(n))
- [ ] O(n * m)
- [ ] O(m log(m))

---

### Question
How is the starting point of the cycle found once a cycle is detected in the linked list?

### Choices

- [x] Reset the slow pointer to head and move both pointers one step at a time.
- [ ] Continue moving fast pointer until it reaches the head.
- [ ] Move slow pointer two steps at a time.
- [ ] Move fast pointer to the start of the cycle.


---
## Agenda
- What is doubly linked list?
- LRU Cache
- Check if LL is palindrome

So let's start.

---

### What is doubly linked list?
A dll is a type of data structure used to store collection of elements. It is similar to a singly linked list but with an additional feature- each node in a dll contains pointers or references to both the next and the previous nodes in the list.

### Example

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/483/original/upload_213ccfab994121707413abee35188ad7.png?1697178938" width=500 />

The `previous` pointer of the first node always points to `null` and the `next` pointer of the last node also points to `null` in the doubly linked list.

### Structure
```
class Node {
    int data;
    Node prev, next;
    
    Node(x) {
        data = x;
        prev = NULL;
        next = NULL;
    }
}
```

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/077/479/original/Screenshot_2024-06-09_at_5.38.35_PM.png?1717934924" width=600 />

---


### Question
`prev` Pointer of Head of Doubly Linked List points to:

### Choices
- [ ] Next to Head Node
- [x] Null pointer
- [ ] Tail
- [ ] Depends


---
## Real Life Application - Spotify's Music Manager


### Scenerio
**Spotify** wants to enhance its user experience by allowing users to navigate through their music playlist seamlessly using "**next**" and "**previous**" song functionalities. 

### Problem
You are tasked to implement this feature using a **doubly linked list** where each node represents a song in the playlist. The system should support the following operations:

- **Add Song**: Insert a new song into the playlist. If the playlist is currently empty, this song becomes the "**Current song**".
- **Play Next Song**: Move to the next song in the playlist and display its details.
- **Play Previous Song**: Move to the previous song in the playlist and display its details.
- **Current Song**: Display the **details** of the current song **being played**.


### Constraints:

- Each song is uniquely identified by its song ID.
- The playlist starts empty, and the first song added becomes the current song.
- All operations are valid within the current state of the playlist (i.e., there won’t be a request to play the next song if there is no next song, and no request to play the previous song if there is no previous song).


### Example Input :
```=
Add Song (ID: 1, Name: "Yesterday Blues")
Add Song (ID: 2, Name: "Imagine Dragons")
Play Next Song
Current Song
Add Song (ID: 3, Name: "Hotel California")
Play Next Song
Current Song
Play Previous Song
Play Previous Song
Current Song
```

### Output : 
``` =
Current song playing: Imagine Dragons
Current song playing: Hotel California
Current song playing: Yesterday Blues
```

Since we shall have to move to and from in a list, we can use doubly linked list. This is a real life application of DLL.

---
## Problem 1 Insert node just before tail in a dll


1. Say we have direct access to first and last node via head and tail pointer.
2. temp = tail.prev
3. Then we can make connections as shown in image below


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/077/481/original/Screenshot_2024-06-09_at_5.44.25_PM.png?1717935285" width="600" />

### Pseudocode

```javascript
function insert_back(Node head, Node tail, Node new_node) {
    temp = tail.prev;
    new_node.prev = temp;
    new_node.next = tail;
    temp.next = new_node;
    tail.prev = new_node
}
```

### T.C
O(1)


---


### Question
In a doubly linked list, the number of pointers affected for an insertion operation between two nodes will be?

### Choices
- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4
- [ ] Depends


---
## Problem 2 Delete a given node from dll


### Problem Statement
Delete a given node from dll
1. Node reference is given
2. Given node will not be head/tail
3. DLL is not NULL

Example -
Say we are given address of node x (#adx), then below connections have to be made

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/077/484/original/Screenshot_2024-06-09_at_5.53.33_PM.png?1717935820" width="600" />

### Pseudocode
```
    function remove(Node x) {
        p = x.prev
        n = x.next
        p.next = n;
        n.prev = p;
        x.prev = x.next = NULL;
        free(x);
    }
```

### T.C
O(1)

---
## Memory Hierarchy


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/077/485/original/Screenshot_2024-06-09_at_5.58.52_PM.png?1717936140" width = 600 />

Cache Memory is a special very high-speed memory. The cache is a smaller and faster memory that stores copies of the data from frequently used main memory locations. There are various different independent caches in a CPU, which store instructions and data. The most important use of cache memory is that it is used to reduce the average time to access data from the main memory. 

There are different ways of implementing cache, one of them is LRU cache.

The Least Recently Used (LRU) Cache operates on the principle that the data most recently accessed is likely to be accessed again in the near future. By evicting the least recently accessed items first, LRU Cache ensures that the most relevant data remains available in the cache.

---
## Problem 3 Implement LRU Cache


### Problem Statement
We have been given a running stream of integers and the fixed memory size of `M`, we have to maintain the most recent `M` elements. In case the current memory is full, we have to delete the least recent element and insert the current data into the memory (as the most recent item).

### Example

{ 7, 3, 9, 2, 6, 10, 14, 2, 10, 15, 8, 14 }
Given cache size = 5

Insert 7
```
-----------
7
-----------
size = 1
```

Insert 3
```
-----------
7 3
-----------
size = 2
```

Insert 9
```
------------
7 3 9
------------
size = 3
```

Insert 2
```
------------
7 3 9 2
------------
size = 4
```

Insert 6
```
----------
7 3 9 2 6
----------
size = 5
```

Insert 10
```
remove 7
-----------
3 9 2 6 10
-----------
size = 5
```

Insert 14
```
remove 3
------------
9 2 6 10 14
------------
size = 5
```

Insert 2
```
2 is already there, remove it and add at end
-----------
9 6 10 14 2
-----------
size = 5
```

Insert 10
```
10 is already there, remove it and add at end
-----------
9 6 14 2 10
-----------
size = 5
```

Insert 15
```
remove 9
------------
6 14 2 10 15
------------
size = 5
```

Insert 8
```
remove 6
------------
14 2 10 15 8
------------
size = 5
```

Insert 14
```
14 is already there, remove it and add at end
------------
2 10 15 8 14
------------
size = 5
```

---


### Question
What is the behavior of an LRU cache memory when a new item is inserted and the cache is already full?

### Choices

- [x] The new item is added to the cache, and the least recently used item is removed from the cache.
- [ ] The new item is not added to the cache, and the least recently used item is not removed from the cache.
- [ ] The new item is added to the cache, and the least recently used item is updated to be the most recently used item.
- [ ] The new item is not added to the cache, and the most recently used item is removed from the cache.


---
### Explanation


In an LRU cache, the least recently used item is always the one that is removed when the cache is full and a new item needs to be inserted. This ensures that the most recently accessed items are always prioritized and kept in the cache.

---
## LRU Solution flow

## Flowchart

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/151/original/upload_82e7a60d97ef6bef6d579178a4035d03.png?1692855639)

- If a data `x` will come, so first we search it in cache, it is available or not.
    - If `x` is present in cache(HIT) then:
        - delete(x)
        - insertBack(x)
    - If `x` is not present in cache(MISS) then:
        - If cache size is not full, insertBack(x)
        - If cache size is full, deleteFront() and insertBack(x).


**Note :** Duplicates are not possible inside cache.

**Finally operations Required :**
1. **search(x)**
2. **remove(x)**
3. **insertBack(x)**

## Complexities of implementing LRU through various Data Structures

|    Operations     | ArrayList |      Singly Linked List      | Singly LinkedList + HashSet`<Data>` | Doubly Linked List + `HashMap<Data, Address>` |
|:-----------------:|:---------:|:----------------------------:|:-----------------------------------:|:---------------------------------------------:|
|   **search(x)**   |   O(N)    |             O(N)             |                O(1)                 |                     O(1)                      |
|   **remove(x)**   |   O(N)    |             O(N)             |                O(N)                 |                     O(1)                      |
| **insertBack(x)** |   O(1)    | O(1): if tail node is stored |    O(1): if tail node is stored     |                     O(1)                      |
    
    

## Example of HashMap Storage 

**Doubly Linked List**
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/152/original/upload_3adf0ccde4f6e984f0539ba67281e432.png?1692855686)

**Storage in HashMap**
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/153/original/upload_265836e1268b993818190f0185c40c05.png?1692855708)

### Example
**Input:**
Data: 7 3 9 10 14 9 10 15 8 14
Cache size: 3

**Solution:**
In some cases, sometimes we may need to delete head/tail node also. So first of all we are taking two dummy nodes `head` and `tail`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/154/original/upload_709510197670a1e0649f1d4c3a1d6d09.png?1692855731" width=400/>

- Declare a `HashMap<int, Node> hm`.
- First 7 will come, 7 is not present in the cache as it is not in Map, so insert 7 in doubly linked list just before `tail` and store the `<7,address_of_node_inserted>` in map.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/155/original/upload_8c5d209ecd77ceae6d879f407a7c320c.png?1692855759" width=400/>


`hm: {<7,a1>}`

- Now 3 will come, 3 is not present in the cache as it is not in Map, so insert 3 in doubly linked list just before `tail` and store the `<3,address_of_node _inserted>` in map.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/157/original/upload_071bf3ad5d6d202096cd7d2b5cf066e5.png?1692855788" width=400/>

`hm:{<7,a1>, <3,a2>}`

- Now 9 will come, 9 is also not present in the cache as it is not in Map, so insert 9 in doubly linked list just before `tail` and store the `<9,address_of_node _inserted>` in map.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/158/original/upload_5eef6aa42b1c1582738e99aea53650fd.png?1692855813" width=500/>

`hm:{<7,a1>, <3,a2>, <9,a3>}`

- Now 10 will come, 10 is also not present in the cache as it is not in Map, but the size of cache is fill as hashmap size is equal to the cache size, so delete `#a1`, and `#a1` can be accessed by `head.next` then we can simply delete it and delete it from hashMap also and insert 10 in doubly linked list just before `tail` and store the `<10,address_of_node _inserted>` in map.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/159/original/upload_d9c228557188bdc85eb6f71c7042a7ec.png?1692855834" width=600/>

hm:{ ~~<7,a1>~~, <3,a2>, <9,a3>, <10,a4>}

- Now 14, we can insert 14 as similar to 10.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/160/original/upload_1ae952300db1d4652a2b3ae2703cd9dc.png?1692855855" width=600/>

hm:{ ~~<7,a1>~~, ~~<3,a2>~~ , <9,a3>, <10,a4>, <14,a5>}

- Now 9, it is already present in cache,so first get the address of 9 from HashMap. Then delete 9 from doubly linked list and insert 9 at back before the `tail` node and update address of 9 in hashMap also.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/044/161/original/upload_c168153c0d04219af2a3b934b554dfb5.png?1692855881" width=600/>

hm:{ ~~<7,a1>~~, ~~<3,a2>~~ , <9,~~a3~~ a6>, <10,a4>, <14,a5>}

- Now 10, it is already present in cache,so first get the address of 10 from HashMap. Then delete 10 from doubly linked list and insert 10 at back before the `tail` node and update address of 10 in hashMap also.

hm:{ ~~<7,a1>~~, ~~<3,a2>~~ , <9,~~a3~~ a6>, <10,~~a4~~ a7>, <14,a5>}

- similary other elements can be inserted in cache.

Implementation of LRU is mentioned in different langauges(https://docs.google.com/document/d/1IC_c1mFOwWHyst-YtuXbhxfZlNXxxYTnxu1MWTS6QkA/edit)

## PseudoCode
```java 
class Node {
    integer data;
    Node next;
    Node prev;

    constructor Node(x) {
        data = x;
        next = null;
        prev = null;
    }
}

// Initialization
Node head = new Node(-1);
Node tail = new Node(-1);
head.next = prev;
tail.prev = head;
HashMap<integer, Node> hm;

function LRU(x, limit) {
    // if x present
    if (hm.containsKey(x) == true) {
        Node t = hm.get(x);
        DeleteNode(t);
        Node nn = new Node(x);
        insertBack(nn, tail);
        hm.put(x, nn);
    } else {
        if (hm.size() == limit) {
            // delete the first node
            Node t = head.next;
            int val = t.data;
            DeleteNode(t);
            hm.remove(val);
        }
        Node nn = new Node(x);
        insertBack(nn, tail);
        hm.put(x, nn);
    }
}

function insertBack(Node nn, Node tail) {
    t = tail.prev;
    t.next = nn;
    tail.prev = nn;
    nn.prev = t;
    nn.next = tail;
}

function DeleteNode(Node temp) {
    t1 = temp.prev;
    t2 = temp.next;
    t1.next = t2;
    t2.prev = t1;
    temp.next = null;
    temp.prev = null;
}
```

---
## Problem 4 Check Palindrome


### Problem Statement
Given a Linked List, check if it is a palindrome.

### Example:
maam, racecar, never, 121, 12321 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/215/original/upload_cda9b4e733dcc81c3804f1a2d12d9021.png?1696393390" width=500/>


---

### Question
Check the Given linked list is Palindrome or not.

Linked List : ```Head -> 1 -> Null```

### Choices
- [x] YES
- [ ] NO

### Explanation:

Yes, The Given Linked List is an Palindrome, Because it reads the same in reverse order as well.

---

### Solution 1 :
Create a copy of linked list. Reverse it and Compare

### Complexity
**Time Complexity -** O(N) 
**Space Complexity -** O(N).


### Solution 2 :
1. Find middle element of linked list 
2. Reverse second half of linked list 
3. Compare first half and compare second half 

**Step wise solution:**

1. **Find length of linked list**
```java
n = 0
temp = Head
while(temp != null){
    n++
    temp = temp.next
}
```
2. **Go to the middle element**
// If n = 10(even), we'll reverse from 6th node.
// If n = 9(odd), then also we'll reverse from 6th node.(**5th node will be middle one that need not be compared with any node**)

So, regardless of even/odd, we can skip (n + 1) / 2 nodes.
```java
temp Head
(for i --> 1 to (n + 1) / 2){
    temp =temp.next
}
//temp middle
```
3. Now reverse the linked list from $((n+1)/2 + 1)th$ node.
4. Compare both the linked list

### T.C & S.C

Total time complexity for checking palindrome is O(N) and space complexity is O(N).



