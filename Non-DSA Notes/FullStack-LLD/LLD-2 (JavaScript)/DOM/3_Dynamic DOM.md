# Dynamic DOM (Consume and work with an API)



## Agenda
* Create a weather app using an API.
* We will be using the "weather API" for getting the data of real-time weather and use that data in our app. 
* Pre-requisites required for this app include **JSON**, **API** which will be covered in this lecture itself. 



### JSON
* It stands for JavaScript Object Notation which is a data representation format.
* Let us consider an example to understand. Suppose, you have a farm and you sell products like vegetables, fruits, eggs etc. When a customer comes, everything is organized in different sections. You won't be storing everything inside a single container. It will be segregated like this- 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/288/original/upload_ec216d48c7ab4156e45c07960e9bb9c4.png?1695148844)

When a customer demands a product, that particular product will be given to them. In the same way, an API also works. 

**API**
* Stands for **Application Programming Interface**.
* It is an interface where all the data and protocols can be stored in a section-wise manner. 
* Just like the above example in the way we served the request to the customers, the data will be saved in an interface called as API
* Consider that apart from the customers, the you also cater to the needs of a restaurant by providing them with the products that they need. 
* In this way, the demands of both customers and restaurant gets their demands fulfilled.
* These customers are basically **clients**. The shops are nothing but **servers**.
> Ask the students if they are familiar with the concept of client and server. 

* The data is being requested from an external factor. Whatever the client needs, he will seek that from the external source. 
* There are different use cases of various data and it is impossible to store it in a single place. 

**Key points**
* API acts as a bridge between client and server. 
* It has huge sets of data that can be used for applications.
* API not only has data, but also has protocols, method implementations etc. 

#### Example
Consider you want to order a burger from Zomato or Swiggy. You decide to order it from Burger King. For that, Zomato will need to use the API of burger king to get the data of Burger king. 

* This data is coming from the API.
* The API is stored in JSON format.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/289/original/upload_53dd165cb742742e9f97796f9941eaf0.png?1695148884)


> Ask students if they have heard about APIs, then mention that some of the experienced folks might have heard about this. Earlier, REST APIs and SOAP APIs were used to store data and write APIs. Now JS devs thought about introducing JSON which is similar to the JS Syntax.


**Key points**
* JSON stands for JavaScript Object Notation. 
* It has a format similar to that of objects in JS. It has key-value pairs.
* The value can be obtained by using a key.
* The JSON file should end with '.json' extension. 


>Open VSCode and create a Farm.json file.

Coming to the previous example, a farm can have name, registration number, number of goods etc. There are many farms as such. **We want to create a dataset of all the farms where we can see data of each individual farm.**


#### Code

First start with this code, and tell the students to ensure that the **keys** are enclosed in **double quotes** so that it does not throw an error. 
```javascript

[
    {
        "name":"Farm 1",
        "products":["Eggs","Milk","vegetables"],
        "registrationNo":1234,
        "Employees":70,
        "isOperating": true
    }
]
```

This is the first object. Whenever we are creating different objects within the same JSON file, ensure that the **keys remain the same** for all the objects. They should **not change**. 

The code for 3 farms is-
```javascript

{
    {
        "name":"Farm 1",
        "products":["Eggs","Milk","vegetables"],
        "registrationNo":1234,
        "Employees":70,
        "isOperating": true
    },
    {
        "name":"Farm 2",
        "products":["Eggs","Milk","Cheese"],
        "registrationNo":12345,
        "Employees":60,
        "isOperating": false
    },
    {
        "name":"Farm 1",
        "products":["vegetables"],
        "registrationNo":12346,
        "Employees":30,
        "isOperating": true
    }
    
}
``` 

> Show some examples of APIs to the students. Tell them that we will be creating a weather app today and open it. 
> https://www.weatherapi.com/
> Inform that they need to sign-in.

* Find the API key and paste it under the **API explorer** tab. 
* Select the protocol as **HTTPS**.
* Click on show response. You can see the JSON format in the response section.

Proceeding to our code, create an `index.html` file. Inside the script tag, paste the above JSON code.

```javascript
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
    <title>Document</title>
</head>
<body>
    <script>
        let data = [
    {
        "name":"Farm 1",
        "products":["Eggs","Milk","vegetables"],
        "registrationNo":1234,
        "Employees":70,
        "isOperating": true
    },
    {
        "name":"Farm 2",
        "products":["Eggs","Milk","Cheese"],
        "registrationNo":12345,
        "Employees":60,
        "isOperating": false
    },
    {
        "name":"Farm 1",
        "products":["vegetables"],
        "registrationNo":12346,
        "Employees":30,
        "isOperating": true
    }
    
]
console.log(data)
</script>
</body>
</html>
```

You will see an array of objects. This is not in the JSON format. To obtain the JSON format, we will enclose the objects in backtick. 

**Key points**
* To convert JSON to JavaScript readable code, we use the **JSON.parse()** method
* The data received from a web server is a string, so to convert we use the JSON.parse() method to convert to a JavaScript object. 
* When working with APIs, we get everything in string, so to parse that JSON, we use the JSON.parse() method. 


>Brief the students about the steps to sign up on the https://www.weatherapi.com/. Ask them to do it accordingly. 

* After logging in, there will be an API key generated which will be unique for everyone. Copy that key first.
* Under **API Response Fields**, you can check all the fields that the API is providing. There are many options available. 
* Under **API Explorer**, paste the key. You will see the API Call as follows.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/292/original/upload_b1ce9393b8bd6d8ad8c11d66a121acac.png?1695149012)


Here the "q" stands for **query** and here we are querying for London. The call is basically our URL and inside this we also have our API key and the search query. 

* Apart from the current data, you can also get the Forecast, Future data as provided by the API. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/293/original/upload_04a31b2878e550d5e6bf91f446d29778.png?1695149064)



> Inform the students that For this project, we will be focusing on the JS part, so the CSS part has already been created and we just have to paste it. 
> Guide the students about the final interface before starting the code. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/294/original/upload_29da4001046dbfb1550deb5c6acdfa5b.png?1695149088)


**Step 1**
Create `index.html`, `style.css` and `index.js` files in VSCode. 

**Step 2**
Inside the `index.html` file, we will be creating various divisions for various parameters like temperature, location, time and date etc. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/295/original/upload_a9c73804d050f6a0f077c520dcb3203b.png?1695149109)

In the other division for weather condition, we will display an emoji along with the weather condition. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/296/original/upload_89a96e16ee00ec649a4e80c5b3f90cc8.png?1695149128)

**Step 3**
Create a form which contains an input field and a button also. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/297/original/upload_7ba43e5dbf022aa0a217332ecc9afad7.png?1695149155)

> Write a step-by-step code for each step. 

**Code**
```javascript
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF - 8">
    <meta http-equiv = "X - UA - Compatible" content = "IE = edge">
    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
    <title>Weather app Class</title>

    <link rel = "stylesheet" href = "style.css">
</head>
<body>

     <div class = "container">
         <div class = "weather">
             <div class = "temp">20</div>
             <div class = "time_location">
                 <p>Location</p>
                 <span>Random time and Date</span>
             </div>

             <div class = "weather_condition">
                  <p><img src = "" alt = ""></p>
                  <span>Condition</span>
             </div>
         </div>
     </div>


     <nav>
         <form>
             <input type = "text" placeholder = "Search_location" class = "searchField">
             <button type = "submit">Search</button>
         </form>
     </nav>


</body>

<script src = "index.js"></script>
</html>
```

Execute the above code, the output is

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/298/original/upload_d0356ec9757a7bebdf0714ff51d749dd.png?1695149252)

This is a simple HTML code, we will have to add CSS to style it.

> Inform the students that we will not focus on the CSS part as it is simple. We will just paste the code. 

**Style.css**-
```css
@import url("https://fonts.googleapis.com/css2?family=Economica&family=Grape+Nuts&family=Roboto:wght@100;300;400;700;900&display=swap");

* {
  margin: 0%;
  padding: 0;
  font-family: "Roboto", sans-serif;
}

.container {
  width: 100%;
  height: 100vh;
  background-color:#01161E;
  display: flex;
  justify-content: center;
  align-items: center;
}


.weather {
  z-index: 2;
  display: flex;
  align-items: center;
  color: white;
}

.weather > div {
  margin: 0.625rem;
}

.weather1 {
  font-size: 4rem;
}

.weather p {
  font-size: 2rem;
}
.weather span {
  font-size: 0.75rem;
}

.weather3 span {
  margin: 0.3rem;
}

.weather3 img {
  width: 2rem;
}
nav {
  height: 100px;
  padding: 1rem 0;
  position: absolute;
  bottom: 0%;
  width: 100%;
  background-color: rgba(180, 177, 177, 0.202);
  display: flex;
  justify-content: center;
  align-items: center;
}

nav form {
  width: 70%;
  grid-template-columns: 5fr 1fr;
  display: grid;
}

.searchField {
  font-size: 1.1rem;
  outline: none;
  color: white;
  background-color: transparent;
  padding: 1rem 0;
  border: none;
  border-bottom: 2px solid white;
  width: 98%;
}

nav form button {
  background-color:#4ECDC4;
  font-size: 1.1rem;
  color: white;
  outline: none;
  border: none;
  cursor: pointer;}
```

After executing the CSS code, the output is

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/299/original/upload_f0509cd60bb58737e5373d70d48b4648.png?1695149282)

**Index.js**-

We will see how to get data from an API. We will use the **fetch API**. The **fetch()** method will be used here.
> Type fetch method in the browser and just show the docs as a glimpse. 

The URL will be passed to the fetch() method as a parameter. We will understand how to use the fetch() method inside our JS code.

We will be coming across various terms like async, await but they will be covered in depth in the later lectures.

Before diving deep into the fetch() method, we will understand the try and catch block which is a pre-requisite for this.

The try block is used to execute the code that might encounter an error. An error can lead to unexpected termination of the program. Hence we put it inside the try block and any error that might be encountered by the try block is sent to the catch block. This is the exception handling concept. 

In the try block, we will define the URL which is the API call. 

```javascript
 let url = `https://api.weatherapi.com/v1/current.json?key=35af7ff606db422880d141328231305&q=${target}&aqi=no`
 ```
Here we have wrapped the url in backticks so that we can use the string template literals which denoted bt the `${}` symbol. 

* Let us understand using a real-life analogy about asynchronous programming. 

* Suppose you are teaching a batch of 100 students. One student asks doubt and it takes 5 minutes to resolve it. Another student asks a doubt which takes another 5 minutes. One more student asks a doubt and it takes 5 minutes. To solve the doubts of 3 students, 97 students has to waste their 15 minutes.

> Ask the students what could a better approach for this?

* A better approach is to teach first and in the last few minutes of the lecture, take up the doubts of the students. In this way, the time of the other students is not wasted. 

* Now just replace students with functions. The first approach is the synchronous programming where everything happens in a sequence. 

* In synchronous programming, important instructions get blocked due to some previous instructions, which causes a delay in the user interface. **Asynchronous** code execution allows to execution next instructions immediately and **doesn't block the flow** because of previous instructions.

**Key points**
* In APIs, we will be using the asynchronous JS. 
* We will be using **async** and **await** keywords which are important. 
* The **async** keyword needs to be added before the function which tells the function that it is asynchronous. 
* The **await** keyword tells that it needs wait till the data comes. 

```javascript
const response = await fetch(url)
```

Now let's run the code till now. 

```java
let target = "Pune"
async function fetchData(target){
    try {
        let url = `https://api.weatherapi.com/v1/current.json?key=8b6d5f63a04a485fa5351525232908&q=${target}&aqi=no`

        const response = await fetch(url)

        console.log(response)
    }
    catch(error){
        console.log(error)
    }
}

fetchData(target)
```

We will obtain this

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/300/original/upload_f06df9d4a4683805954bb656a39fe8f5.png?1695149320)

This is not in the JSON format. We will have to convert this to JSON by using the **.json() method**. 

We will add this line-
```javascript
const data = await response.json()
console.log(data)
```

We will receive the data in JS object format.

Now we will **extract dynamic values from** the object. 

Look into the format, to obtain temperature, we will go under `current` and then in `temp_c`

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/301/original/upload_894097c9f4d2225e2a1f65d7e0100f5b.png?1695149343)

Let us write the required values. 

```java
let currentTemp = data.current.temp_c
let currentCondition = data.current.condition.text
let locationName = data.location.name
let localTime = data.location.localtime
let conditionEmoji = data.current.condition.icon
```
We will print these values on the console to see if they have been fetched properly or not. Output is

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/302/original/upload_a8add666735fe1907f2e69614eac16b5.png?1695149375)


To print and display the data on the website, we will use DOM. The data has to be changed dynamically and for that, DOM has to be used. We will use the classes earlier written in HTML to target and dynamically set values. The code for DOM part-

```javascript
const temperatureField = document.querySelector(".temp");
const cityField = document.querySelector(".time_location p");
const dateField = document.querySelector(".time_location span");
const emojiField = document.querySelector(".weather_condition img");
const weatherField = document.querySelector(".weather_condition span");
const searchField = document.querySelector(".searchField");
const form = document.querySelector("form");
```
> Just explain in short about the variable and which class it is targeting. Eg- `temperatureField` variable is targeting the `temp` class. 

Now, we want to make our search bar work. We will add an event listener to it. Whenever there is an event performed, the event listener will execute the callback function passed as a parameter. 

The search function changes the value of the target(the target city) to the value that we have entered. After typing the city and pressing the submit button, the form will get submitted and the "submit" event will get invoked. 

The `fetchData` function will be passed the value of the target that we have entered. 

```javascript
form.addEventListener('submit' , search )

//search- callback function

function search(){
    target = searchField.value

    fetchData(target)
}

```

The code till now is

```javascript
const temperatureField = document.querySelector(".temp");
const cityField = document.querySelector(".time_location p");
const dateField = document.querySelector(".time_location span");
const emojiField = document.querySelector(".weather_condition img");
const weatherField = document.querySelector(".weather_condition span");
const searchField = document.querySelector(".searchField");
const form = document.querySelector("form");

let target = "Pune"
async function fetchData(target){
    try {
        let url = `https://api.weatherapi.com/v1/current.json?key=8b6d5f63a04a485fa5351525232908&q=${target}&aqi=no`

        const response = await fetch(url)

        const data = await response.json()

        form.addEventListener('submit' , search )

        function search(){
            target = searchField.value
        
            fetchData(target)
        }
        console.log(data)

        let currentTemp = data.current.temp_c
        let currentCondition = data.current.condition.text
        let locationName = data.location.name
        let localTime = data.location.localtime
        let conditionEmoji = data.current.condition.icon
        console.log(currentTemp ,currentCondition ,locationName , localTime , conditionEmoji )
    }
    catch(error){
        console.log(error)
    }
}
fetchData(target)
```

After we run the code, we see that even after entering the name of the city in the search bar, the results are not getting updated. It is because, the form is submitting the value somewhere and page is getting refreshed. This is the nature of the form that after it is submitted, the page is refreshed. 

For that, we use the **preventDefault()** method. Our code for the `search()` function becomes-

```javascript
function search(e){

    e.preventDefault()
    target = searchField.value

    fetchData(target)
}
```

Now, when we search for a city, the output is obtained on the console.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/303/original/upload_07b20aa1d296c7ce114e051640ac2a33.png?1695149418)


Now, we will update the data on our page. A function `updateDOM()` will be created which will contain the values to be updates as parameters.


>First demonstrate this example. We will use the **innerText()** method to set the value inside the HTML.

```javascript
function updateDOM(temp , locationName , time , emoji , condition){

    temperatureField.innerText = temp

    cityField.innerText = locationName

    
    emojiField.src = emoji

    weatherField.innerText = condition
}
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/304/original/upload_3086c0907f207f7aecf7c97855c347e4.png?1695149448)


**ADD DAY**

We can also add day along with the date. Here, **date objects** will be used. 

> console.log(time) then ask the students whether the date or the time is useful to get the day. The answer is date.

Since the date and time is separated by a space, we will use the **split()** method to separate them. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/305/original/upload_1ca3475c0f4e577805e4d08339373c48.png?1695149470)

The split() method splits the value at the delimiter provided and returns an array. Here. after splitting the above value, we get the date at 0th position and time at 1st position. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/306/original/upload_6dcd1d672b2d81019b045800199a9104.png?1695149492)

```javascript
const exactTime = time.split(" ")[1]
const exactdate = time.split(' ')[0]
```

To convert date to day, we follow-
```java
const exactDate = new Date(exactdate).getDay()
```

The output is a number which indicate the day in form of a number. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/307/original/upload_7cbfda536fac2d05ec6f13b7ac54321f.png?1695149519)

We will write another function that converts the day number to day. 

```javascript
function getDayFullName(num) {
    switch (num) {
      case 0:
        return "Sunday";

      case 1:
        return "Monday";

      case 2:
        return "Tuesday";

      case 3:
        return "Wednesday";

      case 4:
        return "Thursday";

      case 5:
        return "Friday";

      case 6:
        return "Saturday";

      default:
        return "Don't Know";
    }
  }
```

Our final code is 

```javascript
const temperatureField = document.querySelector(".temp");
const cityField = document.querySelector(".time_location p");
const dateField = document.querySelector(".time_location span");
const emojiField = document.querySelector(".weather_condition img");
const weatherField = document.querySelector(".weather_condition span");
const searchField = document.querySelector(".searchField");
const form = document.querySelector("form");


let target = 'Pune'


form.addEventListener('submit' , search )


function search(e){

    e.preventDefault()
    target = searchField.value

    fetchData(target)
}



async function fetchData(target){
    try {
        let url = `https://api.weatherapi.com/v1/current.json?key=35af7ff606db422880d141328231305&q=${target}&aqi=no`

        const response = await fetch(url)

        const data = await response.json()

        console.log(data)


        let currentTemp = data.current.temp_c
        let currentCondition = data.current.condition.text
        let locationName = data.location.name
        let localTime = data.location.localtime
        let conditionEmoji = data.current.condition.icon

        console.log(currentTemp ,currentCondition ,locationName , localTime , conditionEmoji )


       updateDOM(currentTemp , locationName ,localTime ,conditionEmoji , currentCondition)

    } catch (error) {
        console.log(error)
    }
}



function updateDOM(temp , locationName , time , emoji , condition){


    console.log(time)

    const exactTime = time.split(" ")[1]
    const exactdate = time.split(' ')[0]




    const exactDay = getDayFullName(new Date(exactdate).getDay())
    console.log(exactDay)



    temperatureField.innerText = temp

    cityField.innerText = locationName

    dateField.innerText = `${exactTime}   ${exactDay}   ${exactdate}`


    emojiField.src = emoji

    weatherField.innerText = condition


}



function getDayFullName(num) {
    switch (num) {
      case 0:
        return "Sunday";

      case 1:
        return "Monday";

      case 2:
        return "Tuesday";

      case 3:
        return "Wednesday";

      case 4:
        return "Thursday";

      case 5:
        return "Friday";

      case 6:
        return "Saturday";

      default:
        return "Don't Know";
    }
  }


fetchData(target)
```