## Agenda

Today we are going to start with React.

Prerequisites that you should know:
* HTML/CSS
* Javascript Core (Understanding of how Javascript works).
* DOM (Vanilla JS)
* Modularity (We will know how to export and import different functions and properties from the code. While working with React we use lot of Modular code in terms of components. Everything is modular in React, that why we need to understand Modularity. )

Softwares you must install in System for react
* VS Code
* NodeJS (React is dependent on NodeJS)
* Git (Not necessary)

Before starting with React, we will first understand 1 topic and then we will move forward with React. That topic is Modularity.



whatever code you write shoud be written in form of modules so that you can specifically use, Read and Maintain your Codebase. Modularity refers to the practice of breaking down a larger software program into smaller, self-contained, and reusable modules. These modules encapsulate specific functionality, variables, or objects, making it easier to manage, maintain, and scale your JavaScript code. 

**[Ask the learners]**
Suppose you have written all the modules you are using in NodeJS in a single file, is this a Good practice?

No, this is not a good practice because what modularity says is whatever feature you want to write, make separate module for it.

Suppose you want to code a calculator and you want to make modules for each function it will do. Just make 4 functions addition, subtraction, multiplication and division.

We can simply make 4 functions:



```javascript
function add(a, b){
    console.log(a+b);
}

function sub(a, b){
    console.log(a+b);
}

function mul(a, b){
    console.log(a+b);
}

function div(a, b){
    console.log(a+b);
}

add(2, 3)
sub(10, 5)
mul(3, 4)
div(10, 2)
```

Now we want to make this code modular, and that module, we should be able to use in different JS files. For that we have to import and export functions and properties of the code.

For exporting the function to new file, first lets create 1 file called ModuleTest.js where we will import all these functions that we have just created.

for exporting the functions:

```javascript
module.exports={
    addition: add,
    substraction : sub,
    multiplication : mul,
    division : div
}
```

**[Ask the learners]**
What would you do if you want to import these files?

Using Require, yes we can use require to import a file in other JS file.

So in this case:

```javascript
const calculator = require("./calc")

calculator.addition(2 , 3)
calculator.multiplication(2 ,3)
calculator.substraction(3 , 1)
calculator.division (10 , 5)
```

So we are trying to import a module named "calc" and use the functions addition, multiplication, subtraction, and division from that module. 

Also we dont need to use console.log here because we are already logging the output in the the function definition.

Benefits of this are:
* Code Reusability: Modules are self-contained units of code that can be reused across your application or in other projects. This reduces the need to rewrite the same functionality, saving time and effort.
* Ease of Maintenance: Smaller, well-defined modules are easier to understand and maintain. Developers can focus on individual modules without needing to comprehend the entire codebase, which simplifies debugging and updates.
* Readability: Well-structured modules with clear interfaces and documentation enhance code readability. Other developers (including your future self) can easily understand how to use and interact with a module.

Lets understand module.exports object:

ModuleExports defines an object in which you can pass your functions in keys and you can use those keys whenever you are Importing your module and they will invoke the function associated with them Respetively.

It is used to define what a module should export to be used in other parts of your code. It allows you to encapsulate code in a module and expose specific functions, variables, or objects for use in other files or modules.

So this is all about Modularity.

Now we will look into React. We will be learning it from scratch. 


React is the most popular and important library for Frontend Development. React is most in demand and companies want frontend developers who works on React.

React is JS library for frontend Development developed By Meta(facebook) and this actually is very fast performing tool and it follows Component Based Architecture.

Lets understand what is Component Based Architecture:

If you talk about Vanilla JS, DOM is a tree structure

![](https://hackmd.io/_uploads/rkRtn4zA3.png)

Doing Operations in a DOM is a heavy operations, So remove these Heavy Operations, React introduced Component Based Architecture. It says that anything you create can be hashioned into separate component, allowing you to work on each of them separately.

**[Ask the learners]**
What do I mean by a Component Based Architecture?

If you take a look at LinkedIn's interface, you'll notice several components, and each of these components functions as an independent entity.If you examine the particular section, you'll see that all the sections are distinct components and also operating of one another.

This is precisely what React does, it structures the architecture in a component-centric manner. 

![](https://hackmd.io/_uploads/Skoqk6EAh.png)

If you currently have an application. React's library will partition each of the sections into distinct components, allowing you to work on them separately and independently.This is essentially the core functionality of React. This makes the code maintainable and it also enables you to reuse individual components repeatedly.

Consider LinkedIn as an example. You'll notice that various sections, such as the boxes, share a similar structure, even though they contain different data.


So let's create HTML file, index.html to do one task that is append Hello from HTML in an HTML page.

```javascript=
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="root">
        <h1>Hello From HTML</h1>
    </div>    
</body>
</html>
```

We have created the boilerplate code. Now create a div with an ID root. Inside this root element, you can simply include an `<h1>` tag with the message "Hello from HTML." 

**[Ask the learners]**
Your task is to display this message "Hello From JS" by using Vanilla JavaScript.

For doing that you want to create a script

```javascript=
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="root">
    
    </div>

    <script>
        let greeting = document.createElement('h1')
        
        greeting.innerHTML = 'Hello from JS'

        let root = document.getElementById('root')
        
        root.appendChild(greeting)
    </script>
</body>
</html>
```

Now, what we will be doing is we will be doing the same thing using React. We will understand how React actually handles all of these things, right? Alright, so now let's move on to React. Before delving into React, we have already discussed what React is and its architecture, among other things.

Let's move to our browser and I'll just type React over here. 
https://legacy.reactjs.org/docs/getting-started.html
So this is the link that you need to follow. So just open this link and you will see this particular website. 

React is not inbuilt in your browser, right? So, first let me show you how you can use React with using CDN links. We'll understand this. Then we'll see what is the problem when we'll use React with CDN links. And then we'll move to creating a new React app.

As you will go to these CDN links, you will see all of these CDN scripts. You can just copy this and you can paste it in your HTML file.

```htmlembedded
<script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
```

**[Ask the learners]**
Now you must be wondering that why not just create a single link and you can input the React properties and Dom over there as well? Now why not to do that?

It's all about modularity. React is designed as separate modules because it serves as a comprehensive cross-platform framework, or I should say library, right? This means that in addition to React, we have React Native for mobile development. Furthermore, with React, we can create progressive web apps that can function across various platforms, including laptops, iOS, Android, and any other screen or device you might need, right?

So basically, to have all of those particular features in different particular links, we have these as separate modules. So these modules can be used anywhere. So that's why we have these two separate modules.

you'll have to inject these CDN links in your particular application. Only then you'll be able to use React. If you're not injecting these CDN links, you'll not be able to use React.

if I go to my browser and open console if I type React, now I'm able to access React and React Dom. And now you see if I press Enter, so we have an object. So whole react is just under an object. So now if I open this object, you will see different properties and different methods.


> Note to instructor - Now explain everything in that Object.

So now we'll move to our VS Code and We'll write some code 



Thing that you must remember is whenever you are writing React code, just make sure that whenever you start writing React code, these CDN links should be at the top of the code.

Now let's see how we can use React.createElement() method by creating an element using this.

> Note to instructor - Explain code at each line.

```htmlembedded
<script>
let greeting = React.createElement ('h1' , {} , 'Hello From React')
console.log(greeting)
let root = ReactDOM.createRoot(document.getElementById('root'))
root.render(greeting)
</script>
```

The greeting element has been created from the render method. If I do not render this, then there will be no element inside the div.

If we want to pass attributes to the element that we want to create (let's say ID):

```htmlembedded
<script>
    let greeting = React.createElement ('h1' , {id:'greeting', className:'greet'} , 'Hello From React')
    console.log(greeting)
    let root = ReactDOM.createRoot(document.getElementById('root'))
    root.render(greeting)
</script>
```
So this is how basically, you can pass on your attributes if you want.

We have seen this that how to use create element, how to use create root, how to get your root, how to basically use the render method. We have done with all of these things.

Now Suppose I have an HTML Structure:

```htmlembedded
<div id='parent'>
    <div id='child'>
        <h1 id='content'>Hello from react</h1>
    </div>
</div>
```

**[Ask the learners]**
Now, how can we create a similar Sturture, so can we create it?

You can follow this code

```javascript
let greeting = React.createElement(
    "div",
    { id: "parent" },
    React.createElement(
        "div",
        { id: "child" },
        React.createElement("h1", { id: "content" }, "Hello from React")
    )
);

```
React.createElement("div", { id: "parent" }, ...) - This line creates a React element representing a ``<div>`` with an id attribute of "parent." The ... indicates that there are child elements inside this ``<div>``.
React.createElement("div", { id: "child" }, ...) - Inside the "parent" ``<div>``, another React element is created, representing a nested ``<div>`` with an id attribute of "child." Again, the ... indicates that there are child elements inside this nested ``<div>``.
React.createElement("h1", { id: "content" }, "Hello from React") - Inside the "child" ``<div>``, there's an h1 element with an id attribute of "content" and the text content "Hello from React."

You can clearly say that this should not be the way of writing a code, right? And to basically solve this problem, to solve this mess, to solve this hassle, we use something known as JSX and we'll be talking about JSX just after this. 

Before we move forward, lets take a 1 more question.

**[Ask the learners]**
Now, If I want to add 1 more element in the same structure we have created, so can we create it?

```htmlembedded
<div id='parent'>
    <div id='child'>
        <h1 id='greeting'>Hello from react</h1>
        <h2 id='greeting2'>Hello from react Heading 2</h1>
    </div>
</div>
```

Now if we see we have two elements in same hierarchical order. 

Here we can use an array.

```javascript
let greeting = React.createElement(
    "div",
    { id: "parent" },
    React.createElement(
        "div",
        { id: "child" },
        [React.createElement("h1", { id: "greeting" }, "Hello from React"),
        React.createElement("h2", { id: "greeting2" }, "Hello from React Heading 2")]
    )
);

```

So you can use an array and you can use these methods as each element of the Array.

But yes, this way of writing code is not recommended at all. This is very bad code. This should not be used. But for your knowledge, you must know all of these things.



I'll just create a folder and just call this as demo. So I've created a folder as demo app and in this particular folder we'll be initializing our react application.

We will now go to https://legacy.reactjs.org/docs/create-a-new-react-app.html and we'll be using Create React app moving forward .

If you want to use CDN, you'll have to make use of the Dom. You'll have to write all of these script tags, you'll have to go create different JavaScript files again and again and again. That is not recommended at all. So that's why we'll be using Create React app which will actually give you a whole boilerplate code of React and there you'll be able to work with each and everything that React has to offer.

**Ways To Initialize a React App**
* CDN Links: we talked about 
* CRA (Create React App)
* Vite

We can use The following comamnd to make a React App:

```javascript
npx create-react-app demo
```
npx means node package executor, So now, if you see, this has started installing all of the things that we'll need. So I want every one of you to do this once. And after you have done, you will see all of these files that will be available inside this demo folder.

Let's move forward. So I'll just go to the Vs code and I'll just close all of these files my app is running.

Now you can see that here inside this demo folder, you have all of these files and folders. 
* There is one folder as Node modules, 
* There is one public folder. 
* There's one source folder, 
* There's a git ignore file
* There are two JSON files. 
* There is one README. 

All of these things are here inside this demo folder. 

So first, let's start with the public folder. Let's start with the public. So let's go inside this public and ignore all of these things. They are all logos and favicons. You do not need to worry about this.

So if you go to this index.html file. So now you can see this is all your HTML code. This is all your HTML code. And here you have your root.

![](https://hackmd.io/_uploads/S1Zef8ICh.png)

So if you remember, just a while ago, we were doing this thing that everything that you were creating was going inside the root div only. Was going inside the root div only. So this is basically the starting point of your react app. Everything that you will do will go inside this root only, right? So this is that root.

So whenever you write react code and you will render all of those code, those code will be converted into elements and all of those elements will be created inside this root.

now if you see if you are clear with this root, now we'll go to the source folder and we'll see where this root has been selected.

Let's go to index.js and if you go to index.js, you see that there is a line that is actually getting the ID root.
![](https://hackmd.io/_uploads/Sk1W78IR2.png)


Third thing that you must pay your attention to is this particular render method. 

![](https://hackmd.io/_uploads/B1CWmL802.png)

This says App. This App.js will be rendered inside the root, and this root will have all your HTML elements. I mean, render will convert this app JS file in the form of elements, and all of those elements will be rendered inside your root and you will have your HTML

I'll be deleting some files from this source folder as well and make sure that you delete them very carefully, because if you delete any important file, your app will be destroyed.

We can delete reportWebVitals, setupTest, appTest.js, logo.svg. These are the four files that are not needed right now.

As we have deleted reportWebVitals  file, so we need to remove it from index.js else it will cause error.

![](https://hackmd.io/_uploads/B1JCNUU0h.png)

In app.js remove logo.svg.

Basically there's one command which is `npm start`.

Make sure you're on the same folder where your react app is. So it is inside this demo folder. So here you just have to write `npm start` and you just need to press Enter. 

App has  been started on localhost:3000.

We can update our app.js file to show some content:

![](https://hackmd.io/_uploads/HJS3SLIA2.png)

We are creating a function that is JavaScript. Whenever you create a function that is JavaScript inside this, you are returning a div which is HTML. So basically, when you use JavaScript and HTML together, that thing is known as  JSX. The full form of JSX is JavaScript XML. You can just say that JSX is when you use JavaScript and HTML together, that particular thing is JSX. 

And this kind of functions, this kind of functions are known as functional component. This is a functional component.

But for today, I would like to stop over here only. I don't want to confuse you more. I don't want to go in more depth today because we have already seen a lot of stuff today. So this was an introductory class to React, in which we understood that what react is.

So in the next class, we'll be seeing how components can be created. What are states, what are props, how can you work with props? And how can you basically work along with react?

