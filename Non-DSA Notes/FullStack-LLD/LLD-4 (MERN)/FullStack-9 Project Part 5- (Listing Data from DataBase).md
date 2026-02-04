
## Agenda

We will try to cover most of these topics in today's sessions and the remaining in the next.
* Build the shows components
* Build the seating arrangements
* Book tickets
* Make Payments
* Deploy
It is going to be a bit challenging, advanced, but very interesting session covering topics that are asked very frequently in interviews.

So let's start.


### Handle the Update and Delete Functionalities 

In the button.js add the following code:
import React from "react";

```javascript
function Button({ title, onClick, variant, disabled, fullWidth, type }) {
  let className = "bg-primary p-1 text-white";

  if (fullWidth) {
    className += " w-full";
  }
  if (variant === "outlined") {
    className = className.replace(
      "bg-primary",
      "border border-primary text-primary bg-white"
    );
  }

  return (
    <button
      className = {className}
      type = {type}
      onClick = {onClick}
      disabled = {disabled}
    >
      {title}
    </button>
  );
}

export default Button;
```

The provided React component, named `Button`, is a reusable button element with customizable styles. Here's an explanation of the code:

1. **Props**:<br> The component accepts various props for customization, including `title` (button text), `onClick` (click event handler), `variant` (button style), `disabled` (disabling the button), `fullWidth` (expands button to full width), and `type` (button type, e.g., submit or button).

2. **Conditional Styling**:<br> The component dynamically applies CSS classes based on the props. It defaults to a primary background color and white text. If `fullWidth` is true, it expands to full width. If `variant` is "outlined," it changes to a bordered style with different text and background colors.

3. **Button Element**:<br> The component renders an HTML button element with the defined styles and properties, making it versatile for various UI button needs.

4. **Reusability**:<br> This component promotes code reusability by allowing developers to create buttons with different styles and behaviors based on the provided props. It simplifies button creation in React applications.

In the theaterRoute.js file lets set the routes for the update and delete buttons as follows:

```javascript
//update theatre 

router.put("/update-theatre",authMiddleware ,async(req,res) => {
    try{
        await Theatre.findByIdAndUpdate(req.body.theatreId,req.body);
        res.send({
            success:true,
            message:"Theatre updated"
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})

//delete a theatre
router.post('/delete-theatre', authMiddleware,async (req,res) => {
    try{
        await Theatre.findByIdAndDelete(req.body.theatreId)
        res.send({
            success:true,
            message:"Theatre Deleted"
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})
```

These Express.js router endpoints handle theater-related operations such as updating and deleting theaters. Here's a detailed explanation:

1. **Update Theatre (PUT /update-theatre)**:
   - This route is accessible only to authenticated users due to the 'authMiddleware'.
   - It receives a request containing the theater ID (`theatreId`) and new theater data (`req.body`).
   - Using `Theatre.findByIdAndUpdate`, it updates the theater in the database based on the provided theater ID.
   - Upon a successful update, it responds with a success message, indicating that the theater has been updated.
   - In case of an error (e.g., database update failure), it sends a failure response with an error message.

2. **Delete Theatre (POST /delete-theatre)**:
   - Similarly, this route is protected by 'authMiddleware' for authenticated access.
   - It accepts a request with the theater ID (`theatreId`) to be deleted.
   - Utilizing `Theatre.findByIdAndDelete`, it removes the specified theater from the database.
   - Upon successful deletion, it responds with a success message, confirming that the theater has been deleted.
   - In the event of an error (e.g., database deletion failure), it returns a failure response along with an error message.
   
These routes provide essential functionality for managing theater data, enabling updates and deletions while ensuring user authentication.


Also set the api calls in the theater.js files for the update and delete as follows:

```javascript
export const UpdateTheatre = async (payload) => {
    try{
        const response = await axiosInstance.put('/api/theatres/update-theatre',payload);
        return response.data;
    }catch(err){
        return err.response;
    }
}

export const DeleteTheatre = async(payload) => {
    try{
        const response = await axiosInstance.post('/api/theatres/delete-theatre',payload);
        return response.data
    }catch(err){
        return err.message
    }
}
```

These JavaScript functions facilitate client-side communication with the server to update and delete theaters using Axios:

1. **UpdateTheatre**:
   - This function sends a PUT request to the server's '/api/theatres/update-theatre' endpoint with a payload containing theater data to be updated.
   - Upon success, it returns the response data from the server.
   - In case of an error, it returns the error response received.

2. **DeleteTheatre**:
   - It sends a POST request to the server's '/api/theatres/delete-theatre' endpoint, including the theater ID in the payload for deletion.
   - If the deletion is successful, it returns the response data.
   - In case of an error, it returns an error message.

These functions abstract the HTTP requests needed for updating and deleting theaters, allowing the client application to interact with the server seamlessly while handling potential errors gracefully.

Let's also update the delete and update functionalities and the getdata() in TheaterList.js file as follows:

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
      <div className = "flex justify-end mb - 1">
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

Here's an explanation of the `handleDelete` and update functionality in the `TheatresList` component:

1. **handleDelete Function**:
   - The `handleDelete` function is triggered when a user clicks the delete icon for a theater record.
   - It sends an asynchronous request to delete the theater using the `DeleteTheatre` API call.
   - Upon success, it displays a success message and then refreshes the list of theaters by calling the `getData` function.
   - In case of an error during deletion, it displays an error message.

2. **Update Functionality**:
   - The update functionality is initiated when a user clicks the edit icon for a theater record.
   - It sets the `formType` to "edit" and populates the `TheatreForm` with the details of the selected theater.
   - The user can modify the theater details and save the changes.
   - Upon saving, it sends an asynchronous request to update the theater information using the `UpdateTheatre` API call.
   - If the update is successful, it displays a success message, closes the theater form modal, resets the selected theater, and refreshes the theater list by calling the `getData` function.
   - In case of an error during the update, it displays an error message.

These functionalities allow users to interact with theater records, enabling them to delete theaters they own and edit theater information as needed.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/374/original/upload_34818e2fae2214dd5f22f8a6d2d5911c.png?1695981641)


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/375/original/upload_4281ae0cd8e8083df9ed0ebc0c05f491.png?1695981671)

Implementation of the approval and rejection

For this first we want admin to see all the records in the theater space from all the users so lets start creating the table:


```javascript
import React, { useEffect, useState } from "react";
 import { GetAllTheatres, UpdateTheatre } from "../../apicalls/theatres";
import { useDispatch, useSelector } from "react-redux";
import { HideLoading, ShowLoading } from "../../redux/loadersSlice";
import { message, Table } from "antd";

function TheatreTable() {
  const [theatres, setTheatres] = useState([]);
  const dispatch = useDispatch();

  const getData = async () => {
    try {
      dispatch(ShowLoading());
      const response = await GetAllTheatres();
      console.log(response.data);
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

  const handleStatusChange = async (theatre) => {
    try {
      dispatch(ShowLoading());
      const response = await UpdateTheatre({
        theatreId: theatre._id,
        ...theatre,
        isActive: ! theatre.isActive,
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
      title: "Owner",
      dataIndex: "owner",
      render: (text, record) => {
        return record.owner.name;
      },
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
          <div className = "flex gap-1">
            {record.isActive && (
              <span
                className = "underline"
                 onClick = {() => handleStatusChange(record)}
              >
                Block
              </span>
            )}
            {!record.isActive && (
              <span
                className = "underline"
                onClick = {() => handleStatusChange(record)}
              >
                Approve
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
      <Table columns = {columns} dataSource = {theatres}  />
    </div>
  );
}

export default TheatreTable;
```

The `TheatreTable` component manages and displays a table of theaters with the following functionality:

1. **Data Fetching**:
   - Upon component rendering, it triggers the `getData` function, which sends an asynchronous request to the server to fetch all theaters using the `GetAllTheatres` API call.
   - The retrieved theater data is displayed in a table.

2. **Status Change Handling**:
   - Each theater record in the table has an "Approve" or "Block" option in the "Status" column, depending on its current status.
   - Users can change the status of a theater by clicking on the "Approve" or "Block" link.
   - The `handleStatusChange` function sends an asynchronous request to update the theater's status using the `UpdateTheatre` API call.
   - Upon success, it displays a success message, updates the status, and refreshes the theater list.
   - If the update fails, it displays an error message.

3. **Table Columns**:
   - The table displays theater details such as name, address, phone, email, owner, and status.
   - The owner's name is fetched from the theater data.
   - The status is displayed as "Approved" or "Pending / Blocked."
   - The "Action" column allows users to change the theater's status.

Overall, this component provides an interface for administrators to manage and update the approval status of theaters efficiently.

Now set the theaterRoute to get the deatils of all the theaters:

```javascript
//get all theatre route
router.get('/get-all-theatres',authMiddleware, async(req,res) => {
    try{
        const theatres = await Theatre.find().populate('owner');
        res.send({
            success:true,
            message:"Theatres fetched",
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

This route, accessible only to authenticated users due to the `authMiddleware`, retrieves all theaters from the database. Key points include:

1. It uses the `Theatre` model to query the database for theaters.

2. The `populate('owner')` method populates the theater's owner field, fetching owner details.

3. If successful, it responds with a success message and the theater data.

4. In case of an error, it sends a failure message with an error description.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/376/original/upload_40681e9e00749671f55a4655acedd7bf.png?1695981735)

## Building the Shows API

Now let's start creating the Shows API,  that is when a theater gets approval then we give the options of shows, delete, and update like as shown below.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/378/original/upload_0d4374cb8c3c914e2b4d3321b7f2d054.png?1695981754)

The outline of the Show api is as below: 
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/379/original/upload_a36f2d25c8cd31d52a1e574ed85cc83b.png?1695981773)

Lets start creating this above functionalities in the profile folder like as:

In the theaterList.js do the needful as shown below:
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
      <div className = "flex justify-end mb - 1">
        <Button
          variant = "outlined"
          title = "Add Theatre"
          onClick = {() => {
            setFormType("add");
            setShowTheatreFormModal(true);
          }}
        />
      </div>

      <Table columns = {columns} dataSource={theatres} />

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

Certainly, here's an explanation of `setSelectedTheatre` and other relevant points in the code:

1. **setSelectedTheatre:** This state variable is used to manage the currently selected theater. It is initially set to `null`, indicating no theater is selected.

2. **showTheatreFormModal:** Manages the visibility of the theater form modal. It is initially set to `false`, so the modal is hidden.

3. **formType:** Determines whether the theater form should be in "add" mode or "edit" mode. It is initially set to "add."

4. **theatres:** Stores an array of theater data fetched from the API.

5. **openShowsModal:** Controls the visibility of the modal for theater shows. It is initially set to `false`.

6. **handleDelete:** This function handles the deletion of a theater. It sends a request to delete a theater when the delete icon is clicked.

7. **columns:** Defines the columns for the theater table, including actions like delete, edit, and viewing shows.

8. **useEffect:** Fetches theater data from the API when the component is mounted and whenever there's a change in the `theatres` state.

9. **Button clicks and user interactions:** Various buttons and icons trigger functions like opening the theater form modal, updating theater data, deleting theaters, and viewing shows when clicked.

These elements work together to manage and display a list of theaters, allowing users to add, edit, delete, and view shows for each theater.

In the shows.js in the profile we are having:


```javascript
import { Col, Form, Modal, Row, Table, message } from "antd"
import React , {useEffect, useState} from 'react'
import Button from '../../components/Button'
import {GetAllMovies} from "../../apicalls/movies"
import {AddShow, GetAllShowsByTheatre, DeleteShow} from '../../apicalls/theatres'
import moment from "moment"
import { useDispatch } from "react-redux"
import { HideLoading, ShowLoading } from "../../redux/loadersSlice"

function Shows({ openShowsModal, setOpenShowsModal, theatre }) {

    let [view, setView] = useState("table");
    let [movies,setMovies] = useState([]);
    let [shows,setShows] = useState([]);

    const dispatch = useDispatch();


    const columns = [
        {
          title: "Show Name",
          dataIndex: "name",
        },
        {
          title: "Date",
          dataIndex: "date",
          render: (text, record) => {
            return moment(text).format("MMM Do YYYY");
          },
        },
        {
          title: "Time",
          dataIndex: "time",
        },
        {
          title: "Movie",
          dataIndex: "movie",
          render: (text, record) => {
            return record.movie.title;
          },
        },
        {
          title: "Ticket Price",
          dataIndex: "ticketPrice",
        },
        {
          title: "Total Seats",
          dataIndex: "totalSeats",
        },
        {
          title: "Available Seats",
          dataIndex: "availableSeats",
          render: (text, record) => {
            return record.totalSeats - record.bookedSeats.length;
          },
        },
        {
          title: "Action",
          dataIndex: "action",
          render: (text, record) => {
            return (
              <div className = "flex gap-1 items-center">
                {record.bookedSeats.length === 0 && (
                  <i
                    className = "ri-delete-bin-line"
                    onClick = {() => {
                      handleDelete(record._id);
                    }}
                  ></i>
                )}
              </div>
            );
          },
        },
      ];

      useEffect(() => {
          getData()
      },[])

    return (
        <Modal title = ""
            open = {openShowsModal}
            onCancel = {() => setOpenShowsModal(false)}
            width = {1400}
            footer = {null}>
            <h1 className = "text-primary text-md uppercase mb - 1">
                Theatre : {theatre.name}
            </h1>

            <hr/>

    <div className = "flex justify-between mt - 1 mb - 1 items-center">
        <h1 className = "text-md uppercase">
          {view === "table" ? "Shows" : "Add Show"}
        </h1>
        {(
          <Button
            variant = "outlined"
            title = "Add Show"
            onClick = {() => {
              setView("form");
            }}
          />
        )}
      </div>


      {view === 'table' && <Table columns = {columns} dataSource = {shows}/>}
    </Modal>
    )
}

export default Shows
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/383/original/upload_59c5630ae12b6adcde400dc70c8a1868.png?1695982147)


Certainly, here's an explanation of the provided React component code:

1. **Component Import**:<br> The code begins by importing necessary components and functions from various libraries, including Ant Design for UI components, Redux for state management, and custom API call functions for movies and shows.

2. **State Initialization**:<br> Several state variables are initialized using the `useState` hook. These include `view`, `movies`, and `shows`. `view` controls whether the component displays a table of shows or a form to add a new show. `movies` stores a list of movies fetched from the API, and `shows` stores a list of shows for the selected theatre.

3. **Redux Dispatch**:<br> The `useDispatch` hook is used to access the `dispatch` function from the Redux store. This will be used to dispatch actions to update the loading state.

4. **Table Columns**:<br> The `columns` array defines the columns for the shows table, including show name, date, time, movie, ticket price, total seats, available seats, and actions.

5. **Data Fetching**:<br> The `useEffect` hook is employed to fetch data when the component mounts. The `getData` function is called, which fetches the shows for the selected theatre.

6. **Modal Component**:<br> This component represents a modal dialog. It opens when `openShowsModal` is `true` and displays theater-related information.

7. **Conditional Rendering**:<br> The content inside the modal is conditionally rendered based on the `view` state. If `view` is "table," it displays a table of shows; if it's "form," it displays an "Add Show" form.

8. **Toggle View**:<br> The "Add Show" button allows the user to toggle between the table view and the form view for adding a new show by updating the `view` state.

9. **Rendering**:<br> Depending on the `view`, either the shows table or the "Add Show" form is displayed within the modal.

This component primarily serves as a modal for managing shows related to a theatre. It allows users to view shows in a table format and switch to a form for adding new shows.

### Show Form

Now to add the functionality of the form after clicking on the add show button is explained as below:
```javascript
{view === "form" && (
    <Form layout = "vertical" onFinish = {handleAddShow}>
      <Row gutter = {[16, 16]}>
        <Col span = {8}>
          <Form.Item
            label = "Show Name"
            name = "name"
            rules = {[{ required: true, message: "Please input show name!" }]}
          >
            <input />
          </Form.Item>
        </Col>
        <Col span = {8}>
          <Form.Item
            label = "Date"
            name = "date"
            rules = {[{ required: true, message: "Please input show date!" }]}
          >
            <input
              type = "date"
              min = {new Date()}
            />
          </Form.Item>
        </Col>

        <Col span = {8}>
          <Form.Item
            label = "Time"
            name = "time"
            rules = {[{ required: true, message: "Please input show time!" }]}
          >
            <input type = "time" />
          </Form.Item>
        </Col>

        <Col span = {8}>
          <Form.Item
            label = "Movie"
            name = "movie"
            rules = {[{ required: true, message: "Please select movie!" }]}
          >
            <select>
              <option value = "">Select Movie</option>
              {movies.map((movie) => (
                <option value = {movie._id}>{movie.title}</option>
              ))}
            </select>
          </Form.Item>
        </Col>

        <Col span = {8}>
          <Form.Item
            label = "Ticket Price"
            name = "ticketPrice"
            rules = {[
              { required: true, message: "Please input ticket price!" },
            ]}
          >
            <input type = "number" />
          </Form.Item>
        </Col>

        <Col span = {8}>
          <Form.Item
            label = "Total Seats"
            name = "totalSeats"
            rules = {[
              { required: true, message: "Please input total seats!" },
            ]}
          >
            <input type = "number" />
          </Form.Item>
        </Col>
      </Row>

      <div className = "flex justify-end gap-1">
        <Button
          variant = "outlined"
          title = "Cancel"
          onClick = {() => {
            setView("table");
          }}
        />
        <Button variant = "contained" title = "SAVE" type = "submit" />
      </div>
    </Form>
  )}

```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/384/original/upload_f1bc356a2d742ebbea3174d23feb9939.png?1695982409)


Certainly, here's an explanation of the provided code for rendering the "Add Show" form within a conditional block:

1. **Conditional Rendering**:<br> The code utilizes a conditional rendering approach based on the `view` state. When `view` is equal to "form," the "Add Show" form is rendered.

2. **Form Component**:<br> The form is created using the `<Form>` component from Ant Design. It specifies the `layout` as "vertical" to arrange form items vertically.

3. **Form Fields**:
   - **Show Name**:<br> An input field for entering the name of the show is provided. It is wrapped in a `<Form.Item>` component with validation rules to ensure that the field is required.
   - **Date**:<br> An input field with the type "date" is used for selecting the date of the show. It includes a `min` attribute to ensure that users cannot select dates in the past.
   - **Time**:<br> An input field with the type "time" allows users to input the time of the show. It is also wrapped in a `<Form.Item>` with required validation.   
   - **Movie**:<br> A `<select>` dropdown is used for selecting the movie associated with the show. It dynamically populates the options based on the movies fetched earlier and is required. 
   - **Ticket Price**:<br> Users can input the ticket price for the show as a number. It is validated as a required field.
    - **Total Seats**:<br> An input field for entering the total number of seats available for the show. It is also validated as a required field.

4. **Form Submission**:<br> The form has a "SAVE" button for submitting the data. When the form is submitted, it calls the `handleAddShow` function.

5. **Cancel Button**:<br> A "Cancel" button is provided to switch the view back to the table view by updating the `view` state to "table."



Now lets create a `showModel.js` to create the model as shown below:

```javascript
const mongoose = require('mongoose');

const showSchema = new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    date:{
        type:Date,
        required:true
    },
    time:{
        type:String,
        required:true
    },
    movie:{
        type:mongoose.Schema.Types.ObjectId,
        ref:'movies',
        required:true,
    },
    ticketPrice:{
        type:Number,
        required:true
    },
    totalSeats:{
        type:Number,
        required:true
    },
    bookedSeats:{
        type:Array,
        default:[]
    },
    theatre:{
        type:mongoose.Schema.Types.ObjectId,
        ref:"theatres",
        required:true
    }
},{timestamps:true})

module.exports = mongoose.model('shows',showSchema);
```
The provided code defines a Mongoose schema for a "shows" collection in a MongoDB database. Here's a brief explanation:

1. **Schema Definition**:<br> It defines a schema with various fields such as "name," "date," "time," "movie," "ticketPrice," "totalSeats," "bookedSeats," and "theatre."
2. **Field Types**:<br> Fields have specified data types like strings, dates, numbers, and references to other collections (e.g., "movies" and "theatres").
3. **Required Fields**:<br> Certain fields like "name," "date," "time," "movie," "ticketPrice," "totalSeats," and "theatre" are marked as required.
4. **Default Value**:<br> The "bookedSeats" field is initialized as an empty array by default.
5. **Timestamps**:<br> The schema includes timestamps for when documents are created and updated.
6. **Export**:<br> The schema is exported as a Mongoose model for use in the application, allowing interactions with the "shows" collection in the database.

In the theater.js aslo set the api calls like as shown below:
```javascript
export const AddShow = async (payload) => {
    try{
        const response = await axiosInstance.post('/api/theatres/add-show',payload);
        return response.data;
    }catch(err){
        return err.response;
    }
}
```

In the theaterRoute set the route as shown below:

```javascript
//add a Show
router.post('/add-show',authMiddleware,async(req,res) => {
    try{
        const newShow = new Show(req.body);
        await newShow.save();
        res.send({
            success:true,
            message:"Show Added"
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})
```

The provided code defines an Express.js route for adding a new show to a theater. Here's a breakdown of the code:

1. **Route Definition**:<br> This code defines a POST route at the endpoint '/add-show'. It is protected by the 'authMiddleware', which likely ensures that only authenticated users can access this endpoint.
2. **Request Handling**:<br> When a POST request is made to this endpoint, the route's callback function is executed.
3. **Show Creation**:<br> Inside the try block, a new instance of the 'Show' model (presumably defined elsewhere in the code) is created. It uses the request body (req.body) to populate the show's details, such as name, date, time, movie, ticket price, total seats, etc.
4. **Saving to Database**:<br> The new show object is then saved to the database using the 'await newShow.save()' method, which is an asynchronous operation.
5. **Response**:<br> If the show is successfully saved to the database, a success response is sent with a message indicating that the show has been added. If there's an error during the process (e.g., validation error or a database issue), an error response is sent with an error message.

**Asking Question**
How we can make sure to show every movie in the dropdown in the add show form?

```javascript
function Shows({ openShowsModal, setOpenShowsModal, theatre }) {

    let [view, setView] = useState("table");
    let [movies,setMovies] = useState([]);
    let [shows,setShows] = useState([]);

    const dispatch = useDispatch();

    const getData = async () => {
        try{
            dispatch(ShowLoading());
            const moviesResponse = await GetAllMovies();
            if(moviesResponse.success){
                setMovies(moviesResponse.data);
            }else{
                message.error(moviesResponse.message)
            }

            const showsResponse = await GetAllShowsByTheatre({theatreId:theatre._id});
            if(showsResponse.success){
                setShows(showsResponse.data)
            }else{
                message.error(showsResponse.message);
            }
            dispatch(HideLoading());
        }catch(error){
            message.error(error.message)
            dispatch(HideLoading());
        }
    }
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/385/original/upload_05ba0aae30f1336bd163108eb012b128.png?1695982707)

The provided React component, 'Shows', is responsible for managing and displaying theater shows. Here's a breakdown of the code:

1. **State Management**:<br> The component manages three pieces of state: 'view' (for toggling between table and form view), 'movies' (to store movie data), and 'shows' (to store show data).

2. **Dispatch and Data Retrieval**:<br> The 'dispatch' function from Redux is initialized. When the component mounts, the 'getData' function is called asynchronously.

3. **Data Fetching**:<br> Inside 'getData', the component dispatches a loading action and proceeds to fetch data. First, it fetches movies using 'GetAllMovies' and updates the 'movies' state with the response data if successful. It displays an error message if not.

4. **Fetching Shows by Theatre**:<br> Next, it fetches shows specific to the provided theater ('theatreId') using 'GetAllShowsByTheatre'. The retrieved shows are stored in the 'shows' state, and any error results in an error message.

5. **Loading Handling**:<br> Loading actions are dispatched and hidden during data retrieval to provide feedback to the user.

In the theaterRoute set the route to get shows based on theatres:

```javascript
//get shows based on theatres

router.post('/get-all-shows-by-theatre',authMiddleware,async(req,res) => {
    try{
        const shows = await Show.find({theatre:req.body.theatreId}).populate('movie');
        res.send({
            success:true,
            message:"Shows Fetched",
            data:shows
        })
    }catch(err){
        res.send({
            success:false,
            message:err.message
        })
    }
})
```

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/386/original/upload_4e6bc8e7e0a49e0d1c6d96cb5ff3f241.png?1695982786)

* The 'get-all-shows-by-theatre' route is protected by authentication middleware. It retrieves show data based on the provided theater ID ('`theatreId`'). 
* Using Mongoose, it fetches shows associated with the specified theater, populating the 'movie' field with movie details.
* The retrieved shows are sent as a response with success status, or an error message is provided if there's an issue with the database query.
