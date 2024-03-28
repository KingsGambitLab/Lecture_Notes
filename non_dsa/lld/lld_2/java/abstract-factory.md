# Abstract Factory design pattern

- [Abstract Factory and adapter design patterns](#abstract-factory-pattern)
  - [Abstract Factory](#abstract-factory)
    - [Advantages of Abstract Factory](#advantages-of-abstract-factory)
    - [Implementation](#implementation)
  - [Recap](#recap)
  - [Design patterns in different languages](#design-patterns-in-different-languages)
    - [Abstract Factory](#abstract-factory-1)
      - [Python](#python)
      - [JavaScript](#javascript)

## Abstract Factory

> The abstract factory pattern is a creational pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

Let us take the example of a classroom. We have already created a `User` abstract class. Now we will create the concrete classes `Student` and `Teacher`. To restrict the usage of subclasses, we can create factories for each of the concrete classes. The `StudentFactory` will be used to create `Student` objects and the `TeacherFactory` will be used to create `Teacher` objects.
 

```java
class StudentFactory {
    public User createStudent(String firstName, String lastName) {
        return new Student(firstName, lastName);
    }
}

class TeacherFactory {
    public User createTeacher(String firstName, String lastName) {
        return new Teacher(firstName, lastName);
    }
}
```

So now in order to create a classroom, we can use the respective factories to create the objects.

```java
StudentFactory studentFactory = new StudentFactory();
Student student = studentFactory.createStudent("John", "Doe");

TeacherFactory teacherFactory = new TeacherFactory();
Teacher teacher = teacherFactory.createTeacher("John", "Doe");
```

But now we have a problem, we can use the factories to create any type of student and teacher. Should a teacher teaching Physics be able to teach a student of Biology class? This is where the concept of related or a family of objects comes into play. The `Student` and `Teacher` objects are related to each other. A teacher should only be able to teach a student of the same class. So we can create a factory that can create a family of related objects. The `ClassroomFactory` will be used to create `Student` and `Teacher` objects of the same class.

```java
abstract class ClassroomFactory {
    public abstract Student createStudent(String firstName, String lastName);
    public abstract Teacher createTeacher(String firstName, String lastName);
}
```

Now we can create concrete factories for each family of related objects that we want to create.

```java
class BiologyClassroomFactory extends ClassroomFactory {
    @Override
    public Student createStudent(String firstName, String lastName) {
        return new BiologyStudent(firstName, lastName);
    }

    @Override
    public Teacher createTeacher(String firstName, String lastName) {
        return new BiologyTeacher(firstName, lastName);
    }
}
```
The class `ClassroomFactory` is an abstract class that contains the factory methods for creating the objects. The child classes can override the factory methods to create objects of their own type. The client code can request an object from the factory class without having to know the class of the object that will be returned.

```java
ClassroomFactory factory = new BiologyClassroomFactory();
Student student = factory.createStudent("John", "Doe");
Teacher teacher = factory.createTeacher("John", "Doe");
```

The class `ClassroomFactory` becomes our abstract factory that essentially is a factory of factories.

### Advantages of Abstract Factory
* `Isolate concrete classes` - The client code is not coupled to the concrete classes of the objects that it creates.
* `Easy to exchange product families` - The client code can request an object from the factory class without having to know the class of the object that will be returned. This makes it easy to exchange product families.
* `Promotes consistency among products` - The client code can request an object from the factory class without having to know the class of the object that will be returned. This makes it easy to maintain consistency among products.

### Implementation
1. `Abstract product interface` - Create an interface for the products that will be created by the factory.
```java
interface Button {
    void render();
    void onClick();
}
```
2. `Concrete products` - Create concrete classes that implement the product interface.
```java
class RoundedButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendered rounded button");
    }

    @Override
    public void onClick() {
        System.out.println("Clicked rounded button");
    }
}
```

3. `Abstract factory interface` - Create an interface for the abstract factory that will be used to create the products.
```java
interface FormFactory {
    Button createButton();
}
```

4. `Concrete factories` - Create concrete classes that implement the abstract factory interface.
```java
class RoundedFormFactory implements FormFactory {
    @Override
    public Button createButton() {
        return new RoundedButton();
    }
}
```
5. `Client code` - Request an object from the factory class without having to know the class of the object that will be returned.
```java
FormFactory factory = new RoundedFormFactory();
Button button = factory.createButton();
```

## Recap
* The factory pattern is a creational design pattern that can be used to create objects without having to specify the exact class of the object that will be created.
* It reduces the coupling between the client code and the class of the object that it is creating.
* Simple factory - The factory class contains a static method for creating objects. This technique is easy to implement, but it is not extensible and reusable. It violates the open-closed principle and the single responsibility principle.
* Factory method - The responsibility of creating the object is shifted to the child classes. The factory method is implemented in the base class and the child classes can override the factory method to create objects of their own type. This technique is extensible and reusable. It follows the open-closed principle and the single responsibility principle.


## Design patterns in different languages

### Abstract Factory
#### Python
* [Abstract Factory - I](https://refactoring.guru/design-patterns/abstract-factory/python/example)
* [Abstract Factory - II](https://stackabuse.com/abstract-factory-design-pattern-in-python/)
* [Abstract Factory - III](https://python-patterns.guide/gang-of-four/abstract-factory/)
* [Abstract Factory - IV](https://python.plainenglish.io/abstract-factory-design-pattern-in-python-9a3de77d01eb)

#### JavaScript
* [Abstract Factory - I - Typescript](https://refactoring.guru/design-patterns/abstract-factory/typescript/example#example-0)
* [Abstract Factory - II](https://dev.to/carlillo/understanding-design-patterns-abstract-factory-23e7)
* [Abstract Factory - III](https://gist.github.com/OriginUnknown/d2fc38c8412b52ece8de)
