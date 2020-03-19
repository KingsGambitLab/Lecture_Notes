LLD 1
-----

- **What is the Lowest Level?**
    - Code
    - Not feasible to communicate at this level
    - Large systems can have hundreds of thousands of LOC
- if the interviewer asks you to design amazon, he doesn't expect you to write code. He first expects the HLD/LLD
- **High Level Design**
    - very high level view
    - still allows you to see that there are some components and the way things operate
- **Low level design**
    - closer look, but still higher than code.
    - behavior / skeleton, not implementation

-- --

Example
-------

Website - webpage, application code, DB
Fetch data, persist

**HLD**
- ![186867fa.png](:storage/f62e8f9f-4c32-453b-95d6-8e01da320ef2/186867fa.png =400x)
- doesn't worry about how the data is fetched, what the DB schema is, what tables exist, what the tech stack is


**LLD**

- not the actual code. Higher level than code
- Consider a function that adds two numbers
    ```python
        def add(a: int, b: int) -> int: ...
    ```
    LLD just tells you that the function takes 2 args and returns the sum. Doesn't bother about the actual implementation
- LLD talks about entities (classes), their interactions, and their properties (attributes) and behavior (functions)

-- --

**Procedural Code**
- top-down
- no obvious segregation of responsibility
- no one-to-one mapping to real world entities

**Object Oriented**
- map any real world entity to a code entity (class)
- list down the properties/attributes of each entity
- list down the actions/behavior/methods of each entity
- list down the interactions b/w various entities

-- --

Example:

Template / Blueprint for a Bird
-------------------------------

```python
class Bird:
    weight: float
    height: float
    color: Color
    
    def fly(): ...
```

This template does not signify one particular bird. It describes a class of a Bird.
A specific bird will be represented by an instance of this class.

-- --

Constructing an instance / object
---------------------------------

- invoke the constructor of the class
- 
- ```python

```