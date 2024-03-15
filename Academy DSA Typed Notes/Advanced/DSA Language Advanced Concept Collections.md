# Language Advanced Concept: Collections

---

## Java Collections Framework


* Any group of individual objects which are represented as a single unit is known as a collection of objects.
* A framework is a set of classes and interfaces which provide a ready-made architecture.
* **The Java Collections Framework (JCF)** is a set of classes and interfaces that implement commonly reusable collection data structures like **List, Set, Queue, Map, etc**. The JCF is organized into interfaces and implementations of those interfaces. The interfaces define the functionality of the collection data structures, and the implementations provide concrete implementations of those interfaces.

### Need for a Separate Collection Framework in Java

* Before the Collection Framework(or before JDK 1.2) was introduced, the standard methods for grouping Java objects (or collections) were **Arrays or Vectors, or Hashtables**. 
* All of these collections had no common interface. Therefore, though the main aim of all the collections is the same, the implementation of all these collections was defined independently and had no correlation among them. Hence, it is very difficult for the users to remember all the different methods, syntax, and constructors present in every collection class.
* Let’s understand this with an example of adding an element in a hashtable and a vector. 

```java
// Java program to demonstrate
// why collection framework was needed
import java.io.*;
import java.util.*;
 
class CollectionDemo {
 
    public static void main(String[] args)
    {
        // Creating instances of the array,
        // vector and hashtable
        int arr[] = new int[] { 1, 2, 3, 4 };
        Vector<Integer> v = new Vector();
        Hashtable<Integer, String> h = new Hashtable();
 
        // Adding the elements into the
        // vector
        v.addElement(1);
        v.addElement(2);
 
        // Adding the element into the
        // hashtable
        h.put(1, "geeks");
        h.put(2, "4geeks");
 
        // Array instance creation requires [],
        // while Vector and hastable require ()
        // Vector element insertion requires addElement(),
        // but hashtable element insertion requires put()
 
        // Accessing the first element of the
        // array, vector and hashtable
        System.out.println(arr[0]);
        System.out.println(v.elementAt(0));
        System.out.println(h.get(1));
 
        // Array elements are accessed using [],
        // vector elements using elementAt()
        // and hashtable elements using get()
    }
}
```

---


### Advantages of Java Collections Framework

The advantages of using the JCF are:

* **Consistent API** - The API has a basic set of interfaces like Collection, Set, List, or Map, all the classes (ArrayList, LinkedList, Vector, etc) that implement these interfaces have some common set of methods.
* **Reduces programming effort** - A programmer doesnʼt have to worry about the design of the Collection but rather he can focus on its best use in his program. Therefore, the basic concept of Object-oriented programming (i.e.) abstraction has been successfully implemented.
* **Increases program speed and quality** - Increases performance by providing high-performance implementations of useful data structures and algorithms because in this case, the programmer need not think of the best implementation of a specific data structure. He can simply use the best implementation to drastically boost the performance of his algorithm/program.


---
### Hierarchy of the Java Collection Framework



* The utility package, (java.util) contains all the classes and interfaces that are required by the collection framework.
* The collection framework contains an interface named an **iterable interface** which provides the iterator to iterate through all the collections. This interface is extended by the main collection interface which acts as a root for the collection framework. All the collections extend this collection interface thereby extending the properties of the iterator and the methods of this interface.
* In Java, Collection interface (java.util.Collection) and Map interface (java.util.Map) are the two main “root” interfaces of Java collection classes.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/057/499/original/JCFHierarchy.png?1700552931" width=600>

### Iterable Interface
* This is the root interface for the entire collection framework. The collection interface extends the iterable interface. Therefore, inherently, all the interfaces and classes implement this interface. The main functionality of this interface is to provide an iterator for the collections. Therefore, this interface contains only one abstract method which is the iterator. It returns the 
```
Iterator iterator();
```

---


### Collection Interface

* The Collection interface is the root interface of the Java Collections Framework. It is the foundation upon which the collection framework is built. It declares the core methods that all collections will have. The
* Collection interface is a part of the java.util package.
* The JDK does not provide any direct implementations of this interface: it provides implementations of more specific sub-interfaces like Set and List. This interface is typically used to pass collections around and manipulate them where maximum generality is desired.
* The Collection interface is not directly implemented by any class. However, it is implemented indirectly via its subtypes or subinterfaces like List, Queue, and Set. For Example, the HashSet class implements the Set interface which is a subinterface of the Collection interface.
* It implements the Iterable interface.

### Methods of Collection Interface

The Collection interface includes various methods that can be used to perform different operations on objects. These methods are available in all its subinterfaces.

* **add()** - inserts the specified element to the collection
* **size()** - returns the size of the collection
* **remove()** - removes the specified element from the collection
* **iterator()** - returns an iterator to access elements of the collection
* **addAll()** - adds all the elements of a specified collection to the collection
* **removeAll()** - removes all the elements of the specified collection from the collection
* **clear()** - removes all the elements of the collection


---

### Interfaces that extend the Collections Interface

We are going to learn about the following SubInterfaces that extends the Collections Interface : 
1. **List :** This interface is dedicated to the data of the list type in which we can store all the ordered collection of the objects. This also allows duplicate data to be present in it.
2. **Set:** A set is an unordered collection of objects in which duplicate values cannot be stored. This collection is used when we wish to avoid the duplication of the objects and wish to store only the unique objects. 
3. **SortedSet:** This interface is very similar to the set interface. The only difference is that this interface has extra methods that maintain the ordering of the elements. The sorted set interface extends the set interface and is used to handle the data which needs to be sorted.
4. **Map** : A map is a data structure that supports the key-value pair for mapping the data. This interface doesn’t support duplicate keys because the same key cannot have multiple mappings, however, it allows duplicate values in different keys. A map is useful if there is data and we wish to perform operations on the basis of the key.
5. **Queue:** As the name suggests, a queue interface maintains the FIFO(First In First Out) order similar to a real-world queue line. This interface is dedicated to storing all the elements where the order of the elements matter. For example, whenever we try to book a ticket, the tickets are sold at the first come first serve basis. Therefore, the person whose request arrives first into the queue gets the ticket.
6. **Deque:** This is a very slight variation of the queue data structure. Deque, also known as a double-ended queue, is a data structure where we can add and remove the elements from both the ends of the queue. This interface extends the queue interface.

Let's start going through each one in details one by one.

---


### List Interface

* The **List** interface is a child of **Collection** Interface.The List interface is found in **java.util** package and inherits the Collection interface.
* It is an ordered collection of objects in which duplicate values can be stored. Since List preserves the insertion order, it allows positional access and insertion of elements. 
* The implementation classes of the List interface are ArrayList, LinkedList, Vector and Stack. ArrayList and LinkedList are widely used in Java programming.

* ### Declaration of Java List Interface
    ```
    public interface List<E> extends Collection<E> ; 
    ```
* Since List is an interface, objects cannot be created of the type list. We always need a class that implements this List in order to create an object.
* The list interface is implemented by the following Classes : 
    1. **ArrayList** - Resizable-array implementation of the List interface
    2. **Vector** - Synchronized resizable-array implementation of the List interface
    3. **Stack** - Subclass of Vector that implements a standard last-in, first-out stack
    4. **LinkedList** - Doubly-linked list implementation of the List and Deque interfaces

Let us discuss them sequentially and implement the same to figure out the working of the classes with the List interface. 


---


### ArrayList

* An ArrayList in Java is implemented as a resizable array, also known as a dynamic array. It provides an interface to work with a dynamically sized list of elements, allowing for efficient insertion, deletion, and random access. Here's how an ArrayList is typically implemented:

1. **Backing Array**: The core of an ArrayList is an underlying array that holds the elements. This array is initially created with a default size, and elements are stored sequentially in it.
2. **Resizing**: As elements are added to the ArrayList, the backing array may become full. When this happens, a new larger array is created, and the existing elements are copied from the old array to the new one. This process is called resizing or resizing the array.
3. **Dynamic Sizing**: The resizing operation ensures that the ArrayList can dynamically grow or shrink in size as needed. This dynamic sizing is a key feature that differentiates it from a regular array.
4. **Index-Based Access**: ArrayList allows elements to be accessed by their index. This is achieved by directly accessing the corresponding element in the backing array using the index.
5. **Insertion and Deletion**: When an element is inserted at a specific index or removed from the ArrayList, the other elements may need to be shifted to accommodate the change. This can involve moving multiple elements within the array.
6. **Efficiency**: ArrayList provides efficient constant-time (O(1)) access to elements by index. However, insertion or deletion operations at the beginning or middle of the list may require shifting elements and take linear time (O(n)), where n is the number of elements.
7. **Automatic Resizing**: Java's ArrayList uses automatic resizing strategies to ensure that the array is appropriately resized when needed. The exact resizing strategy can vary across different implementations and versions of Java.


Let’s see how to create a list object using this class : 

```java
// Java program to demonstrate the
// creation of list object using the
// ArrayList class
 
import java.io.*;
import java.util.*;
 
class ListObjectUsingArrayList {
    public static void main(String[] args)
    {
        // Size of ArrayList
        int n = 5;
 
        // Declaring the List with initial size n
        List<Integer> arr = new ArrayList<Integer>(n);
 
        // Appending the new elements
        // at the end of the list
        for (int i = 1; i <= n; i++)
            arr.add(i);
 
        // Printing elements
        System.out.println(arr);
 
        // Remove element at index 3
        arr.remove(3);
 
        // Displaying the list after deletion
        System.out.println(arr);
 
        // Printing elements one by one
        for (int i = 0; i < arr.size(); i++)
            System.out.print(arr.get(i) + " ");
    }
}
```

---


### Vector

* A vector provides us with dynamic arrays in Java. Though, it may be slower than standard arrays but can be helpful in programs where lots of manipulation in the array is needed. This is identical to ArrayList in terms of implementation. However, the primary difference between a vector and an ArrayList is that a Vector is synchronized and an ArrayList is non-synchronized. 

Let’s understand the Vector with an example:

```java
// Java program to demonstrate the
// creation of list object using the
// Vector class
 
import java.io.*;
import java.util.*;
 
class ListObjectUsingVector {
    public static void main(String[] args)
    {
        // Size of the vector
        int n = 5;
 
        // Declaring the List with initial size n
        List<Integer> v = new Vector<Integer>(n);
 
        // Appending the new elements
        // at the end of the list
        for (int i = 1; i <= n; i++)
            v.add(i);
 
        // Printing elements
        System.out.println(v);
 
        // Remove element at index 3
        v.remove(3);
 
        // Displaying the list after deletion
        System.out.println(v);
 
        // Printing elements one by one
        for (int i = 0; i < v.size(); i++)
            System.out.print(v.get(i) + " ");
    }
}
```

---
## Stack


* Stack is a class that is implemented in the collection framework and extends the vector class models and implements the Stack data structure. The class is based on the basic principle of last-in-first-out. In addition to the basic push and pop operations, the class provides three more functions of empty, search and peek. 

Let’s see how to create a list object using this class : 

```java
// Java program to demonstrate the
// creation of list object using the
// Stack class
 
import java.io.*;
import java.util.*;
 
class ListObjectUsingStack {
    public static void main(String[] args)
    {
        // Size of the stack
        int n = 5;
 
        // Declaring the List
        List<Integer> stackObject = new Stack<Integer>();
 
        // Appending the new elements
        // at the end of the list
        for (int i = 1; i <= n; i++)
            stackObject.add(i);
 
        // Printing elements
        System.out.println(stackObject);
 
        // Remove element at index 3
        stackObject.remove(3);
 
        // Displaying the list after deletion
        System.out.println(stackObject);
 
        // Printing elements one by one
        for (int i = 0; i < stackObject.size(); i++)
            System.out.print(stackObject.get(i) + " ");
    }
}
```

---
## Linked List


* LinkedList is a class that is implemented in the collection framework which inherently implements the **linked list data structure**. 
* It is a linear data structure where the elements are not stored in contiguous locations and every element is a separate object with a data part and address part. 
* The elements are linked using pointers and addresses. Each element is known as a node. Due to the dynamicity and ease of insertions and deletions, they are preferred over the arrays.

Let’s see how to create a list object using this class : 

```java
// Java program to demonstrate the
// creation of list object using the
// LinkedList class
 
import java.io.*;
import java.util.*;
 
class ListObjectUsingLinkedList {
    public static void main(String[] args)
    {
        // Size of the LinkedList
        int n = 5;
 
        // Declaring the List with initial size n
        List<Integer> ll = new LinkedList<Integer>();
 
        // Appending the new elements
        // at the end of the list
        for (int i = 1; i <= n; i++)
            ll.add(i);
 
        // Printing elements
        System.out.println(ll);
 
        // Remove element at index 3
        ll.remove(3);
 
        // Displaying the list after deletion
        System.out.println(ll);
 
        // Printing elements one by one
        for (int i = 0; i < ll.size(); i++)
            System.out.print(ll.get(i) + " ");
    }
}
```

---
## Set Interface


* The Set interface extends the Collection interface. It represents the unordered set of elements which doesn't allow us to store the duplicate items. 
* We can store at most one null value in Set.
* This interface contains the methods inherited from the Collection interface and adds a feature that restricts the insertion of the duplicate elements.

* ## Declaration of Set Interface : 

```java
public interface Set extends Collection 
```
* **HashSet** is one of the widely used classes which implements the Set interface.
* We will learn about the implementation of HashSet in the future classes.

Now, let’s see how to perform a few frequently used operations on the HashSet. We are going to perform the following operations as follows:

Adding elements
Accessing elements
Removing elements
Iterating elements
Iterating through Set

**Adding Elements**
```java
// Java Program Demonstrating Working of Set by 
// Adding elements using add() method  
  
// Importing all utility classes 
import java.util.*; 
  
// Main class 
class HashSetClass { 
  
    // Main driver method 
    public static void main(String[] args) 
    { 
        // Creating an object of Set and  
        // declaring object of type String 
        Set<String> hs = new HashSet<String>(); 
  
        // Adding elements to above object 
        // using add() method 
        hs.add("B"); 
        hs.add("B"); 
        hs.add("C"); 
        hs.add("A"); 
  
        // Printing the elements inside the Set object 
        System.out.println(hs); 
    } 
}
```
**Accessing the Elements**
```java
// Java code to demonstrate Working of Set by 
// Accessing the Elements of the Set object 
  
// Importing all utility classes 
import java.util.*; 
  
// Main class 
class HashSetClass { 
  
    // Main driver method 
    public static void main(String[] args) 
    { 
        // Creating an object of Set and  
        // declaring object of type String 
        Set<String> hs = new HashSet<String>(); 
  
        // Elements are added using add() method 
        // Later onwards we will show accessing the same 
  
        // Custom input elements 
        hs.add("A"); 
        hs.add("B"); 
        hs.add("C"); 
        hs.add("A"); 
  
        // Print the Set object elements 
        System.out.println("Set is " + hs); 
  
        // Declaring a string 
        String check = "D"; 
  
        // Check if the above string exists in 
        // the SortedSet or not 
        // using contains() method 
        System.out.println("Contains " + check + " "
                           + hs.contains(check)); 
    } 
}
```
**Removing the Values**
```java
// Java Program Demonstrating Working of Set by 
// Removing Element/s from the Set 
  
// Importing all utility classes 
import java.util.*; 
  
// Main class 
class HashSetClass { 
  
    // Main driver method 
    public static void main(String[] args) 
    { 
        // Declaring object of Set of type String 
        Set<String> hs = new HashSet<String>(); 
  
        // Elements are added 
        // using add() method 
  
        // Custom input elements 
        hs.add("A"); 
        hs.add("B"); 
        hs.add("C"); 
        hs.add("B"); 
        hs.add("D"); 
        hs.add("E"); 
  
        // Printing initial Set elements 
        System.out.println("Initial HashSet " + hs); 
  
        // Removing custom element 
        // using remove() method 
        hs.remove("B"); 
  
        // Printing Set elements after removing an element 
        // and printing updated Set elements 
        System.out.println("After removing element " + hs); 
    } 
}
```
**Iterating through the Set**
```java
// Java Program to Demonstrate Working of Set by  
// Iterating through the Elements  
  
// Importing utility classes  
import java.util.*; 
  
// Main class  
class HashSetClass { 
  
    // Main driver method 
    public static void main(String[] args) 
    { 
        // Creating object of Set and declaring String type 
        Set<String> hs = new HashSet<String>(); 
  
        // Adding elements to Set   
        // using add() method 
  
        // Custom input elements  
        hs.add("A"); 
        hs.add("B"); 
        hs.add("C"); 
        hs.add("B"); 
        hs.add("D"); 
        hs.add("E"); 
  
        // Iterating through the Set 
        // via for-each loop  
        for (String value : hs) 
  
            // Printing all the values inside the object  
            System.out.print(value + ", "); 
          
        System.out.println(); 
    } 
}
```

### LinkedHashSet

* LinkedHashSet class which is implemented in the collections framework is an ordered version of HashSet that maintains a doubly-linked List across all elements. 
* When the iteration order is needed to be maintained this class is used. When iterating through a HashSet the order is unpredictable, while a LinkedHashSet lets us iterate through the elements in the order in which they were inserted. 

Let’s see how to create a set object using this class : 
```java
// Java program to demonstrate the 
// creation of Set object using 
// the LinkedHashset class 
import java.util.*; 
  
class LinkedHashSetClass { 
  
    public static void main(String[] args) 
    { 
        Set<String> lh = new LinkedHashSet<String>(); 
  
        // Adding elements into the LinkedHashSet 
        // using add() 
        lh.add("India"); 
        lh.add("Australia"); 
        lh.add("South Africa"); 
  
        // Adding the duplicate 
        // element 
        lh.add("India"); 
  
        // Displaying the LinkedHashSet 
        System.out.println(lh); 
  
        // Removing items from LinkedHashSet 
        // using remove() 
        lh.remove("Australia"); 
        System.out.println("Set after removing "
                           + "Australia:" + lh); 
  
        // Iterating over linked hash set items 
        System.out.println("Iterating over set:"); 
        Iterator<String> i = lh.iterator(); 
        while (i.hasNext()) 
            System.out.println(i.next()); 
    } 
}
```
---


### Sorted Set Interface

* The SortedSet interface present in java.util package extends the Set interface present in the collection framework. It is an interface that implements the mathematical set.
* This interface contains the methods inherited from the Set interface and adds a feature that stores all the elements in this interface to be stored in a sorted manner.


* ### Declaration of Sorted Set Interface
```java
public interface SortedSet extends Set
```
* TreeSet class is the implementation of SortedSet interface.

### TreeSet

* TreeSet class which is implemented in the collections framework and implementation of the SortedSet Interface and SortedSet extends Set Interface.
* It behaves like a simple set with the exception that it stores elements in a sorted format. TreeSet uses a tree data structure for storage. 
* Objects are stored in sorted, ascending order. But we can iterate in descending order using the method TreeSet.descendingIterator().

Let’s see how to create a set object using this class.

```java
// Java Program Demonstrating Creation of Set object 
// Using the TreeSet class 
  
// Importing utility classes 
import java.util.*; 
  
// Main class 
class TreeSetExample { 
  
    // Main driver method 
    public static void main(String[] args) 
    { 
        // Creating a Set object and declaring it of String 
        // type 
        // with reference to TreeSet 
        Set<String> ts = new TreeSet<String>(); 
  
        // Adding elements into the TreeSet 
        // using add() 
        ts.add("India"); 
        ts.add("Australia"); 
        ts.add("South Africa"); 
  
        // Adding the duplicate 
        // element 
        ts.add("India"); 
  
        // Displaying the TreeSet 
        System.out.println(ts); 
  
        // Removing items from TreeSet 
        // using remove() 
        ts.remove("Australia"); 
        System.out.println("Set after removing "
                           + "Australia:" + ts); 
  
        // Iterating over Tree set items 
        System.out.println("Iterating over set:"); 
        Iterator<String> i = ts.iterator(); 
  
        while (i.hasNext()) 
            System.out.println(i.next()); 
    } 
}
```

---
## Map Interface

* In Java, Map Interface is present in java.util package represents a mapping between a key and a value. Java Map interface is not a subtype of the Collection interface. Therefore it behaves a bit differently from the rest of the collection types. 
* A map contains unique keys.
* Since Map is an interface, objects cannot be created of the type map.
* There are 2 Map Interface : 
    * Map
    * SortedMap
* There are 3 class implementations of maps : 
    * HashMap
    * LinkedHashMap
    * TreeMap
* A Map cannot contain duplicate keys and each key can map to at most one value. Some implementations allow null key and null values like the HashMap and LinkedHashMap, but some do not like the TreeMap.
* The order of a map depends on the specific implementations. For example, TreeMap and LinkedHashMap have predictable orders, while HashMap does not.

### HashMap
* HashMap provides the basic implementation of the Map interface of Java. It stores the data in (Key, Value) pairs.
* To access a value one must know its key.
* This class uses a technique called Hashing. Hashing is a technique of converting a large String to a small String that represents the same String. A shorter value helps in indexing and faster searches.
 
Let’s see how to create a map object using this class.
```java
// Java Program to illustrate the Hashmap Class 
  
// Importing required classes 
import java.util.*; 
  
// Main class 
public class MapObjectUsingHashMap { 
  
    // Main driver method 
    public static void main(String[] args) 
    { 
  
        // Creating an empty HashMap 
        Map<String, Integer> map = new HashMap<>(); 
  
        // Inserting entries in the Map 
        // using put() method 
        map.put("vishal", 10); 
        map.put("sachin", 30); 
        map.put("vaibhav", 20); 
  
        // Iterating over Map 
        for (Map.Entry<String, Integer> e : map.entrySet()) 
  
            // Printing key-value pairs 
            System.out.println(e.getKey() + " "
                               + e.getValue()); 
    } 
}
```
### LinkedHashMap
* LinkedHashMap is just like HashMap with the additional feature of maintaining an order of elements inserted into it. 
* HashMap provided the advantage of quick insertion, search, and deletion but it never maintained the track and order of insertion which the LinkedHashMap provides where the elements can be accessed in their insertion order.

Let’s see how to create a map object using this class.

```java
// Java Program to Illustrate the LinkedHashmap Class 
  
// Importing required classes 
import java.util.*; 
  
// Main class 
public class MapObjectUsingHashMap { 
  
    // Main driver method 
    public static void main(String[] args) 
    { 
  
        // Creating an empty LinkedHashMap 
        Map<String, Integer> map = new LinkedHashMap<>(); 
  
        // Inserting pair entries in above Map 
        // using put() method 
        map.put("vishal", 10); 
        map.put("sachin", 30); 
        map.put("vaibhav", 20); 
  
        // Iterating over Map 
        for (Map.Entry<String, Integer> e : map.entrySet()) 
  
            // Printing key-value pairs 
            System.out.println(e.getKey() + " "
                               + e.getValue()); 
    } 
}
```


### TreeMap
* The map is sorted according to the natural ordering of its keys, or by a Comparator provided at map creation time, depending on which constructor is used. This proves to be an efficient way of sorting and storing the key-value pairs.

Let’s see how to create a map object using this class.

```java
// Java Program to Illustrate TreeMap Class 
  
// Importing required classes 
import java.util.*; 
  
// Main class 
public class MapObjectUsingTreeMap { 
  
    // Main driver method 
    public static void main(String[] args) 
    { 
  
        // Creating an empty TreeMap 
        Map<String, Integer> map = new TreeMap<>(); 
  
        // Inserting custom elements in the Map 
        // using put() method 
        map.put("vishal", 10); 
        map.put("sachin", 30); 
        map.put("vaibhav", 20); 
  
        // Iterating over Map using for each loop 
        for (Map.Entry<String, Integer> e : map.entrySet()) 
  
            // Printing key-value pairs 
            System.out.println(e.getKey() + " "
                               + e.getValue()); 
    } 
}
```

---


### Queue Interface
* The Queue interface is present in java.util package and extends the Collection interface is used to hold the elements about to be processed in FIFO(First In First Out) order.
* It is an ordered list of objects with its use limited to inserting elements at the end of the list and deleting elements from the start of the list, (i.e.), it follows the FIFO or the First-In-First-Out principle.

* ### Declaration of Queue Interface
```java
public interface Queue extends Collection
```

**Creating Queue Objects**
* Since Queue is an interface, objects cannot be created of the type queue. We always need a class which extends this list in order to create an object.
* PriorityQueue and LinkedList are the classes that implements the Queue interface.

Let's look at an example to explore how to create a class using this object.

### LinkedList

```java
import java.util.LinkedList;
import java.util.Queue;
 
public class QueueExample {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();
 
        // add elements to the queue
        queue.add("apple");
        queue.add("banana");
        queue.add("cherry");
 
        // print the queue
        System.out.println("Queue: " + queue);
 
        // remove the element at the front of the queue
        String front = queue.remove();
        System.out.println("Removed element: " + front);
 
        // print the updated queue
        System.out.println("Queue after removal: " + queue);
 
        // add another element to the queue
        queue.add("date");
 
        // peek at the element at the front of the queue
        String peeked = queue.peek();
        System.out.println("Peeked element: " + peeked);
 
        // print the updated queue
        System.out.println("Queue after peek: " + queue);
    }
}
```


### PriorityQueue
Let’s see how to perform a few frequently used operations on the queue using the Priority Queue class.

**1. Adding Elements:** 
In order to add an element in a queue, we can use the add() method. The insertion order is not retained in the PriorityQueue. The elements are stored based on the priority order which is ascending by default. 

```java
// Java program to add elements
// to a Queue
 
import java.util.*;
 
public class PriorityQueueClass {
 
    public static void main(String args[])
    {
        Queue<String> pq = new PriorityQueue<>();
 
        pq.add("Geeks");
        pq.add("For");
        pq.add("Geeks");
 
        System.out.println(pq);
    }
}
```

**2. Removing Elements:** 
In order to remove an element from a queue, we can use the remove() method. If there are multiple such objects, then the first occurrence of the object is removed. Apart from that, poll() method is also used to remove the head and return it. 
```java
// Java program to remove elements
// from a Queue
 
import java.util.*;
 
public class PriorityQueueClass {
 
    public static void main(String args[])
    {
        Queue<String> pq = new PriorityQueue<>();
 
        pq.add("Geeks");
        pq.add("For");
        pq.add("Geeks");
 
        System.out.println("Initial Queue " + pq);
 
        pq.remove("Geeks");
 
        System.out.println("After Remove " + pq);
 
        System.out.println("Poll Method " + pq.poll());
 
        System.out.println("Final Queue " + pq);
    }
}
```

**3. Iterating the Queue:** 
There are multiple ways to iterate through the Queue. The most famous way is converting the queue to the array and traversing using the for loop. However, the queue also has an inbuilt iterator which can be used to iterate through the queue. 
```java
// Java program to iterate elements
// to a Queue
 
import java.util.*;
 
public class PriorityQueueClass {
 
    public static void main(String args[])
    {
        Queue<String> pq = new PriorityQueue<>();
 
        pq.add("Geeks");
        pq.add("For");
        pq.add("Geeks");
 
        Iterator iterator = pq.iterator();
 
        while (iterator.hasNext()) {
            System.out.print(iterator.next() + " ");
        }
    }
}
```



---
## Deque Interface

* Deque interface present in java.util package is a subtype of the queue interface. The Deque is related to the double-ended queue that supports the addition or removal of elements from either end of the data structure. It can either be used as a queue(first-in-first-out/FIFO) or as a stack(last-in-first-out/LIFO). Deque is the acronym for double-ended queue.
* The Deque (double-ended queue) interface in Java is a subinterface of the Queue interface and extends it to provide a double-ended queue, which is a queue that allows elements to be added and removed from both ends.
### Declaration of Dequeue Interface
```java
public interface Deque extends Queue
```

* Since Deque is an interface, objects cannot be created of the type deque. We always need a class that extends this list in order to create an object. 
* ArrayDeque is the class that implements the Dequeue interface

Example : 
```java
// Java program to demonstrate the working
// of a Deque in Java
 
import java.util.*;
 
public class DequeExample {
    public static void main(String[] args)
    {
        Deque<String> deque
            = new LinkedList<String>();
 
        // We can add elements to the queue
        // in various ways
 
        // Add at the last
        deque.add("Element 1 (Tail)");
 
        // Add at the first
        deque.addFirst("Element 2 (Head)");
 
        // Add at the last
        deque.addLast("Element 3 (Tail)");
 
        // Add at the first
        deque.push("Element 4 (Head)");
 
        // Add at the last
        deque.offer("Element 5 (Tail)");
 
        // Add at the first
        deque.offerFirst("Element 6 (Head)");
 
        System.out.println(deque + "\n");
 
        // We can remove the first element
        // or the last element.
        deque.removeFirst();
        deque.removeLast();
        System.out.println("Deque after removing "
                        + "first and last: "
                        + deque);
    }
}
```
---
## Comparables

* The Comparable interface in Java is used to define a natural ordering for a class. When a class implements the Comparable interface, it provides a way to compare instances of that class with each other.
* This natural ordering is primarily used for sorting elements in various collections like TreeSet or when using sorting algorithms like Collections.sort().
* The Comparable interface contains a single method:
```java
int compareTo(T other)
```
* Here, T represents the type of objects being compared. The compareTo method should return a negative integer, zero, or a positive integer based on whether the current object is less than, equal to, or greater than the object being compared (other).
* For example, consider a Person class that implements the Comparable interface to define a natural ordering based on age:

```java
import java.util.*;

class Person implements Comparable<Person> {
    
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
     }

    @Override
     public int compareTo(Person other) {
         return Integer.compare(this.age, other.age);
    }
    
}
```

* Now, instances of the Person class can be easily compared and sorted using their natural ordering (in this case, based on age) without explicitly providing a separate comparator. This is particularly useful when working with collections that require sorting or maintaining a natural order, such as TreeSet or Collections.sort().

---
### Comparators


* In Java, a Comparator is an interface that provides a way to define custom ordering for objects in collections, such as lists or sets. It allows you to specify how elements should be compared and sorted based on specific criteria that you define. The Comparator interface is particularly useful when you want to sort objects in a way that differs from their natural order or when dealing with classes that don't implement the Comparable interface.
* Here's how the Comparator interface is typically used:
    * **Creating a Comparator**: You can create a class that implements the Comparator interface. This class should provide the logic for comparing two objects based on the desired criteria.
    * **Comparison Logic**: The Comparator interface requires you to implement the compare method, which takes two objects as parameters and returns a negative, zero, or positive integer depending on whether the first object is less than, equal to, or greater than the second object, respectively. This method allows you to define the custom ordering logic
    * Using the Comparator: Once you have a Comparator implementation, you can use it in various ways:
        * **Sorting collections**: You can pass the Comparator to sorting methods like Collections.sort() or Arrays.sort() to sort the elements in the desired order.
        * **Creating sorted collections**: You can create collections (like TreeSet or PriorityQueue) that maintain elements in a sorted order using the provided Comparator.
        * **Custom sorting**: You can use the Comparator to perform custom sorting tasks based on specific use cases.

Here's a simple example of how you might use a Comparator to sort a list of Person objects based on
their ages: 

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Person {
    
    String name;
    int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

class AgeComparator implements Comparator<Person> {

    @Override
    public int compare(Person person1, Person person2) {
        return Integer.compare(person1.age, person2.age);
    }
}

public class ComparatorExample {
    
    public static void main(String[] args) {

        List<Person> people = new ArrayList<>();
        
        people.add(new Person("Alice", 28));
        people.add(new Person("Bob", 22));
        people.add(new Person("Charlie", 25));
        
        // Sort the list using the AgeComparator
        Collections.sort(people, new AgeComparator());
        
        // Iterate the List of people and check if it is now sorted on the basis of age or not.
        for (Person person : people) {
            System.out.println(person.name + " - " + person.age);
        }
    }
}
```

* In this example, the AgeComparator class implements the Comparator interface to compare Person objects based on their ages. 
* The Collections.sort() method uses the AgeComparator to sort the list of Person objects. This allows you to customize the sorting behavior without modifying the Person class itself.

