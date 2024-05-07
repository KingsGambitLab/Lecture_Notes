

## Agenda

Today we will be discussing about positioning and flexbox in CSS.

We will talk about Flexbox and responsive later, So first let's start with positioning in CSS.

So let's start.



**[Ask the learners]**
What do you understand when we talk about positioning or position?

> **Note to Instructor:** Wait for 5-10 seconds to get some answers and then continue

The concept of positioning in CSS can be understood by  arrangement of players on a sports field. Imagine football or cricket field. 

**Think of a scenario in football:** you have a center forward positioned at one spot, and you'll find the center midfielder occupying another specific spot. This arrangement of players in different positions is scattered over the field.

Similarly, in CSS, positioning involves placing elements within a web page layout. Just as players are situated precisely on the field, web elements can be located using various CSS positioning techniques. 

Now that we know what is positioning in CSS. We will be now discussing types of position in CSS.



So, let's understand two types of position in CSS:
* **Absolute Position**
* **Relative Position**

Think about a table you have in front of you. Imagine you're looking straight down at the table. It's just a flat square surface, like the top of the table. This is the place where you might put things, like your phone or a cup of coffee.

What we're going to talk about is how you can move this "cell phone" around on the table in two different ways.

**[Ask the learners]**
Can anyone tell what are the two ways we can move this cell phone on table.

When we talk about moving the box around, we're talking about changing its position in these two main directions – X-Axis and Y-Axis. These two coordinates, X and Y, help us understand exactly where the box (or any object) is located on the table.

Let's say you start with the cell phone placed at a specific spot on the table. Now, you want to move it a bit. In CSS terms, this is done by specifying how many centimeters (like pixels) you want to move the box from its current position. 

For example, if you move the box 10 centimeters to the right. So the relative position of the cell phone from its starting point to ending point has changed by 10 cm.

If you are measuring the distance from the starting of the Table. The distance between starting of the table and the cell phone will be the absolute position.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/071/original/upload_189ab829bb663b192a1033cb2dbf5b52.png?1695317443)

So we can define in terms of CSS as:

* **Relative Position:** The element is positioned relative to its previous position.
* **Absolute Position:** The element is positioned absolutely to its parent container.

> **Tip to Instructor:** Ask learners if they have any doubt.


Now, that we know what is Relative and Absolute Positioning. Let's move forward by coding and understanding positions.


Now let's move to VS Code and write some code to understand it better.

> **Tip to instructor:** Make a boilerplate code by creating 4 boxes and use those boxes for explaining position property. While writing the code, make sure to explain each line to the learners.

**HTML Code:**

```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Positioning</title>
    <style>
        .container {
            background-color: dodgerblue;
        }

        .box {
            display: inline-block;
            height: 150px;
            width: 150px;
            background-color: tomato;
            margin: 10px;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

Now lets target this 3rd box and apply position property on it. 

### Exercise 1

#### Problem Statement
Give **static** position value to box 3.

#### Solution
* we can give a separate id to the box3, say box_3.
* Now, in style tag, we can use position property and set the value as **static.**

#### Pseudocode
```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Positioning</title>
    <style>
        .container {
            background-color: dodgerblue;
        }

        .box {
            display: inline-block;
            height: 150px;
            width: 150px;
            background-color: tomato;
            margin: 10px;
        }
        
        #box_3 {
            position: static;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box" id="box_3">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

Static is the default position in which all the elements are positioned, so it will do nothing to the position of box3

There are 5 positions in CSS that we will talk about:

* static
* relative
* absolute
* fixed
* sticky

Now lets give it relative position.

### Exercise 2

#### Problem Statement
Give **relative** position value to box 3 and move it 20px.

#### Solution
* In style of box_3, we can use position property and set the value as **relative** along with top property as 20px.

#### Pseudocode
```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Positioning</title>
    <style>
        .container {
            background-color: dodgerblue;
        }

        .box {
            display: inline-block;
            height: 150px;
            width: 150px;
            background-color: tomato;
            margin: 10px;
        }
        
        #box_3 {
            position: relative;
            top: 20px;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box" id="box_3">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

Now, it will move 20 pixels from the top. We're instructing the box to move '20 pixels down from your original position at the top'.


> **Tip to instructor:** Use different-different values to explain relative value to learners and ask learners if they have any doubt or not.


Now lets give it absolute position.

### Exercise 3

#### Problem Statement
Give **absolute** position value to box 3 and move it 20px.

#### Solution
* In style of box_3, we can use position property and set the value as **absolute**.

#### Pseudocode
```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Positioning</title>
    <style>
        .container {
            background-color: dodgerblue;
        }

        .box {
            display: inline-block;
            height: 150px;
            width: 150px;
            background-color: tomato;
            margin: 10px;
        }
        
        #box_3 {
            position: absolute;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box" id="box_3">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

> **Tip to instructor:** This box 4 vanishing case can be tricky for learners. so take time explaining this.


Now, we can see that box 4 has vanished but "box 4" could be positioned directly underneath "box 3", and because of the overlap, "box 4" might be hidden by "box 3".

If we want "box 4" to be visible and not hidden by "box 3", you might need to adjust the positioning of box 3 and give some top value as 100px.

```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Positioning</title>
    <style>
        .container {
            background-color: dodgerblue;
        }

        .box {
            display: inline-block;
            height: 150px;
            width: 150px;
            background-color: tomato;
            margin: 10px;
        }
        
        #box_3 {
            position: absolute;
            top: 100px;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box" id="box_3">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

Now, we can see it is moving down, so that means box3 is now trying to adjust with the window itself.

In this case, the element box3 is removed from the normal document flow. The other elements will behave as if that box3 is not in the document. No space is created for the element in the page layout. The values of left, top, bottom and right determine the final position of the box3.

Now box3 is not trying to move relative to its original position, it will try to move relative to the window, means from the entire top of the window it is taking 100px. 

> **Tip to instructor:** Now use right, left and bottom properties to explain it better.

Now lets understand what fixed position is.

**Fixed position:** 
* Fixed Position is basically when your Element will take a place with the Respect to the window and it will not move from there.
* Fixed-positioned element is "fixed" in a specific location on the screen, and it won't move when the user scrolls up or down the page. This can be useful for creating elements that should always be visible, like navigation bars or call-to-action buttons, regardless of where the user is on the page. 
* The element will maintain its position relative to the viewport's coordinates, providing a consistent visual reference point as the user interacts with the content.

### Exercise 4

#### Problem Statement
Give **fixed** position value to box 3 and fix it at the bottom of the scrollable page.

#### Solution
* In style of box_3, we can use position property and set the value as **fixed**.
* For fixing it to the bottom of the page, we can give right property as 4px and bottom as 1px.

#### Pseudocode
```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Positioning</title>
    <style>
        .container {
            background-color: dodgerblue;
            height: 4000px;
        }

        .box {
            display: inline-block;
            height: 150px;
            width: 150px;
            background-color: tomato;
            margin: 10px;
        }
        
        #box_3 {
            position: fixed;
            right: 4px;
            bottom: 1px;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box" id="box_3">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

Now if we scroll the page, the box3 will be fixed at the bottom right of the page.

> **Tip to instructor:** Ask the learners, if they have any doubts

Now, lets understand sticky value:

**Sticky:**
* When an element is given a "position" value of "sticky," it acts like a relative-positioned element within its containing element until a certain scroll threshold is reached. Once the user scrolls beyond that threshold, the element becomes "stuck" in place and behaves like a fixed-positioned element, remaining visible on the screen. 
* In other words, a sticky element starts as part of the normal document flow, just like a relatively positioned element. As the user scrolls, the element follows its normal position until it reaches a designated point (usually when its top or bottom edge reaches a specific distance from the viewport's edge). At that point, it becomes "sticky" and remains fixed at that position while the rest of the content scrolls.

Lets go to the zomato website and see its navbar, here you can see when we scroll the page, this navbar is getting fixed at the top of the page.

So on reaching a particular value, sticky gets fixed.

### Exercise 5

#### Problem Statement
Give **sticky** position value to box 3 and fix it at the top of the scrollable page.

#### Solution
* In style of box_3, we can use position property and set the value as **sticky**.
* For fixing it to the top of the page, we can give top property as 0.

#### Pseudocode
```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Positioning</title>
    <style>
        .container {
            background-color: dodgerblue;
            height: 4000px;
        }

        .box {
            display: inline-block;
            height: 150px;
            width: 150px;
            background-color: tomato;
            margin: 10px;
        }
        
        #box_3 {
            position: sticky;
            top: 0;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box" id="box_3">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

Now if we scroll the page, the box3 will behave normally will it touches the top and them it becomes fixed to the top of the page.


Now let's talk about Flex box.

**Flex Box:**
* Flex box stands for flexible box
* liberty to align and Justify our Elements with just some line of code but you need to think graphically.
* It's a layout model in CSS that makes arranging elements a whole lot easier. 
* With flexbox, you have a container that holds your elements, and it's like your shelf. Inside this container, you can use the power of flexbox to control how your elements behave.

Flexbox is just a concept of CSS that makes your life very easy.

> **Note to instructor:** Now use the below boilercode to start with explaining flex.

Now, lets create some boxes again in HTML to start with flexbox.

```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox</title>
    <style>
        .container {
            background-color: tomato;
            border: 2px solid black;
            height: 500px;
            width: auto;
        }

        .box {
            height: 100px;
            width: 100px;
            background-color: dodgerblue;
            margin: 10px;
        }
        
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

So this is the basic boxes that we made similar to above.

Now lets use the **display: flex;** property in the parent container

```css
.container {
    background-color: tomato;
    border: 2px solid black;
    height: 500px;
    width: auto;
    display: flex;
}
```

When you apply the CSS property display: flex; to an element, you're essentially creating a flex container. This container establishes a flex formatting context for its child elements, or "flex items." This means that the child elements within this container will follow the rules and behaviors defined by the flexbox layout model.

Default property of flex box is to arrange all the elements in the row as you can also see here.

You can also use many flex-direction property to arrange the elements in different ways.

> **Note to instructor:** Use different-different values with flex-direction property like row, column, row-reverse, column-reverse etc, to explain it better.

You can also use this important property called **justify-content**.

**justify-content:** Defines how flex items are distributed along the main axis (horizontal for row layout, vertical for column layout). 

So if we want to center all the row items, we can use **justify-content: center**

```css
.container {
    background-color: tomato;
    border: 2px solid black;
    height: 500px;
    width: auto;
    display: flex;
    justify-content: center;
}
```

The justify-content: center; property applied to a flex container in CSS aligns its child elements **horizontally** at the center of the container along the main axis. 

But there is 1 more property that is used to align items vertically that is **align-items**.

> **Note to instructor:** Explain the axis using the below diagram. diagram refence: https://css-tricks.com/snippets/css/a-guide-to-flexbox/

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/073/original/upload_1ec9fd4a198aa44de652e4864bd69a53.png?1695317491)

**[Ask the learners]**
If I say, I want my flex direction is row, what will be my main axis?

- X axis

**[Ask the learners]**
And If I say, I want my flex direction is column, what will be my main axis?

- Y axis

Now lets take more examples of **justify-content** property.

> **Note to Instructor:** Explain each of the values with examples.

* **justify-content: flex-start;**
    * Flex items are aligned at the beginning of the container (left for a row layout, top for a column layout).
* **justify-content: flex-end;**
    * Flex items are aligned at the end of the container (right for a row layout, bottom for a column layout).
* **justify-content: center;**
    * Flex items are centered along the container's main axis.
    * Equal space is added before the first item and after the last item, creating a balanced appearance.
* **justify-content: space-between;**
    * Flex items are evenly spaced along the main axis.
    * The first item aligns with the container's start, the last item aligns with the container's end, and equal space is added between the items.
* **justify-content: space-around;**
    * Flex items are evenly spaced along the main axis, with space distributed around them.
    * Space is added before the first item, after the last item, and between each pair of items.
* **justify-content: space-evenly;**
    * Flex items are evenly spaced along the main axis, with equal space added between them.
    * Equal space is added before the first item, between all items, and after the last item.

There are many options for this property, you can choose to play around with all of them.

Now lets understand **align-items** property.

The **align-items property** lets you control how flex items are positioned on the cross axis within the container.

> **Note to Instructor:** Explain each of the values of align-items with examples.

* **align-items: flex-start;**
    * Flex items align at the start of the cross axis (top for row layout, left for column layout).
    * No additional space is added between items and the container's cross axis edge.
* **align-items: flex-end;**
    * Flex items align at the end of the cross axis (bottom for row layout, right for column layout).
    * No additional space is added between items and the container's cross axis edge.
* **align-items: center;**
    * Flex items are vertically centered along the cross axis.
    * Equal space is added above and below the items, creating a balanced appearance.
* **align-items: baseline;**
    * Flex items are aligned along their text baselines.
    * This value can be useful when items have varying font sizes or text content.
* **align-items: stretch;**
    * Flex items are stretched to fill the container's cross axis.
    * If no height is explicitly set on the items, they will take up the full height of the container.



**[Ask the learners]**
If flex-direction if set to row and justify-content is center, which direction it will align?

- Horizontally

Now, we have covered two important properties, justify-content and align-items. Now we will move formward with some interesting properties.


**[Ask the learners]**
Do you know what is a responsive website?

- A responsive website is a website that can work of different screen size and can adapt to those different screen sizes. It responds and adjusts its layout, images, and content to fit the screen it's being viewed on, whether that's a desktop computer, tablet, or smartphone.

Lets take an example to scaler's website

> **Note to Instructor:** Navigate to https://www.scaler.com/ and show its responsiveness

If you minimize the screen, you can see that everything is changing according to the screen size. Design is not breaking and is adapting to the screen size whether it is mobile view or the desktop view.

> **Note to Instructor:** Now to explain screensize better, you can navigate to our HTML page and show different mobile and responsive views in inspect tab.

In inspect tab of our HTML website, we can check how our website will look in different dimensions and screen sizes.

If we decrease the screen size, we can see that the boxes are shrinking. That means it is not responsive, There are various properties in flex box that we can use to make our website responsive.

In the current scenario the boxes are getting shrinked but if I don't want it to shrink and I want them to adjust according to the screen size, for that we can use some CSS properties.

There is 1 property know as **flex-wrap**

**flex-wrap:** The flex-wrap property in flexbox controls whether flex items should wrap onto multiple lines within the flex container when there's not enough space to fit them all on a single line. 

So if we use the above code with flex-wrap property, we can see that the boxes are now responsive and not shrinking.

```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox</title>
    <style>
        .container {
            background-color: tomato;
            border: 2px solid black;
            height: 500px;
            width: auto;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;

        }

        .box {
            height: 200px;
            width: 200px;
            background-color: dodgerblue;
            margin: 10px;
        }
        
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

> **Note to Instructor:** Now create more boxes to expain **flex-wrap** property better.


The flex-wrap property is especially useful when dealing with responsive layouts. It allows you to control how flex items reorganize when the available space changes. For example, if you have a row of cards and they don't fit on a smaller screen, setting flex-wrap: wrap; would cause them to stack vertically, creating a more readable layout.

Here's what each value of flex-wrap does:

* flex-wrap: nowrap;
    * This is the default value.
    * Flex items will stay on a single line, even if they cause overflow. They won't wrap to the next line.
* flex-wrap: wrap;
    * When there's not enough space for all items on a single line, flex items will wrap to the next line. They will stack vertically if needed.
* flex-wrap: wrap-reverse;
    * Similar to wrap, but the wrapping happens in reverse order. The last flex item becomes the first item on the new line, and so on.


Now we can discuss about item wise flex box,For now we were using flex box in container but now we will use flex box within the container items 


> **Note to Instructor:** Navigate to https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-properties-for-the-childrenflex-items and explain that we can use flex properties for children items.


There is 1 property called **order** that is used for ordering the items.

The **order** property in flexbox allows you to control the visual order in which flex items appear within a flex container, regardless of their order in the HTML markup. It's particularly useful for reordering items for different screen sizes or creating unique visual layouts. H

lets give the order property to box1, and see what happens:

```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox</title>
    <style>
        .container {
            background-color: tomato;
            border: 2px solid black;
            height: 500px;
            width: auto;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;

        }

        .box {
            height: 200px;
            width: 200px;
            background-color: dodgerblue;
            margin: 10px;
        }

        .box1{
            order: 5;
        }
        
    </style>
</head>

<body>
    <div class="container">
        <div class="box box1">1</div>
        <div class="box">2</div>
        <div class="box">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

Now you can see that the box1 is ordered at the last.

let's understand this with an example:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/074/original/upload_738cab0d87a85a216d67986e5105b3e4.png?1695317536)

Suppose, we gave order: 4 to box1 and order: 2 to box3.

> **Note to Instructor:** So the question is how will the boxes arrange themselves?

* box1 has the order 4, so it will go at last.
* box3 has order 2, so it will go at third.
* box 2 will be at 2nd position 
* box1 will be at first.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/075/original/upload_e5323381ac5d2c537cd4459693a88763.png?1695317559)

Now lets' understand flex-shrink property. 

The **flex-shrink** property in flexbox determines how flex items shrink when the container's available space is limited. It defines the ability of an item to shrink in relation to other items in the container when the container's size is reduced. 

let's understand this with an example:

We are providing flex-shrink property as 2 to box3.

```htmlembedded
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox</title>
    <style>
        .container {
            background-color: tomato;
            border: 2px solid black;
            height: 500px;
            width: auto;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;

        }

        .box {
            height: 200px;
            width: 200px;
            background-color: dodgerblue;
            margin: 10px;
        }

        .box3{
            flex-shrink: 2;
        }
        
    </style>
</head>

<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box box3">3</div>
        <div class="box">4</div>
    </div>
</body>

</html>
```

Now, whenever we are downsizing the screen box will be the first one to shrink the most.

Similarly there is a property called flex-grow

**flex-grow:** 
* This defines the ability for a flex item to grow if necessary. It accepts a unitless value that serves as a proportion. It dictates what amount of the available space inside the flex container the item should take up.

> **Note to Instructor:** Show the similar example as flex-shrink.

lets see a basic example:

```htmlembedded
.box3{
    flex-shrink: 2;
}
```

Now the box3 will grow the most on increasing the screen size

> **Note to Instructor:** Now ask for doubts to the learners about the doubt that came up during the class.
