## Topics to be Covered

1. **How to Retrieve Parameters in an API Call**
2. **How to Send Responses in an API Call**
3. **How to Call an External API (FakeStore API)**

---


## How to Retrieve Parameters in an API Call

We will start by designing the **ProductService** in our API, which will manage several key operations related to products in an e-commerce system. These operations include:

- **Creating a New Product:** This operation will allow clients to add new products to the system by providing necessary details like title, description, and price.
  
- **Updating Product Metadata:** Metadata refers to the static parts of the product that rarely change, such as the title and description. We will provide an endpoint to update these details as necessary.
  
- **Retrieving All Products:** This operation will return a list of all products available in the system, which can be useful for displaying a catalog or managing inventory.

- **Fetching Details of a Single Product:** This will allow clients to retrieve detailed information about a specific product, identified by its unique `productId`.

- **Associating Products with Different Categories:** This operation will enable products to be linked to various categories, helping organize them within the system.

### Understanding API Endpoints

In Spring, an API is essentially a method within a controller class. Let’s think about the different endpoints we need to create for the **ProductService**:

### 1. Retrieve All Products
- **Endpoint:** `GET /products`
- **Purpose:** This endpoint allows clients to retrieve a list of all products available in the system. It’s a simple `GET` request that returns a collection of product data.

### 2. Retrieve Single Product Details
- **Endpoint:** `GET /products/{productId}`
- **Purpose:** When a client needs information about a specific product, they can use this endpoint. The `productId` is passed as a **path variable** in the URL, indicating which product’s details should be fetched.

   - Example: `GET /products/123` would retrieve the details for the product with the ID `123`.

### 3. Create a New Product
- **Endpoint:** `POST /products`
- **Purpose:** To add a new product to the system, clients will send a `POST` request to this endpoint. Creating a product typically requires multiple parameters, such as title, description, and price. These details are too complex to be passed via path variables, so they are sent in the **request body**.

   - **Request Body Example:**
   ```json
   {
     "title": "New Product",
     "description": "A description of the new product.",
     "price": 19.99,
     "imageUrl": "http://example.com/image.jpg",
     "category": "Electronics"
   }
   ```

### 4. Apply Filters to Retrieve Products
- **Purpose:** Sometimes, clients need to retrieve products based on specific criteria like title, description, or price. However, it’s impractical to create separate endpoints for every possible filter. Instead, filters are passed as **query parameters** in the URL. These parameters are appended to the URL after a `?` and modify how the controller processes the request.

   - Example: `GET /products?title=Smartphone&price=500` could filter products based on their title and price.

   - **Query Parameter Example:**
     - `GET /products?category=Electronics`
     - `GET /products?title=Smartphone&sort=price`

### Summary of Parameter Passing Methods:

1. **Path Variables:** Parameters included in the URL path itself, such as `{productId}` in `/products/{productId}`.
2. **Request Body:** Used in `POST` and `PUT` requests to send complex data like JSON objects.
3. **Query Parameters:** Appended to the URL to filter or modify the request, used in `GET` requests.

These different methods allow flexibility in how clients can interact with your API, providing a powerful toolset for managing product data.

---

## Sending Responses in an API Call and Calling External Services

### Setting Up the Spring Application

To begin, we need to ensure that our Spring application is correctly set up to handle these API calls. The application should follow the **Model-View-Controller (MVC)** architecture, which organizes the code into three main components:

- **Model:** Represents the data structure. In our case, this would be the `Product` class.
- **View:** Handles the presentation layer. While this is not directly relevant for a backend API, it could involve rendering JSON responses.
- **Controller:** Manages the incoming HTTP requests, processes them, and returns appropriate responses.

### Implementing the Controller

The controller in a Spring application is responsible for defining the endpoints and handling the requests made to those endpoints. Below is an example of how we might set up a basic `ProductController`:

```java
package dev.naman.productservicettsmorningdeb24.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ProductController {

    @PostMapping("/products")
    public void createProduct() {
        // Logic to create a new product
    }
    
    @GetMapping("/products/{id}")
    public void getProductDetails(@PathVariable("id") Long productId) {
        // Logic to fetch product details by ID
    }

    @GetMapping("/products")
    public void getAllProducts() {
        // Logic to retrieve all products
    }

    public void updateProduct() {
        // Logic to update a product
    }
}
```

#### Key Annotations Explained:
- **@RestController:** This annotation is used to mark the class as a Spring MVC Controller where each method returns a domain object instead of a view. It is a combination of `@Controller` and `@ResponseBody`, and it simplifies the creation of RESTful web services.
  
- **@GetMapping and @PostMapping:** These annotations are used to map HTTP `GET` and `POST` requests to specific methods in the controller. For example, `@GetMapping("/products/{id}")` maps a `GET` request for a specific product to the `getProductDetails` method.

### Handling Responses

After receiving a request, the server must send an appropriate response back to the client. In a typical RESTful API, this response is often in the form of JSON. However, manually creating JSON responses can lead to messy and error-prone code. Instead, Spring simplifies this process by automatically converting Java objects to JSON and vice versa.

To manage this, we send and receive data in the form of **Objects**. Spring handles the conversion (serialization) of these objects into JSON format when sending the response and deserializes JSON into objects when receiving a request.

### Using DTOs (Data Transfer Objects)

DTOs are special objects that are used to transfer data between the client and the server. They encapsulate only the necessary information, providing a level of abstraction and security by not exposing the internal data structure (Models) directly.

- **Purpose of DTOs:**
  - They act as a data carrier between different layers of the application.
  - They prevent the exposure of the internal models directly to the client.
  - They allow for the customization of data sent and received without altering the core model.

### Example: Creating the Product Model

Before we proceed with implementing DTOs, let’s define our core data structure, the `Product` model:

```java
package dev.naman.productservicettsmorningdeb24.models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Product {
    private Long id;
    private String title;
    private String description;
    private double price;
    private String imageUrl;
    private Category category;
}
```

#### Explanation of Annotations

:
- **@Getter and @Setter:** These annotations are provided by the Lombok library, and they automatically generate getter and setter methods for all the fields in the class. This reduces boilerplate code and keeps the model clean.
  
- **@NoArgsConstructor and @AllArgsConstructor:** These annotations generate constructors with no arguments and all arguments, respectively. This provides flexibility when creating instances of the `Product` class.

### Building Our First API Service

While the controller handles the endpoints, it’s essential to separate the business logic into a service layer to keep the code organized and maintainable. This separation allows the controller to focus on handling HTTP requests and responses, while the service layer manages the underlying logic and data processing.

For example, in our proxy server setup, we might create a service class named `FakeStoreProductService`, which will handle the interaction with the external FakeStore API.

```java
package dev.naman.productservicettsmorningdeb24.services;

import dev.naman.productservicettsmorningdeb24.models.Product;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class FakeStoreProductService implements ProductService {

    @Override
    public Product getSingleProduct(Long productId) {
        // Logic to fetch a single product from the external API
        return null;
    }

    @Override
    public List<Product> getProducts() {
        // Logic to fetch a list of products from the external API
        return null;
    }
}
```

### Integrating the Service in the Controller

The `ProductController` will now use the `ProductService` to handle the business logic. This is done using **Dependency Injection**, where the service is injected into the controller, allowing it to be used in the controller methods.

```java
package dev.naman.productservicettsmorningdeb24.controllers;

import dev.naman.productservicettsmorningdeb24.models.Product;
import dev.naman.productservicettsmorningdeb24.services.ProductService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ProductController {

    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @PostMapping("/products")
    public void createProduct() {
        // Logic to create a new product
    }

    @GetMapping("/products/{id}")
    public Product getProductDetails(@PathVariable("id") Long productId) {
        return productService.getSingleProduct(productId);
    }

    @GetMapping("/products")
    public void getAllProducts() {
        // Logic to retrieve all products
    }

    public void updateProduct() {
        // Logic to update a product
    }
}
```

### Explanation of Dependency Injection:
- **Dependency Injection:** Spring’s mechanism to manage object creation and their dependencies automatically. The service (`ProductService`) is injected into the controller, allowing the controller to use its methods without needing to instantiate the service directly. This promotes loose coupling and enhances testability.

