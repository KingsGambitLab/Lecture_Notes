LLD 4
-----

Cascader Pattern
----------------
```java
public class Address {
    String city, state, zip, lines[];
}
```

1. Validating address
    - Need to validate each part
1. Algo(zip) < Algo(state) < Algo(city) < Algo(lines)
    - both in difficulty and time complexity
1. Need to check combined as well
    - `* <` Algo(combined)
1. Has been observed that most of the time, people make mistakes in Zip
    - Does it make sense to validate everything else?
    - No. Check zip first
1. We provide this combined validator to our client
    ```java
    public class CombinedValidator {
        private static ZipValidator z = new ZipValidator();
        private static StateValidator s = new StateValidator();

        bool validate(Address a) {
            return z.validate(a)
                && s.validate(a)
                && ...;
            // order is important to fail fast
        }
    }
    ```
1. Fail fast - prune the bad requests
    - just like in recursion - branch and bound
1. Can we improve upon the &&?
    - Could be more complex than &&
    - Have multiple steps for each validator
1. Abstract it out into a loop
    - Find the repeated thing
    - Make a loop for it.
1. But class is different each time
    - Can we make it same?
    - Code classes against an interface
        ```java
        public interface Validator {
            bool validate(Address);
        }

        public class ZipValidator implements Validator {
            bool validate(Address a) { ... }
        }
        ```
1. Make the loop (using Runtime Polumorphism)
    - What DS should we use to store the Validators?
    ```java
    public class CombinedValidator {
        private List<Validator> validators;
        public CombinedValidator() {
            validators = Arrays.asList(
                new ZipValidator(),
                new StateValidator(),
                ... 
            );
        }

        bool validate(Address a) {
            for(Validator v: validators)
                if(!v.validate(a))
                    return false;
            return true;
        }
    }
    ```
1. Could we have used a Set instead of List?
    - No. Order matters!
1. Clients appear asking for different Combinations
    - Either expose the programming interface - clients pass their own lists
    - Many times, you onboard a client
    - Communication over email / person like "we need to validate xyz using your code"
    - You provide them with one function call for that
1. Provide a combination for each client, associated with a client name
    - c1 neess V1, V2, V3
    - c2 needs V1, V4
    - ...
    - can use hashmap
    - should we store lists in values?
    - No, we can use CombinedValidator
1. CombinedValidator can implement Validator
    ```java
    class X {
        Map<clientName, Validator> mapping;
        public X() {
            mapping.put("order_page", CombinedValidator(Arrays.asList(
                new ZipValidator(),
                new CityValidator(),
                new LinesValidator(),
            )));
            mapping.put("KYC_check", CombinedValidator(Arrays.asList(
                new ZipValidator(),
                new CityValidator(),
            )));
        }
    }
    ```
1. Lots of objects being created in constructor. Make it singleton.
1. Convert it into a factory (+singleton)
    ```java
    class ValidatorCascadeFactory {
        Map<clientName, Validator> mapping;
        private ValidatorCascadeFactory() {
            mapping.put("order_page", CombinedValidator(Arrays.asList(
                new ZipValidator(),
                new CityValidator(),
                new LinesValidator(),
            )));
            mapping.put("KYC_check", CombinedValidator(Arrays.asList(
                new ZipValidator(),
                new CityValidator(),
            )));   
        }
        public CascadeFactory getInstance() // singleton
        public Validator getValidator(String clineName) // factory
        // note: exception handle in getValidator
    }
    
    public class ValidatorCascade implements Validator {
        private List<Validator> validators;
        
        public ValidatorCascade(List<Validator> validators);

        bool validate(Address a) {
            for(Validator v: validators)
                if(!v.validate(a))
                    return false;
            return true;
        }
    }
    ```
1. Cascade
    - staircase
    - fail: exit
    - pass: move to next step
1. Client Code
    ```java
    class ClientValidator {
        bool validate(Address a) {
            return ValidatorCascadeFactory.getInstance()
                                          .getValidator(name)
                                          .validate(a);
        }
    }
    ```
1. Note that in this code, we used Cascade, Factory, Singleton
1. Order important?
    - yes, here
    - not always
1. Address cleaning
    - clean zip
    - clean city
    - clean State
    - clean lines
1. Need to perform all. All are independent - don't effect one another
1. Can use a Set instead of a List
1. Must use List in substrategy
    - first remove ,
    - then remove space
    - then lowercase
    - ...
-- --
