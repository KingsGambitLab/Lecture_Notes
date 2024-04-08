# Functional Programming in Java
---
Functional Programming (FP) is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. In Java, functional programming features were introduced in Java 8 with the addition of lambda expressions, the `java.util.function` package, and the Stream API. Here are the key concepts of Functional Programming in Java:
- Lambda Expressions
- Functional Interfaces
- Stream API
- Immutabilitity
- Higher Order Functions
- Parallelism 

### 1. Lambda Expressions:
Lambda expressions are a concise way to represent anonymous functions. They provide a clear and concise syntax for writing functional interfaces (interfaces with a single abstract method). Lambda expressions are the cornerstone of functional programming in Java.

```java
// Traditional anonymous class
Runnable runnable1 = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello, world!");
    }
};

// Lambda expression
Runnable runnable2 = () -> System.out.println("Hello, world!");
```

### 2. Functional Interfaces:
Functional interfaces are interfaces with a single abstract method, often referred to as functional methods. They can have multiple default or static methods, but they must have only one abstract method.
```java
@FunctionalInterface
interface MyFunctionalInterface {
    void myMethod();
}
```
Lambda expressions can be used to instantiate functional interfaces:
```java
MyFunctionalInterface myFunc = () -> System.out.println("My method implementation");
```

In Java, the `java.util.function` package provides several functional interfaces that represent different types of functions. These functional interfaces are part of the functional programming support introduced in Java 8 and are commonly used with lambda expressions. Here's an explanation of some commonly used functional interfaces in Java:

##### Function<T, R>
Represents a function that takes one argument of type T and produces a result of type R.
The method `apply(T t)` is used to apply the function.
```java
Function<String, Integer> stringLengthFunction = s -> s.length();
int length = stringLengthFunction.apply("Java");
```

##### Consumer<T>
Represents an operation that accepts a single input argument of type T and returns no result. The method `accept(T t)` is used to perform the operation.
```java
Consumer<String> printUpperCase = s -> System.out.println(s.toUpperCase());
printUpperCase.accept("Java");
```

##### BiFunction<T,U,R>
Represents a function that takes two arguments of types T and U and produces a result of type R. The method `apply(T t, U u)` is used to apply the function.
```java
BiFunction<Integer, Integer, Integer> sumFunction = (a, b) -> a + b;
int sum = sumFunction.apply(3, 5);
```
##### Predicate<T>
Represents a predicate (boolean-valued function) that takes one argument of type T.
The method `test(T t)` is used to test the predicate
```java
Predicate<Integer> isEven = n -> n % 2 == 0;
boolean result = isEven.test(4); // true
```
##### Supplier<T>
Represents a supplier of results.
The method get() is used to get the result.
```java
Supplier<Double> randomNumberSupplier = () -> Math.random();
double randomValue = randomNumberSupplier.get();
```

These functional interfaces facilitate the use of lambda expressions and support the functional programming paradigm in Java. They can be used in various contexts, such as with the Stream API, to represent transformations, filters, and other operations on collections of data. The introduction of these functional interfaces in Java 8 enhances code readability and expressiveness.

### 3. Streams
Streams provide a functional approach to processing sequences of elements. They allow you to express complex data manipulations using a pipeline of operations, such as map, filter, and reduce. Streams are part of the `java.util.stream` package.

```java
List<String> strings = Arrays.asList("abc", "def", "ghi", "jkl");

// Filter strings starting with 'a' and concatenate them
String result = strings.stream()
        .filter(s -> s.startsWith("a"))
        .map(String::toUpperCase)
        .collect(Collectors.joining(", "));

System.out.println(result); // Output: ABC
```
### 4. Immutablility 
Functional programming encourages immutability, where objects once created cannot be changed. In Java, you can use the final keyword to create immutable variables.

The immutability is a big thing in a multithreaded application. It allows a thread to act on an immutable object without worrying about the other threads because it knows that no one is modifying the object. So the immutable objects are more thread safe than the mutable objects. If you are into concurrent programming, you know that the immutability makes your life simple.

### 5. Higher-Order Functions:
Functional programming supports higher-order functions, which are functions that can take other functions as parameters or return functions as results. Higher-order functions are a key concept in functional programming, enabling a more expressive and modular coding style. Java, starting from version 8, introduced support for higher-order functions with the introduction of lambda expressions and the `java.util.function` package.


```java
// Function that takes a function as a parameter
public static void processNumbers(List<Integer> numbers, Function<Integer, Integer> processor) {
    for (int i = 0; i < numbers.size(); i++) {
        numbers.set(i, processor.apply(numbers.get(i)));
    }
}

// Usage of higher-order function
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
processNumbers(numbers, x -> x * 2);
System.out.println(numbers); // Output: [2, 4, 6, 8, 10]
```

### 7. Parallelism:
Functional programming encourages writing code that can easily be parallelized. The Stream API provides methods for parallel execution of operations on streams.
```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

// Parallel stream processing
int sum = numbers.parallelStream()
                .mapToInt(Integer::intValue)
                .sum();
System.out.println(sum); // Output: 15
```
---
## Benefits of Functional Programming in Java
- **Conciseness**: Lambda expressions make code more concise and readable.
- **Parallelism**: Easier to parallelize code due to immutability and statelessness.
- **Predictability**: Immutability reduces side effects and makes code more predictable.
- **Testability**: Functions with no side effects are easier to test.
- **Modularity**: Encourages modular and reusable code.

Functional programming in Java complements the existing object-oriented programming paradigm and provides developers with powerful tools to write more expressive, modular, and maintainable code. It promotes the use of pure functions, immutability, and higher-order functions, leading to code that is often more concise and easier to reason about.
