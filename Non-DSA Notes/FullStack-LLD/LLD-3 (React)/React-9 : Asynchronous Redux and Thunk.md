# React Redux and Redux Toolkit


### Redux

Redux is a management tool used to manipulate data within creating a store from where each component can access the properties by dispatching actions to reducers.

**Example**

Let's take an example to understand.

Initialise a react app you can name it `Redux app`.

We will be creating a replica of an E-commerce shopping cart application using Redux.

First, let's create two pages - the home page and the cart page.

You can have two pages using React Router (allows page routing). First, Install React Router then Create a nav bar and add two links: for the home page and cart page.

To install React Router run the command `npm install react-router-dom

The very first step after installing the react router is to **import browser router** then routes and then every specific route.

```javascript!
import { BrowserRouter, Routes, Route } from 'react-router-dom';
```

Step 1: Create a Home page

```javascript!
import React from "react";

const Home = () => {

    return (
        <div>
            <h1>This is Home page.</h1>
        </div>
    )      
}

export default Home
```

Step 2: Create a Cart page

```javascript!
import React from 'react'

const Cart = () => {
  return (
    <div>
        <h1>This is Cart page.</h1>

    </div>
  )
}

export default Cart
```

In the `app.js` file import Browser router, routes and route and add paths to both the pages.

```javascript!
import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Cart  from './pages/Cart';
import Home from './pages/Home';
import NavBar from './components/NavBar';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path = '/' element = {<Home/>}></Route>
          <Route path = '/cart' element = {<Cart/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
```

Now, we want to create a nav bar for our app. To do that create a folder named components inside your source folder. Create a file named NavBar.js inside that folder.
After that add the following simple CSS and Links to your pages.

`NavBar.js`

```javascript!
import React from 'react'
import { Link } from 'react-router-dom'

const NavBar = () => {
  return (
    <div
        style = {{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between'
        }}>
            <span className='logo'>Redux Store</span>
            <div>
                <Link className='navLink' to = '/'>Home</Link>
                <Link className='navLink' to='/cart'>Cart</Link>
                <span className='cartCount'>Cart items:0</span>
            </div> 

    </div>
  )
}

export default NavBar
```

Add your NavBar to your app.js inside the `<BrowserRouter></BrowserRouter>` tag.

Add some CSS inside the `index.css` file to make your page look more optimised.

`index.css`

```css!
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto',
      'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
      'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding: 20px;
  background: whitesmoke;
}
img {
  height: 80px;
}
.card {
  background: white;
  padding: 20px;
  text-align: center;
  border-radius: 10px;
}

.productsWrapper{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
}
.btn{
  border: none;
  outline: none;
  background: gold;
  padding: 5px 10px;
  color: black;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.btn:hover{
  background: green;
}

.remove-btn{
  border: none;
  outline: none;
  background: gold;
  padding: 5px 10px;
  color: black;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.remove-btn:hover{
  background-color: red;
}
.heading{
  padding: 25px 0;
}
.cartCount{
  font-weight: bold;
  text-transform: uppercase;
  margin-left: 40px;
}
.navLink{
  text-decoration: none;
  color: black;
  margin-left: 20px;
}

.cartCard{
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff;
  margin-bottom: 20px;
  padding: 14px;
  border-radius: 5px;
}
```

Now, to create our shopping cart application we will be using [fakeStoreAPI](https://fakestoreapi.com) from where we can get some product data.

How to get data from an API?
-> The package that we are going to use is **Axios**. But Fetch can also be used to get data from an API.

Fresh applications do not have access to Axios. Therefore, you have to install it using the command `npm install axios`.

By using axios, you can use Promises or use the fetch API or async await.

We will create a separate component named `Products.js` inside your components folder to get the data pick that component and add it to our home page.

We use two Hooks: **useEffect** to make asynchronous calls to your API and **useState** for maintaining a state.

Function is defined as async and whenever you do something that will take time you use the await.
By using useEffect hook we can call for our API.

This is your API endpoint: `'https://fakestoreapi.com/products'`

`Products.js`
```javascript!
import axios from 'axios'
import React, { useEffect, useState } from 'react'

const Products = () => {

    const    [products, setProducts] = useState([])

    useEffect(() => {
        const getProducts = async () => {
            const res = await axios.get('https://fakestoreapi.com/products')
            console.log(res)
        }

        getProducts()
    },[]) 
    
  return (
    <div></div>
  )
}

export default Products
```
We want this data to be added to our Home page. To do that add the Products component inside Home.js.

To display all the products from this API we will use `setProducts(res.data)` and create a new div inside which we will add all the components we want to display like product image, and price and add to the cart button.

`Products.js`

```javascript!
return (
    <div>

        <div className='productsWrapper'>
            {
                products.map((product) => {
                    return <div className='card'>
                        <img src= {product.image}/>
                        <h6>{product.title}</h6>
                        <h5>{product.price}</h5>
                        <button className='btn'>Add to cart</button>
                    </div>
                })
            }
        </div>
    </div>
  )
}
```

Now, what we want is that when we click on the add to cart button the number of cart items should increase. But cart items are added in our navBar component while the add to cart button is added in our Products component.

**[Ask the learners]**
How can I pass data from the product component to the cart component or the navBar component?
-> **Redux** is used to pass the data. Redux is flexible as it can be used with other frameworks as well. We can't use prop drilling or context API because of optimisation issues.

You can install the Redux toolkit using the following command: `npm install @reduxjs/toolkit react-redux`. By installing the redux toolkit two libraries will be installed: **reactjs/toolkit and react-redux**.

You can also visit [Redux](https://redux-toolkit.js.org/tutorials/quick-start) documentation to read more about the Redux toolkit.

Before writing redux code install this [chrome](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd/related) extension.

*When we use redux there are a few things to keep in mind*
* Create a centralised store for all your component features and properties.
* We can create slices (a slice is for a specific component where every function will be written for that specific component) of different components. Whatever component you are trying to integrate your features for, you should create separate slices for them.

In the example of the shopping cart, we will create a cart slice. To create a slice there is a method known as `createSlice` which takes an object inside which we can define everything that we want that particular slice to perform.

`cartSlice.js`

```javascript!
import { createSlice } from "@reduxjs/toolkit";


const cartSlice = createSlice({
    name:'cart',
    initialStat:[],
    reducers : {
        add(state, action){
            state.push(action.payload)
        }
    }
```

**cartSlice:** It is created for your cart. Everything that you will do for your cart will be added.
name
**initialState:** The state from where we are going to start there it will be empty. 
**reducers:** Inside the reducers key you will put all those functions that you want to be implemented in your cart. For example: we want to add to the cart feature and remove from the cart feature inside our redux application.
**action.payload:** What is the action you are taking with the data that goes inside action.payload.

We are pushing action.payload. InitialState was empty but now as we have taken an action all the data will be pushed to the initialState array. After that, you can count the length of all the objects inside the array and whatever will be the length will be the number added to your cart.

First, we need to export the add reducer that we are destructuring out from the cartSlice.

Second, you have to export the whole cartSlice.

```javascript!
export const {add} = cartSlice.actions //exporting the add reducer

export default cartSlice.reducer   //exporting the whole cartslice
```

We will be creating a central store named store.js in our Store folder to store everything related to every component will be stored in it. 
Same way as we have the createSlice method by redux, there's another method known as configureStore.

As we know we have an InitialState array and to fetch the data from that particular state for that we have a special kind of hook that is provided from react redux known as **useSelector**. This hook has access to all the global states.

Add useSelector inside the navBar component as shown:

```javascript!
const items = useSelector((state) => state.cart) //use the state of the cart
console.log(items.length) 
```

the console log will give output 0 as initially, cart items are 0.

> We have to use Provider from the react-redux library as our app.js will be the initial page that will show all the components. Therefore to wrap all the components we will be using Provider (not from context API) but from react-redux. Inside Provider, we will add a store as we added value inside our context API provider.

**useDispatch** hook is used to use your reducers. We can dispatch actions to our reducers.

Whatever product is getting added is your action payload.

What we want is for the number of cart items should increase as we click on the 'Add to cart' button that exists in the `Products.js` component. To use reducers we will import the useDispatch hook inside our Products.js component.


```javascript!
import { useDispatch } from 'react-redux'
import { add } from '../Store/cartSlice'

const dispatch = useDispatch()
    const handleAdd = (product) => {
        dispatch(add(product))
    }
    
    <button onClick={() => handleAdd(product)} className='btn'>Add to cart</button>
```

After this add `{items.length}` in your Cart Items `<span className='cartCount'>Cart items:{items.length}</span>`

The number of cart items will increase on the `Add to cart` button.

![](https://hackmd.io/_uploads/H1CteEcAn.png)

When you open the Redux dev tool in your browser, go to 'State' where you will see the cart inside 'Tree', and 'Chart'.

Whenever you add an item the data related to that product is added to the cart as you can see in the image.

![](https://hackmd.io/_uploads/H1UC-EqCn.png)

Redux is predictable because you can have control of every step that you are doing. You see the scroll bar in the image shown below, using that scroll bar you can control every step.

![](https://hackmd.io/_uploads/B1GDXN90n.png)

### Cart page

The data will be passed the same way we passed the product length in our cart items.

We want product images, prices, and titles to be displayed on our cart page. And also we will add a remove button to remove any product from our cart. 

Add remove reducer inside our cartSlice in your store.

`cartSlice.js`

This reducer will return and filter out from the state that has some products. Wherever the data doesn't match return it and remove the data that matches. Also, export remove reducer the way we did add reducer.

```javascript=
remove(state , action){
            return state.filter((item)=> item.id !== action.payload)
        }
```

`Cart.js`

```javascript=
import React from 'react'
import {useSelector , useDispatch} from 'react-redux'

import { remove } from '../Store/cartSlice'

const Cart = () => {
  const items = useSelector((state)=> state.cart)
  const dispatch = useDispatch()


  const handleRemove =(itemId)=>{
       dispatch(remove(itemId))
  }
  return (
  
    <div>
      <div className='cartWrapper'>

{
  items.map((item)=>(
    <div className='cartCard'> 
       <img src={item.image}></img>
       <h5>{item.title}</h5>
       <h5>Price : ${item.price} </h5>

       <button className='remove-btn' onClick={()=> handleRemove(item.id)}>Remove Item</button>
    </div>
  ))
}
</div>
        <h1>This is Cart page.</h1>

    </div>
  )
}

export default Cart
```