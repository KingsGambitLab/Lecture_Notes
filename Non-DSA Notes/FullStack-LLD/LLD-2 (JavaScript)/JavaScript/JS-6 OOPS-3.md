# Full Stack LLD & Projects: JavaScript - OOPS-3 : Call Apply Bind and Memory of Objects

**Agenda of this Lecture:**

* Call Method 
* Apply Method
* Bind Method
* How memory of reference data type works
     * Shallow copy
     * Deep copy


Lets consider and example:


```javascript 
let student = {
  firstName: 'Adam',
  lastName: 'Smith',
  age: 25,
  
  getEmail: function() {
    console.log(`${this.firstName}.${this.lastName}@gmail.com`);
  }
};

// Calling the getEmail function using the 'call' method
student.getEmail();
```




If we want to avoid repeating the code for the `getEmail` function for both the student and teacher objects by creating a shared function and using call to bind it to different objects.

```javascript 
function getEmailFn() {
  console.log(`${this.firstName}.${this.lastName}@gmail.com`);
}

let student = {
  firstName: 'Adam',
  lastName: 'Smith',
  age: 25,
  getEmail: getEmailFn
};

let teacher = {
  firstName: 'Steve',
  lastName: 'Rogers',
  age: 35,
  getEmail: getEmailFn
};

student.getEmail(); 
teacher.getEmail(); 
```

**Note:** This will return an error of `function not defined`. To solve this, we have three methods.



### Explanation

The `getEmail` property should hold a reference to the function` getEmailFn`, not its execution result. Also, the usage of `this.firstName` and `this.lastName` outside a function will not refer to the desired context. Here's the corrected version:

```javascript 
function getEmailFn(firstName, lastName) {
  console.log(`${firstName}.${lastName}@gmail.com`);
}

let student = {
  firstName: 'Adam',
  lastName: 'Smith',
  age: 25,
  getEmail: getEmailFn(this.firstName, this.lastName)
};

let teacher = {
  firstName: 'Steve',
  lastName: 'Rogers',
  age: 35,
  getEmail: getEmailFn(this.firstName, this.lastName)
};

student.getEmail; 
teacher.getEmail; 
```

**Note:** This both will retur `undefined.undefined@gmail.com`

**To solve this , we can use call method**

```javascript 
let student = {
  firstName: 'Adam',
  lastName: 'Smith',
  age: 25,
  getEmail: function() {
    console.log(`${this.firstName}.${this.lastName}@gmail.com`);
  }
};

let teacher = {
  firstName: 'Steve',
  lastName: 'Rogers',
  age: 35,
  getEmail: function() {
    console.log(`${this.firstName}.${this.lastName}@gmail.com`);
  }
};

student.getEmail.call(student);
teacher.getEmail.call(teacher);
```


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/451/original/Screenshot_2023-09-20_150801.png?1695202699)



By using the `call` method, we attach a common `getEmailFn` function to both student and teacher objects, allowing it to be invoked with the correct context using call. This avoids repetition by dynamically binding the function to different objects and ensures accurate email address generation.

**We can pass some arguments as well to the call method:**

```javascript 
function getEmailFn(subjects) {
  return  (${this.firstName}.${this.lastName}@gmail.com)`;
}

function chooseSubject(sub1, sub2) {
  return `${sub1} and ${sub2}`;
}

let teacher1 = {
  firstName: 'Steve',
  lastName: 'Rogers',
  age: 35,
  getEmail: getEmailFn
};

let teacher2 = {
  firstName: 'Tony',
  lastName: 'Stark',
  age: 40,
  getEmail: getEmailFn
};
```

The `call` method in JavaScript allows you to invoke a function on an object while providing a specific context (this value) for that function to use, along with optional arguments that the function can accept. This enables dynamic context binding and the passing of specific values directly to the function being called.


### Explanation

**Apply** and **Call** method are almost same. The only difference is, when we are using apply method, we need to pass an **array** as the argument.

```javascript 
function getEmailFn(subjects) {
  return `${subjects} (${this.firstName}.${this.lastName}@gmail.com)`;
}

function chooseSubject(sub1, sub2) {
  return `${sub1} and ${sub2}`;
}

function chooseBatches(batch1, batch2, batch3) {
  return `${batch1} ${batch2} ${batch3}`;
}

let teacher1 = {
  firstName: 'Steve',
  lastName: 'Rogers',
  age: 35,
  getEmail: getEmailFn
};

let teacher2 = {
  firstName: 'Tony',
  lastName: 'Stark',
  age: 40,
  getEmail: getEmailFn
};
```

**Note:** This will give error as apply method takes array as argument. This is the corrected approach:

```javascript
function getEmailFn(subjects) {
  return `${subjects} (${this.firstName}.${this.lastName}@gmail.com)`;
}

function chooseSubject(sub1, sub2) {
  return `${sub1} and ${sub2}`;
}

function chooseBatches(batch1, batch2, batch3) {
  return [batch1, batch2, batch3];
}

let teacher1 = {
  firstName: 'Steve',
  lastName: 'Rogers',
  age: 35,
  getEmail: getEmailFn
};

let teacher2 = {
  firstName: 'Tony',
  lastName: 'Stark',
  age: 40,
  getEmail: getEmailFn
};

let batches = chooseBatches('BatchA', 'BatchB', 'BatchC');

console.log("Retrieving teacher1's email:");
console.log(teacher1.getEmail.apply(teacher1, batches));

console.log("\nRetrieving teacher2's email:");
console.log(teacher2.getEmail.apply(teacher2, batches));
```

In this version, the apply method is called with the entire batches array as its second argument, as the function getEmailFn only expects a single argument (subjects). This will work correctly because the apply method will pass each element of the array as a separate argument to the function.


### Explanation

The `bind` method in JavaScript creates a new function that, when invoked, has a specific this value set to a provided value. It's useful for "binding" a function to a particular object as its context. The new function produced by bind can also have preset arguments if provided.

```javascript 
let callLater = getEmail.bind(teacher1);
console.log(callLater());
```

**Explanation:**

* `bind` creates a new function callLater that will have the getEmail function's logic from teacher1 as its content.
* The `bind` method doesn't execute the function immediately; it prepares a new function with the specified context.
* To actually execute the callLater function and log the email address, you need to call it with parentheses like `callLater()`.


### Explanation


Lets consider few cases:

**Case-1:**

```javascript 
let person1 = `Adam`;
let person2 = `Steve`;

console.log(person1);
console.log(person2);
```

```
Output:

Adam
Steve
```

**Case-2:**

```javascript 
let person1 = `Adam`;
let person2 = `Steve`;

person2 = person1

console.log(person1);
console.log(person2);
```

```
Output:

Adam
Adam
```

**Case-3:**

```javascript 
let person1 = {
  name: `Adam`,
  age: 25
}


let person2 = person1

console.log(person1);
console.log(person2);
```

``` 
Output:

{ name: 'Adam', age: 25 }
{ name: 'Adam', age: 25 }
```

**Case-4:**

```javascript 
let person1 = {
  name: `Adam`,
  age: 25
}


let person2 = person1

person2.name = 'Steve'

console.log(person1);
console.log(person2);
```

```
Output:

{ name: 'Steve', age: 25 }
{ name: 'Steve', age: 25 }
```
Here's a concise explanation of each case in terms of data types:

**Case-1:**
Strings (Primitive Data Type)
Both person1 and person2 hold separate string values.

**Case-2:**
Strings (Primitive Data Type)
person2 is assigned the value of person1, so they both reference the same string value.

**Case-3:**
Objects (Reference Data Type)
person2 points to the same object as person1, resulting in both variables referencing the same object in memory.

**Case-4:**
Objects (Reference Data Type)
person2 references the same object as person1. Changing a property via one variable affects the shared object's property value.


**Heap and Stack Memory:**

* **Stack Memory:** It's used for function call data and local variables, managed automatically with Last-In-First-Out order. In cases 1-2, stack stores string values and references.
* **Heap Memory:** It's for dynamic memory allocation, managed manually, suitable for larger data structures. In cases 3-4, heap holds shared object data and object property changes.

**Pass by value and Pass by reference:**

* **Pass by Value:** When passing a primitive data type, a copy of the actual value is passed. In cases 1-2, strings are passed by value when assigned or copied.
* **Pass by Reference:** When passing a reference data type, a reference (memory address) to the actual data is passed. In cases 3-4, objects are passed by reference when shared between variables.

### Shallow Copy

A shallow copy creates a new object or array, but the contents within it remain references to the original data. It copies the top-level structure without recursively copying nested objects or arrays.

The **spread operator (...)** can be used to create shallow copies of arrays and objects. It creates a new array or object and copies the enumerable properties or elements from the original. However, for nested objects, only references to the inner objects are copied, not the inner objects themselves.

**Example:**

```javascript
let person1 = {
  name: 'Adam',
  age: 25,
  address: {
    city: 'New York',
    country: 'USA'
  }
};

let person2 = {
  ...person1,  // Shallow copy top-level properties
  name: 'Steve',
  address: {
    ...person1.address,  // Shallow copy nested address object
    city: 'Delhi'
  }
};

console.log(person1);
console.log(person2);
``` 

```
Output:

{
  name: 'Adam',
  age: 25,
  address: { city: 'New York', country: 'USA' }
}
{ name: 'Steve', age: 25, address: { city: 'Delhi', country: 'USA' } }
```

### Deep Copy

A deep copy creates a completely independent copy of an object or array, including all nested objects or arrays. It ensures that changes made to the copied structure do not affect the original.

**Example:**

```javascript 
let person1 = {
  name: 'Adam',
  age: 25,
  address: {
    city: 'New York',
    country: 'USA'
  }
};

let person2 = JSON.parse(JSON.stringify(person1));

person2.name = 'Steve';
person2.address.city = 'Delhi';

console.log(person1);
console.log(person2);
```

``` 
Output:

{
  name: 'Adam',
  age: 25,
  address: { city: 'New York', country: 'USA' }
}
{ name: 'Steve', age: 25, address: { city: 'Delhi', country: 'USA' } }
```

---





