## Topics to be Covered

1. **Introduction to Kafka**: Understanding Kafka as a messaging queue system and its role in improving application performance.
2. **Building a Notification System**: We will demonstrate how to implement an account creation notification system that sends a confirmation email asynchronously when a user signs up.
3. **Kafka in Distributed Systems**: Exploring the concept of Kafka producers and consumers, and how Kafka helps manage tasks in high-load environments by decoupling services.



## Kafka

### Overview of Kafka

Kafka is a **distributed messaging system** designed to handle large-scale data streaming and real-time data feeds. It allows services to communicate asynchronously, ensuring that tasks can be processed in parallel without overwhelming the system. Kafka excels in scenarios where many tasks don’t need to be processed immediately, but instead can be queued and handled at a later time.

Kafka is often used in microservice architectures, where different services need to interact with one another but don’t always need immediate responses. It decouples the **producer** (which creates tasks) from the **consumer** (which processes tasks), allowing systems to remain responsive even during peak loads.

### Real-World Example: YouTube Video Uploads

Consider the process of uploading a video to YouTube. When a user uploads a video, several tasks must be completed before the video can be fully processed:
- **Thumbnail generation**
- **Content verification**
- **Copyright checks**

If YouTube were to wait until all these tasks were completed before confirming the upload, it would result in a poor user experience. Instead, YouTube gives the user a confirmation as soon as the video upload is successful and processes the additional tasks asynchronously in the background. This approach enhances user experience by providing an immediate response, while still allowing all the necessary checks to occur.

### E-commerce Example: Flipkart Order Processing

Another example is Flipkart, an e-commerce platform. When a user places an order, several actions are triggered:
1. An **SMS confirmation** is sent.
2. An **email with order details** is dispatched.

During regular times, Flipkart’s servers can handle these tasks easily. However, during large-scale events like **Big Billion Days**, where a huge number of orders are placed simultaneously, the load on the servers increases significantly. Although the order-handling servers are generally scaled to handle this, secondary services such as the email or SMS services may not be able to manage the sudden surge in requests.

One approach to solving this issue is to **scale up** the SMS and email servers, but this can be expensive. A more efficient solution is to delay these secondary tasks by placing them in a **queue**. The queue holds the requests temporarily, allowing the servers to process them later when they are less loaded. This approach allows Flipkart to maintain performance without incurring the costs associated with scaling all services.

### The Problem with the Previous Approach

In traditional systems, every request is processed immediately. However, this leads to several issues:
- **High memory (RAM) consumption**: Processing tasks synchronously consumes significant system resources.
- **Decreased performance**: The system may slow down or crash if too many requests are processed simultaneously.

### Introducing Kafka as a Solution

Kafka offers an improved approach by decoupling task execution from user-facing processes. The key principle is to "Do as little as possible synchronously, and handle the remaining tasks asynchronously." Kafka allows us to process tasks in parallel, after the immediate critical steps (such as saving to the database) are completed.

#### How Kafka Works:
1. A **Kafka Producer** sends events or tasks (e.g., an email request) to a **queue**.
2. The **queue** holds the events until the system has the resources to process them.
3. A **Kafka Consumer** retrieves tasks from the queue and processes them.
4. Once processed, the system sends a response or confirmation back to the user (e.g., an email or SMS confirmation).

In this architecture, Kafka acts as a **black box** that holds and organizes tasks, ensuring that they are processed when appropriate.

![Kafka Workflow](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/812/original/Screenshot_2024-09-07_203725.png?1725721655)

Kafka is used to manage this queue system, ensuring that tasks are processed efficiently and asynchronously.

### Handling Load with Multiple Consumers: The Concept of Consumer Groups

In distributed systems, there may be multiple consumers (e.g., multiple email servers) available to process tasks. Kafka uses the concept of **Consumer Groups** to distribute tasks among these consumers.

#### What is a Consumer Group?

A **Consumer Group** is a group of consumers (instances of a service) that work together to process tasks from a queue. The idea is to balance the load across multiple instances of the same service, so no single instance is overwhelmed.

For example, imagine you have two computers that can help you complete a task. If both computers already have tasks pending, you will choose the one with the least number of pending tasks to minimize the overall completion time. Kafka works similarly, assigning tasks to the least busy consumer within a consumer group.

A **Load Balancer** may also be used to distribute tasks efficiently, ensuring that each instance of a service receives an appropriate amount of work.

---

### Avoiding Direct Database Interaction

A best practice in modern microservice architecture is to avoid having individual services (like an email service) interact directly with the database. Instead, Kafka serves as an intermediary:
1. The service sends a task (event) to Kafka’s queue.
2. The queue processes the event and communicates with the database.

This decoupling improves the scalability and reliability of the system by reducing dependencies between services and the database.

---

### Kafka Producers and Consumers

In Kafka, there are two main roles:
- **Kafka Producer**: A service that generates events and sends them to the Kafka queue. For example, when an order is placed, the **Order Service** sends an event to Kafka to notify the system of the order.
- **Kafka Consumer**: A service that retrieves events from the Kafka queue and processes them. For example, the **Email Service** retrieves the event from Kafka and sends an email to the customer.

This decoupled architecture allows for efficient, asynchronous processing of tasks across multiple services.

![Service Interaction in Kafka](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/924/original/Screenshot_2024-09-09_073854.png?1725847761)

In the above diagram, the Order Service and SMS Service act as Kafka producers, while the Email Service acts as a Kafka consumer.

### Real-World Application of Kafka

In real-world scenarios, we often do not build Kafka from scratch but use **managed Kafka services** such as **AWS Kafka**. These services handle the complexities of scaling, managing, and operating Kafka, allowing developers to focus on building business logic.

---

### JSON Object Handling in Kafka

Kafka communicates using **JSON objects** to exchange data. In **Spring** applications, the **Jackson library** is commonly used to convert objects into JSON format, which Kafka can then process. This allows different services to send and receive data in a structured format, ensuring compatibility and ease of integration.

![Kafka Example](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/926/original/Screenshot_2024-09-09_075358.png?1725848650)

---

### Email Notification Service Example

One common use case of Kafka is to implement an **email notification service**. When a user signs up on a platform:
1. An event is sent to Kafka by the **Sign-Up Service** (Kafka Producer).
2. Kafka stores the event in a queue.
3. The **Email Service** (Kafka Consumer) retrieves the event from the queue and sends an email to the user.

For more details on sending emails using the **SMTP protocol**, you can refer to [this tutorial on sending mail in Java](https://www.digitalocean.com/community/tutorials/javamail-example-send-mail-in-java-smtp).

![Email Notification Process](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/927/original/Screenshot_2024-09-09_081552.png?1725849992)

 The provided [GitHub repository](https://github.com/Naman-Bhalla/emailServiceMWFEve) can be used as a reference for setting up this email service.

