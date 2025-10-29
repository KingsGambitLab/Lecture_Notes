

## Agenda

We will try to cover most of these topics in today's sessions and the remaining in the next.
* Build the shows components
* Build the seating arrangements
* Book tickets
* Make Payments
* Deploy
It is going to be a bit challenging, advanced, but very interesting session covering topics that are asked very frequently in interviews.

So let's start.

## Build the Home Page

As till now we have completed the home page, where all the movies and upcoming movies are shown as below:
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/446/original/upload_2f04c7d551fcc86af920399ec3c6ad5b.png?1695995692)
As we click on the movies then the related information about the movies theaters and the shows timings should be visible in the below blank region.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/447/original/upload_5e3b842eca1765968a94ee60bebe0355.png?1695995733)


## Shows
Now we will be implementing those related functionalities as follows:
If we get this below data in the theaterforMovie then we can show the related shows and the timings and all.


```javascript
import { message } from "antd";
import { useEffect, useState } from "react";
import {useNavigate, useParams} from "react-router-dom"
import { GetMovieById } from "../apicalls/movies";
import { useDispatch } from "react-redux";
import { HideLoading, ShowLoading } from "../redux/loadersSlice";
import {GetTheatresByMovie} from "../apicalls/theatres"
import moment from "moment";

export default function TheatreForMovie(){
    let [movie,setMovie] = useState()
    let [theatres,setTheatres] = useState();
    let [date,setDate] = useState(moment().format("YYYY-MM-DD"));
    const [isHovering, setIsHovering] = useState(false);
    const params = useParams();
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const getData = async() => {
        try{
            dispatch(ShowLoading());
            const response = await GetMovieById(params.id)
            if(response.success){
                setMovie(response.data);
                message.success(response.message)
            }else{
                message.error(response.message);
            }
            dispatch(HideLoading());
        }catch(err){
            dispatch(HideLoading());
            message.error(err.message)
        }
    }

    const getTheatres = async () => {
        try{
            dispatch(ShowLoading());
            const response = await GetTheatresByMovie({date,movie:params.id})
            console.log(response.data);
            if(response.success){
                setTheatres(response.data);
                message.success(response.message)
            }else{
                message.error(response.message);

            }
            dispatch(HideLoading());
        }catch(err){
            dispatch(HideLoading());
            message.error(err.message);
        }
    }

    const handleMouseEnter = (id) => {
        setIsHovering(true);
      };
    
      const handleMouseLeave = (id) => {
        setIsHovering(false);
      };

    useEffect(() => {
        getData();
    },[])

    useEffect(() => {
        getTheatres()
    },[date])

    return (
        movie && (
          <div>
            {/* movie information */}
            <div className = "flex justify-between items-center mb-2">
              <div>
                <h1 className = "text-2xl uppercase">
                  {movie.title} ({movie.language})
                </h1>
                <h1 className = "text-md">Duration : {movie.duration} mins</h1>
                <h1 className = "text-md">
                  Release Date : {moment(movie.releaseDate).format("MMM Do yyyy")}
                </h1>
                <h1 className = "text-md">Genre : {movie.genre}</h1>
              </div>
    
              <div className = "mr-3">
                <h1 className = "text-md ">Select Date</h1>
                <input
                  type = "date"
                  min = {moment().format("YYYY-MM-DD")}
                  value = {date}
                  onChange = {(e) => {
                    setDate(e.target.value);
                    navigate(`/movie/${params.id}?date=${e.target.value}`);
                  }}
    
                />
              </div>
            </div>
            <hr />
            {/* movie theatres */}
            <div className = "mt - 1">
              <h1 className = "text - xl uppercase">Theatres</h1>
            </div>
            <div className = "mt - 1 flex flex-col gap-1">
              {theatres.map((theatre) => (
                <div className = "card p-2">
                  <h1 className = "text-md uppercase">{theatre.name}</h1>
                  <h1 className = "text-sm">Address : {theatre.address}</h1>
                  <div className = "divider"></div>
                  <div className = "flex gap-2">
                    {theatre.shows
                      .sort(
                        (a, b) => moment(a.time, "HH:mm") - moment(b.time, "HH:mm")
                      )
                      .map((show) => (
                        <div key = {show._id} style = {{
                          backgroundColor: isHovering ? '#DF1827' : 'white',
                          color: isHovering ? 'white' : '#DF1827',
                        }}
                        onMouseEnter = {handleMouseEnter}
                        onMouseLeave = {handleMouseLeave}
                          className = "card p-1 cursor-pointer border-primary"
                          onClick = {() => {
                            navigate(`/book-show/${show._id}`);
                          }}
                        >
                          <h1 className = "text-sm">
                            {moment(show.time, "HH:mm").format("hh:mm A")}
                          </h1>
                        </div>
                      ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )
      );
    }
```

The code is a React component named `TheatreForMovie` that is responsible for displaying information about a movie and its associated theaters. It utilizes various React hooks and asynchronous API calls. Here's a breakdown of its functionality:

1. **State Management**:
   - The component uses `useState` to manage state variables for `movie`, `theatres`, and `date`.
   - It also manages the `isHovering` state to handle mouse hover events.

2. **Initialization**:
   - The component extracts route parameters using `useParams()` and obtains a navigation function using `useNavigate()`.
   - It also obtains a Redux dispatch function using `useDispatch()`.

3. **Data Retrieval**:
   - Two asynchronous functions, `getData()` and `getTheatres()`, are defined to fetch movie details and theater information, respectively.
   - These functions use API calls (e.g., `GetMovieById` and `GetTheatresByMovie`) to retrieve data.
   - Loading states are managed using Redux actions (`ShowLoading` and `HideLoading`).

4. **Mouse Hover Effects**:
   - `handleMouseEnter` and `handleMouseLeave` functions are used to toggle the `isHovering` state when hovering over theater showtimes.
   - This is used to change the background and text color of showtime cards.

5. **Effect Hooks**:
   - The `useEffect` hook is utilized to fetch movie data (`getData()`) when the component mounts. It runs once because it has an empty dependency array.
   - Another `useEffect` hook is used to fetch theater data (`getTheatres()`) whenever the `date` state changes.

6. **Rendering**:
   - The component conditionally renders the movie and theater information if the `movie` state exists.
   - Movie information, including title, language, duration, release date, and genre, is displayed.
   - A date input allows users to select a date, triggering a navigation change.
   - Theater information is displayed, including theater name, address, and showtimes.
   - Showtimes are sorted by time and displayed in cards that respond to hover events.

7. **Sorting of Theater Shows**:
   - Within the rendering section of the component, theater shows are sorted based on their showtimes.
   - This sorting is achieved through the `.sort()` method applied to the `theatre.shows` array.
   - The sorting logic compares the showtimes, ensuring that shows are displayed in chronological order.
   - The `moment` library is used to parse and format showtime values for comparison.
   - As a result, theater shows are presented to users in ascending order of showtime, providing a clear and organized view of available showtimes for the selected date.

## Seating Component

Now lets start with the seating component, after selecting the show of the theater as follows.  

```javascript
onClick = {() => {
    navigate(`/book-show/${show._id}`);
}}
```

When a user clicks an element (like a button), the `onClick` function runs. It uses the `navigate` function to take the user to a new page, typically based on the show's ID.


### Get show by id
```javascript
//get show by id
router.post('/get-show-by-id',authMiddleware,async(req,res) => {
    try{
        const show = await Show.findById(req.body.showId)
        .populate("movie")
        .populate("theatre")
        res.send({
            success:true,
            message:"Show fetched",
            data:show,
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})
```
This specific route handles a POST request to retrieve information about a show by its ID. Let's break down what this code does:

1. **Route Definition**:
   - This route is defined to listen for POST requests on a specific path, which is "/get-show-by-id".

2. **Middleware**:
   - It includes an authentication middleware function called `authMiddleware`. This function is likely responsible for verifying the user's identity and ensuring that only authorized users can access this route.

3. **Request Handling**:
   - When a POST request is made to this route, the server executes the code inside the `try` block.

4. **Show Retrieval**:
   - Inside the `try` block, the code uses the `Show` model (presumably a MongoDB model) to find a show document in the database based on the provided `showId`. This is done using `Show.findById(req.body.showId)`.
   - The `populate` method is used to retrieve additional information related to the show, specifically details about the associated movie and theater. This populates the "movie" and "theatre" fields in the `show` document with their respective data.

5. **Response**:
   - If the show is successfully found and populated, a response is sent back to the client with a `success` status set to `true`.
   - The response includes a message indicating that the show has been fetched and the `show` data itself.

6. **Error Handling**:
   - If any errors occur during the process (e.g., the show with the provided ID doesn't exist or there's an issue with the database), the code inside the `catch` block is executed.
   - In case of an error, a response is sent back to the client with a `success` status set to `false`, and an error message is provided.

In summary, this route is designed to handle POST requests to fetch details about a show by its ID. It uses authentication middleware to secure the route, retrieves the show data from a database, populates related movie and theater information, and sends a response with the retrieved data or an error message, depending on the outcome of the database operation.


```javascript
export const GetShowById = async (payload) => {
    try{
        const response = await axiosInstance.post('/api/theatres/get-show-by-id',payload)
        return response.data
    }catch(err){
        return err.message
    }
}
```

The `GetShowById` function serves as a client-side utility for making HTTP POST requests to a server's `/api/theatres/get-show-by-id` endpoint. It is designed to retrieve specific show information based on a provided `payload`, which typically includes data necessary for the request, such as a `showId`.

The function operates asynchronously, utilizing Axios to handle the HTTP request. Within a `try...catch` block, it awaits the completion of the request, ensuring that the program doesn't proceed until a response is received.

On success, the function extracts and returns the response data from the server using `return response.data`. This allows the caller to access and utilize the fetched show data.

However, in the event of an error—whether due to network issues, server problems, or other reasons—the `catch` block captures and handles the error. 


### How Many Seats Are There for That Show

Different shows have different number of the shows as below:


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/448/original/upload_04c10a7c926af4fbb8d515abf9873734.png?1695995938)

```javascript
import { message } from "antd";
import { useEffect, useState } from "react"
import { useParams, useNavigate } from "react-router-dom";
import { GetShowById } from "../apicalls/theatres";
import {BookShowTickets, MakePayment } from "../apicalls/bookings";
import Button from "../components/Button";
import { HideLoading, ShowLoading } from "../redux/loadersSlice";
import StripeCheckout from "react-stripe-checkout";
import moment from "moment"
import { useDispatch, useSelector } from "react-redux";

export default function BookShow(){
  const { user } = useSelector((state) => state.users);
   const [selectedSeats, setSelectedSeats] = useState([]);
    let [show,setShow] = useState();
    const params = useParams();
    const dispatch = useDispatch();
    const navigate = useNavigate()
    const getData = async() => {
        try{
            const response = await GetShowById({showId:params.id})
            if(response.success){
                setShow(response.data);
            }else{
                message.error(response.message)
            }
        }catch(err){
            message.error(err.message)
        }
    }

    const getSeats = () => {
      const columns = 12;
      const totalSeats = show.totalSeats; // 120
      const rows = Math.ceil(totalSeats / columns); // 10
      
      return (
          <div>
              <p className = "m - 4">Screen This Side</p>
              <hr/>
        <div className = "flex gap-1 flex-col p-2 card">
          <hr/>
          
          {Array.from(Array(rows).keys()).map((seat, index) => {
            return (
              <div className = "flex gap-1 justify-center">
                    {/* 0,  1 ,2, ,3, ..        11 
               0 [ [ 0, 1, 2, 3, 4, 5,6,7.. ,11],
               1   [0,  1, 2, 3, ..        ,11],
               2  .
                  .
               9   [0,1,2           , .... 11]
                ] */}
                {Array.from(Array(columns).keys()).map((column, index) => {
                  const seatNumber = seat * columns + column + 1;
                  // 12*1 + 3+ 1 = 16
                  let seatClass = "seat";
                  // seat = 0 // coloumns = 12
                  //0 + 1 + 1 = 2
                  if (selectedSeats.includes(seat * columns + column + 1)) {
                    seatClass = seatClass + " selected-seat";
                  }
                  if (show.bookedSeats.includes(seat * columns + column + 1)) {
                    seatClass = seatClass + " booked-seat";
                  }
                  return (
                    seat * columns + column + 1 <= totalSeats && (
                      <div
                        className = {seatClass}
                        onClick = {() => {
                          if (selectedSeats.includes(seatNumber)) {
                            setSelectedSeats(
                              selectedSeats.filter((item) => item !== seatNumber)
                            );
                          } else {
                            setSelectedSeats([...selectedSeats, seatNumber]);
                          }
                        }}
                      >
                        <h1 className = "text-sm">{seat * columns + column + 1}</h1>
                      </div>
                    )
                  );
                })}
              </div>
            );
          })}
        </div>
        </div>
      );
    };

    const book = async (transactionId) => {
      try {
        dispatch(ShowLoading());
        const response = await BookShowTickets({
          show: params.id,
          seats: selectedSeats,
          transactionId,
          user: user._id,
        });
        if (response.success) {
          message.success(response.message);
          navigate("/profile");
        } else {
          message.error(response.message);
        }
        dispatch(HideLoading());
      } catch (error) {
        message.error(error.message);
        dispatch(HideLoading());
      }
    };

    const onToken = async (token) => {
      // console.log(token)
      try {
        dispatch(ShowLoading());
        const response = await MakePayment(
          token,
          selectedSeats.length * show.ticketPrice * 100
        );
        if (response.success) {
          message.success(response.message);
          // console.log(response.data);
          book(response.data);
        } else {
          message.error(response.message);
        }
        dispatch(HideLoading());
      } catch (error) {
        message.error(error.message);
        dispatch(HideLoading());
      }
    };

    useEffect(() => {
        getData();
    },[])

    return (
      show && (
        <div>
          {/* show infomation */}
  
          <div className = "flex justify-between card p-2 items-center">
            <div>
              <h1 className = "text-sm">{show.theatre.name}</h1>
              <h1 className = "text-sm">{show.theatre.address}</h1>
            </div>
  
            <div>
              <h1 className = "text-2xl uppercase">
                {show.movie.title} ({show.movie.language})
              </h1>
            </div>
  
            <div>
              <h1 className = "text-sm">
                {moment(show.date).format("MMM Do yyyy")} - {" "}
                {moment(show.time, "HH:mm").format("hh:mm A")}
              </h1>
            </div>
          </div>
  
          {/* seats */}
  
          <div className = "flex justify-center mt-2">{getSeats()}</div>
  
          {selectedSeats.length > 0 && (
            <div className = "mt-2 flex justify-center gap-2 items-center flex-col">
              <div className = "flex justify-center">
                <div className = "flex uppercase card p-2 gap-3">
                  <h1 className = "text-sm"><b>Selected Seats</b> : {selectedSeats.join(" , ")}</h1>
  
                  <h1 className = "text-sm">
                    <b>Total Price</b> : {selectedSeats.length * show.ticketPrice}
                  </h1>
                </div>
              </div>
              <StripeCheckout
                token = {onToken}
                amount = {selectedSeats.length * show.ticketPrice * 100}
                billingAddress
                stripeKey = "pk_test_eTH82XLklCU1LJBkr2cSDiGL001Bew71X8"
              >
                <Button title = "Book Now" />
              </StripeCheckout>
            </div>
          )}
        </div>
      )
    );
  }
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/449/original/upload_8519871882badc6cea20e45f3b757fda.png?1695996092)

Let's dive into the `BookShow` component and focus on the details, particularly the part that handles rendering the seats with the `for` loops:

1. **Component Structure**:<br> The `BookShow` component is a React functional component responsible for booking show tickets. It receives data about a show and allows users to select seats for booking.

2. **Fetching Show Data**:<br> The `getData` function is called when the component mounts (`useEffect`). It fetches details about the show specified by the `params.id` using the `GetShowById` API call and sets the show data in the component's state.

3. **Rendering Seats**:
   - The `getSeats` function is responsible for rendering the seats grid. It calculates the number of rows and columns based on the `totalSeats` of the show.
   - It returns a JSX structure that represents the seats grid. The grid is divided into rows and columns using nested `map` functions.

   ```jsx
   {Array.from(Array(rows).keys()).map((seat, index) => {
     return (
       <div className="flex gap-1 justify-center">
         {Array.from(Array(columns).keys()).map((column, index) => {
           // ... Seat rendering logic
         })}
       </div>
     );
   })}
   ```

   - The outer `map` iterates over the rows, and the inner `map` iterates over the columns. For each seat, it calculates a unique `seatNumber` based on the row and column indices.
   - The seat's appearance (e.g., styling) depends on its characteristics, such as whether it's selected or booked. This is determined by the `seatClass`.
   - Seats that are already booked (`show.bookedSeats`) are given a "booked-seat" class.
   - Seats that are currently selected by the user are given a "selected-seat" class.
   - Seats that are neither booked nor selected are rendered without any additional class.

4. **Selecting and Deselecting Seats**:
   - Seats can be selected or deselected by clicking on them. This interaction is handled by the `onClick` event attached to each seat `<div>`.
   - When a seat is clicked, the `setSelectedSeats` function is used to update the `selectedSeats` state based on whether the clicked seat is already in the selected seats array or not.

5. **Displaying Selected Seats and Total Price**:
   - Below the seat grid, there's a section that displays the selected seats and the total price. This section is conditionally rendered only when there are selected seats (`selectedSeats.length > 0`).
   - It shows the selected seat numbers joined by a comma and calculates the total price based on the number of selected seats and the ticket price for the show.

6. **Booking Seats and Making Payments**:
   - The component includes functions (`book` and `onToken`) for booking seats and handling payment. When the user confirms the booking, these functions are called to initiate the booking process and make a payment.


## Seat Selection/Deselection Functionaities

  ```javascript
 if (selectedSeats.includes(seat * columns + column + 1)) {
                    seatClass = seatClass + " selected-seat";
                  }
                  if (show.bookedSeats.includes(seat * columns + column + 1)) {
                    seatClass = seatClass + " booked-seat";
                  }
                  return (
                    seat * columns + column + 1 <= totalSeats && (
                      <div
                        className = {seatClass}
                        onClick = {() => {
                          if (selectedSeats.includes(seatNumber)) {
                            setSelectedSeats(
                              selectedSeats.filter((item) => item !== seatNumber)
                            );
                          } else {
                            setSelectedSeats([...selectedSeats, seatNumber]);
                          }
                        }}
                      >
                        <h1 className = "text-sm">{seat * columns + column + 1}</h1>
                      </div>
                    )
                  );
```


- **Class Assignment**:
  - The `seatClass` variable is initially set to an empty string for each seat.
  - The first `if` statement checks if the current seat number (calculated as `seat * columns + column + 1`) is included in the `selectedSeats` array. If it is, the `"selected-seat"` class is appended to `seatClass`.
  - The second `if` statement checks if the seat number is included in the `show.bookedSeats` array. If it is, the `"booked-seat"` class is appended to `seatClass`.

- **Rendering Seats**:
  - The code then returns a `div` element representing the seat.
  - The condition `seat * columns + column + 1 <= totalSeats` ensures that only valid seats are rendered based on the total number of seats available.
  - The `className` attribute is set to `seatClass`, which may include `"selected-seat"` and/or `"booked-seat"` classes based on the conditions.
  - An `onClick` event handler is attached to the seat `div`. When a user clicks on a seat, it triggers this function.
  - Inside the `onClick` function:
    - If the clicked seat number is already in the `selectedSeats` array, it's removed from the array using `selectedSeats.filter()`. This means the user is deselecting the seat.
    - If the clicked seat number is not in `selectedSeats`, it's added to the array, indicating the user's selection.

```css!
/* seats */
  
  .seat {
    height: 30px;
    width: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    border : 1px solid #b1b1b1;
    cursor: pointer;
  }
  
  
  .selected-seat {
    background-color: #118838;
  }
  
  .selected-seat h1 {
    color: white !important;
  }
  
  .booked-seat {
    background-color: #b1b1b1;
    cursor: not-allowed;
    pointer-events: none;
  }
  
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/450/original/upload_c4f6952777f7fe93082df2c33a466bea.png?1695996181)

The provided CSS code defines styles for rendering seats in a grid. Each seat (`.seat`) has a height and width, is centered both horizontally and vertically, and has a border to separate seats. The `cursor` property changes to a pointer to indicate interactivity. Selected seats (`.selected-seat`) have a green background and white text for visibility.
Booked seats (`.booked-seat`) have a gray background and a disabled cursor, preventing further interaction. These styles effectively visualize seat availability and user selections, enhancing the user experience in a seat selection interface.


## Add the Payment Options 

"React Stripe Checkout" refers to a React library or component that allows developers to easily integrate Stripe's payment processing capabilities into their React applications. This library streamlines the process of creating a checkout experience, handling payments, and managing user interactions with the Stripe API.

Key features and steps typically involved in using "React Stripe Checkout" include:

1. **Installation**:<br> Developers can install the library in their React project using npm or yarn.
2. **Configuration**:<br> Setting up Stripe credentials and configuring payment options, such as currency and amount.
3. **Integration**:<br> Adding the "React Stripe Checkout" component to the application's payment page or modal.
4. **User Interaction**:<br> Users can enter their payment details, including card information.
5. **Tokenization**:<br> The library securely tokenizes the payment information, ensuring sensitive data is not exposed to the application server.
6. **Payment Processing**:<br> Stripe processes the payment using the token and completes the transaction.



```javascript
<StripeCheckout
token = {onToken}
amount = {selectedSeats.length * show.ticketPrice * 100}
billingAddress
               stripeKey = "pk_test_eTH82XLklCU1LJBkr2cSDiGL001Bew71X8"
 >
<Button title = "Book Now" />
</StripeCheckout>
```
            
The code snippet provided is an example of how you might use the "react-stripe-checkout" library to integrate Stripe's payment processing into a React application. Here's an explanation of the code:

1. **\<StripeCheckout> Component:** This is the main component from the "react-stripe-checkout" library, and it acts as a wrapper around your payment button. It allows you to configure and handle the payment process.

2. **token={onToken}:** This prop specifies the callback function (`onToken`) that will be called when the payment is successful. The `token` contains the payment information, which you can then use to process the payment on the server.

3. **amount={selectedSeats.length * show.ticketPrice * 100}:** This prop specifies the total amount to charge in the smallest currency unit (cents in this case). It calculates the total based on the number of selected seats and their individual ticket prices.

4. **billingAddress:** This prop indicates that you want to collect the customer's billing address during the payment process.

5. **stripeKey:** This prop is where you provide your Stripe API key (in test mode, as indicated by the "pk_test_" prefix). It connects your React app to your Stripe account.

6. **<Button title="Book Now" />:** This is the button or UI element that triggers the payment process when clicked. It's wrapped inside the `<StripeCheckout>` component, making it the "Pay Now" or "Book Now" button.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/451/original/upload_82e3bafc31613a0c60453969ca8cb490.png?1695996351)

When a user clicks the "Book Now" button, the `<StripeCheckout>` component will handle the payment process. If the payment is successful, it will call the `onToken` callback
function, allowing you to perform further actions, such as storing the payment details on your server or updating the UI to reflect the successful payment.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/452/original/upload_ae57e6a2ed7a0a47022fb038eb3b6a53.png?1695996513)

Make sure to replace the `stripeKey` value with your actual Stripe API key, and ensure that your Stripe account is set up correctly to handle payments in test mode.


In bookShow.js file make the below changes as follows:
```javascript
const onToken = async (token) => {
  // console.log(token)
  try {
    dispatch(ShowLoading());
    const response = await MakePayment(
      token,
      selectedSeats.length * show.ticketPrice * 100
    );
    if (response.success) {
      message.success(response.message);
      // console.log(response.data);
      book(response.data);
    } else {
      message.error(response.message);
    }
    dispatch(HideLoading());
  } catch (error) {
    message.error(error.message);
    dispatch(HideLoading());
  }
};
```
* The onToken function is defined, which handles payment processing using Stripe.
* It dispatches actions for showing and hiding a loading indicator.
* It makes a payment request to the server using the MakePayment function and the payment token.
* Depending on the response, it displays success or error messages and potentially triggers further actions like booking.


In bookRoute.js file make the below changes as follows:
```javascript
const authMiddleware = require("../middlewares/authMiddleware");

const router = require("express").Router();
const stripe = require("stripe")(process.env.stripe_key);
const Booking = require('../models/bookingModel')
const Show = require('../models/showModel')

router.post('/make-payment',authMiddleware,async(req,res) => {
    try{
        const {token,amount} = req.body;
        console.log(token);
        const customer = await stripe.customers.create({
            email:token.email,
            source:token.id
        })
        const charge = await stripe.charges.create({
            amount:amount,
            currency:"usd",
            customer:customer.id,
            receipt_email:token.email,
            description:"Ticket has been booked for a movie"
        })

        const transactionId = charge.id;
        res.send({
            success:true,
            message:"Payment done, Ticket booked",
            data:transactionId
        })

    }catch(err){    
        res.send({
            success:false,
            message:err.message
        })
    }
})
```
* The Express route "/make-payment" is defined, which expects a POST request with payment-related data, including the token and amount.
* It uses the Stripe API to create a customer and charge their card.
* If the payment is successful, it returns a success message along with a transaction ID.
* If there's an error, it returns an error message.

In booking.js file make the below changes as follows:

```javascript
import { axiosInstance } from "."


export const MakePayment = async(token,amount) => {
    try{
        const response = await axiosInstance.post('/api/bookings/make-payment',{token,amount});
        return response.data
    }catch(err){
        return err.response
    }
}
```

The MakePayment function is defined, which makes an API call to your server's "/make-payment" endpoint with the payment token and amount.
It returns the response data if successful or the error response if there's an issue.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/475/original/upload_9ed9f36f03a3bea064f0f0844874a731.png?1696008818)

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/476/original/upload_a136b39f32498d0585a1b504ab4c675b.png?1696008840)


## Bookings in the Profile

```javascript
const mongoose = require("mongoose");

const bookingSchema = new mongoose.Schema(
  {
    show: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "shows",
    },
    user: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "users",
    },
    seats: {
      type: Array,
      required: true,
    },
    transactionId: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model("bookings", bookingSchema);
```
* A Mongoose schema called bookingSchema is defined, representing the structure of booking documents.
* It includes fields such as show (a reference to the show), user (a reference to the user making the booking), seats (an array of selected seats), and transactionId (a unique identifier for the transaction).
* The schema is exported as a Mongoose model named "bookings."


In bookingRoute.js file make the below changes as follows:
```javascript
//book shows
router.post("/book-show", authMiddleware, async (req, res) => {
    try {
      // save booking
      const newBooking = new Booking(req.body);
      await newBooking.save();

      const show = await Show.findById(req.body.show);
      // update seats
      await Show.findByIdAndUpdate(req.body.show, {
        bookedSeats: [...show.bookedSeats, ...req.body.seats],
      });

      res.send({
        success: true,
        message: "Show booked successfully",
        data: newBooking,
      });
    } catch (error) {
      res.send({
        success: false,
        message: error.message,
      });
    }
  });


  router.get("/get-bookings", authMiddleware, async (req, res) => {
    try {
      const bookings = await Booking.find({ user: req.body.userId })
        .populate("user")
        .populate("show")
            .populate({
                path: "show",
                populate: {
                path: "movie",
                model: "movies",
                },
            })
            .populate({
                path: "show",
                populate: {
                path: "theatre",
                model: "theatres",
                },
            });

      res.send({
        success: true,
        message: "Bookings fetched successfully",
        data: bookings,
      });
    } catch (error) {
      res.send({
        success: false,
        message: error.message,
      });
    }
  });
```
* A new route handler "`/book-show`" is defined, which expects a POST request to book a show.
* It creates a new booking record using the provided data and saves it to the database.
* It also fetches the existing show data to update the list of booked seats.
* The response includes a success message and the newly created booking data or an error message in case of failure.
* Another route handler "`/get-bookings`" is defined, which expects a GET request to fetch all bookings of a user.
* It retrieves user-specific booking records, populates relevant data (user, show, movie, and theatre), and sends them in the response.
* The response includes a success message and the booking data or an error message in case of failure.


In bookings.js file make the below changes as follows:

```javascript
// book shows
export const BookShowTickets = async (payload) => {
    try {
      const response = await axiosInstance.post(
        "/api/bookings/book-show",
        payload
      );
      return response.data;
    } catch (error) {
      return error.response.data;
    }
  };

  export const GetBookingsOfUser = async () => {
    try {
      const response = await axiosInstance.get("/api/bookings/get-bookings");
      return response.data;
    } catch (error) {
      return error.response.data;
    }
  };
```
* Two functions are defined to make API calls related to bookings.
* BookShowTickets sends a POST request to the "`/book-show`" endpoint to book show tickets, including the show ID, selected seats, transaction ID, and user ID.
* `GetBookingsOfUser` sends a GET request to the "`/get-bookings`" endpoint to fetch the bookings of the currently authenticated user.

In bookingShow.js file make the below changes as follows:
```javascript
const book = async (transactionId) => {
      try {
        dispatch(ShowLoading());
        const response = await BookShowTickets({
          show: params.id,
          seats: selectedSeats,
          transactionId,
          user: user._id,
        });
        if (response.success) {
          message.success(response.message);
          navigate("/profile");
        } else {
          message.error(response.message);
        }
        dispatch(HideLoading());
      } catch (error) {
        message.error(error.message);
        dispatch(HideLoading());
      }
    };
```

* The book function is defined, which is responsible for handling the booking of show tickets.
* It makes an API call using BookShowTickets, passing relevant data such as the **show ID, selected seats, transaction ID, and user ID**.
* Depending on the response, it displays success or error messages and potentially navigates to the user's profile page.
* Loading indicators are shown while the booking process is in progress.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/477/original/upload_56c81be1c50ede02d12ccb1deb18708e.png?1696009093)
