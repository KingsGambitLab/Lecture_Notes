

## Agenda
**Topics to cover in Express:**


We will try to cover most of these topics in today's sessions and the remaining in the next.
* What is express 
* How to use express with node
* Http methods-get,post,put,delete, patch
* Postman-to test your api endpoints
* Middlewares 
It is going to be a bit challenging, advanced, but very interesting session covering topics that are asked very frequently in interviews.

So let's start.


## Express Module
In Node.js, the Express module is a popular framework for building web applications and APIs. It simplifies the process of handling HTTP requests and responses and provides a structured way to create routes and middleware. Let's explore the Express module with some examples.

**Example 1: Setting Up an Express Application**

First, you need to install Express in your project:

```bash
npm install express --save
```

Now, let's create a simple Express application:

```javascript
// Import the Express module
const express = require('express');

// Create an Express application
const app = express();

// Define a route
app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

In this example:
- We import the `express` module and create an Express application instance.
- We define a route for the root URL ("/") using `app.get()`, which responds with "Hello, Express!" when accessed via a GET request.
- We start the server on port 3000.

**Example 2: Express Routes**

Express allows you to define multiple routes for different URL paths and HTTP methods. Here's an example:

```javascript
app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

app.get('/about', (req, res) => {
  res.send('This is the about page.');
});

app.post('/data', (req, res) => {
  res.send('Received a POST request.');
});
```

In this example:
- We define a route for the root URL ("/") and an "/about" page that responds to GET requests.
- We also define a route for "/data" that responds to POST requests.


---
### Postman

Postman is a popular and powerful tool used by developers and testers to simplify the process of testing APIs (Application Programming Interfaces). It provides an intuitive graphical user interface (GUI) that allows you to send HTTP requests to your API endpoints, inspect responses, and automate API testing. Here are some key features and uses of Postman:

1. **Creating a Request**:
   - Open Postman and click the "New" button to create a new request.
   - Choose the HTTP method (e.g., GET, POST) for your request.

2. **Request URL**:
   - Enter the URL of the API endpoint you want to test in the request URL field.

3. **Headers**:
   - You can set request headers by clicking on the "Headers" tab.
   - Headers are used to pass additional information to the server, such as authentication tokens or content type.

4. **Request Body**:
   - If your request requires a request body (e.g., for POST or PUT requests), you can define it in the "Body" tab.
   - You can send data in various formats like JSON, form-data, x-www-form-urlencoded, etc.

5. **Sending a Request**:
   - Click the "Send" button to send the request to the specified endpoint.
   - Postman will display the response in the lower part of the window.

6. **Response**:
   - You can view the response status code, headers, and body in the response section.
   - You can also format and highlight the response body using the options provided.

7. **Collections**:
   - Organize your requests into collections for better management.
   - Create a new collection by clicking the "New" button under "Collections."

8. **Variables**:
   - Use environment and global variables to store values that can be reused across requests.
   - Variables are helpful for managing different environments (e.g., development, production) or dynamic data.

9. **Tests and Assertions**:
   - Write test scripts to validate the response data.
   - You can use JavaScript to write custom tests.
   - Use the "Tests" tab in the request to add test scripts.


These are some of the basic concepts and features of Postman. It's a versatile tool with many capabilities that can greatly simplify the process of working with APIs, testing, and collaborating with your team. As you become more familiar with Postman, you can explore its advanced features and customization options to suit your specific needs.


Here are simple examples of how to implement POST and DELETE requests in an Express.js application.

**POST Request Example**:

In this example, we'll create a basic Express application that handles a POST request to add a new user to a list of users.

```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON request bodies
app.use(express.json());

// Sample user data (in-memory storage)
let users = [
  { id: 1, name: 'User 1' },
  { id: 2, name: 'User 2' }
];

// POST endpoint to add a new user
app.post('/users', (req, res) => {
  const newUser = req.body;

  // Assign a unique ID to the new user (in a real app, you'd typically use a database)
  const userId = users.length + 1;
  newUser.id = userId;

  // Add the new user to the list
  users.push(newUser);

  res.status(201).json({ message: 'User created', user: newUser });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

To test this, send a POST request to `http://localhost:3000/users` with a JSON body, for example:

```json
{
  "name": "New User"
}
```

The server will respond with a JSON message confirming that the user has been created.

**DELETE Request Example**:

In this example, we'll create an Express application that handles a DELETE request to remove a user from the list.

```javascript
const express = require('express');
const app = express();
const port = 3000;

// Sample user data (in-memory storage)
let users = [
  { id: 1, name: 'User 1' },
  { id: 2, name: 'User 2' }
];

// DELETE endpoint to delete a user by ID
app.delete('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);

  // Find the user index by ID
  const userIndex = users.findIndex(user => user.id === userId);

  if (userIndex === -1) {
    return res.status(404).json({ message: 'User not found' });
  }

  // Remove the user from the array
  users.splice(userIndex, 1);
  
  res.json({ message: 'User deleted' });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

To test this, send a DELETE request to `http://localhost:3000/users/1` to delete the user with ID 1.

These examples demonstrate how to implement POST and DELETE requests in an Express.js application. They focus on the core functionality without extensive error handling or database interactions. In practice, you would typically include more robust validation and potentially use a database for data storage.



## Middleware
Middleware functions in Express.js are functions that have access to the request (`req`) and response (`res`) objects and can perform actions or transformations on them. They are used to handle tasks like parsing request data, authentication, logging, error handling, and more. Middleware functions can be added to your Express application using `app.use()` or applied to specific routes using `app.use()` or `app.METHOD()` (e.g., `app.get()`, `app.post()`).

Here's a simple example of how to create and use middleware in an Express.js application:

```javascript
const express = require('express');
const app = express();
const port = 3000;

// Custom middleware function
const loggerMiddleware = (req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next(); // Call the next middleware in the chain
};

// Register the middleware globally for all routes
app.use(loggerMiddleware);

// Route handler
app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

In this example:

1. We define a custom middleware function called `loggerMiddleware`. It logs the request method and URL along with a timestamp.

2. We use `app.use()` to register the `loggerMiddleware`, which means it will be executed for all incoming requests.

3. We have a simple route handler for the root path ("/") that sends a "Hello, Express!" response.

When you run this Express application, every incoming request will trigger the `loggerMiddleware` to log information about the request. This is just one example of middleware; you can create and use middleware functions for various purposes, including authentication, request validation, error handling, and more.

Middleware functions are executed in the order they are registered with `app.use()`, so the order of middleware registration matters. You can also apply middleware to specific routes by using `app.use()` or `app.METHOD()` for those routes.

For example, if you wanted to apply `loggerMiddleware` only to a specific route, you could do the following:

```javascript
app.get('/special', loggerMiddleware, (req, res) => {
  res.send('This route is special!');
});
```

In this case, the `loggerMiddleware` will only run for requests to the "/special" route.

Remember that middleware functions can perform various tasks, and you can create custom middleware to suit your application's needs.

### Authentication middleware
Authentication middleware in an Express.js application is used to check if a user is authenticated before allowing access to certain routes or resources. Below is a simple example of how to create an authentication middleware to protect routes and ensure users are authenticated before accessing them. We'll use a basic username and password authentication mechanism for demonstration purposes.

Here's an example where we use `app.use` to protect all routes with the authentication middleware:

```javascript
const express = require('express');
const app = express();
const port = 3000;

// Sample user data (in-memory storage)
const users = [
  { id: 1, username: 'user1', password: 'password1' },
  { id: 2, username: 'user2', password: 'password2' },
];

// Middleware for basic authentication
const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (!authHeader) {
    return res.status(401).json({ message: 'Unauthorized' });
  }

  const [authType, authCredentials] = authHeader.split(' ');

  if (authType !== 'Basic') {
    return res.status(401).json({ message: 'Unauthorized' });
  }

  const credentials = Buffer.from(authCredentials, 'base64').toString('utf-8');
  const [username, password] = credentials.split(':');

  const user = users.find((u) => u.username === username && u.password === password);

  if (!user) {
    return res.status(401).json({ message: 'Unauthorized' });
  }

  req.user = user; // Attach the user object to the request for later use
  next();
};

// Apply the authentication middleware globally for all routes
app.use(authenticate);

// Protected route
app.get('/protected', (req, res) => {
  res.json({ message: 'You have access to the protected resource!', user: req.user });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

In this updated example:

- We use `app.use(authenticate)` to apply the `authenticate` middleware globally for all routes. This means that every route defined after `app.use(authenticate)` will require authentication.

- The "/protected" route does not have the `authenticate` middleware applied directly to it. Instead, it inherits the authentication requirement from the global middleware.

Now, all routes are protected by the authentication middleware, and you don't need to manually apply the middleware to each individual route.

### Route-level middleware
Route-level middleware in Express.js allows you to apply middleware functions to specific routes rather than applying them globally to all routes. This gives you more fine-grained control over which routes have specific middleware functions applied to them. Here's an example of how to use route-level middleware:

```javascript
const express = require('express');
const app = express();
const port = 3000;

// Sample user data (in-memory storage)
const users = [
  { id: 1, username: 'user1', password: 'password1' },
  { id: 2, username: 'user2', password: 'password2' },
];

// Middleware for basic authentication
const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (!authHeader) {
    return res.status(401).json({ message: 'Unauthorized' });
  }

  const [authType, authCredentials] = authHeader.split(' ');

  if (authType !== 'Basic') {
    return res.status(401).json({ message: 'Unauthorized' });
  }

  const credentials = Buffer.from(authCredentials, 'base64').toString('utf-8');
  const [username, password] = credentials.split(':');

  const user = users.find((u) => u.username === username && u.password === password);

  if (!user) {
    return res.status(401).json({ message: 'Unauthorized' });
  }

  req.user = user; // Attach the user object to the request for later use
  next();
};

// Apply the authentication middleware to a specific route
app.get('/protected', authenticate, (req, res) => {
  res.json({ message: 'You have access to the protected resource!', user: req.user });
});

// Another route without authentication middleware
app.get('/public', (req, res) => {
  res.json({ message: 'This is a public resource.' });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

In this example:

- We define the `authenticate` middleware as before.

- We apply the `authenticate` middleware to the "/protected" route by including it as a second argument after the route path when defining the route.

- The "/public" route does not have the `authenticate` middleware applied, so it does not require authentication.

With this setup, the "/protected" route requires authentication because the `authenticate` middleware is applied to it. The "/public" route, on the other hand, does not require authentication and is accessible without any additional middleware. Route-level middleware allows you to customize the middleware applied to each route in your Express.js application.



### Built-in Middleware
Sure, let me explain these three commonly used built-in middleware functions in Express:

1. **express.static(root, [options])**:

   - `express.static` is a middleware function that serves static files such as HTML, CSS, JavaScript, images, and more.
   - It is often used to serve client-side assets, making it easy to host static files like HTML, CSS, and JavaScript for your web application.
   - The `root` parameter specifies the root directory from which to serve static files.
   - The optional `options` object allows you to configure various settings, such as caching and file handling.

   Example:

   ```javascript
   const express = require('express');
   const app = express();

   // Serve static files from the 'public' directory
   app.use(express.static('public'));
   ```

   In this example, if you have an "index.html" file in the "public" directory, you can access it in your browser by navigating to `http://localhost:3000/index.html`.

#### Static Hosting
Static hosting, also known as static web hosting or static file hosting, refers to the process of serving static files, such as HTML, CSS, JavaScript, images, and other assets, over the internet using a web server. Static files are files that do not change dynamically based on user interactions or database queries.

Static hosting is commonly used for websites, single-page applications (SPAs), documentation sites, and other web-based content that does not require server-side processing.

2. **express.json([options])**:

   - `express.json` is a middleware function that parses incoming JSON requests and makes the parsed data available in the `req.body` property.

3. **express.urlencoded([options])**:

   - `express.urlencoded` is a middleware function that parses incoming URL-encoded data from forms and makes it available in the `req.body` property.

These built-in middlewares in Express simplify common tasks like serving static files and parsing request data, making it easier to handle different types of requests in your web application or API.

### Route Parameters and Query Parameters
In web development, route parameters and query parameters are mechanisms for passing data to a web server or an application, typically through a URL. They are commonly used to customize and control the behavior of a web application by providing information about the requested resource or specifying additional options.

**Route Parameters**:

Route parameters are part of the URL's path and are used to define variable parts of a route. They are typically denoted by placeholders in the route pattern, surrounded by colons (`:`). When a client makes a request with a URL that matches the route pattern, the values specified in the URL are extracted and made available to the server or application.

For example, in a RESTful API, you might have a route for retrieving a specific user's profile:

```
GET /users/:userId
```

In this URL, `:userId` is a route parameter. When a request is made to `/users/123`, the server can extract the value `123` from the URL and use it to retrieve the user with that ID.


**Query Parameters**:

Query parameters are part of the URL's query string and are used to provide additional information or data to the server. They are typically specified after the `?` character in the URL and are in the form of key-value pairs.

For example, in a search feature, you might have a URL that includes query parameters to filter results:

```
GET /search?q=keyword&page=2&sort=desc
```

In this URL, `q`, `page`, and `sort` are query parameters. They allow the server to understand the search query, the desired page, and the sorting order.


In summary, route parameters and query parameters are essential for building dynamic web applications and APIs. They allow you to customize the behavior of your routes and pass data between clients and servers effectively. Route parameters are part of the URL's path and are extracted using placeholders in the route pattern, while query parameters are part of the URL's query string and are provided as key-value pairs after the `?` character. Express.js simplifies the handling of both types of parameters in your server-side code.

