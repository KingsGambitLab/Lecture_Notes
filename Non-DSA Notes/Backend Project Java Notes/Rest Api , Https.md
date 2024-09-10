
## Topics to be Covered

1. **Creating and Starting Our First SpringBoot App:** .
2. **Understanding the MVC Pattern**
3. **Introduction to APIs** 
4. **Deep Dive into REST APIs**
5. **Preview of Fakestore API Implementation**

---

## Creating and Starting Our First SpringBoot App

1. **Opening Intellij IDEA:**
   - Launch **Intellij IDEA Ultimate**.
   - Click on the "New" button to start a new project.
   - Select the "Spring Initializer" option, which is a built-in utility in Intellij IDEA designed by the SpringBoot team. This tool simplifies the process of starting a SpringBoot project by pre-configuring many of the necessary components.

   ![Spring Initializer](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/170/original/1.png?1725112903)
   
   - **Alternative Option:** If Intellij IDEA is not available, use the web-based [Spring Initializer](https://start.spring.io/). This tool provides the same functionality and allows you to generate a SpringBoot project structure that can be downloaded and imported into your preferred IDE.

2. **Project Naming and Language Selection:**
   - **Project Name:** Enter `myfirstspringproject` as the project name.
   - **Language:** Select **Java** as the programming language. Java is chosen because it runs on the Java Virtual Machine (JVM), which allows Java applications to be platform-independent. Unlike languages like C and C++, which are platform-dependent and require different code for different operating systems, Java code runs on the JVM, making it versatile across various platforms.

3. **Understanding Dependency Management with Maven:**
   - **Dependency Management:** the importance of managing third-party libraries and dependencies in a project. Maven is introduced as a tool for this purpose. 
   - **Why Maven?** Maven is widely used in Java projects for dependency management, build automation, and project management. It simplifies the process of including necessary libraries and ensures that your project has everything it needs to compile and run correctly.

4. **Package Naming Conventions:**
   - **Unique Identification:** Explain why Java uses package names to organize files and avoid conflicts. For instance, if multiple developers create a file named `Hello.java` and share it publicly, package names help ensure that each file can be uniquely identified.
   - **Example:** `package dev.naman.scaler.productservice.Hello.java`
   - **Group ID and Artifact ID:**
     - **Group ID:** Typically the reverse of a unique domain name (e.g., `com.scaler`). This helps in uniquely identifying the organization or group responsible for the project.
     - **Artifact ID:** The specific name of the project or module within a larger application (e.g., `productservice`).

5. **Java Version and Dependency Selection:**
   - **Java Version:** Choose **Java 17** for this project, as it is a stable and long-term supported version.
   - **Dependencies:** Select the following essential dependencies to include in your project:
     - **Spring Boot Dev Tools:** For development-time features, such as automatic restarts and live reloads.
     - **Lombok:** To reduce boilerplate code by providing annotations that generate code for common tasks like getters, setters, and constructors.
     - **Spring Configuration Processor:** For managing Spring configuration metadata.
     - **Spring Web:** To enable web development features, such as creating RESTful web services.

   ![Dependency Selection](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/172/original/2.png?1725112930)

6. **Generating and Exploring the Project:**
   - After selecting the dependencies, click "Create" to generate the project.
   - **Generated Structure:** The SpringBoot initializer will create a project structure with pre-configured files and directories.
   - Navigate to the following location in your project directory:
     - `src -> main -> java -> package`
   - **Create a New File:** Name it `MyFirstAPI.java`. This file will contain the code for your first API.

7. **Running the Application:**
   - Implement a simple dynamic endpoint in the `MyFirstAPI.java` file. For example, create an endpoint `http://localhost:8000/hello/{name_of_person}` that returns a personalized greeting message, such as "Hello {name_of_person}".


8. **Emphasizing Code Structure:**
   - Highlight the importance of organizing code in a way that maintains readability and manageability as the project grows. This prepares students for the next topic on the MVC pattern, which is essential for structuring larger codebases.

---

## Understanding the MVC Pattern


**Analogy for MVC:**
- Imagine you are at a restaurant:
  - **Waiter (Controller):** Takes your order and communicates it to the chef.
  - **Chef (Service):** Prepares the food based on the order.
  - **Waiter (Controller):** Delivers the prepared food to you.
  - **Refrigerator (Repository):** Stores the ingredients (data) that the chef uses to prepare the food.
  - **Customer (Client):** Receives the food (view) as per their order.

![MVC Analogy](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/173/original/3.png?1725112953)

**Applying MVC to Web Applications:**
- When building an API, such as a `/login` endpoint, you might need to perform several tasks:
  - Validate user input.
  - Authenticate the user by checking credentials in a database.
  - Send notifications or emails upon successful login.
  - If all these tasks are handled in a single method, it can become cumbersome and difficult to maintain.

**MVC Pattern Breakdown:**
- **Controller (C):**
  - Acts as the waiter, handling incoming HTTP requests from the client (browser or mobile app).
  - Responsibilities:
    - Validate the incoming request (e.g., checking for required parameters).
    - Call the appropriate services to handle the business logic.
    - Return the appropriate response to the client.
  - Example: `loginService`, `emailService`.

- **Service (S):**
  - The core of the application where the business logic resides.
  - Responsibilities:
    - Perform complex operations, such as user authentication, data processing, etc.
    - Interact with the repository to fetch or store data.
  - **Separation from Repository:** Services should not directly interact with the database; instead, they should call repository classes to handle data persistence. This ensures that changes in the database structure only affect the repository, not the entire application.

- **Repository (R):**
  - Manages database interactions.
  - Responsibilities:
    - Handle CRUD operations (Create, Read, Update, Delete) for the data models.
    - Provide an abstraction layer over the database, making it easier to switch databases or change schema with minimal impact on the rest of the application.

  ![MVC Flow](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/174/original/4.png?1725112973)

- **Model (M):**
  - Represents the data or business entities within the application.
  - Example: In an e-commerce application, a `Product` model might represent items in a product catalog.

- **View (V):**
  - The user-facing side of the application that displays data.
  - **Selective Data Presentation:** Not all data stored in the database is sent to the client. The view determines how much and what kind of data is presented to the user.
  - Example: If a product in the database has a lot of details, the view might only show the product name, price, and a brief description to the client.

**Benefits of MVC:**
- **Code Organization:** MVC allows for a clean separation of concerns, making code easier to maintain and extend.
- **Scalability:** As the application grows, the separation of concerns makes it easier to manage changes and additions without impacting other parts of the system.

---

## What are APIs?

**Definition:**
- **API:** A set of rules (contract) that allows one software application to communicate with another. It defines the types of requests that can be made, how to make them, and the expected responses.

**Key Concepts:**
1. **Interface as a Contract:**
   - Think of an API as a contract between two software components. This contract specifies:
     - What requests can be made (e.g., fetch data, submit data).
     - What information needs to be sent with the request (e.g., parameters, headers).
     - What the expected response will be (e.g., data format, status codes).

2. **Communication Between Applications:**
   - **Frontend to Backend:** APIs are commonly used to allow the frontend (user interface) of an application to communicate with the backend (server-side logic and database).
   - **Backend to Backend:** APIs also facilitate communication between the backend of one application and the backend of another. For example, a payment processing service might communicate with an e-commerce platform through APIs.

**Importance of APIs:**
- APIs enable modular software development, where different parts of an application or different applications altogether can interact seamlessly.
- They promote reusability and scalability by allowing different systems to communicate without needing to know the internal workings of each other.

**Introduction to REST APIs:**
- **REST (Representational State Transfer):** A set of guidelines for designing networked applications, particularly APIs, that emphasize simplicity, scalability, and statelessness.
- REST APIs are widely used because they make APIs more understandable and easier to interact with.

**Next Steps:**
- Students are encouraged to explore the [best practices for API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) Documentation.

---

## REST APIs

**REST API Principles:**
1. **Resource-Centric Design:**
   - REST APIs should be designed around the resources they are intended to manage (e.g., users, products, orders).
   - **Resource Naming:** The API endpoints should represent the resource, not the action. For example, to retrieve product details, use `/product/{product_id}` instead of `/get_product_details`.

2. **Avoiding Verb-Based Endpoints:**
   - Do not include actions (verbs) in the endpoint names. Instead, use HTTP methods to define the action.
   - Example of Bad Practice: `/upload_video`
   - Example of Good Practice: Use `/videos` with appropriate HTTP methods like POST or PUT to handle uploads.

3. **CRUD Operations:**
   - REST APIs typically involve four basic operations on resources:
     - **Create:** Add a new resource.
     - **Read:** Retrieve existing resources.
     - **Update:** Modify existing resources.
     - **Delete:** Remove resources.

**HTTP Methods and Their Usage:**
1. **GET:**
   - Used to retrieve information about a resource.
   - Example: `GET /product/{product_id}` returns details about a specific product.

2. **POST:**
   - Used to create a new resource.
   - Example: `POST /products` creates a new product in the database.

3. **PUT:**
   - Used to update an existing resource or create a new one if it does not exist.
   - Example: `PUT /product/{product_id}` updates the product if it exists or creates it if it does not.

4. **PATCH:**
   - Similar to PUT but only updates partial data rather than the entire resource.
   - Example: `PATCH /product/{product_id}` might update only the product's price while leaving other fields unchanged.

5. **DELETE:**
   - Used to remove a resource from the server.
   - Example: `DELETE /product/{product_id}` deletes the specified product.

   ![HTTP Methods](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/175/original/5.png?1725112997)

**Important Considerations:**
- **Conventions and Best Practices:** While HTTP methods are technically just words that can be customized, following established conventions (GET, POST, PUT, PATCH, DELETE) ensures that your API is intuitive and easy to use.
- **Code Implementation:** The actual behavior of an HTTP method is defined in the backend code. While it's possible to misuse HTTP methods (e.g., creating a resource with GET), such practices are discouraged as they violate REST principles and can lead to confusion.




