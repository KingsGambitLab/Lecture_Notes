# Volatile Keyword
---

## Recap of Basics
- Interleaving: When threads start and pause, in the same blocks as other threads, this is called interleaving.
- The execution of multiple threads happens in arbitrary order. The order in which threads execute can't be guranteed.

## Atomic Action 
An action that effectively happens all at once - either it happens completely or doesn't happen at all. 

Even increments and decrements aren't atomic, nor are all primitive assignments.
Example - Long and double assignments may not be atomic on all virtual machines.

## Thread Safe Code
An object or a block of code is thread-safe, if it is not comprised by execution of concurrent threads. 
This means the correctness and consistency of program's output or its visible state, is unaffected by other threads.
Atomic Operations and immutable objects are examples of thread-safe code.

In real life, there are shared resources which are available to multiple concurrent threads in real time. We have techniques, to control acess to the resources to prevent affects of interleaving threads. These technicques are - 
1) Synchronisation/Locking
2) Volatile Keyword

### Problem 1 - Atomicity/Synchronization
... alreaedy seen ...


### Problem 2 - Memory Inconsistency Errors, Data Races 
The Operating system may read from heap variables, and make a copy of the value in each thread's own storage.  Each threads has its own small and fast memory storage, that holds its own copy of shared resource's value.

Once thread can modify a shared variable, but this change might not be immediately reflected or visible. Instead it is first update in thread's local cache. The operating system may not flush the first thread's changes to the heap, until the thread has finished executing, causing memory inconsistency errors. 

### Solution - Volatile Keyword
- The volatile keyword is used as modifier for class variables.
- It's an indicator that this variable's value may be changed by multiple threads.
- This modifier ensures that the variable is always read from, and written to the main memory, rather than from any thread-specific cache.
- This provides memory consistency for this variables value across threads.
Volatile doesn't gurantee atomicicty. 

However, volatile does not provide atomicity or synchronization, so additional synchronization mechanisms should be used in conjunction with it when necessary.

**When to use volatile**
- When a variable is used to track the state of a shared resource, such as counter or a flag.
- When a varaible is used to communicate between threads.

**When not use volatile**
- When the variable is used by single thread.
- When a variable is used to store a large amount of data.







