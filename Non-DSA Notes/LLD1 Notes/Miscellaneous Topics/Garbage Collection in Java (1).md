
# Chapter - Garbage Collection in Java
-----


### Introduction

One of the reasons that make Java as a robust programming language is its memory management. Memory management can be a difficult, tedious task in traditional programming environments. For example, in C/C++, the programmer will often manually allocate and free dynamic memory. This sometimes leads to problems, because programmers will either forget to free memory that has been previously allocated or, worse, try to free some memory that another part of their code is still using. Java virtually eliminates these problems by managing memory allocation and deallocation for you. In fact, deallocation is completely automatic, because Java provides garbage collection for unused objects. In this tutorial, we will study the following topics.

**Part-I** 
- Java Memory Model (Stack and Heap)
- Need for Garbage Collection (Operations, Benefits, Disadvantanges)
- Benefits and Disadvantages of GC 

**Part-II** 
- Memory Allocation, Defragmentation and Garbage Collection 
- Conditions for Garbage Collector to run
- Garbage Collection for Java Objects
- Handling unmanaged resources 

**Part-III**
- Choosing a Garbage Collection Algorithm 
- Understanding Mark and Sweep
- Garbage Collectors in Java 17

### Java Memory Model - Stack vs Heap
Applications need memory to run, because they need to create objects in the memory and perform computational tasks. These can be created on Stack and Heap Memory. Lets us quickly discuss the features of stack and heap memory.

Local primitive variables and reference variables to objects data types are created on stack memory and cleared automatically when the stack frame is popped after the function call gets over. Hence, everything associated when stack memory gets cleared off automatically following the LIFO order in the call stack. There is no garbage collection involved in stack memory. Because of simplicity in memory allocation (LIFO), stack memory is very fast when compared to heap memory.

```java
    func(){
        int a = 10; //here 'a' is created on stack
        int arr[] = new int[10]; 
        // here arr reference is created on stack but actual allocation is on heap
        ...
    }
```
However, you need heap memory when you need to allocate any kind of objects like arrays, user defined objects, dynamic data structures such as arraylist, strings, trees etc

Whenever an object is created, it’s always stored in the Heap space and stack memory contains the reference to it.  Objects stored in the heap are globally accessible whereas stack memory can’t be accessed by other threads. Creating objects on heap also allows passing large objects by reference across different functions, thus avoiding the need to create a copy of the object. For such objects on heap de-allocation is required for unused objects, which can be performed explicitly by invoking `delete` in langages like C++. But language like Java, Python provide support for automatic garbage collection.

 When stack memory is full, Java runtime throws `java.lang.StackOverFlowError` whereas if heap memory is full, it throws `java.lang.OutOfMemoryError: Java Heap Space error`. Stack memory size is very less when compared to Heap memory. We can use `-Xms` and `-Xmx` JVM option to define the startup size and maximum size of heap memory. We can use `-Xss` to define the stack memory size.
 

### Need for Garbage Collection

The garbage collector manages the allocation and release of memory for an application. Therefore, developers working with managed code don't have to write code to perform memory management tasks. Automatic memory management can eliminate common problems such as forgetting to free an object and causing a memory leak or attempting to access freed memory for an object that's already been freed.

**Operations performed by a Garbage Collector**
- Allocates from and gives back memory to the operating system.
- Hands out that memory to the application as it requests it.
- Determines which parts of that memory is still in use by the application.
- Reclaims the unused memory for reuse by the application.
- Running memory defragmentation.

**Benefits of Garbage Collector**
- Frees developers from having to manually release memory.
- Allocates objects on the managed heap efficiently.
- Reclaims objects that are no longer being used, clears their memory, and keeps the memory available for future allocations.
- Provides memory safety by making sure that an object can't use for itself the memory allocated for another object.
- No overhead of handling Dangling Pointer

**Disadvantages of Garbage Collector**
- Java garbage collection helps your Java environments and applications perform more efficiently. However, you can still potentially run into issues with automatic garbage collection, including degraded application performance. 
- Since JVM has to keep track of object reference creation/deletion, this activity requires more CPU power than the original application. It may affect the performance of requests which require large memory.
- Programmers have no control over the scheduling of CPU time dedicated to freeing objects that are no longer needed.
- Using some GC implementations might result in the application stopping unpredictably.


While you can’t manually override automatic garbage collection, there are things you can do to optimize garbage collection in your application environment, such as changing the garbage collector you use, removing all references to unused Java objects, tuning the parameters of Garbage collector etc.

**Memory Allocation, Defragmentation & Garbage Collection**
We’ve seen how heap memory can provide a flexible way of allocation chunks of memory on-the-go. The chunks aren’t planned ahead of time; it’s a real-time thing: when the program, for whatever reason, needs more memory, then the operating system finds an available chunk and allocates that chunk to the program.The program can use it until it’s done with that chunk, at which time it releases the chunk for later use by the same or a different program.
![](https://www.insidetheiot.com/wp-content/uploads/2019/12/Memory-hole.png)

After some time, the memory might look like this.
![](https://www.insidetheiot.com/wp-content/uploads/2019/12/Full-memory.png)

Now what? There’s enough free memory for the new allocation, but the problem is that it’s all broken up all over the place. Said another way, it’s fragmented. We really don’t want to break up the allocation and spread it over multiple holes. That would use more memory (for managing where all the pieces are), and it would slow things down.

So we’re left with the problem: how do we allocate that new chunk? We first need to reorganize the memory and move things around to get all of those holes together into a larger chunk of available memory. That means closing up the holes and “pushing” the holes to the end of the memory where they can be reused.

That process of moving things around to bring the free memory chunks together is called **defragmentation**.The process of defragmenting memory by moving multiple free “holes” in memory together so that they can be allocated more effectively.And yeah, it takes some time to do. It’s also hard to predict when it will be needed, since it all depends on who needs memory and releases memory at what time. The process is fast enough to where you may not notice it, but it can make a difference.

![](https://www.insidetheiot.com/wp-content/uploads/2019/12/Final-allocation.png)

**Pseudocode for New()**
```java
def new():
    obj = allocate() //request for memory 
    if obj == NULL:
        GC.collect() //trigger garbage collector
        obj = allocate() //re-try to allocate memory
        if obj == NULL: //no garbage was collected or not sufficient memory
            raise OutOfMemoryError 
            
    return obj
```

**Important Note** 
Garbage collection only occurs sporadically (if at all) during the execution of your program. It will not occur simply because one or more objects exist that are no longer used. Furthermore, different Java run-time implementations will take varying approaches to garbage collection, but for the most developers, you should not have to think about it while writing your programs. The classes in the **java.lang.ref** package provide more flexible control over the garbage collection process.

There are various ways in which the references to an object can be released to make it a candidate for Garbage Collection. Some of them are:

**By making a reference null**
```java
Student student = new Student();
student = null;
```

**By assigning a reference to another**
```java
Student studentOne = new Student();
Student studentTwo = new Student();
studentOne = studentTwo;
```
**Conditions for a Garbage Collector to run**
Garbage collection occurs when one of the following conditions is true:

- The system has low physical memory. The memory size is detected by either the low memory notification from the operating system or low memory as indicated by the host.

- The memory that's used by allocated objects on the managed heap surpasses an acceptable threshold. This threshold is continuously adjusted as the process runs.

- The GC.Collect() method is called. In almost all cases, you don't have to call this method because the garbage collector runs continuously. This method is primarily used for unique situations and testing.

**Handling unmanaged resources and finalize() Method**
For most of the objects your application creates, you can rely on garbage collection to perform the necessary memory management tasks automatically. However, unmanaged resources require explicit cleanup. The most common type of unmanaged resource is an object that wraps an operating system resource, such as a file handle, window handle, or network connection. Although the garbage collector can track the lifetime of a managed object that encapsulates an unmanaged resource, it doesn't have specific knowledge about how to clean up the resource. finalize() method in Java is a method of the Object class that is used to perform cleanup activity before destroying any object. It is called by Garbage collector before destroying the objects from memory. You can either use a safe handle to wrap the unmanaged resource, or override the Object.Finalize() method. `finalize()` method is called by default for every object before its deletion. This method helps Garbage Collector to close all the resources used by the object and helps JVM in-memory optimization.

-----
### Choice of a Garbage Collector Algorithm

Any garbage collection algorithm must perform 2 basic operations. One, it should be able to detect all the unreachable objects and secondly, it must reclaim the heap space used by the garbage objects and make the space available again to the program.

When does the choice of a garbage collector matter? For some applications, the answer is never. That is, the application can perform well in the presence of garbage collection with pauses of modest frequency and duration. However, this isn't the case for a large class of applications, particularly those with large amounts of data (multiple gigabytes), many threads, and high transaction rates. Garbage collectors make assumptions about the way applications use objects, and these are reflected in tunable parameters that can be adjusted for improved performance.


Here are few desirable properties of a Garbage Collector.

##### 1. Safety
A garbage collector is safe when it never reclaims the space of a LIVE object and always cleans up only the dead objects.
Although this looks like an obvious requirement, some GC algorithms claim space of LIVE objects just to gain that extra ounce of performance.

##### 2.Throughput
A garbage collector should be as little time cleaning up the garbage as possible; this way it would ensure that the CPU is spent on doing actual work and not just cleaning up the mess.
Most garbage collectors hence run small cycles frequently and a major cycle does deep cleaning once a while. This way they maximize the overall throughput and ensure we spend more time doing actual work.


##### 3.Completeness
A garbage collector is said to be complete when it eventually reclaims all the garbage from the heap.
It is not desirable to do a complete clean-up every time the GC is executed, but eventually, a GC should guarantee that the garbage is cleaned up ensuring zero memory leaks.

##### 4.Pause Time
Some garbage collectors pause the program execution during the cleanup and this induces a "pause". Long pauses affect the throughput of the system and may lead to unpredictable outcomes; so a GC is designed and tuned to minimize the pause time.
The garbage collector needs to pause the execution because it needs to either run defragmentation where the heap objects are shuffled freeing up larger contiguous memory segments.


##### 5.Space overhead
Garbage collectors require auxiliary data structures to track objects efficiently and the memory required to do so is pure overhead. An efficient GC should have this space overhead as low as possible allowing sufficient memory for the program execution.


##### 6.Language Specific Optimizations
Most GC algorithms are generic but when bundled with the programing language the GC can exploit the language patterns and object allocation nuances. So, it is important to pick the GC that can leverage these details and make its execution as efficient as possible.
For example, in some programming languages, GC runs in constant time by exploiting how objects are allocated on the heap.

##### 7.Scalability
Most GC are efficient in cleaning up a small chunk of memory, but a scalable GC would run efficiently even on a server with large RAM. Similarly, a GC should be able to leverage multiple CPU cores, if available, to speed up the execution.


Amdahl's law (parallel speedup in a given problem is limited by the sequential portion of the problem) implies that most workloads can't be perfectly parallelized; some portion is always sequential and doesn't benefit from parallelism. In the Java platform, there are currently four supported garbage collection alternatives and all but one of them, the serial GC, parallelize the work to improve performance. It's very important to keep the overhead of doing garbage collection as low as possible.

# Garbage Collection Algorithm 

A theoretical, most straightforward garbage collection algorithm iterates over every reachable object every time it runs. Any leftover objects are considered garbage. The time this approach takes is proportional to the number of live objects, which is prohibitive for large applications maintaining lots of live data.


## Mark-and-sweep Algorithm
Over the lifetime of a Java application, new objects are created and released. Eventually, some objects are no longer needed. You can say that at any point in time, the heap memory consists of two types of objects:

- Live - these objects are being used and referenced from somewhere else

- Dead - these objects are no longer used or referenced from anywhere and can be deleted.


The Java garbage collection process uses a mark-and-sweep algorithm. Here’s how that works 
There are two phases in this algorithm: *mark followed by sweep*.

- During the mark phase, the garbage collector traverses object trees starting at their roots. When an object is reachable from the root, the mark bit is set to 1 (true). Meanwhile, the mark bits for unreachable objects is unchanged (false).


![](https://www.freecodecamp.org/news/content/images/2021/01/image-76.png)


- During the sweep phase, the garbage collector traverses the heap, reclaiming memory from all items with a mark bit of 0 (false).

**What are Garbage Collection Roots?**
Garbage collectors work on the concept of Garbage Collection Roots (GC Roots) to identify live and dead objects. The garbage collector traverses the whole object graph in memory, starting from those Garbage Collection Roots and following references from the roots to other objects. 

*Object graph* is basically a dependency graph between objects.In this graph, the nodes are Java objects, and the edges are the explicit or implied references that allow a running program to "reach" other objects from a given one. It is used to determine which objects are reachable and which not, so that all unreachable objects could be made eligible for garbage collection.

----
#### Garbage Collectors in Java 17
Java 17 supports several types of garbage collectors, including the Serial GC, Parallel GC, Concurrent Mark Sweep (CMS) GC, G1 GC, and the newly-introduced Z Garbage Collector (ZGC) and Shenandoah GC. Each of these garbage collectors has unique characteristics and can be chosen based on the requirements of your Java application.  The Java garbage collectors employ various techniques to improve the efficiency of these operations:

- Java Garbage Collectors implement a generational garbage collection strategy that categorizes objects by age. Having to mark and compact all the objects in a JVM is inefficient. As more and more objects are allocated, the list of objects grows, leading to longer garbage collection times.
![](https://www.freecodecamp.org/news/content/images/size/w2400/2021/01/image-70.png)

- Use multiple threads to aggressively make operations parallel, or perform some long-running operations in the background concurrent to the application.

- Try to recover larger contiguous free memory by compacting live objects.


**1. Serial Garbage Collector**

The Serial GC, also known as the ‘single-threaded’ GC, is the simplest form of garbage collection in Java. It uses just one CPU thread for garbage collection, which means it can be efficient for applications with a small heap size (up to approximately 100MB). However, during the garbage collection process, user threads are paused, which can lead to latency issues in larger applications.  All garbage collection events are conducted serially in one thread. Compaction is executed after each garbage collection.

![](https://www.freecodecamp.org/news/content/images/size/w1600/2021/01/image-68.png)


Compacting describes the act of moving objects in a way that there are no holes between objects. After a garbage collection sweep, there may be holes left between live objects. Compacting moves objects so that there are no remaining holes. 
 To enable Serial Garbage Collector, we can use the following argument:

```java -XX:+UseSerialGC -jar Application.java```

**2. Parallel Garbage Collector**
Unlike Serial Garbage Collector, it uses multiple threads for managing heap space, but it also freezes other application threads while performing GC. The parallel collector is intended for applications with medium-sized to large-sized data sets that are run on multiprocessor or multithreaded hardware. This is the default implementation of GC in the JVM and is also known as Throughput Collector. Running the Parallel GC also causes a "stop the world event" and the application freezes. Since it is more suitable in a multi-threaded environment, it can be used when a lot of work needs to be done and long pauses are acceptable, for example running a batch job.

Multiple threads are used for minor garbage collection in the Young Generation. A single thread is used for major garbage collection in the Old Generation.
If we use this GC, we can specify maximum garbage collection threads and pause time, throughput, and footprint (heap size) using command line arguments.

```java -XX:+UseParallelGC -jar Application.java```

![](https://www.freecodecamp.org/news/content/images/size/w1600/2021/01/image-66.png)

**3. Concurrent Mark and Sweep**
This is also known as the concurrent low pause collector. Multiple threads are used for minor garbage collection using the same algorithm as Parallel. Major garbage collection is multi-threaded, like Parallel Old GC, but CMS runs concurrently alongside application processes to minimize “stop the world” events. Because of this, the CMS collector uses more CPU than other GCs. If you can allocate more CPU for better performance, then the CMS garbage collector is a better choice than the parallel collector. No compaction is performed in CMS GC.

![](https://www.freecodecamp.org/news/content/images/size/w1600/2021/01/image-67.png)


The JVM argument to use Concurrent Mark Sweep Garbage Collector is ```java -XX:+UseConcMarkSweepGC```

**4. G1 Garbage Collector**
G1 (Garbage First) Garbage Collector is designed for applications running on multi-processor machines with large memory space. It’s available from the JDK7 Update 4 and in later releases.

 When performing garbage collections, G1 shows a concurrent global marking phase (i.e. phase 1, known as Marking) to determine the liveness of objects throughout the heap.

After the mark phase is complete, G1 knows which regions are mostly empty. It collects in these areas first, which usually yields a significant amount of free space (i.e. phase 2, known as Sweeping).

```java -XX:+UseG1GC -jar Application.java```


**5. Z Garbage Collector**
The Z Garbage Collector (ZGC) is a scalable low latency garbage collector. ZGC performs all expensive work concurrently, without stopping the execution of application threads for more than 10ms, which makes is suitable for applications which require low latency and/or use a very large heap (multi-terabytes).
The Z Garbage Collector is available as an experimental feature, and is enabled with the command-line options 
```java -XX:+UnlockExperimentalVMOptions -XX:+UseZGC```

#### Conclusion
Remember, there’s no one-size-fits-all when it comes to choosing a garbage collector. A GC that works great for one application might not be the best choice for another. As with most aspects of system tuning, the best strategy often involves a mix of knowledge, experimentation, and a thorough understanding of your specific use case.

If your application doesn't have strict pause-time requirements, you should just run your application and allow the JVM to select the right collector.

Most of the time, the default settings should work just fine. If necessary, you can adjust the heap size to improve performance. If the performance still doesn't meet your goals, you can modify the collector as per your application requirements:

**Serial** - If the application has a small data set (up to approximately 100 MB) and/or it will be run on a single processor with no pause-time requirements

**Parallel** - If peak application performance is the priority and there are no pause-time requirements or pauses of one second or longer are acceptable

**CMS/G1** - If response time is more important than overall throughput and garbage collection pauses must be kept shorter than approximately one second

**ZGC** - If response time is a high priority, and/or you are using a very large heap





