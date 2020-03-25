## Queue

- Linear Data Structure
- First In first Out

### Operations:

(Mention overflow and underflow conditions)
- Enqueue()
- Dequeue()

### Applications

- CPU Scheduling
- Disk Scheduling
- In real life scenario, Call Center phone systems uses Queues to hold people calling them in an order, until a service representative is free.

### Implementation

- Array

  Maintain two pointers: Front and end. 
  Both will point to -1 in the end.
  Enqueue -> rear, Deequeue -> front
  
  Problems  
  
    - not being able to dynamically resize. 
    - front becomes equal to rear even when array is empty. 
    
- Circular Array

```cpp

class Queue {
	int *arr;
	int ms; // max size
	int cs; // current size
	int front;
	int rear;
public:
	Queue(int default_size = 4) {
		front = 0;
		rear = default_size-1;
		ms = default_size;
		arr = new int[ms];
		cs = 0;
	}
	bool isFull() {
		return cs==ms;
	}
	bool isEmpty() {
		return cs == 0;
	}
	void enqueue(int data) {
		if(!isFull()) {
			rear = (rear+1)%ms;
			arr[rear] = data;
			cs++;
		}
	}
	void dequeue() {
		if(!isEmpty()) {
			front = (front+1)%ms;
			cs--;
		}
	}
	int getFront() {
		return arr[front];
	}
};

```

- LinkedList

	Enqueue - Add at head. O(n) if no tail pointer otherwise O(1)
	Dequeue - O(1)
	
- Stack ( 2 ways of implementation )


### Double Ended Queue

- A very powerful data structure. 
	insertFront(): Adds an item at the front of Deque.
	insertLast(): Adds an item at the rear of Deque.
	deleteFront(): Deletes an item from front of Deque.
	deleteLast(): Deletes an item from rear of Deque.
	
- Supports both stack and queue operations. 

- Implementation of Circular Double Ended Queue

  - Circular Array
  - Doubly LinkedList
  
**Q1 - Print all binary numbers upto d digits**
Input: 3
Output: 0 1 10 11 100 101 110 111

**Q2- Given some N, and some digits 1, 2...k, find the first N numbers that can be formed from these digits. 

Note: You can do level order traversal (BFS) using queue. 
    
**Q3- Given arr[n] and window size k, find max for every window of size k. 

static void printMax(int arr[], int n, int k) 
    { 
        
        Deque<Integer> Qi = new LinkedList<Integer>(); 
  
       
        int i; 
        for (i = 0; i < k; ++i) { 
           
            while (!Qi.isEmpty() && arr[i] >= arr[Qi.peekLast()]) 
                Qi.removeLast(); // Remove from rear 
  
            
            Qi.addLast(i); 
        } 
  
        
        for (; i < n; ++i) { 
           
            System.out.print(arr[Qi.peek()] + " "); 
  
           
            while ((!Qi.isEmpty()) && Qi.peek() <= i - k) 
                Qi.removeFirst(); 

            while ((!Qi.isEmpty()) && arr[i] >= arr[Qi.peekLast()]) 
                Qi.removeLast(); 
  
            // Add current element at the rear of Qi 
            Qi.addLast(i); 
        } 
  
        // Print the maximum element of last window 
        System.out.print(arr[Qi.peek()]); 
    } 

**Q4- Given a stream of characters and we have to find first non repeating character each time a character is inserted to the stream**
```java
    static void firstNonRepeating(String str) 
    { 
        int[] charCount = new int[MAX_CHAR]; 
        Queue<Character> q = new LinkedList<Character>(); 
        for (int i = 0; i < str.length(); i++) { 
            char ch = str.charAt(i);
            q.add(ch); 
            charCount[ch - 'a']++;  
            while (!q.isEmpty()) { 
                if (charCount[q.peek() - 'a'] > 1) 
                    q.remove(); 
                else { 
                    System.out.print(q.peek() + " "); 
                    break; 
                } 
            } 
            if (q.isEmpty()) 
                System.out.print(-1 + " "); 
        } 
        System.out.println(); 
    } 
```
**Q5- Shortest Subarray with Sum at Least K**



 

