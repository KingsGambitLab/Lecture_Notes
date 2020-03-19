Queues
------

- preserves order - FIFO
- queue of people in front of a ticker place

**Operations:**

stack: push and pop, peek

queue:
- enqueue / pushfront
- dequeue / popfront / removefront
- front
    - can't be done efficiently with just enqueue and dequeue
- note: dequeue != deque. DEQue stands for Double Ended Queue


-- --


Binary Numbers
--------------
> Generate all binary numbers upto $d$ digits.

- Keep 2 queues
- print 0
- Start with [1]
- pop and print
- append both 0 and 1 to it, and append to queue
- how to append to number? $\displaystyle x = 10x + 0, 10x + 1$

```
0
1
10 11
11 100 101
100 101 110 111
...
```

K-ary numbers
-------------
> Given N
> Print first N positive numbers, whose digits are either 1, 2, 3
> 
> output: 1 2 3 11 12 13 21 22 23 31 ...

-- --


Some Tree:
```
1          2           3
11 12 13  21 22 23   31 32 33
```
- BFS: level order traversal: Queue
- DFS: stack 

-- --


Implementations
---------------

**Queue using Array**
- front pointer
- read pointer
- enqueue: insert after rear. increment rear
- dequeue: return front. increment front
- issue: wasted space
    - empty space, but overflow
    - can be fixed by using a circular queue


**Queue using Stacks**
- enqueue: push  $O(1)$
- dequeue: pop all into auxillary. pop and return top of auxillary. push all back again  $O(n)$


What is we want dequeue to be fast, but enqueue can be slow?

- enqueue: pop all into auxillary stack. Push x. Pop and push all into original
- dequeue: pop



**Stack using Queue**
- push: enqueue  $O(1)$
- pop: dequeue all into auxillary queue. Make sure you don't dequeue last element. Copy back values  $O(n)$


Similarly, complexities can be reversed here too


-- --


Circular Queue using Array:
---------------------------

```
1 2 3 4 _ _
dequeue 3 times
enqueue 5, 6, 7

Failure, even though empty place is available
```

- Draw it circularly
- use mod with size to keep track of front and rear

```python
def __init__(N):
    N
    front = rear = -1

def enqueue(x): 
    if (rear + 1) % N == front:
        raise Overflow
    elif front == -1:
        front, rear = 0, 0
        queue[rear] = x 
    else:
        rear = (rear + 1) % N
        queue[rear] = x

def dequeue(self):
    if front == -1:
        raise Underflow
    elif front == rear:  
        x = queue[front] 
        front, rear = -1, -1
        return x
    else:
        x = queue[front] 
        front = (front + 1) % N
        return x
```


-- --


Doubly Ended Queue
------------------

- insert_front
- insert_last
- delete_front
- delete_last

Standard implementations in all languages (usually circular and array)
Just google and use.

- use array implementation vs linked list implementation
- array
    - space efficient
    - cache - locality of reference
    - can't increase size easily
    - vector
        - amortized O(1) if double
- linked list
    - can increase size easily
    - space inefficient
    - easier to distribute over multiple machines

-- --
Window Max
----------

> Given A[n]
> Given $k$
> Find max element for every $k$ size window


**Naive**

Keep window of size $k$. Calculate max every time.  
$O(nk)$

**Optimized**

Given
```
9 1 3 2 8 6 3 ...
```
window of size 6

- The 8 doesn't allow windows after 9 to have other maxes. So max can't be 1, 3, 2
- So we need to maintain the useful (decreasing) elements

- Read array from left to write and maintain the decreasing elements. So we need push_front
- But when some element in the window becomes useless, pop it from the left. So we need remove_last
- So we can use deque



```
N = 9, k = 3
10   1   2   9   7   6   5   11   3
\------------/








```

- first element of the useful elements is the max.
- pop from last if the element cant be part of next window. So, store indexes

$O(n)$



**Variation**

output max + min for every window of size k