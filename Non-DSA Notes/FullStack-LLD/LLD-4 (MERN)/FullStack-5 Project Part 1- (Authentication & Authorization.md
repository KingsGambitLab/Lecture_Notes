
## Agenda

The agenda for today's session includes implementing authentication and authorization, exploring protected routes for both users and administrators, discussing BookMyShow integration, covering payment processing with Stripe, and generating tickets. Toward the end, we will focus on deployment. Our initial focus for today will be on the authentication and authorization aspects.

---
title: Project Setup and Adding Frontend Code for Registration
description: In this segment, we'll set up React, Express, Node.js, and a MongoDB database, and we'll also write frontend code for user registration.
duration: 2700
card_type: cue_card
---

## Project Setup and Adding Frontend Code for Registration

Before we move into authentication and authorization, it's essential to set up the project infrastructure. We'll start by configuring React, Express, Node.js, and MongoDB. These components must be installed and configured correctly to proceed.

To begin, let's create a folder named "bookMyShow-project." Inside this folder, create another one called "client," where we'll develop the frontend of our application. To kickstart the React app, use the following command:

```cpp
npm create-react-app
```

Additionally, create a folder named "server" in the main project directory. The "client" folder will house all the frontend code, while the "server" folder will be dedicated to setting up our Express backend. With the React app initialized, let's navigate to the "App.js" file to continue.


#### Pseudocode
```cpp
function App() {
  return (
    <div>
      <h1>
        Hello
      </h1>
    </div>
  )
}
export default App;
```

Now, let's initiate our client application by running the command npm start. 


> Note to instructor - Take a moment to show the local host and see how our app looks.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/324/original/upload_c3cacc7db150560f524aa121bf3cb867.png?1695968640)

With our React app successfully set up, it's time to create two fundamental pages: the login and registration pages. These pages are essential components of any application.

Our initial set of pages includes:

1. Home Page
2. Register Page
3. Login Page

To expedite the development process, we will leverage Ant Design, a library that provides pre-built components, eliminating the need for extensive custom CSS. Within the component section, you'll find various components, each with an example code.

Since our focus is on building the login and registration pages, we'll primarily work with forms. So, let's navigate to the component section, search for "form," and explore multiple form examples. You can choose a form that suits your needs and copy the code from there.

In our client directory, let's begin by installing the required dependencies:

```javascript
npm install react-router-dom antd axios
```


Now, let's structure our project by creating a "pages" folder. Inside this folder, create three subfolders: "login," "register," and "Home." Within each of these subfolders, create an "index.js" file.

Here's the structure for "index.js" within the "Home" folder:


#### Pseudocode
```javascript
const Home = () => {
  return (
    <div>
      This is my home page
    </div>
  )
}
export default Home;
```


Similarly, for the "index.js" file in the "login" folder:


#### Pseudocode
```javascript
const Login = () => {
  return (
    <div>
      This is my Login page
    </div>
  )
}
export default Login;
```



And for the "index.js" file in the "register" folder:

#### Pseudocode

```javascript
const Register = () => {
  return (
    <div>
      This is my Register page
    </div>
  )
}
export default Register;
```

We will navigate to the 'App.js' file import all of these components set up React Router DOM and create our first route 


#### Pseudocode

```javascript
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path = '/' element = {<Home />} />
          <Route path = '/login' element = {<Login />} />
          <Route path = '/register' element = {<Register />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
```


> Note to instructor - Test the functionality of our home page

Within our 'client' folder, we'll create a stylesheet that we'll use in our components. We already have five CSS files prepared:

* '`alignment.css`' contains alignment-related code for flex, margin, justify, padding, and more, so we won't need to worry about these aspects.
* `'custom.css'` is available for customization if you want to tailor the appearance of your application.
* `'form-elements.css'` provides styles for form elements.
* `'sizes.css'` is for adjusting various sizes.
* `'theme.js'` contains definitions for themes, text styles, fonts, and colors that we'll be using.
    

Now, let's turn our attention to the registration page. Here's what we need for this page:

* **Three fields:** name, email, and password.
* A 'Register' button that users can click to complete the registration process.

We'll use the form components provided by Ant Design to facilitate this."

#### Pseudocode
```javascript
import React from 'react';
import { Form } from 'antd';

const Register = () => {
  return (
    <div>
      <Form>
        <Form.Item label = 'Name' name = 'name' rules = {[{ required: true, message: "Please enter your name" }]}>
          <input type = 'text' />
        </Form.Item>
      </Form>
    </div>
  );
}

export default Register;


```





Now, let's proceed to include the remaining fields.


#### Pseudocode
```htmlembedded
import React from 'react';
import { Form } from 'antd';

const Register = () => {
  return (
    <div>
      <Form>
        <Form.Item label = 'Name' name='name' rules = {[{ required: true, message: "Please enter your name" }]}>
          <input type = 'text' />
        </Form.Item>
        <Form.Item label = 'Email' name = 'Email' rules = {[{ required: true, message: "Please enter your email" }]}>
          <input type = 'text' />
        </Form.Item>
        <Form.Item label = 'Password' name = 'Password' rules = {[{ required: true, message: "Please enter your password" }]}>
          <input type = 'text' />
        </Form.Item>
      </Form>
    </div>
  );
}

export default Register;


```

Now, let's make sure to include all our stylesheets in 'App.js' for consistency



#### Pseudocode
```javascript
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import './stylesheets/alignment.css';
import './stylesheets/sizes.css';
import './stylesheets/form-elements.css';
import './stylesheets/theme.css';
import './stylesheets/Custom.css';

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path = "/" element = {<Home />} />
          <Route path = "/login" element = {<Login />} />
          <Route path = "/register" element = {<Register />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

```

We've already added the necessary styling, and to save time, we'll directly integrate our form code into the 'index.js' file of the 'Register' component. We're removing the previously written code and replacing it with Ant Design components to help you understand how to use them effectively.

But there's one element missing - a button. To address this, let's create a 'components' folder. Inside this folder, we'll create a 'buttons' subfolder where we'll add the button code. Then, we'll import the button component into our 'Register' page."


#### Pseudocode
```javascript
import React, { useEffect } from 'react';
import Button from '../../components/Button';
import { Link, useNavigate } from 'react-router-dom';
import { Form, message } from 'antd';
import { RegisterUser } from '../../apicalls/users';

const Register = () => {
  const navigate = useNavigate();

  const onFinish = async (values) => {
    try {
      const response = await RegisterUser(values);
      if (response.success) {
        message.success(response.message);
        console.log(response.message);
      } else {
        message.error(response.message);
        console.error(response.message);
      }
    } catch (error) {
      message.error(error);
    }
  };

  useEffect(() => {
    if (localStorage.getItem('token')) {
      navigate('/');
    }
  }, []);

  return (
    <div className = "flex justify-center h-screen items-center bg-primary">
      <div className = "card p - 3 w - 400">
        <h1 className = "text - xl mb - 1">Welcome to Scaler Shows! Please Register</h1>
        <hr />
        <Form layout = "vertical" className = "mt - 1" onFinish = {onFinish}>
          <Form.Item
            label = "Name"
            name = "name"
            rules = {[{ required: true, message: 'Please input your name!' }]}
          >
            <input type = "text" />
          </Form.Item>
          <Form.Item
            label = "Email"
            name = "email"
            rules = {[{ required: true, message: 'Please input your email!' }]}
          >
            <input type = "email" />
          </Form.Item>
          <Form.Item
            label = "Password"
            name = "password"
            rules = {[{ required: true, message: 'Please input your password!' }]}
          >
            <input type = "password" />
          </Form.Item>

          <div className = "flex flex - col mt - 2 gap - 1">
            <Button fullWidth title = "REGISTER" type = "submit" />
            <Link to = "/login" className = "text-primary">
              {' '}
              Already have an account? Login
            </Link>
          </div>
        </Form>
      </div>
    </div>
  );
};

export default Register;

```



## Implementation of the Login Page

Next, we will craft the login page, following a similar approach. We'll modify the button text to 'Login' and eliminate the 'name' field from the login page's form.


#### Pseudocode
```javascript
import React , {useEffect} from 'react'
import {Form, message} from "antd";
import Button from "../../components/Button";
import { Link , useNavigate } from "react-router-dom";
import { LoginUser } from '../../apicalls/users';



const Login = () => {
   const navigate = useNavigate()

  const onFinish = async(values) => {
     try {
      const response = await LoginUser(values)

      if(response.success){
        message.success(response.message)
        localStorage.setItem('token' , response.data)
        window.location.href = "/";
       }
      else{
        message.error(response.message)
      }
     } catch (error) {
      message.error(error.message)
     }
  }

  useEffect(() => {
    if (localStorage.getItem("token")) {
      navigate("/");
    }
  }, []);

  return (
    <div className = "flex justify-center h-screen items-center bg-primary">
    <div className = "card p - 3 w - 400">
      <h1 className = "text-xl mb-1">Welcome Again! Please Login</h1>
      <hr />
      <Form layout = "vertical" className = "mt - 1" onFinish = {onFinish}>
        <Form.Item
          label = "Email"
          name = "email"
          rules = {[{ required: true, message: "Please input your email!" }]}
        >
          <input type = "email" />
        </Form.Item>
        <Form.Item
          label = "Password"
          name = "password"
          rules = {[{ required: true, message: "Please input your password!" }]}
        >
          <input type = "password" />
        </Form.Item>

        <div className = "flex flex - col mt - 2 gap - 1">
          <Button fullWidth title = "LOGIN" type = "submit" />
          <Link to = "/register" className = "text-primary">
            {" "}
            Don't have an account? Register
          </Link>
        </div>
      </Form>
    </div>
  </div>
  )
}

export default Login
```



## Establish Server-Side Architecture

Next, we'll move into the server-side operations. Within our server directory, we'll create a file named 'server.js' and proceed to install the Express framework.

To enhance security, we'll make use of 'bcryptjs', a package specialized in password hashing. The necessary packages can be installed with the following command:

```javascript
npm install express mongoose bcryptjs jsonwebtoken

```

While the client side encompasses all frontend code, the server side will house the backend logic. In 'server.js', we'll initiate the Express server. This step forms the foundation for our backend operations.


#### Pseudocode
```javascript
const express = require('express');
const app = express();

app.listen(8082, () => {
    console.log('Server is Running');
});

```

In the code snippet provided, we have the 'server.js' file for our Express application. To start the server, you can use 'npx nodemon server.js.' This command ensures that your server automatically restarts upon code changes, streamlining the development process.

As part of our server setup, we'll create an environment configuration ('`.env`') file where you can store essential information such as the MongoDB URL and `JSON Web Token (JWT)` secrets. This allows us to keep sensitive data secure.

Furthermore, we'll establish a 'dbconfig.js' file in the 'config' folder. This file will contain the configuration settings for connecting to our MongoDB database.

#### Pseudocode
```javascript
const mongoose = require('mongoose')



mongoose.connect(process.env.mongo_url)
const connection = mongoose.connection

connection.on('connected' , () => {
    console.log('Connection Succesful')
})
```

To bring everything together, the revised 'server.js' code snippet includes the necessary 'require' statements, environment variable loading, and the inclusion of the 'dbConfig' module. This ensures that our server is properly configured and ready to run on port 8082."


#### Pseudocode
```javascript
const express = require('express');
const app = express();
require('dotenv').config(); // Load environment variables
const dbConfig = require('./config/dbConfig'); // Import database configuration

app.listen(8082, () => {
    console.log('Server is Running');
});
```






## Exploring Authentication

Authentication is a fundamental aspect of our application. We'll define the schema and create a model based on that schema. For user registration, our schema will encompass essential fields like name, password, and email.

To structure our project effectively, we'll establish a 'model' folder. Our initial model, 'userModel.js,' will commence with defining a schema. With this schema in place, we'll proceed to create a model, enabling the creation of various user documents. Mongoose will play a pivotal role in defining our schema.

#### Pseudocode
```javascript
// userModel.js

const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  password: {
    type: String,
    required: true
  },
  isAdmin: {
    type: Boolean,
    required: true,
    default: false
  }
});

module.exports = mongoose.model('users', userSchema);
```

Additionally, we'll implement email validation and introduce an 'isAdmin' property to manage admin-specific permissions for select users.

Routing is another crucial aspect. We'll create user routes within our 'routes' folder.


#### Pseudocode
```javascript
// userRoutes.js

const router = require('express').Router();
const User = require('../models/userModel');

// Register a user
router.post('/register', async (req, res) => {
  try {
    const userExists = await User.findOne({ email: req.body.email });

    if (userExists) {
      return res.send({
        success: false,
        message: 'User Already Exists'
      });
    }

    const newUser = new User(req.body);
    await newUser.save();

    res.send({ success: true, message: 'Registration Successful, Please login' });
  } catch (error) {
    console.log(error);
  }
});

module.exports = router;
```

In the 'server.js' file, we will establish a route for user-related operations:

#### Pseudocode
```javascript
const express = require('express');
const app = express();
require('dotenv').config();
const dbConfig = require('./config/dbConfig');
const userRoute = require('./routes/userRoute');

app.use(express.json());
app.use('/api/users', userRoute);

app.listen(8082, () => {
    console.log('Server is Running');
});

```

> Note to instructor - Test the functionality till this point


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/325/original/upload_0a1c4c3b0afa456fb137116cf0e88e23.png?1695969450)


## Investigating Hashing and Encryption

Hashing and encryption are both methods used to protect data, but they operate differently, and their purposes vary.

Encryption is a two-way process that involves converting data into a coded format (cipher) that can be easily reversed back to its original form (plaintext) using a decryption key. In encryption, there's always a corresponding decryption process, allowing data to be securely stored and transmitted while maintaining its reversibility.

Hashing, on the other hand, is a one-way process. It involves converting data, such as a password, into a fixed-length string of characters, often a hash value or digest. The key distinction is that there's no straightforward way to reverse this process and obtain the original data. If, for instance, a password like "abc" is hashed, it becomes something like "%B#82^&," and this transformation is irreversible. 


One common library used for hashing in JavaScript is bcrypt. Now, let's implement bcrypt in the 'userRoute' code:

#### Pseudocode
```javascript
const router = require('express').Router();
const bcrypt = require('bcryptjs');
const User = require('../models/userModel');

// Register a user
router.post('/register', async (req, res) => {
  try {
    const userExists = await User.findOne({ email: req.body.email });

    if (userExists) {
      return res.send({
        success: false,
        message: 'User Already Exists'
      });
    }

    // Hash the password
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(req.body.password, salt);
    req.body.password = hashedPassword;

    const newUser = new User(req.body);
    await newUser.save();

    res.send({ success: true, message: "Registration Successful, Please login" });

  } catch (error) {
    console.log(error);
  }
});

module.exports = router;

```

In this code, we've integrated bcrypt to securely hash the user's password before storing it in the database. This enhances password security ensures that plaintext passwords are not stored.




![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/326/original/upload_ea5e3fdb5425c91bf4e666263f4ffa03.png?1695969502)



![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/327/original/upload_e13d594015ef8e048d6515afeecbd113.png?1695969539)
