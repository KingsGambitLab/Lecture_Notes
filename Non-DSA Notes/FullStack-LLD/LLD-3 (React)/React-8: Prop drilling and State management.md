# React 8 Prop Drilling and Context API


### Agenda 

1. We will understand the problem of prop drilling
2. We will overcome prop drilling by using context API
3. We will discuss useRef hook
4. We will discuss useMemo hook(you should have a basic knowledge of memorisation) 


### Prop drilling 

When you have a piece of specific information that is required at a specific component but to reach that specific component you will have to go through all the components that are one level up the hierarchy. 

To understand this in a better way let's take an example of a family tree where the family wants to pass on information to their granddaughter but they will have to pass the information first to the parents then to the children and in the end, the information will reach the granddaughter as shown in the image.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/503/original/Screenshot_2023-09-20_172236.png?1695210781)

Now if we replace the family with the components the tree will look something like this.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/504/original/Screenshot_2023-09-20_172248.png?1695210795)

In the above image, the prompt: "message:'Hi'" should reach component E but it will have to go through component B and component D as well. Here, one level up is Component D then Component B and then Component A. So, this problem is known as prop drilling. 


**Example**


To understand the issue with prop drilling, let's create a React APP with the name Context and then create one folder named "prop_drill" inside the source (src) folder. Inside the folder prop_drill, we will add all the components that are going to be used to replicate the family tree we saw above as an example. Inside the prop_drill folder make five files named 'family.js', 'parents.js', 'children.js', 'grandson.js' and 'granddaughter.js'.

First, create a `family.js` component by importing the react function component export.

```javascript!
import React from 'react';

function Family(){
    return{
        <div>Family</div>
    }
}

export default Family
```


Now, add the family component inside the `app.js` file.

```javascript!
import logo from './logo.svg';
import './App.css';
import Family from './prop_drill/Family';

function App() {
  return (
    <div className="App">
      <Family/>
    </div>
  );
}

export default App;
```

In the app.css file, simple CSS code is added to make the hierarchical family tree.

```css!
/*app.css file */
.family{
  display: flex;
  justify-content: left;
  margin: 1rem;
}

.parent{
  border: 5px solid #000;
  padding: 0.5rem;
}

.children{
  border: 3px solid #ff5722;
  padding: 0.5rem 0 0 1em;
}

.gson{
  border: 2px solid #3f51b5;
  padding: 0.5rem 0 0 1.5rem;
  margin: 0.2rem;
}

.gdaughter{
  border: 2px solid #e929ad;
  padding: 0.5rem 0 0 1.5rem;
  margin: 0.2rem;
}
```

Now, we will create a class of family inside the family.js file and also import the Parent file.

```javascript!
import Parent from './Parent';

const Family = () => {
  return (
    <div className='family'>
      <Parent/>
    </div>
  );
}

export default Family
```

Add the following program in the Children.js file.

```javascript!
import GrandDaughter from "./GrandDaughter";
import GrandSon from "./GrandSon";


const Children = () => {

    return(
        <div className="children">
            <h2>Children</h2>
            <GrandSon/>
            <GrandDaughter/>
        </div>
    );
}

export default Children;
```

After executing the above programs when we run the `npm start` command for our app the result will look like this:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/505/original/Screenshot_2023-09-20_172333.png?1695210819)

Now let's create the remaining two files of grandson and granddaughter as well:

```javascript!
// grandson.js
const GrandSon = () => {

    return(
        <div className="gson">
            GrandSon
        </div>
    );
}

export default GrandSon;
```

```javascript!
//granddaughter.js
const GrandDaughter = () => {

    return(
        <div className="gdaughter">
            GrandDaughter
        </div>
    );
}

export default GrandDaughter;
```

As you can see in app.js we have added a parent component and in parent.js we have added a children component. Same way to create heirarchy we have added both grandson and granddaughter in children.js.

The result will look something like this after executing the code:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/506/original/Screenshot_2023-09-20_172355.png?1695210842)


Now, let's pass the information from one component to the granddaughter component. For that, create an object in the app.js file inside the function or outside the function.

```javascript!
const familyInfo = {
  familyName: "The Griffins",

  onlyForParents : () => {
    console.log("Info for Parents");
  },

  onlyForGrandChildren : () => {
    console.log("Info for GrandChildren");
  }
}
```

**[Ask the learners]**
How will you pass the familyInfo object in the family component?
-> **By passing prompts** We will pass info prompt inside we will pass familyInfo.

```javascript!
function App() {
  return (
    <div className="App">
      <Family info={familyInfo}/>
    </div>
  );
}
```
Now, the family component will have access to the familyInfo. For that, we need to destructure the info prompt from app.js.

```javascript!
const Family = ({info}) => {
  return (
    <div className='family'>
      <Parent/>
    </div>
  );
}
```

Now, let's console log parentInfo.familyName from the parent.js file.

```javascript!
import Children from './Children'

const Parent = ({parentInfo}) => {
    console.log('This is from parents:',parentInfo);
    return (
        <div className="parent">
           <h1>{`Parent ${parentInfo.familyName}`}</h1>
           <Children/>
        </div>
    );
}

export default Parent;
```

The result will look something like this:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/507/original/Screenshot_2023-09-20_172422.png?1695210868)

Let's invoke `onlyForParents` in Parent.js.

```javascript!
<p>{parentInfo.onlyForParents()}</p>
```
To show the result on the screen, remove console.log from onlyForParents and also from onlyForGrandChildren then add a return statement. 

**Result**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/508/original/Screenshot_2023-09-20_172442.png?1695210891)

The information from parents is now to be passed on to Children. To do that the same steps are followed from family to parents.

```javascript!
const Children = ({childrenInfo}) => {

    return(
        <div className="children">
            <h2>{`Children ${childrenInfo.familyName}`}</h2>
            <GrandSon/>
            <GrandDaughter/>
        </div>
    );
}
```

The family name is to be passed on to the grandchildren. It will also follow the same process.

`grandSon.js`

```javascript!
const GrandSon = ({grandSonInfo}) => {

    return(
        <div className="gson">
            <h3>{`GrandSon ${grandSonInfo.familyName}`}</h3>
        </div>
    );
}

export default GrandSon;
```

`grandDaughter.js`

```javascript!
const GrandDaughter = ({grandDaughterInfo}) => {

    return(
        <div className="gdaughter">
        <h3>{`GrandDaughter ${grandDaughterInfo.familyName}`}</h3>
        </div>
    );
}

export default GrandDaughter;
```

`children.js`

```javascript!
import GrandDaughter from "./GrandDaughter";
import GrandSon from "./GrandSon";


const Children = ({childrenInfo}) => {

    return(
        <div className="children">
            <h2>{`Children ${childrenInfo.familyName}`}</h2>
            <GrandSon grandSonInfo = {childrenInfo}/>
            <GrandDaughter grandDaughterInfo = {childrenInfo}/>
        </div>
    );
}

export default Children;
```

**Result**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/509/original/Screenshot_2023-09-20_172506.png?1695210912)

Passing the information onlyForGrandChildren.

`grandSon.js`
```javascript!
<div className="gson">
        <h3>{`GrandSon ${grandSonInfo.familyName}`}</h3>
        <p>{grandSonInfo.onlyForGrandChildren()}</p>
</div>
```

`grandDaughter.js`

```javascript!
<div className="gdaughter">
    <h3>{`GrandDaughter ${grandDaughterInfo.familyName}`}</h3>
    <p>{grandDaughterInfo.onlyForGrandChildren()}</p>
</div>
```

**Result**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/510/original/Screenshot_2023-09-20_172527.png?1695210933)

As we can see the information was passed on from one component to another. Here, the components were very few. If the components are more than 10 it will not be a tedious task and will be more prone to errors.

*To overcome this, the concept of Context API was introduced.*



### Context API

Context is a global state that can have the data the developer wants to pass to all the other components.

Let's understand it with the same example of family.
So, in a family where we were passing the information from component to component, we will create a context in component A i.e., family. The context will contain the message which will be available globally and could be accessed by any component without passing from one component to another.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/511/original/Screenshot_2023-09-20_172547.png?1695210954)

The context works as a provider and all the other components will work as consumers.

**Example**

Let's use the example of family and code using context API. For that, create a new folder inside your source folder with the name ContextComponents (the same way as already done in the above example of prop drilling). Inside this folder create the same files as were already created inside prop_drill.

Also, copy the code for all the js files created which will be rendered.

We will create a context for the family as it is the topmost component after `app.js`. For that, create a new file `FamilyContext.js` where the context will be created. To create a context there is already an inbuilt method named `createContext` in React. The FamilyContext can be imported into your app.js file.

```javascript!
//FamilyContext.js
import React, { createContext } from "react";

//the variable familycontext becomes a context
export const FamilyContext = React.createContext()
```

After importing FamilyContext in your app.js file, we can actually wrap the FamilyC component inside the FamilyContext. And we can pass down the value by just passing the value property inside the FamilyContext tag. Also, remove prompts from files. We have to add a provider with the context as it is a provider and the other components are consumer.

`ParentsC.js`

```javascript!
import ChildrenC from './ChildrenC';
import { FamilyContext } from './FamilyContext';
import { useContext } from 'react';

const ParentsC = () => {
    const parentInfo = useContext(FamilyContext);
    console.log(parentInfo);
    return (
        <div className="parent">
           <h1>{`Parent ${parentInfo.familyName}`}</h1>
           <p></p>
           
        </div>
    );
}

export default ParentsC;
```

`app.js`

```javascript!
function App() {
  return (
    <div className="App">
      <FamilyContext.Provider value = {familyInfo}>
          <FamilyC/>
      </FamilyContext.Provider>
      
    </div>
  );
}
```
After the console log the result comes out using the context.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/512/original/Screenshot_2023-09-20_172612.png?1695210981)

In the same way, it can be done for both children and grandChildren.

`GrandSon.js`
```javascript!
import { useContext } from "react";
import { FamilyContext } from "./FamilyContext";
const GrandSonC = () => {
    let grandSonInfo = useContext(FamilyContext)
    return(
        <div className="gson">
            <h3>{`GrandSon ${grandSonInfo.familyName}`}</h3>
            <p></p>
        </div>
    );
}

export default GrandSonC;
```

`GrandDaughter.js`

```javascript!
import { useContext } from "react";
import { FamilyContext } from "./FamilyContext";

const GrandDaughterC = () => {
    let grandDaughterInfo = useContext(FamilyContext)
    return(
        <div className="gdaughter">
        <h3>{`GrandDaughter ${grandDaughterInfo.familyName}`}</h3>
        <p>{grandDaughterInfo.onlyForGrandChildren()}</p>
        </div>
    );
}

export default GrandDaughterC;
```

`Children.js`

```javascript!
import { FamilyContext } from "./FamilyContext";
import { useContext } from "react";
import GrandSonC from "./GrandSonC";
import GrandDaughterC from "./GrandDaughterC";
const ChildrenC = () => {
    const childrenInfo = useContext(FamilyContext)
    return(
        <div className="children">
            <h2>{`Children ${childrenInfo.familyName}`}</h2>
            <GrandSonC/>
            <GrandDaughterC/>
        </div>
    );
}

export default ChildrenC;
```

**Result**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/513/original/Screenshot_2023-09-20_172650.png?1695211017)

As we can see, we got the same results using both prop drilling and context API. But, in Context API we didn't use any prompts instead we just passed the context by importing in our components.

> The context is an orchestrator or a centralized place where related elements within a hierarchy can access data from another element within the same hierarchical scope.

You can go through this [article](https://www.smashingmagazine.com/2020/01/introduction-react-context-api/) for more information.



### useRef Hook

Let's understand what is useRef and why is it important using an example.

Create a new component and name it Ref inside your ContextComponents folder.

`Ref.js`
```javascript!
import React, { useState } from "react";

function Ref() {
    const [name, setName] = useState("Alex");
    
    function clear(){
        setName('')
    }
    return(
        <>
            <h1>UseRef</h1>
            <input type="text" value={name} onChange = {(e) => setName(e.target.value)}>

            </input>
            <button onClick={() => clear()}> Clear</button>
        </>
    );
        
}

export default Ref;
```

Add this Ref component in the App.js file (comment out the div element).

**Result**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/514/original/Screenshot_2023-09-20_172712.png?1695211038)

In the result, we see that a blue outline is visible at the border of the text box even though there is no code added. But as soon as we click on the clear button, the blue border is also removed, basically all the focus is removed from the text box. Here, we do not want the focus should be moved from the input box or textbox.

UseRef Hook allows you to access DOM properties inside React which returns an object. The object contains a key known as "current" where you can set anything inside it. This key will allow you to manipulate that particular element with respect to the DOM.

So in the above code, we will use the useRef hook. This useRef will allow you to get the input object inside the `current` key. In HTML, we have access to the `ref` attribute which stands for Reference.

```javascript!
function Ref() {
    const [name, setName] = useState("Alex");
    
    function clear(){
        setName('')
        RefElement.current.focus()
    }

    let RefElement = useRef('')
    console.log(RefElement);
    return(
        <>
            <h1>UseRef</h1>
            <input ref ={RefElement} type="text" value={name} onChange = {(e) => setName(e.target.value)}>

            </input>
            <button onClick={() => clear()}> Clear</button>
        </>
    );      
}
```

In the above code, we are setting the key default input as an empty string for the `current` key. The reference is set for the input field. As we don't want to move the focus from the input field we will add the RefElement in the clear() function and use the DOM method focus().

**Result**

![](https://hackmd.io/_uploads/H1f5VJHR3.png)

In the result, we can see even if we click on the clear button the focus from the input field is not moved.

Let's take another example where we want to change the text colour as well.

To do that create another button and name it Change Color. Make a function with the name changeColor() add the RefElement we created and use the DOM properties for changing the color.

```javascript!
function changeColor(){
        RefElement.current.style.color = 'Pink'
    }

<button onClick={() => changeColor()}> Change Color</button>
```

**Result**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/515/original/Screenshot_2023-09-20_172733.png?1695211059)

You can read the following article on [Medium](https://medium.com/trabe/react-useref-hook-b6c9d39e2022) to understand useRef Hook better.
--

### useMemo

In dynamic programming, there's a step called Memoization. Memoization means to have a temporary memory area where things get stored so that no function calls are made instead we can go there and get the value and use that value. Same way it works for React too.

Let's take a very simple example where we will get the factorial of numbers.
Create a new file named `Factorial.js` inside the ContextComponents folder.

```javascript!
import React, { useState } from 'react'

function Factorial() {

    const [number, setNumber] = useState(1)
    const [inc, setInc] = useState(0)
    
    const onChange = (event) =>{
        setNumber(Number(event.target.value))
    }

    const onClick = () => {
        setInc(i=>i+1)
    }
    let factorial = factorialOf(number)
  return (
    <div>
    <span>Factorial of - </span> 
    <input type= 'number' value={number} onChange={onChange}></input>
    <span>Factorial Value: {factorial} </span>

    <button onClick={onClick}>re-render</button>
    </div>
  )
}

function factorialOf(n){
    console.log('Factorial function called: ')

    return n<=0 ?1: n* factorialOf(n-1)
}

export default Factorial
```

The above code is not optimised as there are so many function calls when we try to increase the value. Why? Because with each increasing number, we are calling the function again and again. Also, the number of function calls increases while clicking on re-render as you can see in the image.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/516/original/Screenshot_2023-09-20_172755.png?1695211082)

The re-render button takes the input number and calculates the factorial again because we do not have the value of the factorial already set. That means on clicking the button it calls the function again and again which is not optimised. To overcome this, we will use **useMemo Hook** which is similar to `useEffect` where we do not try to update the state again and again. We update the state only when there's a dependency.

Similarly, there's `useMemo` that is used to memoize the function. It accepts the function that you need to memoize and also comes with the condition of when you want to call the function.

In the above example, we need to memoize the factorial function. To do that use the `useMemo` hook.

```javascript!
const factorial = useMemo(() => factorialOf(number),[number])
```

After running the program, we see that even if we click on the re-render button the function is not called. It is only called when changing the values. The value that was already there is being memoized.

You can refer to this [article](https://dmitripavlutin.com/react-usememo-hook/) to understand useMemo Hook.