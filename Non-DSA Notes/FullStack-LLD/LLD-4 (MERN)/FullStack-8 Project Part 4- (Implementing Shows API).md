
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
Till now we have completed the login page, then the home page if you click on the name then it will take us to the admin page. as shown below. 

You have to take care of the admin rights, wwhich will have all the rights of adding movies and their related properties.

Admin can manage the movies and can manage the theaters. Then we will talk about the shows that in which region which show is running, timeof that show.

Add movies has already been done, where you can provide movie name, description, duration, etc. If you click on the Save button, it is not saved.

Whenever, the save button clicked it calls the submit. So we have to implement the operation of saving the form data into the database when clicked on the save button.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/351/original/upload_d571955d6145ed8751d953e02d03a702.png?1695975201)

As route is already working, what shoukd be the second step.
**Asking Question?**
We should create an axios instance for the movies as well as we created for the users in the Apicalls so that we can do the add movies, delete movies etc.

In the movies.js do the following as explained below:

```javascript
import { axiosInstance } from "."

export const AddMovie = async (payload) => {
    try{
        const response = await axiosInstance.post('/api/movies/add-movie',payload);
        return response.data
    }catch(err){
        return err.response
    }
}
```
Heer the *payload* is the form data and the respective endpoint is `/api/movies/add-movie`.

Now lets implement the onFinish method, as exaplined:

```javascript
import React from "react";
import { Col, Form, message, Modal, Row } from "antd";
import Button from "../../components/Button";
import { useDispatch } from "react-redux";
import { HideLoading, ShowLoading } from "../../redux/loadersSlice";
import { AddMovie } from "../../apicalls/movies";
import moment from "moment";

function MovieForm({
  showMovieFormModal,
  setShowMovieFormModal,
  selectedMovie,
  setSelectedMovie,
  getData,
  formType,
}) {
  if (selectedMovie) {
    selectedMovie.releaseDate = moment(selectedMovie.releaseDate).format(
      "YYYY-MM-DD"
    );
  }

  const dispatch = useDispatch();
  const onFinish = async (values) => {
    try {
      dispatch(ShowLoading());
      let response = null;

      if (formType === "add") {
        response = await AddMovie(values);
      } else {
        response = await UpdateMovie({
          ...values,
          movieId: selectedMovie._id,
        });
      }

      if (response.success) {
        getData();
        message.success(response.message);
        setShowMovieFormModal(false);
      } else {
        message.error(response.message);
      }
      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };

  return (
    <Modal
      title = {formType === "add" ? "ADD MOVIE" : "EDIT MOVIE"}
      open = {showMovieFormModal}
      onCancel = {() => {
        setShowMovieFormModal(false);
        setSelectedMovie(null);
      }}
      footer = {null}
      width = {800}
    >
      <Form layout = "vertical" initialValues = {selectedMovie} onFinish = {onFinish}>
        <Row gutter = {16}>
          <Col span = {24}>
            <Form.Item label = "Movie Name" name = "title">
              <input type = "text" />
            </Form.Item>
          </Col>

          <Col span = {24}>
            <Form.Item label = "Movie Description" name = "description">
              <textarea type = "text" />
            </Form.Item>
          </Col>

          <Col span = {8}>
            <Form.Item label = "Movie Duration (Min)" name="duration">
              <input type = "number" />
            </Form.Item>
          </Col>

          <Col span = {8}>
            <Form.Item label = "Language" name = "language">
              <select name = "" id = "">
                <option value = "">Select Language</option>
                <option value = "Telugu">Telugu</option>
                <option value = "English">English</option>
                <option value = "Hindi">Hindi</option>
                <option value = "Tamil">Tamil</option>
              </select>
            </Form.Item>
          </Col>

          <Col span = {8}>
            <Form.Item label = "Movie Release Date" name = "releaseDate">
              <input type = "date" />
            </Form.Item>
          </Col>

          <Col span = {8}>
            <Form.Item label = "Genre" name = "genre">
              <select name = "" id = "">
                <option value = "">Select Genre</option>
                <option value = "Action">Action</option>
                <option value = "Comedy">Comedy</option>
                <option value = "Drama">Drama</option>
                <option value = "Romance">Romance</option>
              </select>
            </Form.Item>
          </Col>
          <Col span = {16}>
            <Form.Item label = "Poster URL" name = "poster">
              <input type = "text" />
            </Form.Item>
          </Col>
        </Row>

        <div className = "flex justify-end gap - 1">
          <Button
            title = "Cancel"
            variant = "outlined"
            type = "button"
            onClick = {() => {
              setShowMovieFormModal(false);
              setSelectedMovie(null);
            }}
          />
          <Button title = "Save" type = "submit" />
        </div>
      </Form>
    </Modal>
  );
}

export default MovieForm;
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/352/original/upload_a70e2e0e32a7532230b2f7a7365ac26c.png?1695975681)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/353/original/upload_41c18a345df705ec9018fa1510263b73.png?1695975706)


The provided JavaScript code defines an `onFinish` function that handles form submissions asynchronously:

1. **Try-Catch Block**:<br> Wraps the code in a try-catch block to handle potential errors.

2. **Dispatch Loading Indicator**:<br> Dispatches a loading indicator using the `ShowLoading` action.

3. **Conditional API Call**:<br> Depending on the `formType` (add or update), it makes an API call to either add a new movie or update an existing one.

4. **API Response Handling**:<br> If the API call is successful (`response.success` is true), it triggers a data refresh (`getData()`), displays a success message, and hides the modal.
   - If the API call fails, it displays an error message.

5. **Error Handling**:<br> In case of any errors during the process, it displays an error message and hides the loading indicator.


To show the added movies lets see the getdata function which is used to setMovies as in the below code:

```javascript
import React, { useEffect } from "react";
import Button from "../../components/Button";
import MovieForm from "./MovieForm";
import moment from "moment";
import { message, Table } from "antd";
import { useDispatch } from "react-redux";
import { HideLoading, ShowLoading } from "../../redux/loadersSlice";
 import { DeleteMovie, GetAllMovies } from "../../apicalls/movies";

function MoviesList() {
  const [movies, setMovies] = React.useState([]);
  const [showMovieFormModal, setShowMovieFormModal] = React.useState(false);
  const [selectedMovie, setSelectedMovie] = React.useState(null);
  const [formType, setFormType] = React.useState("add");
  const dispatch = useDispatch();
  const getData = async () => {
    try {
      dispatch(ShowLoading());
      const response = await GetAllMovies();
      if (response.success) {
        setMovies(response.data);
      } else {
        message.error(response.message);
      }
      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };
```

The React component, `MoviesList`, handles the rendering and management of a list of movies. Here's  explanation of its functionality:

1. **State Variables**:
   - `movies`: Stores an array of movie data.
   - `showMovieFormModal`: Controls the visibility of a movie form modal.
   - `selectedMovie`: Keeps track of the currently selected movie for editing.
   - `formType`: Specifies whether the form is for adding ("add") or updating ("update") a movie.

2. **Dispatch and API Functions**:
   - `dispatch`: Provides access to the Redux dispatch function.
   - `getData()`: An asynchronous function that fetches movie data using the `GetAllMovies` API call.
     - It dispatches a "ShowLoading" action to display a loading indicator.
     - Upon success, it updates the `movies` state with the fetched data.
     - If the API call fails, it displays an error message using the Ant Design `message` component and hides the loading indicator.

3. **Component Rendering**:
   - The component renders a list of movies in a table format using the Ant Design `Table` component.
   - Each row in the table represents a movie and displays its details.
   - The component also provides buttons to add a new movie and edit existing movies.

4. **Modal Handling**:
   - Clicking the "Add Movie" button sets `formType` to "add" and shows the movie form modal.
   - Clicking the "Edit" button for a specific movie sets `formType` to "update," populates `selectedMovie` with the movie data, and opens the modal for editing.

5. **Effect Hook**:
   - The `useEffect` hook is used to trigger the `getData` function when the component mounts, ensuring that movie data is fetched and displayed.

Overall, this component manages movie data, handles API calls for fetching movies, and provides a user interface for adding and editing movie information.


We also need to write the get route in the movieRoute.js file : 

```javascript
//get all the movies
router.get('/get-all-movies', authMiddleware ,async(req,res) => {
    try{
        const movies = await Movie.find();
        res.send({
            success:true,
            message:"All Movie Fetched",
            data:movies,
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})
```

This Express.js route handler responds to a GET request at '/get-all-movies' after authenticating the user. It retrieves all movie records from a database using the `Movie.find()` method. If successful, it sends a JSON response indicating success, along with the fetched movie data.

In case of any errors during database access, it responds with an error message. This route is designed to provide a list of all movies and is typically used in the context of a web application or API for accessing movie data.

Now also implement the api call for the get all movies, 

```javascript
//get all the movies

export const GetAllMovies = async() => {
    try{
        const response = await axiosInstance.get('/api/movies/get-all-movies');
        return response.data;
    }catch(err){
        return err.response
    }
}
```
As you can see the changes in the admin page as below:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/353/original/upload_41c18a345df705ec9018fa1510263b73.png?1695975706)


As you can see in the above image that there are two button one like dustbin and other is the pen like which are used for delete and modifying the details  of the movie added.

```javascript
import React from "react";
import { Col, Form, message, Modal, Row } from "antd";
import Button from "../../components/Button";
import { useDispatch } from "react-redux";
import { HideLoading, ShowLoading } from "../../redux/loadersSlice";
import { AddMovie, UpdateMovie } from "../../apicalls/movies";
import moment from "moment";

function MovieForm({
  showMovieFormModal,
  setShowMovieFormModal,
  selectedMovie,
  setSelectedMovie,
  getData,
  formType,
}) {
  if (selectedMovie) {
    selectedMovie.releaseDate = moment(selectedMovie.releaseDate).format(
      "YYYY-MM-DD"
    );
  }

  const dispatch = useDispatch();
  const onFinish = async (values) => {
    try {
      dispatch(ShowLoading());
      let response = null;

      if (formType === "add") {
        response = await AddMovie(values);
      } else {
        response = await UpdateMovie({
          ...values,
          movieId: selectedMovie._id,
        });
      }

      if (response.success) {
        getData();
        message.success(response.message);
        setShowMovieFormModal(false);
      } else {
        message.error(response.message);
      }
      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };

  return (
    <Modal
      title = {formType === "add" ? "ADD MOVIE" : "EDIT MOVIE"}
      open = {showMovieFormModal}
      onCancel = {() => {
        setShowMovieFormModal(false);
        setSelectedMovie(null);
      }}
      footer = {null}
      width = {800}
    >
      <Form layout = "vertical" initialValues = {selectedMovie} onFinish = {onFinish}>
        <Row gutter = {16}>
          <Col span = {24}>
            <Form.Item label = "Movie Name" name = "title">
              <input type = "text" />
            </Form.Item>
          </Col>

          <Col span = {24}>
            <Form.Item label = "Movie Description" name = "description">
              <textarea type = "text" />
            </Form.Item>
          </Col>

          <Col span = {8}>
            <Form.Item label = "Movie Duration (Min)" name = "duration">
              <input type = "number" />
            </Form.Item>
          </Col>

          <Col span = {8}>
            <Form.Item label = "Language" name = "language">
              <select name = "" id = "">
                <option value = "">Select Language</option>
                <option value = "Telugu">Telugu</option>
                <option value = "English">English</option>
                <option value = "Hindi">Hindi</option>
                <option value = "Tamil">Tamil</option>
              </select>
            </Form.Item>
          </Col>

          <Col span = {8}>
            <Form.Item label = "Movie Release Date" name = "releaseDate">
              <input type = "date" />
            </Form.Item>
          </Col>

          <Col span = {8}>
            <Form.Item label = "Genre" name = "genre">
              <select name = "" id = "">
                <option value = "">Select Genre</option>
                <option value = "Action">Action</option>
                <option value = "Comedy">Comedy</option>
                <option value = "Drama">Drama</option>
                <option value = "Romance">Romance</option>
              </select>
            </Form.Item>
          </Col>
          <Col span = {16}>
            <Form.Item label = "Poster URL" name = "poster">
              <input type = "text" />
            </Form.Item>
          </Col>
        </Row>

        <div className = "flex justify-end gap-1">
          <Button
            title = "Cancel"
            variant = "outlined"
            type = "button"
            onClick = {() => {
              setShowMovieFormModal(false);
              setSelectedMovie(null);
            }}
          />
          <Button title = "Save" type = "submit" />
        </div>
      </Form>
    </Modal>
  );
}

export default MovieForm;
```

The `MovieForm` component is responsible for rendering a modal that allows users to add or edit movie details. Here's a breakdown of how it handles adding and editing movies:

**Add Movie (formType === "add"):**
1. The component displays a modal with a form to input movie details.
2. Upon submitting the form, it triggers the `onFinish` function.
3. Inside `onFinish`, it dispatches a loading indicator using Redux.
4. It makes an asynchronous API call to add a new movie using `AddMovie(values)`.
5. If the API call succeeds (`response.success` is true), it triggers a data refresh by calling the `getData()` function, displays a success message, and hides the modal.
6. If the API call fails, it displays an error message.

**Edit Movie (formType === "update"):**
1. When editing a movie, the component pre-fills the form with the existing movie details.
2. Upon form submission, it triggers the `onFinish` function.
3. Inside `onFinish`, it dispatches a loading indicator using Redux.
4. It makes an asynchronous API call to update the movie details using `UpdateMovie({...values, movieId: selectedMovie._id})`.
5. If the update succeeds (`response.success` is true), it triggers a data refresh with `getData()`, shows a success message, and hides the modal.
6. If the update fails, it displays an error message.

In both cases, the component ensures a smooth user experience by managing loading states, handling API calls, and providing user feedback through messages.

Add the corresponding api call and the set the route as shown below:
```javascript
import React, { useEffect } from "react";
import Button from "../../components/Button";
import MovieForm from "./MovieForm";
import moment from "moment";
import { message, Table } from "antd";
import { useDispatch } from "react-redux";
import { HideLoading, ShowLoading } from "../../redux/loadersSlice";
 import { DeleteMovie, GetAllMovies } from "../../apicalls/movies";

function MoviesList() {
  const [movies, setMovies] = React.useState([]);
  const [showMovieFormModal, setShowMovieFormModal] = React.useState(false);
  const [selectedMovie, setSelectedMovie] = React.useState(null);
  const [formType, setFormType] = React.useState("add");
  const dispatch = useDispatch();
  const getData = async () => {
    try {
      dispatch(ShowLoading());
      const response = await GetAllMovies();
      if (response.success) {
        setMovies(response.data);
      } else {
        message.error(response.message);
      }
      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };

  const handleDelete = async (movieId) => {
    try {
      dispatch(ShowLoading());
      const response = await DeleteMovie({
        movieId,
      });
      if (response.success) {
        message.success(response.message);
        getData();
      } else {
        message.error(response.message);
      }
      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };

  const columns = [
    {
      title: "Poster",
      dataIndex: "poster",
      render: (text, record) => {
        return (
          <img
            src = {record.poster}
            alt = "poster"
            height = "60"
            width = "80"
            className = "br-1"
          />
        );
      },
    },
    {
      title: "Name",
      dataIndex: "title",
    },

    {
      title: "Description",
      dataIndex: "description",
    },
    {
      title: "Duration",
      dataIndex: "duration",
    },
    {
      title: "Genre",
      dataIndex: "genre",
    },
    {
      title: "Language",
      dataIndex: "language",
    },
    {
      title: "Release Date",
      dataIndex: "releaseDate",
      render: (text, record) => {
        return moment(record.releaseDate).format("DD-MM-YYYY");
      },
    },
    {
      title: "Action",
      dataIndex: "action",
      render: (text, record) => {
        return (
          <div className = "flex gap - 1">
            <i
              className = "ri-delete-bin-line"
              onClick = {() => {
                handleDelete(record._id);
              }}
            ></i>
            <i
              className = "ri-pencil-line"
              onClick = {() => {
                setSelectedMovie(record);
                setFormType("edit");
                setShowMovieFormModal(true);
              }}
            ></i>
          </div>
        );
      },
    },
  ];

  useEffect(() => {
    getData();
  }, []);

  return (
    <div>
      <div className = "flex justify-end mb - 1">
        <Button
          title = "Add Movie"
          variant = "outlined"
          onClick = {() => {
            setShowMovieFormModal(true);
            setFormType("add");
          }}
        />
      </div>

      <Table columns = {columns} dataSource = {movies} />

      {showMovieFormModal && (
        <MovieForm
          showMovieFormModal = {showMovieFormModal}
          setShowMovieFormModal = {setShowMovieFormModal}
          selectedMovie = {selectedMovie}
          setSelectedMovie = {setSelectedMovie}
          formType = {formType}
          getData = {getData}
        />
      )}
    </div>
  );
}

export default MoviesList;
```

The `MoviesList` React component manages the update and delete functionalities for movie records displayed in a table. Here's how these functionalities work:

**Update Functionality:**
1. When the edit icon is clicked (`<i className="ri-pencil-line">`), it triggers the `handleDelete` function.
2. `handleDelete` sets the `selectedMovie` state with the movie data and switches the `formType` to "edit" to indicate an edit operation.
3. It sets `showMovieFormModal` to `true` to display the movie form modal for editing.
4. The user can modify the movie details in the form and click "Save" to update the movie.
5. Upon saving, the `onFinish` function in the `MovieForm` component sends an API request to update the movie's information.
6. If successful, it triggers `getData()` to refresh the movie list with the updated data.

**Delete Functionality:**
1. When the delete icon is clicked (`<i className="ri-delete-bin-line">`), it triggers the `handleDelete` function.
2. `handleDelete` sends an API request to delete the movie record with the specified `movieId`.
3. If the deletion is successful, it displays a success message and triggers `getData()` to refresh the movie list, excluding the deleted movie.
4. If the deletion fails, it displays an error message.

These functionalities allow users to update and delete movie records directly from the user interface, with appropriate feedback messages for success or failure.

The relative route for the upadte movie and the delete movie as below: 

```javascript
//update a movie
router.post('/update-movie', authMiddleware ,async (req,res) => {
    try{
        await Movie.findByIdAndUpdate(req.body.movieId,req.body);
        res.send({
            success:true,
            message:"Movie updated"
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message,
        })
    }
})

//delete a movie

router.post('/delete-movie',authMiddleware,async (req,res) => {
    try{
        await Movie.findByIdAndDelete(req.body.movieId);
        res.send({
            success:true,
            message:"Movie Deleted"
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/355/original/upload_9f4961d70b0e24f1179382489a53d370.png?1695976453)

As explained in the below image, that the theater owner do not have the rights to add the movies unleass these are the rights of the admin that it can add the movies to the particular theaters.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/356/original/upload_69d257eb2f83f29f73c5a19aac936c01.png?1695976689)


We will give two rights to the users as follows:
1. Book a show
2. Apply for theaters(This requires Admin rights)

If a normal users login to the application it will not redirected to the admin page, it will go to the profile page.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/357/original/upload_15e44afb185c3ed7ac241ebbb7048d98.png?1695976776)

In the profile folder create two files named as TheaterList and theaterForm.

In the index.js we will create appy for theater as follows:

```javascript
import React from "react";
import { Tabs } from "antd";
// import { useSelector, useDispatch } from "react-redux";
import PageTitle from "../../components/PageTitle";
import TheatresList from "./TheatresList";
import Bookings from "./Bookings";
// import Bookings from "./Bookings";
function Profile() {
  return (
    <div>
      <PageTitle title = "Profile" />

      <Tabs defaultActiveKey = "1">
        <Tabs.TabPane tab = "Bookings" key = "1">
           <Bookings/>
        </Tabs.TabPane>
        <Tabs.TabPane tab = "Apply for Theater" key = "2">
           <TheatresList/>
           {/* List of Theatre */}
        </Tabs.TabPane>
      </Tabs>
    </div>
  );
}

export default Profile;
```


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/358/original/upload_03887272bb275ed1c08d3376572f5c3f.png?1695976874)

This React component, `Profile`, renders a user profile page with two tabs using the Ant Design `Tabs` component:

1. **Page Title**: Displays a page title with "Profile."

2. **Tabs**:
   - Two tabs are created, with the first tab labeled "Bookings" and the second tab labeled "Apply for Theater."
   - The "Bookings" tab (`<Bookings />`) displays user booking information.
   - The "Apply for Theater" tab (`<TheatresList />`) displays a list of theaters or provides a way to apply for theaters, but the specific implementation details are commented out.
   - `defaultActiveKey` is set to "1" to make the "Bookings" tab the default active tab when the page loads.

This component is part of a user profile page and allows users to navigate between their bookings and theater-related actions. 


Now start working for the apply for theaters that have two components as theaterForm and theaterList which are pretty much similar as we created for the movies components.
 
For the TheaterList:

```javascript
import React, { useEffect, useState } from "react";
import Button from "../../components/Button";
import { useNavigate } from "react-router-dom";
import TheatreForm from "./TheatresForm";
import {
  DeleteTheatre,
  GetAllTheatres,
  GetAllTheatresByOwner,
} from "../../apicalls/theatres";
import { useDispatch, useSelector } from "react-redux";
import { HideLoading, ShowLoading } from "../../redux/loadersSlice";
import { message, Table } from "antd";
import Shows from "./Shows";

function TheatresList() {
  const { user } = useSelector((state) => state.users);
  const [showTheatreFormModal = false, setShowTheatreFormModal] =
    useState(false);
  const [selectedTheatre = null, setSelectedTheatre] = useState(null);
  const [formType = "add", setFormType] = useState("add");
  const [theatres, setTheatres] = useState([]);

  const [openShowsModal = false, setOpenShowsModal] = useState(false);

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const getData = async () => {
    try {
      dispatch(ShowLoading());
      const response = await GetAllTheatresByOwner({
        owner: user._id,
      });
      if (response.success) {
        setTheatres(response.data);
      } else {
        message.error(response.message);
      }
      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };

  const handleDelete = async (id) => {
    try {
      dispatch(ShowLoading());
      const response = await DeleteTheatre({ theatreId: id });
      if (response.success) {
        message.success(response.message);
        getData();
      } else {
        message.error(response.message);
      }
      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };

  const columns = [
    {
      title: "Name",
      dataIndex: "name",
    },
    {
      title: "Address",
      dataIndex: "address",
    },
    {
      title: "Phone",
      dataIndex: "phone",
    },
    {
      title: "Email",
      dataIndex: "email",
    },
    {
      title: "Status",
      dataIndex: "isActive",
      render: (text, record) => {
        if (text) {
          return "Approved";
        } else {
          return "Pending / Blocked";
        }
      },
    },
    {
      title: "Action",
      dataIndex: "action",
      render: (text, record) => {
        return (
          <div className = "flex gap-1 items-center">
            <i
              className = "ri-delete-bin-line"
              onClick = {() => {
                handleDelete(record._id);
              }}
            ></i>
            <i
              className = "ri-pencil-line"
              onClick = {() => {
                setFormType("edit");
                setSelectedTheatre(record);
                setShowTheatreFormModal(true);
              }}
            ></i>

            {record.isActive && (
              <span
                className = "underline"
                onClick = {() => {
                  setSelectedTheatre(record);
                  setOpenShowsModal(true);
                }}
              >
                Shows
              </span>
            )}
          </div>
        );
      },
    },
  ];

  useEffect(() => {
    getData();
  }, []);
  return (
    <div>
      <div className = "flex justify-end mb-1">
        <Button
          variant = "outlined"
          title = "Add Theatre"
          onClick = {() => {
            setFormType("add");
            setShowTheatreFormModal(true);
          }}
        />
      </div>

      <Table columns = {columns} dataSource = {theatres} />

      {showTheatreFormModal && (
        <TheatreForm
          showTheatreFormModal = {showTheatreFormModal}
          setShowTheatreFormModal = {setShowTheatreFormModal}
          formType = {formType}
          setFormType = {setFormType}
          selectedTheatre = {selectedTheatre}
          setSelectedTheatre = {setSelectedTheatre}
          getData = {getData}
        />
      )}

      {openShowsModal && (
        <Shows
          openShowsModal = {openShowsModal}
          setOpenShowsModal = {setOpenShowsModal}
          theatre = {selectedTheatre}
        />
      )}
    </div>
  );
}

export default TheatresList;
```


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/359/original/upload_9cfd56a37fd2c9469b303f53c484df8a.png?1695976979)

The `TheatresList` React component manages a list of theaters and provides functionality for viewing, adding, editing, and deleting theaters. Here are the key points:

1. **State Management**:
   - It utilizes React `useState` hooks to manage various states such as `showTheatreFormModal`, `selectedTheatre`, `formType`, `theatres`, and `openShowsModal`.

2. **Data Fetching**:
   - The `getData` function retrieves theaters associated with the current user from the API using `GetAllTheatresByOwner`.
   - It dispatches loading indicators and handles success and error responses.

3. **Table Display**:
   - The component renders theater data in a table using Ant Design's `Table` component.
   - Each row displays theater details and offers options to edit, delete, or view shows associated with a theater.

4. **Edit and Delete Functionality**:
   - Clicking the edit icon triggers the `setFormType` and `setSelectedTheatre` functions to prepare the theater for editing and opens the theater form modal.
   - Clicking the delete icon triggers the `handleDelete` function, which deletes the theater and refreshes the data.

5. **Add Functionality**:
   - Clicking the "Add Theatre" button opens the theater form modal for adding a new theater.

6. **Shows Modal**:
   - If a theater is active, clicking "Shows" opens a modal (`<Shows />`) to view shows associated with that theater.

7. **UseEffect**:
   - A `useEffect` hook fetches theater data when the component mounts, ensuring up-to-date information.

8. **Redux and Navigation**:
   - It utilizes Redux for dispatching loading actions and stores user data.
   - The `useNavigate` hook from React Router DOM is imported but not used in this component.

In summary, this component provides a comprehensive interface for managing theaters, including viewing, editing, deleting, and adding new theaters, as well as viewing shows associated with active theaters.

For the TheaterForm:

```javascript
import { Form, message, Modal } from "antd";
import React from "react";
import { useDispatch, useSelector } from "react-redux";
 import { AddTheatre,UpdateTheatre } from "../../apicalls/theatres";
import Button from "../../components/Button";
import { HideLoading, ShowLoading } from "../../redux/loadersSlice";

function TheatreForm({
  showTheatreFormModal,
  setShowTheatreFormModal,
  formType,
  setFormType,
  selectedTheatre,
  setSelectedTheatre,
  getData,
}) {
  const { user } = useSelector((state) => state.users);
  const dispatch = useDispatch();
  const onFinish = async (values) => {
    values.owner = user._id;
    try {
      dispatch(ShowLoading());
      let response = null;
      if (formType === "add") {
        response = await AddTheatre(values);
      } else {
        values.theatreId = selectedTheatre._id;
        response = await UpdateTheatre(values);
      }

      if (response.success) {
        message.success(response.message);
        setShowTheatreFormModal(false);
        setSelectedTheatre(null);
        getData();
      } else {
        message.error(response.message);
      }

      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };

  return (
    <Modal
      title = {formType === "add" ? "Add Theatre" : "Edit Theatre"}
      open = {showTheatreFormModal}
      onCancel = {() => {
        setShowTheatreFormModal(false);
        setSelectedTheatre(null);
      }}
      footer = {null}
    >
      <Form
        layout = "vertical"
        onFinish = {onFinish}
        initialValues = {selectedTheatre}
      >
        <Form.Item
          label = "Name"
          name = "name"
          rules = {[{ required: true, message: "Please input theatre name!" }]}
        >
          <input type = "text" />
        </Form.Item>

        <Form.Item
          label = "Address"
          name = "address"
          rules = {[{ required: true, message: "Please input theatre address!" }]}
        >
          <textarea type = "text" />
        </Form.Item>

        <Form.Item
          label = "Phone Number"
          name = "phone"
          rules = {[
            { required: true, message: "Please input theatre phone number!" },
          ]}
        >
          <input type = "text" />
        </Form.Item>

        <Form.Item
          label = "Email"
          name = "email"
          rules = {[{ required: true, message: "Please input theatre email!" }]}
        >
          <input type = "text" />
        </Form.Item>
        <div className = "flex justify-end gap-1">
          <Button
            title = "Cancel"
            variant = "outlined"
            type = "button"
            onClick = {() => {
              setShowTheatreFormModal(false);
              setSelectedTheatre(null);
            }}
          />
          <Button title = "Save" type = "submit" />
        </div>
      </Form>
    </Modal>
  );
}

export default TheatreForm;
```


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/360/original/upload_90ac9cc27b849665c6a22e036b5bdd3b.png?1695977124)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/361/original/upload_4434c4051a5de1fe86f5e6f9479a49db.png?1695977147)



The `TheatreForm` React component manages the form for adding and editing theater details. It works as follows:

1. **State and Props**:
   - It receives various props such as `showTheatreFormModal`, `setShowTheatreFormModal`, `formType`, `selectedTheatre`, `setSelectedTheatre`, and `getData`.
   - It retrieves the current user from the Redux store using `useSelector`.
   - It uses `useDispatch` to dispatch loading actions.

2. **Form Submission**:
   - Upon form submission, the `onFinish` function is called.
   - It sets the `owner` field in the form data to the current user's ID.
   - It sends an API request to either add a new theater using `AddTheatre` or update an existing theater using `UpdateTheatre` based on the `formType`.
   - If the API call succeeds, it displays a success message, closes the modal, resets selected theater, and refreshes the theater data using the `getData` function.
   - If the API call fails, it displays an error message.

3. **Form Structure**:
   - The form includes fields for theater name, address, phone number, and email.
   - Validation rules ensure that required fields are filled in.

4. **Modal Display**:
   - The component renders a modal with the title "Add Theatre" or "Edit Theatre" based on the `formType`.
   - The modal opens when `showTheatreFormModal` is `true` and closes when canceled.

5. **Button Actions**:
   - Buttons for "Cancel" and "Save" are displayed at the bottom of the form.
   - Clicking "Cancel" closes the modal and resets the selected theater.
   - Clicking "Save" triggers the form submission.

This component provides a user-friendly interface for adding and editing theater details and communicates with the API to save changes.

Now lets define the routes for the theaterRoutes similar to the movies route for the add, delete , and update. But before this we should create the theaterModel so that we can create the data.

theaterModel.js will include like:

```javascript
const mongoose = require('mongoose');

const theatreSchema = new mongoose.Schema({
    name:{
        type:String,
        required:true,
    },
    address:{
        type:String,
        required:true,
    },
    phone:{
        type:Number,
        required:true,
    },
    email:{
        type:String,
        required:true
    },
    owner:{
        type:mongoose.Schema.Types.ObjectId,
        ref:'users'
    },
    isActive:{
        type:Boolean,
        default:false
    }
},
    {timestamps:true}
)

module.exports = mongoose.model('theatres',theatreSchema);
```

This code defines a MongoDB schema for theaters using Mongoose, a popular Node.js library for interacting with MongoDB. Here's an explanation:

1. **Mongoose and Schema Creation**:
   - The code imports the `mongoose` library, which provides tools for working with MongoDB.
   - It creates a new Mongoose schema called `theatreSchema` using the `mongoose.Schema` constructor.

2. **Schema Fields**:
   - The schema defines several fields for theater documents:
     - `name`: A required field of type String, representing the theater's name.
     - `address`: A required field of type String, representing the theater's address.
     - `phone`: A required field of type Number, representing the theater's phone number.
     - `email`: A required field of type String, representing the theater's email address.
     - `owner`: A reference field of type mongoose.Schema.Types.ObjectId, referring to the 'users' collection. It indicates the owner or creator of the theater.
     - `isActive`: A Boolean field, which is optional and defaults to `false`. It can be used to mark a theater as active or inactive.

3. **Timestamps**:
   - The schema includes timestamps, which automatically add `createdAt` and `updatedAt` fields to each theater document. These fields store the creation and last update timestamps.

4. **Exporting the Model**:
   - The schema is used to create a Mongoose model using `mongoose.model`. This model is named 'theatres' and is based on the `theatreSchema`. It represents the collection in the MongoDB database where theater documents will be stored.


theaterRoute.js will include like:

```javascript
const router = require("express").Router();
const authMiddleware = require("../middlewares/authMiddleware");
const Theatre = require('../models/theatreModels');
const Show = require('../models/showModel');

//add a theatre
router.post('/add-theatre',authMiddleware,async(req,res) => {
    try{
        const newTheatre = new Theatre(req.body);
        await newTheatre.save();
        res.send({
            success:true,
            message:"Theatre Added"
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})
```
This Express.js router handles the addition of theaters to a database. Here's a brief explanation:

- The router is set up to handle POST requests to the '`/add-theatre`' endpoint.
- It utilizes the 'authMiddleware' to ensure authentication before proceeding.
- Upon receiving a request, it creates a new theater instance using the provided request body data.
- The new theater is saved to the database.
- If the operation succeeds, it sends a success response with a "Theatre Added" message.
- In case of an error, it sends a failure response with an error message.

Add the theaterRoute into the server as well, after this we just need to create the form , as shown below `TheaterForm.js` and in the theaterList.js we are having the `getdata()` function:

```javascript
 const getData = async () => {
    try {
      dispatch(ShowLoading());
      const response = await GetAllTheatresByOwner({
        owner: user._id,
      });
      if (response.success) {
        setTheatres(response.data);
      } else {
        message.error(response.message);
      }
      dispatch(HideLoading());
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };
```

The `getData` function is an asynchronous operation that retrieves theater data owned by a specific user. It dispatches a loading state, sends an API request with the user's ID, and updates the component's state with the received data if the request succeeds.

In case of a request failure, it displays an error message. Finally, it dispatches a "HideLoading" action to remove the loading indicator. This function ensures a user-friendly interface for fetching and displaying theater information while handling potential errors gracefully.

In the **theaterRoutes.js** we are having the route to get all the theater as below:
```javascript
//get theatre owner specific
router.post('/get-all-theatre-by-owner', authMiddleware,async (req,res) => {
    try{
        const theatres = await Theatre.find({owner:req.body.owner})
        res.send({
            success:true,
            message:"Theatre added",
            data:theatres
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/362/original/upload_5f0fa81da0238fbdf4895de553f190bc.png?1695977269)

This Express.js router handles a POST request to fetch theaters owned by a specific user. Here's a concise explanation :

- The router defines a route at '`/get-all-theatre-by-owner`' that requires authentication via '`authMiddleware`'.
- Upon receiving the request, it attempts to find theaters in the database that match the provided owner's ID.
- If theaters are found, it sends a success response with a "Theatre added" message and includes the theater data.
- In case of an error (e.g., database query failure), it sends a failure response with an error message.
- This route allows users to retrieve theaters associated with their owner ID, facilitating owner-specific theater data access.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/363/original/upload_4ed8dec54ec2a7ba137801d844893220.png?1695977326)

