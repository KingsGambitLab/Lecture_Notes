LLD 3
-----

Factory Pattern
---------------

1. Trying to validate address
    ```java
    class Address {
        String country, state, city, []addressLines, zip;
    }
    ```
1. Algorithm for validating address will differ  from country to country.
1. Different countries have different breakups.
    - Some countries don't have states
    - Japan has provinces
    - Some European countries have counties
    - Meaning of state could be different

    - Could have different ways of writing the addresses
    - US addresses are more structured
    - Indian addresses have lots of different ways - c/o xyz
    - Chinese people write addresses in Chinese
1. So, different classes for each country
    ```java
    public class INValidator {
        public bool validate(Address a) {}
    }

    public class USValidator {
        public bool validate(Address a) {}
    }
    ```

    Now, let's say that I ship these validators as a library
    Some client wants to use these validators to validate a random address

    ```java
    public class ClientValidator {
        public bool validate(Address a) {
            if(a.country == 'India')
                return new INValidator().validate(a);
            else if(a.country == 'USA')
                return new USValidator().validate(a);
            ...
        }
    }
    ```
1. **Is this good?**
    - client needs to know the name of the class for each country
    - difficult to test
    - unknown country - Indonesia. Does a class exist for it?
    - IN stands for India or Indonesia?
        - could lead to correct addresses being invalidated or wrong addresses be accepted
1. **Pull into interface**
    - ![24debe26.png](:storage/e65b85d8-61b9-4991-b67d-d0c285e92bb4/24debe26.png =300x)
    - all these classes are multiple forms of the same thing
    - interface `Validator`, which asks to implement method `valdiate`
    - coding your classes against an interface
1. **Runtime polymorphism**: `Validator v = new INValidator();`
1. **Who should worry about the mapping from country name to Validator?**
    - client should not
    - I should
    - Keep a map
1. Need to create a class whose responsibility is to keep this mapping
    ```java
    class X {
        // why private? don't allow client to change this
        private static Map<String, Validator> validators;
        
        public X() {
            validators.put("USA", USValidator);
            validators.put("USA", INValidator);
        }
        
        public Validator getValidator(String country) {
            // return validators.get(country); - bad
            // could lead to null pointer exception
            if(validators.has(country))
                return validators.get(country);
            
            throw new InvalidCountryException();
        }
    }
    ```
1. Too many objects being created in the constructor. Will be used many times. Use Singleton Pattern.
    - make constructor private
    - create an instance variable
    - expose a getinstance function
1. Client code
    ```java
    public class ClientValidator {
        public bool validate(Address a) {
            return X.getInstance(
                    .getValidator(a.country)
                    .validate(a);
        }
    }
    ```
1. Client just knows about the interface Validator, and that there's a factory which gives you different implementations of the Validators.
1. Factory Design Pattern
1. Rename X to ValidatorFactory
1. Remember that factories should usually be singleton
1. Notice that we use a pattern that we've already used
1. Usecases - 

Gotchas
- don't use this in any language
- Python has dispathcing libraries
- Strategy pattern
- Don't abstract too much
- unless you're a library author

-- --

Stackoverflow
-------------

- Interviewer asks you to implement Stackoverflow
- First step? Start coding?
- **Use Cases**
    - Anyone can search and view questions
    - Question, answers, comments
    - Guest can only search. To add/vote you need to be a member
    - Each question can have an active bounty
    - Text can contain photos
    - User can earn badges
    - Admin can blcok users
    - Moderator can close questions
- Identify entities - will become classes
- Identify attributes and behavior
- Identify relationships
- ![5d93c037.png](:storage/e65b85d8-61b9-4991-b67d-d0c285e92bb4/5d93c037.png =500x)
    ```python
    class Question:
        status: Enum
        title: str
        description: str
        votes: int

        def close(): pass

    class Comment:
        content: stre
        votes: int

    class Answer:
        content: str
        votes: int
        accepted: bool
    ```
-  ![Screenshot 2019-10-09 at 8.48.21 PM.png](:storage/e65b85d8-61b9-4991-b67d-d0c285e92bb4/0b1d9eeb.png =500x)
    ```python
    class Bounty:
        prize: int
        expiry: DateTime

        def claim(): pass

    class Photo:
        alt_text: str
        url: str
    ```
- Note where we have composition or not
    ![f2f50632.png](:storage/e65b85d8-61b9-4991-b67d-d0c285e92bb4/f2f50632.png =600x)
    ```python
    class Member:
        age: int
        sex: str
        def create_question(): pass
    
    class Moderator(Member):
        def close_question(): pass
    
    class Admin(Member):
        def block_member(): pass
    ```  
- **Direction of arrows.** Member -> Question = Member has instance of Question
- **Composition vs Association**
- ![741698f7.png](:storage/e65b85d8-61b9-4991-b67d-d0c285e92bb4/741698f7.png =400x)
    ```python
    class Account:
        password: str
        creation_date: DateTime
        
        def delete_account(): pass
    ```
- Badge
    - badges are static
    - same badge, multiple people can own
    - same person can own multiple badges
    - not composition, because deleting either doesn't delete the other
    ```python
    class Badge:
        text: str
    ```
- Search interface
- Guest account - doesn't extend member
- Guest uses search
- ![7b76882f.png](:storage/e65b85d8-61b9-4991-b67d-d0c285e92bb4/7b76882f.png =400x)



Movie Ticket Booking
--------------------

- bookmyticket
- list all the centers of halls - **PVR** (brand), etc
- each **cinema center** can have multiple **halls / audis**
- movie vs movie show (cost, etc)
- hall can run some movie at some time
- each movie can have multiple shows
- search by title, language
- show seating arrangement
- show list of reserved and available seats
- difference b/w the physical chair vs a seat
- pay via cash/card
- no two customers should have the same seat
- discount coupons