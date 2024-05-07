

## Agenda
**Topics to cover in Node:**
* Exploring different node inbuilt modules
* Understanding server side development with node (http)
* Understanding http  module with req and res
* Serving static html sites & json files via the server

We will try to cover most of these topics in today's sessions and the remaining in the next.

It is going to be a bit challenging, advanced, but very interesting session covering topics that are asked very frequently in interviews.

So let's start.

## Nodejs
Node.js is an open-source, server-side JavaScript runtime environment that allows you to run JavaScript code on the server. It was created by Ryan Dahl and first released in 2009. Node.js is built on the V8 JavaScript engine, which is also used in Google Chrome, and it provides an event-driven, non-blocking I/O model that makes it well-suited for building scalable and high-performance network applications.
## Why use nodejs for web server
Node.js is a popular choice for web servers, especially in scenarios involving heavy I/O operations and small server requirements. Here's why Node.js is a suitable option for such use cases:

1. **Non-Blocking I/O Model:** Node.js is designed around a non-blocking, event-driven architecture. This means it can efficiently handle multiple I/O operations concurrently without blocking the execution of other tasks. When performing heavy I/O operations, such as reading and writing files, making network requests, or interacting with databases, Node.js can initiate these operations and continue executing other code while waiting for the I/O operations to complete. This asynchronous approach is highly advantageous for scenarios with many concurrent I/O tasks.
2. **Scalability:** In situations involving heavy I/O, it's common for multiple clients to make simultaneous requests to the server. Node.js's non-blocking model allows it to handle a large number of concurrent connections efficiently, making it a suitable choice for scalable applications. It can process incoming requests as soon as they arrive, rather than waiting for each request to complete before moving on to the next one.
3. **Low Overhead:** Node.js has a relatively small memory footprint compared to some other web server technologies. This makes it well-suited for small server applications where resource utilization needs to be efficient. You can run multiple Node.js instances on a single server without consuming excessive system resources.
5. **Rich Ecosystem:** Node.js has a vast ecosystem of libraries and modules available through npm, which can simplify the development of web servers for various purposes. Developers can find packages to handle specific I/O tasks, such as file uploads, database connections, and HTTP requests, making it easier to build web servers tailored to their needs.

## How are we going to learn nodejs development 
Learning Node.js development and building a full-stack MERN (MongoDB, Express.js, React, Node.js) application involves multiple steps and concepts. Here's a roadmap to guide you through the process:

1. **Basic JavaScript Knowledge**:
   Before diving into Node.js, ensure you have a strong foundation in JavaScript, as Node.js is JavaScript on the server-side.

2. **Node.js Fundamentals**:
   Start by learning the basics of Node.js, including installation, core modules, and working with the Node.js runtime. You can find introductory tutorials and courses online.

3. **Module and Package Management (npm)**:
   Understand how to use npm (Node Package Manager) to manage dependencies and create projects. Learn how to initialize a project, install packages, and create a package.json file.

4. **Server Concepts with Node.js**:
   Explore the core concepts of building a server with Node.js. This includes creating an HTTP server, handling requests, and sending responses.

5. **Web Server with Express.js**:
   Dive into Express.js, a popular Node.js framework for building web applications and APIs. Learn how to set up routes, handle HTTP requests, and use middleware for tasks like authentication and error handling.

6. **RESTful API with Express.js**:
   Extend your Express.js knowledge to create RESTful APIs. Understand HTTP methods (GET, POST, PUT, DELETE), request and response handling, and best practices for building APIs.

7. **MVC Architecture**:
   Explore the Model-View-Controller (MVC) architectural pattern and how it applies to building web applications with Node.js and Express.js. Organize your code into models, views, and controllers for better maintainability.

8. **MongoDB**:
   Learn about MongoDB, a NoSQL database commonly used with Node.js. Understand how to install MongoDB, perform CRUD operations, and work with collections and documents.

9. **Mongoose**:
   Integrate Mongoose, an ODM (Object-Document Mapping) library, with your Node.js and Express.js application to simplify database operations and schema management.

10. **JWT Authentication**:
    Implement JSON Web Token (JWT) authentication to secure your APIs. Learn how to generate tokens, validate them, and protect routes using JWT.

11. **React Integration**:
    If you want to build a MERN application, learn React for front-end development. Understand React components, state management, and how to create a user interface.

12. **Integration of MERN App**:
    Combine your knowledge of Node.js, Express.js, MongoDB, and React to build a full-stack MERN application. Create RESTful APIs on the server and connect them to your React front-end.

13. **Miscellaneous**:
    Explore other concepts like error handling, testing (using tools like Jest), deployment (using platforms like Heroku or AWS), and performance optimization.

14. **Practice and Build Projects**:
    The best way to solidify your skills is by working on projects. Start with simple projects and gradually move on to more complex ones to gain practical experience.

## Fs module in depth 
The `fs` module in Node.js stands for "File System," and it provides a way to work with the file system on your computer or server. It allows you to read from and write to files, manipulate directories, perform file operations, and more. Let's explore some of the key functionalities of the `fs` module in-depth:

**1. Reading Files:**

The `fs` module provides methods for reading the contents of files. The most commonly used method for this purpose is `fs.readFile()`:

```javascript
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
```

In this example, `readFile()` reads the content of 'example.txt' and then calls the provided callback function with any errors encountered and the file's contents.

**2. Writing Files:**

You can also use the `fs` module to write data to files using methods like `fs.writeFile()`:

```javascript
const fs = require('fs');

const content = 'Hello, world!';

fs.writeFile('example.txt', content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File has been written.');
});
```

Here, `writeFile()` creates or overwrites 'example.txt' with the provided content.

**3. Synchronous vs. Asynchronous Operations:**

Most `fs` module functions come in both synchronous and asynchronous versions. The asynchronous versions (e.g., `fs.readFile()`) allow non-blocking file operations, while synchronous versions (e.g., `fs.readFileSync()`) block the Node.js event loop until the operation is complete.

Asynchronous methods are typically preferred in Node.js to maintain the application's responsiveness.

**4. Working with Directories:**

You can perform operations on directories using methods like `fs.mkdir()`, `fs.rmdir()`, `fs.readdir()`, and `fs.stat()`. These methods allow you to create, remove, list, and get information about directories, respectively.

**5. Renaming and Deleting Files:**

`fs.rename()` can be used to rename files, and `fs.unlink()` to delete them:

```javascript
fs.rename('old-file.txt', 'new-file.txt', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File has been renamed.');
});

fs.unlink('file-to-delete.txt', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File has been deleted.');
});
```

**6. File Statistics:**

The `fs.stat()` method provides information about a file's status, including its size, permissions, and modification timestamp.

```javascript
fs.stat('example.txt', (err, stats) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File size: ' + stats.size);
  console.log('Is directory? ' + stats.isDirectory());
});
```

**7. Watching for Changes:**

Node.js also allows you to watch for changes to files and directories using `fs.watch()` and `fs.watchFile()` methods, which can be useful for real-time monitoring of file system changes.


In Node.js, you can use the `fs` module to create and delete directories. Here's how you can do it:

**Creating a Directory:**

To create a directory, you can use the `fs.mkdir()` method. Here's an example:

```javascript
const fs = require('fs');

const directoryName = 'my-directory';

fs.mkdir(directoryName, (err) => {
  if (err) {
    console.error(`Error creating directory: ${err}`);
  } else {
    console.log(`Directory "${directoryName}" created successfully.`);
  }
});
```

In this code, `fs.mkdir()` is used to create a directory named "my-directory." The callback function is called when the directory creation is complete. If an error occurs, it will be logged.

**Deleting a Directory:**

To delete a directory, you can use the `fs.rmdir()` method. Here's an example:

```javascript
const fs = require('fs');

const directoryName = 'my-directory';

fs.rmdir(directoryName, { recursive: true }, (err) => {
  if (err) {
    console.error(`Error deleting directory: ${err}`);
  } else {
    console.log(`Directory "${directoryName}" deleted successfully.`);
  }
});
```

In this code, `fs.rmdir()` is used to delete the "my-directory" directory. The `{ recursive: true }` option is provided to ensure that the directory and its contents are deleted recursively. The callback function is called when the deletion is complete, and any errors are logged.

Make sure to handle errors appropriately when creating or deleting directories in your Node.js applications to ensure that your code is robust and reliable.

You can check whether a directory or file exists in Node.js using the `fs` module. Here's how you can do it:

**Checking if a Directory Exists:**

To check if a directory exists, you can use the `fs.existsSync()` method. Here's an example:

```javascript
const fs = require('fs');

const directoryPath = '/path/to/your/directory';

if (fs.existsSync(directoryPath)) {
  console.log(`The directory "${directoryPath}" exists.`);
} else {
  console.log(`The directory "${directoryPath}" does not exist.`);
}
```

Replace `/path/to/your/directory` with the actual path to the directory you want to check. `fs.existsSync()` returns `true` if the directory exists and `false` if it doesn't.

**Checking if a File Exists:**

To check if a file exists, you can use the `fs.existsSync()` method as well. Here's an example:

```javascript
const fs = require('fs');

const filePath = '/path/to/your/file.txt';

if (fs.existsSync(filePath)) {
  console.log(`The file "${filePath}" exists.`);
} else {
  console.log(`The file "${filePath}" does not exist.`);
}
```

Replace `/path/to/your/file.txt` with the actual path to the file you want to check. `fs.existsSync()` returns `true` if the file exists and `false` if it doesn't.


It's worth noting that `fs.existsSync()` is a synchronous method, so it can block the Node.js event loop. If you prefer an asynchronous approach, you can use the `fs.access()` method. Here's an example:

```javascript
const fs = require('fs');

const pathToCheck = '/path/to/your/directory-or-file';

fs.access(pathToCheck, fs.constants.F_OK, (err) => {
  if (err) {
    console.log(`The path "${pathToCheck}" does not exist.`);
  } else {
    console.log(`The path "${pathToCheck}" exists.`);
  }
});
```

Replace `/path/to/your/directory-or-file` with the actual path you want to check. The `fs.access()` method asynchronously checks if the path exists and whether it's accessible (in this case, using the `fs.constants.F_OK` flag to check for existence).

Both approaches can be used to determine whether a directory or file exists in your Node.js application, depending on your preference for synchronous or asynchronous code.


## Path Module
The `path` module in Node.js provides utilities for working with file and directory paths. It's an essential module when dealing with file system operations and path manipulation in your Node.js applications. Here are some important functions and concepts from the `path` module:

1. **`path.join([...paths])`**: This method joins multiple path segments into a single path string, taking care of platform-specific path separators (e.g., backslashes on Windows and forward slashes on Unix-like systems).

   ```javascript
   const path = require('path');
   const fullPath = path.join('folder', 'subfolder', 'file.txt');
   ```

2. **`path.resolve([...paths])`**: Resolves an absolute path from multiple path segments, starting from the root directory. It can be helpful for creating absolute paths based on relative ones.

   ```javascript
   const path = require('path');
   const absolutePath = path.resolve('folder', 'subfolder', 'file.txt');
   ```

3. **`path.basename(path[, ext])`**: Returns the base filename of a path, optionally removing a file extension if provided.

   ```javascript
   const path = require('path');
   const fileName = path.basename('/path/to/file.txt');
   ```

4. **`path.dirname(path)`**: Returns the directory name of a path.

   ```javascript
   const path = require('path');
   const dirName = path.dirname('/path/to/file.txt');
   ```

5. **`path.extname(path)`**: Returns the file extension of a path, including the dot.

   ```javascript
   const path = require('path');
   const extension = path.extname('/path/to/file.txt');
   ```

6. **`path.parse(pathString)`**: Parses a path string into an object with properties like `root`, `dir`, `base`, `name`, and `ext`.

   ```javascript
   const path = require('path');
   const pathInfo = path.parse('/path/to/file.txt');
   ```

7. **`path.normalize(path)`**: Normalizes a path by resolving '..' and '.' segments and converting slashes to the appropriate platform format.

   ```javascript
   const path = require('path');
   const normalizedPath = path.normalize('/path/to/../file.txt');
   ```

8. **`path.isAbsolute(path)`**: Checks if a path is an absolute path.

   ```javascript
   const path = require('path');
   const isAbsolute = path.isAbsolute('/path/to/file.txt');
   ```

9. **`path.relative(from, to)`**: Returns the relative path from one path to another.

   ```javascript
   const path = require('path');
   const relativePath = path.relative('/path/from', '/path/to');
   ```

The `path` module is particularly useful when working on cross-platform applications or when dealing with file and directory paths dynamically in your Node.js code. It ensures that your path manipulation is consistent and compatible with various operating systems.

### Copy a file from one folder to another in Node.js
To copy a file from one folder to another in Node.js, you can use the `fs` module. Here's how you can do it:

```javascript
const fs = require('fs');
const path = require('path');

// Define the source and destination file paths
const sourceFilePath = '/path/to/source-folder/source-file.txt';
const destinationFilePath = '/path/to/destination-folder/destination-file.txt';

// Create a readable stream from the source file
const readStream = fs.createReadStream(sourceFilePath);

// Create a writable stream to the destination file
const writeStream = fs.createWriteStream(destinationFilePath);

// Pipe the data from the source file to the destination file
readStream.pipe(writeStream);

// Handle any errors that may occur during the copy process
readStream.on('error', (err) => {
  console.error(`Error reading the source file: ${err}`);
});

writeStream.on('error', (err) => {
  console.error(`Error writing to the destination file: ${err}`);
});

// When the copy is complete, log a success message
writeStream.on('finish', () => {
  console.log('File copied successfully.');
});
```

In this code:

1. Replace `/path/to/source-folder/source-file.txt` with the actual path to the source file you want to copy.
2. Replace `/path/to/destination-folder/destination-file.txt` with the desired path and name for the destination file.

Here's an explanation of what the code does:

- It uses the `fs.createReadStream()` method to create a readable stream from the source file.
- It uses the `fs.createWriteStream()` method to create a writable stream to the destination file.
- It uses the `.pipe()` method to pipe the data from the source stream to the destination stream, effectively copying the file.
- It sets up error event listeners on both the source and destination streams to handle any errors that may occur during the copy process.
- It sets up a finish event listener on the destination stream to log a success message when the copy is complete.

This code will copy the contents of the source file to the destination file. If the destination file already exists, it will be overwritten. Make sure to handle errors and adjust file paths as needed for your specific use case.


---
title: Server side development  
description: Exploring Server side Development with http module
duration: 2100
card_type: cue_card
---
## Server side development
Server-side development, client-side development, and working with database clients are essential components of modern web application development. Let's explore these concepts:

**1. Server-Side Development:**

Server-side development refers to the part of web application development that occurs on the server, typically using server-side technologies and programming languages. Here are key aspects:

- **Server:** A server is a computer or software application that responds to client requests over a network. In web development, a server typically hosts the backend of a web application.
- **Server-Side Technologies:** Common server-side technologies include Node.js, Python (with frameworks like Django or Flask), Ruby (with Ruby on Rails), Java (with Spring or Java EE), PHP, and more. These technologies enable you to create the server logic, handle requests from clients, interact with databases, and generate dynamic content.
- **Server Logic:** Server-side code manages user authentication, business logic, data processing, and database interactions. It often generates HTML, JSON, or other data to send back to the client.
- **Security:** Security measures like input validation, authentication, authorization, and protecting against common vulnerabilities (e.g., SQL injection, XSS) are typically implemented on the server side.

**2. Client-Side Development:**

Client-side development focuses on the part of web application development that occurs in the user's web browser. Here are key aspects:

- **Client:** The client is the user's device (e.g., web browser) that sends requests to a server to access web content or services.
- **Client-Side Technologies:** Common client-side technologies include HTML, CSS, and JavaScript. HTML is used for structuring web content, CSS for styling, and JavaScript for adding interactivity and functionality to web pages.
- **Front-End Frameworks:** Developers often use front-end frameworks and libraries like React, Angular, or Vue.js to build complex and responsive user interfaces.
- **User Experience:** Client-side development is responsible for creating an engaging and user-friendly experience. This includes handling user interactions, form validations, and rendering dynamic content without requiring full page reloads.
- **Performance:** Optimizing client-side performance is crucial, as the client device has limited resources. Techniques like lazy loading, minification, and caching are employed to enhance the user experience.

**3. Database Client:**

A database client is a software component or library that allows your server-side code to communicate with a database management system (DBMS). Here are key aspects:

- **Database Management System (DBMS):** A DBMS is software that manages databases, including storing, retrieving, updating, and organizing data. Examples of DBMSs include MySQL, PostgreSQL, MongoDB, and SQLite.
- **Database Client Libraries:** To interact with a DBMS, developers use specific client libraries or drivers for their chosen programming language. These libraries provide functions and methods to connect to the database, execute queries, and retrieve results.
- **ORM (Object-Relational Mapping):** Some server-side frameworks and languages offer ORMs (e.g., Sequelize for Node.js, Hibernate for Java) that provide a higher-level abstraction for working with databases. ORMs map database tables to objects in code, simplifying database interactions.
- **Data Access:** Server-side code uses database clients to perform CRUD operations (Create, Read, Update, Delete) on data stored in databases. This includes querying data, inserting new records, updating existing records, and deleting records.


## Server-side development using the `http` module
Server-side development using the `http` module in Node.js allows you to create a basic HTTP server to handle incoming requests and send responses. Here's a step-by-step guide to building a simple HTTP server using the `http` module:

1. **Import the `http` Module:**
   Start by requiring the `http` module in your Node.js script:

   ```javascript
   const http = require('http');
   ```

2. **Create the HTTP Server:**
   You can create an HTTP server using the `http.createServer()` method. This method takes a callback function that will be invoked for each incoming HTTP request.

   ```javascript
   const server = http.createServer((req, res) => {
     // Handle incoming requests here
   });
   ```

3. **Handle Incoming Requests:**
   Inside the callback function, you can handle incoming HTTP requests. The `req` object represents the request, and the `res` object is used to send the response back to the client.

   ```javascript
   const server = http.createServer((req, res) => {
     // Set response header
     res.setHeader('Content-Type', 'text/plain');
     
     // Write response content
     res.write('Hello, World!');
     
     // End the response
     res.end();
   });
   ```

   In this example, we set the `Content-Type` header to `'text/plain'`, write "Hello, World!" as the response content, and then end the response.

4. **Specify the Listening Port and Host:**
   You need to specify the port and host (usually `'localhost'` for development) on which your server will listen for incoming requests:

   ```javascript
   const port = 3000;
   const host = 'localhost';
   
   server.listen(port, host, () => {
     console.log(`Server is listening on http://${host}:${port}`);
   });
   ```

5. **Start the Server:**
   Finally, you can start the server by calling the `server.listen()` method. This will start listening for incoming HTTP requests on the specified port and host.

6. **Test Your Server:**
   Run your Node.js script, and your server will be accessible at the specified URL (e.g., http://localhost:3000). You can use a web browser or tools like cURL or Postman to send HTTP requests to your server.

Here's the complete code for a basic HTTP server:

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  // Set response header
  res.setHeader('Content-Type', 'text/plain');
  
  // Write response content
  res.write('Hello, World!');
  
  // End the response
  res.end();
});

const port = 3000;
const host = 'localhost';

server.listen(port, host, () => {
  console.log(`Server is listening on http://${host}:${port}`);
});
```

This simple HTTP server will respond with "Hello, World!" to any incoming request. You can expand upon this foundation to handle different types of requests and serve dynamic content based on the requested URL or route.

You can modify the code to send an HTML response containing an `<h1>` tag. Here's an example of a Node.js HTTP server that responds with an HTML `<h1>` tag:

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  // Set response header with Content-Type as text/html
  res.setHeader('Content-Type', 'text/html');
  
  // Write HTML response
  res.write('<html><head><title>Node.js HTTP Server</title></head><body>');
  res.write('<h1>Hello, World!</h1>');
  res.write('</body></html>');
  
  // End the response
  res.end();
});

const port = 3000;
const host = 'localhost';

server.listen(port, host, () => {
  console.log(`Server is listening on http://${host}:${port}`);
});
```

In this code:

- We set the `Content-Type` header to `'text/html'` to indicate that the response will contain HTML content.
- We use `res.write()` to send the HTML content, which includes an `<h1>` tag with the text "Hello, World!".
- The response is ended with `res.end()`.

Now, when you access the server in your web browser, you will receive an HTML response with the specified `<h1>` tag. This demonstrates how you can send HTML content as a response using the Node.js `http` module.


### Nodemon
Nodemon is a tool that helps you develop Node.js applications by automatically restarting the Node.js process whenever changes are detected in your project's files. It's particularly useful during development because it eliminates the need to manually stop and restart your Node.js application every time you make code changes.

Here's how to use Nodemon:

1. **Installation**:
   You can install Nodemon globally using npm (Node Package Manager) with the following command:

   ```bash
   npm install -g nodemon
   ```

   Alternatively, you can install it as a development dependency in your project by running the following command inside your project directory:

   ```bash
   npm install --save-dev nodemon
   ```

2. **Basic Usage**:
   After installing Nodemon, you can use it to run your Node.js application instead of the standard `node` command. For example:

   ```bash
   nodemon your-app.js
   ```

   Replace `your-app.js` with the entry point file of your Node.js application.

3. **Automatic Restart**:
   Nodemon will watch for changes in the project directory and its subdirectories. Whenever you save changes to your code, Nodemon will automatically restart your Node.js application with the updated code. This eliminates the need to manually stop and restart the application.

4. **Nodemon Configuration**:
   Nodemon allows you to customize its behavior by using a `nodemon.json` configuration file or specifying configuration options in your project's `package.json` file. You can configure things like which files to watch, ignore specific files or directories, and more.

   Example `nodemon.json`:

   ```json
   {
     "watch": ["src"],
     "ignore": ["node_modules"]
   }
   ```

   Example `package.json` (under the `"nodemon"` key):

   ```json
   "nodemon": {
     "watch": ["src"],
     "ignore": ["node_modules"]
   }
   ```

5. **Additional Features**:
   Nodemon offers additional features such as running scripts, passing environment variables, and more. You can explore these options in the Nodemon documentation and tailor them to your specific needs.

Nodemon is a valuable tool for improving the development workflow in Node.js projects, as it simplifies the process of testing and iterating on your code. It's commonly used in combination with development frameworks like Express.js to streamline web application development.

### Json in the response and setting the header
You can modify the code to send a JSON response from your Node.js HTTP server. Here's an example of a Node.js HTTP server that responds with JSON data:

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  // Set response header with Content-Type as application/json
  res.setHeader('Content-Type', 'application/json');
  
  // Define JSON data
  const jsonData = {
    message: 'Hello, World!',
    date: new Date(),
  };

  // Convert JSON object to a JSON string
  const jsonResponse = JSON.stringify(jsonData);

  // Write JSON response
  res.write(jsonResponse);
  
  // End the response
  res.end();
});

const port = 3000;
const host = 'localhost';

server.listen(port, host, () => {
  console.log(`Server is listening on http://${host}:${port}`);
});
```

In this code:

- We set the `Content-Type` header to `'application/json'` to indicate that the response will contain JSON data.
- We define a JSON object called `jsonData`, which contains a message and the current date.
- We use `JSON.stringify()` to convert the JSON object into a JSON string.
- The response is ended with `res.end()`.

Now, when you access the server in your web browser or send an HTTP request to it, you will receive a JSON response containing the specified data. This demonstrates how you can send JSON data as a response using the Node.js `http` module.

