
### Introduction
Representational State Transfer (REST) constitutes an architectural paradigm that prescribes a set of guidelines for the construction of web services. A RESTful API provides a straightforward and adaptable means to interact with web services, devoid of any intricate processing requirements.

### Working
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/541/original/Screenshot_2023-09-20_184131.png?1695215654)

A client communicates with a server by issuing an HTTP request using a web URL, which can take the form of HTTP GET, POST, PUT, or DELETE requests. In return, the server provides a response in the form of a resource, which can take various formats such as HTML, XML, images, or JSON. Currently, JSON is the prevalent and widely used format in the realm of Web Services. 

#### Code
```javascript!
const express = require('express')
const fs = require('fs')
const data = fs.readFileSync('data.json')
console.log('This is JSON data -> ' + data)
const app = express()
app.listen(8080, ()=>{
    console.log('server started')
})
```

### Introduction
In HTTP there are five methods that are commonly used in a REST-based Architecture:

* GET
* POST 
* PUT
* PATCH
* DELETE

We'll revisit these later in this script. 

**Code:**
```javascript!
const express = require('express')
const app = express()
const fs = require('fs')
const data = JSON.parse(fs.readFileSync('data.json', "utf-8"))
const products = data.products
app.use(express.json())

console.log('This is JSON data -> ' + data)
//HTTP methods

app.get('/products', (req, res)=>{
    res.send(products)
})
//we can pass something in id, find that id in json and find it's properties
//get


app.listen(8080, ()=>{
    console.log('server started')
})
```

**Explanation:**

### GET() method
`GET()` is used to request data from a specified resource, such as a web page, an API endpoint, or any other resource accessible via a URL. It is primarily used for read-only operations, where we want to retrieve information without modifying the resource.

When a `GET()` request is made, it fetches data from the server without causing any changes to the resource. The data is then returned in the response, and the resource then remains unchanged on the server.

**Code:**
```javascript!
const express = require('express')
const app = express()
const fs = require('fs')
const data = JSON.parse(fs.readFileSync('data.json', "utf-8"))
const products = data.products
app.use(express.json())

console.log('This is JSON data -> ' + data)
//HTTP methods

app.get('/products', (req, res)=>{
    res.send(products)
})
app.get('/products/:id', (req, res) =>{
    const id = req.params.id
    console.log(id)
    const product = products.find(p=>p.id === id)
    console.log(product)
})
//we can pass something in id, find that id in json and find it's properties
//get


app.listen(8080, ()=>{
    console.log('server started')
})
```

**Output** 
```
undefined
```
**Explanation:**
**Now why did we get output as undefined?** 

Whenever you pass some thing to your id it comes in string format as opposed to when to pass it as `console.log(2)` it goes as arugment in number format 

Let's rectify this and see how it works

**Rectified Code:**
```javascript!
const express = require('express')
const app = express()
const fs = require('fs')
const data = JSON.parse(fs.readFileSync('data.json', "utf-8"))
const products = data.products
app.use(express.json())

console.log('This is JSON data -> ' + data)
//HTTP methods

app.get('/products', (req, res)=>{
    res.send(products)
})
app.get('/products/:id', (req, res) =>{
    const id = Number(req.params.id)
    console.log(id)
    const product = products.find(p=>p.id === id)
    console.log(product)
})
//we can pass something in id, find that id in json and find it's properties
//get


app.listen(8080, ()=>{
    console.log('server started')
})

```

**Output** 
```
Server Started
2
{
  id: 2,
  title: 'iPhoneX',
  Description: 'Sim Free Model A1981'
  price: 899,
  discount Percentage: 17.94
  rating: 4.44,
  stocks: 34,
  brand: 'Apple',
  category: 'smartphones',
  ...
}
```


**Note:** 
If you want to structure the output in JSON format then instead of `console.log(product)` you can do `res.json(product)`

### POST() method
`POST()` method is used to submit data to a specified resource, often to create a new resource on the server or to trigger a specific action that involves data submission.

When a `POST()` request is made, the data us sent to the server, and the server processes this data according to the resource's endpoint or the API's defined behavior. A new resource is created, if it already exists it updates it or triggers some other action. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/543/original/Screenshot_2023-09-20_184458.png?1695215705)

**Code:**
```javascript!
..same code

//post method
app.post('/products', (req, res)=>{
    console.log(req.body)
    products.push(req.body)
    res.status(201).json(req.body)
})

```

### PUT() method
The `PUT()` method is an HTTP request method used to update a resource or create a new resource at a specific URI (Uniform Resource Identifier)

**Code:**
```javascript!
app.put('/products/:id', (req, res)=>{
    const id = Number(req.params.id)
    const productIndex = products.findIndex(p=>p.id===id)
    products.splice(productIndex, 1, {...req.body, id:id})
    res.status(201).json()
})

//talk about splice in terms of array while explaining

```

### PATCH() method
`PATCH()` is used to request partial modifications or updates to an existing resource.

When a `PATCH()` request is made, it typically sends a patch document or set of instructions to the server, indicating how the resource should be modified. The server processes these instructions and applies the specified changes to the resource

**Code:**
```javascript!
app.patch('/products/:id', (req, res)=>{
    const id = Number(req.params.id)
    const productIndex = products.findIndex(p=>p.id===id)
    const product = products(productIndex)
    products.splice(productIndex, 1, {...product, ...req.body})
    res.status(201).json()
})
```

### DELETE() Method
`DELETE()` is used to request the removal or deletion of a resource located at a specific URI.

When a DELETE() request is made, it instructs the server to delete the resource identified by the URI. After a successful DELETE() operation, the resource no longer exists at that URI.

**Code:**
```javascript!
app.delete('/products/:id', (req, res)=>{
    const id = Number(req.params.id)
    const productIndex = products.findIndex(p=>p.id===id)
    const product = products(productIndex)
    products.splice(productIndex, 1)
    res.status(201).json(product)
})
```

### Introduction to MongoDB
MongoDB, an open-source document-oriented database, is purpose-built for efficiently handling extensive datasets. It falls within the NoSQL (Not only SQL) database category due to its departure from the conventional table-based storage and retrieval of data.

### MongoDB Architecture
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/544/original/Screenshot_2023-09-20_184157.png?1695215721)

Now we know that MongoDB serves as a database server where data is stored. In other words, MongoDB provides an environment where you can initiate a server and subsequently create multiple databases within it.

Data in MongoDB is organized into collections and documents. This establishes a hierarchical relationship between databases, collections, and documents, which can be explained as follows:

**NOTE:** MongoDB's server supports the concurrent operation of multiple databases.
#### Analogy
Let's understand the MongoDB architecture with the help of an analogy

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/545/original/Screenshot_2023-09-20_184204.png?1695215735)

Let's consider a Mongoose application connected to a database called "Scaler." Within this database, there are three collection (courses, instructors, and students), and each collection corresponds to a multiple documents each representing data stored in diverse formats.

#### Install MongoDB on your system
You can install MongoDB on your system by typing the following command in your command terminal
```
npm install mongodb 
```

#### Adaptability of MongoDB
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/546/original/Screenshot_2023-09-20_184211.png?1695215762)

Mongoose is specifically designed for Node.js, and so it's a natural choice for developers working with JavaScript on the server-side. This compatibility ensures seamless integration with Node.js applications.
#### Connect to MongoDB

**Code:**
```javascript!
const mongoose = require('mongoose')
const DB = "API"
mongoose.connect(DB, {
    useNewUrlParser : true,
    useUnifiedTopology : true,
}).then(()=>{
  console.log('connection sucessful')  
}).catch((err)=>{
  console.log(error)  
})
```

Run your file with:
```
npx nodemon test.js
```

**Explanation:**
Once Mongoose library is imported, a constant variable `DB` is defined with the value of API which represents the name or URL of the MongoDB database we want to connect to

A connection is then initiated with the MongoDB database using the `mongoose.connect` method and options object is passed with the  `useNewUrlParser` (enables the use of the new URL parser for MongoDB) and `useUnifiedTopology` (enables the use of the new Server Discovery and Monitoring engine in MongoDB) options set to `true`. These options configures the connection.

Once the connection is successful, a message is then logged on the console. If however an error is encountered during the connection to database process the error message is logged onto the console

In this way this code sets up a connection to a MongoDB database named "API" using Mongoose


