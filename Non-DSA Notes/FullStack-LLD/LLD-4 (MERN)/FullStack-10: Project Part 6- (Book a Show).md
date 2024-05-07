
## Agenda

We will try to cover most of these topics in today's sessions and the remaining in the next.
* Build the Home Page
* Map movies to theaters
* Build the shows components
* Build the seating arrangements
* Book tickets
* Make Payments
* Deploy
It is going to be a bit challenging, advanced, but very interesting session covering topics that are asked very frequently in interviews.

So let's start.


## Build the Home Page

Whenwever you login to the home page you must see what all movies are playing and then you want to book that particular movie.

But before moving that as we left a part in shows component , basically the working of the delete button.

**Asking the question:**
Have you attempted the homework of making the delete button?
**No**

Lets quickly write the code for the delete button, lets add the route of the "delete-show".
Basically on hitting the endpoint "/delete-show", will await the shows model and find by id to delete by getting the showID and then respectively shows the sucess message or the respective error.

For this route, will go to the client and make the axios instance for this to delete-movies. So now will be writing the axios instance where we will bw hitting on the route "/api/theatres/delete-show" and sending the id in the payload.

Now will be writing the handledelete method that will be accepting the id and will be calling the deleteshow and id will taken as payload and the `getdata()` gets called or else the error message. and just put this handledelete in the onClick.


Now just demonstarate, by inserting the show name, date, time, movie, ticket_price, and total_seats. Now will be trying the delete button.


Lets start with home page, 
### Start by Discussing the Wireframe of The Homepage

* In the home page, will be search part for searching the movies name.
* Then will be adding the posters of the different movies which will be clickable that goes to the some another page.
* On the other page , that will have the details of the movies and below that there will details of the theaters and in the nother space there will be date picker. The available theaters with the selected movie and date/time will be shown with name and time.
* When we will click on the theaters components, that will consist of the seating arrangements and then the users will be able to select the particular seat.
* Then after clicking on the Book Ticket button which will go to the another page that will show the movies details with seat, amount, and the make payment button.
* On clicking the make_payment button that will take us to the stripe portal to make the payments.

### Let's start changing the index.js file as follows:
First of all add the input space for searching the movie name and give classname as search-input.

* Add the height and border-radius to the search-input to give some styling.
* Now as you see in the mongodb in the movies we are having the information of the movies stored.
* To get the details of the movies to add them in the cards that will be done using the get_all_movies route.
* To start building the card, lets divide it int row and col using antd.
* In the row, there will be movies title, seach space and the column properties.
*  Now will bw creating the two states one for the movies and other for the searchText using useState.
*  Define the method of getdata for the getting all the movies by using loader and dispatch by useDispatch.
* To call the getData() method , use the useEffect and will get all the movies. Also import the HideLoading and ShowLoading from the loaderSlice. Also the message from the antd.
* For the searchText , will be adding the onChange on the event that will use the setSearchText method with the event's target value. And basically the search for the particular text by after converting to the lower case is done with the movies title.


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/390/original/upload_b9165fabb38882138bfde830cd6e8612.png?1695983804)

### Mapping of the Theater and Shows

As there are multiple theaters, with multiple shows and multile movies, then how to map the correct movies details, lets discuss this:

For example in the shows at PVR Superplex having the show of the movie Captain America.
Let's suppose they are having shows of the movies at 3 PM and 9PM so are they will be displayed two times. 

Do they show they show the PVR Superplex haing two shows one at the 3pm and the other at 9pm. Or do they show like PVR Superplex two times with differently. The first one is the better approach like in the below image.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/391/original/upload_1e89157fcafdf4aea3f4657bb8190f61.png?1695983835)

Like one theater one time, and then we can add on the shows of different time as above.

We have to use the route parameter for the different routes for the different movies by sending the movies id.

Lets import the useNavigate from the react-router-dom, use this in the navigate method where we are changing the movie_id. Also import moment.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/393/original/upload_75f0d47c5e4a2f8b8f02d693f814204a.png?1695983857)

Hence the route changes as we click on the movie as seen in the route we got the movie id along with the date. Same as we observer on the different websites like amazon.

So now we have to show the movies details along with the show details let start, 
* We have to take a another component, names as TheatreForMovies.
* In the app.js whenever there will be route of type movie with id, then we will go to this component of theatresForMovies.
* First of all we have to just build the movies_Details and then the date picker.
* Using the movie id we can get all the data using the function `getData()`. 

---
title: Map Movies to the theaters
description: Explanation of all the related components and the routes for the mapping page of the  movies with theaters.
duration: 2100
card_type: cue_card
---

## Map Movies to the theaters

**Get a movie by ID route**
Lets create the route for this, go to the movie-route.js by just passing the id, so by simply attaching the movie_id with the axiosInstance we can get the id using the route and api call.

Here's a explanation of the code: 

1. **Imports**:
   - The code imports necessary modules and functions from various libraries such as Ant Design (`antd`), React (`react`), React Router (`react-router-dom`), and others.

2. **React Hooks**:
   - The `useParams` and `useNavigate` hooks are used from React Router to access the URL parameters and navigate between routes, respectively.
   - The `useState` and `useEffect` hooks are used to manage component state and perform side effects when the component mounts.

3. **Redux Dispatch**:
   - The `useDispatch` hook is used to get the Redux dispatch function, which will be used later to dispatch actions.

4. **Data Fetching with getData Function**:
   - The `getData` function is defined as an asynchronous function. It is responsible for fetching movie data by its ID from an API using the `GetMovieById` function from the `apicalls/movies` module.
   - While fetching data, a loading spinner is displayed using `dispatch(ShowLoading())`.
   - After receiving a response, it checks if the response was successful. If successful, it sets the movie data and displays a success message; otherwise, it displays an error message.
   - Finally, it hides the loading spinner using `dispatch(HideLoading())`.

5. **Render Movie Information**:
   - The movie information is displayed in JSX within a conditional rendering block (`movie && ...`) to ensure that the component renders only when `movie` data is available.
   - It displays various details about the movie, such as title, language, duration, release date, and genre. The `moment` library is used to format the release date.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/394/original/upload_5ccf189b12d1fb2422a35e17af842a02.png?1695983908)


**Addition of the date picker using moment:**

* The component will render a section that includes a label "Select Date" and a date picker input field.
* The date picker will have a minimum date restriction set to the current date. Users won't be able to select a date earlier than today's date.
* When a user interacts with the date picker and selects a new date, an onChange event will be triggered.
* Additionally, the code uses the navigate function (likely from React Router) to navigate to a new URL. This new URL includes query parameters with the movie ID (params.id) and the selected date. For example, if the user selects a date of "2023-09-20" for a movie with an ID of "123," the URL might become something like "`/movie/123?date=2023-09-20`."
* The change in the URL, including the selected date as a query parameter, can trigger a different route in your application or update the content displayed on the page.
* This enables your application to react to the selected date and possibly show movie-related information for the chosen date.

**Now start creating threaters and shows running on them:**

Lets start by getting the theater, using the id of the theater for example if the bruce having two 2 theaters with JAWAN movies and the Maek has 1 theater with Captain America then if the user selecting the JAWAN movies how many theater should be given?

**Asking Question** So exactly the 2 theaters should be given which are havin the movie JAWAN.

Lets get all the unique theaters which have the shows of a movie

It's an Express.js route handler that aims to retrieve all unique theaters that have shows of a specific movie on a given date. Here's the explanation:

1. **Route Definition**:
   - This code defines an Express.js POST route at the endpoint `/get-all-theatres-by-movie`. It expects the request to be authenticated using the `authMiddleware` middleware.

2. **Request Parsing**:
   - In the route handler, it extracts the `movie` and `date` parameters from the request body using destructuring: `const { movie, date } = req.body;`.

3. **Fetching Shows**:
   - It then queries the database to find all the shows of a specific movie on the given date using the `Show` model. The `find` method is used with the `movie` and `date` parameters.
   - Additionally, it uses `.populate('theatre')` to populate the `theatre` field in the `shows` collection with corresponding theater information.

4. **Finding Unique Theaters**:
   - The code initializes an empty array called `uniqueTheatre` to store unique theater data.

5. **Sending Response**:
   - The route handler sends a JSON response to the client, indicating that the request was successful (`success: true`).
   - The `message` field provides a success message, stating "Unique Data Fetched."
   - The `data` field in the response is set to the `uniqueTheatre` array, which contains the unique theater information.

6. **Error Handling**:
   - In case an error occurs during the process (e.g., a database query error), the catch block is executed. It sends a JSON response indicating the failure (`success: false`) and includes an error message in the `message` field.


The provided code is a JavaScript function that exports a function named `GetTheatresByMovie`. This function is likely used to make an HTTP POST request to a specific API endpoint in order to get theaters that are showing a particular movie on a given date. Here's an explanation of the code:

1. **export const GetTheatresByMovie = async (payload) => { ... }**:
   - This line exports a function called `GetTheatresByMovie` as a named export from the module.
   - The function is defined as an asynchronous function, indicating that it can perform asynchronous operations, such as making HTTP requests.

2. **try { ... } catch (err) { ... }:**
   - The function is wrapped in a try-catch block, which is used for error handling. It attempts to perform the specified operation within the try block and catches any errors that may occur.

3. **const response = await axiosInstance.post('/api/theatres/get-all-theatres-by-movie', payload);:**
   - Inside the try block, the code uses the `axiosInstance` (presumably an Axios instance configured for making HTTP requests) to send an HTTP POST request to the `/api/theatres/get-all-theatres-by-movie` endpoint.
   - The `payload` variable is expected to contain the data to be sent as the request body. This likely includes information about the movie and the date.

4. **return response.data;:**
   - If the HTTP request is successful (i.e., the server responds with a valid JSON response), the function returns the `data` property of the response. This typically contains the data returned by the server, such as theater information.

5. **return err.response:**
   - If an error occurs during the HTTP request (e.g., a network error or a server error), the catch block returns the `response` property of the `err` object. 



The provided code appears to be a JavaScript function named `getTheatres`. This function is designed to fetch theater information related to a specific movie and date, similar to the previous code you shared. Here's an explanation of this code:

1. **const getTheatres = async () => { ... }:**
   - This function is defined as an asynchronous function and does not take any arguments.

2. **try { ... } catch (err) { ... }:**
   - The function is wrapped in a try-catch block for error handling. It attempts to perform the specified operations within the try block and catches any errors that may occur.

3. **dispatch(ShowLoading());:**
   - Before making the API request, it dispatches an action (likely a Redux action) to show a loading spinner or loading indicator, indicating that data is being fetched.

4. **const response = await GetTheatresByMovie({ date, movie: params.id });:**
   - Inside the try block, it calls the `GetTheatresByMovie` function, passing an object as the payload. This object includes the `date` and `movie` parameters required for the API request. `params.id` is presumably the movie ID.
   - The function is awaited, meaning it will wait for the HTTP request to complete and return a response.

5. **console.log(response.data);:**
   - It logs the `data` property of the response to the console. This typically contains the data returned by the server, which in this case, should be theater information related to the specified movie and date.

6. **Response Handling:**
   - If the response indicates success (`response.success` is `true`), it updates the component state with the theater data using `setTheatres(response.data)` and displays a success message using `message.success(response.message)`.
   - If the response indicates failure (`response.success` is `false`), it displays an error message using `message.error(response.message)`.

7. **dispatch(HideLoading());:**
   - Finally, it dispatches an action (likely a Redux action) to hide the loading spinner or loading indicator, indicating that the data fetching process has completed.

8. **Error Handling:**
   - In case an error occurs during the API request (e.g., network error or server error), the catch block is executed. It hides the loading indicator, and it displays an error message using `message.error(err.message)`.


**Code for the Unique Theaters:**

Route handler for fetching all unique theaters that have shows of a specific movie on a given date. Here's an explanation:

1. **Route Definition**:
   - This code defines an Express.js POST route at the endpoint `/get-all-theatres-by-movie`. It expects the request to be authenticated using the `authMiddleware` middleware.

2. **Request Parsing**:
   - In the route handler, it extracts the `movie` and `date` parameters from the request body using destructuring: `const { movie, date } = req.body;`.

3. **Fetching Shows**:
   - It then queries the database (likely using an ORM like Mongoose) to find all the shows of a specific movie on the given date. The `Show` model is used to query the shows, and the `populate` method is used to retrieve associated theater information for each show: `const shows = await Show.find({ movie, date }).populate('theatre');`.

4. **Finding Unique Theaters**:
   - The code initializes an empty array called `uniqueTheatre` to store unique theater data.

   - It iterates through each `show` in the `shows` array using a `forEach` loop.

   - For each `show`, it checks if there is already a theater with the same `_id` in the `uniqueTheatre` array.

   - If no matching theater is found (`!theatre`), it filters all shows with the same theater `_id` and pushes a new object into the `uniqueTheatre` array. This object combines the theater data with an array of shows for that theater.

5. **Response**:
   - Finally, the route handler sends a response to the client. If successful, it sends a JSON response with `success`, a success message, and the `uniqueTheatre` array containing theater information and associated shows.

6. **Error Handling**:
   - In case of an error during the process (e.g., database query error), it sends a JSON response indicating the failure with an error message.

This route essentially retrieves all theaters that are showing a particular movie on a specific date, eliminating duplicates, and presents the data in a structured format, making it easier for clients to work with unique theater information and associated show details.