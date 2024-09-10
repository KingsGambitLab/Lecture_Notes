##  Topics to be covered:

  - **REST APIs**
  - **REST API Best Practices**
  - **Integrating FakeStore API**
  - **Writing Models for our Product Service**

---

## REST API

### Introduction

![Rest API](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/176/original/1.png?1725113693)

- **Definition**: REST API (Representational State Transfer Application Programming Interfaces) is a set of principles and conventions that allows different software systems to communicate over the internet. It is widely used to interact with web services.
- **Core Concept**: When an API call is made, the state of an entity is being transferred. REST APIs have become a standard method for software systems to exchange data over the web.

---

## REST API Best Practices

### Centralization Around Resources

- **Resources as Central Concept**: In RESTful API design, resources (e.g., users, products, orders) represent entities in the system.
- **Endpoint Structure**: API endpoints should be organized around these resources, with interactions performed using HTTP methods:
  - `GET` - Retrieve a resource
  - `POST` - Create a new resource
  - `PUT` - Update an existing resource
  - `DELETE` - Remove a resource
- **Endpoint Naming**: Use nouns in endpoints rather than verbs. For example, use `https://mysite.com/posts` instead of `https://mysite.com/getPosts`.

### Statelessness of REST APIs

- **Concept**: Each API request should be independent and self-sufficient, containing all the necessary information to be processed by any server without relying on previous interactions.
  
**Key Principles:**

1. **API Request Servicability**: 
   - Requests should be handled by any available server through a load balancer, ensuring uniformity and quick processing.
   - **Architecture Overview**:
     - The user's request is sent to a load balancer.
     - The load balancer forwards the request to any available server (e.g., server-1 or server-5).
   - **Result**: Servers should not store any session-specific data, which should instead be handled by a central database accessible by all servers.

   ![Server Load Balancing](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/178/original/2nd_actual.png?1725113776)

2. **Self-Sufficient API Requests**:
   - Example: A user logs in via server-1, but subsequent requests might be routed to server-5. Server-5 won’t know if the user is logged in unless proper credentials (like tokens) are passed with the request.
   - **Implementation**: All APIs should include necessary credentials (e.g., tokens) to ensure they can be processed independently.

   ![Self-Sufficient Requests](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/179/original/3.png?1725113806)

3. **Avoiding Chatty APIs**:
   - **Misconception**: API endpoints do not need to mirror database tables.
   - **Best Practice**: The API should expose only the necessary data and functionality, possibly involving data transformation within the API layer, without exposing the database structure.
  
4. **Independence of Response Data Types**:
   - **Data Formats**: RESTful APIs typically use JSON and XML, which are standard, easily parsed data formats ensuring interoperability between systems.
   - **Documentation**: Clearly specify the data formats used in your API documentation to avoid confusion.
   - **Alternative Format**: Proto (protocol buffers) is another format, more machine-friendly than human-readable, enabling faster responses.

   ![Proto Format](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/180/original/4.png?1725113824)

---

## FakeStore API

### Introduction & Usage

- **Purpose**: To simulate database interaction when you are not yet proficient in database handling via code.
- **Tool**: We will use [FakeStore API](https://fakestoreapi.com/) as a proxy server.
- **Application**: The API will serve as a placeholder, enabling us to build our product service by calling this third-party API while also preparing to interact with an actual database in the future.

---

## Writing Models for Our Product Service

### Defining Models

- **Purpose**: Models define the structure and relationships of data within your application. For a product service, typical models include:
  - **Product**:
    - Categories
    - Name
    - Description
    - Additional attributes as needed
  - **Category**:
    - ID
    - Name


