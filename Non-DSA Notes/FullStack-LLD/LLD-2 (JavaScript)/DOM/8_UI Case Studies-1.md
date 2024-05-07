
## Agenda

- What is Event Propagation?
- Concept of Bubbling 
- Concept of capturing
- Machine coding question
    - Star Rating Component
    - Counter Component

We will try to cover most of these topics in today's sessions and the remaining in the next.

It is going to be a bit challenging, advanced, but very interesting session covering topics that are asked very frequently in interviews.

So let's start.


## Event Propagation
   Event propagation refers to the process of how events are dispatched and processed in the Document Object Model (DOM) hierarchy of elements in web development. There are two main phases of event propagation: capturing phase and bubbling phase. During these phases, events can propagate through the DOM tree from the root to the target element (capturing) or from the target element back up to the root (bubbling).

### Bubbling
   Event bubbling is one of the phases of event propagation in the DOM. When an event occurs on a DOM element, it first triggers the event handlers on the target element itself, then it bubbles up to its parent elements in the DOM hierarchy. This allows for the creation of more general event listeners that can be applied to parent elements to handle events from multiple child elements.

### Capturing
   Event capturing is the other phase of event propagation in the DOM. During the capturing phase, events start from the root element and propagate down to the target element. This phase occurs before the bubbling phase and can be useful when you want to capture events on parent elements before they reach their child elements.

Certainly, let's use an example to explain event bubbling and capturing with three nested `<div>` elements: `#grandparent`, `#parent`, and `#child`. Suppose you have the following HTML structure:

```html
<div id="grandparent">
  <div id="parent">
    <div id="child"></div>
  </div>
</div>
```

Now, let's say we attach a click event listener to each of these `<div>` elements and observe how event propagation works.

```javascript
const grandparent = document.querySelector('#grandparent');
const parent = document.querySelector('#parent');
const child = document.querySelector('#child');

grandparent.addEventListener('click', function() {
  console.log('Grandparent clicked');
});

parent.addEventListener('click', function() {
  console.log('Parent clicked');
});

child.addEventListener('click', function() {
  console.log('Child clicked');
});
```

Here's how the event propagation works during both the capturing and bubbling phases when you click on the `#child` element:

1. **Capturing Phase:**
   When an event occurs, it starts from the root element (`<html>`) and goes down the DOM tree. In this phase, the event handlers are triggered in the following order:

   1. `#grandparent` capturing
   2. `#parent` capturing
   3. `#child` capturing (target phase)

   However, we don't have capturing event listeners in this example, so nothing will be logged during this phase.

2. **Target Phase:**
   This is where the event reaches the target element, which is `#child`. The event handler for `#child` is triggered, and you will see the message "Child clicked" logged to the console.

3. **Bubbling Phase:**
   After the target phase, the event bubbles up through the DOM tree in the opposite direction. The event handlers are triggered in the following order:

   1. `#child` bubbling
   2. `#parent` bubbling
   3. `#grandparent` bubbling (root phase)

   As a result, you will see the messages "Parent clicked" and "Grandparent clicked" logged to the console, in that order.

So, the output in the console when you click on the `#child` element will be:

```
Child clicked
Parent clicked
Grandparent clicked
```

This example demonstrates the sequence of event propagation during both the capturing and bubbling phases in the context of nested `<div>` elements. The capturing and bubbling phases allow you to handle events at different levels of the DOM hierarchy.

Let's explore the event propagation using the `useCapture` parameter set to both `true` and `false` for the same example with the three nested `<div>` elements: `#grandparent`, `#parent`, and `#child`.

```javascript
const grandparent = document.querySelector('#grandparent');
const parent = document.querySelector('#parent');
const child = document.querySelector('#child');

grandparent.addEventListener('click', function() {
  console.log('Grandparent clicked (Bubbling)');
}, false);

parent.addEventListener('click', function() {
  console.log('Parent clicked (Bubbling)');
}, false);

child.addEventListener('click', function() {
  console.log('Child clicked (Bubbling)');
}, false);

grandparent.addEventListener('click', function() {
  console.log('Grandparent clicked (Capturing)');
}, true);

parent.addEventListener('click', function() {
  console.log('Parent clicked (Capturing)');
}, true);

child.addEventListener('click', function() {
  console.log('Child clicked (Capturing)');
}, true);
```

In this example, we've added event listeners with both capturing and bubbling phases for each of the three elements. The `useCapture` parameter is set to `true` for capturing and `false` for bubbling.

**Scenario 1: useCapture set to `false` (Bubbling)**

When you click on the `#child` element, the event will propagate in the bubbling phase. The order of event handling will be:

1. `#child` clicked (Bubbling)
2. `#parent` clicked (Bubbling)
3. `#grandparent` clicked (Bubbling)

The output in the console will be:

```
Child clicked (Bubbling)
Parent clicked (Bubbling)
Grandparent clicked (Bubbling)
```

**Scenario 2: useCapture set to `true` (Capturing)**

When you click on the `#child` element, the event will propagate in the capturing phase. The order of event handling will be:

1. `#grandparent` clicked (Capturing)
2. `#parent` clicked (Capturing)
3. `#child` clicked (Capturing)

The output in the console will be:

```
Grandparent clicked (Capturing)
Parent clicked (Capturing)
Child clicked (Capturing)
```

In both scenarios, the event propagation follows the sequence based on the capturing or bubbling phase, as determined by the `useCapture` parameter. Keep in mind that the capturing phase occurs before the bubbling phase and that events propagate through the DOM hierarchy accordingly.

### Event Propagation Cycle
The event propagation cycle refers to the sequence of phases through which an event travels within the Document Object Model (DOM) hierarchy. There are two main phases in the event propagation cycle: the capturing phase and the bubbling phase. Here's an overview of the cycle:

1. **Capturing Phase:**
   - The event starts at the root of the DOM tree (typically the `<html>` element).
   - The event travels down the DOM tree through each ancestor element of the target element.
   - During this phase, event handlers registered with the capturing phase (`useCapture` set to `true`) are triggered on each ancestor element in the order they appear in the hierarchy from the root to the target.
   - The event reaches the target element.

2. **Target Phase:**
   - The event reaches the target element for which the event was triggered.
   - Event handlers registered on the target element are executed.

3. **Bubbling Phase:**
   - After the target phase, the event travels back up the DOM tree in reverse order.
   - Event handlers registered with the bubbling phase (`useCapture` set to `false`) are triggered on each ancestor element in the reverse order from the target to the root.
   - The event eventually reaches the root of the DOM tree.

This cycle allows developers to define event listeners that respond to events at different levels of the DOM hierarchy. By using capturing and bubbling, you can efficiently manage and handle events on multiple elements without needing to attach individual listeners to each element.


Certainly, let's modify the example to demonstrate how to stop event propagation after the click event on the `#child` element using the `stopPropagation` method. Here's the updated code:

```javascript
const grandparent = document.querySelector('#grandparent');
const parent = document.querySelector('#parent');
const child = document.querySelector('#child');

grandparent.addEventListener('click', function(e) {
  console.log('Grandparent clicked (Bubbling)');
});

parent.addEventListener('click', function(e) {
  console.log('Parent clicked (Bubbling)');
});

child.addEventListener('click', function(e) {
  console.log('Child clicked (Bubbling)');
  e.stopPropagation(); // Stop propagation after clicking the child element
});
```

In this example, when you click on the `#child` element, the event propagation will be stopped after the event handler for the `#child` element executes. As a result, the event will not continue to bubble up to the parent and grandparent elements. Only the message "Child clicked (Bubbling)" will be logged to the console.

If you remove the line `e.stopPropagation();`, you'll see the standard bubbling behavior where the event continues to propagate, and you'll see all three messages in the console: "Child clicked (Bubbling)", "Parent clicked (Bubbling)", and "Grandparent clicked (Bubbling)".

Remember that stopping propagation can impact the expected behavior of event handling, so it should be used with caution and only when necessary.




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

For each problem, you'll need to design and implement a solution using the programming language of your choice. Make sure to consider the user experience, error handling, and any other relevant aspects. Depending on the context of the coding round, you might be required to write modular and efficient code, handle edge cases, and possibly interact with a user interface (if applicable).

### Creating a counter component
Firstly we will be discussing the problem statement of Creating a counter component that displays a number and has buttons to increment and decrement the number. The user should be able to click the buttons to increase or decrease the displayed number.

Certainly, here's a simple implementation of a counter app using HTML, CSS, and JavaScript that includes the functionalities you mentioned:

**HTML (index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles.css">
  <title>Counter App</title>
</head>
<body>
  <div class="counter">
    <button class="btn" id="decrement">-</button>
    <span id="count">0</span>
    <button class="btn" id="increment">+</button>
    <button class="btn" id="reset">Reset</button>
  </div>
  <script src="script.js"></script>
</body>
</html>
```

**CSS (styles.css):**
```css
body {
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

.counter {
  display: flex;
  align-items: center;
}

.btn {
  padding: 10px 15px;
  font-size: 18px;
  background-color: #3498db;
  color: #fff;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #2980b9;
}
```

**JavaScript (script.js):**
```javascript
const decrementButton = document.getElementById('decrement');
const incrementButton = document.getElementById('increment');
const resetButton = document.getElementById('reset');
const countDisplay = document.getElementById('count');

let count = 0;

decrementButton.addEventListener('click', () => {
  if (count > 0) {
    count--;
    countDisplay.textContent = count;
  }
});

incrementButton.addEventListener('click', () => {
  count++;
  countDisplay.textContent = count;
});

resetButton.addEventListener('click', () => {
  count = 0;
  countDisplay.textContent = count;
});
```

In this implementation, we have an HTML structure with buttons for decrementing, incrementing, and resetting the counter. The JavaScript code adds event listeners to these buttons to handle their respective functionalities. The counter value is displayed and updated in the `countDisplay` element. The CSS styles provide a basic look for the counter app.

Copy and paste the HTML, CSS, and JavaScript code into separate files (index.html, styles.css, script.js) in the same directory, and then open the index.html file in a web browser to see and interact with the counter app.

### Star Rating Component
Firstly we will be discussing the problem statement of Designing a star rating component that allows users to rate something using stars. The component should display a visual representation of the rating using filled and empty stars. Users can click on the stars to select a rating..

Absolutely, here's an explanation for the star rating component that includes comments in the JavaScript code to help you understand how it works:

**index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles.css">
  <title>Star Rating Component</title>
</head>
<body>
  <div class="rating">
    <!-- Display five stars, each with a data-value attribute representing its rating value -->
    <span id="stars">
      <span class="star" data-value="1">&#9733;</span>
      <span class="star" data-value="2">&#9733;</span>
      <span class="star" data-value="3">&#9733;</span>
      <span class="star" data-value="4">&#9733;</span>
      <span class="star" data-value="5">&#9733;</span>
    </span>
    <!-- Display the current rating -->
    <p>Rating: <span id="rating">0</span>/5</p>
  </div>
  <script src="script.js"></script>
</body>
</html>
```

**script.js:**
```javascript
// Get all star elements
const stars = document.querySelectorAll('.star');

// Get the rating display element
const ratingDisplay = document.getElementById('rating');

// Add a click event listener to each star
stars.forEach(star => {
  star.addEventListener('click', () => {
    // Get the value from the data-value attribute
    const value = parseInt(star.getAttribute('data-value'));
    // Update the rating display and stars based on the clicked value
    updateRating(value);
  });
});

// Function to update the rating display and filled stars
function updateRating(value) {
  stars.forEach(star => {
    // Get the value from the data-value attribute
    const starValue = parseInt(star.getAttribute('data-value'));
    // Toggle the 'filled' class based on whether the star's value is less than or equal to the selected value
    star.classList.toggle('filled', starValue <= value);
  });
  // Update the rating display text content
  ratingDisplay.textContent = value;
}
```

**styles.css:**
```css
body {
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

.rating {
  text-align: center;
}

.star {
  font-size: 24px;
  cursor: pointer;
  transition: color 0.3s ease;
}

.star.filled {
  color: gold;
}
```

In this star rating component, users can click on stars to indicate their rating. The JavaScript code adds a click event listener to each star, and the `updateRating` function toggles the "filled" class on stars based on their value compared to the selected rating. The CSS styles provide visual feedback by changing the color of filled stars to gold.

