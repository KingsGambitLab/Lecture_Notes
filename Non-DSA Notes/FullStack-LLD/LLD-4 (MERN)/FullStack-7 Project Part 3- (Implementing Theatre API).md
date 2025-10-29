

## Protected Route
A protected route is a route that is not available publicly

**So how to access it?** 

It can only be accessed after passing ones credentials only after which can one see the actual route. 


## Token
**JWT (JSON Web):** Whenever a person logs in, a JWT token is generated which is totally unique and this token is then saved to a local storage of browser user is using. 

### How does it work?
If the token is already present in the browser local storage system knows that user is logged in. 

```javascript
const token = jwt.sign({userID: user_id}, process.env.jwt_secret, {expires})
```
### Properties Used: 

Our objective is to retrieve the userID of the currently signed-in user. Following are the steps: 

* We obtain the userID from the database where user information is stored. 
* For this specific user, a JSON web token is generated.
* To achieve this, we utilize a **jwt_secret**, which is essentially a unique value responsible for generating these web tokens.
* Additionally, we employ a property that defines the token's lifespan, ensuring that after a user logs in, they will have access for only one day. 
* Subsequently, once the token expires, the user will need to log in again. 

```javascript
console.log(token)

res.send({
    sucess: true,
    message: "User logged in",
    data: token
})
```


## Implementation of a protected route?
Once the token is generated and sent to the database which will then be used to implement a protected route only after which will a user be able to access the content of a particular route

```javascript
router.get('/get-current-user', authMiddleware, async (req, res) => {
    try{
        const user = await User.findById(req.body.userId).select('')
        res.send({
            sucess: true,
            message: "User details fetched successfully"
            data: user
        })
    }
    catch(error){
        res.send({
           success: false,
            message: error.message,
        });
    }
})

```

Here `/get-current-user` is a protected route, 
`authMiddleware` checks if the user is authorized to acess this route by checking if the user is authenticated or not. 

Only if the token is present in the database (generated prior by jwt_secret) only then we will allow the user to access the contents. 

```javascript
module.exports = function(req, res, next){
    try{
        const token = req.headers.authorization.split('')[1]
        const decoded = jwt.verify(token, process.env.jwt_secret)
        req.body.userId = decoded.userId
        next()
    }
    catch(error){
        res.status(401).send({success: false, message: "Invalid"})
    }
}
```

If a token is available, we first decode the user ID and then proceed to the next step.

Returning to our earlier code, we retrieve the userID and omit the password as it is unnecessary. Once we locate the user, we display a message indicating that they may proceed.


## Front-end
Now that the backend part is done we need to move onto the front end part of this

Let's see checks needed for login function

```javascript
import React from 'react'

const ProtectedRoute = ({childern}) => {
    return {
        <div></div>
    }
}
export default ProtectedRoute
```
Here,
**childern (home page):** a component that I want to make it protected

### Redux
As we move further manging a state is diffcult which is why we'll be using redux

```javascript
npm install @reduxjs/toolkit
npm install react-redux
```

We're using redux here to basically use a loader whenever a user logs in

Three files can be created as following
```javascript
/redux
- loaderSlice.js
- store.js
- userSlice.js

```
**userSlice.js**
```javascript!
import {createSlice} from '@reduxjs/toolkit';

const loadersSlice = createSlice({
    name: "loaders",
    initialState: {
        loading: false,
    },
    reducers: {
        ShowLoading : (state) => {
            state.loading = true;
        },
        HideLoading : (state) => {
            state.loading = false;
        }
    }
});
export const {ShowLoading, HideLoading} = loaderSlice.actions;
export default loadersSlice.reducer;
```

**Store.js**
```javascript
import { configureStore } from "@reduxjs/toolkit";
import loadersReducer from "./loadersSlice";
import usersReducer from "./usersSlice";

const store = configureStore({
  reducer: {
    loaders: loadersReducer,
    users: usersReducer,
  },
});

export default store;
```

**loaderSlice.js**

```javascript
import {createSlice} from '@reduxjs/toolkit';

const loadersSlice = createSlice({
    name: 'loaders',
    initialState: {
        loading : false,
    },
    reducers: {
        ShowLoading : (state) => {
            state.loading = true;
        },
        HideLoading : (state) => {
            state.loading = false;
        }
    }
});

export const {ShowLoading, HideLoading} = loadersSlice.actions;
export default loadersSlice.reducer;
```

Our second step would be to show details if the existing user tries to login again, so the question here is how to get the details of a particular user

We can get user data from the following 
```javascript
const { user } = useSelector{(state) => state.users}
```

Thus our final `protectedroute.js` is:

```javascript
import { message } from "antd";
import React, { useEffect} from "react";
import { GetCurrentUser } from "../apicalls/users";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { SetUser } from "../redux/usersSlice";
import { HideLoading, ShowLoading } from "../redux/loadersSlice";

function ProtectedRoute({ children }) {
  const { user } = useSelector((state) => state.users);
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const getpresentUser = async () => {
    try {
      dispatch(ShowLoading());
      const response = await GetCurrentUser();
      dispatch(HideLoading());
      if (response.success) {
        dispatch(SetUser(response.data));
      } else {
        dispatch(SetUser(null));
        message.error(response.message);
        localStorage.removeItem("token");
        navigate("/login");
      }
    } catch (error) {
      dispatch(HideLoading());
      dispatch(SetUser(null));
      message.error(error.message);
    }
  };

  useEffect(() => {
    if (localStorage.getItem("token")) {
      getpresentUser();
    } else {
      navigate("/login");
    }
  }, []);

  return (
    user && 
    (
      <div className = "layout p-1">
        <div className = "header bg-primary flex justify-between p-2">
          <div>
            <h1 className = "text-2xl text-white cursor-pointer"
              // onClick={() => navigate("/")}
            >Book My Show</h1>
          </div>

          <div className = "bg-white p-1 flex gap-1">
            <i className = "ri-shield-user-line text-primary mt-1"></i>
            <h1
              className = "text-sm underline"
              onClick = {() => {
                if (user.isAdmin) {
                  navigate("/admin");
                } else {
                  navigate("/profile");
                }
              }}
            >
              {user.name}
            </h1>

            <i
              className = "ri-logout-box-r-line mt-1"
              onClick = {() => {
                localStorage.removeItem("token");
                navigate("/login");
              }}
            ></i>
          </div>
        </div>
        <div className = "content mt-1 p-1">{children}</div>
      </div>
    )
  );
}

export default ProtectedRoute;
```
## Summary so far
To sum up we have the following: 
* `userRoute.js` file
* Get current user route
* Middleware
* **API calls**: In order to get the current user
* **Redux**: contains slices and store.js files
* `Protected route.js` file



## Login
In order to prevent the user from going back to login page after logging in we can do the following 

```javascript
useEffect{() => {
    if(localStorage.getItem("token")){
        navigate("/");
    }
}, []};
```
You can use CDN remix icon link in your html file to add stylish icons
 

## Users
We'll have two types of user
### Admin
1. **Add the movies:** By editing updates
2. **Add the theatres**
`isAdmin: true`

### User
1. login/logout
2. see the shows
3. book the tickets
4. generate ticket
5. make payment
`isAdmin: false`

`/admin` If this is present in the url of the app then check for certain permissions by checking if `isAdmin` property is *true*, if yes give the rights and if not then revert to

`/profile`: normal user rights. 




## UI - Display
The finished UI should have the following: 
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/687/original/upload_9010f428767216bb0f328d971b568460.png?1697915994)

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/688/original/upload_a50a1c5e7351b37a4c5c3b8c469e34b5.png?1697916285)


### Display: Form elements
1. **Add button**: It places the text at respective places/variables
2. **Movie Route**: Adds movies using Instance.AddMovies
3. **Table** at UI



