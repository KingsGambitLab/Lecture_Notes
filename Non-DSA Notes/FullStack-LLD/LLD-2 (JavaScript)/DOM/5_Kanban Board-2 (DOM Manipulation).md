# Full Stack LLD & Projects: JavaScript-8: Kanban Board-2(DOM Implementation & Manipulation)



**Agenda of this Lecture:**

* Ticket Generation
* Adding Task, colour, ID to generated ticket
* Ticket Removal
* Locking Mechanism
* Editing Ticket Content



### Explanation 

We'll begin by implementing the ticket generation feature, which involves creating a function to dynamically generate new task tickets. These tickets will then be manipulated and moved across the columns using DOM (Document Object Model) manipulation.

In the file `script.js` we will add this function:

```javascript 
function createTicket() {
  // Create a new ticket container element
  let ticketCont = document.createElement('div');
}
```

Now we will add **class** to this particular div using the `setAttribute` : 

```javascript 
function createTicket() {
  // Create a new ticket container element
  let ticketCont = document.createElement('div');

  // Set the class attribute of the ticket container
  ticketCont.setAttribute('class', 'ticket-cont'); // 
}
```

Whenever this function is called, a new ticket will be created with class `ticket-cont`.

As `ticketCont` contains 3 more divs inside, we will create them inside this function using `innerHTML` function

```javascript 
function createTicket() {
  // Create a new ticket container element
  let ticketCont = document.createElement('div');
  ticketCont.setAttribute('class', 'ticket-cont');

  // Create the HTML content for the ticket container
  ticketCont.innerHTML = `
    <div class="ticket-color"></div>
    <div class="ticket-id">12345/div>
    <div class="task-area">Random Task</div>`
  
  mainCont.appendChild(ticketCont)
```

So we are passing the HTML codes here, so whenever a ticket is created , these 3 divs will also be there.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/613/original/upload_ed6901a16250a577c26b8e2795b1f89d.png?1695229185)



### Explanation

The `addEventListener` method is used to attach an event listener to a DOM element, allowing you to respond to specific events like clicks, key presses, mouse movements, etc.

We add an event listener to the `modalCont` element for the 'keydown' event. This event occurs when a key on the keyboard is pressed and then released.

```javascript 
modalCont.addEventListener('keydown', function(e) {
  let key = e.key;

  if (key === 'Shift') {
    createTicket(); // Call the createTicket function to create a new ticket
    modalCont.style.display = 'none'; // Hide the modal
    textArea.value = ''; // Clear the textarea's content
  }
})
```
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/624/original/upload_55a8528debc5766a05e91dfe21a5cad8.png?1695232320)



### Explanation

As of now everything like Task, color and ID of the created task is static. In this we will be making it dynamic.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/625/original/1.png?1695232401)

So we can choose color, and the ticket will come with a randomly generated ID.

To identify and select these priority color divs, we will use `querySelectorAll` method

We want to select all elements with the class name 'priority-color' using `querySelectorAll` and then iterate through each of these elements using the forEach method. Here's how you can do that:

```javascript 
let allPriorityColors = document.querySelectorAll('.priority-color');

allPriorityColors.forEach(function(colorElem) {
  colorElem.addEventListener('click', function() {
    // Remove 'active' class from all priority colors
    allPriorityColors.forEach(function(priorityColorElem) {
      priorityColorElem.classList.remove('active');
    });

    // Add 'active' class to the clicked colorElem
    colorElem.classList.add('active');

    // Implement additional logic to assign the selected color to a task
    // For example, you can use this space to perform your task color assignment
  });
});
```

In this code, when a color element with the class 'priority-color' is clicked, the event listener:

* Iterates through all `allPriorityColors` and removes the 'active' class from each element.
* Adds the 'active' class to the clicked `colorElem`.
* Implements additional logic to assign the selected color to a task 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/626/original/2.png?1695232419)

So right now we have implemented such that we can select this color, but now we want to get the value of the particular color.

Now we will have a **color array**.

We define an array of colors and updates the modalPriorityColor variable based on the selected color when a color element is clicked. 

```javascript
let colors = ["lightpink", "lightgreen", "lightblue", "black"];
let modalPriorityColor = colors[colors.length - 1]; // Default to black

let allPriorityColors = document.querySelectorAll('.priority-color');

allPriorityColors.forEach(function(colorElem) {
  colorElem.addEventListener('click', function() {
    // Remove 'active' class from all priority colors
    allPriorityColors.forEach(function(priorityColorElem) {
      priorityColorElem.classList.remove('active');
    });

    // Add 'active' class to the clicked colorElem
    colorElem.classList.add('active');

    modalPriorityColor = colorElem.classList[0]; // Update modalPriorityColor
  });
});
```

In this code:

* You define an array colors with color names.
* `modalPriorityColor` is initially set to the last color in the array ('black') as the default.
* The event listener loop iterates through each color element and adds a click event listener.
* When a color element is clicked, the 'active' class is toggled as before.
* Additionally, the `modalPriorityColor` is updated to match the class name of the clicked color element, indicating the selected color.



**Passing ticketColor to createTicket Function:**

In the `createTicket` function, you need to add a parameter `ticketColor` to the function signature. This parameter is intended to hold the selected color for the ticket. When calling the `createTicket` function inside the `modalCont` event listener, you're passing the `modalPriorityColor` as an argument to this function.

This change allows you to set the ticket color dynamically based on the selected priority color. You can use the ticketColor parameter to apply the selected color to the appropriate part of the ticket's HTML content.

```javascript 
function createTicket(ticketColor) {
  // Create a new ticket container element
  let ticketCont = document.createElement('div');
  ticketCont.setAttribute('class', 'ticket-cont');

  // Create the HTML content for the ticket container
  ticketCont.innerHTML = `
    <div class="ticket-color" style="background-color: ${ticketColor};"></div>
    <div class="ticket-id">12345</div>
    <div class="task-area">Random Task</div>
  `;
  
  // Append the ticket container to the main container
  mainCont.appendChild(ticketCont);
}

// Event listener for 'Shift' key press in modalCont
modalCont.addEventListener('keydown', function(e) {
  let key = e.key;

  if (key === 'Shift') {
    createTicket(modelPriorityColor); // Create a new ticket with the selected color
    modalCont.style.display = 'none'; // Hide the modal
    textArea.value = ''; // Clear the textarea's content
  }
});
```
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/628/original/4.png?1695232451)


Now we need to update the task details

* The `createTicket` function accepts two parameters: `ticketColor` for the color of the ticket and `ticketTask` for the content of the ticket's task.
* The `ticketTask` parameter is used to dynamically insert the task content into the task-area div element.
* In the modalCont event listener, the content of the `textAreaCont` element is retrieved using .value and assigned to taskContent.
* When the 'Shift' key is pressed, a new ticket is created with the selected color and task content, and then the modal is hidden.
* The content of the `textAreaCont` element is cleared for the next input.

```javascript 
function createTicket(ticketColor, ticketTask) {
  // Create a new ticket container element
  let ticketCont = document.createElement('div');
  ticketCont.setAttribute('class', 'ticket-cont');

  // Create the HTML content for the ticket container
  ticketCont.innerHTML = `
    <div class="ticket-color" style="background-color: ${ticketColor};"></div>
    <div class="ticket-id">12345</div>
    <div class="task-area">${ticketTask}</div>
  `;
  
  // Append the ticket container to the main container
  mainCont.appendChild(ticketCont);
}

// Event listener for 'Shift' key press in modalCont
modalCont.addEventListener('keydown', function(e) {
  let key = e.key;

  if (key === 'Shift') {
    let taskContent = textAreaCont.value; // Get the content from the textarea
    createTicket(modelPriorityColor, taskContent); // Create a new ticket with the selected color and task content
    modalCont.style.display = 'none'; // Hide the modal
    textAreaCont.value = ''; // Clear the textarea's content
  }
});
```

Now we need to uniquely generate ID for each task created:

We will be using an external library **shortID** for this

```javascript 
function createTicket(ticketColor, ticketID, ticketTask) {
  // Create a new ticket container element
  let ticketCont = document.createElement('div');
  ticketCont.setAttribute('class', 'ticket-cont');

  // Create the HTML content for the ticket container
  ticketCont.innerHTML = `
    <div class="ticket-color" style="background-color: ${ticketColor};"></div>
    <div class="ticket-id">${ticketID}</div>
    <div class="task-area">${ticketTask}</div>
  `;
  
  // Append the ticket container to the main container
  mainCont.appendChild(ticketCont);
}

// Event listener for 'Shift' key press in modalCont
modalCont.addEventListener('keydown', function(e) {
  let key = e.key;

  if (key === 'Shift') {
    let taskContent = textAreaCont.value; // Get the content from the textarea
    let ticketID = shortid(); // Generate a unique ticket ID
    createTicket(modelPriorityColor, ticketID, taskContent); // Create a new ticket with the selected color, ticket ID, and task content
    modalCont.style.display = 'none'; // Hide the modal
    textAreaCont.value = ''; // Clear the textarea's content
  }
});
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/629/original/5.png?1695232474)



To remove the task, we can do similarly to what we did for adding task:

```javascript 
let removeTaskFlag = false;

let removeBtn = document.querySelector('.remove-btn'); // Replace with the actual class or ID selector
removeBtn.addEventListener('click', function() {
  removeTaskFlag = !removeTaskFlag; // Toggle the removeTaskFlag when the button is clicked
  
  if (removeTaskFlag) {
    alert('Delete button is activated.');
  }
});
```

---

