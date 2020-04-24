
# Linked List

- LinkedList donot have index based access
- Arrays have index based access

**Pros n Cons**

- Array give random access but LL dont. 
- Lesser storage required for arrays because ll also stores pointers
- insertions in between nodes is easy in LL whereas insertion in between positions of array is difficult

### Linked list structure

```cpp
class Node {
	public:
	int data;
	Node *next
};
```

**Time Complexity of Operations in LinkedList**

- Insertion 
	- At front O(1)
	- At end O(n) 
	- At Middle O(k) ( Addition after kth Node)
- Deletion
	- At front O(1)
	- At end O(n) ( If tail not present )
	- At Middle O(k) ( Addition after kth Node)

- Traversal
  	- O(n)

*Essential feature to know in the LL is head*

**Q - How to delete the complete list if we know the head??**
In Java just delete the head, but in C or C++ there is no auto garbage collection, we will iteratively delete the nodes

**Q - Find the value of nth node from first**
Just iterate from head till n iterations

## Assignment Questions 

**Q1 - Find the value of nth node from last**

*Approach 1*
(Use length of linked list)
1) Calculate the length of Linked List. Let the length be len.
2) Print the (len – n + 1)th node from the beginning of the Linked List.

*Can we do it in single iteration?*

Double pointer concept : First pointer is used to store the address of the variable and second pointer used to store the address of the first pointer. If we wish to change the value of a variable by a function, we pass pointer to it. And if we wish to change value of a pointer (i. e., it should start pointing to something else), we pass pointer to a pointer.
One approach is to find length of LL as L, then . go to L - n + 1 th node


**Q- Reverse the LinkedList**

**Iteratively**

 ```java
 
Initialize three pointers prev as NULL, curr as head and next as NULL.
Iterate trough the linked list. In loop, do following.

// Before changing next of current,
// store next node
next = curr->next

// Now change next of current
// This is where actual reversing happens
curr->next = prev

// Move prev and curr one step forward
prev = curr
curr = next

```

**Recursively**

![Screenshot 2020-04-24 at 7 12 00 PM](https://user-images.githubusercontent.com/35702912/80218963-846d6b80-865f-11ea-9744-92bb588334d0.png)

```cpp

Node* reverse(Node* head) 
    { 
        if (head == NULL || head->next == NULL) 
            return head; 
  
        /* reverse the rest list and put  
          the first element at the end */
        Node* rest = reverse(head->next); 
        head->next->next = head; 
  
        /* tricky step -- see the diagram */
        head->next = NULL; 
  
        /* fix the head pointer */
        return rest; 
    } 
```

**Q2- K Reverse**

https://leetcode.com/problems/reverse-nodes-in-k-group/solution/

**Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.**

**k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
**

```java
class Solution {
    
    public ListNode reverseLinkedList(ListNode head, int k) {
        
        // Reverse k nodes of the given linked list.
        // This function assumes that the list contains 
        // atleast k nodes.
        ListNode new_head = null;
        ListNode ptr = head;
        
        while (k > 0) {
            
            // Keep track of the next node to process in the
            // original list
            ListNode next_node = ptr.next;
            
            // Insert the node pointed to by "ptr"
            // at the beginning of the reversed list
            ptr.next = new_head;
            new_head = ptr;
            
            // Move on to the next node
            ptr = next_node;
            
            // Decrement the count of nodes to be reversed by 1
            k--;
        }
            
            
        // Return the head of the reversed list
        return new_head;
    
    }
            
    public ListNode reverseKGroup(ListNode head, int k) {
        
        int count = 0;
        ListNode ptr = head;
        
        // First, see if there are atleast k nodes
        // left in the linked list.
        while (count < k && ptr != null) {
            ptr = ptr.next;
            count++;
        }
            
        
        // If we have k nodes, then we reverse them
        if (count == k) {
            
            // Reverse the first k nodes of the list and
            // get the reversed list's head.
            ListNode reversedHead = this.reverseLinkedList(head, k);
            
            // Now recurse on the remaining linked list. Since
            // our recursion returns the head of the overall processed
            // list, we use that and the "original" head of the "k" nodes
            // to re-wire the connections.
            head.next = this.reverseKGroup(ptr, k);
            return reversedHead;
        }
            
        return head;
    }
}
```



**Q3 - Given a singly linked list  _L_:  _L_0→_L_1→…→_L__n_-1→_L_n,  
reorder it to:  _L_0→_L__n_→_L_1→_L__n_-1→_L_2→_L__n_-2→… 
You may not  modify the values in the list's nodes, only nodes itself may be changed.**

https://leetcode.com/problems/reorder-list/solution/


- Approach -> 
1) Find middle of LL
2) Reverse the half after middle
3) Start reordering one by one

```java
class Solution {
  public void reorderList(ListNode head) {
    if (head == null) return;

    // find the middle of linked list [Problem 876]
    // in 1->2->3->4->5->6 find 4 
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }

    // reverse the second part of the list [Problem 206]
    // convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
    // reverse the second half in-place
    ListNode prev = null, curr = slow, tmp;
    while (curr != null) {
      tmp = curr.next;

      curr.next = prev;
      prev = curr;
      curr = tmp;
    }

    // merge two sorted linked lists [Problem 21]
    // merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
    ListNode first = head, second = prev;
    while (second.next != null) {
      tmp = first.next;
      first.next = second;
      first = tmp;

      tmp = second.next;
      second.next = first;
      second = tmp;
    }
  }
}
```

**Q4- Copy List**

https://leetcode.com/problems/copy-list-with-random-pointer/

**A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.**

**Return a deep copy of the list.**

## Homework Problems

**Q1- Find mid node in LL**

Approach 1 -> calculate length then again traverse length/2 distance
Approach 2 ->Mid point is at distance 'd' and end point is at distance '2d'

**Q2- Remove Duplicates from a LinkedList**

**Q3- Reverse a linked list A from position B to C.**

**Q4 - Given a linked list, swap every two adjacent nodes and return its head. You may  not  modify the values in the list's nodes, only nodes itself may be changed.**
```java
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode  curr = head.next;
        ListNode prev = head;
        while(head != null && head.next != null){
            
            ListNode first = head;
            ListNode second = head.next;
            prev.next = second;
            first.next = second.next;
            second.next = first;
            
            
            prev = first;
            head = first.next;
        }
        
        return curr;
     }
}
```



