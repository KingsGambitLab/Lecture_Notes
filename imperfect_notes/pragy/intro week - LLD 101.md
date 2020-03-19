Intro Week - 4 - LLD 101
------------------------

Why LLD?
--------
- Must know for cracking any good tech company
- Don't miss out, because it will be a red flag in a design interview


What will we cover?
-------------------

- Basics & Fundas
- 10-12 days for LLD later on
- Essential Design Patterns - factory, consumer producer, etc
- Class Diagrams
- Object Oriented
- Design Patterns
- Different Paradigms


Contrast from what we usually do
--------------------------------

- All code in one file
    - some functions where all logic goes
- From top to bottom
- What paradigm is this?
    - procedural
- functional / declarative / event loop driven

Object Oriented
---------------

1. Split the code according to entities
1. For every entity that you can think of for your problem
    - create a separate blueprint
1. For each entity, think of
    - properties
    - attributes
1. Think of
    - functionalities
    - behavior
1. Think of relationships

```python
class Bird:
    weight: float
    height: float
    color: Color
    
    def fly(): ...
    def eat(): ...
```

**Note** that classes are blueprints
When you create an instance/snapshot of a class, you get an object

```java
new Bird()
Bird()
```

Constructor
-----------

```python
# python
class Bird:
    def __init__(self):
        pass
b = Bird()
```
```java
// java
class Bird {
    public Bird() {}
}

Bird b = new Bird();
```

Now,
- different birds can fly in different ways
- some birds don't even fly

Thus, our fly function must depend on the bird

```python
def fly(bird_type):
    if bird_type == 'hen':
        ...
    elif bird_type == 'kiwi':
        ...
    ...
```

**Issues:**

- Hard to read
- Hard to maintain
- Hard to test
- Hard to change

**Solution:**

- Abstract out the common things


Inheritance
-----------
Explain inheritance
- super class
- subclasses

```python
class Bird:
    def fly():
        // flap wings
        
class Eagle(Bird):
    ...

class Peacock(Bird):
    ...
```

Does this solve the problem?
- Not yet
- Need method overriding

```python
class Bird:
    def fly():
        # flap wings
        
class Eagle(Bird):
    @override
    def fly():
        ...

class Peacock(Bird):
    @override
    def fly():
        ...
```

**Issue:**
- No schema enforcement
    - I want every subclass to implement fly
    - some user can forget to implement the method
    - user won't get any warning/error

**Solutions:**
abstract classes / interfaces

Interfaces
----------

- Enforce implementations
- Issue: Code replication
- can't put common logic in an interface

Abstract Base Classes
---------------------

- Put common logic in parent class.
- Put specific logic in child classes.

-- --

Encapsulation
-------------

- don't want client to change my stuff
- private/protected .. access modifiers
- What if I still want to access stuff?
    - getter/setter

Abstraction vs Encapsulation
----------------------------

- Hiding details vs Hiding data

python doesn't have encapsulation

-- -- 

How will you
- Explain a 10k line code?
- design interviewbit?

UML diageram
Code -> IB -> TLE/Acc/Failed

Ignore asyncronous, other details


Ways to Explain
---------------

1. Structural explanation
    - classes
    - relations b/w classes
3. Behavioral explanation
    - non-tech guy can understand
        - what the system does
        - How things behave
    - use cases
        - responsibilities of system
    - not the responsibilities of system
        - as important as knowing the responsibilities


Use-Case vs Test-Case
---------------------

- Usecase
    - broader version of test case
    - Any person can understand a use case

**Example: Library management system**
- use case
    - search books
    - issue books
- test case
    - what if searched booked doesn't exist?
    - what if it has a unicode char
    - what if book already issued?


**Online shopping system**
- use cases
    - search product
        - by category
        - by name
    - add to cart
    - checkout cart
    - make payment


Draw System boundary
--------------------

Anything that is inside my use case. Everything outside, I don't care about

**Actors**
- customer


**Relations b/w use cases**
- when is a checkout successful? when the payment succeeds
- so, checkout usecase uses payment usecase
- similarly, search by category, and search by name, extend the search usecase

 ![6a92fd66.png](/users/pragyagarwal/Boostnote/attachments/a62e6867-75c8-4514-b15a-588945be52ad/6a92fd66.png =400x)
 
-- --

Example LLD Question
--------------------

- DS/Algo questions are deterministic problems
- LLD, HLD are open ended
- Questions are very short
- You need to ask lots of questions.

Design a Cofee Machine
----------------------

- first step?
    - start drawing?
    - start coding?
    - cry?
- Gather Requirements & Usecases
    1. Design a **coffee machine** which makes different **beverages** based on set **ingredients**.
    2. The initialization of the **recipes** for each drink should be hard-coded, although it should be relatively easy to add new drinks.
    3. The machine should display the ingredient **stock** (+cost) and **menu** upon startup, and after every piece of valid **user** input.
    4. Drink cost is determined by the combination of ingredients. For example, Coffee is 3 units of coffee (75 cents per), 1 unit of sugar (25 cents per), 1 unit of cream (25 cents per).
    5. Ingredients and Menu items should be printed in alphabetical order. If the drink is out of stock, it should print accordingly. If the drink is in stock, it should print "Dispensing: ".
    6. To select a drink, the user should input a relevant number. If they submit "r" or "R" the ingredients should restock, and "q" or "Q" should quit. Blank lines should be ignored, and invalid input should print an invalid input message.


Entities are nouns. Verbs are usually not entities

**Detected entities**
- beverage
- ingredient
- recipe
- stock
- menu
- user
- cofee-machine

**Identify relations**

Example
- beverage has a recepie
- recepie can have multiple ingredients
- stock has multiple ingredients
- menu has multiple beverages
- user has account - hidden requirement


- Think the rest of the entities and relations
- Give us a write up on the same
- Purpose
    - try
    - learn in LLD class
    - contrast with earlier submission

