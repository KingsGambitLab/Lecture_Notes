

Agenda:

* Add movies to the watchlist using local storage.
* Implement a feature to sort movies by ratings and popularity.
* Incorporate a feature to filter movies based on genre.
* Add functionality to delete movies from the watchlist.
* Integrate a search feature to find movies.



Setting Movies in Local Storage:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/502/original/Screenshot_2023-09-20_171911.png?1695210561)

> Note to instructor -  Help students understand and brainstorm this feature.


We are storing favorite movies in the watchList array, and now we will save them to local storage.

#### Pseudocode

```javascript=
// watchList handlers

const addToWatchList = (movie) => {
    const newWatchList = [...watchList, movie];
    setWatchList(newWatchList);
    localStorage.setItem('imdb', JSON.stringify(newWatchList))
}

```

> Note to instructor - Please feel free to test if everything is functioning correctly up to this point.

Next, we will retrieve the objects from local storage to display them in our watchlist. Here, we will retrieve all the items.


#### Pseudocode

```jsx=
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function WatchList() {
    const [favourites, setFavourites] = useState([]);
    
    useEffect(() => {
        (function () {
            let moviesFromLS = localStorage.getItem('imdb');
            moviesFromLS = JSON.parse(moviesFromLS) || [];
            setFavourites(moviesFromLS);
            
            axios
                .get('URL_HERE')
                .then((res) => {
                    setMovies(res.data.results);
                });
        })();
    }, [pageNum]);
    
    return (
        <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
            <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                <thead>  
                    <tr className="bg-gray-50">
                        <th className="px-6 py-4 font-medium text-gray-900">Name</th> 
                        <th>
                            <div className="flex">
                                <div>Ratings</div>
                            </div>
                        </th>
                        <th>
                            <div className="flex">
                                <div>Popularity</div>
                            </div>
                        </th>
                        <th>
                            <div className="flex">
                                <div>Genre</div>
                            </div>
                        </th>
                    </tr>
                </thead>
                <tbody className="divide-y divide-gray-100 border-t border-gray-100">  
                    {favourites.map((movie) => (
                        <tr className="hover:bg-gray-50" key={movie.id}>
                            <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                            </td>
                            <td className="pl-6 py-4">
                                {movie.vote_average}
                            </td>
                            <td className="pl-6 py-4">
                                {movie.popularity}
                            </td>
                            <td className="pl-2 py-4">
                                Action
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default WatchList;


```

This code manages a list of favorite movies (favourites) by first checking and retrieving any saved movies from local storage. It then makes an API request to fetch additional movie data based on a specified URL when the pageNum dependency changes. The retrieved movie data is stored in the favourites state variable, and the fetched movie results are stored in the movies state variable.



Now, let's delve into the "Remove from Watchlist" functionality.

#### Pseudocode

```javascript=
// watchList handlers

const removeFromWatchList = (movie) => {
    const filteredWatchList = watchList.filter((m) => {
        return m.id !== movie.id;
    });
    setWatchList(filteredWatchList);
    localStorage.setItem('imdb', JSON.stringify(filteredWatchList));
}

```
This removes a movie from the watchlist by filtering out the movie with a matching ID from the watchList state. The updated watchlist is then set in the state, and the modified list is stored in local storage under the key 'imdb' after converting it to a JSON string.

We will now modify this condition. If the movie is included in our watchlist, the code will be updated as follows:

#### Pseudocode

```jsx=
<div className="p-2 bg-gray-900 rounded-xl absolute right-2 top-2">
    {watchList.includes(movie) === false ? (
        <div onClick={() => addToWatchList(movie.id)}>
            😀
        </div>
    ) : (
        <div onClick={() => removeFromWatchList(movie.id)}>
            ❌
        </div>
    )}
</div>


```

This change allows for proper handling of adding and removing movies from the watchlist based on their presence in the watchList array.



We have successfully retrieved all movies from the watchlist component after storing them in local storage


To achieve this, we will create a new component and wrap the entire content within this fragment. This will allow us to structure the layout further with additional div elements as needed.

#### Pseudocode

```jsx=
function WatchList() {
    let movies = {
        // Some movie data here
    }
    
    let genreIds = {
        28: "Action",
        12: "Adventure",
        // Some data here
    }

    const [favourites, setFavourites] = useState([]);
    const [genres, setGenres] = useState([]);
    
    useEffect(() => {
        (function () {
            let moviesFromLS = localStorage.getItem('imdb');
            moviesFromLS = JSON.parse(moviesFromLS) || [];
            setFavourites(moviesFromLS);
            
            axios
                .get(
                    // URL_HERE
                )
                .then((res) => {
                    setMovies(res.data.results);
                });
        })();
    }, [pageNum]);

    // useEffect for genre
    useEffect(() => {
        let temp = movies.map((movie) => genreIds[movie.genre_ids[0]]);
        setGenres(["All genres", ...temp]);
    });
    
    return (
        <>
            <div className="mt-6 flex space-x-2 justify-center">
                {genres.map((genre) => {
                    return <div>{genre}</div>
                })}
            </div>
            <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
                <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                    <thead>  
                        <tr className="bg-gray-50">
                            <th className="px-6 py-4 font-medium text-gray-900">Name</th> 
                            <th>
                                <div className="flex">
                                    <div>Ratings</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Popularity</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Genre</div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100 border-t border-gray-100">  
                        {favourites.map((movie) => (
                            <tr className="hover:bg-gray-50" key={movie.id}>
                                <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                    <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                    <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                                </td>
                                <td className="pl-6 py-4">
                                    {movie.vote_average}
                                </td>
                                <td className="pl-6 py-4">
                                    {movie.popularity}
                                </td>
                                <td className="pl-2 py-4">
                                    Action
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default WatchList;

```

This is responsible for rendering a list of movie genres in the user interface. It first creates a div element to display the genres using the map function, and then it sets up a useEffect to populate the genres state variable. Inside the useEffect, it maps the genre IDs of movies to their corresponding genre names using the genreIds object and includes "All genres" as the first option. This enables users to filter movies by genre, and the genres are dynamically generated based on the movies in the movie array.

To update the genres, we will replace the static actions with the actual genre data.
#### Pseudocode
```jsx=
<td className="pl-2 py-4">
    Action
</td>   
```


#### Pseudocode

```jsx=
function WatchList() {
    let movies = {
        // some movie data here
    }

    let genreIds = {
        28: "Action",
        12: "Adventure"
        // some data here 
    }

    const [favourites, setFavourites] = useState([]);
    const [genres, setGenres] = useState([]);

    useEffect(() => {
        (function () {
            let moviesFromLS = localStorage.getItem('imdb');
            moviesFromLS = JSON.parse(moviesFromLS) || [];
            setFavourites(moviesFromLS);

            axios
                .get(
                    // URL here
                )
                .then((res) => {
                    setMovies(res.data.results);
                });
        })();
    }, [pageNum]);

    // useEffect for genres
    useEffect(() => {
        let temp = movies.map((movie) => genreIds[movie.genre_ids[0]]);
        setGenres(["All genres", ...temp]);
    });

    // Last class code
    return (
        <>
            <div className="mt-6 flex space-x-2 justify-center">
                {genres.map((genre) => {
                    return <div>{genre}</div>;
                })}
            </div>
            <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
                <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                    <thead>
                        <tr className="bg-gray-50">
                            <th className="px-6 py-4 font-medium text-gray-900">Name</th>
                            <th>
                                <div className="flex">
                                    <div>Ratings</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Popularity</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Genre</div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100 border-t border-gray-100">
                        {favourites.map((movie) => (
                            <tr className="hover:bg-gray-50" key={movie.id}>
                                <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                    <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                    <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                                </td>
                                <td className="pl-6 py-4">{movie.vote_average}</td>
                                <td className="pl-6 py-4">{movie.popularity}</td>
                                <td className="pl-2 py-4">{genreIds[movie.genre_ids[0]]}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default WatchList;


```





Now, we will proceed to add a feature that allows us to filter movies based on their genres. To implement this functionality, we will simply...


#### Pseudocode

```jsx=
function WatchList() {
    let movies = {
        // some movie data here
    }

    let genreIds = {
        28: "Action",
        12: "Adventure"
        // some data here 
    }

    const [favourites, setFavourites] = useState([]);
    const [genres, setGenres] = useState([]);
    const [currGenre, setCurrGenre] = useState("All Genres"); // Added current genre state

    useEffect(() => {
        (function () {
            let moviesFromLS = localStorage.getItem('imdb');
            moviesFromLS = JSON.parse(moviesFromLS) || [];
            setFavourites(moviesFromLS);

            axios
                .get(
                    // URL here
                )
                .then((res) => {
                    setMovies(res.data.results);
                });
        })();
    }, [pageNum]);

    // useEffect for genres
    useEffect(() => {
        let temp = movies.map((movie) => genreIds[movie.genre_ids[0]]);
        setGenres(["All Genres", ...temp]);
    });

    // Genre filter
    const filteredArray = currGenre === 'All Genres' ? favourites : favourites.filter((movie) => genreIds[movie.genre_ids[0]]);

    // Last class code
    return (
        <>
            <div className="mt-6 flex space-x-2 justify-center">
                {genres.map((genre) => {
                    return (
                        <div key={genre} onClick={() => setCurrGenre(genre)} className={currGenre === genre ? "bg-blue-200" : ""}>
                            {genre}
                        </div>
                    );
                })}
            </div>
            <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
                <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                    <thead>
                        <tr className="bg-gray-50">
                            <th className="px-6 py-4 font-medium text-gray-900">Name</th>
                            <th>
                                <div className="flex">
                                    <div>Ratings</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Popularity</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Genre</div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100 border-t border-gray-100">
                        {filteredArray.map((movie) => (
                            <tr className="hover:bg-gray-50" key={movie.id}>
                                <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                    <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                    <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                                </td>
                                <td className="pl-6 py-4">{movie.vote_average}</td>
                                <td className="pl-6 py-4">{movie.popularity}</td>
                                <td className="pl-2 py-4">{genreIds[movie.genre_ids[0]]}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default WatchList;


```
In this update, we introduced the currGenre state variable to track the currently selected genre for movie filtering. We created a section in the component that presents genres as clickable options. When a genre is selected, the currGenre state is updated accordingly.

Additionally, we introduced the filteredArray variable to facilitate movie filtering based on the chosen genre. If "All Genres" is selected, all movies from the favorites list are displayed. Otherwise, movies are filtered by their genre using the genreIds mapping.

Now, for each genre, let's generate a button.

#### Pseudocode

```jsx=
function WatchList() {
    let genreIds = {
        28: "Action",
        12: "Adventure"
        // some data here 
    }
    const [favourites, setFavourites] = useState([]);
    const [genres, setGenres] = useState([]);
    // state for filtering genres
    const [currGenre, setCurrGenre] = useState('All Genres')

    useEffect(() => {
        (function () {
            let moviesFromLS = localStorage.getItem('imdb')
            moviesFromLS = JSON.parse(moviesFromLS) || []
            setWatchList(moviesFromLS)

            axios
                .get(
                    // URL here
                )
                .then((res) => {
                    setMovies(res.data.results);
                });
        })();
    }, [pageNum]);

    // useEffect for genre
    useEffect(() => {
        let temp = movies.map((movie) => genreIds[movie.genre_ids[0]])
        setGenres(["All genres", ...temp])
    });

    // creating filter func acc to genre
    let filteredArray = []

    // genre filter 
    filteredArray = currGenre == 'All Genres' ? favourites : favourites.filter((movie) => genreIds[movie.genre_ids[0]])

    // last class code 
    return (
        <>
            <div className="mt-6 flex space-x-2 justify-center">
                {genres.map((genre) => {
                    return (
                        <button
                            className={currGenre == genre ? 'm-2 text-lg px-2 bg-blue-400 text-white rounded-xl font-bold' : 'm-2 text-lg px-2 bg-gray-400 text-white rounded-xl font-bold'}
                        >
                            {genre}
                        </button>
                    )
                })}
            </div>
            <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
                <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                    <thead>
                        <tr className="bg-gray-50">
                            <th className="px-6 py-4 font-medium text-gray-900">Name</th>
                            <th>
                                <div className="flex">
                                    <div>Ratings</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Popularity</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Genre</div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100 border-t border-gray-100">
                        {favourites.map((movie) => (
                            <tr className="hover:bg-gray-50" key={movie.id}>
                                <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                    <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                    <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                                </td>
                                <td className="pl-6 py-4">{movie.vote_average}</td>
                                <td className="pl-6 py-4">{movie.popularity}</td>
                                <td className="pl-2 py-4">{genreIds[movie.genre_ids[0]]}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default WatchList;




```



Now, we have the ability to alter genres by setting the genre upon clicking.


#### Pseudocode

```jsx=
function WatchList() {
        
    let genreIds = {

        28: "Action",
        12: "Adventure"
        // some data here 
    }
    const[favourites, setFavourites] = useState([])
    const[genres, setGenres] = useState([])
    // state for filtering genres
    const[currGenre, setCurrGenre] = useState('All Genres')
    
    useEffect(()=>{
        (function() {
            let moviesFromLS = localStorage,getItem('imdb')
            moviesFromLS = JSON.parse(moviesFromLS) || []
            setWatchList(moviesFromLS)
            
            axios
            .get(
            )
            .then((res) =>
                 {
                setMovies(res.data.results);
            });
        })();
    }, [pageNum]);
    
    
    // useEffect for genre
      useEffect(()=>{
          let temp = movies.map((movie) =>genreIds[movie.genre_ids[0]])
          setGenres(["All genres", ...temp])
    });
    
    // creating filter func acc to genre
    
    let filteredArray = []
    
    // genre filter 
    
    filteredArray = currGenre == 'All Genres' ? favourites : favourites.filter((movie) =>genreIds[movie.genre_ids[0]])
    
    
    // last class code 
    return (
        
        <>
        <div className = "mt-6 flex space-x-2 justify-center">
            {genres.map((genre)=>{
                return <button className = {currGenre == genre ? 'm-2 text-lg px-2 bg-blue-400 text-white rounded-xl font-bold' : 'm-2 text-lg px-2 bg-gray-400 text-white rounded-xl font-bold'}
                           
                           onClick={()=>{
                     setCurrGenre(genre)   
                    }}
                           
                           
                           >{genre}</button>
            })}
        </div>
        <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
            <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                <thead>  
                    <tr className="bg-gray-50">
                        <th className="px-6 py-4 font-medium text-gray-900">Name</th> 
                        <th>
                            <div className="flex">
                                <div>Ratings</div>
                            </div>
                        </th>
                        <th>
                            <div className="flex">
                                <div>Popularity</div>
                            </div>
                        </th>
                        <th>
                            <div className="flex">
                                <div>Genre</div>
                            </div>
                        </th>
                    </tr>
                </thead>
                <tbody className="divide-y divide-gray-100 border-t border-gray-100">  
                    // updated this to filteredArray as we are making changes in this array
                    {filteredArray.map((movie) => (
                        <tr className="hover:bg-gray-50" key={movie.id}>
                            <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                            </td>
                            <td className="pl-6 py-4">
                                {movie.vote_average}
                            </td>
                            <td className="pl-6 py-4">
                                {movie.popularity}
                            </td>
                            <td className="pl-2 py-4">
                               {genreIds[movie.genre_ids[0]]}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
        </>
    );
}

export default WatchList;

```






To understand sorting, think of it as arranging data in a specific order, which can be either ascending or descending. We will use JavaScript's sort method to achieve this.

First, we'll create a state variable to manage the sorting.

#### Pseudocode

```jsx=
function WatchList() {
    let genreIds = {
        28: "Action",
        12: "Adventure"
        // some data here 
    }
    const [favourites, setFavourites] = useState([])
    const [genres, setGenres] = useState([])
    // state for filtering genres
    const [currGenre, setCurrGenre] = useState('All Genres')
    // state for sorting by rating 
    const [rating, setRating] = useState(0)

    useEffect(() => {
        (function () {
            let moviesFromLS = localStorage.getItem('imdb')
            moviesFromLS = JSON.parse(moviesFromLS) || []
            setWatchList(moviesFromLS)

            axios
                .get(
                )
                .then((res) => {
                    setMovies(res.data.results);
                });
        })();
    }, [pageNum]);

    // useEffect for genre
    useEffect(() => {
        let temp = movies.map((movie) => genreIds[movie.genre_ids[0]])
        setGenres(["All genres", ...temp])
    });

    // creating filter func acc to genre
    let filteredArray = []

    // genre filter 
    filteredArray = currGenre === 'All Genres' ? favourites : favourites.filter((movie) => genreIds[movie.genre_ids[0]])

    // condition for sorting of movies with respect to ratings
    if (rating === -1) {
        filteredArray = filteredArray.sort(function (objA, objB) {
            return objB.vote_average - objA.vote_average
        })
    }

    if (rating === 1) {
        filteredArray = filteredArray.sort(function (objA, objB) {
            return objA.vote_average - objB.vote_average
        })
    }

    // last class code 
    return (
        <>
            <div className="mt-6 flex space-x-2 justify-center">
                {genres.map((genre) => {
                    return <button className={currGenre === genre ? 'm-2 text-lg px-2 bg-blue-400 text-white rounded-xl font-bold' : 'm-2 text-lg px-2 bg-gray-400 text-white rounded-xl font-bold'}
                        onClick={() => {
                            setCurrGenre(genre)
                        }}>{genre}</button>
                })}
            </div>
            <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
                <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                    <thead>
                        <tr className="bg-gray-50">
                            <th className="px-6 py-4 font-medium text-gray-900">Name</th>
                            <th>
                                <div className="flex">
                                    {/* image showing arrow for up rating */}
                                    <img src=""
                                        onClick={() => {
                                            setRating(1)
                                        }}
                                    />
                                    <div>Ratings</div>
                                    {/* image showing arrow for down rating */}
                                    <img src=""
                                        onClick={() => {
                                            setRating(-1)
                                        }}
                                    />
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Popularity</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Genre</div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100 border-t border-gray-100">
                        {/* updated this to filteredArray as we are making changes in this array */}
                        {filteredArray.map((movie) => (
                            <tr className="hover:bg-gray-50" key={movie.id}>
                                <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                    <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                    <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                                </td>
                                <td className="pl-6 py-4">
                                    {movie.vote_average}
                                </td>
                                <td className="pl-6 py-4">
                                    {movie.popularity}
                                </td>
                                <td className="pl-2 py-4">
                                    {genreIds[movie.genre_ids[0]]}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default WatchList;

```

The provided code segment handles the sorting of movies based on ratings. It uses a rating state variable to determine the sorting order. If rating is set to -1, it sorts the filteredArray of movies in descending order of ratings (highest to lowest). If rating is set to 1, it sorts the filteredArray in ascending order of ratings (lowest to highest). This functionality allows users to toggle between sorting movies by ratings in both ascending and descending orders.








Now, moving forward to implement the delete functionality.


#### Pseudocode

```jsx=
function WatchList() {
    const genreIds = {
        28: "Action",
        12: "Adventure"
        // some data here 
    };

    const [favourites, setFavourites] = useState([]);
    const [genres, setGenres] = useState([]);
    // state for filtering genres
    const [currGenre, setCurrGenre] = useState('All Genres');
    // state for sorting by rating 
    const [rating, setRating] = useState(0);

    useEffect(() => {
        (function () {
            let moviesFromLS = localStorage.getItem('imdb');
            moviesFromLS = JSON.parse(moviesFromLS) || [];
            setFavourites(moviesFromLS);

            axios
                .get(
                    // URL here
                )
                .then((res) => {
                    setMovies(res.data.results);
                });
        })();
    }, [pageNum]);

    // useEffect for genre
    useEffect(() => {
        let temp = movies.map((movie) => genreIds[movie.genre_ids[0]]);
        setGenres(["All genres", ...temp]);
    });

    // creating filter func acc to genre
    let filteredArray = [];

    // genre filter 
    filteredArray = currGenre === 'All Genres' ? favourites : favourites.filter((movie) => genreIds[movie.genre_ids[0]]);

    // condition for sorting movies according to rating
    if (rating === -1) {
        filteredArray = filteredArray.sort(function (objA, objB) {
            return objB.vote_average - objA.vote_average;
        });
    }

    if (rating === 1) {
        filteredArray = filteredArray.sort(function (objA, objB) {
            return objA.vote_average - objB.vote_average;
        });
    }

    // delete functionality
    const del = (movie) => {
        let newArray = favourites.filter((m) => m.id !== movie.id);
        setFavourites([...newArray]);
        localStorage.setItem('imdb', JSON.stringify(newArray));
    };

    // last class code 
    return (
        <>
            <div className="mt-6 flex space-x-2 justify-center">
                {genres.map((genre) => (
                    <button className={currGenre === genre ? 'm-2 text-lg px-2 bg-blue-400 text-white rounded-xl font-bold' : 'm-2 text-lg px-2 bg-gray-400 text-white rounded-xl font-bold'}
                        onClick={() => {
                            setCurrGenre(genre);
                        }}>
                        {genre}
                    </button>
                ))}
            </div>
            <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
                <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                    <thead>
                        <tr className="bg-gray-50">
                            <th className="px-6 py-4 font-medium text-gray-900">Name</th>
                            <th>
                                <div className="flex">
                                    {/* image showing arrow for up rating */}
                                    <img
                                        src=""
                                        onClick={() => {
                                            setRating(1);
                                        }}
                                    />
                                    <div>Ratings</div>
                                    {/* image showing arrow for down rating */}
                                    <img
                                        src=""
                                        onClick={() => {
                                            setRating(-1);
                                        }}
                                    />
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Popularity</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Genre</div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100 border-t border-gray-100">
                        {/* updated this to filteredArray as we are making changes in this array */}
                        {filteredArray.map((movie) => (
                            <tr className="hover:bg-gray-50" key={movie.id}>
                                <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                    <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                    <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                                </td>
                                <td className="pl-6 py-4">{movie.vote_average}</td>
                                <td className="pl-6 py-4">{movie.popularity}</td>
                                <td className="pl-2 py-4">{genreIds[movie.genre_ids[0]]}</td>
                                {/* adding delete button */}
                                <td className="pl-2 py-4">
                                    <button className="text-red-600" onClick={() => del(movie)}>Delete</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default WatchList;


```

The code now includes a delete functionality that allows you to remove movies from the watchlist. The del function filters the movies and updates the state and local storage accordingly.






#### Pseudocode

```jsx=
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function WatchList() {
    // Define genre IDs
    let genreIds = {
        28: "Action",
        12: "Adventure"
        // Add more genre data here
    }

    // State for favorites, genres, selected genre, rating, and search string
    const [favourites, setFavourites] = useState([]);
    const [genres, setGenres] = useState([]);
    const [currGenre, setCurrGenre] = useState('All Genres');
    const [rating, setRating] = useState(0);
    const [searchStr, setSearchStr] = useState('');

    useEffect(() => {
        // Fetch movie data from local storage and API
        (function () {
            let moviesFromLS = localStorage.getItem('imdb');
            moviesFromLS = JSON.parse(moviesFromLS) || [];
            setFavourites(moviesFromLS);

            axios.get(
                // Add API URL here
            ).then((res) => {
                setMovies(res.data.results);
            });
        })();
    }, [pageNum]);

    // useEffect for genre
    useEffect(() => {
        let temp = movies.map((movie) => genreIds[movie.genre_ids[0]]);
        setGenres(["All genres", ...temp]);
    });

    // Create filter function according to genre
    let filteredArray = [];

    // Genre filter
    filteredArray = currGenre === 'All Genres' ? favourites : favourites.filter((movie) => genreIds[movie.genre_ids[0]]);

    // Condition for sorting movies according to rating
    if (rating === -1) {
        filteredArray = filteredArray.sort(function (objA, objB) {
            return objB.vote_average - objA.vote_average;
        });
    }

    if (rating === 1) {
        filteredArray = filteredArray.sort(function (objA, objB) {
            return objA.vote_average - objB.vote_average;
        });
    }

    // Movies searching functionality
    filteredArray = filteredArray.filter((movie) => {
        return movie.title.toLowerCase().includes(searchStr.toLowerCase());
    });

    // Delete functionality
    const del = (movie) => {
        let newArray = favourites.filter((m) => m.id !== movie.id);
        setFavourites([...newArray]);
        localStorage.setItem('imdb', JSON.stringify(newArray));
    }

    // Return the JSX for the WatchList component
    return (
        <>
            <div className="mt-6 flex space-x-2 justify-center">
                {genres.map((genre) => {
                    return (
                        <button
                            key={genre}
                            className={currGenre === genre ? 'm-2 text-lg px-2 bg-blue-400 text-white rounded-xl font-bold' : 'm-2 text-lg px-2 bg-gray-400 text-white rounded-xl font-bold'}
                            onClick={() => {
                                setCurrGenre(genre);
                            }}
                        >
                            {genre}
                        </button>
                    );
                })}
            </div>

            {/* Input field for movie search */}
            <div className="text-center">
                <input
                    type="text"
                    className="border bg-gray-200 border-4 text-center p-1 m-2"
                    placeholder="Search For Movies"
                    value={searchStr}
                    onChange={(e) => setSearchStr(e.target.value)}
                />
            </div>

            <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
                <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
                    <thead>
                        <tr className="bg-gray-50">
                            <th className="px-6 py-4 font-medium text-gray-900">Name</th>
                            <th>
                                <div className="flex">
                                    {/* Image showing arrow for up rating */}
                                    <img
                                        src=""
                                        onClick={() => {
                                            setRating(1);
                                        }}
                                    />
                                    <div>Ratings</div>
                                    {/* Image showing arrow for down rating */}
                                    <img
                                        src=""
                                        onClick={() => {
                                            setRating(-1);
                                        }}
                                    />
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Popularity</div>
                                </div>
                            </th>
                            <th>
                                <div className="flex">
                                    <div>Genre</div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100 border-t border-gray-100">
                        {filteredArray.map((movie) => (
                            <tr className="hover:bg-gray-50" key={movie.id}>
                                <td className="flex items-center px-6 py-4 font-normal text-gray-900">
                                    <img className="h-[6rem] w-[10rem] object-fit" src="" alt="" />
                                    <div className="font-medium text-gray-700 text-sm">{movie.title}</div>
                                </td>
                                <td className="pl-6 py-4">
                                    {movie.vote_average}
                                </td>
                                <td className="pl-6 py-4">
                                    {movie.popularity}
                                </td>
                                <td className="pl-2 py-4">
                                    {genreIds[movie.genre_ids[0]]}
                                </td>
                                {/* Adding delete button */}
                                <td className="pl-2 py-4">
                                    <button className="text-red-600" onClick={() => del(movie)}>Delete</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default WatchList;

```

A new state variable, searchStr, is introduced using useState to hold the user's search string. The movie searching functionality is implemented by further filtering the filteredArray based on searchStr. It utilizes the filter method to match the lowercase movie titles with the lowercase search string, effectively enabling movie searches. An input field is added to the component, allowing users to input their search query, with the value bound to searchStr and an onChange handler to update it based on user input.


