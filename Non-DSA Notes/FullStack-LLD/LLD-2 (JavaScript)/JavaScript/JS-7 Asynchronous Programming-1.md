# Asynchronous Programming 2

#### Definition

**Promise:** In JavaScript, a promise is an object representing the eventual completion (or failure) of an asynchronous operation. It provides a way to handle asynchronous code more cleanly and manage the results or errors that may occur when the operation completes. Promises have three states: pending, resolved (fulfilled), or rejected, and they allow you to attach callback functions to handle these different outcomes.

*States of Promise*

* Made a Promise => Pending State
* Promise can be fulfilled => Resolved
* Promise can not be fulfilled => Rejected State
* Setled => Promise Executed

#### Syntax

```javascript
let myPromise = new Promise(function(resolve, reject){

})

console.log(myPromise)
```

**Output:**

![](https://hackmd.io/_uploads/rJDlN6WAh.png)

**Explanation:** Wherever there is no resolve and no reject condition so it always lies under the pending condition.


#### Question

Create resolve and reject states of Promise 

#### Solution

**Reject State:**

```javascript
let myPromise = new Promise(function(resolve, reject){
    const a = 4
    const b = 5

    if(a == b) {
        resolve('Yes They are Equal')
    }
    else {
        reject('No They are not Equal')
    }
})

console.log(myPromise)

```

**Output:**

![](https://hackmd.io/_uploads/rJV47ZMR3.png)

**Explanation:** Whenever condition is not fulfilled or condition is not true it always lies under the rejected state

**Resolve States:**

```javascript
let myPromise = new Promise(function(resolve, reject){
    const a = 4
    const b = 4

    if(a == b) {
        resolve('Yes They are Equal')
    }
    else {
        reject('No They are not Equal')
    }
})

console.log(myPromise)

```

**Output:**

![](https://hackmd.io/_uploads/B1U1VbfR3.png)

**Explanation:** Whenever condition is fulfilled or condition is true it always lies under the resolved state.


#### Question

1. What is the use of then method and How to use then mehtod?

```javascript
let myPromise = new Promise(function(resolve, reject){
    const a = 4
    const b = 4

    if(a == b) {
        resolve('Yes They are Equal')
    }
    else {
        reject('No They are not Equal')
    }
})


// then method
myPromise.then(function(data){
    console.log(data)
})

```

**Output:**

![](https://hackmd.io/_uploads/B1YzDZfR3.png)

**Explanation:** Whenever a promise is resolved the data inside the resolve passes to the then method.

2. What is the use of catch method and How to use catch mehtod?

```javascript
let myPromise = new Promise(function(resolve, reject){
    const a = 4
    const b = 4

    if(a == b) {
        resolve('Yes They are Equal')
    }
    else {
        reject('No They are not Equal')
    }
})


// then method
myPromise.then(function(data){
    console.log(data)
})

```

**Output:**

![](https://hackmd.io/_uploads/H1iKeQ702.png)

**Explanation:** Whenever a promise is rejected the method will throw an error and to handle these errors we use a catch method.  

#### Question

**How to read a file using Promises?**

#### Solution

First of we will se how to read file using javascript only

```javascript
const fs = require('fs')

fs.readFile('f1.txt', cb)

function cb(err, data) {
    if(err) {
        console.log(err)
    }else {
        console.log("This is File 1 data -> " + data)
    }
}

```

**Output:**

![](https://hackmd.io/_uploads/BJueDXX03.png)


Now we will se how to read the file with using promises.

For Resolve State:  

```javascript
const fs = require('fs')

let promiseReadFile = fs.promises.readFile('f1.txt')

promiseReadFile.then(function(data) {
    console.log('This is file data -> ' + data)
})

promiseReadFile.catch(function(err) {
    console.log('This is Your Error -> ' + err)
})

```

**Output:**

![](https://hackmd.io/_uploads/HkHSommCn.png)

For Reject State:  

```javascript
const fs = require('fs')

let promiseReadFile = fs.promises.readFile('f5.txt')

promiseReadFile.then(function(data) {
    console.log('This is file data -> ' + data)
})

promiseReadFile.catch(function(err) {
    console.log('This is Your Error -> ' + err)
})

```

```f1.txt
I AM FILE 1 DATA

```

**Output:**

![](https://hackmd.io/_uploads/HJEe37Q0h.png)

**Explanation:** There is a in-built process of 'resolve' and 'reject' body which passes through the then and catch method. If the promise is fulfilled then it lies under the 'resolve' state using 'then' method. else it lies under the 'reject' state using 'catch' method.  

#### Question

**How to read all files using promises?**

```javascript
const fs = require('fs')

let promiseReadFile1 = fs.promises.readFile('f1.txt')
let promiseReadFile2 = fs.promises.readFile('f2.txt')
let promiseReadFile3 = fs.promises.readFile('f3.txt')

// For File 1
promiseReadFile1.then(function(data) {
    console.log('This is file 1 data -> ' + data)
})

promiseReadFile1.catch(function(err) {
    console.log('This is Your Error -> ' + err)
})

// For File 2
promiseReadFile2.then(function(data) {
    console.log('This is file 2 data -> ' + data)
})

promiseReadFile2.catch(function(err) {
    console.log('This is Your Error -> ' + err)
})

// For File 3
promiseReadFile3.then(function(data) {
    console.log('This is file 3 data -> ' + data)
})

promiseReadFile3.catch(function(err) {
    console.log('This is Your Error -> ' + err)
})

```

```f1.txt
I AM FILE 1 DATA

```

```f2.txt
I AM FILE 2 DATA

```

```f3.txt
I AM FILE 3 DATA

```

**Output:**

![](https://hackmd.io/_uploads/ByPjJNQ02.png)

**Explanation:** Since we are using promises so the order can be changed every time becuase it's following parallel operation and parallel operations can only happens when the code is asynchronous.  

**Optimized Solution**

For then method

```javascript
const fs = require('fs')

let f1p = fs.promises.readFile('f1.txt')
let f2p = fs.promises.readFile('f2.txt')
let f3p = fs.promises.readFile('f3.txt')

function readFileCallback(data) {
    console.log('This is the data -> ' + data)
}

f1p.then(readFileCallback)
f2p.then(readFileCallback)
f3p.then(readFileCallback)

```

**Output:**

![](https://hackmd.io/_uploads/HJ8D7EX0n.png)

For catch method

```javascript
const fs = require('fs')

let f1p = fs.promises.readFile('f1.txt')
let f2p = fs.promises.readFile('f2.txt')
let f3p = fs.promises.readFile('f3.txt')

function readFileCallback(data) {
    console.log('This is the data -> ' + data)
}

function handleError(err) {
    console.log('This is my error -> ' + err)
}

f1p.then(readFileCallback)
f2p.then(readFileCallback)
f3p.then(readFileCallback)

f1p.catch(handleError)
f2p.catch(handleError)
f3p.catch(handleError)

```

**Output:**

![](https://hackmd.io/_uploads/HJFA4EmRn.png)

**Explanation:** Since we are using promises so the order can be changed every time becuase it's following parallel operation and parallel operations can only happens when the code is asynchronous.  


#### Definition:
Asynchronous JavaScript is a programming paradigm that allows you to execute code concurrently without blocking the main execution thread.

* Call Stack
* Node APIs
* Callback Queue
* Event Loop

```javascript
const fs = require('fs')

console.log('Before')

let f1p = fs.promises.readFile('f1.txt')
let f2p = fs.promises.readFile('f2.txt')
let f3p = fs.promises.readFile('f3.txt')

function readFileCallback(data) {
    console.log('This is the data -> ' + data)
}

function handleError(err) {
    console.log('This is my error -> ' + err)
}

f1p.then(readFileCallback)
f2p.then(readFileCallback)
f3p.then(readFileCallback)

f1p.catch(handleError)
f2p.catch(handleError)
f3p.catch(handleError)

console.log('After')

```

**Output:**

![](https://hackmd.io/_uploads/HJGqwEm0h.png)

**Visualization**

![](https://hackmd.io/_uploads/SyaF_4QCh.png)


#### Example

```javascript
function logA() { console.log('A') }
function logB() { console.log('B') }
function logC() { console.log('C') }
function logD() { console.log('D') }

// Click the "RUN" button to learn how this works!
logA();
setTimeout(logB, 0);
Promise.resolve().then(logC);
logD();

```

**Output:**

![](https://hackmd.io/_uploads/r1wuFNm03.png)

**Explanation:** MicroTaks queue will be given the higher priority promisified code will run earlier than callback.

**Visulization:**

![](https://hackmd.io/_uploads/HyJBhVQ0h.gif)

**Promise Chaining:** Promise chaining in JavaScript is a technique for working with asynchronous code using Promises. It involves linking multiple asynchronous operations together, ensuring that one operation starts only after the previous one has completed successfully. This is typically achieved using the `.then()` method to handle the result of a Promise and return another Promise, allowing you to chain multiple operations together in a clean and sequential manner.  


![](https://hackmd.io/_uploads/Sy4elHQC2.png)

#### Example

```javascript
const fs = require('fs')

console.log('Before')

let f1p = fs.promises.readFile('f1.txt')

function cb1(data) {
    console.log('This is File 1 Data -> ' + data)

    let f2p = fs.promises.readFile('f2.txt')

    return f2p
}

function cb2(data) {
    console.log('This is File 2 Data -> ' + data)

    let f3p = fs.promises.readFile('f3.txt')

    return f3p
}

function cb3(data) {
    console.log('This is File 3 Data -> ' + data)
}

f1p.then(cb1).then(cb2).then(cb3)

console.log('After')

```

**Output:**

![](https://hackmd.io/_uploads/SJAXSrQ02.png)

**Explanation:** It's following serial operation and serial operations dosen't affect the order.  