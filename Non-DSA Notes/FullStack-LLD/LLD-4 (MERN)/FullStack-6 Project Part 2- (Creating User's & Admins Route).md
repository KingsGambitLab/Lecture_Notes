# Full Stack LLD & Projects: FullStack-5: Project Part 2- (Creating User's & Admins Route)


## Agenda
* Revise the concepts taught in the previous class.
* Registration route creation
* Login route creation for the user
* JWT and Protected Route



## Login and Registration Route Creation

>Before proceeding, show a glimpse of the project done till now. 
>Ask the students if they have any doubt uptil now. 

Now that we have written the code for registration, we will be going ahead with the login process. 

* Registration is a one-time process. 
* Login- After entering the username and password, we only need to check for the credentials if the user exists in the database or not

>Ask the students which method should be used to create login route. Like for registration, we used the POST method, similarly, what should be used here?

The answer is, we will be using the POST method for login route creation. It is so, because we are sending the data to the backend and then matching it.

### Steps

**Step 1**- Create a post request with name `/login` and it will have a async callback. 

**Step 2**- We will have the first check for email whether it is present in the database or not.
```javascript
const user = await User.findOne({email : req.body.email})
```
The above line is used to find the user email in the particular list of emails.

**Step 3**- If the user is not present, we will not allow the user to login and give an error message. We will set `success` as `false` and message as 'user does not exist'.

```javascript
if(!user){
   return res.send({
      success : false,
      message : 'User does not exist'
   })
}
```
**Step 4**- Now we will be checking for password. We will check if the entered password matches the password in the database. In Bcrypt, there are two methods to compare- `compare` and `compareSync`. As we are using `await`, we will be using `compare`. It will compare the entered password into hash form with the password in the database.

```javascript
const validPassword = await bcrypt.compare(req.body.password , user.password)
```

Here, the first parameter is the password we have entered and the second parameter is the password corresponding to the username.

**Step 5**- If the passwords do not match, we will display an error message.

```javascript
if(!validPassword){
        return res.send({
            success : false,
            message : 'Invalid Password'
  })
}
```
**Step 6**- If everything is successful, we will send a successful message that the user has been logged in successfully.

```javascript
res.send({
        success : true,
        message : 'User Logged in',
})
```

Now, let us test our code. The route in postman will be changed to `login`. We also do not require the `name` key in our data so we erase it and only keep the `email` and `password`. We send the data and we received 'success' message.

>Also show the message after entering an incorrect email and password.

Now, the data needs to be shown on the frontend. We need to link the client and the server. We will be splitting the terminal- zsh and open client and server in split view.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/343/original/upload_f3674562643f00dcbd6f06ce1e68219a.png?1695972822)


On the left is Client and on the right is Server. To run the server we will use the following commands one by one-

```javascript
cd bookmyshow-project

cd server

server.js
```

Now, we have to link our server and client. In our `client` folder, we will go under `package.json` and add the following code-

```javascript
"proxy": "http://localhost:8082"
```

The address is the server address which can be found from postman. Our client will now use the above address as proxy. 


Frontend should know what data should be there, what data is coming, what data to validate. We will be creating a folder `apicalls` under `client` folder. We will be using **axios** to make API calls.

We will create a file called `index.js` under `apicalls` where we will set axios. 

We will import axios and create axios instance. 

```javascript
import axios from 'axios'

export const axiosInstance = axios.create({
    headers : {
        credentials : 'include',
        method : 'post',
        'Content-Type' : 'application/json'
}
})
```
The `create` method of axios is used to create an instance. We will add the above headers.

Now we will set up the route for frontend with file name `user.js`.

**Step 1**- We will require axios instance. As it is in the same folder, we will just use a `.`(dot)

**Step 2**- Register a new user. We will create a function`RegisterUser` which will take in the payload. it is an async function. Inside it we will use a try-catch function. A variable `response` is created and we will be using `axiosInstance` and the method is `post`. The route which we will hit on is `/register` right now. Then the response data will be returned. 

```javascript
export const RegisterUser = async ()=>{
   try {
        const response = await axiosInstance.post('/register' , payload)
        return response.data
   } catch (error) {
      return error
   }
}
```

>Open `pages` folder and then `Register` folder and within it open `index.js`.

**Payload**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/344/original/upload_9441d841911b694a4ceef8a4b3bc465f.png?1695972854)

Now in the above code, we can see that there are various fields and we have to enter some data in it. There is a button of `type="submit"` which sends the data which is entered by the user. That data is known as the **payload**.

In our `registerUser` function, our route is `/register`, and the method is `axios.post`. The proxy that we have set- `"proxy": "http://localhost:8082"` is the server's proxy. The axios instance that we have created will look at the server/ proxy that we have made and inside our proxy we have `register` which will set the data. Basically that user will be registered at the backend. 

**Step 3**- 
* Now, we need to get our payload out and send it to the `register` function. In our `index.js` file opened before, we will be making changes to it. 
* We will be using the `onFinish` function by AntD. It is an AntD version of `onSubmit`. 
* We will implement a `onFinish()` function. Whatever data we get, we will call it as `values`. 
* We will also import the `registerUser` function. 
```javascript
import { RegisterUser } from '../../apicalls/users'
```
* We will have a try-catch block. So, inside the try block, we will try to send values to the `registerUser` function as payload values. 
* If it has been successfully submitted, there won't be any error and success message will be displayed. If it has an error, an error will be displayed. 
```javascript
const Register = () => {
  const onFinish= async (values)=>{
   try {
        const response = await RegisterUser(values)
        if(response.success){
          message.success(response.message)
          console.log(response.message)

        }
        else{
          message.error(response.message)
          console.log(response.message)
        }
   } catch (error) {
       message.error(error)
   }
  }
```
We will also add payload as a parameter to 

```javascript

export const RegisterUser = async (payload) => {
   try {
        const response = await axiosInstance.post('/register' , payload)
        return response.data
   } catch (error) {
      return error
   }
}
```

We will also add the `onFinish` prop to the Form Component.

```javascript
<Form layout = "vertical" className = "mt - 1" onFinish = {onFinish}>
```
Now let us try to register our user on the webpage. 

If the application runs successfully, you will see a success message. If there is any error, like CORS error, we need to fix it. Let's know more about it-

CORS error stands for Cross Origin Resource Sharing. These issues arise due to cross resource sharing. To prevent this, we have to install CORS first and add it in our index.js by using the following lines-
```javascript
var cors = require('cors')
app.use(cors())
```

### Login Route Creation

For login route, inside our users.js file, we will create a `LoginUser` function. You can change the `/login` route to `api/users/login` and similarly for registration and in our `server.js` where we had declared the routes.
```javascript
export const LoginUser = async (payload) => {
   try {
      const response = await axiosInstance.post('api/users/login' , payload)
      return response.data
 } catch (error) {
    return error
 }
}
```
In our `index.js` file of the Login folder, we will write our code. for login data submission to the backend. 

**Login**
* If the user exists, then login successfully. 
* As soon as we login, we will send the user to the home page. And we need the user to navigate from one page to another. For that we will first import hook `useNavigate` from React DOM. Modify the line to
```javascript
import { Link , useNavigate } from "react-router-dom";
```
We will add the location to the navigate function to where we want the current page.
```javascript
const Login = () => {

const navigate = useNavigate()
const onFinish = async(values) =>{
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
}
```


## JWT



### Introduction

* JWT stands for **JSON Web Token**.
* Tell the students that in most of the websites, we do not need to login again and again. In sites like FB, Instagram, when we login before, it does not ask us to login again whenever we open the app. It is possible because of **JWT**.
* JWT is important to get logged in for a particular session. 
* Send [JWT](https://jwt.io/) token link to the students.
* JWT tokens are unique for each session.

### Generate Tokens
 Let us try to generate a unique token for in our `userRoute.js` file for login.
 
 We will first require the jwt package. 
 
 ```javascript
 const jwt = require('jsonwebtoken')
 ```
 
 We will define a `token` variable and use the `sign` method that creates a token. We have to pass it an ID for it to generate a token. 
 
In our `.env` file, we will define `jwt-secret` is a text that you create by yourself. It should not be exposed which might cause harm to the system. 

In our case, we will assign it-
```javascript
jwt_secret = scaler-movies
```

The `expiresIn` function is used to mention for how much time we want the token to remain alive. 
 ```javascript!
 const token = jwt.sign({userId : user._id} , process.env.jwt_secret , {expiresIn :"1d"})

console.log(token)
````

Using the above token, a session will be available to us. A session is a time period. In the above example, we have used `1d` which means 1 day. The token is alive for 1 day and will expire after it.

We will also send data as token using the following-

```javascript
 res.send({
        success : true,
        message : 'User Logged in',
        data : token
})
```
In the Postman app, let us try to login and check whether we receive tokens or not. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/345/original/upload_737138f77bbf2405b8dd1a6bccbd797e.png?1695973009)


Now, paste the data part as selected above and let us go to the JWT website and paste it.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/346/original/upload_ccaf8a491276cc6f0702d41fa1e16f30.png?1695973028)

In the payload part, you can see the `userId` starts with `64` and ends with `56`. Now, when we check in database in postman, we can see the a user with same starting and ending id. 

If you want to check for which particular user a token was generated, we can go to JWT website, paste the token and get the ID of that user. 

In our frontend, we will be going to our `index.js` file and setting the token in our local storage. 

```javascript
 if(response.success){
        message.success(response.message)
        localStorage.setItem('token' , response.data)
        window.location.href = "/";
       }
```
The token saved as `response.data` will be saved as token in the local storage. That token will be saved for the time period set by us earlier.

Many times we see the message **session expired** that means the token saved in the local storage has gone. 

we login again now. After logging in we can see under the Applications tab and under local storage the token being stored. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/347/original/upload_86e590e42dbba2888f15677de6f5857f.png?1695973053)




>Ask the students if they have any idea about Protected Routes.

### Introduction
* Protected Route is a route that is not accessible publicly. 
* Login and register page are public routes. But, if you want to see the home page, you will have to pass through the login and registration.
* Some of the resources like Paid courses are coded in such a way that they are under Protected Routes. 

Open `userRoute.js` and create a protected route. 

### Create a Protected Route
* We will be creating a route. Here we want to get the details so we will be using the `get` method. 
* We do not need the password, so we will be using `-name of the property` hyphen along with the name of the property which we do not want. 
* For the code to work, we will have to create a middleware. Inside our `server` folder, we will create a middlware. File called `authMiddleware.s` will be created. 
```javascript
router.get('/get-current-user',authMiddleware, async (req , res) => {
    try {
        const user = await User.findById(req.body.userId).select('-password')

        res.send({
            success : true,
            message : 'User details fetched Successfully',
            data : user
        })
    } catch (error) {
        res.send({
            success: false,
            message: error.message,
          });
    }
})
```

For the middleware, we will write the following code-

Inside the try block, we will use the authorization token. It will contain all the details how you are authorized. 

Authorization token consists of two parts-
* Bearer
* JSON web token


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/348/original/upload_0a53611cf032de2e3578251e93142fac.png?1695973084)

* We want the JSON web token, so we will be using the 1st index. 
* We will be using the `decoded` variable to check whether the `jwt_secret` matches the token generated. If it is generated by the secret, then that user has to be allowed. 


```javascript
const jwt = require('jsonwebtoken')


module.exports = function(req , res , next){
    try {
        const token = req.headers.authorization.split(' ')[1]

        const decoded = jwt.verify(token , process.env.jwt_secret)

        req.body.userId = decoded.userId

        next()
    } catch (error) {
        res.status(401).send({ success: false, message: "Invalid token" });
    }
}
```

If the user is not verified, an error message is generated. 

In our `index.js` file of `apicalls`, we will add the authorization by including-

```javascript
authorization : `Bearer ${localStorage.getItem('token')} `
```

So, when we hit the `/get-current-user` route, it will pass through the middleware `authMiddleware` and when the middleware lets it pass, we will get the user. 

