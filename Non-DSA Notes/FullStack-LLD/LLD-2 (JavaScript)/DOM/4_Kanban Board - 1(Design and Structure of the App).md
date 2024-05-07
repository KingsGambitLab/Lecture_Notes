

## Agenda
**Topics to cover in Javascript:**

Certainly, here are the headings for the provided topics:

1. **Kanban Board**
2. **Create and Update Task**
3. **Lock and Unlock Tasks**
4. **Colors**
5. **Pop-up Dialog Box**
6. **Delete**
8. **Local Storage**

We will try to cover most of these topics in today's sessions and the remaining in the next.

So let's start.



## Demo of the project:

Initially showing the demonstartion of the adding task, setting the colors, unlock/lock feature, filtering based on the colors and delete feature.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/293/original/upload_a9d95787724a2eefbc93ff4c186e60f4.png?1695962045)

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/294/original/upload_13e69cd676c1c6d6d59196e64feca84f.png?1695962069)

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/295/original/upload_17f12377711408328263574d51b2f1d2.png?1695962111)

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/296/original/upload_be9923603755a2c965d7de8883361c37.png?1695962174)

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/297/original/upload_072c08517a1a2e792b109cd3e694555b.png?1695962206)




Discussing about the local storage and the crud operation and also try to cover the drag-drop functionalities, accessibility.

On the highest level, mainly there are two components, to mark those will be using the two divs namely toolbox-container and maincontainer.

Inside the toolbox container first there are different tags for colors which we ca have and after that these two boxes of + and X. Apart fro that we can those ticket also.


### WireFrame of the Kanban Board

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/298/original/upload_ad6e9829fa6c28b5099af52832588dac.png?1695962233)

In toolbox container there are two container namely toolbox-priority-cont and action-btn-cont. 
* Inside the toolbox-priority-cont we are having the four divs of colors(pink, blue, purple and green).
* In the toolbox-priority-cont having the two divs of add-btn and remove-btn. Alaso adding the font from the cdn font library. 


Opening the live server and just seeing the effects of the added code till now and nothing is visible till now since no css has been added.

```htmlembedded
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta http-equiv = "X - UA - Compatible" content = "IE = edge">
    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
    <title>KanbanBoard</title>
    <link rel = "stylesheet" href = "./style.css">
    <link rel = "stylesheet" href = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw == " crossorigin = "anonymous" referrerpolicy = "no-referrer" />
</head>
<body>
    <div class = "toolbox-cont">
        <div class = "toolbox-priority-cont">
            <div class = "color red"></div>
            <div class = "color blue"></div>
            <div class = "color green"></div>
            <div class = "color black"></div>
        </div>
        <div class = "action-btn-cont">
            <div class = "add-btn">
                <i class = "fa-solid fa-plus fa-xl"></i>
            </div>
            <div class = "remove-btn">
                <i class = "fa-solid fa-trash fa-lg"></i>
            </div>
        </div>
    </div>

    <div class = "main-cont">
        <!-- <div class = "ticket-cont">
             <div class = "ticket-color red"></div>
             <div class = "ticket-id">#qu45</div>
             <div class = "task-area" contenteditable = "true">Some Task</div>
             <div class = "lock-unlock"><i class = "fa-solid fa-lock"></i></div>
        </div> -->
    </div>


    <div class = "modal-cont">
        <textarea class = "textarea-cont" placeholder = "Enter Your Task"></textarea>
        <div class = "priority-color-cont">
            <div class = "priority-color red"></div>
            <div class = "priority-color blue"></div>
            <div class = "priority-color green"></div>
            <div class = "priority-color black active"></div>
        </div>
    </div>

    <script src = "https://cdn.jsdelivr.net/npm/short-unique-id@latest/dist/short-unique-id.min.js"></script>
    <script src = "./script.js"></script>
</body>
</html>
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/299/original/upload_e30d878377b9bd9cf474cb1301fc205a.png?1695962642)

Nothing is visible as no css has been added.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/300/original/upload_c2936d373f1e1a5f3d8ab5201bec1447.png?1695962669)

Let's start creating the css file namely style.css, and adding the code for the colors first by creating the css variables for the colors like pink, green, purple etc.

```css 
/* create css variables  */
:root{
    --ligthBackground: #F9F5EB;
    --background:#E4DCCF;
    --red:#EA5455;
    --blue:#002B5B;
    --green:#245953;
}

*{
    box-sizing: border-box;
}

body{
    margin: 0;
    padding: 0;
    background-color: var(--background);
}
```

Now adding the css for the toolbox container starting with height, background-color and then adding the toolbox-priority-container by providing it with height, background-color. Same for the action-btn also same color and height. 

```css
/* styling starts from here */


/* ************toolbox_cont **********/
.toolbox-cont{
    height: 5rem;
    background-color: var(--blue);
    display: flex;
    align-items: center;
    position: fixed;
    top: 0;
    width: 100vw;
}
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/301/original/upload_d4f9f4cf35c5bfa09c037dd33e66d59f.png?1695962712)

Now adding the display: flex in the parent conatiner namely in the toolbox-container in the css code. Add margin-left in the toolbox-priority-cont and margin-left in the action-btn-cont. Also change the background-color of the action-btn-cont to the light. 

Now add the color blocks in the toolbox-priority-cont. Providing the height and width to the color block. Also add the display:space-evenly and align-items:center to the parent class.

```css
.toolbox-priority-cont{
    height: 3rem;
    width: 18rem;
    background-color:var(--ligthBackground);
    margin-left: 5rem;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
}

.action-btn-cont{
    height: 3rem;
    width: 10rem;
    background-color:var(--ligthBackground);
    margin-left: 5rem;
    display: flex;
    align-items: center;
    justify-content: space-around;   
}

.color{
    height: 1.5rem;
    width: 3rem;
}
.red{
    background-color: var(--red);
}

.blue{
    background-color: var(--blue);
}

.green{
    background-color: var(--green);
}

.black{
    background-color: black;
}
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/302/original/upload_42e73b6053c5fad1c385afff28524242.png?1695962753)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/303/original/upload_3a3b8bfceafc27620ccce6c37351288b.png?1695962778)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/304/original/upload_f85dbc2e4cc9ebf27377b4e604430cbd.png?1695962805)

Provide the font size to the both add-btn and remove-btn and also add the display:flex, align-item:center and justify-content:space-evenly in the action-btn-cont.

```css
.add-btn,.remove-btn{
    font-size: 1.25rem
}
.action-btn-cont{
    height: 3rem;
    width: 10rem;
    background-color:var(--ligthBackground);
    margin-left: 5rem;
    display: flex;
    align-items: center;
    justify-content: space-around;   
}
```
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/305/original/upload_d2b4ce1974ce2ded96f913efa5888f58.png?1695962865)

Now let's add the hover effect to the button of add-btn and remove-btn as follows:
```css
.add-btn:hover{
background-color: #4BB543;
}
.remove-btn:hover{
background-color: #4BB543;
}
```

**Asking Question?**

Can you add the hover effect to these color boxes in the nav bar?
**Ans:** You can try by themself.

Now lets start creating the modal with its html and css structure as follows:

```htmlembedded
    <div class = "modal-cont">
        <textarea class = "textarea-cont" placeholder = "Enter Your Task"></textarea>
        <div class = "priority-color-cont">
            <div class = "priority-color red"></div>
            <div class = "priority-color blue"></div>
            <div class = "priority-color green"></div>
            <div class = "priority-color black active"></div>
        </div>
    </div>

```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/306/original/upload_b5fb49c924748828c00aa7fcd3b96aec.png?1695962964)

```css
 .modal-cont{
   height: 50vh;
   width: 45vw;
   display: flex;
   background-color: lightsalmon;
   position: absolute;
   top:30%;
   left: 27%;
   display: none;


}
 .textArea-cont{
     height: 100%;
     width: 75%;
     resize: none;
     outline: none;
     border: none;
     background-color: #dfe4ea;
     font-size: 2rem;
     color: black;
 }
 .priority-colors-container{
     height: 100%;
     width: 25%;
     display: flex;
     flex-direction: column;
     background-color: #4b4b4b;
     align-items: center;
     justify-content: space-around;

 }
 .priority-color{
     height: 3rem;
     width: 5rem;
 }

 .active{
     border: 5px solid lightsalmon;
 }
```
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/307/original/upload_5cc60a83b1501db2f03ac1db28e1f9aa.png?1695963048)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/308/original/upload_6897796c561e5883f5e5d43bcf818ec0.png?1695963073)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/309/original/upload_b649635bc4877058c29f45833a32b7f9.png?1695963095)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/310/original/upload_918fb74d1dda35302a77b8d06711e3d5.png?1695963117)

This CSS code defines styles for a modal container and its components:

1. **.modal-cont:**
   - Defines the modal's dimensions and appearance.
   - Positioned absolutely with a specific top and left offset.
   - Initially hidden with `display: none`.

2. **.textArea-cont:**
   - Represents a text area within the modal.
   - Takes 75% of the modal's width.
   - Has specific styling for background color, font size, and no borders.

3. **.priority-colors-container:**
   - A container for priority color elements.
   - Takes 25% of the modal's width.
   - Aligns items vertically and adds a background color.

4. **.priority-color:**
   - Represents priority color elements.
   - Fixed dimensions for each element.

5. **.active:**
   - Adds a border to elements with this class, using a lightsalmon color.

Overall, these styles are likely used for a modal interface, with a text area and priority color options.

Now we will be working for the buttons of + and X by giving the event listener to them. Here is a basic structure of the event Litener for them as follows:

```htmlembedded
Eventlistener.(click):
let flag=false
flag=true
if(flag=true){
modal visible
}
```

```javascript!
let addBtn = document.querySelector('.add-btn')
let modalCont = document.querySelector('.modal-cont')
let addTaskFlag = false

addBtn.addEventListener('click' , function(){
    // Display the model
    addTaskFlag = !addTaskFlag
    
    if(addTaskFlag == true){
        modalCont.style.display = 'flex'
    }
    else{
        modalCont.style.display = 'none'
    }

})
```
This JavaScript code adds functionality to a button:

1. `addBtn` and `modalCont` variables are defined to select HTML elements with specific classes.

2. An event listener is added to `addBtn` for a click event.

3. When the button is clicked, a flag (`addTaskFlag`) toggles between true and false.

4. If `addTaskFlag` is true, the modal container (`modalCont`) is displayed by changing its `display` style property to 'flex'.

5. If `addTaskFlag` is false, the modal container is hidden by setting its `display` property to 'none'.

This code toggles the visibility of the modal when the button is clicked.


Now lets create the structure of the task ticket as follows:

```htmlembedded
<!-- Task Ticket -->

<div class = "main-cont">
     <!-- <div class = "ticket-cont">
         <div class = "ticket-color"></div>
         <div class = "ticket-id">12345</div>
         <div class = "task-area" contenteditable = "false">Random Task</div>
          <div class = "ticket-lock">
            <i class = "fa-solid fa-lock"></i>
          </div>
</div> -->
```
Now also give the styling to the task ticket:
```javascript
 .modal-cont{
   height: 50vh;
   width: 45vw;
   display: flex;
   background-color: lightsalmon;
   position: absolute;
   top:30%;
   left: 27%;
   display: none;
}
.ticket-cont{
    height: 12rem;
    width: 15rem;
    background-color: coral;
}
.ticket-color{
    height: 1rem;
}

.ticket-id{
    background-color: yellow;
    height: 2rem;
}
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/311/original/upload_39d93710a1f82436e4b11ae641ab6240.png?1695963264)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/312/original/upload_9a008ba1c7965ffce4d7f4ea2c2e34e2.png?1695963295)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/313/original/upload_2d430278f46b2c037ad120ae71d7a62c.png?1695963341)


This CSS code defines styles for a modal container and its associated ticket elements:

1. **.modal-cont:**
   - Defines the modal's dimensions and appearance.
   - Positioned absolutely with specific top and left offsets.
   - Initially hidden with `display: none`.
   - Has a flex display and a light salmon background color.

2. **.ticket-cont:**
   - Represents a ticket container.
   - Fixed height and width for each ticket.
   - Coral background color.

3. **.ticket-color:**
   - Represents a color strip on the ticket.
   - Fixed height and width, typically used for visual categorization.

4. **.ticket-id:**
   - Represents the ID section of the ticket.
   - Has a yellow background color and a specific height.

These styles appear to be used for creating a modal with tickets, each with a color strip and an ID section.


