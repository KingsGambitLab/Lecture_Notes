## Topics to be covered
1. How search APIs are typically implemented in real-world applications
2. Understanding and implementing paging in search APIs
3. How sorting enhances search results, and its implementation
4. Introduction to ElasticSearch and its use in scaling search functionality for large datasets

---

## Search API Implementation

### Overview

Search APIs are fundamental in modern applications, especially in domains like e-commerce, where users search through extensive product catalogs. The implementation of these APIs requires handling large and complex queries efficiently, often involving filters, sorting, and pagination. Typically, **POST** APIs are used for search operations due to their ability to handle larger and more complex data structures compared to **GET** APIs.

### Why Use POST Instead of GET for Search?

When implementing a search API, you will often see **POST** being used rather than **GET**. This is due to the nature of the data being sent and how the HTTP protocol handles this data.

- **GET requests** do not have a body, and all parameters must be passed via the URL. This means that you are limited by the length of the URL (around 2000 characters, depending on the browser), which is not ideal for complex search queries.
- **POST requests**, on the other hand, allow for a request body, making them capable of sending complex, large data structures, including nested filters, sort parameters, and pagination controls.

**Scenario Example**:  
Imagine an e-commerce site where a user wants to search for products with multiple filters such as category, price range, brand, and review ratings. Such a query can quickly grow beyond what can be reasonably placed in a URL. This is where **POST** becomes the better choice.

**Question :** Why is POST preferred over GET for search APIs?  
**Answer :** GET has a limitation on URL size, making it unsuitable for sending large or complex queries. In contrast, POST allows sending detailed query parameters in the request body.

**Visual Aid**:  
- **GET vs POST Request Differences**
  ![image](https://hackmd.io/_uploads/Sy7hVh5dT.png)

### Pros and Cons of GET vs POST

Both **GET** and **POST** methods have their advantages depending on the context.

- **GET**:  
  - Use when the query is simple and the URL needs to be shareable/bookmarked.
  - Useful for idempotent operations, where the request doesn't alter the state of data.
  - Example: If a user needs to share a link that returns the same result every time it's accessed.

- **POST**:  
  - Ideal for complex queries that can't fit into the URL.
  - Allows sending data in the body, making it suitable for large data inputs.
  - Example: A search query with multiple filters and complex parameters.

**Summary**:  
Use **GET** for simple, shareable queries, and **POST** for more complex operations where data needs to be passed in the body. The choice depends on the use case, and there is no one-size-fits-all solution.

**Visual Summary**:
- **Trade-offs Between GET and POST**
  ![image](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/667/original/1.png?1725529536)

---

## Paging

### Understanding the Concept of Pagination

In web applications, especially those dealing with large datasets, it is inefficient and unnecessary to load all data at once. Instead, **pagination** allows us to fetch a subset of data at a time. This process of dividing data into discrete "pages" improves performance and user experience by reducing the amount of data transferred and displayed at any given time.

### Why Pagination is Important

When an API call returns large amounts of data, fetching it all in one request has several downsides:

1. **Slow API Response**: Transmitting a large dataset increases the time it takes for the API to respond, leading to a poor user experience.
2. **Unnecessary Data Transfer**: Fetching all data when only a portion is needed leads to wasted bandwidth and processing power.

With **pagination**, we control how much data is fetched and displayed at a time, usually through parameters like `pageNo` and `pageSize`.

#### How Pagination Works:

Pagination typically works by:
1. Sending a request with `pageNo` (the current page number) and `pageSize` (the number of records per page).
2. The server responds with a subset of data for that page.

For example:
- Request: `pageNo = 2`, `pageSize = 10`
- Response: The server returns 10 records from the second page (records 11–20).

**Visual Aid**:  
- **Flow of Pagination**
  ![image](https://hackmd.io/_uploads/S16Lq6cuT.png)

This structure not only optimizes performance but also improves the overall efficiency of data retrieval, ensuring that users are only exposed to manageable chunks of information at a time.

### Detailed Implementation of Pagination in Product Service

To implement pagination in a service like product search, we use the **Pageable** class, which helps structure how the API handles page numbers and sizes.

1. **Pageable Interface**:  
This interface defines methods for pagination parameters such as page number and page size.

```java
public interface Pageable {
    int getPageNumber();  // Current page number
    int getPageSize();    // Size of each page
    Sort getSort();       // Sorting parameters, if any
}
```

2. **SearchController**:  
Here is how the `SearchController` can manage search queries with pagination.

```java
@PostMapping
public Page<GenericProductDto> searchProducts(@RequestBody SearchProductDto searchProductDto){
    return searchService.searchProducts(searchProductDto.getQuery(), searchProductDto.getPageNumber(), searchProductDto.getSizeOfEachPage());
}
```

3. **Search Service Implementation**:  
In the service layer, we fetch products based on the search query and pagination parameters.

```java
public Page<GenericProductDto> searchProducts(String query, int PageNumber, int SizeofEachPage){
    Page<Product> productPage = productRepository.findAllByTitleContaining(query, PageRequest.of(PageNumber, SizeofEachPage));
    List<Product> products = productPage.get().collect(Collectors.toList());
    List<GenericProductDto> productDtos = products.stream()
                                                   .map(GenericProductDto::from)
                                                   .collect(Collectors.toList());

    return new PageImpl<>(productDtos, productPage.getPageable(), productPage.getTotalElements());
}
```

This method provides a paginated response based on the requested page number and size, improving both performance and usability.

**Note**:  
The provided code is a demonstration of how pagination works. You are encouraged to implement the full flow yourself for deeper understanding.

**Example in Practice**:  
- **Pagination in Real-Life Applications**
  ![image](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/668/original/2.png?1725529586)

---

## Sorting

### Introduction to Sorting

Sorting is another essential feature in search APIs that allows users to organize data based on various attributes such as price, rating, or date. Sorting makes it easier for users to find what they are looking for by controlling the order in which data is presented.

#### How Sorting Works

1. Fetch all the data related to a query.
2. Sort the data according to specified parameters (e.g., price descending, rating ascending).
3. Return the data in a paginated, sorted format.

Sorting ensures that users can, for example, view products from the lowest to the highest price or from the highest-rated to the lowest-rated.

### Sorting Implementation in Product Service

Sorting is implemented by adding an additional parameter to the search request—**sortByParameters**—that defines the sorting criteria.

1. **Search Service with Sorting**:  
The service class now handles sorting by fetching products and ordering them based on user-defined parameters.

```java
public Page<GenericProductDto> searchProducts(String query, int PageNumber, int SizeofEachPage, List<String> sortByParameters){
    Sort sort = Sort.by(sortByParameters.get(0));  // Start with the first sort parameter
    for (int i = 1; i < sortByParameters.size(); i++) {
        sort = sort.and(Sort.by(sortByParameters.get(i)));  // Chain additional sort parameters
    }

    Page<Product> productPage = productRepository.findAllByTitleContaining(query, PageRequest.of(PageNumber, SizeofEachPage).withSort(sort));
    List<Product> products = productPage.get().collect(Collectors.toList());
    List<GenericProductDto> productDtos = products.stream()
                                                   .map(GenericProductDto::from)
                                                   .collect(Collectors.toList());

    return new PageImpl<>(productDtos, productPage.getPageable(), productPage.getTotalElements());
}
```

In this example, we allow multiple sorting criteria to be specified by chaining `Sort` methods, making the service flexible to handle complex sorting needs.

2. **SearchController Update**:  
The `SearchController` is updated to include sorting parameters in the request body.

```java
@PostMapping
public Page<GenericProductDto> searchProducts(@RequestBody SearchProductDto searchProductDto){
    return searchService.searchProducts(searchProductDto.getQuery(), searchProductDto.getPageNumber(), searchProductDto.getSizeOfEachPage(), searchProductDto.getSortBy());
}
```

**Optimization Tip**:  
To avoid hardcoding the sorting parameters, dynamically build the `Sort` object based on the input list. This allows for greater flexibility and scalability.

**Code Optimization**:

```java
Sort sort = Sort.by(sortByParameters.get

(0));  // Use the first parameter to start
for (int i = 1; i < sortByParameters.size(); i++) {
    sort = sort.and(Sort.by(sortByParameters.get(i)));  // Add subsequent sorting fields
}
```

---

## ElasticSearch

### Introduction to ElasticSearch

So far, we've implemented basic searching, sorting, and pagination. However, as datasets grow in size and complexity—especially in large-scale applications like e-commerce websites—traditional SQL-based search can become inefficient. Enter **ElasticSearch**, a distributed search engine that provides fast and scalable full-text search functionality.

#### Why ElasticSearch?

**Consider an example :**
A user searches for "Pan 5kg" on an e-commerce site. However, the product title only contains "Pan" without mentioning "5kg." Using a traditional SQL query, finding this product based on the "5kg" keyword would be challenging and inefficient, especially when scaling to millions of products.

ElasticSearch solves this problem by indexing data in a way that allows for complex, full-text search operations across multiple fields (e.g., title, description, specifications) quickly and efficiently.

### What is ElasticSearch?

ElasticSearch is:
- **Distributed**: Designed to scale across multiple servers.
- **RESTful**: It can be queried using standard HTTP requests.
- **Optimized for search**: Specifically built for handling large-scale search workloads.

### AWS OpenSearch: ElasticSearch as a Service

In real-world applications, ElasticSearch can be deployed using **AWS OpenSearch**, which is a managed service provided by AWS for setting up and running ElasticSearch.

- OpenSearch is to ElasticSearch what RDS is to MySQL—an AWS-managed version of an open-source technology.
- You can deploy OpenSearch on AWS and integrate it into your application for fast and efficient search capabilities.

### Implementing ElasticSearch

To integrate ElasticSearch into your Java application, you can use **spring-data-elasticsearch**. This Spring Data module allows seamless interaction with ElasticSearch.

1. **Set Up OpenSearch in AWS**:  
   Deploy and configure OpenSearch in AWS for your application.
   
2. **Spring Data ElasticSearch**:  
   Add the **spring-data-elasticsearch** dependency to your project.

   Example setup and implementation: [Baeldung ElasticSearch Tutorial](https://www.baeldung.com/spring-data-elasticsearch-tutorial).

**Key Features of ElasticSearch**:
- **Full-text search**: Search across multiple fields (e.g., product descriptions) for a more flexible search experience.
- **Speed**: Designed for fast query execution even with large datasets.
- **Scalability**: Can handle massive amounts of data spread across multiple servers.

ElasticSearch is the preferred choice for large-scale, production-level search operations due to its efficiency and flexibility.
