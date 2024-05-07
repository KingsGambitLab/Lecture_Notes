

# Component Architecture
- Component is a section of an architecture.
- When we divide the complete projects into small sections then that architecture is known as component architecture. 
- Every section of an architecture is a separate section in itself.

**Example:**
Let us take an example of LinkedIn, in the LinkedIn search box, news, connections, etc. all are different sections, which are built separately but they work together.

## Creating Components
- Everything written in the app.js is rendered on the website.

Here let us take an example of a demo component before creating our component:
```javascript=
function App(){
    return {
        <div>
            <h1> Hello from react</h1>
        </div>
    };
}
export default App
```

- Components that are created with function are known as functional components.
- Here is a function with the name `App` and this function returns a `div` which contains the `h1` tag.



### Functional Component 
You can define a Javascript function and from that function, you can return JSX code and that function will be able to accept props.

**Props** is an object that can have different values for every component.

**JSX:** is a way of writing Javascript and HTML together.


**Creating First Component:**
1. Inside `src`, we will create a folder named `components`.
2. Let us create the first component inside this folder with the name `MyComponent.js`.
3. **Component names always start with a capital letter.**
4. Now open `MyComponent.js`, now we will create a functional component here with the name `MyComponent`.
5. We will create a function with the name `MyComponent`.

```javascript=
function MyComponent(){
    
}
```

6. This function simply returns a `div` with a `h1`.


```javascript=
function MyComponent(){
    return{
        <div>
            <h1> My first component </h1>
        </div>
    }
}
```

7. Now we need to export this component using the `export` keyword.

```javascript=
function MyComponent(){
    return{
        <div>
            <h1> My first component </h1>
        </div>
    }
}
export default MyComponent
```

Here `default` ensures that this component can be used anywhere inside the app.

8. Now we need to import the component inside the main component i.e. `app.js`.
9. We need to write the below line inside `app.js` to import `MyComponent`.

```javascript=
import MyComponent from './components/MyComponent';
function App(){
    return {
        <div>
            <h1> Hello from react</h1>
        </div>
    };
}
export default App
```

10. Now we will use `MyComponent` inside the `App` component of the `App.js` file.

```javascript=
import MyComponent from './components/MyComponent';
function App(){
    return {
        <div>
            <h1> Hello from react</h1>
            <MyComponent/>
        </div>
    };
}
export default App
```


**Creating Second Component**

1. Create a file name `MyComponent2.js` inside the `components` folder.
2. Open the `MyComponent2.js` file.
3. Now type `rfce` to create a functional component automatically.
4. Here `rfce` stands for react functional component export.
5. After typing `rfce` press enter, and then a functional component is created automatically.
6. And below code will appear automatically.

```javascript=
import React from 'react'
function MyComponent2(){
    return{
        <div>MyComponent2</div>
    }
}
export default MyComponent2
```

7. Now we just have to write our content inside this component.
```javascript=
import React from 'react'
function MyComponent2(){
    return{
        <div>
            <h3>this is my component2</h3>
        </div>
    }
}
export default MyComponent2
```


8. Now we can import MyComponent2 in `app.js` by writing the below line inside `app.js` to import `MyComponent2`.

```javascript=
import MyComponent2 from './components/MyComponent2';
import MyComponent from './components/MyComponent';
function App(){
    return {
        <div>
            <h1> Hello from react</h1>
            <MyComponent/>
        </div>
    };
}
export default App
```

9. Now we will use `MyComponent2` inside the `App` component of the `App.js` file.

```javascript=
import MyComponent2 from './components/MyComponent2';
import MyComponent from './components/MyComponent';
function App(){
    return {
        <div>
            <h1> Hello from react</h1>
            <MyComponent/>
            <MyComponent2/>
        </div>
    };
}
export default Appexport default App
```

10. We can see that we can use multiple components in a single app component.




# JSX
- JSX is not HTML. We can use also javascript inside it.

**Always write javascript code above the return statement.**

Let us take an example of the `MyComponent.js` file.

1. Open `MyComponent.js` file.
2. Declare one javascript variable inside it.

```javascript=
function MyComponent(){
    const name = 'Steve'
    return{
        <div>
            <h1> My first component </h1>
        </div>
    }
}
export default MyComponent
```

3. We can use this javascript variable inside the return statement.


```javascript=
function MyComponent(){
    const name = 'Steve'
    return{
        <div>
            <h1> My name is {name} </h1>
        </div>
    }
}
export default MyComponent
```

4. Now the value of the name variable i.e. `Steve` will be displayed in output.
5. This is only possible due to **JSX**, which allows us to combine JavaScript with HTML, as it is not possible with HTML only.
6. As we defined variable in javascript, we can also define a function, which can be called.\


```javascript=
function MyComponent(){
    const name = 'Steve'
    const showMessage =()=>{
        return 'hello this is a message from showMessage function'
    }
    return{
        <div>
            <h1> My name is {name} {showMessage()} </h1>
        </div>
    }
}
export default MyComponent
```

7. Now the value returned by the function is always displayed in output.




# Component Reusability
- Components can be reused in react.
- And according to our use case we can pass and modify data by something called **props** and **state**.


**Reusing a component:**
We can use a single component multiple times.

```javascript=
import MyComponent2 from './components/MyComponent2';
import MyComponent from './components/MyComponent';
function App(){
    return {
        <div>
            <h1> Hello from react</h1>
            <MyComponent/>
            <MyComponent/>
            <MyComponent/>
            <MyComponent/>
            <MyComponent2/>
        </div>
    };
}
export default App
```

As in this, all the components have the same data, we can use the same component again and again but we can also pass different data to component by **props.**

## Props
- Props stands for properties.
- And every component can have different properties.

1. Let us create a new component `UserProfile`, and create a file `UserProfile.js` inside the components folder.
2. Now inside `UserProfile.js` write `rfce` and press enter and then write our content.

```javascript=
import React from 'react'
function UserProfile(){
    return{
        <div>
            <h3>Name: Steve, Age: 25, Occupation: Software Engineer</h3>
        </div>
    }
}
export default UserProfile
```

3. Now import this component in `app.js` file.


```javascript=
import UserProfile from './components/UserProfile';

function App(){
    return {
        <div>
            <UserProfile/>
        </div>
    };
}
export default App
```

4. Now we want to reuse the `UserProfile` component.
5. Now we will use props.
6. And we will access props using the key inside it.

```javascript=
import React from 'react'
function UserProfile(props){
    return{
        <div>
            <h3>Name: {props.name}, Age: {props.age}, Occupation: {props.occupation}</h3>
        </div>
    }
}
export default UserProfile
```

7. And then we will pass different values for calling the component.


```javascript=
import UserProfile from './components/UserProfile';

function App(){
    return {
        <div>
            <UserProfile name='Steve' age={25} occupation='Software Engineer'/>
            <UserProfile name='John' age={35} occupation='Civil Engineer'/>
            <UserProfile name='Mark' age={40} occupation='Businessmen'/>
        </div>
    };
}
export default App
```

**Integer value always passed in {}**
Now we can see that we are using the same component three times with different data. So our output will be something like this.

![](https://hackmd.io/_uploads/r1Ppvg-02.png)




# Disadvantages of Props
**Props are immutable**, which means we can not change it at the component level.
Whatever value is coming from the main component, we need to use only that value, we can not change it inside the component.



# State
- There are two types of components in react, one is a class-based component and another is a functional component.
- Functional component is also known as state-less component, but **hooks** are introduced that allow functional components to have access to state and other React features.



# Hooks
Hooks are introduced that allow functional components to have access to state and other React features.
The first hook is `useState`.




# Event handling
We just want to create a button, we want that when that button is clicked then a message is displayed on the console.

1. Let us create a new component named `Event.js`, so create a file named `Event.js` inside the components folder.
2. Inside this component we will create a button.

```javascript=
import React from 'react'
function Event(){
    return{
        <div>
            <h1> Event handling</h1>
            <button>click me</button>
        </div>
    }
}
export default Event
```

2. We need to import this component inside the `App` component.

```javascript=
import Event from './components/Event';

function App(){
    return {
        <div>
            <Event/>
        </div>
    };
}
export default App
```

3. Now for performing event handling(when the button is clicked then a message is displayed on the console), we will create a function inside the `Event` component.

```javascript=
import React from 'react'
function Event(){
    const handleClick=()=>{
        console.log('Button was clicked')
    }
    return{
        <div>
            <h1> Event handling</h1>
            <button>click me</button>
        </div>
    }
}
export default Event
```

4. Now we need to call this function on the `onClick` event of the button.

```javascript=
import React from 'react'
function Event(){
    const handleClick=()=>{
        console.log('Button was clicked')
    }
    return{
        <div>
            <h1> Event handling</h1>
            <button onClick={handleClick}>click me</button>
        </div>
    }
}
export default Event
```

5. Now when we click on this a message is displayed on the console.




# Hooks
- **Functional component are stateless component**, means it does not has any state,
- **Class Based components are stateful components.**


**Hooks are there to implement all the functionality of the state in the functional component.**

First, we will learn the `useState` hook.



# useState
We will create a simple application, which has two buttons one button will increment the value and another button will decrement the value.

1. We will create a component named `Counter`, so create a file named `Counter.js` inside the components folder.
2. Inside `Counter.js`, write `rfce` and press enter.

```javascript=
import React from 'react'
function Counter(){
    return{
        <div>
            <h1> Counter</h1>
            
        </div>
    }
}
export default Counter
```

3. Import the `Counter` component inside the `App` component.


```javascript=
import Counter from './components/Counter';

function App(){
    return {
        <div>
            <Counter/>
        </div>
    };
}
export default App
```

4. Now we will create two buttons inside the `Counter` component one for increment and another one for decrement, and we will also display the count in the `Counter` component.

```javascript=
import React from 'react'
function Counter(){
    return{
        <div>
            <h2>The count value is</h2>
            <button>Increment</button>
            <button>Decrement</button>
        </div>
    }
}
export default Counter
```

5. **useState hook is a function that is inbuilt react, and it will give two values one value is variable and another value is function.**
6. First we need to import `useState`.

```javascript=
import React from 'react'
import {useState} from 'react'
function Counter(){
    return{
        <div>
            <h2>The count value is</h2>
            <button>Increment</button>
            <button>Decrement</button>
        </div>
    }
}
export default Counter
```


## Syntax of useState
```javascript=
const[variable, function]=useState()
```

Whatever value is passed inside the useState that will be used for initialization of the variable, like in the below example variable will be initialized with 0.


```javascript=
const[variable, function]=useState(0)
```

7. Inside our functional component, we will use `useState`, and initialize count by 0.

```javascript=
import React from 'react'
import {useState} from 'react'
function Counter(){
    const[count, setCount] = useState(0)
    
    return{
        <div>
            <h2>The count value is </h2>
            <button>Increment</button>
            <button>Decrement</button>
        </div>
    }
}
export default Counter
```

8. We will create increment and decrement functions, and call those functions on the `onClick` event of buttons.

```javascript=
import React from 'react'
import {useState} from 'react'
function Counter(){
    const[count, setCount] = useState(0)
    function increment(){
        setCount(count+1)
    }
    function decrement(){
        setCount(count-1)
    }
    return{
        <div>
            <h2>The count value is </h2>
            <button onClick={increment}>Increment</button>
            <button onClick={decrement}>Decrement</button>
        </div>
    }
}
export default Counter
```

9. We will display this `count` value inside h2.

```javascript=
import React from 'react'
import {useState} from 'react'
function Counter(){
    const[count, setCount] = useState(0)
    function increment(){
        setCount(count+1)
    }
    function decrement(){
        setCount(count-1)
    }
    return{
        <div>
            <h2>The count value is {count}</h2>
            <button onClick={increment}>Increment</button>
            <button onClick={decrement}>Decrement</button>
        </div>
    }
}
export default Counter
```

Now if we see the output our count value is initially displayed as 0, and when we click the increment button, the value will increment, and then the incremented value will be displayed, and when we click the decrement button, then the value will decrement, and then the decremented value will be displayed,

10. We can also set the condition that the count will not be decremented only if its value is 0.

```javascript=
import React from 'react'
import {useState} from 'react'
function Counter(){
    const[count, setCount] = useState(0)
    function increment(){
        setCount(count+1)
    }
    function decrement(){
        if(count===0){
            setCount(count)
        }
        else{
            setCount(count-1)
        }
    }
    return{
        <div>
            <h2>The count value is {count}</h2>
            <button onClick={increment}>Increment</button>
            <button onClick={decrement}>Decrement</button>
        </div>
    }
}
export default Counter
```




# Destructuring
- destructuring values inside the props.
- Props is an object, that has a key-value pair.
- Now we will do destructuring inside the `UserProfile` component.



```javascript=
import React from 'react'
function UserProfile(props){
    // destructuring
    const {name, age, occupation} = props
    return{
        <div>
            <h3>Name: {props.name}, Age: {props.age}, Occupation: {props.occupation}</h3>
        </div>
    }
}
export default UserProfile
```

- Now we can access values directly by the variable.

```javascript=
import React from 'react'
function UserProfile(props){
    // destructuring
    const {name, age, occupation} = props
    return{
        <div>
            <h3>Name: {name}, Age: {age}, Occupation: {occupation}</h3>
        </div>
    }
}
export default UserProfile
```


- We can also do destructuring in this way.

```javascript=
import React from 'react'
function UserProfile({name, age, occupation}){
    return{
        <div>
            <h3>Name: {name}, Age: {age}, Occupation: {occupation}</h3>
        </div>
    }
}
export default UserProfile
```


# DOM

- DOM is a tree.

![](https://hackmd.io/_uploads/SJwxcbZA2.png)

- **DOM Manipulations/Operations:** In these elements we can perform some operations, like remove them, add them, insert some data inside them, etc.

- When the DOM manipulation happens, then the whole DOM gets rerendered.

- **Re-Rendering:** When we change anything in a single element, then the whole tree is re-rendered.
- And re-rendering of the whole DOM is not so good, it makes the application slow.
- **To overcome this problem, react introduced virtual DOM.**


# Virtual DOM

Virtual DOM is in memory copy of actual DOM.
- Let us assume we have a real DOM.

![](https://hackmd.io/_uploads/ryDwiWW03.png)


- Now react will create a copy of this DOM.

![](https://hackmd.io/_uploads/H1odobZCh.png)

- Now whenever any change happens in any particular element, then react will first make changes in the virtual DOM, it will not do changes directly in the real DOM.
- Let us assume a `h2` element is changed, then react will do these changes in virtual DOM.

![](https://hackmd.io/_uploads/SJPZ3b-C2.png)

- Now again any other changes happen in any element, let us suppose the `p` element is changed.
- So React will make changes in another virtual DOM.

![](https://hackmd.io/_uploads/Bycr3ZZR3.png)

- **React will keep a record of all the changes and keep creating a virtual DOM at every change.**
- And last virtual DOM has all the changes.
- So according to the final/last virtual DOM, it will re-render the real DOM only once. This process that virtual DOM follows is known as **batch processing.**

And whole process of creating a virtual DOM at every updation, keeping a copy of every virtual DOM and re-rendering the real DOM once is known as **Reconcillation**.
And algorithm used by virtual DOM to compare all the virtual DOMs is known as **diffing algo**
