




# Agenda
- Arrays in depth
- Objects in depth
- Functions in depth
- Strings in depth
- More differences between let, var and const.


# Arrays 
The array is a data structure to store multiple values of multiple data types. The elements are stored in an indexed manner.

## Accessing array element
Any array element can be accessed by an index. If we want to access the fifth element of an array named `arr`, then we have to simply write `arr[4]`, as the array works on 0-indexing.

```javascript=
let arr = [1, 'Scaler', true, undefined, null, [1, 2, 3]]
console.log(arr)
// access an element with index from an array
console.log(arr[4]) // print null

let d=arr[5]
console.log(d) // print [1, 2, 3]
console.log(d[0]) // print 1

```

## Changing an array element
We can change the value of any element by its index, if we want to change the value of the fourth element of an array named `arr`, then we need to simply write `arr[3]='new value'`

```javascript=
let arr = [1, 'Scaler', true, undefined, null, [1, 2, 3]]
console.log(arr) // print [1, 'Scaler', true, undefined, null, [1, 2, 3]]
// change an array element to a different value
arr[3] = 'Mrinal'
arr[4] = 700
console.log(arr) //print [1, 'Scaler', true, 'Mrinal', 700, [1, 2, 3]]

```

## Length of an array
Gives the length of the array, length means the total number of elements in an array.

```javascript=
let arr = [1, 'Scaler', true, undefined, null, [1, 2, 3]]
console.log(arr.length) // print 6 as there are a total of 6 elements in an array.

```

## Array methods
**Push Method:**
Inserting an element into an array at the end
```javascript=
let cars = ['swift', 'BMW', 'Audi']
console.log(cars) // print ['swift', 'BMW', 'Audi']
cars.push('Urus')
console.log(cars) // print ['swift', 'BMW', 'Audi', 'Urus']
```

**Pop Method:**
Delete the element from the end of the array
```javascript=
let cars = ['swift', 'BMW', 'Audi', 'Urus']
console.log(cars) // print ['swift', 'BMW', 'Audi', 'Urus']
cars.pop()
console.log(cars) // print ['swift', 'BMW', 'Audi']
```
Popped elements can also be stored in another variable.
```javascript=
let cars = ['swift', 'BMW', 'Audi', 'Urus']
var removedElement = cars.pop()
console.log(removedElement) // print Urus
```

**Unshift Method**
Insert an element at the start of an array(0th index).

```javascript=
let cars = ['swift', 'BMW', 'Audi']
console.log(cars) // print ['swift', 'BMW', 'Audi']
cars.unshift('Urus')
console.log(cars) // print ['Urus', 'Swift', 'BMW', 'Audi']
```

**Shift Method**
Remove the 0th index element of an array.
```javascript=
let cars = ['swift', 'BMW', 'Audi', 'Urus']
console.log(cars) // print ['swift', 'BMW', 'Audi', 'Urus']
cars.shift()
console.log(cars) // print ['BMW', 'Audi', 'Urus']
```

Shifted elements can also be stored in another variable.
```javascript=
let cars = ['swift', 'BMW', 'Audi', 'Urus']
var removedElement = cars.shift()
console.log(removedElement) // print swift
```


# Loops
Loops are used with arrays when we want to perform similar operations on all the elements of an array.

## Example
**Example 1:** To print the square of every element of an array.
```javascript=
let arr = [1, 2, 3, 4, 5]
for(let i=0;i<arr.length;i++){
    console.log(arr[i]*arr[i])
}
// print 1 4 9 16 25
```

**Example 2:** Storing the square of every element of an array in another array.
```javascript=
let arr = [1, 2, 3, 4, 5]
let squareArr = []
for(let i=0;i<arr.length;i++){
    squareArr.push(arr[i]*arr[i])
}
console.log(squareArr) // print [1, 4, 9, 16, 25]
```




# Functions
The function is an abstract body and inside that body particular logic is written and that function expects some values which are known as parameters of the function. At the time of invoking the function we need to pass those values as an argument.

**Example of simple function**
```javascript=
// function accepting parameters
function ServeBeverage(drink, quantity){
    console.log('I want '+ quantity + " " + drink)
}
// calling function by passing arguments
serveBeverage('coffee',4) // print I want 4 coffee
```



## Ways of defining function in javascript
In JavaScript, we have multiple ways of defining functions.
### Traditional way of writing function
We can define functions in a way similar used in another programming language for function definition.
```javascript=

function sayHi(){
    console.log('mrinal says hi')
}
// calling function
sayHi()
```

### Function as Expressions(First class citizens)
We can write functions inside the variable in JavaScript. That's why it is known as first-class citizens.
**Example**
```javascript=
// Function as Expressions
let sayHi=function(){
    console.log('mrinal says hi')
}
// calling function
sayHi()
```

### Arrow function
We can write the arrow function even without using the function keyword.
**Example**
```javascript=
// Arrow function
let sayBye=()=>{
    console.log('mrinal says bye')
}
// calling function
sayBye()
```



# Execution context in javascript
How the javascript code gets executed.
```javascript=
var a = 2
var b = 3
function add(num1, num2){
    var ans = num1+num2
    return ans;
}
var addition = add(4, 5)
console.log(addition) // print 9
add(addition, 4) 
let add1 = addition(a, b)
let add2 = addition(5, 6)
console.log(add1) // print 5
console.log(add2) // print 11
```

Javascript code executes two phases:
1. **Memory Allocation:** Every particular variable is assigned with undefined value initially. Initially, no value is assigned to the variable, only memory is allocated. And every function will get its whole body in this phase.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/084/original/upload_85139e0f5170f5e8eece1dd1782b44b7.png?1695318758)

2. **Code Execution:** Code will get executed in this phase. Now the values of variables are assigned. When the function is called and it starts executing then another memory allocation, the code block is created. For every function calling, another execution context will be created. And execution context of the whole program is known as the global execution context.
Variables declared inside the function are written inside the execution context of that particular function.


Execution context is created when the function is called and the answer is stored in the add1 variable.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/085/original/upload_1a31012a1e876a8f7c95aa73d0eef002.png?1695318823)

After completing the function execution, a particular function execution context returns the value. And we do not need that function execution context further.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/086/original/upload_d3e7d682244f9386192f25604345466b.png?1695318849)


Now again execution context is created when the add() function is called again and the return value of the function is stored in add2.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/087/original/upload_5d5e478c9528b7fe00cc0b799debdc76.png?1695318906)
After the completion of function execution, there is no requirement for that function execution context.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/088/original/upload_80a8e7c9979b2c4b7e9a6129459cfeca.png?1695318933)

Now the execution of the program is completed, now global function execution context is also not required further.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/089/original/upload_e27ec9b99f9a4fc64569b634d07f2a30.png?1695318988)


**Execution context for the below code**

```javascript=
var n = 3
function square(num){
    var ans = num*num
    return ans
}
let square1 = square(n)
```

- Firstly global execution context will be created.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/090/original/upload_4af9552ee646a0fe31bae98443b75adf.png?1695319026)

- Then the value to the n will be assigned.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/091/original/upload_bdeb77ccd5eed38c0a9afe636098474e.png?1695319049)

- Now execution context is created for the square method as it is called.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/092/original/upload_e409b43de48b1647ec498a5bb8cd358c.png?1695319076)
- Variables declared inside the function are initialized by undefined values in the function execution context.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/093/original/upload_4ee9ea62766996fd53d0645bd52785b3.png?1695319103)

- Now the value will be assigned to the variables of the function execution context.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/094/original/upload_30b10d1997acbd7260a784b6f639b4c2.png?1695319173)

- After that function execution context returns value to the global execution context and the function execution context is not required further.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/095/original/upload_2c00f2a7212c3e93e02fa480dcf396c1.png?1695319197)

- Now the program is executed completely so we do not need global execution context further.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/096/original/upload_fe64e69af8a31efb89e43340574b7b9d.png?1695319220)



# More differences between let, var and const.

```javascript=
var a = 4

function printName(){
    console.log('my name is mrinal')
}
console.log(a)
printName()
```

**Output**
```
4
my name is mrinal
```

```javascript=
console.log(a)
printName()
var a = 4

function printName(){
    console.log('my name is mrinal')
}

```

**Output**
```plaintext
undefined
my name is mrinal
```

**Explanation**
First is the memory allocation phase of the program, and initially all the variables are initialized with undefined values before program execution. In the memory allocation phase, a = undefined and fn printName() will be created. After that program execution phase will start, in which first the value of a printed i.e. undefined after the function is called, function execution context will be created and then the value is assigned to the variable.

```javascript=
console.log(a)
printName()
var a = 4

function printName(){
    console.log('my name is mrinal')
}
let printAge = function(){
    console.log(24)
}
printAge()
```

**Output**
```plaintext
undefined
my name is mrinal
24
```


```javascript=
console.log(a)
printName()
printAge()
var a = 4

function printName(){
    console.log('my name is mrinal')
}
let printAge = function(){
    console.log(24)
}

```

But now this program will give an error that printAge is not defined. We are getting this error as we are working with function as expression and printAge does not have a function during initialization. It has an undefined value during initialization.

**let**
```javascript=
console.log(a)
printName()
let a = 4

function printName(){
    console.log('my name is mrinal')
}
let printAge = function(){
    console.log(24)
}
printAge()
```

This program will give an error at line console.log(a) that `cannot access 'a' before initialization`. This is because let will first initialise your variable with temporal dead zone. Whenever a variable is created with the `let`, then that variable can not be accessed before initialisation means until the code execution phase is not started. Before code execution, it is in a temporal dead zone.



# Temporal dead zone(TDZ)
When you declare a variable with let or const, then these variables can not be accessible before their initialization and at this moment they will be in a temporal dead zone.

||var|let|const|
|:-:|:-:|:-:|:-:|
|TDZ|&cross;|&check;|&check;|




# Objects
Objects are basically in which data is stored in the form of key-value pairs. 
## Example
```javascript=
let person ={
    name: 'Mrinal',
    age: 24,
    phone: 1234567
}
console.log(person)
// dot notation
console.log(person.age)
// bracket notation
console.log(person['phone'])
```

We can store any kind of value in an object. We can also write a function inside the object using `:`. Another object can also be created within the object.

```javascript=
let captainAmerica ={
    name : 'Steve Rogers',
    age : 102,
    // Array
    allies : ['Tony', 'bruce', 'bucky']
    // function inside an object
    sayHi : function(){
        console.log('Captain says hi')
    }
    // nested object
    address :{
        country : 'USA',
        city : {
            name : 'Brokkly',
            pincode : 12345
        }
    }
    isAvenger : true
}
// accessing age from captainAmerica object
console.log(captainAmerica.age)  // print 102
// accessing element of array allies from captainAmerica object
console.log(captainAmerica.allies[1]) // print bruce
// accessing element from the nested object
console.log(captainAmerica.address.city) // print complete city object
console.log(captainAmerica.address.city.pincode) // print 12345

// changing some values of an object
captainAmerica.isAvenger=false

// adding new key-value in object
captainAmerica.movies=['End Game', 'Age of Ultorn', 'Civil War']
//The above statement will create a key with movies if it is not available in the object otherwise it will update the previous value of movies.


// calling function defined within an object
captainAmerica.sayHi()


//Deleting key from an object

delete captainAmerica.age
```