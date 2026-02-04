

# IMDB Clone React Website

## Project Description

We will be creating an IMDB clone, where we will fetch Real-time trending movies data and will show it in grid format, we will be designing the whole application by using Tailwind CSS.

## Features of the project

The following will be the features of our IMDB clone:

- The user will be able to view all the latest & trneding movies (IMDB API)
- User can create his own separate watchlist
- User can filter movies according to genre
- User can sort movies according to ratings
- Pagination will be implemented to move from one page to another to get updated data of other movies
- Search feature will be there for movies.
- We will be deploying this to netlify

## Wireframe 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/481/original/Screenshot_2023-09-20_170326.png?1695209627)


## Implementation

> **Note**: This lecture is in continuation to *'Full Stack LLD & Projects: React-4: IMDB Project- Part 1'*, please refer that lecture before hopping onto this one.

In this lecture we will be implementing the following features:

- Briefing Client side Routing and React Router
- Watchlist Component
- Pagination


### Component


- **WatchList.jsx**

  - This JavaScript file defines the `WatchList` component, which represents the user's watchlist section in the IMDb web application. Users can view and manage the list of movies they have added to their watchlist.
  - The component function takes several props:
    - `watchList`: An array containing the user's watchlist of movies.
    - `handleRemoveFromWatchList`: A function to handle the removal of movies from the watchlist.
    - `setWatchList`: A function to update the watchlist state.
   
  - The component also uses local state variables to manage filtering and searching of watchlist movies. These state variables include `genreList`, `currGenre`, and `search`.
  - Inside the component, there are several functions and effects that manage various aspects of the watchlist:
    - `hanldeFilter(genre)`: Updates the current genre filter when a genre is clicked.
    - `handleSearch(e)`: Updates the search query when the user types in the search input.
    - `sortIncreasing()`: Sorts the watchlist in increasing order of movie ratings.
    - `sortDecreasing()`: Sorts the watchlist in decreasing order of movie ratings.
  - The `useEffect` hook is used to populate the `genreList` state with unique genres based on the movies in the watchlist. It ensures that the genre filter options are updated whenever the watchlist changes.
  - The component's `return` statement defines the structure of the WatchList component:
    - Genre filter buttons are displayed at the top. Users can click on these buttons to filter the watchlist by genre.
    - A search input field allows users to search for movies in the watchlist based on their titles.
    - A table displays the watchlist movies, including columns for movie name, ratings, popularity, genre, and a delete option.
    - The table rows are generated based on the current genre filter and search query.
    - The ratings column headers allow users to sort the watchlist in ascending or descending order based on movie ratings.
    - The delete option in each row allows users to remove a movie from their watchlist.
  - The `WatchList` component provides essential functionality for users to manage and view their watchlist, making it a valuable feature of the IMDb web application.

**Code**:

```javascript=
import { useEffect, useState } from "react";
import genreids from "../Utility/genre";

function WatchList(props){
  let {watchList,handleRemoveFromWatchList,setWatchList} = props;
  let [genreList,setGenreList] = useState(["All Genres"]);
  let [currGenre,setCurrGenre] = useState("All Genres");
  let [search,setSearch] = useState("");

  let hanldeFilter = (genre)=>{
    setCurrGenre(genre)
  }

  let handleSearch = (e)=>{
    setSearch(e.target.value);
  }

  let sortIncreasing = ()=>{
    let sorted = watchList.sort((movieA,movieB)=>{
      return movieA.vote_average-movieB.vote_average
    })
    setWatchList([...sorted]);
  }

  let sortDecreasing = ()=>{
    let sorted = watchList.sort((movieA,movieB)=>{
      return movieB.vote_average-movieA.vote_average
    })
    setWatchList([...sorted]);
  }

    useEffect(()=>{
      let temp = watchList.map((movieObj)=>{
        return genreids[movieObj.genre_ids[0]];
      })
      temp = new Set(temp);
      setGenreList(["All Genres",...temp]);
    },[watchList])

    return( 
        <>
        <div className="flex justify-center flex-wrap m-4">
            {genreList.map((genre)=>{
              return <div key={genre} onClick={()=>hanldeFilter(genre)} className={
                currGenre == genre?"hover:cursor-pointer flex justify-center items-center w-[9rem] h-[3rem] rounded-xl bg-blue-400 m-4 text-white font-bold "
              :"hover:cursor-pointer flex justify-center items-center w-[9rem] h-[3rem] rounded-xl bg-gray-400/50 m-4 text-white font-bold "}>{genre}</div>
            })}
         </div>


         <div className="flex justify-center my-4">
            <input onChange={handleSearch} value={search} className="h-[3rem] w-[18rem]
             border-none outline-none bg-gray-200
             px-4 text-lg " type="text" placeholder="Search for Movies" />
        </div>


        <div className="overflow-hidden rounded-lg shadow-md border border-gray-200 m-8">
            <table className="w-full text-gray-500 text-center ">
                <thead className="bg-gray-50 text-gray-900 border-b-2">
                    <tr>
                        <th>Name</th>
                        <th className="flex">
                            <div onClick={sortIncreasing} className="p-2"><i className="fa-solid fa-arrow-up"></i></div>
                           <div className="p-2">Ratings</div>
                           <div onClick={sortDecreasing} className="p-2"><i className="fa-solid fa-arrow-down"></i></div> 
                        </th>
                        <th>Popularity</th>
                        <th>Genre</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody className="text-gray-700">
                {watchList.filter((obj)=>{
                  if(currGenre == "All Genres"){
                    return true;
                  }else{
                    return genreids[obj.genre_ids[0]] == currGenre;
                  }
                })
                .filter((movieObj)=>{
                  return movieObj.title.toLowerCase().includes(search.toLocaleLowerCase());
                })
                .map((movieObj)=>{
                    return   <tr className="border-b-2">
                        <td className="flex items-center px-6 py-4">
                            <img className="h-[6rem] w-[10rem]" src={`https://image.tmdb.org/t/p/original/${movieObj.poster_path}`} alt="" />
                            <div className="mx-4  ">{movieObj.title}</div>
                        </td>
                        <td>{movieObj.vote_average}</td>
                        <td>{movieObj.popularity}</td>
                        <td>{genreids[movieObj.genre_ids[0]]}</td>
                        <td onClick={()=>handleRemoveFromWatchList(movieObj)} className=" text-red-600">Delete</td>
                    </tr>
                })}
                </tbody>
            </table>
        </div>
        </>
    )
}

export default WatchList;
```


- **Pagination.jsx**:

  - This JavaScript file defines the `Pagination` component, which is responsible for rendering pagination controls for navigating between pages of trending movies on the IMDb web application.
  - The component function takes three props as arguments:
    - `pageNo`: The current page number, indicating the page of trending movies being displayed.
    - `handleNext`: A function to handle the next page button click event.
    - `handlePrev`: A function to handle the previous page button click event.
  - The component renders the following elements:
    - A `div` element with a set of CSS classes to style the pagination container. It is flex-based, horizontally centered, and has a background color of gray (#808080). This container holds the pagination controls.
    - Inside this container, there are three `div` elements representing the pagination controls:
      1. The first `div` contains a left arrow icon, which is likely a visual cue for users to go to the previous page of trending movies. It has padding (`px-8`) for spacing and a hover effect that changes the cursor to a pointer when hovered over. The `onClick` event handler is set to `handlePrev`, indicating that clicking this element will trigger the `handlePrev` function.
      2. The second `div` displays the current page number (`pageNo`). It is styled with a bold font weight for emphasis.
      3. The third `div` contains a right arrow icon, which serves as a control for users to navigate to the next page of trending movies. Similar to the left arrow, it has padding, a hover effect, and an `onClick` event handler set to `handleNext`.
  - The `Pagination` component provides a simple and intuitive way for users to move between pages of trending movies. It enhances the user experience by allowing them to explore a variety of movie options conveniently.

**Code**:

```javascript=
export default function Pagination({pageNo,handleNext,handlePrev}){

    return(
        <div className="flex justify-center p-4 mt-8 items-center bg-gray-400">
            <div onClick={handlePrev} className="px-8 hover:cursor-pointer "><i className="fa-solid fa-arrow-left"></i></div>
            <div className="px-8 font-bold hover:cursor-pointer">{pageNo}</div>
            <div onClick={handleNext} className="px-8 hover:cursor-pointer"><i className="fa-solid fa-arrow-right"></i></div>
        </div>
    )
}
```
