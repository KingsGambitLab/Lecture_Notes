# Full Stack LLD & Projects: React-9: React Redux Interview Question 1


We will discuss some Advanced hooks which are generally asked in React Interview and are very Important to optimize your react

* Use Reducer
* Use Transition

### Explanation

In this existing project, we have made a TODO list application where if we enter the task and date, it will create a TODO task, and if we clicke on the tick option, it will mark the task as done by striking off the task.

To generate random task-ids, we have used **react-uuid** library, which can be installed easily by `npm install` command.

```javascript 
const handleTask = (e) => {
    e.preventDefault();
    const key = e.target.name;
    const value = e.target.value;
    setTask({...task, [key]: value});
  }
```

This above code handles user input in a TODO list project. It prevents default form submission, extracts input field name and value, and updates the task state, likely representing a new task's properties like name and description. This is a key part of adding tasks to the TODO list.


```javascript 
 const addTask = () => {
    console.log(task);
    console.log(uuid());
    const updated = {...task, "id": uuid(), "isDone": false}
    console.log(updated);
    setList([...list, updated]);
  }
```


This above code defines an `addTask` function that logs the current task state, generates a unique ID using `uuid()`, creates an updated task object with an ID and a default "isDone" status of false, logs the updated task, and finally updates the list state by appending the updated task to it. This function is typically used to add a new task to a TODO list.

```javascript 
const markDone = (id) => {
    console.log(`Task with ${id} is done!`);
    const index = list.findIndex((task) => task.id === id);
    const doneTask = [...list];
    doneTask[index].isDone = true;
    setList(doneTask);
  }
```

This above code defines a `markDone` function that takes an id as a parameter. It logs a message indicating that a task with the specified id is marked as done. It then finds the index of the task with that id in the list array using `findIndex`, creates a copy of the list, updates the isDone property of the found task to true, and finally updates the list state with the modified task. This function is typically used to mark a task as completed in a TODO list.

```javascript 
const deleteTask = (id) => {
    console.log(`Task with ${id} to remove!`)
    const filteredTask = list.filter((task) => task.id !== id);
    setList([...filteredTask]);
  }
```



This code defines a `deleteTask` function that takes an id as a parameter. It logs a message indicating that a task with the specified id is being removed. It then creates a new array filteredTask by filtering out the task with the given id from the list. Finally, it updates the list state with the filtered array, effectively removing the task with the specified id. This function is typically used to delete a task from a TODO list.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/533/original/Screenshot_2023-09-20_183518.png?1695215251)

### Explanation 

As we can see, currently we are changing one particular state (ie setList) using three different functions.

In larger projects, managing state changes across multiple functions can lead to increased complexity, potential inconsistencies, and difficulties in debugging, making centralized state management solutions like Redux or context API more valuable for maintaining code quality and scalability.

So for this we can use **useReducer** hook. 

Using the useReducer hook can be a beneficial approach to centralize state management in larger projects. It provides a structured way to manage complex state logic, reduce code duplication, and maintain consistency in state updates, making it a suitable choice for maintaining state in more organized and scalable manner.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/534/original/Screenshot_2023-09-20_183527.png?1695215271)

**Without useReducer:**

* **Events:** User interacts with the UI, triggering various events (e.g., clicks, inputs).
* **State:** Multiple state variables are scattered throughout the component to track different aspects of the application's data.
* **Updates:** Events directly modify these state variables, potentially leading to scattered and uncoordinated state changes.

**With useReducer:**

* **Events:** User interactions still trigger events as before.
* **Reducer:** A centralized reducer function defines how state changes in response to different actions.
* **Dispatch:** Events are dispatched with specific actions to the reducer.
* **State:** The reducer updates the state based on the action and returns a new state object.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/535/original/Screenshot_2023-09-20_183539.png?1695215335)



### Explanation

**Syntax:**

```javascript 
const [state, dispatch] = useReducer(reducer, initialState);
```

**Anatomoy:**

* **State:** This represents the current state of your data, similar to state variables in `useState`. It's what you want to manage or update.
* **Initial State:** The initial value for your state before any actions are applied. It's specified when you call useReducer, like `useReducer(reducerFunction, initialState)`.
* **Dispatch Method:** A function provided by `useReducer` that you use to send actions to the reducer. Actions are objects that describe what should happen to the state.
* **Actions:** These are plain JavaScript objects that contain a type field (a string identifying the action) and optionally, a payload field carrying additional data. Actions describe what specific changes should be made to the state.



### Explanation

We will be now modifying our existing TODO list project using `useReducer`.

We will create a file `reducers.js` and start implementing the script for reducer.

```javascript 
const taskReducers = (state , action) =>{
    switch(action.type){
        case "ADD_TASK" : {
            const newTask = {...action.payload , "id" : uuid() , "isDone": false }
            return [...state , newTask]

        }

        case "REMOVE_TASK" : {
          const taskRemained = state.filter((task)=> task.id !== action.payload )
          return [...taskRemained]

        }

        case "DONE_TASK" : {
            const index = state.findIndex((task) => task.id === action.payload);
            const doneTask = [...state];
            doneTask[index].isDone = true;
            return [...doneTask]
  
          }
    }
}
``` 

Here's an explanation of each reducer case in the `taskReducers` function:

1. **ADD_TASK:**

* When an action of type "ADD_TASK" is dispatched, it creates a new task object by spreading the payload (which should contain task details).
* It adds an "id" to the new task using a unique identifier (e.g., `uuid()`).
* It sets the "isDone" property to false for the new task.
* Finally, it returns a new state array by adding the new task to the existing state array.

2. **REMOVE_TASK:**

* When an action of type "REMOVE_TASK" is dispatched, it filters out the task with the specified ID from the state using `filter()`.
* It returns a new state array with the specified task removed.


3. **DONE_TASK:**

* When an action of type "DONE_TASK" is dispatched, it finds the index of the task with the specified ID in the state using `findIndex()`.
* It creates a copy of the state array.
* It updates the "isDone" property of the task at the found index to true.
* Finally, it returns a new state array with the updated task.

Similarly we will create reducers for other functions like `handleTask`.

```javascript 
const formReducers = (state , action) => {
    switch(action.type){
        case 'HANDLE_TASK' : {
            return {
                ...state,
                [action.field] : action.payload
            }
        }

        default :
        return state
    }
}
```



**HANDLE_TASK:**

* When an action of type "HANDLE_TASK" is dispatched, it updates the state.
* It creates a new state object by spreading the existing state.
* It sets a property in the new state object using the action.field as the key and action.payload as the value.
* This case is typically used to handle form input changes, where action.field represents the field name (e.g., "title" or "description") and action.payload contains the new value entered by the user.

Now we will make changes in our TODO List script. Lets name the new script as `TodoReduced.js`.

```javascript 
const TodoReduced = () => {

  const [state , dispatch] = useReducer(taskReducers , [])

  const [task , dispatchForm] = useReducer(formReducers ,{
    title: "",
    by: ""
  } )
```

* The first `useReducer` hook initializes the state variable to manage the TODO list items. It uses the taskReducers reducer function and an empty array [] as the initial state. This hook is responsible for managing the list of tasks, including adding, removing, and marking tasks as done.
* The second `useReducer` hook initializes the task variable to manage form input fields for creating new tasks. It uses the formReducers reducer function and an initial state object containing two fields: "title" and "by." This hook is responsible for handling changes in the form inputs where users can enter the title and creator of a new task.

Now we will modify our `handleTask` code.

```javascript 
const handleTask = (e) => {
    e.preventDefault();
    dispatchForm({
        type : 'HANDLE_TASK',
        field : e.target.name,
        payload : e.target.value
    })
  }
```

* **`e.preventDefault();`:** Prevents the default form submission behavior, ensuring that the page does not refresh when the form is submitted.
* **`dispatchForm({ type: 'HANDLE_TASK', field: e.target.name, payload: e.target.value });`:** Dispatches an action to the formReducers reducer. It specifies the action type as "HANDLE_TASK," along with the field (the name of the form input) and the payload (the new value entered by the user). This action is used to update the state related to the form inputs, like the task.

```javascript 
return (
    <>
      <div>
        <h1>My TodoList by using useReducer</h1>
        <div>
          I want to do <input type="text" name="title" onChange={handleTask}/> by{" "}
          <input type="date" name="by" onChange={handleTask} />
          <button className="wishBtn" onClick={()=> dispatch({type :"ADD_TASK" , payload : task })}>Add a Task</button>
        </div>
        <ul>
          {state && state.length >0 && state.map((item) => (
            <li key={item.id}>
              <span style={{ textDecoration: item.isDone ? "line-through" : "" }}>
                <strong>{item.title}</strong> is due by {item.by}</span>
              <span><TiTick size={24} onClick={() => dispatch({type:"DONE_TASK" , payload :item.id})} /></span>
              <span><TiTrash size={24} onClick={() => dispatch({type : "REMOVE_TASK" , payload : item.id})}/></span>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
};
```

* It renders the TODO list component, which includes an input field for the task title, an input field for the task due date, and a "Add a Task" button.
* The `onChange` event handlers (handleTask) are used to capture changes in the input fields and update the form-related state.
* It maps over the `state` array (representing the list of tasks) and displays each task with its title and due date.
* If a task is marked as done, it displays a line-through style, and there are icons to mark a task as done or delete it. These actions (`DONE_TASK` and `REMOVE_TASK`) are dispatched to update the list of tasks in the state.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/536/original/Screenshot_2023-09-20_183551.png?1695215357)




We will create a component which will take input, and print the input we gave.

```javascript 
const List = () => {

    const [input, setInput] = useState('')
    const [list, setList] = useState([])

    const [isPending , startTransition] = useTransition()

    const LIST_SIZE = 11000


    function handleChange(e) {
        setInput(e.target.value)

        startTransition(()=>{
            const newList = []
            for (let i = 0; i < LIST_SIZE; i++) {
                newList.push(e.target.value)
            }
    
            setList(newList)
         })

       
        

    }
    return (
        <div>

            <input type='text' value={input} onChange={handleChange}></input>
            {
                isPending? <div> Loadingg..</div> :  list.map((item) => {
                    return <div>{item}</div>
                })
            }

        </div>
    )
}
```

This component, named `List`, renders an input field that captures user `input`. When the user types, it updates the input state. However, it also utilizes `startTransition` from the `useTransition` hook to optimize rendering for a large list (specified by `LIST_SIZE`). While `input` is being processed, it displays "Loading..." to improve user experience. After processing, it maps over the list state and displays the input value multiple times based on `LIST_SIZE`. 



---
