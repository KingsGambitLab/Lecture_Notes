LLD 5
-----

- some have still not submitted the BookMyShow diagram
- So postpone it to next class
- For now, BookMyShow


Hotel Management System
-----------------------

- support booking different room types
    - suite
    - king size
    - delux
    - **Entities:**
        - booking
        - room
    - **Relations:**
        - booking-room
        - room-subclass
- search and book rooms for a guest
    - **Entities:**
        - search interface
        - guest
    - who else can use search? We can not only book rooms online. People also visit the frontdesk and book rooms
    - **Relationships**
        - guest uses search interface
        - Receptionist
- Who booked a particular room, say 1004
    - **Relation:**
        - room booking has multiple guests
        - one guest can only bok one room
- cancel a booking
    - behavior. no new entity / relation here
- track housekeeping tasks
    - **Entities:**
        - housekeeing task
        - housekeeper
    - **Relation:**
        - housekeeper can perform * tasks
- customer can ask for room service
    - room service is different from house keeping
    - don't have to pay for housekeeping
    - have to pay for roomservice
    - order food/drinks in roomservice
    - **Entities:**
        - room service
- payment should be supported through various modes
    - card
    - cash

-- --

How should we start?
- from building
- from brand

```python
class HotelBranch:
    name: str
    
    def get_number_of_centers():
    def add_location():
    
class HotelCenter: # actual physical building
    location: Address
    name: str
    
    def get_rooms():
```

HotelBrand  1 <>----- * HotelBranch

```python
class Room:
    room_number: str
    room_type: str  # or subclass
    price: float
    is_booked: bool
    
    def check_in():
    def check_out():
```
HotelCenter 1 <>----- * Room

-- --

How will you get into your room?
Do you need something?
Each room can have multiple keys, right?

```python
class RoomKey:
    id: str
    barcode: str
    issued_at_date: Date
    is_active: bool
```

Room 1 <>----- * Key

-- --

Humans
- guest
- receptionist
- housekeeper
- manager


```python
class Person:
    name: str
    phone_number: str
    email_id: str

class Guest(Person):
    def create_booking():

class Receptionist(Person):
    def create_booking():
    
class Housekeeper(Person): # or servant. Or differnt subclasses of servant - cleaner / food server / masseur
    def add_service_charge(): # for services they offer
    # no def create_booking()
```

Person <--- ext --- Guest
Person <--- ext --- Receptionist
Person <--- ext --- Housekeeper

-- --

How do you track / manage these people?
Account

```python
class Account:
    name: str
    email: str
    password: str
```

Person 1 <>------ 1 Account

-- --

How do you track of your sales?
Booking

What is it that you book? Brand/Hotel/Room?
Room

```python
class Booking:
    booking_number: str
    start_time: DateTime
    end_time: DateTime
    status: successfull / failed
    
    def modify():
    def cancel():
```

Can there be multiple bookings for a particular room?
- Yes, for different times. All bookings can exist simultaneously


Room 1 ---- * Booking
- Composition or Association?
- If room goes bad - leaking / haunted / something not working
- Would you cancel my booking? No - reassign to a room of the same type
- Association
Room ---> Booking


Booking * ------> 1 Guest

Does not need to be composition, because room can be booked for a friend. Could be though depending on the case

-- --

What does a housekeeper do?
- various housekeeping tasks

```python
class HouseKeepingTask:  # or record
    description: str
    start_time: DateTime
    duration: Time 
```

HouseKeeper 1 -----> * HouseKeepingTask

Not a composition

HouseKeepingTask * <------ Room
Same room could have multiple tasks that were/need to be done

What if room is destroyed? Should destroy previous tasks?
- no
- but what about foriegn keys?
- keep a note in room saying invalid or something
- depends on requirements
- We will discuss DB schema design later in LLD

-- --

RoomService (not the same as housekeeping)

```python
class FoodService:
    
class MassageService:
```

HouseKeeper 1 ------- * Service

-- --

Now, each service will need some payment.
Invoice

```python
class InvoiceItem:
    amount: float
    time: DateTime
```

InvoiceItem  1 ------- 1 Service
Each instance of service associated with each instance of invoiceitem
Or we could make Service objects static
Then, Invoice * ------ 1 Service

InvoiceItem * ------ RoomBooking
Same room can request multiple services

-- --

All invoiceitems associated with an invoice

```python
class Invoice:
    
```

Do you always charge money all the time? No. at the end
RoomBooking 1 -------> 1 Invoice

InvoiceItem * ------<> 1 Invoice

-- --

Searching

```python
<<interface>> Search:
    search_by_room_type()
    search_by_floor()
```

have catalogues of rooms and mapping that we need
Who can use this?
Receptionist

**Why is search an interface?**
Because search can be done on various things - users, rooms, tasks ..
So, the common functionality of search is an interface. Then there are several modules that implement that interface

-- --

going forward, we will look at DB schema design for things like this

-- --

