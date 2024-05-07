
## Agenda

- What is Event Delegation?
    - Relation with concept of Bubbling 
- Machine coding question
    - Star Rating Component
    - Counter Component

We will try to cover most of these topics in today's sessions and the remaining in the next.

It is going to be a bit challenging, advanced, but very interesting session covering topics that are asked very frequently in interviews.

So let's start.

## Event delegation

Event delegation and event bubbling are closely related concepts that work hand-in-hand to optimize event handling in web development. When applied together, they provide an efficient way to manage interactions on a large number of elements.

Imagine you're browsing a website like Amazon, and on the product listing page, there are multiple product cards, each containing an "Add to Cart" button. Here's how event delegation and event bubbling come into play:

1. **Event Delegation:**
   Event delegation involves attaching a single event listener to a common ancestor element (in this case, the container holding the product cards). Instead of placing event listeners on each "Add to Cart" button individually, you attach one listener to the container.

2. **Event Bubbling:**
   Event bubbling refers to the natural propagation of an event through the DOM hierarchy. When an event occurs on a deeply nested element, it first triggers the event handler on that element and then "bubbles up" through its ancestors.

Now, let's see how these concepts work together:

- When a user clicks the "Add to Cart" button on a product card, the event starts at the button (target) and then bubbles up through its parent elements.
- Since you've attached a single event listener to the container holding the product cards, the event bubbles up to the container.
- The event listener captures the event at the container level and checks whether the clicked element (the button) matches certain criteria (e.g., having the class `add-to-cart`).
- If the criteria are met, the listener knows that an "Add to Cart" action is intended and can extract information about the specific product from the event's context

Let's go through an example with code to demonstrate event delegation and event bubbling using different categories of products (headphones, laptops, mobiles) on a web page:

**HTML Structure:**
```html
<div id="categories">
  <div class="category" id="headphones">
    <h2>Headphones</h2>
    <div class="product">Product A</div>
    <div class="product">Product B</div>
  </div>
  <div class="category" id="laptops">
    <h2>Laptops</h2>
    <div class="product">Product X</div>
    <div class="product">Product Y</div>
  </div>
  <div class="category" id="mobiles">
    <h2>Mobiles</h2>
    <div class="product">Product P</div>
    <div class="product">Product Q</div>
  </div>
</div>
```

**JavaScript:**
```javascript
const categoriesContainer = document.getElementById('categories');

categoriesContainer.addEventListener('click', (event) => {
  const clickedElement = event.target;
  
  // Check if the clicked element is a product
  if (clickedElement.classList.contains('product')) {
    const category = clickedElement.closest('.category').querySelector('h2').textContent;
    const product = clickedElement.textContent;
    
    console.log(`Clicked on ${product} in the ${category} category.`);
    // Handle the click action for the product here
  }
});
```

In this example:

- The `categoriesContainer` element is the common ancestor for all categories and products.
- The event listener is attached to the `categoriesContainer` to capture clicks on any of its child elements.
- When a product is clicked, the event bubbles up through the category section, reaching the `categoriesContainer`.
- The listener checks if the clicked element has the class `product`. If it does, it extracts the category and product information and performs the necessary action.
- This code efficiently handles clicks on products within any category, demonstrating the combined usage of event delegation and event bubbling.

With this setup, regardless of the number of categories or products, you only need one event listener to handle all clicks, making your code more maintainable and efficient.

Let's create an example where event delegation is used to change the background color of elements by clicking on them. In this example, we'll create a set of colored boxes, and clicking on any box will change its background color using event delegation.

**HTML Structure:**
```html
<div id="colorPalette">
  <div class="color-box" style="background-color: red;"></div>
  <div class="color-box" style="background-color: green;"></div>
  <div class="color-box" style="background-color: blue;"></div>
</div>
```

**JavaScript:**
```javascript
const colorPalette = document.getElementById('colorPalette');

colorPalette.addEventListener('click', (event) => {
  const clickedElement = event.target;
  
  // Check if the clicked element is a color box
  if (clickedElement.classList.contains('color-box')) {
    const color = clickedElement.style.backgroundColor;
    document.body.style.backgroundColor = color;
  }
});
```

In this example:

- The `colorPalette` element is the common ancestor for all color boxes.
- The event listener is attached to the `colorPalette` to capture clicks on any of its child elements.
- When a color box is clicked, the event bubbles up to the `colorPalette`.
- The listener checks if the clicked element has the class `color-box`. If it does, it extracts the background color of the clicked color box.
- The background color of the `body` element is then set to the extracted color, effectively changing the page's background color.

This example demonstrates how event delegation can be used to efficiently manage interactions across a set of elements, in this case, color boxes. By using event delegation, you handle all color box clicks with a single event listener, making the code cleaner and more maintainable.

Here are the problem statements for each of the machine coding round problems you mentioned:

1. **Star Rating Component:**
   Design a star rating component that allows users to rate something using stars. The component should display a visual representation of the rating using filled and empty stars. Users can click on the stars to select a rating.

2. **Counter Component:**

3. **Nested Comment System:**
   Build a nested comment system where users can leave comments on a post. Each comment can have replies, creating a nested structure. Users should be able to reply to comments and collapse/expand comment threads.

4. **Product Card Component:**
   Design a product card component that displays information about a product. It should include details like the product name, image, price, and a "Add to Cart" button. Users can click the button to add the product to their cart.

5. **OTP Input Section:**
   Implement an OTP (One-Time Password) input section where users receive an OTP via SMS or email and need to enter it to verify their identity. The component should provide a field for each digit of the OTP and handle the validation process.
   
### Nested Comment System
Firstly we will be discussing the problem statement of building a nested comment system where users can leave comments on a post. Each comment can have replies, creating a nested structure. Users should be able to reply to comments and collapse/expand comment threads.

**Nested Comment System: Overview**

A nested comment system allows users to leave comments on a post, and each comment can have replies, forming a threaded or hierarchical structure. Users should also be able to collapse and expand comment threads for better readability. This is commonly seen on social media platforms and discussion forums.

- **Nested Structure:** Comments are organized hierarchically, where each comment can have zero or more child comments (replies).
- **Collapse/Expand:** Users can collapse or expand comment threads to show or hide replies, improving readability for lengthy discussions.
- **Event Delegation:** Since comments can be added dynamically, event delegation is useful for handling interactions like replying and collapsing.

**HTML Structure:**

```<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles.css">
  <title>Nested Comments Example</title>
</head>
<body>
  <div id="comments">
    <div class="comment">
      <p>User A: This is a great post!</p>
      <button class="reply-btn">Reply</button>
      <button class="collapse-btn">Collapse</button>
      <div class="replies">
        <div class="comment">
          <p>User B: I agree!</p>
          <button class="reply-btn">Reply</button>
        </div>
      </div>
    </div>
  </div>
  <script src="script.js"></script>
</body>
</html>

```

**CSS:**

```css
.comment {
  margin: 10px;
  border: 1px solid #ccc;
  padding: 10px;
}

.reply-btn,
.collapse-btn {
  margin-right: 10px;
}

.all-comment:not(:first-child) {
  margin-left: 4rem;
}

```

**JavaScript:**

```javascript
const commentsContainer = document.getElementById('comments');

commentsContainer.addEventListener('click', (event) => {
  const clickedElement = event.target;

  // Handle replying to comments
  if (clickedElement.classList.contains('reply-btn')) {
    const comment = clickedElement.closest('.comment');
    const replyBox = document.createElement('div');
    replyBox.className = 'comment reply';
    replyBox.innerHTML = `
      <p><input type="text" placeholder="Your reply..."></p>
      <button class="submit-btn">Submit</button>
    `;
    comment.querySelector('.replies').appendChild(replyBox);
  }
  
  // Handle collapsing/expanding comment threads
  if (clickedElement.classList.contains('collapse-btn')) {
    const comment = clickedElement.closest('.comment');
    const replies = comment.querySelector('.replies');
    replies.style.display = replies.style.display === 'none' ? 'block' : 'none';
  }
});

commentsContainer.addEventListener('click', (event) => {
  const clickedElement = event.target;
  
  // Handle submitting replies
  if (clickedElement.classList.contains('submit-btn')) {
    const replyInput = clickedElement.closest('.comment.reply').querySelector('input');
    const replyText = replyInput.value;
    const newReply = document.createElement('div');
    newReply.className = 'comment';
    newReply.innerHTML = `<p>User: ${replyText}</p>`;
    clickedElement.closest('.comment.reply').appendChild(newReply);
    replyInput.value = '';
  }
});
```

**Explanation:**

- The HTML structure represents a simple comment system with reply and collapse buttons.
- The CSS provides basic styling for comments and buttons.
- The JavaScript code uses event delegation on the `commentsContainer`.
- When the "Reply" button is clicked, a new reply box is dynamically added under the corresponding comment.
- When the "Collapse" button is clicked, the replies are toggled to show or hide.

This example demonstrates a basic nested comment system. Depending on your requirements, you can expand this system to include user authentication, data storage, and more advanced features.

Assuming you integrate the provided HTML, CSS, and JavaScript code and open the HTML file in a web browser, here's what you can expect:

1. The page will display a comment with a "Reply" button and a "Collapse" button.
2. Clicking the "Reply" button will create a new reply box beneath the comment where users can input their replies.
3. Clicking the "Collapse" button will toggle the visibility of the replies.

For the sake of visualization, imagine that you see a page with a comment, and when you click the "Reply" button, a new reply box appears under the comment. If you click the "Collapse" button, the replies will be hidden, and clicking it again will show them again.

Please note that you'll need to create an HTML file and include the provided HTML, CSS, and JavaScript code within appropriate sections (HTML, `<style>` for CSS, and `<script>` for JavaScript) for this to work as intended.

In this example, the CSS rule .all-comment:not(:first-child) targets all elements with the class .all-comment except for the first one, and applies a left margin of 4rem to create an indentation effect. However, I noticed that your HTML structure uses the class .comment for comments, so I've updated the rule in the CSS accordingly.
``` css
.all-comment:not(:first-child){
margin-left:4rem;
}
```
You can place this CSS rule in your styles.css file to achieve the desired indentation for nested comments. Just ensure that the structure of your HTML matches the example provided.