# Java Strings - Advanced Concepts
In this tutorial we discuss 3 important concepts related to Strings.
- String Pool 
- String Immutability 
- String Builder


String are handled differently in Java.  There are two ways to store strings - one as string literals stored in String Pool and as string objects stored in regular heap space. Lets discuss about them.

### 1. Strings in String Pool
Each time you create a string literal, the JVM checks the "string constant pool" first. If the string already exists in the pool, a reference to the pooled instance is returned. If the string doesn't exist in the pool, a new string instance is created and placed in the pool. For example:

**String Literal Syntax**
```java
String s1 = "Hello World";  
String s2 = "Hello World";//It doesn't create a new instance  
``` 
![](https://www.baeldung.com/wp-content/uploads/2018/08/Why_String_Is_Immutable_In_Java.jpg)

In the above example, only one object will be created. Firstly, JVM will not find any string object with the value "Hello World" in string constant pool that is why it will create a new object. After that it will find the string with the value "Hello World" in the pool, it will not create a new object but will return the reference to the same instance.

**Java String Pool** is the special memory region where Strings are stored by the JVM. Since Strings are immutable in Java, the JVM optimizes the amount of memory allocated for them by storing only one copy of each literal String in the pool. This process is called interning

### 2. String Allocated Using the Constructor
When we create a String via the new operator, the Java compiler will create a new object and store it in the heap space reserved for the JVM.

Every String created like this will point to a different memory region with its own address.

Let’s see how this is different from the previous case:

```java
String s1 = new String("Welcome");
String s2 = new String("Welcome");
//creates two objects and two reference variables point to different addresses 
```
---
### Big Question - String Literal vs String Object?
We have just seen that when we create a String object using the `new()` operator, it always creates a new object in heap memory. On the other hand, if we create an object using String literal syntax e.g. “Hello World”, it may return an existing object from the String pool, if it already exists. Otherwise, it will create a new String object and put in the string pool for future re-use.

At a high level, both are the String objects, but the main difference comes from the point that new() operator always creates a new String object. Also, when we create a String using literal – it is interned.

In general, we should use the String literal notation when possible. It is easier to read and it gives the compiler a chance to optimize our code.

----

## Immutablibity of Java Strings

*Immutable* simply means unmodifiable or unchangeable. This means that once the object has been assigned to a variable, we can neither update the reference nor change the internal state by any means.

In Java, Strings are immutable. An obvious question that is quite prevalent in interviews is “Why Strings are designed as immutable in Java?” The key benefits of keeping this class as immutable are caching, security, synchronization, and performance.

Let’s discuss how these things work.

#### Why String objects are immutable in Java?
As Java uses the concept of String literal. Suppose there are 5 reference variables, all refer to one object "Sachin". If one reference variable changes the value of the object, it will be affected by all the reference variables. That is why String objects are immutable in Java.

Following are some more features of String which makes String objects immutable.

**1. Heap Space**
The immutability of String helps to minimize the usage in the heap memory. When we try to declare a new String object, the JVM checks whether the value already exists in the String pool or not. If it exists, the same value is assigned to the new object. This feature allows Java to use the heap space efficiently.

Java String Pool is the special memory region where Strings are stored by the JVM. Since Strings are immutable in Java, the JVM optimizes the amount of memory allocated for them by storing only one copy of each literal String in the pool. This process is called **interning**

**2. Security**
The String is widely used in Java applications to store sensitive pieces of information like usernames, passwords, connection URLs, network connections, etc. It’s also used extensively by JVM class loaders while loading classes.

Hence securing String class is crucial regarding the security of the whole application in general. For example, consider this simple code snippet:

```java
void criticalMethod(String userName) {
    // perform security checks
    if (!isAlphaNumeric(userName)) {
        throw new SecurityException(); 
    }
	
    // do some secondary tasks
    initializeDatabase();
	
    // critical task
    connection.executeUpdate("UPDATE Customers SET Status = 'Active' " +
      " WHERE UserName = '" + userName + "'");
}
```

In the above code snippet, let’s say that we received a String object from an untrustworthy source. We’re doing all necessary security checks initially to check if the String is only alphanumeric, followed by some more operations.

Remember that our unreliable source caller method still has reference to this userName object.

If Strings were mutable, then by the time we execute the update, we can’t be sure that the String we received, even after performing security checks, would be safe. The untrustworthy caller method still has the reference and can change the String between integrity checks. Thus making our query prone to SQL injections in this case. So mutable Strings could lead to degradation of security over time.

It could also happen that the String userName is visible to another thread, which could then change its value after the integrity check.

**3. Synchronization**
Being immutable automatically makes the String thread safe since they won’t be changed when accessed from multiple threads.

Hence immutable objects, in general, can be shared across multiple threads running simultaneously. They’re also thread-safe because if a thread changes the value, then instead of modifying the same, a new String would be created in the String pool. Hence, Strings are safe for multi-threading.

**4. Hashcode Caching**
Since String objects are abundantly used as a data structure, they are also widely used in hash implementations like HashMap, HashTable, HashSet, etc. When operating upon these hash implementations, hashCode() method is called quite frequently for bucketing.

The immutability guarantees Strings that their value won’t change. So the hashCode() method is overridden in String class to facilitate caching, such that the hash is calculated and cached during the first hashCode() call and the same value is returned ever since.

This, in turn, improves the performance of collections that uses hash implementations when operated with String objects.

On the other hand, mutable Strings would produce two different hashcodes at the time of insertion and retrieval if contents of String was modified after the operation, potentially losing the value object in the Map.

-----

# String Builder Class

String builder is a class that represents a *mutable sequence* of characters. 
Both StringBuilder and StringBuffer create objects that hold a mutable sequence of characters. Let’s see how this works, and how it compares to an immutable String class:

```java
String immutable = "abc";
immutable = immutable + "def";
```
Even though it may look like that we’re modifying the same object by appending “def”, we are creating a new one because String instances can’t be modified.

When using either StringBuffer or StringBuilder, we can use the append() method:
```java
StringBuffer sb = new StringBuffer("abc");
sb.append("def");
```
In this case, there was no new object created. We have called the append() method on sb instance and modified its content. StringBuffer and StringBuilder are mutable objects.

You can look at more methods available in string buffer at [official documentation](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StringBuilder.html).

Some of the commonly used methods are `toString()`, `insert()`, 'delete()',`append()`, `getChars()` etc.


**String Builder Demo**
```java
public class StringBuilderExample {

    static void generateString(){
        String s = "";
        //Adding to String Object
        // Inffecient Runs in O(n*n)
        for(int i=0; i<100000;i++){
            s = s + (char)('A' + i); //inefficient
        }
        return s;
    }

    static void generateStringUsingSB(){
        StringBuilder sb = new StringBuilder();
        //Efficient
        //Runs in O(N)
        for(int i=0; i<100000;i++){
            sb.append((char)('A' + i)); //efficient
        }
       return sb.toString();
    }

    public static void main(String[] args) {
        //you can do a time comparison for both
        long start = System.currentTimeMillis();
        generateStringUsingSB();
        long end = System.currentTimeMillis();
        System.out.println(end-start);
    }

```


**String Buffer vs String Builder**
StringBuffer is synchronized and therefore thread-safe. StringBuilder is compatible with StringBuffer API but with no guarantee of synchronization.Because it’s not a thread-safe implementation, it is faster and it is recommended to use it in places where there’s no need for thread safety


Simply put, the StringBuffer is a thread-safe implementation and therefore slower than the StringBuilder. In single-threaded programs, we can take of the StringBuilder. Yet, the performance gain of StringBuilder over StringBuffer may be too small to justify replacing it everywhere. 


