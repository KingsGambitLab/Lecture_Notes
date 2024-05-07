## Full Stack LLD & Projects: React -10: React Redux Interview Question 2


**Agenda of this lecture:**

* Code splitting
* Lazy loading
* Higher order components
* Controlled and Uncontrolled components



### Explanation

Before jumping into code splitting we will first understand the concept of **bundling** in react.

A React application can have multiple components, each spread across different JavaScript files. When you build the application, you want to bundle these separate files into a single file for optimized delivery to the browser. Webpack is a popular tool used for this purpose. It takes all your application's code, along with its dependencies, and packages them into a single bundle file, which is efficient for loading and executing in the browser.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/537/original/Screenshot_2023-09-20_183604.png?1695215370)

Webpack helps with bundling in a React application by efficiently combining multiple JavaScript files and assets into a single bundle. It optimizes resource delivery, reduces HTTP requests, and enhances the application's loading performance.

### Code splitting

Code splitting is a technique that allows a React application to break its code into smaller, separate files or "chunks." Instead of loading the entire application code upfront, only the necessary code is loaded when a specific feature or route is accessed. This improves initial loading times and resource efficiency, enhancing the overall user experience.

Code splitting is like fetching ingredients from the fridge only when you need them to make a sandwich. In React, it means loading parts of your application's code on-demand, improving performance by reducing initial load times and resource usage.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/538/original/Screenshot_2023-09-20_183611.png?1695215389)



First lets see how data is split and then we will see how react components can be split:-

**Splitting of Data:**


The `data.js` looks like this:-

```javascript 
export const moviesData = [{
    id : '1',
    name : 'Mission Impossible : Dead reckoning'
},
{
    id : '2',
    name : 'Oppenhiemer'
},
   {
    id : '3',
    name : 'Barbie'
   }
]
```

When you bundle your code, it combines all the imported modules, like data.js, into one optimized file. This makes it easier to manage and deploy your application because you only need to serve a single bundle file to the client browser.

In this the data is split using **dynamic importing** in JavaScript. Instead of loading the movie data immediately, the `getMovies` function uses the `import()` function to fetch the data from a separate file called data.js when needed. This is a form of code splitting, as it loads the data module only when required, which can help optimize performance by reducing the initial load time of your application.


### Explanation

Bundling of react components is done using **Lazy Loading**.

React components are bundled using Lazy Loading. Lazy Loading is a technique that allows you to load components only when they are needed, rather than upfront when the application initially loads.

Here's how it works:

* Each component (`Home`, `Products`, `Testimonials`, and `About`) is imported using the `lazy()` function, which dynamically imports the component files when they are required.
* This means that the code for these components is split into separate chunks and loaded on-demand, reducing the initial load time of your application.
* Lazy Loading helps optimize performance by loading only the necessary components when the user navigates to specific routes, improving the user experience and minimizing unnecessary network requests.

```javascript 
const Home = lazy(()=> import('./pages/Home'))
const Products = lazy(()=> import('./pages/Products'))
const Testimonials = lazy(()=> import('./pages/Testimonials'))
const About = lazy(()=> import('./pages/About'))
```

Now we will wrap the routes:-

The lazy loading of components is related to how routes are wrapped using React's Suspense and React Router's Routes components.

the lazy loading of components is related to how routes are wrapped using React's Suspense and React Router's Routes components.

* **Suspense:** The `<Suspense>` component is used to specify a fallback UI (in this case, `<h2>Loading...</h2>`) while waiting for dynamically imported components to load. It's a key part of lazy loading as it ensures a smooth user experience by displaying a loading indicator until the requested component is ready.
* **Routes:** Inside the `<Routes>` component, various routes are defined, and each route specifies a component to render when the corresponding URL is matched. These components, such as `<Home />`, `<About />`, `<Products />`, and `<Testimonials />`, are dynamically imported using lazy loading. This means that the components will only be loaded from the server when their respective routes are accessed by the user.

```javascript 
return (
    <div className="App">
      {/* <h1>These are the Movies</h1>
      <button onClick={getMovies}>Show Movies</button>
      <p>{movies.length>0 ? JSON.stringify(movies) : ''}</p> */}

      {/* <Suspense fallback={<h2>Loading...</h2>}>
       <BrowserRouter>

        <Navbar/>
    
       <Routes>

        <Route path='/' element={<Home/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/products' element={<Products/>}/>
        <Route path='/testimonials' element={<Testimonials/>}/>
       </Routes>
     
       
       </BrowserRouter>
       </Suspense> */}

       {/* <CompA/>
       <CompA dark />
       <CompA yellow/> */}


       <Controlled/>
       <Uncontrolled/>
     

      
    </div>
  );
```


### Explanation


High Order Components (HOCs) are a design pattern in React that allows you to reuse component logic and share it among multiple components. HOCs are not components themselves but functions that take a component and return a new enhanced component with additional behavior. They are a way to abstract common functionality from components and promote code reusability.

Let's use three components, A, B, and C, each with different features, to illustrate the concept:

1. Component A (3 features)
Component A is a base component with three specific features: FeatureX, FeatureY, and FeatureZ.
Component B (4 features)
2. Component B also requires the same three features as Component A (FeatureX, FeatureY, FeatureZ) and an additional feature, FeatureW.
Component C (5 features)
3. Component C needs the same three features as Components A and B (FeatureX, FeatureY, FeatureZ), plus two extra features, FeatureV and FeatureU.

```javascript 
import React from 'react'


const styles = {
    dark : {
        background : 'black',
        color : 'white'
    } ,

    yellow : {
        background : "yellow",
        color : 'red'
    }
}

function HOC(WrappedComp) {

    // args = [dark  ,yellow]
  return function (args){
    let temp ={}

    if(args.dark){
        temp = {...styles.dark}
    }

    else if (args.yellow){
        temp = {...styles.yellow}
    }

    let obj = {...args , style : temp}

    return <WrappedComp {...obj}/>

  }
}

export default HOC
```

This code defines a Higher Order Component (HOC) that takes another component, WrappedComp, as an argument and returns an enhanced version of it with additional styling based on the provided arguments (dark or yellow).

* The styles object contains predefined styles for both 'dark' and 'yellow' modes.
* The HOC function takes `WrappedComp` as an argument and returns a new function.
* Inside this function, it checks whether the args object contains a 'dark' or 'yellow' property.
* Depending on the property found, it applies the corresponding styles to temp.
* The style property is added to the args object with the selected styles.
* Finally, the `WrappedComp` is rendered with the updated args containing the chosen styles.


### Explanation

**Controlled Components:** Controlled components are React components where the value of an input element is controlled by the component's state. In this given below  example, the `Controlled` component maintains the value of the input field (text) in its state and updates it through the `onChange` event handler. This ensures that the input's value is always synchronized with the component's state, making it a controlled component. Controlled components are useful for managing and validating user input in React applications.

```javascript 
import React , {useState} from 'react'

const Controlled = () => {

    const [text , setText] = useState('')

    const handleSubmit = (e)=>{
        e.preventDefault()
        
        console.log(text)
    }
  return (
    <div>
        <form>
            <input type='text' value={text} placeholder='controlled' onChange={(e)=>setText(e.target.value)}/>
            <button onClick={handleSubmit}>Submit</button>
        </form>
    </div>
  )
}

export default Controlled
```

**Uncontrolled Components:** Uncontrolled components are React components where the value of an input element is not controlled by React state but is directly managed by the DOM. In the given below example, the `Uncontrolled` component uses a `ref` (`inputRef`) to directly access the input field's value from the DOM when needed. Unlike controlled components, React doesn't track or manage the input value's changes in its state. Uncontrolled components are useful in cases where you need to integrate with non-React code or libraries and need direct access to DOM elements.

```javascript 
import React , {useRef} from 'react'

const Uncontrolled = () => {
    const inputRef = useRef(null)


    const handleSubmit = (e)=>{
        e.preventDefault()
        console.log(inputRef.current.value)
    }
  return (
    <div>
        <form>
            <input type='text' placeholder='uncontrolled' ref={inputRef}/>
            <button onClick={handleSubmit}>Submit</button>
        </form>
    </div>
  )
}

export default Uncontrolled
```

