# Introduction to Document Object Model

#### Definition
Dom is a tree structure in which every HTML element is arranged in heirarchical order.

#### Example

```htmlembedded
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <div>

        <h1>This is heading 2</h1>

    </div>

    <div>

        <h1>This is heading 1</h1>

        <p>This is Paragraph</p>

    </div>
</body>
</html>

```

#### Output

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/258/original/upload_364afb8e43132cd223c90b39c021e52a.png?1695145205)


#### DOM tree visualization of above example

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/259/original/upload_604c9f192818c3459c15d376d0569b83.png?1695145257)

**Note:**
* We will be uisng javascript to put the interactivity in our web apps or websites.
* JavaScript is used to put interactivity in DOM elements.


#### Question

On clicking the button append hello to the page.

#### Solution

**Step 1:**  Slecting html element

To select oe identify a particular html element we have methods.
* getElementById
* QuerySelector
* QuerySelectorAll


**Code:** Using getElementById

```htmlembedded
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <button id = "btn - 1"> Say Hello </button>

    <script>
    
        // on clicking the button append hello to the page

        let btn = document.getElementById('btn-1')
        console.log(btn)

    </script>
</body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/260/original/upload_a6d7d3c5b18e7b6ed529ca4088ae1dee.png?1695145319)


**Code:** Using getElementsByClassName

```htmlembedded
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <button class = "btn - 1"> Say Hello </button>

    <script>
    
        // on clicking the button append hello to the page

        let btn = document.getElementsByClassName('btn - 1')
        console.log(btn)

    </script>
</body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/261/original/upload_a6d7d3c5b18e7b6ed529ca4088ae1dee_%281%29.png?1695145383)


**Code:** Using querySelector by ID

```htmlembedded
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <button id = "btn - 1"> Say Hello </button>

    <script>
    
        // on clicking the button append hello to the page

        let btn = document.querySelector('#btn - 1')
        console.log(btn)

    </script>
</body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/262/original/upload_7fbdad793912e0939837795b61709f36.png?1695145503)

**Code:** Using querySelector by class

```htmlembedded
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <button id = "btn - 1"> Say Hello </button>
    <button class = "btn - 1"> Say Bye </button>

    <script>
    
        // on clicking the button append hello to the page

        let btn = document.querySelector('.btn-1')
        console.log(btn)

    </script>
</body>
</html>

```

**Output:**
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/265/original/upload_4718ed7f5720b3cee58f8644ee6a62d2.png?1695145596)


**Code:** Using querySelector by elements

The document method querySelector() returns the first element within the document that matches the specified selector, or group of selectors. If no matches are found, null is returned.

```htmlembedded
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <button id = "btn - 1"> Say Hello </button>

    <script>
    
        // on clicking the button append hello to the page

        let btn = document.querySelector('button')
        console.log(btn)

    </script>
</body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/266/original/upload_a6d7d3c5b18e7b6ed529ca4088ae1dee_%282%29.png?1695145709)

**Step 2:** hello should get appended

**What is an event?**
Anything that happens depending on some other thins is an event. Let's say you are clicking on button then something will happen (hello is getting printed).  

**Method - addEventListener:** We can add any event to any of our elements with using addEventListener method.  


```javascript
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <button id = "btn - 1"> Say Hello </button>

    <script>
    
        // on clicking the button append hello to the page

        let btn = document.querySelector('#btn-1')
        console.log(btn)

        btn.addEventListener('click', function(e){
            
            // console.log(e)

            let divElem = document.createElement('div')

            divElem.innerText = 'Hello'

            let body = document.querySelector('body')

            body.appendChild(divElem)

        })

    </script>
</body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/267/original/upload_c04b7917d2c7dd94fad263612d3bae02.png?1695145825)

#### Append Hello DOM Tree

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/270/original/upload_604c9f192818c3459c15d376d0569b83.png?1695145889)


#### Question

Fix the list by inserting the missing element using querySelectorAll and insertBefore

#### Solution

**Step 1:** creating node list

**Note:** Node list is an array like structure which will have your elements in indexed form stored.  

```javascript
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        
        <li>8</li>
        <li>9</li>
        <li>10</li>
    </ul>

    <script>
        // Fix the list by inserting the missing element using querySelectorAll and insertBefor

        let allItems = document.querySelectorAll('li');
        console.log(allItems);      

    </script>
</body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/271/original/upload_fc8a7cf791547f64129ac0eef13aa66e.png?1695146016)

**Step 2:** adding element 

```javascript
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        
        <li>8</li>
        <li>9</li>
        <li>10</li>
    </ul>

    <script>
        // Fix the list by inserting the missing element using querySelectorAll and insertBefore

        let ourList = document.querySelector('ul');
        console.log(ourList);

        let allItems = document.querySelectorAll('li');
        console.log(allItems);   
        
        let indexThatHas8 = allItems[6];

        let sevenElement = document.createElement('li')
        sevenElement.innerText = '7'

        ourList.insertBefore(sevenElement, indexThatHas8)

    </script>
</body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/273/original/upload_9cda233672dc980dc39259973628c350.png?1695146091)


#### Question

Fix the mathmatical problem using JS 

#### Solution

```javascript
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0">
    <title>Document</title>
</head>
<body>
    <!-- Q. Fix the mathmatical problem usng JS <br> -->
    <p>2 + 2 = 22</p>

    <script>
        let para = document.querySelector('p')
        para.innerText = `2 + 2 = 4`
    </script>
    
</body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/274/original/upload_7e599ac46343deed76441a6ec8a415e8.png?1695146150)


#### Question

Write a script which fetches the data-color attribute of the card and double clicking on them and attahces the fetched class to that card and also changes the data-color attribute to "used"

#### Solution

**classList:** An element can have multiple classes attached to it and all of those classes are collected in a structure called classList.

Example:

```javascript
<div class = "card test blue"> Our card </div>

```

The classList for this div will be - [card, test, blue]

```javascript
<!DOCTYPE html>
<html lang = "en">
  <head>
    <meta charset = "UTF - 8" />
    <meta http - equiv = "X - UA - Compatible" content = "IE = edge" />
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0" />
    <title>Document</title>
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        padding-top: 5rem;
      }

      .blue {
        background-color: blue;
        box-shadow: 0px 0px 6px 5px;
      }

      .green {
        background-color: green;
        box-shadow: 0px 0px 6px 5px;
      }

      .red {
        background-color: red;
        box-shadow: 0px 0px 6px 5px;
      }

      .card {
        border: 1px solid;
        height: 10rem;
        width: 10rem;
        margin: 2rem;
      }
    </style>
  </head>

  <body>
    <div class = "card" data-color = "blue"></div>  
    <div class = "card" data-color = "red"></div>
    <div class = "card" data-color = "blue"></div>
    <div class = "card" data-color = "red"></div>
    <div class = "card" data-color = "red"></div>
    <div class = "card" data-color = "blue"></div>
    <div class = "card" data-color = "green"></div>
    <div class = "card" data-color = "blue"></div>
    <div class = "card" data-color = "green"></div>
    <div class = "card" data-color = "blue"></div>
    <script>
      // Q Write a script which fetches the data-color attribute of the card on 
      //double clicking on them and attaches the fetched class to that card.
      // Also changes the data-color attribute to "used"

      let cardsNodeList = document.querySelectorAll('.card')

      console.log(cardsNodeList)

      for(let i = 0 ; i < cardsNodeList.length; i ++ ){
        cardsNodeList[i].addEventListener('dblclick' , function(e){
          console.log(e.currentTarget)
           let classTobeAttached = e.currentTarget.getAttribute('data-color')

           console.log(classTobeAttached)

           e.currentTarget.classList.add(classTobeAttached)
           e.currentTarget.setAttribute('data-color' , 'used')

        })
      }
    </script>
  </body>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/276/original/upload_108dfa145e3eef14525de6578e2be0f0.png?1695146343)
