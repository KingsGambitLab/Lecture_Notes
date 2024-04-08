![](data:image/png;base64,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)
------
# Understanding Static and Final Keyword in Java

## Static Keyword
Java uses static keyword at 4 different places. Lets learn about each of them.
- Static Instance Variables 
- Static Methods 
- Static Block
- Static Classes.

**Static Members and Methods**
There will be times when you will want to define a class member that will be used independently of any object of that class. Normally, a class member must be accessed only in conjunction with an object of its class. However, it is possible to create a member that can be used by itself, without reference to a specific instance. 

To create such a member, precede its declaration with the keyword static. When a member is declared `static`, it can be accessed before any objects of its class are created, and without reference to any object. You can declare both methods and variables to be static. 

The most common example of a static member is main( ). main( ) is declared as static because it must be called before any objects exist.

Instance variables declared as static are, essentially, global variables. When objects of its class are declared, no copy of a static variable is made. Instead, all instances of the class share the same static variable.

**Math.java**
```java
public class Math {
    static String author = "Prateek";

    static int area(int l,int b){
        return l*b;
    }
}
```
In the above example the static keywod has been used to create a static data member and a static method. We don't need create a Math Class objects to acess the methods and data members, instead we can directly refer `Math.author` and  `Math.area(v1,v2)` from main.
```java
  public static void main(String[] args) {
        //static block will execute when the class is loaded
        
        System.out.println("Area of Rectangle " + Math.area(10,20));
        System.out.println(Math.author);
    }
```

**Restrictions on Static Methods**:

•  They can only directly call other static methods of their class.

•  They can only directly access static variables of their class.

•  They cannot refer to `this` or `super` in any way. (Super keyword is used in inheritance) 


**Static Block**
If you need to do computation in order to initialize your static variables, you can declare a static block that gets executed exactly once, when the class is first loaded. 
As soon as the class is loaded, all of the static statements are run.

```java
public class StaticDemoExample {
    static int a = 3;
    static int b;

    static{
        System.out.println("Inside Static Block");
        b = a*4;
        printData();
    }

    static void printData(){
        System.out.println(a);
        System.out.println(b);
    }

    public static void main(String[] args) {
        //static block will execute when the class is loaded
        // it is used to init static variables
    }
}
```
In the above code, static block will automatically as you launch the program, the class is loaded and static block is executed. Despite the main being empty, the code will output the following as static block is still executed.

*Code Output*
```
Inside Static Block
3
12
```

## Nested Classes and 'Static' Modifier 
It is possible to define a class within another class; such classes are known as nested classes. There are two types of nested classes: static and non-static. Lets learn about them.

**Static Nested Class (Static Inner Class)**:
- A static nested class is a nested class that is declared as static.
- It does not have access to the instance-specific members of the outer class.Because it is static, it must access the non-static members of its enclosing class through an object.
- You can create an instance of a static nested class without creating an instance of the outer class.
- Static nested classes are often used for grouping related utility methods or encapsulating code within a class.
- Note: In Java, only nested classes are allowed to be static.


```java
public class OuterClass {
    // Outer class members

    static class StaticNestedClass {
        // Static nested class members
    }
}
```
**Inner Class (Non-static Nested Class)**

- An inner class is a nested class that is not declared as static.
- It can access both static and instance-specific members of the outer class.
- An instance of an inner class can only be created within an instance of the outer class.
- Inner classes are often used for implementing complex data structures or for achieving better encapsulation.

```java
public class OuterClass {
    // Outer class members

    class InnerClass {
        // Inner class members
    }
}
```
**Nested Static Classes in Builder Design Pattern**
This kind of class design is particularly useful in Builder Design Pattern which you will study later as a part of Low Level Design Course. In short, The Builder Design Pattern is a creational design pattern that allows you to create complex objects step by step. It's especially useful when you have an object with many optional parameters or configurations. Here's an example of how you can implement the Builder pattern in Java:

Suppose you want to create a Person class with optional attributes like name, age, address, and phone number using the Builder pattern:

```java
public class Person {
    private String name;
    private int age;
    private String address;
    private String phoneNumber;

    // Private constructor to prevent direct instantiation
    private Person() {
    }

    // Nested Builder class
    public static class Builder {
        private String name;
        private int age;
        private String address;
        private String phoneNumber;

        public Builder(String name) {
            this.name = name;
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Builder address(String address) {
            this.address = address;
            return this;
        }

        public Builder phoneNumber(String phoneNumber) {
            this.phoneNumber = phoneNumber;
            return this;
        }

        public Person build() {
            Person person = new Person();
            person.name = this.name;
            person.age = this.age;
            person.address = this.address;
            person.phoneNumber = this.phoneNumber;
            return person;
        }
    }

    // Getter methods for Person class
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getAddress() {
        return address;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", Age: " + age + ", Address: " + address + ", Phone: " + phoneNumber;
    }
}
```

__PersonDemo.java__
```java
public class PersonDemo {
    public static void main(String[] args) {
        Person person1 = new Person.Builder("John")
                .age(30)
                .address("123 Main St")
                .phoneNumber("555-1234")
                .build();

        Person person2 = new Person.Builder("Alice")
                .age(25)
                .phoneNumber("555-5678")
                .build();

        System.out.println(person1);
        System.out.println(person2);
    }
}
```
This allows you to create Person objects with various combinations of attributes while keeping the code clean and readable.



------------------
### Final Keyword
The keyword final has three uses. First, it can be used to create the equivalent of a named constant. The other two uses of final apply to inheritance as discussed below.

**1. Final in Variables**
A field can be declared as final. Doing so prevents its contents from being modified, making it, essentially, a constant. This means that you must initialize a final field when it is declared. You can do this in one of two ways: First, you can give it a value when it is declared. Second, you can assign it a value within a constructor. The first approach is probably the most common. Here is an example:
```
final int FILE_NEW = 1;
final int FILE_OPEN = 2;
final int FILE_SAVE = 3;
final int FILE_SAVEAS = 4;
final int FILE_QUIT = 5;
```

Subsequent parts of your program can now use FILE_OPEN, etc., as if they were constants, without fear that a value has been changed. It is a common coding convention to choose all **uppercase identifiers** for final fields, as this example shows.

In addition to fields, both method parameters and local variables can be declared final. Declaring a parameter final prevents it from being changed within the method. Declaring a local variable final prevents it from being assigned a value more than once.

The keyword final can also be applied to methods, but its meaning is substantially different than when it is applied to variables. 


**2. Using final to Prevent Method Overriding**
While method overriding is one of Java’s most powerful features, there will be times when you will want to prevent it from occurring. To disallow a method from being overridden, specify final as a modifier at the start of its declaration. Methods declared as final cannot be overridden. The following fragment illustrates final.

![](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781260463422/files/ch08-0194.jpg)
Because meth( ) is declared as final, it cannot be overridden in B. If you attempt to do so, a compile-time error will result.

Methods declared as final can sometimes provide a performance enhancement: The compiler is free to inline calls to them because it “knows” they will not be overridden by a subclass. When a small final method is called, often the Java compiler can copy the bytecode for the subroutine directly inline with the compiled code of the calling method, thus eliminating the costly overhead associated with a method call. Inlining is an option only with final methods. Normally, Java resolves calls to methods dynamically, at run time. This is called late binding. However, since final methods cannot be overridden, a call to one can be resolved at compile time. This is called early binding.

**3. Using final to Prevent Inheritance**
Sometimes you will want to prevent a class from being inherited. To do this, precede the class declaration with final. Declaring a class as final implicitly declares all of its methods as final, too. As you might expect, it is illegal to declare a class as both abstract and final since an abstract class is incomplete by itself and relies upon its subclasses to provide complete implementations.

Here is an example of a final class:
![](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781260463422/files/ch08-0195.jpg)
As the comments imply, it is illegal for B to inherit A since A is declared as final.








