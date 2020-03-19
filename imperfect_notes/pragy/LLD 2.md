LLD 2
-----


- Do you understand what a class is?
- Why we use OOP
- What an object is?
    - an instance of a class.
    - a physical entity that has some snapshot of the values of the attributes of the class

-- --
Builder Pattern
---------------

1.
    ```java
    class Bird {
        String color
        public Bird(String color) {
            this.color = color;
        }
    }

    Bird b = new Bird(); // how to create an object
    Bird b = new Bird("green"); // how to set attributes initially
    ```
    
1. **Now let's say that we wanted to add attributes to the class**
    ```java
    int height, weight;
    ```
    
1. **Do we need to change the way we're invoking the constructor?** Because we now want to pass the height and weight too?
    
    ```java
    public Bird(String color, int height, int weight) {}
    ```
    
1. **Now let's say we wanted to add 10 more attributes.** What change would you have to do?
    
1. Use a longer constructor.
    
1. **Is that a good idea? What can do wrong with that?**
    - constuctor becomes huge
    - increases complexity, hence increases errors. Might confuse the order of variables. Might forget to pass some. Might pass incorrect values.
    - So, never write a function that takes in so many parameters.
    
1. **There is an even bigger problem. Identify?**
    Backwards compatibility. Existing  code breaks!
    Explain how with example.
    
1. **Solution 1**:
    - Have multiple constructors
    - constructor overloading
    - old code continues to use old constructor. New code uses new constructor
    
1. **Issue?**
    Can't choose which attribute to set. Must set all attributes.
    
1. **Bad Solution 1**
    - Make constructor for every possible combination
    - how many constructors? $2^n$
    - Adding any attribute is a nightmare
    
1. **Bad solution 2**
    - pass an object
        ```java
        public Bird(Attributes obj) {
            this.weight = obj.weight;
            ...
        }
        ```
    - same problem now repeated for obj
    - So, doesn't help
    
1. Builder Pattern
    ```java
    public class Bird {
        int height, weight;
        String color;
        
        // set to private to enforce builder
        public Bird(Builder builder) {
            // same as bad solution 2, but Builder is special
            this.height = builder.height;
            this.weight = builder.weight;
            this.color = builder.color;
        }
        
        // -------------------- Builder --------------------
        // explain why static
        public static class Builder {
            int height, weight;
            String color;
            public Builder(); // don't pass values in constructor
            public Builder setHeight(int height) {
                this.height = height;
                return this; // explain the return type
            }
            public Builder setWidth(int width) {
                this.width = width;
                return this;
            }
            public Builder setColor(String color) {
                this.color = color;
                return this;
            }
            public Bird build() {
                // because we need an instance of Bird
                // and not an instance of Builder
                Bird b = new Bird(this);
                return b;
            }
        }
        // --------------------------------------------------
    }
    
    Bird b = new Bird.Builder()
                     .setHeight(10)
                     .setColor("red")
                     // can skip some variable - weight
                     .build();
    ```
1. Client can now initialize Bird in whatever order, using whatever attributes they want.
1. **What if we now wanted to add an attribute?**
1. Simply put the attribute in class and Builder. Add one line in contructor. Add one method in Builder
1. **Benefits:**
    - Simpler to use
    - Backwards Compatible
1. This is in Java, C++. Languages like Python have something else.
1. How to now enforce some attribute?
1. Put it in the builder constructor
    ```java
    public Builder(int height) {
        this.height = height;
    }
    ```
    Client can still change the height later.
1. How to enforce Builder? make Bird constructor private
1. This is called Builder Pattern.
1. Useful for classes with lots of attributes, and whose attribute requirements can be changed.

-- --

Stateful vs Stateless
---------------------

```java
// Stateful
public class Adder {
    int a;
    int b;
    public int add() {
        return this.a + this.b;
    }
}

Adder a = new Adder(5, 6);
int result = a.add();

// Stateless  - draw on RHS
public class Adder {
    public static int add(int a, int b) {
        return a + b;
    }
}

int result = Adder.add(5, 6);
```

- What is better? Stateful or Stateless? todo: -50
- Math.max, System.out - stateless

-- --

Address Validation
------------------

- useful in lots of companies, especially ecommerce sites like amazon
- if while placing an order, if you put the city as Mumbai but the pin as Delhi, will it accept? Should it accept?
- why important - must validate the address before the order is shipped

```java
class Address {
    addressLines;
    city;
    state;
    zip;
}
```

- algorithm to validate the address lines would be much different from the one which validates the zip
- zip is only a few chars. Address line can be huge
- Different Class for each.
    - Because can have multiple logic depending on country / state
    - namespace
- component level validators:
    - AddressLinesValidator
    - ZipValidator
    - SateValidator
    - CityValidator
- top level validator:
    ```java
    public class AddressValidator {
        public bool validate(Address a) {
            return (
                AddressLinesValidator.validate(a.addressLines)
                && ZipValidator.validate(a.zip)
                && StateValidator.validate(a.state)
                && CityValidator.validate(a.city)
            );
        }
    }
    ```
- Let's try to write for a component level validator
    ```java
    public class ZipValidator {
        public book validate(String zip) {
            // some logic here
        }
    }
    ```
    How would this be actually implemented?
- Have some DB containing the valid zip codes
- Should the DB call be here?
    - DB is on a different server
    - Complex connection code. Network call. Caching. Access control.
    - Nopes. Single responsibility.
    - Have a different class for all DB operations
- Same DB will also have details about cities, states, ...

Singleton Pattern
-----------------

```java
public class ResourceInitializer {
    // where do you initialize all the things?
    public ResourceInitializer() {
        // connect to DB
        // query
        // parse results
        // store data in this.attribute
    }
}
```
- What happens if we create a new DB instance for each call?
    - repeated expensive connections
    - DB will get DOS'd
- Don't want clients to create multiple isntances
- First instance itself will load all the needed data and store it in attributes
- Clients must share one common isntance
- Hide the constructor - private

```java
public class ResourceInitializer {
    private static ResourceInitializer INSTANCE;
    
    private ResourceInitializer() {
        // connect to DB
        // query
        // parse results
        // store data in this.attribute
    }
    public static ResourceInitializer getInstance() {
        if(INSTANCE == null) {
            INSTANCE = new ResourceInitializer();
        }
        return INSTANCE;
    }
}
```

- now, clients can't access contructor.
- they must call getInstance to get an instance
- same instance shared across all clients
- now it can have attributes that can be initalized in constructor

```java
public Set<String> zips;

private ResourceInitializer() {
    // init zips
}

ZipValidator {
    bool validateZip(String zip) {
        return ResourceInitializer.getInstance().zips.contains(zip);
    }
}
```
- this code saves lot of resources and time

-- --
    
    