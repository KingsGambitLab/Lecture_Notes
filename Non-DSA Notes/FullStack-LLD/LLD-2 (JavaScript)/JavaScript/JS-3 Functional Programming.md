

# Today's Content
- Callback functions
- Higher Order Functions
- Writing clean code with higher-order functions.
- Array Methods(Map, Filter, Reduce, etc.)
- Interview Questions



# Functional Programming
Following are the types of programming paradigms:
- Procedural Programming Paradigm(eg:- C, )
- Object Oriented Paradigms(eg:- Java, C++)
- Functional Programming Paradigm(eg:- javascript)

## Callback Functions
These are the functions that can be passed to another function as an argument. 

### Example
```javascript
function printName(cb){
    console.log('Shikhar')
    // calling received callback function
    cb()
}
function printLastName(){
    console.log('Singh')
}
function printAge(){
    console.log(24)
}
printName(printLastName) 
printName(printAge) 
```

**Output:**
Shikhar
Singh 
Shikhar
24

**Explanation:**
In`printName(printLastName)` statement, we are passing `printLastName` as a callback, and it is accepted by the `printName` as a `cb` argument. And when `cb()` is executed then the callback function is called.

**We can also pass multiple callback functions**
```javascript
function printName(cb1, cb2, cb3){
    console.log('Shikhar')
    cb1()
    cb2()
    cb3()
}
function printLastName(){
    console.log('Singh')
}
function printAge(){
    console.log(24)
}
function printAddress(){
    console.log('Delhi')
}
printName(printLastName, printAge, printAddress) 
```

**Output:**
Shikhar
Singh
24
Delhi

We can also pass the callback function within another callback function



# Coding question
We are given an array, which has the radius of different circles, we need to find the area, circumference and diameter for all the radiuses.

## Approach
We will simply create a different function for calculating area, circumference and diameter and in every function we will simply iterate over an array, and then store the calculated value in the result array, and return that array. 

## PseudoCode
```javascript
let myRadiusArray = [2, 3, 4, 5, 8]


function calculateArea(radiusArr){
    let result = []
    for(let i = 0 ; i < radiusArr.length ; i ++ ){
        result.push(3.14 * radiusArr[i] * radiusArr[i])
    }
    return result
}
let finalAreas = calculateArea(myRadiusArray)
console.log('This is area array => ', finalAreas)


function calculateCircumference(radiusArr){
    let result = []
    for(let i = 0 ; i < radiusArr.length ; i ++ ){
        result.push( 2 * Math.PI * radiusArr[i])
    }
    return result
}
let finalCircumferences = calculateCircumference(myRadiusArray)
console.log('This is Circumference array =>', finalCircumferences)



function calculateDiameter(radiusArr){
    let result = []
    for(let i = 0 ; i < radiusArr.length ; i ++ ){
        result.push(radiusArr[i] * 2)
    }
    return result
}
let finalDiameters = calculateDiameter(myRadiusArray)
console.log('This is Diameter array =>', finalDiameters)
```

**Output**
```plaintext
This is area array =>  [ 12.56, 28.259999999999998, 50.24, 78.5, 200.96 ]
This is Circumference array => [
  12.566370614359172,
  18.84955592153876,
  25.132741228718345,
  31.41592653589793,
  50.26548245743669
]
This is Diameter array => [ 1, 1.5, 2, 2.5, 4 ]
```

## Better Approach
Here we can see that every function has the same structure, and here we are violating the dry principle.
**Dry Principle** says that do not repeat yourself.
While writing a code just try to write simple code, so that you do not need to repeat the same structure again and again. Now we will try to generalize this code. Let us try to solve this problem using a higher-order function.


# Higher Order Function
Higher-order functions are those functions where the function is passed as an argument. This means that which callback function is passed as an argument.

## Example
Here `printName()` is the higher-order function
```javascript
function printName(cb){
    console.log('Shikhar')
    // calling received callback function
    cb()
}
function printLastName(){
    console.log('Singh')
}
printName(printLastName) 
 
```

# Solution of coding question Using Higher Order Function
Below is the javascript for the above coding question using a higher-order function.
```javascript
let myRadiusArray = [2, 3, 4, 5, 8]

function circleArea(radius){
    return Math.PI * radius * radius;
}
function circleCircumference(radius){
    return 2 * Math.PI * radius;
}
function circleDiameter(radius){
    return 2 * radius;
}
function calculateArea(radiusArr, logic){
    let result = []
    for(let i = 0 ; i < radiusArr.length ; i ++ ){
        result.push(logic(radiusArr[i]))
    }
    return result
}
let finalAreas = calculateArea(myRadiusArray, circleArea)
console.log('This is area array => ', finalAreas)
let finalCircumferences = calculateArea(myRadiusArray, circleCircumference)
console.log('This is Circumference array =>', finalCircumferences)
let finalDiameter = calculateArea(myRadiusArray,  circleDiameter)
console.log('This is Diameter array =>', finalDiameters)
```




#  Functional Programming
- Never manipulate or change your original array.




# map

Let us suppose we are given an array of numbers and we want the square of every number of an array. We can solve it by creating a new array for the result and iterating over the original array, to find the square of every element and add it to the result.

**Code**
```javascript
let arr = [1, 2, 3, 4, 5]
let SquareArr = []
for(let i = 0 ; i < arr.length ; i ++ ){
    SquareArr.push(arr[i] * arr[i])
}
console.log(SquareArr)
```

We can also write this code for finding squares within the function.
```javascript
let arr = [1, 2, 3, 4, 5]
function squareArrFn(arr){
    let SquareArr = []
    for(let i = 0 ; i < arr.length ; i ++ ){
        SquareArr.push(arr[i] * arr[i])
    }
    return SquareArr;
}
let squareArrFinal = squareArrFn(arr)
console.log(squareArrFinal)
```

For these questions, where we want to apply operations on every element of an array, then we can use the map. **,ap is a higher-order function which will not change the original array**. There is an unbuilt loop in a `map` which will take array elements one by one.

```javascript
let arr = [1, 2, 3, 4, 5]
let squaredValues = arr.map(function(num){
    return num * num;
})
console.log(squaredValues)
```

## Checking how the map works
Suppose we have an array `arr = [1, 2, 3, 4, 5]`, and we want a square of all the elements of an array. `map` first look at the array, then it will take callback function and traverse every element of an array and apply an operation on it. 


We can see that long code can be easily converted into small code using `map`.

**Using a map to find an area for the given radiuses in the form of an array**
```javascript
let radiusArr = [1, 2, 3, 4]
let areaArr = radiusArr.map(function(num){
    return Math.PI * num * num;
})
console.log(areaArr)
```



# Problem Statement
You are given a transaction array treat the transaction amount in rupees, and convert those amounts into dollars and conversion rate is also provided to us.

## Idea
We can use the `map` to apply similar operations to all the elements of an array. 

## PseudoCode
```javascript
const transactions = [1000, 3000, 4000, 2000, - 898, 3800, - 4500];
const inrtToUsd = 80;

let conversionToDollars = transactions.map(function(amount){
    return amount / inrtToUsd;
})
console.log(conversionToDollars)
```


# filter
`filter` is a higher-order function that will work based on a condition and will only have the values inside the result array for which the condition is satisfied. 
The `filter` will work like a `map`, but in the `map`, we will operate all the elements of an array. But in the `filter`, we will apply some conditions to the elements of an array.
The `filter` will work in boolean(true/false) values.


## Example
We are given an array of numbers that contains both even and odd numbers and we need an array which only contains the even numbers of the input array. 

**Solution:** If the remainder of the number on dividing it by 2 is zero(`element % 2 == 0`), then it is an even number. Here we can use the filter. Here we have created `evenArray` and used a filter on `myArr`, so the elements that satisfy the condition will only be added to the `evenArray`.

```javascript
let myArr = [1, 2, 5, 7, 8, 2, 6, 9, 13, 17]

let evenArray = myArr.filter(function(num){
    return num % 2 == 0;
})
console.log(evenArray)
```

**Output:**
[2, 8, 2, 6]





# Problem Statement
You are given a transaction array, and use a `filter` to find the positive transaction amounts


## Solution
We want only positive values, so positive values are always greater than 0, so we will apply this condition using the `filter`.

## PseudoCode
```javascript
const transactions = [1000, 3000, 4000, 2000, - 898, 3800, - 4500];

let positiveValue = transactions.filter(function(amount){
    return amount > 0;
})
console.log(positiveValue)
```

**Output:**
 [1000, 3000, 4000, 2000, 3800]


# Problem Statement
You are given an array of numbers and you need to calculate the sum of all the elements of an array.


## Solution
We will define a variable `sum`, initialize it with 0, iterate over the array and add elements one by one to `sum` the variable.


```javascript
let arr = [1, 2, 3, 4, 5]
let sum = 0
for(let  i = 0 ; i < arr.length ; i ++ ){
    sum = sum + arr[i]
}
console.log(sum)
```

**Output:**
15



# reduce
Just like above we have reduced all the array elements into one value i.e. sum, so basically `reduce` is used to reduce multiple elements into a single one.

## Example
Suppose we want to solve the above question using `reduce`, which means we want to find the sum of all elements of an array using `reduce`.

```javascript
let arr = [1, 2, 3, 4, 5]
let totalSum = arr.reduce(function(acc, num){
    acc = acc + num
    return acc
},0)
console.log(totalSum)
```

**Output:**
15


**Explanation:**
Here 0 written after `}` is the initialising value of `acc`, this means `acc` will be initiated with 0, and `acc` is used to store the sum and `num` is the current element of an array at every iteration and at every iteration, `num` is added to `acc`.