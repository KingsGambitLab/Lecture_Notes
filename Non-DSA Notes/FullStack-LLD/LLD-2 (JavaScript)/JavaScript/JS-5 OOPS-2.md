

## Agenda
**Topics to cover in Javascript Oops**
* This keyword 
* Constructor functions
* Classes & Classical Inheritance
* Prototype &  Prototypal Inheritance
* Call ,Apply & Bind Methods
* Memory of objects (Reference Datatypes)

We will try to cover most of these topics in today's sessions and the remaining in the next.

It is going to be a bit challenging, advanced, but very interesting session covering topics that are asked very frequently in interviews.

So let's start.

## Classes and Constructors in OOP

The concept of classes and constructors in the context of Object-Oriented Programming (OOP) and the similarities between classes and constructor functions. Here's a more organized explanation of the concepts:


1. **Classes:** In modern JavaScript (ES6 and later), classes provide a way to define blueprints for creating objects. A class is a template for creating objects with shared properties and methods.

2. **Constructor Functions:** In pre-ES6 JavaScript, constructor functions were widely used to create objects with similar properties and methods. They serve as templates for creating instances of objects.

**Shared Properties and Methods:**

- Both classes and constructor functions allow you to create multiple objects (instances) that share the same properties and methods defined by the class or constructor.

**Constructor Method:**

- In both classes and constructor functions, the constructor method is used to initialize the properties of an object when it's created. It's automatically invoked when you create a new instance of the class or constructor.

**Using `this`:**

- Within the constructor method, the `this` keyword is used to refer to the current instance being created. It's used to set the initial values of the instance's properties.

**Example (Assuming Based on Context):**

Here's a restructured example based on the context you've provided:

```javascript
// Class (ES6+)
class Person {
  constructor(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
  }
}

// Creating instances of the Person class
const person1 = new Person("Adam", 24, "Male");
const person2 = new Person("Gage", 30, "Male");

// Constructor Function (Pre-ES6)
function Car(brand, model, color) {
  this.brand = brand;
  this.model = model;
  this.color = color;
}

// Creating instances of the Car constructor
const car1 = new Car("Mercedes", "S-Class", "Blue");
const car2 = new Car("Jaguar", "XE", "Black");

// Accessing properties of instances
console.log(person1.name); // Output: "Adam"
console.log(car1.model);   // Output: "S-Class"
```

In this example, both the `Person` class and the `Car` constructor serve as blueprints for creating instances. The `constructor` method (implicitly in classes, explicitly in constructors) sets the initial properties for the instances.

It's important to note that while the concepts and usage are similar, the syntax and capabilities of classes are more modern and flexible than traditional constructor functions. ES6 introduced classes as a more organized and syntactically convenient way to work with OOP concepts in JavaScript.

Certainly! It seems like you want to know about the structure of a class in JavaScript, including the constructor, prototype methods, and static methods. Here's a breakdown of each part:

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  // Prototype Method
  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }

  // Static Method
  static compareAges(person1, person2) {
    if (person1.age > person2.age) {
      return `${person1.name} is older than ${person2.name}.`;
    } else if (person1.age < person2.age) {
      return `${person2.name} is older than ${person1.name}.`;
    } else {
      return `${person1.name} and ${person2.name} are the same age.`;
    }
  }
}
```

Here's a breakdown of the components of the `Person` class:

1. **Constructor:**
   - The constructor method is used to create and initialize instances of the class.
   - It's called automatically when a new instance is created using the `new` keyword.
   - In the example, the constructor takes `name` and `age` parameters and assigns them to the instance's properties using `this`.

2. **Prototype Method (`greet`):**
   - Prototype methods are added to the class's prototype, which means they are shared among all instances of the class.
   - In the example, the `greet` method is defined, which logs a message with the person's name and age.
   - This method can be called on any instance of the `Person` class.

3. **Static Method (`compareAges`):**
   - Static methods are called on the class itself, rather than on instances of the class.
   - In the example, the `compareAges` static method is defined to compare the ages of two people and return a message.
   - This method can be called on the `Person` class itself, without needing to create instances.

Here's how you would use the class:

```javascript
const person1 = new Person("Alice", 30);
const person2 = new Person("Bob", 25);

person1.greet(); // Output: Hello, my name is Alice and I am 30 years old.
person2.greet(); // Output: Hello, my name is Bob and I am 25 years old.

console.log(Person.compareAges(person1, person2)); // Output: Alice is older than Bob.
```

In this example, the class `Person` encapsulates the properties (name, age) and behaviors (greeting and age comparison) of a person. The constructor initializes the properties, the `greet` method is a shared behavior among instances, and the `compareAges` method is a static utility method to compare the ages of different persons.


## Inheritance in JavaScript

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows you to create a new class based on an existing class. The new class inherits properties and methods from the existing class, which is often referred to as the parent class or superclass. The new class is known as the subclass or child class.

**Example:**

Let's use an example to illustrate inheritance in JavaScript:

```javascript
// Parent class (Superclass)
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

// Child class (Subclass)
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age); // Call the parent class constructor
    this.grade = grade;
  }

  study() {
    console.log(`${this.name} is studying hard for their exams.`);
  }
}

// Creating instances of the subclasses
const person = new Person("Alice", 30);
const student = new Student("Bob", 18, "12th");

// Using inherited methods and subclass-specific methods
person.greet();    // Output: Hello, my name is Alice and I am 30 years old.
student.greet();   // Output: Hello, my name is Bob and I am 18 years old.
student.study();   // Output: Bob is studying hard for their exams.
```

In this example:
- The `Person` class serves as the parent class. It has a `constructor` and a `greet` method.
- The `Student` class is the child class that extends the `Person` class using the `extends` keyword. It adds a `grade` property and a `study` method.
- The `super()` method is used in the `Student` constructor to call the constructor of the parent class and pass the required parameters.
- Instances of both classes are created and can access inherited methods (`greet`) as well as subclass-specific methods (`study`).

By using inheritance, you can create a hierarchy of classes with shared behavior and properties, making your code more organized, reusable, and easier to maintain.

Let's create three classes: `Person`, `Student`, and `Teacher`, to demonstrate inheritance and the usage of `this` keyword. The `Person` class will be the parent class, and both `Student` and `Teacher` will be subclasses that inherit from `Person`. We'll also explore how to use the `super` keyword to call the parent class's constructor.

```javascript
// Parent class
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  introduce() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

// Subclass: Student
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age); // Call parent class's constructor using super()
    this.grade = grade;
  }

  study() {
    console.log(`${this.name} is studying.`);
  }
}

// Subclass: Teacher
class Teacher extends Person {
  constructor(name, age, subject) {
    super(name, age);
    this.subject = subject;
  }

  teach() {
    console.log(`${this.name} is teaching ${this.subject}.`);
  }
}

// Creating instances
const person = new Person("Alice", 30);
const student = new Student("Bob", 18, "12th");
const teacher = new Teacher("Eve", 40, "Math");

// Using methods and properties
person.introduce(); // Output: Hello, my name is Alice and I am 30 years old.

student.introduce(); // Output: Hello, my name is Bob and I am 18 years old.
student.study();     // Output: Bob is studying.

teacher.introduce(); // Output: Hello, my name is Eve and I am 40 years old.
teacher.teach();     // Output: Eve is teaching Math.
```

Explanation:

1. The `Person` class is the parent class. It has a constructor that initializes `name` and `age`, and an `introduce` method that uses the `this` keyword to access the instance properties.

2. The `Student` class is a subclass of `Person`. It uses the `super` keyword to call the parent class's constructor and sets the `grade` property. It also has a `study` method.

3. The `Teacher` class is another subclass of `Person`. It similarly calls the parent class's constructor using `super` and sets the `subject` property. It also has a `teach` method.

4. Instances of all three classes (`person`, `student`, and `teacher`) are created and methods from the parent and subclass are called.

In this example, the `super` keyword is used to invoke the constructor of the parent class, and the `this` keyword is used to access instance-specific properties and methods. Inheritance allows `Student` and `Teacher` to reuse properties and methods from the `Person` class, demonstrating the concept of code reusability in object-oriented programming.

---
title: Prototype &  Prototypal Inheritance
description: Concept Prototype &  Prototypal Inheritance in the OOP
duration: 2100
card_type: cue_card
---
## Prototype and Constructor Function
The concepts of prototype, constructor functions, and objects with an example of creating car objects with a shared prototype method.

In JavaScript, every function has a property called `prototype`, which is an object that can be used as a blueprint for creating new objects.

```javascript
// Constructor Function for Car
function Car(name, color) {
  this.name = name;
  this.color = color;
}

// Adding a shared prototype method
Car.prototype.drive = function() {
  console.log(`${this.name} is driving.`);
};
```

### Creating Objects with Constructor Function

Objects created using a constructor function share properties and methods defined in the prototype.

```javascript
// Creating car objects using the constructor function
const car1 = new Car("Toyota", "Blue");
const car2 = new Car("Ford", "Red");
const car3 = new Car("Honda", "Silver");

// Using the shared prototype method
car1.drive(); // Output: Toyota is driving.
car2.drive(); // Output: Ford is driving.
car3.drive(); // Output: Honda is driving.
```

In this example:
- The `Car` constructor function defines properties `name` and `color`.
- We add a shared prototype method `drive()` to the `Car` constructor's prototype.
- Three car objects (`car1`, `car2`, `car3`) are created using the constructor function.
- All three car objects share the `drive()` method from the prototype.

### Prototype Chain

The prototype chain allows objects to inherit properties and methods from their prototypes.

```javascript
console.log(car1.hasOwnProperty("name")); // true
console.log(car1.hasOwnProperty("drive")); // false
```

- The `hasOwnProperty` method checks if a property is directly defined on the object.
- The `name` property is directly defined on the `car1` object, so `hasOwnProperty` returns `true`.
- The `drive` method is inherited from the prototype, so `hasOwnProperty` returns `false`.

Absolutely, I'll break down the concept of prototypes and how they relate to constructor functions using the example of three car objects with a shared `drive()` method.


**Example - Car Objects:**

```javascript
// Constructor function for Car
function Car(name, color) {
  this.name = name;
  this.color = color;
}

// Adding a shared method to the Car constructor's prototype
Car.prototype.drive = function() {
  console.log(`${this.name} is driving.`);
};

// Creating car instances
const car1 = new Car("Toyota", "Blue");
const car2 = new Car("Honda", "Red");
const car3 = new Car("Ford", "Black");

// Using the shared method
car1.drive(); // Output: Toyota is driving.
car2.drive(); // Output: Honda is driving.
car3.drive(); // Output: Ford is driving.
```

Explanation:

- The `Car` constructor function is created with parameters `name` and `color`, which set the properties of each car object.
- The `drive` method is added to the `Car` constructor's prototype. This means all instances of `Car` will have access to the `drive` method through inheritance.
- Three car instances (`car1`, `car2`, and `car3`) are created using the `Car` constructor.
- The `drive` method is called on each car instance, and it uses the `this` keyword to refer to the specific instance.

In this example, the `drive` method is defined once on the prototype of the `Car` constructor, and all car instances share this method. This approach reduces memory usage and makes the code more efficient since the method isn't duplicated for each instance.

Remember, prototypes and constructor functions are at the core of how JavaScript implements inheritance and code reuse.

### Method shadowing
Method shadowing refers to the concept of overriding a method inherited from a parent object's prototype by defining a method with the same name in the child object. In your context of constructor functions and prototypes, let's explore method shadowing using the car example:

```javascript
// Constructor function for Car
function Car(name, color) {
  this.name = name;
  this.color = color;
}

// Adding a shared method to the Car constructor's prototype
Car.prototype.drive = function() {
  console.log(`${this.name} is driving.`);
};

// Child constructor function for ElectricCar
function ElectricCar(name, color, batteryType) {
  Car.call(this, name, color); // Call the parent constructor to set name and color
  this.batteryType = batteryType;
}

// Inherit from Car prototype
ElectricCar.prototype = Object.create(Car.prototype);

// Adding a method specific to ElectricCar
ElectricCar.prototype.charge = function() {
  console.log(`${this.name} is charging.`);
};

// Method shadowing in ElectricCar
ElectricCar.prototype.drive = function() {
  console.log(`${this.name} is driving silently.`);
};

// Creating car instances
const car1 = new Car("Toyota", "Blue");
const eCar1 = new ElectricCar("Tesla", "Black", "Lithium-ion");

// Using the drive method
car1.drive();   // Output: Toyota is driving.
eCar1.drive();  // Output: Tesla is driving silently.
```

Explanation:

1. We have the `Car` constructor with a shared `drive` method.
2. We create a child constructor `ElectricCar` that inherits properties from `Car` using `Car.call(this, name, color)`.
3. We set up inheritance for the `ElectricCar` prototype using `Object.create(Car.prototype)`.
4. We add a specific method `charge` for `ElectricCar`.
5. We use method shadowing by defining a new `drive` method in `ElectricCar` prototype, which overrides the inherited `drive` method.

In the example, `ElectricCar` inherits the `drive` method from `Car`. However, by defining a new `drive` method in `ElectricCar`, the inherited method is shadowed or overridden. This is a way to provide specialized behavior for a method in a subclass while still utilizing the inheritance structure.

Remember, method shadowing allows you to override inherited methods, giving you flexibility to adapt and extend functionality in child classes.