# Queues: Implementation & Problems


## Agenda
**Topics to cover in DSA(Queue):**

* Queue
* Implementation of the queue using array
* Implementation of the queue using stack
* Perfect Number Question
* Doubly ended queue
* Sliding Window Maximum

---

## Queue
A queue represents a linear data structure where items are added at one end and removed from the other end. It follows the "First-In-First-Out" (FIFO) principle, meaning that the item that has been inserted first in queue will be the first one to be removed. To illustrate this concept, let's use a ticket counter as an example.

**Example: Ticket Counter Queue**

Imagine you're at a ticket counter for a popular event, and there are several people waiting in line to purchase tickets. This line of people forms a queue, and the first person who has come in this line will get the ticket first.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/893/original/upload_0dabcb159a39d120faf30f6112ccc7fe.png?1697475336" width=700/>


Common operations in a queue include:

1. **Enqueue**:<br> This operation adds an element to the back (or rear) of the queue. It is also called "push" in some contexts.
2. **Dequeue**:<br> This operation removes and returns the element from the front of the queue. It is also called "pop" in some contexts.
3. **Peek or Front**:<br> This operation allows you to look at the element at the front of the queue without removing it. It is useful for inspecting the next item to be processed.
4. **IsEmpty**:<br> This operation checks if the queue is empty. If it's empty, it means there are no elements in the queue.
5. **Size or Length**:<br> This operation returns the number of elements currently in the queue. It provides the count of items in the queue.


**Q. Can a stack or queue have a limit of elements it can have, and then we can use isFull()?**

**Sol.** Yes, both stacks and queues can have a limit on the number of elements they can hold, and you can use an "isFull()" method to check if they have reached their capacity. This concept is commonly referred to as a "bounded" stack or queue.


---
## Implementaion of queue


### Implementaion of Queue
Here's how you can implement a queue using a dynamic array along with pseudocode for the `enqueue`, `dequeue`, and `isEmpty` operations:

Queue using Dynamic Array:
- Initialize an empty dynamic array (e.g., ArrayList or Python list) to store the elements.
- Initialize two pointers: 'front' and 'rear'. Initially, both are set to -1.


### enqueue()
```java
enqueue(element):
    if rear is -1:
        //Queue is empty
        set front and rear to 0
    
    else if rear is at the end of the array:
        //Check if there is space for expansion
        if front > 0:
            # Move elements to the beginning of the array
            for i from front to rear:
                array[i - front] = array[i]
            set rear to (rear - front)
            set front to 0
        else:
            # If no space, resize the array by creating a new larger array
            # You can choose your resizing strategy
            new_size = current_array_size * 2  
            
            create a new array of size new_size
            copy elements from the current array to the new array
            set array to new_array
            set rear to (rear - front)
            set front to 0


    array[rear] = element
    increment rear by 1

```

### dequeue()
```javascript
dequeue():
    if front is -1:
        # Empty queue, nothing to dequeue
        return "Queue is empty"
    else:
        element = array[front]
        increment front by 1
        if front > rear:
            # Reset front and rear to -1 if the queue is empty
            set front and rear to -1
        return element
```


### isEmpty()
```javascript
isEmpty():
    if front is -1:
        return true
    else:
        return false
```

This pseudocode provides a basic implementation of a queue using a dynamic array. It handles the enqueue and dequeue operations efficiently by resizing the array when necessary to accommodate more elements. The `isEmpty` function checks if the queue is empty by examining the state of the `front` pointer.

### Implementation of Queues using linkedlist

1. **Insert at Head (prepend):**
   - **Time Complexity:** O(1)
   - **Explanation:** Inserting a node at the head of a singly linked list involves creating a new node, setting its `next` pointer to the current head, and updating the head pointer to the new node. This operation takes constant time because it doesn't depend on the size of the list.

2. **Insert at Tail (append):**
   - **Time Complexity:** O(n)
   - **Explanation:** To insert a node at the tail of a singly linked list, you typically need to traverse the entire list to find the current tail node. This operation takes linear time since you have to visit each node in the list to reach the end.

3. **Delete at Head:**
   - **Time Complexity:** O(1)
   - **Explanation:** Deleting a node at the head of a singly linked list is a constant-time operation. You simply update the head pointer to point to the next node in the list.

4. **Delete at Tail:**
   - **Time Complexity:** O(n)
   - **Explanation:** Deleting a node at the tail of a singly linked list also requires traversing the entire list to find the current tail node. This operation takes linear time since you have to reach the end of the list to perform the deletion.


Queue functionality can be achieved by using two of the methods mentioned:

1. **Insertion at Head and Deletion at tail:**<br> This approach can be used to provide the functionality of queue.Elements are inserted at the head (enqueue operation)with TC O(1) and removed from the tail with TC O(n)(dequeue operation). This ensures that the first element added to the queue is the first one to be removed.

2. **Insertion at Tail and Deletion at Head:**<br> This approach can also be used to create a queue using LinkedList.Elements are inserted at tail with TC O(n) and removed from the head with TC O(1). We can optimise the TC of insertion at tail to O(1) by maintaining a tail pointer and this is why we generally used this approach for queue creation through LinkedList.



---


### Question
What will be the state of the queue after these operations

enqueue(3), enqueue(7), enqueue(12), dqueue(), dqueue(), enqueue(8), enqueue(3)

### Choices
- [x] 12, 8, 3
- [ ] 3, 7, 12, 8
- [ ] 3, 8, 3
- [ ] 7, 12, 3

### Explanation

Let's break down the sequence of queue operations:

enqueue(3) : Queue becomes [3]
enqueue(7) : Queue becomes [3, 7]
enqueue(12) : Queue becomes [3, 7, 12]
dequeue() : Removes the element from the front, and the queue becomes [7, 12]
dequeue() : Removes the element from the front, and the queue becomes [12]
enqueue(8) : Queue becomes [12, 8]
enqueue(3) : Queue becomes [12, 8, 3]

So, after these operations, the final state of the queue is [12, 8, 3]




---


### Question
What will be the state of the queue after these operations

enqueue(4), dqueue(), enqueue(9), enqueue(3), enqueue(7), enqueue(11), enqueue(20), dqueue()


### Choices
- [ ] 4, 9, 3, 7
- [x] 3, 7, 11, 20
- [ ] 9, 3, 7, 11
- [ ] 3, 7, 20

### Explanation
Let's go through the sequence of queue operations:

enqueue(4): Queue becomes [4]
dequeue(): Removes the element from the front, and the queue becomes empty.
enqueue(9): Queue becomes [9]
enqueue(3): Queue becomes [9, 3]
enqueue(7): Queue becomes [9, 3, 7]
enqueue(11): Queue becomes [9, 3, 7, 11]
enqueue(20): Queue becomes [9, 3, 7, 11, 20]
dequeue(): Removes the element from the front, and the queue becomes [3, 7, 11, 20]

So, after these operations, the final state of the queue is [3, 7, 11, 20]


---
## Problem 1 Implementaion of queue using Stack



### Idea 1 - Dry Run

Consider the data:

`[5 4 7 9 Dequeue 8 10 Dequeue Dequeue]`

Lets take an Empty Stack initially,

Push 5, 4, 7, 9 then the stack becomes

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/572/original/upload_6b2096a03507a250c66e632ce5635055.png?1722331185" width=150 />

Now, From the data, It is an Dequeue operation, So we need to remove the front element which appears at the bottom of the stack.

How to remove that ? 

Since we cant remove the element, at the bottom.  
- Lets have another stack and push all the elements of Stack1 to Stack2.
- Then pop the top element of Stack2.
- Then Push all the elements of Stack2 to Stack1.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/573/original/upload_8693cd8b15414d9e0356213342c5a0a9.png?1722331293" width=400/>

### Idea 1 - Approach

For Enqueue: -> O(1)
* Push x in Stack1

For Dequeue: -> O(N)
* Transfer all the elements from Stack1  -> Stack2
* Remove top element of Stack2
* Transfer all the elements from Stack2  -> Stack1


### Idea 2 - DryRun

Consider the below data,

`[5 4 7 9 Dequeue 8 10 Dequeue Dequeue 14 Dequeue Dequeue 21]`

Enqueue 5, 4, 7 and 9 one by one into Stack1

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/580/original/upload_81e1009e4f8a70f9c95c60ab851af3c0_%282%29.png?1722332846" width=250/>


Now Its an **Dequeue** operation.

We will do the same process like before, except the last.

- Push all the elements of Stack1 to Stack2.
- Then pop the top element of Stack2.

Now we haven't copied to the Stack 1

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/581/original/upload_3be48ae4520d0b2a13e05e18fec30c8c_%281%29.png?1722332920" width=600/>

Now Enqueue 8 and 10 one by one, to the Stack1.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/582/original/upload_709d143eca24800a017ed08644255e8f_%281%29.png?1722332994" width=250/>

Now its an Dequeue Operation! Which number is standing at the front of the queue ? 
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/584/original/upload_244ec6692f986d197ed3fb7ccf2c2f97.png?1722333112" width=550/>

Its 4, Its is found on the Top of Stack2.  

Pop 4 from Stack2

Again Its an Dequeue Operation, Pop 7 from Stack2 which is the Front element of the Queue.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/585/original/upload_94e547a115e9596988488b0739bedce7.png?1722333166" width=550/>


Enqueue 14 to Stack1.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/586/original/upload_067c754d9bc6b7eecc715a62a6e77663.png?1722333205" width=300/>


Dequeue Operation

- Pop 9 from Stack2;

Again Dequeue Opeation, Right now Stack2 is Empty!

Now lets do the same process again,
- Push all the elements of Stack1 to Stack2
- Pop the Top element of Stack1

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/083/587/original/upload_3a3f942de0cc7589e2f52f74d1e97508.png?1722333245" width=600/>


### Idea 2- Approach

For Enqueue: -> O(1)
* Push x in Stack1

For Dequeue: -> Best Case: O(1) Worst Case: O(N)
* If Stack2 is empty:
    * Transfer all the elements from Stack1  -> Stack2
* Then Remove top element of Stack2


---

## Doubly Ended Queue

A double-ended queue (deque) is a data structure that allows elements to be added or removed from both ends, making it versatile for various operations. A double-linked list is a common choice for implementing a deque because it provides efficient operations for adding and removing elements from both ends. 

Here are some basic operations that are possible with a doubly-ended queue implemented using a double-linked list:

1. **Insertion at Front (push_front)**: Add an element to the front (head) of the deque. 
2. **Insertion at Back (push_back)**: Add an element to the back (tail) of the deque. 
3. **Removal from Front (pop_front)**: Remove and return the element from the front of the deque. 
4. **Removal from Back (pop_back)**: Remove and return the element from the back of the deque. 
5. **Front Element Access (front)**: Get the element at the front of the deque without removing it. 
6. **Back Element Access (back)**: Get the element at the back of the deque without removing it. 

A **double-linked list** is well-suited for implementing a **deque** because it allows for efficient insertions and removals at both ends. Each node in the linked list has pointers to the next and previous nodes, making it easy to manipulate the list in both directions.


---
## Problem 2 Sliding Window Maximum


### Problem Statement

Given an integer array `A` and an window of size k find the max element.

### Input

- An integer array `A` and integer `k` .

### Output

- An integer representing the maximum length of a subarray of `A` in which the average of all elements is greater than or equal to `k`. If no such subarray exists, return 0.

### Example

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/902/original/upload_4c4499c78441c8180afcf468db0c57f4.png?1697475913" width=600/>

### Question Explanation
Find max elements in 4-element sliding windows of array A:
- `[1, 8, 5, 6]` -> max: 8
- `[8, 5, 6, 7]` -> max: 8
- `[5, 6, 7, 4]` -> max: 7
- `[6, 7, 4, 2]` -> max: 7
- `[7, 4, 2, 0]` -> max: 7
- `[4, 2, 0, 3]` -> max: 4
Result: `[8, 8, 7, 7, 7, 4]`.

1. Initialize an empty list `max_elements`.
2. Iterate from index 0 to 3 (inclusive) to create windows of size 4.
3. Find the maximum element in each window and append it to `max_elements`.
4. Result: `[8, 8, 7, 7, 7, 4]`, representing max elements in each 4-element window in `A`.

---

### Question
Given an integer array `A` and an window of size k find the max element.

A = [1, 4, 3, 2, 5]
k = 3

### Choices
- [x] [4, 4, 5]
- [ ] [5, 5, 5]
- [ ] [1, 4, 3]
- [ ] [5, 4, 3]


### Explanation:

Maximum of [1, 4, 3] is 4
Maximum of [4, 3, 2] is 4
Maximum of [3, 2, 5] is 5

So, `[4, 4, 5]` is the answer.

---
## Sliding Window Maximum Approaches



### Brute Force Approach

Brute-force approach to find max element in a window of size `k` in array `A` involves iterating through windows, finding max within each, and storing results. Time complexity: **O(n * k)** and space complexity: **O(1)**.

### Dry Run using the Sliding Window Approach

Array `A = [1, 8, 5, 6, 7, 4, 2, 0, 3]` and `k = 4`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/903/original/upload_c51f03fd7ab32785b5087c21a5d907e3.png?1697475979" width=700/>

Let's dry run the code with the given example:

Array `A = [1, 8, 5, 6, 7, 4, 2, 0, 3]` and `k = 4`.

1. Initialize an empty queue `q`.
2. Start iterating through the array elements.
   - **For i = 0, A[i] = 1:**
     - Queue `q` is empty, so nothing happens.
     - Enqueue `i` at the rear of the queue. `q = [0]`.
   - **For i = 1, A[i] = 8:**
     - The front element of the queue is at index `0`, which is smaller than the current element and thus can't be the maximum for any window.
     - Deque the element and Enqueue `i` at the rear of the queue. `q = [1]`.

   - **For i = 2, A[i] = 5:**
     - `q` is not empty, and `A[r]` (element at index `1`) is greater than `A[i]`, so we don't do anything.
     - Enqueue `i` at the rear of the queue. `q = [2]`.
    
   - **For i = 3, A[i] = 6:**
     - `q` is not empty, and `A[r]` (element at index `2`) is smaller than `A[i]`, so we deque it, now 8 is greater than 6 so don't do anything.
     - Enqueue `i` at the rear of the queue. `q = [3]`. 

    **After the first K insertions, the q = [8,6];
Now the maximum of this window is present in the front so print it and slide the window.
To slide the window, check if A[i - k] is present in front, if yes then dequeue it. Add the next element to slide the window**

   - Continue this process for the remaining elements.

3. The final output will be the maximum elements in each group of size `k`:

   - For `k = 4`, the maximum elements are `[8, 8, 7, 7, 4, 2, 3]`.

So, the dry run demonstrates how the code finds and prints the maximum elements in groups of size `k` as it iterates through the array.

### Pseudocode (Using Dequeue)

```javascript
function findMaximumInGroups(A, k):
    Initialize an empty queue q
    n = length(A)  // Total number of elements in the array A
    
    for i from 0 to k - 1:
        while (!q.isEmpty() and A[i] >= A[q.rear()]):
            q.dequeueRear() // Remove elements that are smaller than A[i]
        q.enqueueRear(i) // Add the current element to the queue

    print A[q.front()] // Print the maximum element in the current group

    // Slide for next windows
    
    for i from k to n - 1:
        if (!q.isEmpty() and q.front() == i - k):
            q.dequeueFront() // Remove elements that are outside the current window
        
        while (!q.isEmpty() and A[i] >= A[q.rear()]):
            q.dequeueRear() // Remove elements that are smaller than A[i]
        q.enqueueRear(i) // Add the current element to the queue
    
    print A[q.front()] // Print the maximum element in the last group

# Example usage: 
A = [1, 8, 5, 6, 7, 4, 2, 0, 3]
k = 4
findMaximumInGroups(A, k)

```

### Complexity
**Time Complexity:** O(n)
**Space Complexity:** O(n)

---
## Scenario Real-Time Stock Trading Alerts


### **Scenario:**
At TechTrade Inc., a trading team focuses on day-trading technology stocks. They employ a strategy that involves selling stocks at short-term peaks to maximize profits. The team uses an algorithm to determine the best time to sell stocks based on minute-to-minute price data.

Stock Prices Array 𝐴
Consider the minute-by-minute stock prices of a tech company, TechCorp, over a 10-minute interval:

A=[220,215,230,225,240,235,230,245,250,240]

### **Objective:**
The trading team wants to identify the highest stock price in every 3-minute window to pinpoint the optimal selling moments.

Detailed Process and Trader Actions:

1. First Window 
* 9:00−9:02AM: Prices = [220, 215, 230]
* Maximum = 230
* Action: The team sets an alert to consider selling if the price approaches 230 again.

2. Second Window 
* 9:01−9:03AM: Prices = [215, 230, 225]
* Maximum = 230
* Action: No immediate action as the price did not increase.

3. Third Window 
* 9:02−9:04AM: Prices = [230, 225, 240]
* Maximum = 240
* Action: The team sells a portion of their holdings at 240, capitalizing on the peak.

4. Fourth Window 
* 9:03−9:05AM: Prices = [225, 240, 235]
* Maximum = 240
* Action: No additional sales as the price remains below the previous maximum.

5. Fifth Window 
* 9:04−9:06AM: Prices = [240, 235, 230]
* Maximum = 240
* Action: Monitor for stability or increase beyond 240 for further sales.

6. Sixth Window 
* 9:05−9:07AM: Prices = [235, 230, 245]
* Maximum = 245
* Action: Another selling opportunity as the price peaks at 245.

7. Seventh Window 
* 9:06−9:08AM: Prices = [230, 245, 250]
* Maximum = 250
* Action: The highest peak yet; the team sells a significant portion at 250.

8. Eighth Window 
* 9:07−9:09AM: Prices = [245, 250, 240]
* Maximum = 250
* Action: The price did not increase; the team holds off on further sales.

### **Conclusion:**
Each value in the output array 230,230,240,240,240,245,250,250 guides the traders on when to sell. By setting alerts based on these maximum values, the team can execute trades at the most advantageous moments, capitalizing on short-term highs to maximize returns. This real-time decision-making process aids in managing a high-volume trading portfolio efficiently and profitably.

### Approach to solve
This problem is nothing but a real life application of sliding window.
