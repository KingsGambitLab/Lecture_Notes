# OOPs 2
### Constructors

If you remember, we have studied **classes and objects** in the previous lecture, so what is a class and object? Let's have a quick recap of it.


**Class:** Blueprint of an entity.
**Object:** Instance of class

Now let's look at how a class comes into reality.

Let's define a class named Student.
```java
Student {
    String name;
    int age;
    doubly psp;
}
```
Now, let's make an object of the Student class.
```java
Student st = new Student();
```
Now, from the basics of programming, we all know that to declare a variable, we write:
```java
int a = 12;
```
Let's compare this with object creation:
```java
int a = 12;
Student st = new Student();
```
We can see that **Student** is the Data type here and **st** is a variable name, but


This thing => **Student();** is called a **constructor**, which creates the object of the class.

This thing, when you don't create a constructor, is called a **default constructor**. Let's discuss it in detail.

---

### Default Constructor
If we don't create our own constructor in a class, a **default constructor** is created.

**Default constructor** creates a new object of the class and sets the value of each attribute as the default value of that type. 

Examples of default values of datatype:
* **0** for integer,
* **null** for String,
* **0.0** for float, etc.

> **Note:** A default constructor will assign default values only if we haven't assigned values to class attributes while declaring the variable.

So if we are not creating any constructor, then our class is going to make its own constructor.

A default constructor can be assumed to be present like this:
```java
class Student {
    String name;
    int age;
    double psp;
    String univName;
    
    Student() {
        name = null;
        age = 0;
        psp = 0.0;
        univName = null;
    }
}
```

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/713/original/Screenshot_2023-08-07_091328.png?1692723204" width="400"/>

But,
* By the definition of the default constructor, we know that, **if we create our own constructor** then a default constructor is not created.

So, by looking at Student(), we can say that no parameters are passed here, right?
So, **the default constructors take no parameters**.

**Summarising** the default constructor:
1. Takes no parameter.
2. Sets every attribute of class to it's default value (unless defined).
3. Created only if we don't write our own constructor.
4. It's public i.e. can be access from anywhere.

---

### Manual Constructor
Now, let's create our own constructor using the same `Student` class

```java
public class Student {
    String name;
    private int age = 21;
    String univName;
    double psp;

    public Student (String studentName, String universityName) {
        name = studentName;
        univName = universityName;
    }
}
```
Let's create a client class.
```java
public class Client {
    public static void main(String[] args) {
        Student st = new Student(); //ERROR
}
```
But here, why its throwing error?
* Because now there is no default constructor, since we have our own constructor, and it has parameters. So we have to pass the parameters here.

So, let's do like this,
```java
public class Client {
public static void main(String[] args) {
    Student st = new Student("Utkarsh", "JIIT");
}
```
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/715/original/Screenshot_2023-08-07_103207.png?1692723759" width="500"/>

Now, let's move to the copy constructor and learn more about it.

---
### Copy Constructor

Now, **What is a copy constructor?**
Let's say we already have an object of student class, and then we want to create a new object of student that has the exact same values of attributes as older objects.

**For example:**
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/718/original/Screenshot_2023-08-07_113204.png?1692723906" width="500"/>

If `st1` as an object and we need to create one more object `st2`, with the same attribute values, we can do it with the copy constructor.

```java
class Student {
    String name;
    int age;
    
    Student() {
        name = null;
        age = 0;
    }
    Student(Student st) {
        name = st.name;
        age = st.age;
    }
}
```

So basically, to make a copy, we need to pass it as a parameter to the copy constructor, as the data type is Student.
```java
Student st1 = new Student();
st1.name = "Utkarsh";
st1.age = 27;

Student st2 = new Student(st1); // Copy Constructor
```

So now we understand how to write a copy constructor, but what is the use case of the copy constructor?

* The copy constructor comes in use when we have an object, and a newly created object needs the same values, so we don't assign it ourselves. We use the copy constructor the get the work done.
* Some of the attributes may be private and cannot be accessed by the user, but a copy constructor can access it and make the copy itself.

### Question

Is copy constructor same as doing `Student st2 = st1;`?

**Choices**

- [ ] Yes
- [ ] In some cases only
- [x] No


Let's see how do things work internally?
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/728/original/Screenshot_2023-08-07_115214.png?1692725483" width="500"/>

* So we have a memory, and st1 is present in the memory with all the data, as shown in the above diagram. 
* When we write student `st2 = st1`, we just make st2 to point as s1, i.e., **a new object is not created**.
* Now the problem here is if we do changes in st2, i.e. `st2.name = 'xyz'`, it will change the value of st1.


Now if we create the object using copy constructor then it has a different address. So it's not pointing in the memory, as we have seen in the example above.

---
### Deep and Shallow copy

### Shallow copy

* When we have created a new object, but behind the scenes, the new object still refer to attributes of the old object. i.e., the new object still refers to the same data as the old copy.

```python
original_books = ["Book A", "Book B"]
shallow_copy_books = original_books

shallow_copy_books.append("Book C")

print(original_books)  # Output: ["Book A", "Book B", "Book C"]
```

### Deep copy

* When we have created a new object behind the scenes, the new object do not refer to attributes of the old object. i.e., the new object has no shared data.

```python
import copy

original_books = ["Book A", "Book B"]
deep_copy_books = copy.deepcopy(original_books)

deep_copy_books.append("Book C")

print(original_books)  # Output: ["Book A", "Book B"]
```

---
### Inheritance



**How is inheritance represented?**
**Ans** - Inheritance is represented as parent-child relations between different classes.

Now, let's talk about the scaler's hierarchy of representation.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/747/original/Screenshot_2023-08-08_112052.png?1692729330" width="500"/>

Now, Let's say User has the following attributes:
* Username
* Login


So, We can say that:
* Instructor
* Mentor
* TA
* Student

They all are **specific types** of users i.e. they will share all the members / attributes / methods of **User** and may have some more of their own.

A **child class / subclass** can have specific attributes / behaviors which may not be present in the **parent class / superclass**.

>Consider the below diagram for explaining child / subclass & parent / superclass terms more clearly.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/748/original/Screenshot_2023-08-08_113025.png?1692729357" width="500"/>

So we can **conclude**: A child class inherits all the members of the parent class and may or may not add their own members.

---

### Parent-Child Relationship in Code

How can we represent a parent-child relationship in code? Let's say we need to make a relationship between the User and the Instructor.


To build this, Let's say we have a **Parent class called User**, as shown below: 
```java
class User {
    String userName;
    
    void login() {
        ...
    }
}
```
**Instructor** is a child/subclass of User, so how can we do that?
```java
Class Instructor extends User.
```
So here `extends` is the **keyword in Java** that is used to create a child class.

The `extend` keyword is specific to Java and is used to create a subclass that inherits properties and behaviors from a superclass.

While the keyword itself may vary in other programming languages, the concept is similar. Here are a few examples from different languages:

- **In Python:** The inheritance is indicated using **parentheses**. 
For example: `class Subclass(SuperClass):`

- **In C++:** The inheritance is specified using a **colon**. 
For example: `class Subclass : public SuperClass { };`

- **In C#:** The inheritance is specified using a **colon**.
For example: `class Subclass : BaseClass { }`

So, while the specific syntax and keywords may differ, the concept of class extension or inheritance is present in various object-oriented programming languages.

The instructor class has the following methods:
```java
class Instructor extends User {
    String batchName;
    double avgRating;
    
    void scheduleClass() {
        ...
    }
}
```

* Does the Instructor class needs a username property? 
    * Yes
* Do we need to code it?
    * No
* So, how can we use it?
    * We are extending it from the User class.

Extends means, **keeping the original things and adding more things to it**.

---
### Constructor Chaining


How do we create an object of any class?
```java
Instructor i = new Instructor();
```
* Did we ever created `Instructor()` constructor?
    * No, Right?

* So, how it came into the picture?
    * Yes, It is a Default Constructor.
This constructor initializes to default values of all the attributes, so can we do like:
```java
i.username = "Utkarsh";
i.login();
```
Yes, because it's coming from the `User` class.

Can we also do:
```java
i.avgRating = 4
```
Yes, because it's part of the Instructor's class.

**Note:** In Inheritance, a parent class is nothing but generalization, and every child is a specification.

Now, assume we are given this relation:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/752/original/Screenshot_2023-08-08_124458.png?1692729547" width="300"/>

---
### Question

Which of these classes has the highest level of abstraction?

**Choices**

- [x] A
- [ ] B
- [ ] C
- [ ] D


First of all, what is abstraction?
- It's an idea.

So, what does the highest level of abstraction mean?
- A bigger idea that means a more general idea.

So out of them, **A** is the most generic class, right? 
That's why **A has the highest level of abstraction.**

---
### Question

Do the child class contains all the attributes of parent class?

**Choices**

- [x] Yes
- [ ] No
- [ ] Can't say


Definitely, **Yes**.
Example is Animal :arrow_right: Dog

So now the question is, how are they initialized? Who initializes them?

Let's see what happens behind the scenes:

* Let's say we have a User class as shown below:
    <img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/753/original/Screenshot_2023-08-08_130539.png?1692729576" width="150"/>
And we create a `User` object:
 **`User user = new User();`**

So,
How will the attributes get initialized?
**Ans** - Since we haven't created our constructor, our attributes get assigned to null values by default constructor, as shown below.
    * <img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/754/original/Screenshot_2023-08-08_130908.png?1692729607" width="200"/>

* Or we may create our own constructor:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/755/original/Screenshot_2023-08-08_131123.png?1692729739" width="200"/>


Now, If we create a child class / sub-class named instructor:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/756/original/Screenshot_2023-08-08_131915.png?1692729766" width=250/>

**Now the question is:** When we create an instructor, someone has to initialize the attribute that came from the parent.

There are scenarios now:
1. We know how to initialize, and we understand how to change, so **we will initialize** the values to those attributes, like this:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/757/original/Screenshot_2023-08-08_132224.png?1692729800" width="300"/>

But DO YOU THINK we will always Know how to initialize the attributes?
Ans - **No!** But there is someone who'll always know how and what to initialize. 

2. A **constructor of the parent** definitely knows how and what to initialize the attributes. Let's understand How it's done!

---
### Steps to Create an Object of Child

**(Assuiming no constructor is created, its only default constructors are present)**

Suppose we have a class named **A**.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/758/original/Screenshot_2023-08-08_172426.png?1692729822" width="100"/>

Now `B` is a child of `A`,
`C` is a child of `B`, and 
`D` is a child of `C.`

Suppose we create an object of **D**:
```java
D d = new D();
```

So, **What really happens when we call `D()`?**
1. Constructor of D will be called.
2. Since D is also a child of someone, so before its execution, it will call the constructor of C.
3. Similarly, C will call the constructor of B first.
4. And B will call the constructor of A before it's execution.

So, **Who's constructor will be finished first?**
- **A**'s constructor will be finished first, then  **B** will be finished, then **C** will be finished, then **D** will be finished.

Because, 
* **Can a child be born before its parents are born?** 
**No**, right?
    * That's why the parent class constructor will be called first. We haven't specifically called the parents constructor but by default, the parent constructor is called.

**Note:**
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/759/original/Screenshot_2023-08-08_180123.png?1692729914" width="500"/>

What will happen if we add a parameterized constructor in class **C** as shown below:
```java
public class C extends B {
    C() {
        System.out.println("Constructor of C");
    }
    C(String a) {
        System.out.println("Constructor of C with params");
    }
}
```
What will be the output if we run the code now?
The output will still be the same right, i.e., `Default Constructor of C` will be printed with all other constructors from A, B & D.

But, What if we want to **print the manual constructor** of class C?

To make this happen, we need to make changes in our **D** class.
We have to add the **super** function in the first line of our constructor.

```java
public class D extends C {
    D() {
        super ("Hello"); // This must be the first line
        System.out.println("Constructor of D");
    }
}
```
The **super("Hello");** will make the parametrized constructor from Class C become active.

**Note:** This super() line in the code must be written in the **first line inside a constructor**. Otherwise, it throws an error. 

---
## Polymorphism

What really is polymorphism?

There's a very famous explanation of Polymorphism i.e. **Poly means Many** and **Morphism means Form**.

Which means, someone who has multiple forms.

So, till now, in today's class, have you learned about something which had multiple forms?
**Ans** - Yes, a user could have multiple forms. Because a user can be a student, instructor, TA, etc.

So this can be an example of multiple forms.

**Another example** - Suppose we have a list of Animals. Animals have Mammals, Reptiles, Aquatic, etc. classifications.

**Can we write:**
`Animal a = new Dog();`
Yes, because this is an **object of type Dog**, which is a Mammal and which is an Animal. So we can write it!

**But, Can we write:**
`Dog d = new Animal();`
No, this is **not allowed** since every Dog is an Animal, but every Animal must not be a Dog.

**That means: We can put an object of the child class in a variable that takes parent data type.**

**Suppose we have three classes, A, B, and C.** as shown below:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/761/original/Screenshot_2023-08-08_200212.png?1692730048" width="500"/>

Now if we write:
```java
A a = new C();
a.company = "ABC";
```
This will **throw an error** because **a** has a datatype of **A**, but A doesn't have any variable named company.

* Compiler only allows you access to members of the data type of the variable.

Now, suppose you have a method called:
**changePassword()**

* Is this change password method need a Student / TA / Instructor, OR just a user?
    * Just a User, right?
Because it doesn't matter which type of user is asking for a changepassword.

=> **The more generic your code is, the better the reusability will be.**
This is one of the use cases of Polymorphism.

There are **two types of polymorphism**:
1. Compile Time Polyphormism
2. RunTime Polymorphism

Now we have seen that one way of having many forms is **Inheritance**. The other is called **Method overloading**.

---

### Method Overloading
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/762/original/Screenshot_2023-08-09_094412.png?1692730077" width="500"/>

Suppose we have a class **A**, and it has a method named `hello()`.

* Can a class have another method with the same name but having different parameters?
    * Yes, this second method `hello(String Name)` is having same name.

Now, this is called **Method overloading**.

Here also, can you identify **Polymorphism**?
**Ans** - The same method name has many forms.

So, If we write:
```java
hello();
hello(name);
```
Does the compiler knows which method to call? In each of the statements?
* Yes, It knows. So it will be the respective parameters which matches the method definition.

:arrow_right: As here, the final form that will execute is known to the *Compiler*. That's why it is known as **Compile time Polymorphism**.

Which of the following is a method overloading, and which of them is not?
* <img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/763/original/Screenshot_2023-08-09_100541.png?1692730381" width="500"/>
Yes, the first 2 are method overloading, but the last one is not method overloading. 


:arrow_right: So there is something called a **Method Signature**. 
A method signature is: **`Name of method (Data type of Params)`**

Example: If we have a method:
`void printHello(String Name, int age)`

* Method signature for this method will be:
 `printHello(String, int)`
 
**Methods are known to be overloaded when they have the same name but different signatures.**

---
### Question

Is this allowed in the same class?
```
void printHello(String s) {...}

String printHello(String s) {...}
```

**Choices**

- [ ] Yes
- [x] No
- [ ] Can't say


Since the method signature of both the functions is same, the compiler will not be able to distinguish between the functions and hence will give **compile time error**.

---
### Method overriding

Suppose we have a class **A**,
```java
Class A {
    void doSomething(String a) {
        ...
    }
}
```
And we  have another class **B** which inherits from **A**, and this class also had a method named `doSometihng`,
```java
Class B extends A {
    String doSomething(String c) {
        ...
    }
}
```
So, Is this allowed?
**Ans** - No, 
Since all the methods of the parent class are present in the child class, like:
```java
Class B extends A {
    String doSomething(String c) {
        ...
    }
    // Parent method inherited
    void doSomething(String a) {
        ...
    }
}
```
And, in the child class, we are having 2 methods with the same signature which it's not allowed. It's going to give us a **Compile time error**.


Now let's see another scenario of the same classes. But here, the **return type of both methods is going to be the same**.

Suppose we have a class **A**,
```java
Class A {
    void doSomething(String a) {
        ...
    }
}
```
And we  have another class **B** which inherits from **A**, and this class also had a method named `doSometihng`, like:
```java
Class B extends A {
    void doSomething(String c) {
        ...
    }
}
```

If parent and child classes have the same method with the same name and same return type, and the same signature, this is called **Method overriding.**
In Method overriding, the Parent class methods get hidden.

Let's say we have two classes, as shown below:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/767/original/Screenshot_2023-08-09_112752.png?1692731362" width="500"/>

And in the **Main()** method we run the following:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/043/768/original/Screenshot_2023-08-09_113052.png?1692731390" width="500"/>
So we can see that at first, we have `Hello` as output, and in the last statement, we get  `Bye` as output.

Now there are some points that you have to understand:

* The method that is executed is of the data type that is **actually** present at the time of code and **not the type of variable**.
* Do we know the exact code that is about to run in compile time?
    * No, and that's why it's called **RunTime polymorphism**

=> ***Compiler relies on the data type of variable, whereas runtime relies on the actual object.***
