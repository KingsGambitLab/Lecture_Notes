LLD 6
-----

BookMyShow
----------

```python
class CinemaBrand:
    name: str

class CinemaCenter:
    address: str

'Brand 1 <>---- * Center'

class CinemaHall:
    hall_number: int
    number_of_seats: int
    
'Center 1 <>---- * Hall'

# show seat is different from phycial Hall seat
class HallSeat:
    location: Location
    type: str # delux / normal / ..
    # can you book a physical seat?
    # note: don't have the price of chair here
    # note: don't have is_reserved here

'Hall 1 <>---- * HallSeat'
    
class Movie:
    name: str
    director: str
    description: str
    language: str
    
class Show:
    created_on: Date
    start_time: Time
    end_time: Time
    
'Movie 1 <>----- * Show'
'Hall 1 ---- * Show'

class Booking:
    number: str
    number_of_seats: int
    
    def cancel():

'Booking * ----<> 1 Show'

class ShowSeat:
    seat_number: int
    is_reserved: bool

'Booking 1 ----- * ShowSeat'
'HallSeat 1 <>----- * ShowSeat'
'Show 1 <>---- * ShowSeat '  # can have. not strictly needed. Depends on usecase


class Payment:
    amount: float
    trans_id: str

class Coupon:
    id: int
    amount: float
    expiry: Date
    
'Payment 1 ----- 0-1 Coupon'
'Payment 1 ----- Booking'
    
class Cash(Payment):
class Card(Payment):
'''
Cash <--ext-- Payment
Card <--ext-- Payment
'''

# first show without inheritance
    
class Customer(Person):
    make_booking()

'Customer 1 ----> Booking'

class Admin(Person):
    add_movie()
    add_show()
    block_show()

'Admin 1 ---- * Show'
'Admin 1 ---- * Movie'

class FrontDesk(Person):
'FrontDesk 1 ---> * Booking'

class Person:
    name: str
    address: str
    email: str
    
'''
FrontDesk <--ext-- Person
Admin <--ext-- Person
Customer <--ext-- Person
'''

class Account:
    id
    password

'Account 1 ----<> 1 Person'

class Guest:
    # note: doesn't extend person
    register()

<<interface>> interface Search:
    by_name()
    by_language()
    
'Person ---uses--> search'
'Guest ---uses--> search'

class Catalogue <implements> Search:
    movie_titles: {name -> list of movies}
    language_titles: {lang -> list of movies}
    by_name()
    by_language()
```

-- --

Schema Design
-------------


- store everything in one table
- yay \o/
- is this good design?
why store into multiple tables?
-------------------------------

Anomalies:
- college name, rank. Student name. Branch.
- **insert anomaly:** null values when data is not known
- **delete anomaly:** deleting a student causes loss of info about a particular college's rank
- **update anomaly:** updating the rank of a college needs updation of thousands of rows


- Map each entity to a table
    - Attributes of entity become the columns of the table
    - Define a primary key (could be a single column or a group of column)
- Create a table for each relationship
    - Think about if the relationship needs to have some properties or not:
        - entities: students, course
        - relationship: enrolled
        - relationship attributes: enrollment date, marks, type (elective/audit/core)
        - add these attribs to the relationship table
    - The primary key of the relationship table will be the group of primary key of each of the participants in the relationship. (ex, (user_id, course_id))
    - Create foreign key constraints: user_id, course_id


Normalizations
--------------

- 1NF: data should be atomic. Don't store lists of things. Instead, make multiple rows.
    - example: languages a student knows.
    - now, I need to decide an id, because the previous id might not be able to identify a unique column
- 2NF, 3NF, BCNF: we won't go over them. More in DBMS class
    - follow logical thinking, and you will automatically get proper normalization

Over Normalization?
-------------------

- n+1 problem
- need to join the tables to get back the data anyway


-- --

- How to do composition in DB?
    - depends. Cascading deleted turned on or not?
    - depends on the DB. Different DBs require different things
        - some will automatically delete references for you
        - some will not
    - safe way: setup your DB to not do it automatically. Do it yourself in code
        - delete references first
        - then delete row
- How to do auto increment in DB?
- null / unique / primary / foreign
    ```sql
    CREATE TABLE Persons (
    ID int NOT NULL AUTO_INCREMENT,
    UNIQUE (ID),
    PRIMARY KEY (ID)
    );
    
    CREATE TABLE Objects (
    ID int NOT NULL AUTO_INCREMENT,
    UNIQUE(ID),
    PRIMARY KEY(ID)
    );
    
    CREATE TABLE PersonObjects (
        PersonID int,
        ObjectID int,
        FOREIGN KEY (PersonID) REFERENCES Persons(ID),
        FOREIGN KEY (ObjectID) REFERENCES Objects(ID),
        PRIMARY KEY (PersonID, ObjectID)
    )

    ```
    

How to do extension? Just create another table
Usually not enforced in DB

