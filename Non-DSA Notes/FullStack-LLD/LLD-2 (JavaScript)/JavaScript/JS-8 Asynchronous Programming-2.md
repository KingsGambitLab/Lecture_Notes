# Asynchronous Programming 3


#### Definition

**Async Function:** An async function is declared with the async keyword. It allows you to write asynchronous code in a more synchronous-like manner. Inside an async function, you can use the await keyword to pause execution until a Promise is resolved.  


**Await:** The await keyword is used inside an async function to wait for a Promise to resolve. It effectively pauses the execution of the function until the Promise resolves and returns its result.  

**Promises:** Async/await is often used with Promises. Promises are objects that represent the eventual completion or failure of an asynchronous operation. They are a way to manage asynchronous code and are frequently returned by functions like fetch.  


#### Question

Create resolve and reject states of Promise to place a order, then process the order and then generate a bill process.

#### Solution

![](https://hackmd.io/_uploads/S141UD7Rh.png)

**Step - 1:** Create a Promise method for placing/accepting the order.

1.1 Create resolve state if order is placed

```javascript
function placeOrder(drink) {
    return new Promise(function(resolve, reject) {
        if(drink === 'coffee') {
            resolve('Order for Coffee Placed.')
        }
        else {
            reject('Order can not be Placed.')
        }
    })
}

placeOrder('coffee').then(function(orderStatus) {
    console.log(orderStatus)
})

```

**Output:**

![](https://hackmd.io/_uploads/rygdYvmA3.png)

1.2 Create reject state if order is not placed

```javascript
function placeOrder(drink) {
    return new Promise(function(resolve, reject) {
        if(drink === 'coffee') {
            resolve('Order for Coffee Placed.')
        }
        else {
            reject('Order can not be Placed.')
        }
    })
}

placeOrder('tea').then(function(orderStatus) {
    console.log(orderStatus)
}).catch(function(error) {
    console.log(error)
})

```

**Output:**

![](https://hackmd.io/_uploads/ByDBcPQR2.png)

**Step - 2:** Create a Promise method for process the order.

```javascript
function placeOrder(drink) {
    return new Promise(function(resolve, reject) {
        if(drink === 'coffee') {
            resolve('Order for Coffee Placed.')
        }
        else {
            reject('Order can not be Placed.')
        }
    })
}

function processOrder(orderPlaced) {
    return new Promise(function(resolve) {
        resolve(`${orderPlaced} and Served.`)
    })
}

placeOrder('coffee').then(function(orderStatus) {
    console.log(orderStatus)
    return orderStatus
}).then(function(orderStatus) {
    let orderIsProcessed = processOrder(orderStatus)
    console.log(orderIsProcessed)
    return orderIsProcessed
}).then(function(orderIsProcessed) {
    console.log(orderIsProcessed)
})

```

**Output:**

![](https://hackmd.io/_uploads/ByszAwmC2.png)


**Step - 3:** Create a Promise method for generate the bill.

```javascript
function placeOrder(drink) {
    return new Promise(function(resolve, reject) {
        if(drink === 'coffee') {
            resolve('Order for Coffee Placed.')
        }
        else {
            reject('Order can not be Placed.')
        }
    })
}

function processOrder(orderPlaced) {
    return new Promise(function(resolve) {
        resolve(`${orderPlaced} and Served.`)
    })
}

function generateBill(processedOrder) {
    return new Promise(function(resolve) {
        resolve(`${processedOrder} and Bill Generated with 200 Rs.`)
    })
}

placeOrder('coffee').then(function(orderStatus) {
    console.log(orderStatus)
    return orderStatus
}).then(function(orderStatus) {
    let orderIsProcessed = processOrder(orderStatus)
    console.log(orderIsProcessed)
    return orderIsProcessed
}).then(function(orderIsProcessed) {
    console.log(orderIsProcessed)
    return orderIsProcessed
}).then(function(orderIsProcessed) {
    let BillGenerated = generateBill(orderIsProcessed)
    return BillGenerated
}).then(function(BillGenerated) {
    console.log(BillGenerated)
}).catch(function(err) {    
    console.log(err)
})
    
```
**Output:**

![](https://hackmd.io/_uploads/r1hZ-O70h.png)

**Explanation:** Firstly, we have create placeOrder function to place the order then if we pass 'coffee' then the promise is in resolve state. As soon as it is resolved we get the orderStatus and printing it. After that as soon as order is placed then we need to process the order this will be also in resolved state. After processing the order we need to generate the bill this should be also in resolved state, this process called the promise chaining method.


**Optimized Solution:** Using Async & Await

**Step - 1:** We will use async and await method to make code more clean and readable. to use async and await we need to create a function.

```javascript
function placeOrder(drink){
    return new Promise(function(resolve , reject){
        if(drink ==='coffee'){
            resolve('Order for Coffee Placed')
        }
        else{
            reject('Order cannot be Placed')
        }
    })
  }
  
  
  function processOrder(orderPlaced){
      return new Promise(function(resolve){
          resolve(`${orderPlaced} and Served`)
      })
  }
  
  function genreateBill(processedOrder){
      return new Promise(function(resolve){
          resolve(`${processedOrder} and Bill generated with 200Rs`)
      })
  }

// Async and Await 
// to use async await you need to create Functions

async function serveOrder(){
        let orderstatus = await placeOrder('coffee')
        console.log(orderstatus)
        let processedOrder = await processOrder(orderstatus)
        console.log(processedOrder)
        let generatedBill = await genreateBill(processedOrder)
        console.log(generatedBill)
}

serveOrder()

```

**Output:**

![](https://hackmd.io/_uploads/B10D6OQCh.png)

**Step - 2:** To Handle error we will use try and cacth method

```javascript
function placeOrder(drink){
    return new Promise(function(resolve , reject){
        if(drink ==='coffee'){
            resolve('Order for Coffee Placed')
        }
        else{
            reject('Order cannot be Placed')
        }
    })
  }
  
  
  function processOrder(orderPlaced){
      return new Promise(function(resolve){
          resolve(`${orderPlaced} and Served`)
      })
  }
  
  function genreateBill(processedOrder){
      return new Promise(function(resolve){
          resolve(`${processedOrder} and Bill generated with 200Rs`)
      })
  }

// Async and Await 
// to use async await you need to create Functions

async function serveOrder(){
    try {
        let orderstatus = await placeOrder('tea')
        console.log(orderstatus)
        let processedOrder = await processOrder(orderstatus)
        console.log(processedOrder)
        let generatedBill = await genreateBill(processedOrder)
        console.log(generatedBill)
    } catch (error) {
        console.log(error)
    }
}

serveOrder()

```

**Output:**

![](https://hackmd.io/_uploads/ry_bRO7A2.png)


#### Question

Create the Promise.all function in JavaScript that returns a single promise and the resolved value contains an array of values.  

#### Solution 

![](https://hackmd.io/_uploads/rJI-MKmR2.png)


```javascript
const p1 = Promise.resolve("pi");  // pi
//returns a promise of resolved value "pi"
const p2 = 3.14;  // 3.14
const p3 = new Promise((resolve, reject) => { 
    //promise method to resolve or reject values
    resolve("Maths"); 
    //p3 contains a promise of resolving "maths" value 
});

let returned_promise = Promise.all([p1 ,p2 ,p3]); 
//checking fulfillment or rejection of any of the promises: p1,p2 and p3 passed as iterable in the function 

returned_promise.then((array)=>{ 
    //returned_promise will contain final returned value of Promise.all() method
    console.log(array); 
    //checking and printing the value returned as promised by Promise.all() method in JS
})

```

**Output:**

![](https://hackmd.io/_uploads/B1GglYX03.png)

**Explanation:** As we can see, the `Promise.all` in JavaScript has returned a single promise and the resolved value contains an array of values.

#### Example 

```javascript
let a = 12

if(a){
    console.log('This is a truthy Value')
}else{
    console.log('This is a Falsy Value')
}

```

**Output:**
![](https://hackmd.io/_uploads/r1mMQYm02.png)


These are the Falsy Values

* undefined
* null
* `0`
* `''`
* NaN
* false

#### Example 1

```javascript
let a = undefined

if(a){
    console.log('This is a truthy Value')
}else{
    console.log('This is a Falsy Value')
}

```

**Output:**

![](https://hackmd.io/_uploads/Hy4tNYX0n.png)

#### Example 2

```javascript
let a = null

if(a){
    console.log('This is a truthy Value')
}else{
    console.log('This is a Falsy Value')
}

```

**Output:**

![](https://hackmd.io/_uploads/Hy4tNYX0n.png)

#### Example 3

```javascript
let a = 0

if(a){
    console.log('This is a truthy Value')
}else{
    console.log('This is a Falsy Value')
}

```

**Output:**

![](https://hackmd.io/_uploads/Hy4tNYX0n.png)

#### Example 4

```javascript
let a = ''

if(a){
    console.log('This is a truthy Value')
}else{
    console.log('This is a Falsy Value')
}

```

**Output:**

![](https://hackmd.io/_uploads/Hy4tNYX0n.png)

#### Example 5

```javascript
let a = NaN

if(a){
    console.log('This is a truthy Value')
}else{
    console.log('This is a Falsy Value')
}

```

**Output:**

![](https://hackmd.io/_uploads/Hy4tNYX0n.png)

#### Example 6

```javascript
let a = false

if(a){
    console.log('This is a truthy Value')
}else{
    console.log('This is a Falsy Value')
}

```

**Output:**

![](https://hackmd.io/_uploads/Hy4tNYX0n.png)

Everything other than this will be  truthy value

#### Example 7

```javascript
let a = 'Scaler'

if(a){
    console.log('This is a truthy Value')
}else{
    console.log('This is a Falsy Value')
}

```

**Output:**

![](https://hackmd.io/_uploads/HyZpBKQ0n.png)

---
title: Diffrence Between `==` and `===`
description:
duration: 900
card_type: cue_card
---

#### Question

What is the Diffrence Between `==` and `===`

#### Example 1

```javascript
let a = 2
let b = '2'

console.log(a==b) // loose checking //
// here in this case only the values are getting checked

```

**Output:**

![](https://hackmd.io/_uploads/SyQd_FQAh.png)

#### Example 2

```javascript
let a = 2
let b = '2'

console.log(a===b) // strict Checking
// Here in this case the value as well as the type is getting checked

```

**Output:**

![](https://hackmd.io/_uploads/ByDgFF7An.png)



#### Question

How to check typeof Operator

#### Example 1

```javascript
let c = 'Scaler'

console.log(typeof c)

```

**Output:**

![](https://hackmd.io/_uploads/Hyl8cFmRh.png)

#### Example 2

```javascript
let c = {name : 'Scaler'} 

console.log(typeof c)

```

**Output:**

![](https://hackmd.io/_uploads/Byv6FK70n.png)


#### Example

```javascript
let c = [1, 2, 3]

// Array.isArray - Boolean Method

let checkArray = Array.isArray(c)

console.log(checkArray)

```

**Output:**

![](https://hackmd.io/_uploads/rJ1ioY702.png)


#### Example

```javascript
let d = 1/0

console.log(d)

```

**Output:**

![](https://hackmd.io/_uploads/By3jntQRn.png)


#### Example

```javascript
let d = 2 + ''

console.log(d)

```

**Output:**

![](https://hackmd.io/_uploads/ByyraK7R2.png)


#### Example 1

```javascript
let sqroot = Math.sqrt(-3)
console.log(sqroot)

```

**Output:**

![](https://hackmd.io/_uploads/HJDbRtmAh.png)

#### Example 2

```javascript
let out = 'Scaler'*10
console.log(out)

```

**Output:**

![](https://hackmd.io/_uploads/r1U9CYmCn.png)


#### Example 1

```javascript
let out = 'Scaler'*10

let checkIsNan = isNaN(out)

console.log(checkIsNan)

```

**Output:**

![](https://hackmd.io/_uploads/H1fKy5mAn.png)

#### Example 2

```javascript
let a = 2

let checkIsNan = isNaN(a)

console.log(checkIsNan)

```

**Output:**

![](https://hackmd.io/_uploads/SyQWl9XR3.png)



#### Example 1

```javascript
let sqroot = Math.sqrt(-3)

console.log(typeof sqroot)

```

**Output:**

![](https://hackmd.io/_uploads/SkcwZ9mR3.png)


```javascript
console.log(isNaN(null))

console.log(isNaN(undefined))

```

**Output:**

![](https://hackmd.io/_uploads/rJqnG5QCh.png)
