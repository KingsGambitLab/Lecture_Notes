### Java Streams
A stream in Java is simply a wrapper around a data source, allowing us to perform bulk operations on the data in a convenient way.

It doesn’t store data or make any changes to the underlying data source. Rather, it adds support for functional-style operations on data pipelines.

In this tutorial we will learn about Sequential Streams, Parallel Streams and Collect() Method of stream.

### Sequential Streams
By default, any stream operation in Java is processed sequentially, unless explicitly specified as parallel.

Sequential streams use a single thread to process the pipeline:
```java
List<Integer> listOfNumbers = Arrays.asList(1, 2, 3, 4);
listOfNumbers.stream().forEach(number ->
    System.out.println(number + " " + Thread.currentThread().getName())
);
```
The output of this sequential stream is predictable. The list elements will always be printed in an ordered sequence:

```
1 main
2 main
3 main
4 main
```

### Multithreading using Parallel Streams
Stream API also simplifies multithreading by providing the `parallelStream()` method that runs operations over stream’s elements in parallel mode. Any stream in Java can easily be transformed from sequential to parallel.

We can achieve this by adding the parallel method to a sequential stream or by creating a stream using the parallelStream method of a collection:

The code below allows to run method doWork() in parallel for every element of the stream:
```java
list.parallelStream().forEach(element -> doWork(element));
```
For the above sequential example, the code will looks like this -

```java
List<Integer> listOfNumbers = Arrays.asList(1, 2, 3, 4);
listOfNumbers.parallelStream().forEach(number ->
    System.out.println(number + " " + Thread.currentThread().getName())
);
```
Parallel streams enable us to execute code in parallel on separate cores. The final result is the combination of each individual outcome.

However, the order of execution is out of our control. It may change every time we run the program:
```
4 ForkJoinPool.commonPool-worker-3
2 ForkJoinPool.commonPool-worker-5
1 ForkJoinPool.commonPool-worker-7
3 main
```
Parallel streams make use of the fork-join framework and its common pool of worker threads. Parallel processing may be beneficial to fully utilize multiple cores. But we also need to consider the overhead of managing multiple threads, memory locality, splitting the source and merging the results.
Refer this [Article](https://www.baeldung.com/java-when-to-use-parallel-stream) to learn more about when to use parallel streams.

`

### Collect() Method

A stream represents a sequence of elements and supports different kinds of operations that lead to the desired result. The source of a stream is usually a Collection or an Array, from which data is streamed from.

Streams differ from collections in several ways; most notably in that the streams are not a data structure that stores elements. They're functional in nature, and it's worth noting that operations on a stream produce a result and typically return another stream, but do not modify its source.

To "solidify" the changes, you **collect** the elements of a stream back into a Collection.

The `stream.collect()` method is used to perform a mutable reduction operation on the elements of a stream. It returns a new mutable object containing the results of the reduction operation.

This method can be used to perform several different types of reduction operations, such as:

- Computing the sum of numeric values in a stream.
- Finding the minimum or maximum value in a stream.
- Constructing a new String by concatenating the contents of a stream.
- Collecting elements into a new List or Set.

```java
public class CollectExample {
   public static void main(String[] args) {
      Integer[] intArray = {1, 2, 3, 4, 5};  

      // Creating a List from an array of elements
      // using Arrays.asList() method
      List<Integer> list = Arrays.asList(intArray);
     
      // Demo1: Collecting all elements of the list into a new 
      // list using collect() method 
      List<Integer> evenNumbersList = list.stream()
            .filter(i -> i%2 == 0)
            .collect(toList());
      System.out.println(evenNumbersList);

      // Demo2: finding the sum of all the values 
      // in the stream
      Integer sum = list.stream()
         .collect(summingInt(i -> i));
      System.out.println(sum);

      // Demo3: finding the maximum of all the values 
      // in the stream
      Integer max = list.stream()
         .collect(maxBy(Integer::compare)).get();
      System.out.println(max);

      // Demo4: finding the minimum of all the values 
      // in the stream
      Integer min = list.stream()
         .collect(minBy(Integer::compare)).get();
      System.out.println(min);

      // Demo5: counting the values in the stream
      Long count = list.stream()
         .collect(counting());
      System.out.println(count);
   }
}
```

In Demo1:  We use the stream() method to get a stream from the list. We filter the even elements and collect them into a new list using the collect() method.

In Demo2: We use the collect() method summingInt(ToIntFunction) as an argument. The summingInt() method returns a collector that sums the integer values extracted from the stream elements by applying an int producing mapping function to each element.

In Demo 3: We use the collect() method with maxBy(Comparator) as an argument. The maxBy() accepts a Comparator and returns a collector that extracts the maximum element from the stream according to the given Comparator.

Lets learn more about Collectors.


### Collectors and Stream.Collect()

Collectors represent implementations of the Collector interface, which implements various useful reduction operations, such as accumulating elements into collections, summarizing elements based on a specific parameter, etc.

All predefined implementations can be found within the [Collectors](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Collectors.html) class.


Within the Collectors class itself, we find an abundance of unique methods that deliver on the different needs of a user. One such group is made of summing methods - `summingInt()`, `summingDouble()` and `summingLong()`.



Let's start off with a basic example with a List of Integers:

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
Integer sum = numbers.stream().collect(Collectors.summingInt(Integer::intValue));
System.out.println("Sum: " + sum);
```
We apply the .stream() method to create a stream of Integer instances, after which we use the previously discussed `.collect()` method to collect the elements using `summingInt()`. The method itself, again, accepts the `ToIntFunction`, which can be used to reduce instances to an integer that can be summed.

Since we're using Integers already, we can simply pass in a method reference denoting their `intValue`, as no further reduction is needed.

More often than not - you'll be working with lists of custom objects and would like to sum some of their fields. For instance, we can sum the quantities of each product in the productList, denoting the total inventory we have.

Let us try to understand one of these methods using a custom class example.
``` java
public class Product {
    private String name;
    private Integer quantity;
    private Double price;
    private Long productNumber;

    // Constructor, getters and setters
    ...
}
...
List<Product> products = Arrays.asList(
        new Product("Milk", 37, 3.60, 12345600L),
        new Product("Carton of Eggs", 50, 1.20, 12378300L),
        new Product("Olive oil", 28, 37.0, 13412300L),
        new Product("Peanut butter", 33, 4.19, 15121200L),
        new Product("Bag of rice", 26, 1.70, 21401265L)
);

```

In such a case, the we can use a method reference, such as `Product::getQuantity` as our `ToIntFunction`, to reduce the objects into a single integer each, and then sum these integers:

```java
Integer sumOfQuantities = products.stream().collect(Collectors.summingInt(Product::getQuantity));
System.out.println("Total number of products: " + sumOfQuantities);
```
This results in:

```
Total number of products: 174
```

You can also very easily implement your own collector and use it instead of the predefined ones, though - you can get pretty far with the built-in collectors, as they cover the vast majority of cases in which you might want to use them.

The following are examples of using the predefined collectors to perform common mutable reduction tasks:
```java

     // Accumulate names into a List
     List<String> list = people.stream().map(Person::getName).collect(Collectors.toList());

     // Accumulate names into a TreeSet
     Set<String> set = people.stream().map(Person::getName).collect(Collectors.toCollection(TreeSet::new));

     // Convert elements to strings and concatenate them, separated by commas
     String joined = things.stream()
                           .map(Object::toString)
                           .collect(Collectors.joining(", "));

     // Compute sum of salaries of employee
     int total = employees.stream()
                          .collect(Collectors.summingInt(Employee::getSalary)));

     // Group employees by department
     Map<Department, List<Employee>> byDept
         = employees.stream()
                    .collect(Collectors.groupingBy(Employee::getDepartment));

     // Compute sum of salaries by department
     Map<Department, Integer> totalByDept
         = employees.stream()
                    .collect(Collectors.groupingBy(Employee::getDepartment,
                                                   Collectors.summingInt(Employee::getSalary)));

     // Partition students into passing and failing
     Map<Boolean, List<Student>> passingFailing =
         students.stream()
                 .collect(Collectors.partitioningBy(s -> s.getGrade() >= PASS_THRESHOLD));
                 
```
You can look at the offical documentation for more details on these methods.
https://docs.oracle.com/javase/8/docs/api/java/util/stream/Collectors.html




