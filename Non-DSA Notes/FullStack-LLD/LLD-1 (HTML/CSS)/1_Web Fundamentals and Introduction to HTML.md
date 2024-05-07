
## Introduction

When we think about accessing a website, there's more happening behind the scenes than meets the eye. The URL, or Uniform Resource Locator, is what we usually type into the address bar to access a web page. However, the URL represents much more than just a web address. It's a pathway to the actual resource we're trying to access on the internet.


## Process
To break it down, when we enter a URL, the full form of URL comes into play: **Uniform Resource Locator**. This term accurately describes what it does — it locates a specific resource on the internet. This resource could be anything from a text document to a video, and the server's job is to provide us with that resource.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/110/original/upload_06940025115633bec555d541d722b876.png?1695109040)


A **server**, in this context, isn't a physical location but rather a program running somewhere in the world. This program generates the website content for us. It's important to note that a server is not a database. Rather, it's a responsive entity that resides somewhere in the vast expanse of the digital world. Imagine it as a helpful entity that receives your request and promptly serves you the requested information.


## Dairy Farm Analogy
Here's an analogy to help clarify the roles involved: Imagine you own a dairy farm and have numerous customers who regularly place orders for dairy products. To manage this influx of orders, you have an **operations team** that handles the order-taking process. They ensure that customers' requests are recorded accurately and are then forwarded to the **production team**.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/111/original/upload_9cef5b39282b29f01216e706282bbb64.png?1695109075)


In the context of websites, the operations team can be likened to the **DNS (Domain Name System)** system. The DNS system acts like an operations team, taking in requests and translating them into specific IP addresses. Think of DNS as a phonebook for the internet. When you enter a domain name like "scaler.com," the DNS system translates it to an IP address that points to a particular server.

However, it's important to note that the server itself is not where the data comes from. Instead, it's comparable to the dairy farm in our analogy—it's responsible for assembling and providing the products. In our website world, the actual data resides in a **database**. This database is akin to a **warehouse** for the dairy farm. All the products are stored there, ready to be accessed when needed.

When a request is made, the server applies specific protocols and data logic to retrieve the necessary information from the database. This process is what ensures that we receive the correct data as a response to our request.

Bringing it all together, the customers in our dairy farm analogy represent clients or users of the website. The operations team corresponds to the DNS system, efficiently directing requests. The dairy farm itself serves as the server, assembling and providing the desired information. And finally, the warehouse embodies the database, housing all the necessary data for the website.

In the grand scheme of things, even though we might simply see a website's interface through our browser, there's a complex interplay of components behind every web page that ensures we get the right information at the right time.


### HTML boiler plate code

#### Code
```html
<!doctype html>
<html lang = "en">
  <head>
    <meta charset = "utf - 8">
    <meta name = "viewport" content = "width = device - width, initial - scale = 1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world ! </h1>
  </body>
</html>
```

### Structure your code
#### Div
Div elements are often used to structure and style sections of a web page, making it easier to apply CSS styles or JavaScript functionality to specific groups of content.

#### Code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Basic HTML</title>
</head>
<body>
    <div>
        <h2>Welcome to Scalar Topics</h2>
        <p>
         We're glad you're here
        </p>
    </div>
</body>
</html>
```
#### Output

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/112/original/upload_b1f0471a9f3040bdd40eb364e9101835.png?1695109208)

#### Section
Sections are used to structure the content of a web page into logical parts, such as chapters, articles, or different sections of a document.

#### Code: 
```html
<!DOCTYPE html>
<html>
<head>
    <title>Basic HTML</title>
</head>
<body>
    <section>
        <h2>Section Title</h2>
        <p>This is a section of content.</p>
        
    </section>
</body>
</html>
```
### Tags and buttons

### Header tags

Header tags are used to structure the hierarchy of content on a webpage, with `<h1>` typically being the main title and `<h2>`, `<h3>`, and so on used for subsections. They help improve the accessibility and readability of content.
    
#### Code:

```html
<h1>Main Heading</h1>
<h2>Subheading</h2>
<h3>Sub-subheading</h3>
```

#### Output

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/113/original/upload_0666ce092529c955114832a23824d462.png?1695109287)

#### Anchor tags
Anchor tags are used to link to other web pages or resources, both within the same website or externally to other websites.

#### Code:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Basic HTML</title>
</head>
<body>
    <section>
        <a href = "https://www.scaler.com/topics/autoboxing-in-java/">Learn autoboxing - in - java</a>
    </section>
</body>
</html>

```
#### Output

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/114/original/upload_a280807eb2f3df89d88691096051f0eb.png?1695109351)

#### Image tags
Image tags are used to display graphics, photographs, icons, or any other visual content on a webpage. The alt attribute provides alternative text for accessibility and SEO purposes.

#### Code:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Basic HTML</title>
</head>
<body>
   <img src = "img.jpg" alt = "Description of the image">
</body>
</html>
```
#### Output
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/115/original/upload_4f0ea4a42e75394bc79c854cbe6cafce.png?1695109387)

#### Buttons
Button elements are used to create clickable elements that can trigger actions when clicked, such as submitting a form or triggering JavaScript functions.

#### Code:
```html
<button type = "button"> BUTTON </button>
```
#### Output
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/116/original/upload_e873e3ecb310330c64503dafcf33ad53.png?1695109456)


