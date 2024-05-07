

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

## This Keyword
Certainly! When covering Object-Oriented Programming (OOP) in JavaScript, the `this` keyword is a crucial concept to understand. Here's a breakdown of topics you can cover regarding the `this` keyword in JavaScript and its relevance to OOP:

1. **Introduction to `this` keyword:**
   - Explain that `this` is a special keyword in JavaScript that refers to the current execution context or the current object.
   - Mention that its value depends on how a function is called, rather than where it is defined.

2. **Global Context:**
   - Describe that in the global context (outside of any function), `this` refers to the global object (e.g., `window` in browsers, `global` in Node.js).

3. **Function Context:**
   - Explain that within a function, the value of `this` can change based on how the function is invoked.
   - Discuss function invocation methods:
     - Regular function invocation: `this` usually refers to the global object (in non-strict mode) or `undefined` (in strict mode).
     - Method invocation: `this` refers to the object that the method is called on.
     - Constructor invocation: `this` refers to the instance being created by the constructor function.
     - `call()` and `apply()` methods: Explicitly set `this` for a function call.
     - Arrow functions: `this` retains the value of the enclosing lexical context.

4. **Object-Oriented Programming (OOP) and `this`:**
   - Explain how `this` is used in the context of OOP to refer to the instance of an object.
   - Describe how methods within an object can access other properties and methods using `this`.

5. **Common `this` Pitfalls:**
   - Describe issues that developers often face with `this`:
     - Losing `this` context in nested functions.
     - Using `this` in callbacks without proper binding.
     - Caching `this` in a variable to ensure proper reference in nested scopes.

6. **Solving `this` Issues:**
   - Introduce solutions to common `this` problems:
     - Using `.bind()`, `.call()`, or `.apply()` to explicitly set `this`.
     - Storing a reference to the outer `this` in a variable to use within nested functions.
     - Using arrow functions to preserve the lexical scope's `this`.

7. **Examples and Demonstrations:**
   - Provide code examples for each type of function invocation and how `this` behaves in each case.
   - Show scenarios where `this` is used within object methods to access object properties.

8. **Best Practices:**
   - Emphasize the importance of understanding the context in which `this` is used.
   - Encourage using arrow functions in methods when you want to retain the outer scope's `this`.
   - Suggest using modern ES6 features like classes to manage `this` more effectively.

9. **Browser vs. Node.js:**
   - Mention the differences in the global object (`window` vs. `global`) and how they affect `this` behavior.

### `this` keyword in Node.js in non-strict mode

Certainly, let's break down the behavior of the `this` keyword in Node.js in non-strict mode for each of the scenarios you mentioned. After that, I'll provide a summary in tabular form.

Assumption: `fn` is a function defined globally, and `obj` is an object containing a method `fn`.

```javascript
// Scenario 1: Console.log(this)
console.log("Scenario 1:");
console.log(this); // Output: {}

// Scenario 2: Console.log(this) -> fn = global object
console.log("Scenario 2:");
function fnGlobal() {
  console.log(this === global); // true
}
fnGlobal();

// Scenario 3: this -> obj -> fn = object itself
console.log("Scenario 3:");
var obj = {
  fn: function () {
    console.log(this === obj); // true
  }
};
obj.fn();

// Scenario 4: this -> obj -> fn -> fn = global object
console.log("Scenario 4:");
var obj2 = {
  fn: function () {
    console.log(this === obj2); // true
    var nestedFn = function () {
      console.log(this === global); // true
    };
    nestedFn();
  }
};
obj2.fn();
```

Now, let's summarize these scenarios in a tabular form:

| Scenario | Code                                   | Output                                    | Explanation                                        |
|----------|-----------------------------------------|-------------------------------------------|----------------------------------------------------|
| 1        | `console.log(this);`                   | `{}`                                      | In global context, `this` refers to the global object. |
| 2        | `function fnGlobal() {...}`<br>`fnGlobal();` | `true` (inside the function)              | In a regular function, `this` refers to the global object. |
| 3        | `obj.fn = function() {...}`<br>`obj.fn();` | `true` (inside the method)                | Inside an object method, `this` refers to the object itself. |
| 4        | `obj2.fn = function() {...}`<br>`obj2.fn();` | `true` (inside the method)<br>`true` (inside nested function) | Inside a nested function, `this` reverts to the global object. |

In scenarios 3 and 4, `this` refers to the object containing the method when that method is directly invoked. However, when a nested function is defined within the method and invoked within it, `this` inside the nested function refers to the global object (`global` in Node.js).

Understanding these behaviors helps in writing clean and predictable code, especially when dealing with methods and nested functions within objects.

### `this` keyword in Browser in non-strict mode

Certainly, let's break down the behavior of the `this` keyword in Browser in non-strict mode for each of the scenarios you mentioned. After that, I'll provide a summary in tabular form.

Assumption: `fn` is a function defined globally, and `obj` is an object containing a method `fn`.

Sure, let's break down each scenario and then summarize them in a tabular form.

**Scenario 1: `console.log(this)`**

```javascript
console.log(this); // Window Object
```

In this scenario, if you directly execute `console.log(this)` in the global context of a web browser (not within any function or object), the output will be the `Window` object. This is because `this` refers to the global object, which is the `Window` object in a browser environment.

**Scenario 2: `console.log(this)` inside a function**

```javascript
function exampleFunction() {
  console.log(this);
}

exampleFunction(); // Window Object
```

In this case, when you call `exampleFunction()`, it's being invoked as a regular function. The `this` inside the function still refers to the global object (`Window` in the browser).

**Scenario 3: `this` inside an object method**

```javascript
var obj = {
  prop: 'I am a property',
  method: function() {
    console.log(this.prop);
  }
};

obj.method(); // "I am a property"
```

In this scenario, `obj` is an object containing a method named `method`. When you call `obj.method()`, the `this` inside the `method` refers to the `obj` itself. Therefore, `this.prop` accesses the `prop` property of the `obj` object.

**Scenario 4: `this` inside nested functions**

```javascript
var obj = {
  prop: 'I am a property',
  method: function() {
    var nestedFunction = function() {
      console.log(this.prop);
    };
    nestedFunction();
  }
};

obj.method(); // undefined
```

Here, within the `nestedFunction`, `this` refers to the global object (`Window` in the browser). This is because the function `nestedFunction` is not a method of `obj`. As a result, `this.prop` will be `undefined` since the global object doesn't have a `prop` property.

Now, let's summarize these scenarios in a tabular form:

| Scenario                   | `this` Value                   | Explanation                                                                   |
|---------------------------|--------------------------------|-------------------------------------------------------------------------------|
| `console.log(this)`       | Window Object                  | Global context, `this` refers to the global object (`Window` in browser).     |
| `console.log(this)`       | Window Object                  | Inside a regular function, `this` still refers to the global object.          |
| `this` in object method   | `obj` (object itself)          | Inside a method, `this` refers to the object on which the method is invoked. |
| `this` in nested function | Window Object                  | Inside a nested function, `this` refers to the global object.                 |

Understanding these scenarios is important for grasping how `this` behaves in different contexts within a browser environment.

### `this` keyword in Node.js in strict mode

Certainly, let's break down the behavior of the `this` keyword in Node.js in strict mode for each of the scenarios you mentioned. After that, I'll provide a summary in tabular form.

Assumption: `fn` is a function defined globally, and `obj` is an object containing a method `fn`. Here's what each scenario seems to be referring to:

1. **`console.log(this)` (Scenario 1)**:
   ```javascript
   "use strict";
   console.log(this); // Outputs an empty object ({})
   ```
   In strict mode, when you log `this` in the global context, it will be an empty object `{}`. This is because strict mode prevents the default binding of `this` to the global object.

2. **`console.log(this)` with Undefined Function (Scenario 2)**:
   ```javascript
   "use strict";
   function myFunction() {
     console.log(this);
   }
   myFunction(); // Outputs undefined
   ```
   In strict mode, when you call a function without specifying its context (`this`), it's set to `undefined`. This is different from non-strict mode, where it would point to the global object.

3. **`this` Inside an Object Method (Scenario 3)**:
   ```javascript
   "use strict";
   var obj = {
     prop: "I'm a property",
     method: function() {
       console.log(this.prop);
     }
   };
   obj.method(); // Outputs "I'm a property"
   ```
   When a method is invoked on an object, `this` within the method refers to the object itself. So, `this.prop` accesses the `prop` property of the `obj` object.

4. **`this` Inside Nested Object Methods (Scenario 4)**:
   ```javascript
   "use strict";
   var outerObj = {
     innerObj: {
       method: function() {
         console.log(this);
       }
     }
   };
   outerObj.innerObj.method(); // Outputs the inner object
   ```
   Inside nested object methods, `this` refers to the closest containing object. In this case, it points to `innerObj` when the `method` is invoked.

Now, let's summarize these scenarios in tabular form:

| Scenario | Example Code                                | `this` Value           | Explanation                                                      |
|----------|---------------------------------------------|------------------------|------------------------------------------------------------------|
| 1        | `console.log(this);`                        | `{}`                   | In strict mode, `this` is an empty object in the global context. |
| 2        | `myFunction();`                             | `undefined`            | Calling a function without context results in `undefined`.     |
| 3        | `obj.method();`                            | `obj` object reference| `this` in an object method points to the object itself.         |
| 4        | `outerObj.innerObj.method();`              | `innerObj` object reference | In nested methods, `this` refers to the closest containing object.  |

Understanding these scenarios and how `this` behaves in different contexts is crucial for writing reliable and maintainable code.


### `this` keyword in Browser in strict mode

Certainly, let's break down the behavior of the `this` keyword in Browser in strict mode for each of the scenarios you mentioned. After that, I'll provide a summary in tabular form.

Assumption: `fn` is a function defined globally, and `obj` is an object containing a method `fn`. Assuming you have the following setup in a browser environment:

```javascript
"use strict";

// Scenario 2
console.log("Scenario 2:");
console.log(this); // Output: undefined

// Scenario 3
var obj = {
  fn: function () {
    console.log("Scenario 3:");
    console.log(this); // Output: obj
  },
};

// Scenario 4
var fn = obj.fn;

// Scenario 1
console.log("Scenario 1:");
console.log(this); // Output: window

// Scenario 4 (contd.)
console.log("Scenario 4:");
fn(); // Output: undefined
```

Now, let's summarize these scenarios in a tabular form:

| Scenario | Code                                             | `this` Value         | Explanation                                                                                       |
|----------|--------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------|
| 1        | `console.log(this);`                            | `window` object     | In the global context, `this` refers to the global object (`window` in browsers).               |
| 2        | `"use strict"; console.log(this);`             | `undefined`         | In strict mode, `this` in the global context is `undefined`.                                    |
| 3        | `obj.fn();`                                     | `obj` object        | When calling a method (`fn`) of an object (`obj`), `this` refers to the object itself (`obj`). |
| 4        | `var fn = obj.fn; fn();`                        | `undefined`         | When a method (`fn`) is assigned to a variable (`fn`) and called, `this` is `undefined`.        |

In summary:

1. In the global context, outside of any function, `this` refers to the global object (`window` in browsers).
2. In strict mode, in the global context, `this` is `undefined`.
3. When a function is a method of an object, `this` within the function refers to the object itself.
4. If a method is assigned to a variable and then invoked, `this` inside the method will be `undefined`.

Remember, the behavior of `this` can be a bit tricky, especially when dealing with nested functions, callbacks, and different contexts. Understanding these scenarios helps you write more predictable and maintainable code in JavaScript.


## Constructor Functions

In JavaScript, constructor functions are used to create and initialize objects. They serve as templates for creating objects with similar properties and methods. Constructor functions are typically written with an initial capital letter to distinguish them from regular functions.

A constructor function defines the structure of an object by setting its properties and methods using the `this` keyword. When you create an object using a constructor function with the `new` keyword, it creates a new instance of that object type and binds the instance to the `this` keyword within the constructor function.

**Car Company Example:**

Imagine you're building a car manufacturing company. Each car will have properties like the make, model, year, and color. You can create a constructor function called `Car` to represent a car object.

**Coding Example:**

Here's how you can implement the car company example using a constructor function:

```javascript
// Constructor function for Car
function Car(make, model, year, color) {
  this.make = make;
  this.model = model;
  this.year = year;
  this.color = color;
  
  this.start = function() {
    console.log(`Starting the ${this.make} ${this.model}`);
  };
}

// Creating car instances
const car1 = new Car("Toyota", "Camry", 2022, "Blue");
const car2 = new Car("Ford", "Mustang", 2023, "Red");

// Using the car instances
console.log(car1); // Car { make: 'Toyota', model: 'Camry', year: 2022, color: 'Blue' }
console.log(car2); // Car { make: 'Ford', model: 'Mustang', year: 2023, color: 'Red' }

car1.start(); // Starting the Toyota Camry
car2.start(); // Starting the Ford Mustang
```

In this example:
- The `Car` constructor function defines the properties (`make`, `model`, `year`, `color`) and the `start` method for a car object.
- Instances of cars (`car1` and `car2`) are created using the constructor function.
- The `start` method is accessed and invoked on each car instance.

By using constructor functions, you can create multiple car instances with the same structure but different property values. This follows the fundamental concept of OOP, where you create objects based on blueprints (constructor functions) that define their structure and behavior.

### Constructor function with `this` example

```javascript
// Constructor function for Car
function Car(nameParam, colorParam, topSpeedParam) {
  // Using 'this' to refer to instance-specific properties
  this.name = nameParam;
  this.color = colorParam;
  this.topSpeed = topSpeedParam;

  // Using 'this' to refer to instance-specific method
  this.drive = function() {
    console.log(`I am driving ${this.name}`);
  };
}

// Creating car instances using 'new'
let car1 = new Car("Ferrari", "Red", '1000km/hr');
let car2 = new Car("8", 'white', '600km/hr');

// Using the car instances
car1.drive(); // Output: I am driving Ferrari
car2.drive(); // Output: I am driving 8
```

Explanation of `this` usage:

1. In the constructor function (`Car`):
   - When creating a new instance using the constructor with `new`, the `this` keyword refers to the newly created instance.
   - Properties (`name`, `color`, `topSpeed`) are assigned to the instance using `this` followed by the property name. For example, `this.name` refers to the `name` property of the specific instance being created.
   - The `drive` method is assigned to each instance with `this.drive`. Inside the `drive` method, `this.name` refers to the `name` property of the instance that is calling the method. This allows each instance to have its own unique behavior.

2. When creating car instances:
   - `let car1 = new Car("Ferrari", "Red", '1000km/hr');` creates an instance of `Car` named `car1`. Within the constructor, `this.name` becomes "Ferrari" for `car1`.
   - `let car2 = new Car("8", 'white', '600km/hr');` creates another instance named `car2`. Inside the constructor, `this.name` becomes "8" for `car2`.

3. Using the car instances:
   - Calling the `drive` method on `car1` (`car1.drive()`) prints "I am driving Ferrari". Within the method, `this.name` refers to the `name` property of `car1`.
   - Calling the `drive` method on `car2` (`car2.drive()`) prints "I am driving 8". Within the method, `this.name` refers to the `name` property of `car2`.

The `this` keyword is essential in JavaScript's OOP to distinguish properties and methods of each individual instance when using constructor functions to create objects.

