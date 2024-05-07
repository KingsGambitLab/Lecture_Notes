# Full Stack LLD & Projects: JavaScript-9: Kanban Board -3(Bussiness Logics & Local Storage)


**Agenda of this Lecture:**

* Locking Mechanism
* Changing the Priority color of the Task
* Filtering out Task with using the priority color filter
* Showing All Tasks on db click



### Explanation

Currently we have just implemented the project, but we dont have any lock in the project. 
Hence, we will be implementing the lock in this section

We can use the **font-awesome** and get a lock icon for our tasks.


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
    <div class="ticket-lock"><i class="fa-solid fa-lock"></i></div>
  `;
  
  // Append the ticket container to the main container
  mainCont.appendChild(ticketCont);

  handleRemoval(ticketCont);
}
```

* We have added an additional `div` element with the class `ticket-lock` to represent the lock icon for each ticket.
* Inside the `ticket-lock` div, you're using Font Awesome's icon syntax to include the lock icon using the fa-lock class from the `fa-solid` style.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/638/original/1.png?1695233411)


Now we have added the lock, but we need to make it functional now:

```javascript 
let lockClose = 'fa-lock';
let lockOpen = 'fa-lock-open';

function handleLock(ticket) {
  let ticketLockElem = ticket.querySelector('.ticket-lock');
  let ticketLockIcon = ticketLockElem.children[0];

  ticketLockIcon.addEventListener('click', function() {
    console.log('Lock Selected'); // Added single quotes around the log message
    if (ticketLockIcon.classList.contains(lockClose)) {
      ticketLockIcon.classList.remove(lockClose);
      ticketLockIcon.classList.add(lockOpen);
      
    } else {
      ticketLockIcon.classList.remove(lockOpen);
      ticketLockIcon.classList.add(lockClose);
      
    }
  });
}
```


Now to make the content editable inside the task section whenever the lock is open, we will make the following changes:

```javascript 
let lockClose = 'fa-lock';
let lockOpen = 'fa-lock-open';

function handleLock(ticket) {
  let ticketLockElem = ticket.querySelector('.ticket-lock');
  let ticketLockIcon = ticketLockElem.children[0];

  let ticketTaskArea = ticket.querySelector('.task-area'); // Corrected selector

  ticketLockIcon.addEventListener('click', function() {
    console.log('Lock Selected');
    if (ticketLockIcon.classList.contains(lockClose)) {
      ticketLockIcon.classList.remove(lockClose);
      ticketLockIcon.classList.add(lockOpen);
      ticketTaskArea.setAttribute('contenteditable', 'true'); // Changed 'contenteditable', 'true'
    } else {
      ticketLockIcon.classList.remove(lockOpen);
      ticketLockIcon.classList.add(lockClose);
      ticketTaskArea.setAttribute('contenteditable', 'false'); // Changed 'contenteditable', 'false'
    }
  });
}
```

* Corrected the selector for `ticketTaskArea` to use '.task-area'.
* Changed the `contenteditable` attribute value to 'true' or 'false' to correctly toggle the editable state of the task area based on the lock state.


### Explanation

In this section we will handle the color of the tasks



```javascript 
function handleColor(ticket) {
  let ticketColorBand = ticket.querySelector('.ticket-color'); // Corrected selector
  ticketColorBand.addEventListener('click', function() {
    let currentColor = ticketColorBand.classList[0]; // Changed index to 0

    let currentColorIdx = colors.findIndex(function(color) {
      return currentColor === color;
    });

    currentColorIdx++; // Increment the index

    let newTicketColorIdx = currentColorIdx % colors.length; // Corrected variable name
    let newTicketColor = colors[newTicketColorIdx]; // Corrected variable name
    
    ticketColorBand.classList.remove(currentColor); // Corrected spelling
    ticketColorBand.classList.add(newTicketColor); // Corrected spelling
  });
}
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/639/original/2.png?1695233433)



### Explanation

In this feature, we need to filter the task according to the priority color.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/640/original/3.png?1695233456)

```javascript 
let toolboxColors = document.querySelectorAll('.color');

for (let i = 0; i < toolboxColors.length; i++) {
  toolboxColors[i].addEventListener('click', function() {
    let selectedToolboxColor = toolboxColors[i].classList[0];

    let allTickets = document.querySelectorAll('.ticket-cont'); // Corrected selector
    for (let j = 0; j < allTickets.length; j++) {
      allTickets[j].remove(); // Removed square brackets and added j to index

      let filteredTickets = ticketsArr.filter(function(ticket) {
        return selectedToolboxColor === ticket.ticketColor;
      });

      filteredTickets.forEach(function(filteredTicket) {
        createTicket(
          filteredTicket.ticketColor,
          filteredTicket.ticketTask,
          filteredTicket.ticketID
        );
      });
    }
  });
}
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/641/original/4.png?1695233480)



