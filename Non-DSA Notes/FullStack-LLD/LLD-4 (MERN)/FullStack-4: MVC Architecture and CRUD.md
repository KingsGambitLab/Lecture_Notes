

## Today's Content
- MVC Architecture
- CRUD operation using MongoDB and Mongoose


# MVC Architecture Overview

Imagine we're using the following analogy to explain the MVC architecture:

"A customer (view) is ordering a pizza, so he makes a request to the waiter (controller). The waiter takes the request and goes to the chef (model) in the kitchen and fetches the items from the kitchen (database) to make the pizza. Once it's ready, the chef serves the pizza back to the waiter, who then serves it to the customer."

Now, let's break down the MVC architecture within this analogy.


**Model:**
- Represents the data and logic of the application.
- In the pizza example, the chef in the kitchen is the model.
- Manages and fetches data (ingredients) and performs operations (cooking) on it.
- The model is unaware of the user interface.

**View:**
- Represents the user interface or what the user interacts with.
- In the pizza example, the customer is the view.
- Displays information (menu options) to the user and captures user input (order).
- Passes user input to the controller.

**Controller:**
- Acts as an intermediary between the model and the view.
- In the pizza example, the waiter is the controller.
- Receives and processes user requests (orders) from the view.
- Interacts with the model (chef) to fetch data (ingredients) and perform actions (cooking).
- Sends updates back to the view to display the result (serving the pizza).


**The following image gives an idea about MVC architecture**:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/052/060/original/upload_24f17def1d1ac7e73c3a74069cf7b9f8.png?1696316119)


In essence, MVC separates the application into three distinct components, making it easier to manage and maintain. The view handles the presentation and user interaction, the model manages the data and logic, and the controller orchestrates the communication between the view and the model. This separation of concerns enhances code organization and promotes scalability and maintainability in software development.


# Question
What is the primary responsibility of the Model component in the MVC architecture?

# Choices
- [ ] Handles user interface interactions.
- [ ] Manages routing and URL handling.
- [x] Represents the data and logic of the application.
- [ ] Interacts with the user and captures input.





# Benifits of MVC architecture


- **Separation of Concerns:**
  - Divides the application into Model, View, and Controller for clear separation of responsibilities.
- **Modular Development:**
  - Supports development and maintenance of separate, reusable modules for each component.
- **Improved Code Reusability:**
  - Allows reuse of Models, Views, and Controllers in different parts of the application or other projects.
- **Enhanced Maintainability:**
  - Changes in one component have minimal impact on the others, simplifying maintenance and debugging.
- **Scalability:**
  - Facilitates parallel development and the addition of new features without major rework.
- **User Interface Flexibility:**
  - Adapts to various user interfaces while keeping the core logic intact.
- **Efficient Testing and Debugging:**
  - Enables isolated unit testing for each component, easing issue identification and resolution.
- **Parallel Development:**
  - Supports multiple developers or teams working on different components simultaneously.
- **Support for Multiple Views:**
  - Utilizes the same Model and Controller with multiple Views for diverse user interfaces.
- **Long-Term Maintainability:**
  - Promotes organized and understandable code, reducing technical debt over time.






# Question
Which of the following is NOT a benefit of using the MVC architecture in software development?

# Choices
- [ ] Enhanced Maintainability
- [ ] Efficient Testing and Debugging
- [ ] Improved Code Reusability
- [x] Tight Coupling between Components



# Mvc Implementation in Project 


### index.js Usage

- **Responsibility**: The `index.js` file serves as the entry point of your application, handling server setup and routing initialization.
- **Server Setup**: It initializes an Express server using the `express` library.
- **Routing Configuration**: The `productRouter` is imported from `productRoutes.js` and configured to handle incoming requests.
- **Middleware**: Express middleware, such as `express.json()`, is applied to handle JSON request bodies.
- **Server Start**: The server is started on port 8080, listening for incoming requests.

```javascript
// index.js

const express = require('express')
const app = express()

// Import the productRouter for handling routes
const productRouter = require('./routes/productsRoutes')

// Use the productRouter middleware to handle routes
app.use('/', productRouter.router)

// Apply middleware to handle JSON request bodies
app.use(express.json())

// Start the server, listening on port 8080
app.listen(8080, () => {
    console.log('Server Started')
})
```

**In this section of code**:

- `express` is used to create and configure the server.
- The `productRouter` is used to define and manage the routes, connecting them to the Controller component.
- Express middleware is applied, such as `express.json()`, which parses incoming JSON request bodies.
- The server is started and listens on port 8080, making your application accessible to clients.

This file essentially serves as the glue that ties together the MVC components, initializing the server, configuring routes, and ensuring proper request handling and response generation.


### Model Implementation

- **Responsibility**:<br> Manages data, performs database interactions, and defines data structure.
- **Data Definition**:<br> The Model defines the structure of core entities (courses) in your application.
- **Database Interaction**:<br> It handles database connections and operations using Mongoose.
- **Entity Schema**:<br> The model includes a schema definition for the 'Course' entity, specifying fields like name, creator, published date, isPublished, and rating.
- **Entity Model**:<br> The 'Course' model is created using Mongoose to represent the data structure.

**Code**:

```javascript
// myDb.js
// ... (previous code)

// Schema definition for the 'Course' model
const courseSchema = new mongoose.Schema({
    name: String,
    creator: String,
    publishedDate: { type: Date, default: Date.now },
    isPublished: Boolean,
    rating: Number
})

// Model creation for the 'Course' entity
const Course = mongoose.model('Course', courseSchema)

// Functions for creating and interacting with 'Course' documents
// (createCourse, getCourse, updateCourse, deleteCourse)
```


#### Code Explanation:

- `mongoose.connect(DB, { useNewUrlParser: true, useUnifiedTopology: true })`: Establishes a connection to the database using the provided MongoDB connection string.
- `courseSchema`: Defines the structure of the 'Course' entity with its fields and data types.
- `Course = mongoose.model('Course', courseSchema)`: Creates a model named 'Course' based on the defined schema, allowing you to interact with the database using this model.
- Functions like `createCourse`, `getCourse`, `updateCourse`, and `deleteCourse` are used for various operations on 'Course' documents in the database.

### Controller Implementation

- **Responsibility**:<br> Acts as an intermediary between the Model and the View (routes), handling incoming requests and preparing responses.
- **Data Processing**:<br> Controller functions process various actions such as retrieving data, creating, updating, and deleting data.
- **Data Interaction**:<br> These functions interact with the Model to perform data operations.
- **Business Logic**:<br> The Controller contains business logic for processing and validating data.
- **Response Preparation**:<br> It prepares and sends responses back to the View (routes) based on the request handling.

**Code**:

```javascript
// productControllers.js

const fs = require('fs')

// Data retrieval from JSON file
const data = JSON.parse(fs.readFileSync('data.json', "utf-8"))
const products = data.products

// Controller functions for handling different actions
// (getAllProducts, getProduct, createProduct, replaceProduct, updateProduct, deleteProduct)
```

#### Code Explanation:

- The Controller functions, such as `getAllProducts`, `getProduct`, `createProduct`, etc., are responsible for handling specific HTTP requests related to products.
- These functions perform data processing, including reading from a JSON file and manipulating product data.
- Business logic, such as finding products by ID or updating product information, is contained within these functions.
- Responses are prepared and sent back to the View (routes) with appropriate HTTP status codes and data.


# Question
In a typical MVC implementation, what is the role of the Controller component?

# Choices
- [ ] Manages the data and logic of the application.
- [ ] Represents the user interface and displays information.
- [ ] Handles routing and URL configuration.
- [x] Acts as an intermediary between the Model and the View, processing requests and preparing responses.




### View (Routes) Implementation

- **Responsibility**:<br> In this project, the View component is represented by routes, which define endpoints for user interactions.
- **Request Handling**:<br> Routes receive incoming HTTP requests from users.
- **Controller Interaction**:<br> They invoke Controller functions to process requests and provide data.
- **Response Generation**:<br> Based on the Controller's response, routes generate and send appropriate HTTP responses.
- **User Interaction**:<br> Routes facilitate user interactions with the application through defined endpoints.

**Code**:

```javascript
// productRoutes.js

const express = require('express')
const productController = require('../controllers/productControllers')

const router = express.Router()

// Routes for different user interactions
router.get('/products', productController.getAllProducts)
router.get('/products/:id', productController.getProduct)
router.post('/products', productController.createProduct)
router.put('/products/:id', productController.replaceProduct)
router.patch('/products/:id', productController.updateProduct)
router.delete('/products/:id', productController.deleteProduct)
```

#### Code Explanation:

- Express routes, defined in `productRoutes.js`, specify various endpoints for user interactions related to products.
- These routes handle HTTP requests, such as GET, POST, PUT, PATCH, and DELETE, for product-related actions.
- The routes interact with the Controller component by invoking the corresponding Controller functions, passing request data as needed.
- Responses generated by the Controller are returned to the client through these routes.

In summary, this project demonstrates the separation of concerns through the Model-View-Controller pattern, with distinct roles for the Model (data management), Controller (business logic), and View (routes for user interaction). The bullet-pointed code explanations provide a detailed breakdown of each component's responsibilities and how they interact within your application.
