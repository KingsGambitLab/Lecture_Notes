


In the previous session, we covered topics such as ticket creation, deletion, locking, and unlocking, as well as dynamically changing the priority color. We comprehensively explored the implementation of these functionalities.

However, a new issue has arisen. Upon initial usage, the filter buttons function as intended. Yet, upon subsequent clicks, a problem arises where duplicate tickets of the selected color are generated.

What might be the underlying cause of this problem?

To address this issue, we're planning to implement a validation process using unique identifier to prevent the occurrence of duplicate tickets.


This is the code that we have implemented till now for filtering tickets.


We've executed the loop that iterates through the toolbox colors, covering every index. For each color dip, we've attached corresponding event listeners. When a click event occurs, our first step is to determine which color dip or filter was clicked – for instance, selecting black would mean retrieving tasks labeled with a black priority color.

Following the color selection from the toolbox, we proceed to match that color with the colors associated with each ticket. We apply a filtering process to narrow down the array of tickets to only include those that match the selected color. The result is an array of filtered tickets, where each ticket object contains information like color values, task details, and IDs.

At this juncture, we remove the default set of tickets and replace them with the newly filtered array. This is the approach we discussed in the previous session. However, an issue arises when we repeatedly select a color, leading to the duplication of arrays.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/630/original/1.png?1695232771)

#### Pseudocode
```javascript

for (let i = 0; i < toolboxColors.length; i++) {
    toolboxColors[i].addEventListener('click', function() {
        let selectedToolBoxColor = toolboxColors[i].classList[0];
        
        let filteredTickets = ticketsArr.filter(function(ticket) {
            return selectedToolBoxColor === ticket.ticketColor;
        });
        
        let allTickets = document.querySelectorAll('.ticket-cont');
        
        for (let i = 0; i < allTickets.length; i++) {
            allTickets[i].remove();
        }
        
        filteredTickets.forEach(function(filteredTicket) {
            createTicket(filteredTicket.ticketColor, filteredTicket.ticketTask, filteredTicket.ticketId);
        });
    });
}

```


To tackle this issue, we're planning to implement a validation mechanism that utilizes unique identifier to ensure that duplicate tickets aren't generated. This way, the filtered ticket array will only consist of distinct tickets corresponding to the selected color.


So, using the unique IDs associated with each ticket is a great way to prevent duplicates. This way, we can ensure that the same ticket isn't added to the filtered array more than once.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/631/original/2.png?1695232789)

 In which part of the code should you integrate this ID-checking mechanism to effectively prevent duplicate tickets from being included in the filtered array?

Within the createTicket method, we'll implement the following logic: if a ticket possesses an existing ID, it will be used; otherwise, a new unique ID will be generated during its initial creation. It's essential to note that the ticket will only be pushed to the array if it lacks an ID, ensuring avoidance of duplication.


#### Pseudocode
```javascript
function createTicket(ticketColor, ticketTask, ticketId) {
    // Adding an identifier
    let id = ticketId || shortid();
}
```

Prior to adding the ID to the array, we will perform a validation to ascertain its existence, and only if it indeed exists, will it be appended within the createTicket method.

#### Pseudocode
```javascript
function createTicket(ticketColor, ticketTask, ticketId) {
    // Adding an identifier
    let id = ticketId || shortid();
    
    // Other code
    
    if (!ticketId) {
        ticketArr.push({ ticketColor, ticketTask, ticketId: id });
    }
}

```

---
title: What is local storage?
description: Gaining Insight into Local Storage and How to Utilize It
duration: 600
card_type: cue_card
---

> Note to instructor - Address any questions that the students might have.


 What kind of ID will the shortid library generate?

It will produce a random ID for the ticket.


Upon accessing your browser, you'll encounter the inspect page, which offers a variety of elements to explore. Within this inspect interface, navigate to the application tab. Here, you'll be presented with numerous sections such as local storage, session storage, and cookies. For today's discussion, our focus will be on local storage.

What exactly is local storage? What are your thoughts on the ideal function of local storage? 

The issue lies in data loss when a page is refreshed. We intend for the application to retain data even after a refresh – that's the core purpose of having this feature.

This occurrence arises from our utilization of local storage as the repository for all our data. Now, let's delve into the concept of local storage. In essence, it offers the capacity to store up to 5mb of information, enabling your browser to retain such data. Imagine a scenario where you're crafting an application and the need for a database isn't there. In situations where a 5-megabyte threshold suffices, local storage serves as a viable means to preserve and manage the data.





What is a Windows object?

Within JavaScript, resides the window object. This object grants access to an array of properties, methods, and functionalities offered by the Document Object Model (DOM).


#### Pseudocode

```htmlembedded
<!DOCTYPE html>
<html>
<head>
    <title>Title of the document</title>
</head>

<body>
    <!-- The content of the document... -->
</body>

<script>
    console.log(window);
</script>

</html>
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/632/original/3.png?1695232812)

We can use numerous methods and properties within the browser including local storage feature. Access to local storage is facilitated through the window object. Within local storage, you can engage actions like setting an item and getting an item. The "setItem" function is utilized to store data, while "getItem" serves to retrieve stored data. This data is maintained in a JavaScript-oriented key-value structure.

Moreover, there's a "removeItem" capability that permits the deletion of specific entries from local storage. Should the need arise to completely erase all data, the "localStorage.clear" command accomplishes that task.



Now, let's see how we are gonna implement local storage

 
In which scenarios will the requirement for local storage arise?

Let's review  all our functionalities:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/633/original/4.png?1695232834)


a. Creating a ticket involves storing them within local storage.
b. Updating a ticket, whether altering its color or task, entails updating these modified values in local storage.
c. Deleting a ticket results in its removal from local storage.

Notably, if you refrain from deletion and subsequently refresh the page, local storage will retain the instance of that particular ticket, so we need to remove that from local storage to reflect the data.

Whenever a ticket creation occurs, we have the option to store it in local storage using the "setItem" method. This involves providing the name of the array as a parameter. Here, during the code insertion within the createTicket method, we will employ the setItem function of localStorage:

#### Pseudocode
```javascript

function createTicket(ticketColor, ticketTask, ticketId) {
    if (!ticketId) {
        ticketArr.push({ ticketColor, ticketTask, ticketId: shortid() });
        localStorage.setItem('tickets', JSON.stringify(ticketArr));
    }
}

```

It's important to note that local storage accommodates data in string format. Thus, any data you intend to store should be converted into string form before insertion.


> Note to instructor - Test to determine whether the local storage has been successfully established or not.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/634/original/5.png?1695232854)

After refreshing the page, you'll notice that the data resides within local storage, yet the paradox emerges – despite setting the data, we encounter a loss of the data itself. The situation unfolds as we've successfully stored the data, yet the process of retrieving the values proves elusive.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/635/original/6.png?1695232878)


We employ the stringify method to establish the data, while the reverse, JSON.parse, allows us to retrieve the data back in JSON format.

As we initiate the application, our first step is to retrieve all the tickets stored within local storage. If we come across any items designated as "tickets," our subsequent approach revolves around displaying or generating these tickets accordingly. For each of these identified tickets, the createTicket method will be invoked.

#### Pseudocode
```javascript=

// local storage

if (localStorage.getItem('tickets')) {
    ticketsArr = JSON.parse(localStorage.getItem('tickets'));
    ticketsArr.forEach(function(ticket) {
        createTicket(ticket.ticketColor, ticket.ticketTask, ticket.ticketId);
    });
}

```

> Note to instructor - Test this by refreshing the page again; you'll observe that nothing is removed.


> Note to instructor - Feel free to address any questions that students might have. 


Initially, let's construct a function that facilitates the retrieval of the ticket's index using its corresponding ID. The ID will help in identifying the ticket that requires updating.

#### Pseudocode
```javascript

function getTicketIdx(id) {
    let ticketIdx = ticketArr.findIndex(function(ticketObj) {
        return ticketObj.ticketId === id;
    });
    return ticketIdx;
}

```

Within the handleLock function, whenever a lock is unlocked through a click event, it becomes imperative to retrieve the index of the corresponding ticket. This enables us to determine the specific location where this action occurred.


#### Pseudocode
```javascript
function handleLock(ticket) {
    let ticketLockElem = ticket.querySelector('.ticket-lock');
    let ticketLockIcon = ticketLockElem.children[0];
    let ticketTaskArea = ticket.querySelector('.task-area');
    
    ticketLockIcon.addEventListener('click', function() {
        let ticketIdx = getTicketIdx(id);
        // Other code
        
        // Updated task
        ticketsArr[ticketIdx].ticketTask = ticketTaskArea.innerText;
        localStorage.setItem('tickets', JSON.stringify(ticketsArr));
    });
}

```

Henceforth, it will be retained with an updated task.




Now, let's proceed to explore the color feature.


#### Pseudocode
```javascript
function handleColor(ticket) {
    let ticketColorBand = ticket.querySelector('.ticket-color');
    
    ticketColorBand.addEventListener('click', function() {
        // getting index
        let ticketIdx = getTicketIdx(id);
        let currentColor = ticketColorBand.classList[1];
        
        let currentColorIdx = colors.findIndex(function(color) {
            return currentColor === color;
        });
        
        currentColorIdx++;
        
        let newTicketColorIdx = currentColorIdx % colors.length;
        let newTicketColor = colors[newTicketColorIdx];
        
        ticketColorBand.classList.remove(currentColor);
        ticketColorBand.classList.add(newTicketColor);
        
        // Updated task
        ticketsArr[ticketIdx].ticketColor = newTicketColor;
        localStorage.setItem('tickets', JSON.stringify(ticketsArr));
    });
}

```



Now, let's evaluate the final feature, which involves deleting data from local storage.


#### Pseudocode
```javascript
function handleRemoval(ticket) {
    ticket.addEventListener('click', function() {
        if (!removeTaskFlag) return;
        
        let idx = getTicketIdx(id);
        ticket.remove(); // UI removal
        
        let deletedElement = ticketsArr.splice(idx, 1);
        localStorage.setItem('tickets', JSON.stringify(ticketsArr));
    });
}

```

