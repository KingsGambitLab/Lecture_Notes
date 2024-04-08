### Threads in Java Recap
In the Java, multithreading is driven by the core concept of a Thread. Lets recap some logic that runs in a parallel thread by using the Thread framework. In the below code example we are creating two threads and running them in parallel.

**Using Thread Class**
```java
public class NewThread extends Thread {
    public void run() {
            // business logic 
            ...
        }
    }
}
```
Class to initialize and start our thread.

```java
public class MultipleThreadsExample {
    public static void main(String[] args) {
        NewThread t1 = new NewThread();
        t1.setName("MyThread-1");
        NewThread t2 = new NewThread();
        t2.setName("MyThread-2");
        t1.start();
        t2.start();
    }
}
```

**Using Runnable**
```java
class SimpleRunnable implements Runnable {
	public void run() {
        // business logic
    }
}
```
The above SimpleRunnable is just a task which we want to run in a separate thread.
There’re various approaches we can use for running it; one of them is to use the Thread class:

```java
public void test(){
    Thread thread = new Thread(new SimpleRunnable());
    thread.start();
    thread.join();
}
```

Simply put, we generally encourage the use of Runnable over Thread:

When extending the Thread class, we’re not overriding any of its methods. Instead, we override the method of Runnable (which Thread happens to implement). 
- This is a clear violation of IS-A Thread principle
- Creating an implementation of Runnable and passing it to the Thread class utilizes composition and not inheritance – which is more flexible
- After extending the Thread class, we can’t extend any other class
- From Java 8 onwards, Runnables can be represented as lambda expressions

### Thread Life Cycle 
During thread lifecycle, threads go through various states. The `java.lang.Thread` class contains a static State enum – which defines its potential states. During any given point of time, the thread can only be in one of these states:

- **NEW** – a newly created thread that has not yet started the execution
- **RUNNABLE** – either running or ready for execution but it’s waiting for resource allocation
- **BLOCKED** – waiting to acquire a monitor lock to enter or re-enter a synchronized block/method
- **WAITING** – waiting for some other thread to perform a particular action without any time limit
- **TIMED_WAITING** – waiting for some other thread to perform a specific action for a specified period
- **TERMINATED** – has completed its execution

#### 1.NEW
A NEW Thread (or a Born Thread) is a thread that’s been created but not yet started. It remains in this state until we start it using the start() method.

The following code snippet shows a newly created thread that’s in the NEW state:

```java
Runnable runnable = new NewState();
Thread t = new Thread(runnable);
System.out.println(t.getState());
```

Since we’ve not started the mentioned thread, the method `t.getState()` prints:
```
NEW
```

### 2. Runnable 
When we’ve created a new thread and called the start() method on that, it’s moved from NEW to RUNNABLE state. Threads in this state are either running or ready to run, but they’re waiting for resource allocation from the system.

In a multi-threaded environment, the Thread-Scheduler (which is part of JVM) allocates a fixed amount of time to each thread. So it runs for a particular amount of time, then leaves the control to other RUNNABLE threads.

For example, let’s add `t.start()` method to our previous code and try to access its current state:

```java
Runnable runnable = new NewState();
Thread t = new Thread(runnable);
t.start();
System.out.println(t.getState());
```

This code is most likely to return the output as:
```
RUNNABLE
```
Note that in this example, it’s not always guaranteed that by the time our control reaches `t.getState()`, it will be still in the RUNNABLE state.

It may happen that it was immediately scheduled by the Thread-Scheduler and may finish execution. In such cases, we may get a different output.

### 3. BLOCKED
A thread is in the BLOCKED state when it’s currently not eligible to run. It enters this state when it is waiting for a monitor lock and is trying to access a section of code that is locked by some other thread.

Let’s try to reproduce this state:
```java
public class BlockedState {
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new DemoBlockedRunnable());
        Thread t2 = new Thread(new DemoBlockedRunnable());
        
        t1.start();
        t2.start();
        
        Thread.sleep(1000); //pause so that t2 states changes during this time
        System.out.println(t2.getState());
        System.exit(0);
    }
}

class DemoBlockedRunnable implements Runnable {
    @Override
    public void run() {
        commonResource();
    }
    
    public static synchronized void commonResource() {
        while(true) {
            // Infinite loop to mimic heavy processing
            // 't1' won't leave this method
            // when 't2' try to enter this
        }
    }
}
```
In this code:

We’ve created two different threads – t1 and t2, t1 starts and enters the synchronized commonResource() method; this means that only one thread can access it; all other subsequent threads that try to access this method will be blocked from the further execution until the current one will finish the processing.

When t1 enters this method, it is kept in an infinite while loop; this is just to imitate heavy processing so that all other threads cannot enter this method

Now when we start t2, it tries to enter the commonResource() method, which is already being accessed by t1, thus, t2 will be kept in the BLOCKED state.
Being in this state, we call `t2.getState()` and get the output as:
```
BLOCKED
```

### 4. WAITING
A thread is in WAITING state when it’s waiting for some other thread to perform a particular action. According to JavaDocs, any thread can enter this state by calling any one of the following three methods:

- object.wait()
- thread.join() or
- LockSupport.park()

Note that in wait() and join() – we do not define any timeout period as that scenario is covered in the next section.


In this example, thread-1 starts thread 2 and waits for thread-2 to finish using `thread.join()` method. During this time t1 is in `WAITING` state. 

**Simple Runnable.java - Thread 1**
```java
public class SimpleRunnable implements Runnable{

    @Override
    public void run(){
        Thread t2 = new Thread(new SimpleRunnableTwo());
        t2.start();
        try {
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

```

**Simple Runnable 2 - Thread 2**
```java
public class SimpleRunnableTwo implements Runnable {
    @Override
    public void run() {
        try{
            Thread.sleep(5000);
        }
        catch(InterruptedException e){
            Thread.currentThread().interrupt();
            e.printStackTrace();
        }

    }
}
```
**Main**
```java
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new SimpleRunnable());
        t1.start();

        Thread.sleep(1000); //1ms pause
        System.out.println("T1 :"+ t1.getState()); //T1 is waiting state
        System.out.println("Main :" + Thread.currentThread().getState());
    }
}
```

### 5. TIMED WAITING
A thread is in `TIMED_WAITING` state when it’s waiting for another thread to perform a particular action within a stipulated amount of time.

According to JavaDocs, there are five ways to put a thread on TIMED_WAITING state:

- thread.sleep(long millis)
- wait(int timeout) or wait(int timeout, int nanos)
- thread.join(long millis)
- LockSupport.parkNanos
- LockSupport.parkUntil

Here, we’ve created and started a thread t1 which is entered into the sleep state with a timeout period of 5 seconds; the output will be `TIMED_WAITING`.

```java
public class SimpleRunnable implements Runnable{
    @Override
    public void run() {
        try{
            Thread.sleep(5000);
        }
        catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}

```
In Main, if you check the state of T1 after 2s it will be `TIMED WAITING`
```java
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new SimpleRunnable());
        t1.start();

        Thread.sleep(2000);
        System.out.println(t1.getState());
    }
}
```


### 6. TERMINATED
This is the state of a dead thread. It’s in the `TERMINATED` state when it has either finished execution or was terminated abnormally. There are different ways of terminating a thread.

Let’s try to achieve this state in the following example:
```java
public class TerminatedState implements Runnable {
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new TerminatedState());
        t1.start();
       
        // The following sleep method will give enough time for 
        // thread t1 to complete
        Thread.sleep(1000);
        System.out.println(t1.getState());
    }
    
    @Override
    public void run() {
        // No processing in this block
        
    }
}
```
Here, while we’ve started thread t1, the very next statement Thread.sleep(1000) gives enough time for t1 to complete and so this program gives us the output as:
```
TERMINATED
```






