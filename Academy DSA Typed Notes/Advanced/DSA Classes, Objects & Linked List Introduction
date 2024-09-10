# DSA: Classes, Objects & Linked List Introduction


## Expectation setting for basic OOPS

In this session we shall be covering basic oops as much as we need for learning further DSA.

OOPS will be covered in much more depth and with hands on exercises in **LLD module**.

---
## Programming Paradigms


### Programming Paradigms
What is a programming paradigm?
* **Answer** - Style or standard way of writing a program.

**Eg:** Everyone must had a burger at Mc Donald ? Yes!
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/085/093/original/download.png?1722934192" width=50 />

No matter at which Mc D we go, we know the burger will be same, why is it so ? Because they follow a standard recepie. 

Because of which customers are usually satisfied as there is predictibility.

While coding as well, it is extremely important to follow a programming paradigm, i.e everyone should follow a standard way of writing a code.


### Without programming paradigm the code will be:
* Less structured 
* Hard to read and understand 
* Hard to test
* Difficult to maintain, etc.

Different programming languages support different type of programming paradigms and some languages also support multiple types of programming paradigms.

OOPS is one such programming paradigm followed by languages like JAVA, PYTHON, C++, C#, JS, RUBY, etc...


---
## Why OOP is required ?


To introduce OOP concepts using a practical example, consider a scenario where you want to store and manage the marks and names of students.

What data structure can be used ? ARRAYS!

Imagine you have two arrays:

**Names Array**: **`["Alice", "Bob", "Charlie"]`**
**Marks Array**: **`[85, 92, 78]`**
Each index in these arrays corresponds to a specific student. For example, index 0 holds "Alice" in the Names Array and 85 in the Marks Array, indicating that Alice scored 85.

## Limitations of Using Arrays
While this approach might seem straightforward, it has significant drawbacks as data complexity increases:

### Scalability Issues:

As you add more students, you need to ensure that every new entry in the names array has a corresponding entry in the marks array at the same index. This gets harder to manage as the array grows, increasing the risk of errors.
Suppose you have hundreds or thousands of students; managing such large arrays can become very cumbersome and increases the likelihood of making mistakes during data entry or updates.

### Maintainability:

If you decide to add more details about each student, such as their address, phone number, or email, you would need to create and manage additional arrays for each attribute.
For every attribute you add, you have to ensure all these arrays are updated consistently whenever changes occur (e.g., adding or removing a student). This not only increases the amount of code but also the potential for bugs where data might not line up correctly across arrays.

### Data Association:

If you sort the Names Array alphabetically, you must also reorder every other array (like Marks, Addresses, etc.) to ensure that each student's information still lines up correctly.
This synchronization issue can lead to significant problems when filtering or searching through data. You might end up displaying or processing incorrect information if arrays are not perfectly aligned after modifications.

### Real-World Implications
The use of arrays in this way is akin to trying to manage a spreadsheet where each column is independent of the others. Any changes in one column require careful updates in the others, which is both time-consuming and prone to error, especially without the safeguards that more sophisticated data structures or systems provide.


---
## OOPs Introduction


OOPs is extemely important concept since most of the languages follows this and this is one of the hot topic of interviews. 

It is not that diffcult as much as it sounds. The concept is a mapping to real world, hence this is something which we already experience in our day-to-day life.

It is a philosophy and from that philosophy, it is just a way of writing code.

The most fundamental things in oops is classes and objects.

---
## Class & Object Definition

**`CLASS`**
Think of a class as a blueprint for creating things. Imagine you’re a toy manufacturer and you want to produce a bunch of toy cars. Before you start, you need a design or a plan that tells you what the toy car will look like, what parts it will have, and how it will function. This design or plan is like a class.

In programming, a class is a blueprint for creating objects. It defines what attributes (properties) and methods (behaviors) the objects created from it will have. But, by itself, the class doesn’t create any actual toy cars—it just provides the instructions.

**`OBJECT`**
An object is like one of the toy cars created from the blueprint. It’s a real, tangible instance of the design. Using the blueprint (class), you can create many toy cars (objects), each with the same properties and abilities defined by the blueprint.

When you create an object, you’re bringing the blueprint to life and giving it specific values for its properties.


**`EXAMPLE`**
*Class (Cookie Cutter):*
*Imagine you have a cookie cutter in the shape of a star. The cookie cutter is the blueprint (class) for making star-shaped cookies.*

*Objects (Cookies):*
*When you use the cookie cutter to cut dough, you create star-shaped cookies (objects). Each cookie is an instance of the star-shaped blueprint provided by the cookie cutter.*


---
## Create a class and an object in Java


```javascript
// creating a class
class Book {
  String title;
  String author;

  void read() {
    System.out.print("Reading a book");
  }
    
  void cover() {
      System.out.print("Covering a book");
  }
}

public class Main {
  public static void main(String[] args) {
    
    // creating an object
    Book java_b1 = new Book();
  }
}
```

### Note: Class comes into existence only when objects are created, otherwise it doesn't have any memory of its own.

Now above we have created "java_b1" object which will have all the attributes - title, author and can execute functions - read(), cover()

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/085/257/original/Screenshot_2024-08-07_at_12.55.21_PM.png?1723015531" width=500/>

### Set the values of attributes
```javascript
java_b1.title = "Almanack";
java_b1.aurthor = "Naval";

System.out.print(java_b1.title); //Almanack
System.out.print(java_b1.aurthor); //Naval
```

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/085/258/original/Screenshot_2024-08-07_at_12.56.26_PM.png?1723015596" width=500/>

---
## Create a class and an object in Python


(Copy on IPAD)

```javascript
// creating a class
class Book:
    title = ""
    aurthor = ""
    
    def read(self):
        return "Reading a book"

    def cover(self):
        return "Covering a book"

// creating an object
python_b1 = Book()
```

### Set the values of attributes
```javascript
python_b1.title = "Almanack"
python_b1.aurthor = "Naval"

print(python_b1.title) //Almanack
print(python_b1.aurthor) //Naval
```

---
## Constructors


### Constructors

Let's define a class named Student.
```java
class Student {
    String name;
    int age;
    double psp;
    String univName;
}
```
Now, let's make an object of the Student class.
```java
Student st = new Student();
```

We can see that **Student** is the Data type here and **st** is a variable name, but

What does the `new Student()` part of the statement do here?

This thing => **Student();** is called a **constructor**, which creates the object of the class.

But can you see any method named Student() in the Student class?
* *No!* Right?

This thing, when you don't create a constructor, is called a **default constructor**. Let's discuss it in detail.

---
## Default constructor


### Default Constructor
If we don't create our own constructor in a class, a **default constructor** is created.

**Default constructor** creates a new object of the class and sets the value of each attribute as the default value of that type. 

Examples of default values of datatype:
* **0** for integer,
* **null** for String,
* **0.0** for float, etc.

> **Note:** A default constructor will assign default values only if we haven't assigned values to class attributes while declaring the variable.

So if we are not creating any constructor, then our class is going to make its own constructor.

### A default constructor can be assumed to be present like this:
```java
class Student {
    String name;
    int age;
    double psp;
    String univName;
    
    //This is how default constructor can be assumed to look like internally.
    Student() {
        name = null;
        age = 0;
        psp = 0.0;
        univName = null;
    }
}
```

As soon as we write below statement, default values to all variables gets assigned.
```
Student st = new Student();
```

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/085/259/original/Screenshot_2024-08-07_at_12.59.24_PM.png?1723015780" width=500 />


### Few Question:
#### 1. In what condition a **default constructor is not created**?
* By the definition of the default constructor, we know that, **if we create our own constructor** then a default constructor is not created.

#### 2. Do we pass any parameter to default constructor ?
* NO! **the default constructors take no parameters**.

#### 3. Do you notice something special about the **name of the constructor**?
* *Yes*, the name of the constructor is same as the class name.

#### 4. What really is the **data type** of the constructor i.e. what data type does the constructor return?
* The data type is assumed to be the class name itself.

### **Summarising** the default constructor:
1. Takes no parameter.
2. Sets every attribute of class to it's default value (unless defined).
3. Created only if we don't write our own constructor.
4. It's public i.e. can be access from anywhere.


## Non-parameterised Constructor
Say, we want to assign some other values by default to variables, for this we can create our own constructor
```java
class Student {
    String name;
    int age;
    double psp;
    String univName;
    
    //This is how default constructor can be assumed to look like internally.
    Student() {
        name = "Bikram";
        age = 40;
        psp = 29.4;
        univName = "ABC";
    }
}
```

As soon as we write below statement, default values to all variables gets assigned.
```
Student st = new Student();
```

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/085/261/original/Screenshot_2024-08-07_at_1.00.32_PM.png?1723015881" width=500 />

#### If we write any constructor inside class, default will not be called.

## Parameterised Constructor
### Now what if we want to initialise with different values everytime an object is created?

For this, we can create parameterised constructor and pass the values while creating an object itself.

```java
public class Student {
    String name;
    int age;
    String univName;
    double psp;

    public Student (String studentName, int studentAge, String universityName, double problemSP) {
        name = studentName;
     	age = studentAge;
     	univName = universityName;
     	psp = problemSP;
    }
}
```

### Create Object

```java
Student st = new Student("Salmaan Bhai", 20, "Holy", 55.6);
```
Now, we don't have to separately assign value to each attribute, but we can easily do so while creating an object.

## Can we also write constructor like -
```java
public class Student {
    String name;
    int age;
    String univName;
    double psp;

    public Student (String name, int age, String univName, double psp) {
        name = name;
     	age = age;
     	univName = univName;
     	psp = psp;
    }
}
```

### What is different? The names of attributes and parameters are same! Isn't it confusing ?
Yes! There is a way to distinguish the class attributes.
We can simply put keyword -"this" in front of them.

```java
public class Student {
    String name;
    int age;
    String univName;
    double psp;

    public Student (String name, int age, String univName, double psp) {
        this.name = name;
     	this.age = age;
     	this.univName = univName;
     	this.psp = psp;
    }
}
```

### This Keyword in Java

* It's typically used to distinguish between **`object variables`** and **`parameter variables`** with the same names.
* This enhances code clarity and prevents naming conflicts.
* Example "title" is a parameter name as well as class variable. If we put **`this.title`**, then we know it is class variable.

## Constructor Code (Python)

```javascript
class Student:
    # Without parameter
    def __init__(self):
        self.name = "Bikram"
        self.age = 40
        self.psp = 29.4
        self.univ_name = "Unknown"
        
    # With parameter
    def __init__(self, name, age, psp, univ_name):
        self.name = name
        self.age = age
        self.univ_name = univ_name
        self.psp = psp
```

### Object creation with parameterised constructor
```javascript
python_b1 = Book("Salmaan Bhai", 20, "Holy", 55.6)
```

### Self Keyword in Python

- **`Self`** keyword is same as "this" keyword in Java.
- But whether **self** is used or not inside the method, it is important to pass as a parameter to the methods of class.
- We can also say that **self** helps in establishing connection between calling object and class methods.


---
## Shallow Copy VS Deep Copy


### Problem Statement
Let's say we already have an object of student class, and then we want to create a new object of student that has the exact same values of attributes as older objects.

**For example:**
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/085/262/original/Screenshot_2024-08-07_at_1.24.57_PM.png?1723017310" width=550 />


---

### Question

Should we write `Student st2 = st1;`?

### Choices

- [ ] Yes
- [ ] In some cases only
- [x] No

###  Explanation


Let's see how do things work internally?
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/085/263/original/Screenshot_2024-08-07_at_1.26.20_PM.png?1723017392" width="500"/>

* So we have a memory, and st1 is present in the memory with all the data, as shown in the above diagram. 
* When we write student `st2 = st1`, we just make st2 to point as s1, i.e., **a new object is not created**.
* Now the problem here is if we do changes in st2, i.e. `st2.name = 'xyz'`, it will change the value of st1.
---

### The above is also known as "Shallow Copy" - when no new object gets. created.

---
## Deep Copy


For creating a new copy of object, we will have to create object using "new" keyword and assign the values to it.

Example -
An object "st" already exist, now we want to create a copy of it.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/085/261/original/Screenshot_2024-08-07_at_1.00.32_PM.png?1723015881" width=500 />

So, we can simply write -


### Student st2 = new Student("Bikram", 40, 29.4, "ABC");

The above it the deep copy, where we use "new" keyword to create the object.


---
## Linked List


### Issues with Array 
We need continuous space in memory to store Array elements. Now, it may happen that we have required space in chunks but not continuous, then we will not be able to create an Array.

### Linked List
* A linear data structure that can utilize all the free memory 
* We need not have continuous space to store nodes of a Linked List.

### Representation of Linked List

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/211/original/upload_7e7b22bf1e51fd9e12b9c9a524701df4.png?1696392677" width=300/>

* it has a data section where the data is present
* a next pointer which points to next element of the linked list

### Structure of Linked List

```java
class Node{
    int data;
    Node next;
    Node(int x){
        data = x;
        next = null;
    }
}
```
### Example of Linked List

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/212/original/upload_ea3fcb891dd06906043a69f5ebabec0d.png?1696392700" width=500/>

<br/>

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/213/original/upload_cb6b9e12558bfca662aa0c8d7502a807.png?1696392732" width=500/>

* the first node of the linked list is called head
* any linked list is represented by its first node

---


### Question
Where will the "next" pointer of the last node point to?

### Choices
- [ ] First Node
- [ ] Any Node
- [ ] Middle Node
- [x] Null


---


### Question
From which node can we travel the entire linked list ?

### Choices
- [ ] Middle
- [x] First
- [ ] Last
- [ ] Any Node


---
## Access kth element


### Access kth element(k = 0; k is the first element)

```java
Node temp = Head // temp is a compy
for i -> 1 to k {
    temp = temp.next
}
return temp.data // never update head otherwise the first node is lost
```
> Time complexity to access the kth element is O(K). Here we can see that linked list takes more time compared to array as it would take constant time to access the kth element.
