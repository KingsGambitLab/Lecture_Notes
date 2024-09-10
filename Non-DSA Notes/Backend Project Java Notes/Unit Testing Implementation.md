## Topics to be covered

  1. **Understanding the concept of Unit Testing in Java**
  2. **Introduction to JUnit, the widely used testing framework**
  3. **Industry-standard conventions for writing test cases**
  4. **Using the AAA (Arrange-Act-Assert) pattern for structuring tests**
  5. **Writing and structuring random test cases**
  6. **Deep dive into assertion methods and their applications**
  7. **Testing Spring Boot applications using `@SpringBootTest`**
  8. **Mocking dependencies with Mockito for unit testing**
  9. **Best practices for testing service-layer components in Spring**
  10. **Handling and testing for exceptions in controller methods**

---

### 1. Introduction to Unit Testing in Java

**Unit Testing** is a software testing technique in which individual units or components of a software application are tested. A unit is the smallest testable part of any software, usually a function or a method in Java. Unit tests validate that each component of the software functions as expected.

- In Java, **JUnit** is the most commonly used library for writing unit tests. It provides simple annotations and methods to structure and execute test cases effectively.
  
- The best practice when using **JUnit** in a project, especially when using **Spring**, is to organize tests in a separate folder, often named `test`, alongside the main application folder. The directory structure should mirror the structure of the main source code folder to keep tests organized and easy to locate.

  **Example**:
  - For a class named `ProductController` in the `controller` folder of `main`, a corresponding test class named `ProductControllerTest` should be placed in the `controller` folder within `test`.

---

### 2. Writing Random Tests in JUnit

In JUnit, each **test case** is represented by a method, typically annotated with `@Test`. These methods contain the logic for checking if the code behaves as expected under certain conditions.

Test cases are generally written following the **AAA pattern**:
- **Arrange**: Set up the necessary objects, data, or conditions for the test.
- **Act**: Perform the actual action that needs to be tested, such as calling a method.
- **Assert**: Verify that the action performed led to the expected result.

**Example: Writing a simple test case**:

```java
public class RandomTest {
    @Test
    void testOnePlusOneIsTwo() {
        // Arrange
        int i = 1 + 1; // Act
        
        // Assert
        assert i == 3;  // This test will fail because 1 + 1 != 3
    }
}
```

In the above example, a simple test is performed to check if the sum of 1 + 1 equals 3. The test will fail since the assertion `i == 3` is incorrect.

To mark a method as a test case in JUnit, we use the `@Test` annotation. Without this annotation, JUnit will not recognize the method as a test. If we change the assertion to `assert i == 2`, the test will pass.

- **Important Concept**: A test case will fail if any of the assertions within that test case fail.
- JUnit also allows more complex assertions, such as checking whether the right type of exception is thrown during execution. For this, libraries like **AssertJ** can be used.

---

### 3. Assertion Methods in JUnit

JUnit provides various assertion methods to validate the results of the code being tested. Here’s a list of commonly used assertions:

- **Basic Assertions**:
  - `assertEquals(expected, actual)`: Verifies that the expected value matches the actual value.
  - `assertNotEquals(expected, actual)`: Confirms that two values are not equal.
  - `assertTrue(condition)`: Verifies that a boolean condition is true.
  - `assertFalse(condition)`: Checks that a condition is false.
  - `assertNull(object)`: Ensures that an object is `null`.

- **Handling Exceptions**:
  - `assertThrows(expectedException.class, executable)`: Validates that a specific exception is thrown when a method is executed.

- **Array Comparisons**:
  - `assertArrayEquals(expectedArray, actualArray)`: Compares two arrays to ensure they contain the same elements in the same order.

- **Checking Time Constraints**:
  - `assertTimeout(Duration.ofSeconds(2), executable)`: Ensures that the test completes within a specific time limit, preventing performance issues.

- **Class Object Assertions**:
  - `assertInstanceOf(ExpectedClass.class, object)`: Checks if an object is an instance of a particular class.

#### Important Rule for Assertions:
In any assertion that takes two parameters, **the expected value should always come first**, followed by the **actual value**. This helps maintain clarity when reading test results, especially when an assertion fails.

---

### 4. Spring Boot Tests

Testing Spring Boot applications requires additional setup to properly load and manage the Spring context. When unit testing a component that interacts with Spring, it is crucial to initialize the Spring Boot application context.

To enable this, annotate the test class with `@SpringBootTest`. This annotation tells Spring Boot to load the entire application context before running the test, simulating the real behavior of the application during execution.

Example of a basic Spring Boot test class:

```java
@SpringBootTest
class ProductControllerTest {
    @Autowired
    private ProductController productController;
}
```

In the above code:
- The `@SpringBootTest` annotation ensures that Spring initializes all necessary components, including controllers, services, and repositories.
- The `@Autowired` annotation injects the `ProductController` instance into the test class, allowing it to be tested.

---

### 5. Mocking Dependencies in Unit Tests

In real-world applications, components often depend on other services. For example, a controller might rely on a service to retrieve data. When unit testing, it’s not efficient to use the actual service layer because it may interact with databases or other external systems.

Instead, we **mock** the dependencies using a library called **Mockito**. This allows us to simulate the behavior of these dependencies, making the test faster and more focused.

**Example: Mocking a service in a test case**:

```java
@MockBean
private ProductService productService;

@Test
void testProductsSameAsService() {
    // Arrange
    List<Product> products = new ArrayList<>();
    Product p1 = new Product(); p1.setTitle("iPhone 15");
    Product p2 = new Product(); p2.setTitle("iPhone 15 Pro");
    Product p3 = new Product(); p3.setTitle("iPhone 15 Pro Max");
    products.add(p1); products.add(p2); products.add(p3);

    when(productService.getAllProducts()).thenReturn(products);

    // Act
    ResponseEntity<List<Product>> response = productController.getAllProducts();

    // Assert
    assertEquals(products.size(), response.getBody().size());
}
```

- The `@MockBean` annotation is used to create a mock object of `ProductService`.
- The `when(...).thenReturn(...)` statement is part of Mockito’s syntax for specifying what the mocked method should return when called.
- This allows us to test the `ProductController`'s `getAllProducts()` method without needing the actual implementation of `ProductService`.

---

### 6. Avoiding Common Bugs in Test Cases

When writing unit tests, it’s important to understand how Java handles references. One common bug occurs when tests modify objects by reference, causing unintended side effects.

For example, if the titles of products are modified in the test case, the original objects may be affected as Java passes values by reference. To avoid this, we should create new instances of objects for comparison.

**Correcting the bug by using separate lists**:

```java
@Test
void testProductsSameAsService() {
    // Arrange
    List<Product> products = new ArrayList<>();
    Product p1 = new Product(); p1.setTitle("iPhone 15");
    Product p2 = new Product(); p2.setTitle("iPhone 15 Pro");
    Product p3 = new Product(); p3.setTitle("iPhone 15 Pro Max");
    products.add(p1); products.add(p2); products.add(p3);

    List<Product> productsToPass = new ArrayList<>();
    for (Product p : products) {
        Product temp = new Product();
        temp.setTitle(p.getTitle());
        productsToPass.add(temp);
    }

    when(productService.getAllProducts()).thenReturn(productsToPass);

    // Act
    ResponseEntity<List<Product>> response = productController.getAllProducts();

    // Assert
    assertEquals(products.size(), response.getBody().size());

    for (int i = 0; i < products.size(); i++) {
        assertEquals(products.get(i).getTitle(), response.getBody().get(i).getTitle());
    }
}
```

---

### 7. Testing for Exceptions in Controller Methods

Sometimes, a controller method may throw an exception if the requested data is not available. For instance, a `getProductById()` method may throw a `ProductNotExistsException` if the requested product doesn’t exist in the database.

To simulate this, we mock the behavior of the `ProductRepository` to return an empty value when searching for a non-existent product ID.

**Testing a non-existent product scenario**:

```java
@MockBean
private ProductRepository productRepository;

@Test
void testNonExistingProductThrowsException() throws ProductNot

ExistsException {
    // Arrange
    when(productRepository.findById(10L)).thenReturn(Optional.empty());

    // Act & Assert
    assertThrows(ProductNotExistsException.class, 
        () -> productController.getSingleProduct(10L));
}
```

- **`assertThrows`** is used to verify that the expected exception (`ProductNotExistsException`) is thrown when attempting to fetch a product with an ID that doesn’t exist.
- Mocking the `ProductRepository` ensures that the service layer doesn’t interact with a real database.

