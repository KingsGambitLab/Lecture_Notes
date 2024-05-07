## Agenda

* JS refresher
* TypeOf Operator
* Objects and JSON
* JS Code Execution - Hoisting and Execution Context
* Hoisting
* Execution Context
* let, var, and const:
* Shadowing: legal and illegal


---


JavaScript is a dynamically typed, high-level programming language commonly used in web development. It employs the V8 engine, written in C++, for high-performance execution. Despite its name, JavaScript is distinct from Java. Its dynamic nature allows variables to change types during runtime, offering flexibility in coding.
## Datatypes in JS
Certainly, here's the information about JavaScript data types:

**Primitive Data Types:**
1. Number
2. String
3. Null
4. Undefined
5. Boolean

**New Primitive Types:**
1. BigInt
2. Symbol

**Non-Primitive Types (Reference Types):**
1. Object
2. Functions
3. Arrays

**New Non-Primitive Types:**
1. Map
2. Set
3. WeakMap
4. WeakSet

Sure, here are the code snippets with explanations and their respective outputs:

1. **Numbers:**
   ```javascript
   console.log(5 / 2); // Output: 2.5
   ```
   Explanation: JavaScript performs the division operation, and the result is `2.5`, which is a floating-point number.

2. **Strings:**
   ```javascript
   let age = 25;
   let str1 = 'I am ' + age + " years old ";
   console.log(str1); // Output: I am 25 years old

   let templateString = `I am ${age} years old`;
   console.log(templateString); // Output: I am 25 years old
   ```
   Explanation: In the first part, string concatenation is used to create `str1`. In the second part, a template string with variable interpolation is used to create `templateString`, both resulting in the same output.

3. **Null and Undefined:**
   ```javascript
   let myNull = null;
   let myUndefined;
   
   console.log(myNull); // Output: null
   console.log(myUndefined); // Output: undefined
   ```
   Explanation: `myNull` is explicitly set to `null`, while `myUndefined` is declared but not assigned a value, resulting in `undefined`.

4. **typeof Operator:**
   ```javascript
   var a = 10;
   console.log(typeof a); // Output: number
   a = "string";
   console.log(typeof a); // Output: string
   a = { "name": "Jasbir" };
   console.log(typeof a); // Output: object
   ```
   Explanation: The `typeof` operator is used to determine the data type of the variable `a`. It returns `"number"`, `"string"`, and `"object"` based on the assigned value.

5. **typeof null and Array Check:**
   ```javascript
   console.log(typeof null); // Output: object

   let arr = [1, 2, 3, 4];
   console.log(Array.isArray(arr)); // Output: true
   ```
   Explanation: `typeof null` returns `"object"` (historical quirk), and `Array.isArray()` accurately checks whether `arr` is an array and returns `true`.

These code snippets demonstrate JavaScript's handling of data types and the use of the `typeof` operator and `Array.isArray()` to determine types and check arrays.


---
 ## Non Primitive 
 ### function

Certainly, here's the code snippet related to functions and a brief explanation:

```javascript
// Function Definition
function fn(param1) {
    console.log("Hello world!", param1);
    return "Returned value";
}

// Function Call
let rVal = fn();

console.log("Return value:", rVal);
```

**Explanation:**
1. `function fn(param1)`: This is a function definition named `fn` that takes one parameter `param1`. Inside the function, it logs "Hello world!" along with the value of `param1` and then returns the string "Returned value."

2. `let rVal = fn();`: This line calls the `fn` function without passing any arguments. Since the function expects a parameter, `param1` inside the function will be `undefined`. It also captures the return value of the function in the variable `rVal`.

3. `console.log("Return value:", rVal);`: Finally, it logs the string "Return value:" along with the value of `rVal`, which is "Returned value."

Please note that calling `fn` without passing a value for `param1` will not result in an error, but `param1` will be `undefined` inside the function. If you want to pass a value when calling the function, you should do so like this: `fn("SomeValue");`.

### Objects and JSON

Here's the code snippet related to JavaScript objects and a brief explanation:

```javascript
// Object Definition
let cap = {
    name: "Steve",
    age: 34,
    isAvenger: true,
    key: "hello"
}

// Loop through Object Properties
for (let key in cap) {
    console.log(key, " ", cap[key], " ", cap.key);
}
```

**Explanation:**
1. An object in JavaScript is a collection of key-value pairs where the key can be a number or a string, and the value can be any valid JavaScript data type.

2. `cap` is an object that represents an entity, possibly a character named "Steve." It contains properties like `name`, `age`, `isAvenger`, and `key`.

3. The `for...in` loop is used to iterate through the properties of the `cap` object. Inside the loop, `key` represents each property name, and `cap[key]` retrieves the value associated with that property.

4. The `console.log` statement within the loop logs the `key`, the corresponding value accessed using `cap[key]`, and `cap.key`. However, note that `cap.key` accesses the property named "key" specifically, whereas `cap[key]` dynamically accesses the property corresponding to the current `key` in the loop.

5. In JavaScript, you can access object properties using the dot notation (e.g., `cap.name`) or square brackets (e.g., `cap['last Name']`).

6. JSON (JavaScript Object Notation) is a widely used data interchange format that is based on the structure of JavaScript objects. JSON uses a similar syntax for key-value pairs but is typically used for data communication between systems.

This code snippet demonstrates the creation of a JavaScript object, accessing its properties using a loop and dot notation, and the dynamic nature of accessing properties using square brackets.


---
## JS Code Execution

### Call Stack:
The call stack is a data structure used in JavaScript to keep track of the currently executing function(s). It follows the Last-In-First-Out (LIFO) principle, which means that the most recently called function is the first one to complete. As functions are called, they are added to the stack, and as they complete, they are removed from the stack.

### Execution Context:
An execution context is a conceptual container that holds all the information related to the execution of a piece of code. Each function call creates a new execution context, which includes information like the function's variables, parameters, references to outer scopes, the value of `this`, and other internal details.

### Global Area:
The global area, also known as the global scope, is where global variables and functions are defined. It's the outermost scope in JavaScript. Code outside of any function is executed in the global scope. The global area has its own execution context.

### Breakdown of Code Execution:

Certainly, here's the code snippet you provided along with an explanation of the code's execution and expected output:

```javascript
let a = 10;

function fn() {
    console.log("I am fn");

    function inner() {
        console.log("I am inner");
    }

    inner();
}

fn();
```

**Explanation:**
1. `let a = 10;`: This declares a variable `a` and assigns it the value `10`.

2. `function fn() { ... }`: This defines a function named `fn`. Inside `fn`, there's another function definition named `inner`.

3. `console.log("I am fn");`: When the `fn` function is called, it logs "I am fn" to the console.

4. `function inner() { ... }`: This defines an inner function named `inner` within the `fn` function.

5. `inner();`: Inside the `fn` function, `inner()` is called. This means the "I am inner" message will be logged to the console.

6. `fn();`: Finally, the `fn` function is called, which in turn calls `inner()`. So, both "I am fn" and "I am inner" messages will be logged to the console.

**Expected Output:**
```
I am fn
I am inner
```

This code demonstrates the concept of nested functions. The `fn` function contains an inner function `inner`, and when `fn` is called, it executes both its own code and the code within `inner`, resulting in both log messages being displayed in the console.


---
### JS Code Execution Quiz


Consider the following JavaScript code:

```javascript
function real() {
    console.log("I am real. Always run me");
}
function real() {
    console.log("No I am real one ");
}
real();
function real() {
    console.log("You both are wasted");
}
```

What will be the output when the code is executed?

- [ ] "No I am real one"  
- [x] "You both are wasted"  
- [ ] Error  

### Explanation
In JavaScript, when you declare multiple functions with the same name, only the last one defined will be retained due to hoisting. Therefore, in this code:

1. The first two function declarations are overwritten by the last one.
1. The real() function is called, and the last version of the function's body is executed, which logs "You both are wasted" to the console.
Hence, the correct answer is B) "You both are wasted".

---
## Execution of the code in JS


It seems like you're describing the code execution process in JavaScript and how execution contexts (EC) work. Here's a breakdown of your explanation:

1. **Code Execution Process:**
   - Code in JavaScript is executed within execution contexts (ECs).

2. **Global Code Execution (GEC):**
   - The global code is executed in the Global Execution Context (GEC). It's the top-level context where the entire script starts.

3. **Inside a Function (Function Execution Context):**
   - When a function is called, its code is executed within its own Function Execution Context.

4. **Execution Context Creation (EC Creation):**
   - During EC creation, JavaScript performs hoisting, which involves memory allocation for variables (initialized with `undefined`) and function declarations (fully allocated).
   - It also sets up the outer scope (if any) and determines the value of the `this` keyword.

5. **Global Object (Browser/Node.js):**
   - In a browser environment, the global object is `window`. In Node.js, it's `global`. These objects contain global variables and functions.

6. **Outer Scope:**
   - Each execution context has access to variables and functions in its outer (enclosing) scope.

7. **`this` Keyword:**
   - The `this` keyword is determined based on the context in which a function is executed. Its value varies depending on how the function is called.

8. **Execution of Code:**
   - After EC creation, the code within the context is executed. Variables and functions are accessible, and the program flows according to the code logic.

This explanation outlines the sequence of events when JavaScript code is executed, starting with EC creation, hoisting, and variable/function allocation, and then proceeding with the actual code execution. Understanding execution contexts is essential to grasp how JavaScript manages variable scope and function execution.

**Code Snippet 1:**

```javascript
var a=10;
real();
function real() { console.log("I am real. Always run me"); }
```

**Explanation:**
1. `var a=10;`: Declares a variable `a` and assigns it the value `10`.

2. `real();`: Calls the function `real()`.

3. `function real() { console.log("I am real. Always run me"); }`: Defines a function `real()` that logs a message to the console.

**Expected Output:**
```
I am real. Always run me
```

In this case, the function `real()` is defined before it is called, so it executes without any issues.

**Code Snippet 2:**

```javascript
let a = 10;
function fn() {
    console.log("a", a);
}
fn();
```

**Explanation:**
1. `let a = 10;`: Declares a variable `a` using `let` and assigns it the value `10`. This variable is in the outer/global scope.

2. `function fn() { console.log("a", a); }`: Defines a function `fn()` that logs the value of `a` to the console. It captures the value of `a` from its outer scope.

3. `fn();`: Calls the function `fn()`.

**Expected Output:**
```
a 10
```

In this case, `fn()` accesses the variable `a` from its outer scope (the global scope) and logs its value, which is `10`.

---
## Let, Var and Const

Certainly, let's break down the provided code snippet step by step and explain the output:

```javascript
let a = 10;
console.log("line number 2", a);

function fn() {
    let a = 20;
    console.log("line number 4", a);
    a++;
    console.log("line number 7", a);
    if (a) {
        let a = 30;
        a++;
        console.log("line number 11", a);
    }
    console.log("line number 13", a);
}

fn();
console.log("line number 16", a);
```

**Explanation:**

1. `let a = 10;`: Declares a variable `a` in the outer/global scope and assigns it the value `10`.

2. `console.log("line number 2", a);`: Logs the value of `a` in the global scope, which is `10`.

3. `function fn() { ... }`: Defines a function named `fn()`.

4. Inside the `fn` function:
   - `let a = 20;`: Declares a new variable `a` in the function scope (local to the function) and assigns it the value `20`.
   - `console.log("line number 4", a);`: Logs the value of the local `a`, which is `20`.
   - `a++;`: Increments the local `a` to `21`.
   - `console.log("line number 7", a);`: Logs the updated local `a`, which is `21`.

5. Inside the `if` block:
   - `let a = 30;`: Declares a new variable `a` with block scope (inside the `if` block) and assigns it the value `30`.
   - `a++;`: Increments the block-scoped `a` to `31`.
   - `console.log("line number 11", a);`: Logs the block-scoped `a`, which is `31`.

6. After the `if` block, but still within the function:
   - `console.log("line number 13", a);`: Logs the function-scoped `a`, which is `21`.

7. `fn();`: Calls the `fn()` function.

8. `console.log("line number 16", a);`: Logs the global `a` value, which is `10`.

**Expected Output:**
```
line number 2 10
line number 4 20
line number 7 21
line number 11 31
line number 13 21
line number 16 10
```
![](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_7f5b2092f952c2202a13120d67117094.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1695283757&Signature=iN9PTmJ8GTyZ0k4JH4%2BSWH%2F5Y4I%3D)

This code demonstrates variable scoping in JavaScript, including global, function, and block scope. Variables with the same name declared in different scopes do not interfere with each other. Block-scoped `let` variables are confined to the block in which they are declared, and the variable declared inside the `if` block doesn't affect the function-scoped or global `a`.


---

## Shadowing
**Variable Shadowing** occurs when a variable declared within a certain scope has the same name as a variable declared in an outer scope. This can lead to confusion and unexpected behavior, especially when accessing or modifying the variables. Let's explore legal and illegal cases of variable shadowing in more detail.

Let's go through the provided code snippets step by step and explain the output for each one:

**Code Snippet 1:**
```javascript
let fruits = "apple";
console.log(fruits); // apple

{
    console.log(fruits); // ReferenceError: Cannot access 'fruits' before initialization (Temporal Dead Zone - TDZ)
    let fruits; 
    console.log(fruits); // undefined
    fruits = "orange";
    {
        console.log(fruits); // orange
    }
    console.log(fruits); // orange
}

console.log(fruits); // apple
```

**Explanation:**
1. A variable `fruits` is declared and initialized with the value `"apple"` in the global scope.

2. Inside a block, a `console.log(fruits)` statement attempts to log the value of `fruits` before it's declared within that block. This results in a `ReferenceError` because of the Temporal Dead Zone (TDZ) for `let` variables.

3. A new `let` variable named `fruits` is declared within the block. It's initially in the TDZ, so `console.log(fruits)` logs `undefined`.

4. `fruits` is assigned the value `"orange"`.

5. Inside a nested block, `console.log(fruits)` logs `"orange"` because it refers to the block-scoped `fruits`.

6. Outside the innermost block, `console.log(fruits)` still logs `"orange"` because it refers to the most recent block-scoped `fruits`.

7. Finally, outside the block, `console.log(fruits)` logs the global `fruits` value, which is `"apple"`.

**Expected Output:**
```
apple
ReferenceError: Cannot access 'fruits' before initialization (Temporal Dead Zone - TDZ)
undefined
orange
orange
apple
```

**Code Snippet 2:**
```javascript
var fruits = "apple";
console.log("21", fruits); // apple

{ 
    let fruits;
    fruits = "orange";
    console.log("25", fruits); // orange
    {
        let fruits;
        console.log("28", fruits); // undefined
    }
    console.log(fruits); // orange
}
console.log(fruits); // apple
```

**Explanation:**
1. A variable `fruits` is declared and initialized with the value `"apple"` using `var` in the global scope.

2. Inside a block, a new `let` variable named `fruits` is declared, shadowing the global `fruits`. It is assigned the value `"orange"` within this block.

3. Inside a nested block, another `let` variable named `fruits` is declared. This variable shadows the outer block-scoped `fruits`. It is not initialized within this block, so it logs `undefined`.

4. Outside the innermost block, `console.log(fruits)` logs the block-scoped `fruits`, which is `"orange"`.

5. Finally, outside the block, `console.log(fruits)` logs the global `fruits`, which is `"apple"`.

**Expected Output:**
```
21 apple
25 orange
28 undefined
orange
apple
```

In this code, variable shadowing occurs when a variable with the same name is declared inside a nested block, shadowing variables from outer scopes. The behavior differs between `var` and `let` declarations, as demonstrated in the code snippets.

