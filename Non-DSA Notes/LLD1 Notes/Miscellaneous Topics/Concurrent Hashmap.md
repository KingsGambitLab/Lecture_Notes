# Concurrent Hashmap

Java Collections provides various data structures for working with key-value pairs. The commonly used ones are  - 
- **Hashmap** (Non-Synchronised, Not Thread Safe)
    - discuss the Synchronized Hashmap method
    
- **Hashtable** (Synchronised, Thread Safe)
    - locking over entire table
    
- **Concurrent Hashmap** (Synchronised, Thread Safe, Higher Level of Concurrency, Faster)
    - locking at bucket level, fine grained locking

**Hashmap and Synchronised Hashmap Method**
Synchronization is the process of establishing coordination and ensuring proper communication between two or more activities. Since a HashMap is not synchronized which may cause data inconsistency, therefore, we need to synchronize it. The in-built method ‘Collections.synchronizedMap()’ is a more convenient way of performing this task.

A synchronized map is a map that can be safely accessed by multiple threads without causing concurrency issues. On the other hand, a Hash Map is not synchronized which means when we implement it in a multi-threading environment, multiple threads can access and modify it at the same time without any coordination. This can lead to data inconsistency and unexpected behavior of elements. It may also affect the results of an operation.

Therefore, we need to synchronize the access to the elements of Hash Map using ‘synchronizedMap()’. This method creates a wrapper around the original HashMap and locks it whenever a thread tries to access or modify it.

```java
Collections.synchronizedMap(instanceOfHashMap);
```

The `synchronizedMap()` is a static method of the Collections class that takes an instance of HashMap collection as a parameter and returns a synchronized Map from it. However,it is important to note that only the map itself is synchronized, not its views such as keyset and entrySet. Therefore, if we want to iterate over the synchronized map, we need to use a synchronized block or a lock to ensure exclusive access.

```java
import java.util.*;
public class Maps {
   public static void main(String[] args) {
      HashMap<String, Integer> cart = new HashMap<>();
      // Adding elements in the cart map
      cart.put("Butter", 5);
      cart.put("Milk", 10);
      cart.put("Rice", 20);
      cart.put("Bread", 2);
      cart.put("Peanut", 2);
      // printing synchronized map from HashMap
      Map mapSynched = Collections.synchronizedMap(cart);
      System.out.println("Synchronized Map from HashMap: " + mapSynched);
   }
}
```

**Hashtable vs Concurrent Hashmap**
HashMap is generally suitable for single threaded applications and is faster than Hashtable, however in multithreading environments we have you use **Hashtable** or **Concurrent Hashmap**. So let us talk about them.

While both Hashtable and Concurrent Hashmap collections offer the advantage of thread safety, their underlying architectures and capabilities significantly differ. Whether we’re building a legacy system or working on modern, microservices-based cloud applications, understanding these nuances is critical for making the right choice.

Let's see the differences between Hashtable and ConcurrentHashMap, delving into their performance metrics, synchronization features, and various other aspects to help us make an informed decision.

**1. Hashtable**
Hashtable is one of the oldest collection classes in Java and has been present since JDK 1.0. It provides key-value storage and retrieval APIs:

```java
Hashtable<String, String> hashtable = new Hashtable<>();
hashtable.put("Key1", "1");
hashtable.put("Key2", "2");
hashtable.putIfAbsent("Key3", "3");
String value = hashtable.get("Key2");
```
**The primary selling point of Hashtable is thread safety, which is achieved through method-level synchronization**.

Methods like put(), putIfAbsent(), get(), and remove() are synchronized. Only one thread can execute any of these methods at a given time on a Hashtable instance, ensuring data consistency.

**2. Concurrent Hashmap**
ConcurrentHashMap is a more modern alternative, introduced with the Java Collections Framework as part of Java 5.

Both Hashtable and ConcurrentHashMap implement the Map interface, which accounts for the similarity in method signatures:
```java
ConcurrentHashMap<String, String> concurrentHashMap = new ConcurrentHashMap<>();
concurrentHashMap.put("Key1", "1");
concurrentHashMap.put("Key2", "2");
concurrentHashMap.putIfAbsent("Key3", "3");
String value = concurrentHashMap.get("Key2");
```

ConcurrentHashMap, on the other hand, provides thread safety with a higher level of concurrency. It allows multiple threads to read and perform limited writes simultaneously **without locking the entire data structure**. This is especially useful in applications that have more read operations than write operations.

**Performance Comparison**
Hashtable locks the entire table during a write operation, thereby preventing other reads or writes. This could be a bottleneck in a high-concurrency environment.

ConcurrentHashMap, however, allows concurrent reads and limited concurrent writes, making it more scalable and often faster in practice.
