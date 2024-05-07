# Asynchronous Redux and Thunk-2	

## Agenda
* Learn about Redux Thunk.
* Introduction to Redux life cycle.
* Introduction to Redux thunk life cycle.
* Modify the code done in the previous class according to the concepts taught in today's class. 


## Redux
> Give a quick walk through of the previous code and the webpage designed till now.
> Revise the concepts taught in the previous class in brief.

* The principle of Redux is single source of truth. 
* The state changes that are done in an application are governed by the **store**. 
* Store will have the reducers that are required to manipulate the data. 

Inside our products component, we are fetching our data from the below code. We use the `useEffect` hook and use `axios`. 

```javascript
useEffect(()=>{
      const getProducts = async ()=>{
          const res = await axios.get('https://fakestoreapi.com/products')
          console.log(res.data)
          setProducts(res.data)
      }
```

But, the data inside `useEffect` hook has to be accessed by multiple components. 

> ASk the students, if it is a good way to define the data using `useEffect` hook for every use case? The answer is No. 

* We can use a **Redux store** to perform these operations. 
* We can do asynchronous tasks in Redux using **Redux Thunk**.

>Create a file called `productSlice.js` inside the `store` folder. 

In `productSlice.js`, follow these steps.

**Step 1**- Import **`createSlice`** from redux toolkit.

```javascript
import { createSlice } from '@reduxjs/toolkit';
```

**Step 2**- We are creating a slice object `productSlice`. Inside that, there is `initialState` where we can have multiple options in the form of an objects. It is so because the API may not return success every time. There might be failures or other things received from an API. 

```javascript
initialState:{
    }
```

**Step 3**- The slice has the first parameter as the name which is `Product`. The `initialState` will be an object. Inside the `initialState`, the first key will be `data` which will be an array. The second key will be `status` which will show the status of page loading.
```javascript
const productSlice=createSlice({
    name:'Product',
    initialState:{
        data:[],
        status:STATUSES.SUCCESS
    },
```

**Step 4**- We will define the different possibilities of `status` outside the `productSlice object`. There can be 3 possibilities-
* **Loading**- You are calling an API and it is loading. 
* **Success**- The API has loaded successfully.
* **Error**- The API has encountered an error. 

```javascript
const STATUSES={
    SUCCESS:'success',
    ERROR:'error',
    LOADING:'loading'
}
```
It is a good practice to have the word `STATUSES` in capitals. 

The value of `status`  inside our `initialState` object will be SUCCESS.

```javascript
initialState:{
    data:[],
    status:STATUSES.SUCCESS
}
```

**Step 5**- We will now create reducers. This reducer will be setting a product and hence will be named as `setProduct`. It takes in two parameters- `state` and `action`. Now we will define the reducer, i.e, what it will do. The data that it will receive will be a payload entirely. 

```javascript
reducers: {
    setProducts(state,action){
        state.data=action.payload
    }
}
```

**Step 6**- To get the data, we will have to use **Thunks**. Thunks are generally functions only but they take asynchronous functions inside them and they process the reducers.

As thunks are nothing but functions, we will use the `function` keyword to define them. It returns an `async function` and a parameter names `dispatch`. 

>Tell the students that there can be multiple possibilities of status which can also lead to an error. How can they be handled? Ans is by using a try and catch block. 

**Step 7**- In the try block, we will get the data. The data is fetched from 

```javascript
const res= await axios.get('https://fakestoreapi.com/products')
```


**Key points**
* The reason to use React Thunks is- The API calls are heavy and they take time.
* Whenever something takes a lot of time in JavaScript, that is tackled using asynchronous way. 

The data needs to be dispatched to our reducer. First we need to export the `setProduct` reducer.

```javascript
export const {setProducts}=productSlice.actions
export default productSlice.reducer
```
Then we will add this line inside our try block.

```javascript!
dispatch(setProducts(res.data))
```

**Step 8**- The 2nd reducer is `setStatus`.

```javascript!
setStatus(state,action){
    state.status=action.payload
}
```

First, the data is in the loading state, the status can be set as loading. It is written before the try block.

```javascript
dispatch(setStatus(STATUSES.LOADING))
```
Then, after the data is fetched, success status is returned. It is inside the try block after the data is dispatched.

```javascript
dispatch(setStatus(STATUSES.SUCCESS))
```

In the catch block, the error is caught.
```javascript
dispatch(setStatus(STATUSES.ERROR))
```

The function `fetchProducts` will be exported using the `export` keyword. Using it, we can use it anywhere in our code. 

The code till now is

```javascript!
import { createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

const STATUSES={
    SUCCESS:'success',
    ERROR:'error',
    LOADING:'loading'
}

const productSlice=createSlice({
    name:'Product',
    initialState:{
        data:[],
        status:STATUSES.SUCCESS
    },
    reducers: {
        setProducts(state,action){
            state.data=action.payload
        }
    },
    setStatus(state,action){
        state.status=action.payload
    }
    
})

export const {setProducts,setStatus}=productSlice.actions
export default productSlice.reducer

export function fetchProducts(){
    return async function fetchProductThunk(dispatch){
        dispatch(setStatus(STATUSES.LOADING))
        try{
            const res= await axios.get('https://fakestoreapi.com/products')
            dispatch(setProducts(res.data))
            dispatch(setStatus(STATUSES.SUCCESS))

        }
        catch(error){
            console.log(error)
            dispatch(setStatus(STATUSES.ERROR))
        }
    }
}

```


Now we will register our `productSlice` in `store.js`. It will be imported in `store.js` file.

```javascript
import productReducer from './productSlice'
```

And we will also use product
```javascript
const store = configureStore({
    reducer : {
       cart : cartReducer,
        products:productReducer
    }
})
```

Now we will check if our data is being reflected in our app. We will check in the inspect section under redux and refresh the page. We will see one slice. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/523/original/Screenshot_2023-09-20_182717.png?1695214750)

It is the store reducer. 

In our products.js we need to import `fetchProducts`. The code-

```javascript
useEffect(()=>{
      const getProducts = async ()=>{
          const res = await axios.get('https://fakestoreapi.com/products')
          console.log(res.data)
          setProducts(res.data)
      }
```

will be replaced with 

```javascript
useEffect(()=>{
      const getProducts = async ()=>{
          dispatch(fetchProducts())
      }
```

After dispatching, we will get all of the reducers. 
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/524/original/Screenshot_2023-09-20_182744.png?1695214775)


Now the state has been updated.
>ASk the students which hook will give the access to the whole state? Ans is `useSelector` hook. In Products.js, modify the import hook line.

```
import {useDispatch,useSelector} from 'react-redux'
```

We will need the product state as we are working on the products now. So, we will say- `useSelector` give me access to the state. 

```javascript
const {data:products,status}= useSelector((state)=>state.products)
```
The names should be used from the store and not slices.


The following lines should be removed from our code. From the Products.js, we will remove the useState hook. We will also remove the import axios line. After saving, the app will look like this-

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/525/original/Screenshot_2023-09-20_182756.png?1695214791)

The data here is coming from Redux- Redux thunk. 

> Give a quick recap of productSlice.js code which contains the thunk. 

We are able to maintain any particular state for any component by using just the store.

### Redux Life Cycle

> Tell the students that we will be understanding the concepts of Redux by referring to the redux documentation. [Refer this](https://redux.js.org/tutorials/essentials/part-1-overview-concepts).

After scrolling down, there will be a figure- 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/526/original/Screenshot_2023-09-20_182810.png?1695214808)

Now we will understand it by comparing with our app. When we go on our app, it is our UI or User Interface. There are several buttons and thee buttons will **dispatch** actions.

So, when you click on the button- add to cart, it will trigger an event and it is dispatched as a action. 

Let us see dispatch.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/527/original/Screenshot_2023-09-20_182821.png?1695214824)

* As soon as you dispatch, the action payload will go via the reducer. 
* The reducer is defined inside the central store.
* The reducer will make changes to the state.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/528/original/Screenshot_2023-09-20_182829.png?1695214838)

* After the state has been updated, it will be be visible in the UI.

**This is the life cycle of Redux**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/529/original/Screenshot_2023-09-20_182838.png?1695214851)

* First step is the UI.
* Some event will occur and they will go inside the **event handler**. 
>Show some examples of event handlers in the code.
* That event will be **dispatched** with the **action payload**. The **action** will be dispatched.
*  The action will be going inside the **reducer**. The reducers are inside the central store where there are multiple reducers.
*  These reducers will make changes to the state.
*  The state will make changes to the UI. 

### Redux Thunk life cycle

Just like Redux life cycle, there is Redux thunk life cycle also. The link is [here](https://redux.js.org/tutorials/essentials/part-5-async-logic). 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/530/original/Screenshot_2023-09-20_182848.png?1695214865)

* It will start from UI.
* An event will happen and it will go to the event handler.
* Action is dispatched here.
* Middleware is any function that is present inside the flow of the function. It does a particular task inside a sequence. 
* As it is async, middleware will send a request to the API. The API will send a response to the middleware. 
* As soon as the response is received, it will go to the reducer. 
* So the reducer is making the changes to the state. 
* The state is making changes to UI. 

> Ask the students to relate the code with the Redux life cycle.


### Redux toolkit
This is the old way to create thunk in React. 

```javascript!
export function fetchProducts(){
    return async function fetchProductThunk(dispatch){
        dispatch(setStatus(STATUSES.LOADING))
        try{
            const res= await axios.get('https://fakestoreapi.com/products')
            dispatch(setProducts(res.data))
            dispatch(setStatus(STATUSES.SUCCESS))

        }
        catch(error){
            console.log(error)
            dispatch(setStatus(STATUSES.ERROR))
        }
    }
}
```

Now as there is Redux toolkit, we can use a method provided to us by the redux toolkit. The method is **`createAsyncThunk`**. 

*  First import `createAsyncThunk` at the start.
*  This method was created to reduce the length of the code and make it more concise. 

```javascript
export const fetchProducts=createAsyncThunk('products',async()=>{
    const res= await axios.get('https://fakestoreapi.com/products')
    return res.data
})
```
Here, 'products' is the name of the thunk.

> Ask the students, if they wonder how the code is working if we are not sending any actions to the reducers. 

There is also a change to the reducers part. We will not be defining the reducers in this way

```javascript
 reducers: {
        setProducts(state,action){
            state.data=action.payload
        }
    },
 setStatus(state,action){
        state.status=action.payload
    }
}
```

Instead, the code shown below will be used. We will use the `extraReducers` function. This function takes in `builders` as a parameter and within this function, we will define our cases. 

The `builder` is similar to promises and has three cases- pending, fulfilled and rejected.

```javascript
extraReducers : (builder)=>{
    builder.addCase(fetchProducts.pending, (state)=>{
        state.status=STATUSES.LOADING
    }).addCase(fetchProducts.fulfilled, (state,action)=>{
        state.data=action.payload
        state.status=STATUSES.SUCCESS
    }).addCase(fetchProducts.rejected, (state)=>{
        state.status=STATUSES.LOADING
    })
}
```
Before running the code, import `fetchProducts` also.

Depending on the data, the callback function will return the status.


Additionally, in our products.js code, we can also see the current status by including the following 

```javascript
if(status===STATUSES.LOADING){
    return <h2>Loading..</h2>
}

if(status===STATUSES.ERROR){
    return <h2>Something is wrong</h2>
}
```