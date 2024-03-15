# OOPS 1


### Programming Paradigms

Types:
* **Imperative Programming** - It tells the computer how to do the task by giving a set of instructions in a particular order i.e. line by line.
```cpp
// For eg:
int a = 10;
int b = 20;
int sum = a + b;
print(sum);
int dif = a - b;
print(dif);
```
* **Procedural Programming** - It splits the entire program into small procedures or functions (section of code that perform a specific task) which are reusable code blocks. 
```cpp
// For eg:
int a = 10;
int b = 20;
addTwoNumbers(a, b);
subtractTwoNumbers(a, b);

void addTwoNumbers(a, b) {
    int sum = a + b;
    print(sum);
}

void subtractTwoNumbers(a, b) {
    int dif = a - b;
    print(dif);
}
```

* **Object Oriented Programming** - It builds the entire program using classes and objects. [will discuss this in detail today!]

* **Declarative Programming** - In this paradigm, you specify "what" you want the program to do without specifying "how" it should be done.
```SQL
-- For eg: (SQL Queries)
select * from Customer;
```
* **Functional Programming**, **Logic Programming**, etc.

Most of the people start their coding journey with procedural programming and hence let's start with the first type of paradigm i.e. procedural programming.

---
## Procedural Programming
It splits the entire program into small procedures or functions (section of code that perform a specific task) which are reusable code blocks. Eg - C, C++, etc.

Procedure is an oldage name of function/method.

```cpp
// For eg:
void addTwoNumbers(a, b) {
    int sum = a + b;
    print(sum);
}

void addThreeNumbers(a, b, c) {
    int sum = a + b;
    addTwoNumbers(sum, c);
}

void main() {
    addThreeNumbers(10, 20, 30);
}
```
---
### Problems with Procedural Programming

**Cons of Procedural programming:**
* Difficult to make sense
* Difficult to debug and understand 
* Spaghetti code i.e. unstructured and needs to be tracked form multiple locations.

So this is all about procedural programming, now lets move to OOPs as we are preparing for the base of OOPs.

---
## Object Oriented Programming Introduction

### OOPS

OOPs came from the need of thinking of software systems in terms of how we humans think about real world.
* Entities are core in OOPs
* Every entity has some attribute and behaviour

In object oriented programming we build the entire program using classes and objects (entity).

**Class:** Blueprint of an idea.

Example - Floor plan of an apartment.
So, while designing new house, we make something called blue print.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/687/original/upload_fd21eec1163e374c6941c99414aa7abf.png?1692719460" width="500"/>

Now this will have exact dimensions as per need. Is the house built? No not yet, but whenever it will get built, the design will be look like this.

**Class represent the strucutre of the idea.**
Class has attributes to define data and methods to define functionalities/behaviour.

Lets build a `Student` class with some attributes and methods.

Its the basic structure, its not a real thing, it just show what data every student holds upto. Also, You can create multiple instances of this class.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/688/original/upload_6d32af9ec0c67eb9779264de5f92beba_%281%29.png?1692719509" width="500"/>

**Object:** They are real instances of the class.

### Question

Will the object of a class occupy memory?

**Choices**

- [ ] No
- [ ] In some cases only
- [x] Yes


Yes they will occupy memory because they are real instance of the class / blueprint.

---
### Classes & Objects Example

Now lets create a class and object and see how this thing works on machine.

1. We will create a class named Student

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/689/original/Screenshot_2023-08-07_145127.png?1692719555" width="500"/>
```java
}
```

2. Then, we will create the main class

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/690/original/Screenshot_2023-08-07_145303.png?1692719596" width="500"/>

3. And we can see that both naman and dinesh have their own identity
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/692/original/Screenshot_2023-08-07_145356.png?1692719666" width="500"/>

---
### Pillars of Object Oriented Programming

Now what is principle and pillar?
* **Principle** - Fundamental foundation / concept.
* **Pillar** - Support to hold things together


**So what does the principle of OOP says?**

Idea of OOP is based on **abstraction** and the whole software system is build around abstraction.

But how would we implement the abstraction? ---> Using the 3 pillars of OOPs i.e.
* **Inheritance**
* **Polymorphism**
* **Encapsulation**


**For example:** 

Your **principal** can be:
- I will be a good person.

But how you would be a good person? Here comes your **pillars**:
- I will be truthfull,
- I will do hardwork,
- I respect everyone, etc.

So we got to know that abstraction is not the pillar of OOPs, it is the main principle on which whole concept of OOP is based.


---
### OOPs Abstraction

Abstraction means ---> **Representing in terms of ideas**.

Now what does ideas mean? ---> Anything in software system that has attrubute and associated behaviour.

So if you are building scaler, you don't have to think about storing individuals like, Naman, Anshuman, Indarjeet. You can use Students, Mentors, TAs, Classes, etc. with their attributes.

**Do they have a behaviour?**

Yes they all have some behaviour. Student can send messages, pause courses these are all behaviours.
So abstraction is an idea of representing complex software system interms of ideas, because ideas are easy to understand.
So, its  an concept of making something abstract.

### What is the purpose of abstraction?

The main purpose is that others dont need to know the details of the idea.

Suppose you are driving a car, and you want it to turn left and speed up, and you steer the steering to left and press the acceleration pedal. It works right? Do you need to know how does this happen? What combustion is happening, how much fuel is used, How steering wheel turned the car? 
No right? This is what we call as abstraction.

Abstraction is way to represent complex software system, in terms of ideas. 

What needed to be represented in terms of ideas?
* Data
* Anything that has behaviours

No one else need to know the details about the ideas.

Now let's move to encapsulation.

---
## OOPs Encapsulation


So what are the purpose for making capsules, and not normal medicine?

If the capsule breaks away, what will happen? 
- It will flow away. So first purpose is to hold the medicine powder together.
- Then there are multiple powders are present in the capsule, it helps them to avoid mixing with each other.
- Third purpose is it protects the medicine from the outside environment.

This is exactly the purpose of Encapsulation in OOP.

Encapsulation allows us to store attribute and Behaviours together. 

### Question

Where do we store attribute and behavious together? What is the technical term for that?

**Choices**

- [x] Class
- [ ] Object
- [ ] Project



Yes, a **class**, and it protects attributes & methods from outer environment i.e. other classes can't have access to it if we restrict.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/686/original/upload_ec5c0fae6db181970a0f3f3e96074b60.png?1692719428" width="500"/>

Here no one can access the age of student other than the class student.

---
## Access Modifiers

We got to know that Encapsulation has two advantages, 
* ONE is it holds data and attributes together and 
* SECOND is it protect members from illegitimate access. You can't access the data from class unless the class allows you to.

Now, The first thing gets sorted by class, i.e. we create a class, and it holds the behaviors and attributes together.

But, **How the SECOND one is implemented?** 
i.e., How in code illegitimate access is prevented? 
How the encapsulation prevents access to class data?

That is something called **access modifiers**.

---
### Question

Which one of these is **not** an access modifier?

**Choices**

- [ ] Public
- [x] Open
- [ ] Private
- [ ] Protected

---
### Types of Access Modifiers

There are four access modifiers in most of the programming languages, they are:
* **Public**
* **Private**
* **Protected**
* **Default** (if we don't use any of the above three, then its the default one)

So what are these access modifiers? Let's quickly look at them.

**Public access modifier** - A public attribute or method can be accessed by everyone.

**Private access modifiers** - A private attribute or method can be accessed by no one, not even the child class.
**Explanation** - It can be accessed by the **same** class. No one outside the class has access to private methods.

**Protected access modifier** - A protected attribute or method can be accessed only from the classes of the same package.

Let me show you a diagram that will be helpful in understanding and will clear most of your doubts.

where:<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/697/original/Screenshot_2023-08-06_161609.png?1692721785" width="500"/>

---
### Question

Which is the **most restricted** access modifier?

**Choices**

- [ ] Public
- [ ] Default
- [x] Private
- [ ] Protected

---
### Question

Which is the **most open** access modifier?

**Choices**

- [x] Public
- [ ] Default
- [ ] Private
- [ ] Protected

---
### `this` Keyword

Before we see the example of access modifier, let's understand **"this" keyword**:
* In programming, "this" is a keyword used to refer to the **current instance of a class or object**. 
* It's typically used to distinguish between instance variables and local variables or method parameters with the same names, and to access or modify instance members within methods.
* This enhances code clarity and prevents naming conflicts in object-oriented languages like Java and C++.

Here is an example:
```Java
public class Person {
    private String name;

    public Person(String name) {
        this.name = name; // "this" refers to the current instance of the class
    }

    public void introduceYourself() {
        System.out.println("Hello, I am " + this.name); // Using "this" to access the instance variable
    }

    public static void main(String[] args) {
        Person person1 = new Person("Alice");
        Person person2 = new Person("Bob");

        person1.introduceYourself(); // Output: Hello, I am Alice
        person2.introduceYourself(); // Output: Hello, I am Bob
    }
}
```
In this example, the "this" keyword is used to differentiate between the instance variable name and the constructor parameter name, ensuring that the correct value is assigned and accessed within the class methods.

---
### Example of Access Modifiers

```Java
package mypackage;

public class AccessModifierExample {
    public int publicVariable = 10; // Public access

    private int privateVariable = 20; // Private access

    protected int protectedVariable = 30; // Protected access

    int defaultVariable = 40; // Default (package-private) access

    public void publicMethod() {
        System.out.println("This is a public method.");
    }

    private void privateMethod() {
        System.out.println("This is a private method.");
    }

    public static void main(String[] args) {
        AccessModifierExample example = new AccessModifierExample();

        System.out.println("Public variable: " + example.publicVariable);
        System.out.println("Private variable: " + example.privateVariable);
        System.out.println("Protected variable: " + example.protectedVariable);
        System.out.println("Default variable: " + example.defaultVariable);
    }
}
```
```Java
package otherpackage;

import mypackage.AccessModifierExample; // Import the class from a different package

public class AnotherClass {
    public static void main(String[] args) {
        AccessModifierExample example = new AccessModifierExample();
        
        System.out.println(example.publicVariable); // Accessing publicVariable is valid
        System.out.println(example.defaultVariable); // Error: Cannot access defaultVariable from a different package
        
        example.publicMethod();
        example.privateMethod(); // Error: Private method is not accessible outside the class
    }
}
```
In this example:

The class **AccessModifierExample** has variables and methods with different access modifiers: public, private, protected, and default.
Access modifiers control the visibility and accessibility of members (variables and methods) outside the class.
Public members are accessible from anywhere, private members are only accessible within the class, protected members are accessible within the class and its subclasses, and default members are accessible within the same package.

Now, you can try all these on your machine just by creating classes and accessing them.

---

### `static` Keyword

The **static** keyword in programming languages like Java and C++ is used to declare **class-level members or methods**, which are associated with the class itself rather than with instances (objects) of the class.

1. **Static Variables (Class Variables):** When you declare a variable as "static" within a class, it becomes a class variable. These variables are shared among all instances of the class. They are initialized only once when the class is loaded, and their values are common to all objects of the class.

2. **Static Methods (Class Methods):** When you declare a method as "static," it becomes a class method. These methods are invoked on the class itself, not on instances of the class. They can access static variables and perform operations that don't require access to instance-specific data.

The **static** keyword is often used for utility methods and constants that are relevant at the class level rather than the instance level. It allows you to access these members without creating an object of the class.

Static variable is created when we load a class.

Here is an example:
```Java
public class MyClass {
    // Static variable
    static int staticVar = 0;

    // Instance variable
    int instanceVar;

    public MyClass(int value) {
        this.instanceVar = value;
        staticVar++;
    }

    public static void main(String[] args) {
        MyClass obj1 = new MyClass(10);
        MyClass obj2 = new MyClass(20);

        System.out.println("Static Variable: " + staticVar); // Output: Static Variable: 2
        System.out.println("Instance Variable (obj1): " + obj1.instanceVar); // Output: Instance Variable (obj1): 10
        System.out.println("Instance Variable (obj2): " + obj2.instanceVar); // Output: Instance Variable (obj2): 20
    }
}
```
In this example, we have a static variable **staticVar** and an instance variable **instanceVar**. The staticVar is incremented every time an object is created, and we access both static and instance variables directly within the main method.

---

### Scope of a variable

Now let's talk about scope of a variable within a program!

In Java, scope refers to the region or context within your code where a specific variable or identifier is accessible and can be used. The scope of a variable is determined by where it is declared, and it influences its visibility and lifetime within the program. 
**There are primarily four types of variable scope in Java:**

1. **Class/Static Scope:** Variables declared as `static` within a class have class-level scope. These variables are associated with the class itself rather than with instances (objects) of the class. They can be accessed using the class name and are shared among all instances of the class.

2. **Instance Scope:** Variables declared within a class but outside any method or constructor have instance scope. These are often referred to as instance variables, and they are associated with specific instances (objects) of the class. Each object has its own copy of these variables.

3. **Method/Local Scope:** Variables declared within a method or a block of code have method or local scope. These variables are only accessible within the specific method or block where they are defined. They go out of scope when the method or block's execution is complete.

4. **Block Scope:** Variables declared within a pair of curly braces `{}` have scope limited to that block. These variables are only accessible within the block in which they are defined.

The scope of a variable is essential for ensuring that the right variables are accessed at the right time and for avoiding naming conflicts. Properly managing variable scope contributes to the clarity and reliability of your code.

Here's a brief example to illustrate variable scope in Java:

```java
public class ScopeExample {
    // Class-level variable (static scope)
    static int classVar = 10;
    
    // Instance variable (instance scope)
    int instanceVar = 20;

    public void exampleMethod() {
        // Method-level variable (method scope)
        int methodVar = 30;
        
        if (true) {
            // Block-level variable (block scope)
            int blockVar = 40;
            System.out.println(classVar + instanceVar + methodVar + blockVar);
        }
        // The 'blockVar' is out of scope here.
    }

    public static void main(String[] args) {
        ScopeExample obj = new ScopeExample();
        obj.exampleMethod();
        // The 'methodVar' and 'blockVar' are out of scope here.
    }
}
```

In this example, you can see how variables with different scopes are defined and accessed within a Java class.
