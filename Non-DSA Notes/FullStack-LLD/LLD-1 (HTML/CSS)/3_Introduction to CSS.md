# Agenda:
- What is CSS
- Need for CSS
- CSS Selectors
- Properties of CSS (color, background, fonts, and texts)

So, lets start!


>Various ways of using CSS
They are: 
1. Inline
2. Internal
3. External


These are the things that we will discuss. Now, let us see them one by one.


- Create a basic HTML file and add a heading **h1** inside the body tag entitled: "Heading 1" and open it in a browser to show how it looks.
- Now, let us see how to add CSS to this element.


# Steps to add style tag:
- Add `<style>` and `</style>` tag inside the head tag of your HTML file. Inside this **style** tag, you can use all the CSS stylings.
- Select the element that you need to add CSS.
- For example, h1 and add curly braces to it. Inside this, you can define the CSS properties as shown below:

```HTML=
h1{
    color : brown;
}



# Using CSS in three different ways:

## 1. Internal CSS 
- When you write CSS in the same HTML file. (using the style tag)


## 2. Inline CSS
- It is writing CSS for a particular element. (using style attribute.) 

### Example
```
<h2 style = "color: red;"> I am heading 2 </h2>
```
- Here we are providing the CSS to that specific element "h2" only, known as Inline CSS. Always try to add a style tag inside the **head tag**.
- Inline CSS has more priority than Internal CSS.


## 3. External CSS
- You can create a separate file for CSS having the extension "**.css**".
- Here you do not need to use any HTML tag. You can directly write your CSS and properties.

### Example

```HTML=
H3{
    color: green;
}
```
To reflect these CSS into your HTML file, you need to link that CSS file to the HTML file.
- Use the "link" tag to do this as shown below.

```
<link rel="CSS_file_name" href="./CSS_file_name.css">
```
- You can add the file location in the **href** to add the CSS file if it is at some other location in your system.

> These are the three ways that can be used to apply CSS to your HTML file. Now we will discuss the ways of selecting a particular element.


- As we have seen in the previous example, **h1{}** was the selector. But there are more ways of selecting elements.
- Have a brief discussion about how the students can select an element as the previous method that we learned till now.

## Descendent selectors
- Anything down the order can be termed as a descendent. For example, a father is the descendent of their child.
- Now, you need to select the obvious list as shown in the image and make it blue color.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/035/original/upload_741aa927d48eecd0dcd6ec59f15eba43.png?1695311213)


- For that first discuss the "**descent selector**". 
- When you select **ol li{}** as the selector then all the elements will get blue. So you need to select the specific parents that are "div" as shown in the example.

- We will write the selector as:
```HTML=
div li{
    color: blue;
}
```
Now moving to Children Selectors.

## Children selectors
Let us take an example as shown below.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/036/original/upload_6e331819a556124295cda866b1ad80df.png?1695311277)


There are two span tags. Here we need to make the text "I am the direct son" blue using CSS.

- Use the greater than **">"** symbol to use direct children.

```html=
div > h1 > span{
    color: blue;

}
```
- It means that you are directing to apply CSS to the span element that is directly children to the **h1**.

Let's see another type of selector which is the Classes

## Classes

- It is a very important part when you are learning CSS.
- Classes are defined as separate entities of similar elements.
- For real real-life example, if you are in class 10, then all the students there should be in class 10 only.
- Similarly, in CSS, similar elements having the same behavior are separated in a specific class as shown below code:


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/037/original/upload_130e57374ed680b30734deba9ee0b2c7.png?1695311313)


- We use dot (.) to select a class and apply CSS to them. Here the name of the class is test so we will apply CSS to this class as below:

```HTML=
.test{
    color: blue;
}
```
This will be applied to both the elements of the class namely the **test**.

> Discuss a question having two different classes namely **class1** and **class2** and apply CSS on them to make one class **blue** and one class **red**.
- Solution:
```HTML=
.class1{
    color: blue;
}:

.class2{
    color: red;
}
```
### Question on multiple classes

Suppose a situation when there are two or more than two classes for a single element as shown below and you have to make some specific elements blue.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/038/original/upload_1a43d7aa8cd4e546b6264e88799e956b.png?1695311389)


- Here we need to select multiple classes **m1** and **m2** and make them blue.
- Solution:
```HTML=
.m1.m2{    <!-- it is multiple selector -->
    color : blue;
}
```
Here you will use multiple classes as shown in the example to apply the CSS to some specific elements in such cases.

### Question on a combination of all the previously discussed selectors.

You have to make the text "**I'm here, find me**" blue as shown in the question image below. Feel free to use any selector or combination of selectors you want.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/039/original/upload_e17f8e227f4328a482d1cc22803e0dc5.png?1695311505)



- **Solution**:

```HTML=
.c1 .c2{
    color: blue;
}
```

### Question on Class with Children Combinator

In this question you need to make the select and make the text "**I'm a direct son**" blue.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/041/original/upload_6e8bceeaca78cf983eb897650d522316.png?1695311598)


- **Solution**:
```HTML=
.c1>p{
    color: blue;
}
```

### Question on id selector
- The id selector uses the id attribute of an HTML element to select a specific element.

- The id of an element is unique within a page, so the id selector is used to select one unique element.
- We use "#" to address the id.


### Example

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/042/original/upload_0a85830042d3f0d832f66b0c11e9ab40.png?1695311661)

- You need to select **s2** with the "id=the-one" and make blue

- Solution:
```HTML=
#the-one{
    color: blue;
}
```

### Question on attribute selector

- CSS attribute selectors are used to select and style HTML elements with the specified attributes and values.
- Let us take an example as shown below. Here we need to select the button element and make the color blue.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/044/original/upload_106e606616e173b79a0a71bd501d9812.png?1695311699)


- **Solution**:
```HTML=
input[value="Select me"]{
    color: blue;
}
```
Here you can write the element like "input" and start the bracket "[]". Inside the bracket, you can write the attribute that you are selecting to apply CSS.

- That's how the attribute selector works.

# 1. Normal Color 
- The very basic way of using colors is as follows as we have discussed earlier that is `h1{color: color_name;}`
- Using this method you can use the 140 colors of CSS. But what do you need to use a color apart from these 140 colors?

# 2. RGB
- Then we use the **RGB value** to change the element colors. 
- RGB is the color concept that shows how you can create any color using a definite proportion of these three colors that are **Red**, **Green**, and **Blue**.
The range of RGB values is from **(000 to 255)**.

Let us take an example how to use RGB values for CSS.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/045/original/upload_001bf16ebd83d5ea0df12fc19d263397.png?1695311917)
[

- You can also add **opacity** property where you pass the RGB values. 
- Range of opacity is from (0.00 to 1.00)
- For example-

```HTML=
color : rgba(255, 165, 100, 0.50);
```



# 3. Color code (Hexadecimal code)
- Color codes are three-byte hexadecimal numbers (meaning they consist of **six digits**), with each byte, or pair of characters in the Hex code, representing the intensity of **red**, **green**, and **blue** in the color respectively.
- We have hex code for every color in CSS.
- You can find these codes on Google search also.


- You can use these hex codes to paste into your CSS thing.
- Remember to apply hashtag **"#"** before the codes. For example- **#DC143C** 

Now, let us see the 4th method of CSS Colors.

# 4. HSC 
- It stands for **Hue**, **Saturation**, and **Lightness**.

## Example
```HTML=
h2{
    color : hsl(100%, 15%, 25%)
}
```
- In this, we define these three properties in percentage.



# Final Question of the session

Now, let us summarize the session and use all the previous selectors and color properties to solve this problem shown below:


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/046/original/upload_cf0319b7c90943234aa84a26a0e8ff6f.png?1695312027)


- **Solution**:
First, we will add a style tag and then write all the CSS provided in the question like this:


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/047/original/upload_2ea1f412f739128739787f0498ccba03.png?1695312161)


Coming to the point 6 of the question. Let us first see what is pseudo selector.

## Pseudo selector
- When you hover over any element and it changes its behavior, it is known as a Pseudo selector.
- For example, if you go on a sign-in button it becomes popped up.

```HTML=
a.hover{
    color : hsla(100%, 15%, 25%, 0.6)
}
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/048/original/upload_14bb1001ae9af53dda59aa7200cd2c8f.png?1695312197)

