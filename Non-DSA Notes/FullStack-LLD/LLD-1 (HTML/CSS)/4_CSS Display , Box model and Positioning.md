The topics we are going to cover in today's session are:
- Previous lecture recap with left topics
- CSS Fonts
- Box Model
- Display Property in CSS

So, let us start with the session.


So, in the previous lecture, we left the background color in CSS.
- It works the same as the color.
- You can add CSS code for background color as :
```HTML=
h1{
    background-color : blue;
}
```

## **Example**:

[IMAGE_1 START SAMPLE]
![](https://hackmd.io/_uploads/ryUXY8npn.png)
[IMAGE_1 FINISH SAMPLE]

Here you will select the class namely "background" and apply CSS to them. It will be reflected to all the **h1s** inside that div tag.

> `color` is used to change the text color but `background-color` is used to change the color area behind that text.

- You can also use an image as the text background. To do this, you need to provide the image URL in the CSS as shown below:
```HTML=
h1{
    background-color : url(" url_of_that_specific_image.jpg ");
}
```

You can set the background size as:
```HTML=
h1{
    background-color : url(" url_of_that_specific_image.jpg ");
    background-size : 400px;
}
```
- In the CSS background property, when it finds any empty space, it starts to repeat its element. You can use the property `background : no-repeat;` to avoid it. 
- -You can customize the repetition of the BG image using the X and Y axis. 

- You can customize various aspects of the font such as size, look, and many dynamics of it. Let us see them one by one.
- First, create a file as shown below:
  
[IMAGE_2 START SAMPLE]
![](https://hackmd.io/_uploads/rJ3VYLh62.png)
[IMAGE_2 FINISH SAMPLE]

Then we will apply CSS to the fonts. First, let us see font family.

## Font family
- The different types of font available in the CSS are termed as font family.
- The font-family property can hold several font names as a "**fallback**" system. If the browser does not support the first font, it tries the next font.
- Font family are like "times", "courier", "arial". If you want to use a single font from this, you can just remove the other font styles from the font family.
- Syntax:
```HTML=
.heading_1{
    font-family: your_desired_font
}
```

## Font weight
- This font property is used to decide the intensity of the font.
- It's value ranges from lightest **100px** to boldest **800px**.
- Syntax:

```HTML=
font-weight: 800px;
```

## Font size
- It refers to the size of the text.
- Syntax:
```HTML=
font-size: xx-larger;
```
```HTML=
font-size: 50%;
```

- There is also a font-style that you can choose to customize your font like bold, italic, etc.

## Google font
- If you are not unable to get the font requirement from the above font properties, then you can use the Google font option.
- You just need to go to the Google search and search "**google font**". Refer website: `https://fonts.google.com/`.
- Here you can find and choose the font. Click over the font and you will get a lot of options to customize that font.
- Click on "**select font_style**" and select the link there.
- Then paste it on your HTML file head tag as shown below.

[IMAGE_3 START SAMPLE]
![](https://hackmd.io/_uploads/Hyn8KInT3.png)
[IMAGE_3 FINISH SAMPLE]

- Now copy the font family from the Google font website and you can use it in the CSS.
- Since you have imported the Google fonts using API till now. Now you can just copy the font family from Google font and paste it at the font family section in the link of the head tag.

- Font and text can be seen as similar but they are not.
- Font focus on the look and styling but Text is the internal working of your text such as spacing, line width, etc.
- First, create a file of HTML is shown below

[IMAGE_4 START SAMPLE]
![](https://hackmd.io/_uploads/Sy-OFI263.png)
[IMAGE_4 FINISH SAMPLE]

First, let us see the text alignment property

## Text Alignment
- It is used to make the alignment of your text like from the left, from the right, or in the center.
- Syntax:

```HTML=
.heading_1{
    text-align : left;
}

```

## Text Decoration
- It is used to make your text attractive using some properties.
- These are oval-line, line-through, underline, etc.
- Syntax:

```HTML=
.heading_1{
    text-decoration : oval-line;
}
```

## Word Spacing
- It defines how many spaces are there between any two consecutive words.
- It is defined using the pixel values.
- Syntax:

```HTML=
.heading_1{
    text-decoration : oval-line;
    word-spacing : 100px;
}
```
## Line Height
- It defines the height between two consecutive lines.
- Syntax:

```HTML=
.heading_1{
    text-decoration : oval-line;
    word-spacing : 100px;
    line-height : 100px;
}
```
These are all text and font properties.


- Anything that we create in HTML and CSS takes the form of a box.
- You can check this by inspecting.
- Go to any website that we have created till now, select an html element paragraph and right click, then click on **inspect**. Here you see the boxing of your content in the right panel.

Always remember to add height and width to your box otherwise, it will not be visible. Make the box as shown below.

[IMAGE_5 START SAMPLE]
![](https://hackmd.io/_uploads/SkQYFU2a2.png)
[IMAGE_5 FINISH SAMPLE]

You can customize the size of the box by changing the height and width values.

> Take a real-life example of creating a township including steps like making land cut, house placing, etc. to discuss the box concept. And introduce `padding`.

## Padding
- It is the empty area inside the container.
- You can apply the padding outside your content but it should be inside your container box.
- Syntax to add padding:

```HTML=
h1{
    padding : 20px;
}
```
- **Increasing the padding** area **decreases the container** space. Because padding is only inside that specific container, it can not go outside of the box.


## Margin
- The CSS margin properties are used to create space around two different elements, outside of any defined borders.
- It prevents your elements from getting overlapped.
- Syntax:
- Create another box as in the previous example then,

```HTML=
.box_2{
    width: 100px;
    height: 120px;
    background-color: blue;
}
```
- There are already some margins by CCS default. But you can customize it as :

```HTML=
.box_2{
    width: 100px;
    height: 120px;
    background-color: blue;
    margin : 0px;
}
```
> You can use the universal selector (*) to apply the desired CSS property to all the elements.

Syntax: 
```
*{
   CSS_Property
}
```

## Applying Margins, Padding and Border 
- First, let us create three containers:

[IMAGE_6 START SAMPLE]
![](https://hackmd.io/_uploads/BkXsY836h.png)
[IMAGE_6 FINISH SAMPLE]

- The CSS that we apply in the containers will be applied to all the containers because they all have the same name.
- When you apply margin 20px, it gets reflected in the element from all sides.
- If you want to apply margin from a specific side say top, then :

```HTML=
.container{
    background-color : lightgreen;
    martin-top : 20px;
}
```
- Likewise, you can apply margin for **bottom**, **left** and **right** side too.

Now, let us apply padding.

- If you apply padding to the container, it gets reflected in the **div tag**. You can check by applying padding to the container.
- So, it should be avoided. Rather it is best practice to **apply padding to the elements** by targeting the element separately in the style tag  as:

```HTML=
h1{
    padding : 20px;
}
```

Coming to margins,
- If can apply four values to the margin property as `margin : 10px 20px 30px 40px;` it will be reflected as `margin : top right bottom left`
- You can try using different margin values to see the different results. 
- If you pass three values to the margin property and forget the last value, as `margin: 10px 20px 30px;`, then it will be reflected as "10 px for top and 20 px as left and right both and 40px for bottom".
- If you pass two values to the margin property as `margin : 10px 20px;`, then it will be reflected as "10px for top and bottom, and 20px as left and right.

> All these concepts are similar for **padding**. You just need to use padding in place of margins. And the rest of the rules will be the same.


## Border
- Border is defined as that extra space that you can create around your HTML elements.
- There are many types of borders such as **solid**, **dashed**, **dotted**, etc. that you need to define in the syntax to see it.
- Syntax:

```HTML=
.container{
    background-color : lightgreen;
    martin-top : 20px;
    border : 2px solid red;
}
```
### Border Alignment Properties
- border-top : 5px solid blue ;
- border-left: 2px solid red;
- border-right: 6px dashed green;
- border bottom: 5px solid red;

### Border Radius Properties
- It is used to apply curved edges to the borders
- Syntax:

```HTML=
border-radius : 20px;
```
You can also apply this radius to a specific side of the border for example : `` border-top-right_radius: 20px;``


> These are the all properties and concepts (Margins, Padding, and Borders) that together are termed as "**Box Model** in CSS".




# Question
What is the order of values when passing all four values in the margin?
# Choices

- [ ] top right left bottom
- [ ] right left top bottom
- [ ] top bottom left right
- [x] top right bottom left


> Summarizing
- Everything that we create in an HTML is taken as a Box known as **Box Model**.
- It will have two dimensions that are Height and Width. 
- And these boxes have three properties that are **Margin**. **Padding**, and **Border**.



First, let us create a file as shown below to understand the working of the Display property:

[IMAGE_7 START SAMPLE]
![](https://hackmd.io/_uploads/H1pRtL2T3.png)
[IMAGE_7 FINISH SAMPLE]

> Note: Rem is also a unit to define pixels. It converts the pixel into 10 times. For example **5rem** is **50px**.


When you see the output you can see that the border is taking the whole area of paragraphs. But it should be on the paragraph **p1** only.

Now, let us add a span tag to the file as shown below:

[IMAGE_8 START SAMPLE]
![](https://hackmd.io/_uploads/Bk8TjInTh.png)
[IMAGE_8 FINISH SAMPLE] 

When you run this file, You can see that these **span tags** are not acting as a paragraph. This means that there are no borders applied to it.

Now, give this span tag border, height, and width property as :

```HTML=
span{
    border: 2px solid blue;
    height: 50px;
    width: 50px; 
}
```
Now give the p tag height and width as :

```HTML=
p{
    border: 2px solid red;
    height: 50px;
    width: 50px;
}
```
You can see in the output that there are no changes seen in the span tag.

> Note: Block elements can have customizable height and width but you can not provide height and width to the inline elements (**span tag** in this case). 


Here comes the need for **Display property**

- Add a random image to the file using **img src tag**.
- Also add an anchor tag entitled "click me".
- You can see that you can provide customizable height and width to the image. Here, it is working as both inline and block elements.
- CSS allows the user to add all of these tags as a Display property.
- Syntax:

```HTML=
p{
    display : inline;
}
```
This makes your element an **inline-block**. That's the work of the Display property in CSS. After that, you can provide height and width to the inline elements too.


