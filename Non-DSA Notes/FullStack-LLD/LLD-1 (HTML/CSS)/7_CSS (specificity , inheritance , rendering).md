# CSS Cascading, Specificity, Inheritance and Overflow


### Introduction

Before starting with the topic, let us understand the simple definition of *Priority and Specific*. These two words create a concept in CSS that is known as Specificity.

**Priority:** Suppose three tasks are to be done. All the tasks can be arranged based on the task that has to be done first. The task with the highest priority will be on the top.

**Specific:** Suppose you are diagnosed with fever then the doctor prescribes you with some medicines that are *particular* to the disease i.e., fever. 


### What is Cascading in CSS?

Cascade is defined as top-to-bottom flow.

*Example:* 
```css!
.h1{
    colour: red;
}
.h1{
    colour: blue;
}
```
The output will be blue because cascading always goes down therefore blue comes later therefore priority will be given to the later part.

**CSS Cascading involves Specificity and Inheritance which will be covered in this lecture.**



### Specificity

To understand specificity let's take an example.

**First**: Create an HTML file to understand specificity.
**Second**: Create an unordered list of let's say "fruits".

```htmlembedded!
<body>  
    <ul>
        <li>Apple</li>
        <li>Mango</li>
        <li>Orange</li>
    </ul>
</body>
```

**Third**: Assign 'id' and 'class' to your unordered list.

```htmlembedded!
<body>
    <ul id = "fruits">
        <li>Apple</li>
        <li class ="favourite">Mango</li>
        <li>Orange</li>
    </ul>
</body>
```

**Fourth**: Using CSS, make the colour of the class "favourite" blue.

The Selector will be id i.e., "fruits" Inside this id select a list element and then a specific class i.e., "favourite".

```htmlembedded!
<style>
    ul#fruits li.favourite{
      color: blue;  
    }    
</style>
```

**Fifth**: Using CSS, change the colour of the unordered list to blue as well.

```htmlembedded!
<style>
    ul#fruits li.favourite{
      color: blue;  
    }    
    
    ul#fruits li{
        color: blue;
    }
</style>
```

**[Ask the learners]**

What will happen if we change the colour of the unordered list to blue after changing the colour of class "favourite" to red?

```htmlembedded!
<style>
    ul#fruits li.favourite{
      color: red;  
    }    
    
    ul#fruits li{
        color: blue;
    }
</style>
```

--> The result will be that **"Mango" will be of red** colour and the rest list elements will be blue because it is using the **Specificity** property.
Hover over the selector `ul#fruits li` you will see "Selector Specificity: (1,0,2)".

Before understanding the Selector Specificity values: 

**[Ask the learners]**

What if the style attribute is applied in the list tag with class = "favourite"?

```htmlembedded!
<body>
    <ul id = "fruits">
        <li>Apple</li>
        <li class ="favourite" style= "color: yellow;">Mango</li>
        <li>Orange</li>
    </ul>
</body>
```

--> The result will be that **the value of Mango will turn to "yellow"** and the rest of the list elements will remain blue because the style attribute does not get affected by the style tag.

### Understanding values in specificity

Specificity can have **four** values if the style attribute is also included.



| Style attribute | IDs | Classes | Elements |
| :--------: | :--------: | :--------: | :---------: |

#### How to count specificity?

The selector `ul#fruits li` has "Selector Specificity: (1,0,2)". But how?

There is 1 ID i.e., fruits. There is no class added in the selector. There are 2 elements in the selector: ul and li. Therefore the value will be (1,0,2).

Similarly, the value of the selector `ul#fruits li.favourite` is (1,1,2).

#### How does the Selector Specificity make sure what selector should be applied?

> Remove style attribute from the list element with class = "favourite".

By comparing both the Selector Specificity values box by box: we see the value of the selector `ul#fruits li.favourite` is (1,1,2) which means it has 1 class while the other selector has no class. Therefore, the `ul#fruits li.favourite` selector will be applied.

**[Ask the learners]**

Arrange them from the least effective to the most effective selector.
1. `.test`
2. `h1.test`
3. `#try`
4. `h1`

--> **4<1<2<3** is the order.

Let's compare the values of each one of them.
1. `.test` - It has one class. Therefore, the value is (0,1,0).
2. `h1.test` - It has one class and one element. Therefore, the value is (0,1,1).
3. `#test` - It has one ID. Therefore, the value is (1,0,0).
4. `h1` - It has one element. Therefore, the value is (0,0,1).

**[Ask the learners]**

Calculate the value of the Selector Specificity of the following selector.
`#try ul div.test h2{}`

--> **(0,1,1,3)**

ID - #try
Class - .test
Element - ul, div, h2

| Style attribute | ID| Class|Element|
| :--------: | :--------: | :--------: | :-------: |
| 0| 1   | 1  |3|

**[Ask the learners]**

Calculate the value of the Selector Specificity of the following selector.
`#try span img .test .main header`

--> **(0,1,2,3)**

ID - #try
Class - .test, .main
Element - span, img, header

| Style attribute | ID| Class|Element|
| :--------: | :--------: | :--------: | :-------: |
| 0| 1   | 2 |3|

> You can use [Keegan](https://https://specificity.keegan.st/) to calculate Specificity value.


### Keyword - `!important`

If the keyword !important is used then it follows the cascading rule regardless of the Specificity Value. Use this keyword only once in a selector. If it is used twice for the same selector then the Specificity rule will be followed.

#### Example

```css!
ul#fruits li.favourite{
      color: red;  
    }    
    
ul#fruits li{
      color: blue !important;
    }
```

All the list elements will turn into a blue colour regardless of the Specificity Value.

> Priority of Inline CSS will be more than Internal CSS and External CSS.

> The priorities of the External CSS file and Internal CSS file can be changed by following the cascading rule. That means, whatever comes later will be followed.


### CSS Inheritance

#### Definition
As the last names are inherited in a family same way inheritance works in CSS which inherits some property from the parent.

We will be looking at the four properties - **Default, Inherit, Initial and Unset**.

Let's take an example where we create an unordered list and add href to all the list elements:

```htmlembedded!
<ul>
    <li>Default <a href="">Link</a> Color </li>
    <li>Inherit <a href="">Link</a> Color </li>
    <li>Initial <a href="">Link</a> Color </li>
    <li>Unset <a href="">Link</a> Color </li>
</ul>
```

First, Let's assign classes to the three properties: Inherit, Initial and Unset.

```htmlembedded!
<ul>
    <li>Default <a href="">Link</a> Color </li>
    <li class = "class-1">Inherit <a href="">Link</a> Color </li>
    <li class = "class-2">Initial <a href="">Link</a> Color </li>
    <li class = "class-3">Unset <a href="">Link</a> Color </li>
</ul>
```

### Inherit Property

Inherit is defined as the properties inherited from the parent. The properties applied to the parent are inherited by the child. 

For example

```htmlembedded!
<style>
    div{
        color: blue;
    }
</style>
<body>
    <div>
        <h2>
            Heading
        </h2>
    </div>
</body>
```

The result will be that the heading tag will inherit the colour that is applied to the div element as it is the parent of the h2 tag.

If the parent is not specified then the parent will always be the body tag by default.

To understand it better, let's take "class-1" from our unordered list of inheritance properties and apply `color: inherit` to the anchor tag.

```css!
body{
    color: red;
}
.class-1 a{
    color: inherit;
}
```

The term inherit means that whatever the colour of the parent tag is **(the default colour of CSS is black in most browsers)**, will be applied to the anchor tag of class: class-1 as well.

### Initial Property

The initial property will always take the default properties.

```css!
body{
    color: red;
}
.class-1 a{
    color: inherit;
}
.class-2 a{
    color: initial;
}
```

The color of the class-2 anchor tag will take the default color i.e., black.

> There exists properties that cannot be inherited like display, and columns etc., You can check [w3schools](https://https://www.w3schools.com/cssref/css3_pr_columns.php) for more details on the properties.

### Unset property

Unset depends on the inherited value.
Unset checks if any properties in the body can be inherited will be inherited.

For example:

```css
body{
    color: red;
    display: inline;
}
.class-1 a{
    color: inherit;
}
.class-2 a{
    color: initial;
}
.class-3 a{
    color: unset;
}
```


### CSS Overflow

When the content goes out of the container is known as **Overflow**.

Let's take an example where we create a div element and add content of 100 words to it. We create a container and give it a static width and height.

```htmlembedded!
<style>
    .content-box{
        border: 2px solid tomato;
        width: 200px;
        height: 200px;
    }
</style>
<body>
    <div class = "content-box">
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a.
    </div>
</body>
```

The result will be that the box will not contain the whole content and it will create an overflow condition. Therefore, we will use overflow to overcome it. We can use auto, hidden, scroll and visible overflow properties.

#### Example

Let's understand how:

```htmlembedded!
<style>
    .content-box{
        border: 2px solid tomato;
        width: 200px;
        height: 200px;
        overflow: hidden; /* the content going outside of the container will be hidden */
    }
</style>
<body>
    <div class = "content-box">
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a.
    </div>
</body>
```

#### Properties of Overflow

**Hidden**: The content that remains outside the container will be hidden or not visible. It does not occupy space where the content is hidden.

**Scroll**: A scroll bar is added inside the container so that you can go through the whole content inside the container.

**Auto**: It works similarly to scroll the only difference is that scroll will always show scroll inside the container while auto will only show when the content is overflowing.

**Visible**: It will make the content visible. There will be no change.

> The container takes only the space designated to it. Therefore, the overflow content will overlap with the other content added after the container.

**[Ask the learners]**

How will we apply the overflow condition if we make the container horizontal for the following div content?

```htmlembedded!
<div class = "horizontal-content">
    Scaler
</div>
```

--> 
```htmlembedded!
<style>
    .horizontal-content{
        font-size: 30px;
        width: 50px;
        height: 30px;
        
        border: 2px solid black;
        
        overflow: hidden;
    }
</style>
```

We can add any other property as well it will work similarly to the vertical container.

> If you want to hide the vertical or horizontal scroll bar you can use the following syntax: `overflow-x: hidden;` or `overflow-y: hidden;`.

