## Topics to be covered:
- **How to Call an External API**
- **How to Send Responses from Your API**
- **Implementing the "Get All Products" API**
- **Understanding ResponseEntity**
- **Handling Exceptions in Spring**
- **How Requests Work in Spring**

---

## 1. How to Call an External API and Send Responses

### Introduction
In this section, we will explore the process of integrating external APIs into your Spring application, specifically using the **FakeStore** API as an example. We'll discuss the challenges of mapping external data to your internal models, the role of Data Transfer Objects (DTOs), and the importance of dependency injection in Spring.

### Data Model Differences and the Role of DTOs
When working with external APIs, it's rare that the data returned by the API will match your internal model structure exactly. For example, consider a scenario where you need to retrieve product information from the FakeStore API. The data structure returned by the FakeStore API might differ significantly from the structure of your internal `Product` model.

#### Example: Product Model Comparison

Here’s a visual comparison:

![Product Model Comparison](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/196/original/1.png?1725165788)

- **Left Side**: The structure of the data returned by the FakeStore API.
- **Right Side**: The structure of your internal `Product` model in `Product.java`.

**Key Point:** Since the data structures differ, you cannot directly map the API response to your internal model. This is where **DTOs** (Data Transfer Objects) come into play. A DTO acts as an intermediary, transforming the external data into a format that aligns with your internal models.

#### Creating a DTO
You would create a DTO class to represent the external data and include a method to convert this DTO into your internal `Product` model.

**Example:**
```java
@Getter
@Setter
public class FakeStoreProductDto {
    private Long id;
    private String title;
    private String image;
    private String description;
    private String category;
    private double price;

    public Product toProduct() {
        Product product = new Product();
        product.setId(id);
        product.setTitle(title);
        product.setDescription(description);
        product.setPrice(price);
        product.setImageUrl(image);

        Category productCategory = new Category();
        productCategory.setTitle(category);
        product.setCategory(productCategory);

        return product;
    }
}
```

In this example:
- The `FakeStoreProductDto` class has fields that match the structure of the data returned by the FakeStore API.
- The `toProduct()` method converts the `FakeStoreProductDto` object into a `Product` object that matches your internal model.

### Dependency Injection in Spring

#### Problem: Managing Multiple Instances
Consider a scenario where multiple classes in your project need to call the `FakeStoreService`. If each class creates its own instance of `RestTemplate` (the object responsible for making HTTP requests), it leads to unnecessary duplication and resource consumption.

**Solution: Dependency Injection**

Instead of creating multiple instances of `RestTemplate`, you can leverage Spring's **Dependency Injection** to manage a single shared instance across your application. This not only optimizes resource usage but also simplifies testing and maintenance.

#### Configuring Dependency Injection
To achieve this, you define a `RestTemplate` bean within a configuration class. This bean is created once and can be injected into any class that needs it.

**Example:**
```java
@Configuration
public class ApplicationConfiguration {

    @Bean
    public RestTemplate createRestTemplate() {
        return new RestTemplate();
    }
}
```

- **Explanation:** 
  - The `@Configuration` annotation marks this class as a configuration class.
  - The `@Bean` annotation indicates that the `createRestTemplate()` method returns an object that should be managed by Spring's application context.
  - Whenever a `RestTemplate` is required, Spring will inject this single instance, ensuring that all classes share the same `RestTemplate` object.

### Implementing the `GetProductById` API

Now that we have the infrastructure in place (DTO and `RestTemplate` bean), we can implement an API to fetch a product by its ID.

#### Example Implementation:
```java
public Product getSingleProduct(Long productId) {
    FakeStoreProductDto fakeStoreProduct = restTemplate.getForObject(
        "https://fakestoreapi.com/products/" + productId,
        FakeStoreProductDto.class
    );

    return fakeStoreProduct.toProduct();
}
```

- **Explanation:**
  - The `getForObject()` method of `RestTemplate` is used to make a GET request to the FakeStore API.
  - The API response is automatically mapped to an instance of `FakeStoreProductDto`.
  - The `toProduct()` method is then called to convert the DTO into your internal `Product` model before returning it.

### Sending Responses

When the API call to the external service is made, the response must be mapped back to your internal model. The `FakeStoreProductDto` is instrumental in this process as it bridges the gap between the external data and your internal data structures.

#### Example:
```java
FakeStoreProductDto fakeStoreProduct = restTemplate.getForObject(
    "https://fakestoreapi.com/products/" + productId,
    FakeStoreProductDto.class
);

return fakeStoreProduct.toProduct();
```

- **Key Point:** The `toProduct()` method ensures that the external API data is correctly translated into the internal `Product` model.

---

## 2. Implementing the `CreateNewProduct` API

### Introduction
Creating a new product in your application requires gathering necessary data (such as title, description, category, price, and image) and sending this data to the external API. However, the data needed to create a product might differ from the data returned by the API when fetching a product.

### Creating a Request DTO

A separate DTO should be created for the data required to create a product. This DTO will exclude fields that are not necessary for product creation, such as `userId` or `productId`.

**Example:**
```java
@Getter
@Setter
public class CreateProductRequestDto {
    private String title;
    private String image;
    private String description;
    private String category;
    private double price;
}
```

- **Explanation:** This DTO captures only the fields needed to create a new product. This ensures that your API remains clean and only transmits the required data.

### Service Implementation

The service layer should be generic, meaning it should not be tightly coupled with the DTOs. The service method should accept individual parameters rather than DTOs, making the service layer more flexible and reusable.

#### Example Implementation:
```java
public Product createProduct(String title,
                             String description,
                             String category,
                             double price,
                             String image) {
    FakeStoreProductDto fakeStoreProductDto = new FakeStoreProductDto();
    fakeStoreProductDto.setTitle(title);
    fakeStoreProductDto.setCategory(category);
    fakeStoreProductDto.setPrice(price);
    fakeStoreProductDto.setImage(image);
    fakeStoreProductDto.setDescription(description);

    FakeStoreProductDto response = restTemplate.postForObject(
        "https://fakestoreapi.com/products", // URL
        fakeStoreProductDto, // Request body
        FakeStoreProductDto.class // Expected response type
    );

    return response != null ? response.toProduct() : new Product();
}
```

- **Explanation:**
  - The method creates an instance of `FakeStoreProductDto` and populates it with the provided parameters.
  - The `postForObject()` method sends the DTO to the FakeStore API to create a new product and returns the API’s response, which is then converted to your internal `Product` model using `toProduct()`.

### Controller Integration

The controller is responsible for handling HTTP requests and invoking the appropriate service methods. It maps the incoming request data to the service method parameters.

**Example:**
```java
public Product createProduct(@RequestBody CreateProductRequestDto request) {
    return productService.createProduct(
        request.getTitle(),
        request.getDescription(),
        request.getCategory(),
        request.getPrice(),
        request.getImage()
    );
}
```

- **Explanation:** 
  - The `@RequestBody` annotation binds the incoming HTTP request body to the `CreateProductRequestDto`.
  - The controller then calls the `createProduct()` method in the service, passing the necessary parameters extracted from the DTO.

---

## 3. Implementing the `Get All Products` API

### Overview

When you need to fetch a list of products, handling the data structure returned by the external API can become challenging due to Java's type erasure, which can cause issues with handling generic types like `List<FakeStoreProductDto>`.

### Problem with Direct Implementation

A direct approach to retrieving a list of products might look like this:

```java
List<FakeStoreProductDto> fakeStoreProducts = restTemplate.getForObject(
    "https://fakestoreapi.com/products", List<FakeStoreProductDto>.class
);
```

However, this can lead to errors because Java’s type system loses track of the specific type of objects in the list due to type erasure. Type erasure is a mechanism where Java removes generic type information at runtime, leading to potential issues when working with collections of parameterized types.

#### Example Error:
Attempting to retrieve a list directly in this manner can result in a `ClassCastException` or other errors because Java struggles to map the response to a parameterized list.

### Solution: Fetching an Array Instead of a List

To work around this issue, retrieve an array of `FakeStoreProductDto` objects instead. Arrays in Java retain type information more reliably than parameterized

 lists.

#### Step-by-Step Solution:
1. **Fetch an array** of `FakeStoreProductDto` from the API.
2. **Manually create a list** and populate it with the converted `Product` objects.

**Example Implementation:**
```java
public List<Product> getProducts() {
    FakeStoreProductDto[] fakeStoreProducts = restTemplate.getForObject(
        "https://fakestoreapi.com/products", FakeStoreProductDto[].class
    );

    List<Product> products = new ArrayList<>();
    for (FakeStoreProductDto dto : fakeStoreProducts) {
        products.add(dto.toProduct());
    }

    return products;
}
```

- **Explanation:** 
  - The API response is first fetched as an array of `FakeStoreProductDto`.
  - Each item in the array is converted to a `Product` object and added to a new list.
  - This method avoids the pitfalls of type erasure by handling the conversion manually.

---

## 4. HTTP Entities: Status Codes, Headers, and Cookies

### Introduction

When working with HTTP responses, it’s important to understand that responses include more than just the payload data. HTTP responses also contain status codes, headers, and cookies, which can be critical for handling responses properly.

### Status Codes

HTTP status codes are standardized codes that indicate the result of the HTTP request. Common examples include:
- **200 OK**: The request was successful.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: The server encountered an unexpected condition.

These codes inform both the client and the server about the outcome of the request and guide the next steps in processing or error handling.

#### Example:
When accessing a webpage or API endpoint that doesn’t exist, you receive a `404 Not Found` status code. This tells you that the resource could not be located.

### Other Parameters in HTTP Responses

In addition to status codes, HTTP responses may include additional metadata such as headers and cookies.

- **Headers:** Provide information about the request or response, such as content type, encoding, and caching policies.
- **Cookies:** Small pieces of data stored on the client-side to maintain session state or track user activities.

### Accessing Response Metadata with `getForEntity`

While `getForObject()` retrieves only the payload, `getForEntity()` provides access to the entire HTTP response, including headers, status codes, and cookies.

#### Example:
```java
public Product getSingleProduct(Long productId) {
    ResponseEntity<FakeStoreProductDto> fakeStoreProductResponse = restTemplate.getForEntity(
        "https://fakestoreapi.com/products/" + productId,
        FakeStoreProductDto.class
    );

    if (fakeStoreProductResponse.getStatusCode() != HttpStatus.OK) {
        // Handle the error appropriately
    }

    FakeStoreProductDto fakeStoreProduct = fakeStoreProductResponse.getBody();
    return fakeStoreProduct.toProduct();
}
```

- **Explanation:** 
  - `getForEntity()` is used to capture the full response from the API.
  - The `ResponseEntity` object contains both the status code and the response body.
  - By checking the status code, you can implement additional error handling logic before processing the response.

---

## 5. Exception Handling in Spring

### The Importance of Exception Handling

Proper exception handling is crucial for creating robust and secure applications. Without it, errors can expose sensitive information or lead to unhandled exceptions that degrade the user experience.

For example, if an invalid product ID is provided, the application might return an error response with internal details, which is both a security risk and poor practice.

### Using `ControllerAdvice` for Global Exception Handling

Spring provides the `@ControllerAdvice` annotation, which allows you to handle exceptions across the entire application, rather than in individual controllers.

#### Example: `ProductNotFoundException`

First, create a custom exception class:
```java
public class ProductNotFoundException extends RuntimeException {
    public ProductNotFoundException(String message) {
        super(message);
    }
}
```

- **Explanation:** 
  - This exception can be thrown when a requested product is not found.
  - It extends `RuntimeException`, making it an unchecked exception that can be used throughout the application.

#### Implementing `ControllerAdvice` for Global Exception Handling

Create a global exception handler using `ControllerAdvice`:
```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ProductNotFoundException.class)
    public ResponseEntity<ErrorDto> handleProductNotFoundException(ProductNotFoundException exception) {
        ErrorDto errorDto = new ErrorDto();
        errorDto.setMessage(exception.getMessage());

        return new ResponseEntity<>(errorDto, HttpStatus.NOT_FOUND);
    }
}
```

- **Explanation:** 
  - The `@ControllerAdvice` annotation indicates that this class provides centralized exception handling across all controllers.
  - The `@ExceptionHandler` method listens for `ProductNotFoundException` and returns a custom error response.
  - The `ErrorDto` class encapsulates the error message, ensuring that only relevant information is returned to the client, protecting internal implementation details.

### Cleaner Error Responses

By handling exceptions globally, the application can return cleaner, more user-friendly error messages.

#### Example:
If a product ID does not exist, instead of exposing internal stack traces, the application can return:
```json
{
    "message": "Product with ID 123 not found"
}
```

- **Key Point:** This approach improves both security and user experience by ensuring that error messages are informative yet not overly revealing.

---

## 6. How Requests Work in Spring

### Introduction

When a client makes a request to a Spring application, the framework handles routing and processing behind the scenes. Understanding this flow is crucial for debugging and optimizing your application.

### Role of DispatcherServlet

The **DispatcherServlet** is the front controller in a Spring MVC application. It acts as the central point for handling incoming requests.

#### Request Flow:
1. **DispatcherServlet** receives the incoming request.
2. It forwards the request to the **Handler Mapping**, which maps the request to the appropriate controller based on predefined mappings.
3. If the mapping is found, the request is sent to the corresponding controller.
4. If no mapping is found, a `404 Not Found` response is returned.

![Request Flow in Spring](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/197/original/2.png?1725165815)

- **Explanation:** 
  - The DispatcherServlet orchestrates the entire request lifecycle, ensuring that requests are handled efficiently and routed to the correct controller.
  - This process ensures that even as your application scales, requests are consistently processed and routed according to your application’s configuration.



