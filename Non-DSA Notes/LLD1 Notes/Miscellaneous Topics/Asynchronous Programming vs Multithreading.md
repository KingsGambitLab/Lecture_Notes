# Asynchronous Programming vs Multithreading 
---


## Asynchronous Programming
Asynchronous programming is a programming paradigm that allows tasks to be executed independently without blocking the main thread. It focuses on managing the flow of the program by handling tasks concurrently and efficiently.  It's commonly used to improve the responsiveness of applications by avoiding long-running operations that might otherwise cause the user interface to freeze. Java provides several mechanisms for asynchronous programming, and in this tutorial, we'll cover the basics using - Threads, CompletableFuture and the ExecutorService.

### 1. Threads
We can create a new thread to perform any operation asynchronously. With the release of lambda expressions in Java 8, it’s cleaner and more readable.

Let’s create a new thread that computes and prints the factorial of a number:
```java
public class ThreadExample {
    public static int factorial(int n){

        System.out.println(Thread.currentThread().getName() + "is running");

        try{
            Thread.sleep(2000);
        }
        catch(InterruptedException e){
            e.printStackTrace();
        }

        int ans=1;
        for(int i=1;i<n;i++){
            ans = ans*i;
        }
        System.out.println(Thread.currentThread().getName() + "is finished");
        return ans;
    }

    public static void main(String[] args) {

        int number = 5;
        Thread newThread = new Thread(()->{
            System.out.println("Factorial of 5 " + factorial(number));
        });
        newThread.start();
        System.out.println("Main is still running-1");
    }
}
```

### 2. FutureTask 
Since Java 5, the Future interface provides a way to perform asynchronous operations using the FutureTask. We can use the submit method of the ExecutorService to perform the task asynchronously and return the instance of the FutureTask.
```java
ExecutorService threadpool = Executors.newCachedThreadPool();
Future<Long> futureTask = threadpool.submit(() -> factorial(number));

while (!futureTask.isDone()) {
    System.out.println("FutureTask is not finished yet..."); 
} 
long result = futureTask.get(); //Blocking Code
threadpool.shutdown();
```
Here we’ve used the `isDone` method provided by the Future interface to check if the task is completed. Once finished, we can retrieve the result using the get method.

### 3. CompletableFuture
CompletableFuture is a class introduced in Java 8 that provides a way to perform asynchronous operations and handle their results using a fluent API. Java 8 introduced CompletableFuture with a combination of a Future and CompletionStage. It provides various methods like supplyAsync, runAsync, and thenApplyAsync for asynchronous programming.

**Example-1**
```java
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

public class CompletableFutureExample {
    public static void main(String[] args) {
        // Create a CompletableFuture
        CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
            // Simulate a time-consuming task
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            return "Hello, CompletableFuture!";
        });

        // Attach a callback to handle the result
        future.thenAccept(result -> System.out.println("Result: " + result));

        // Wait for the CompletableFuture to complete (not recommended in real applications)
        try {
            future.get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
}
```
In this example, we use `CompletableFuture.supplyAsync` to perform a task asynchronously. The thenAccept method is used to attach a callback that will be executed when the asynchronous task completes.

**Example-2**
```
CompletableFuture<Long> completableFuture = CompletableFuture.supplyAsync(() -> factorial(number));
while (!completableFuture.isDone()) {
    System.out.println("CompletableFuture is not finished yet...");
}
long result = completableFuture.get();
```
We don’t need to use the ExecutorService explicitly. The CompletableFuture internally uses ForkJoinPool to handle the task asynchronously. Thus, it makes our code a lot cleaner.


### Uses of Asynchronous Programming:

- IO-Intensive Operations: Asynchronous programming is often used for tasks that involve waiting for external resources, such as reading from or writing to files, making network requests, or interacting with databases.
- Responsive UI: In GUI applications, asynchronous programming helps in maintaining a responsive user interface by executing time-consuming tasks in the background.

- Callback Mechanism: Asynchronous programming often uses callbacks or combinators to specify what should happen once a task is complete.

- Composability: It emphasizes composability, allowing developers to chain together multiple asynchronous operations.

```java
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> "Hello, CompletableFuture!");

// Attach a callback to handle the result
future.thenAccept(result -> System.out.println("Result: " + result));
```

### Multi-threading 
Multithreading involves the concurrent execution of two or more threads to achieve parallelism. It is a fundamental concept for optimizing CPU-bound tasks and improving overall system performance. Key Components for achieving multithreading in Java are thread class and Executor Framework.

- Thread Class: Java provides the Thread class for creating and managing threads.
- Executor Framework: The ExecutorService and related interfaces offer a higher-level abstraction for managing thread pools.

### Use Case of Multithreading:

- CPU-Intensive Operations: Multithreading is suitable for tasks that are CPU-bound and can benefit from parallel execution, such as mathematical computations.

- Parallel Processing: Multithreading can be used to perform multiple tasks simultaneously, making efficient use of available CPU cores.

### Shared State and Synchronization:

- Shared State: In multithreading, threads may share data, leading to potential issues like race conditions and data corruption.

- Synchronization: Techniques like synchronization, locks, and atomic operations are used to ensure proper coordination between threads.

Example using ExecutorService:
```java
ExecutorService executorService = Executors.newFixedThreadPool(2);

// Submit a task for execution
Future<String> future = executorService.submit(() -> "Hello, ExecutorService!");

// Retrieve the result when ready
try {
    String result = future.get(); // This will block until the result is available
    System.out.println("Result: " + result);
} catch (Exception e) {
    e.printStackTrace();
}


// Shutdown the ExecutorService
executorService.shutdown();
```

### Summary
### Asynchronous Programming:
- Focuses on non-blocking execution.
- Primarily used for IO-bound tasks and maintaining responsive applications.
- Utilizes higher-level abstractions like CompletableFuture.
- Emphasizes composability and chaining of asynchronous operations.

### Multithreading:
- Focuses on parallelism for CPU-bound tasks.
- Suitable for tasks that can be executed concurrently.
- Utilizes threads and thread pools, managed by the Thread class and ExecutorService.
- Requires attention to synchronization and shared state management.

In some scenarios, asynchronous programming and multithreading can be used together to achieve both parallelism and non-blocking execution, depending on the nature of the tasks in an application.
