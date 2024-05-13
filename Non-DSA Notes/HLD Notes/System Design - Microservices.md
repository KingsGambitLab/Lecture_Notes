
---
title: Introduction to the Microservices and agenda of session.
description: 
duration: 180 
card_type: cue_card
---


## Agenda 
* Monolith
    * Advantages and disadvantages
* Microservices 
    * Advantages
    * Communication among the services 
    * Distributed transactions(SAGA Pattern)
    * Drawbacks
* When to use what?



---
title: Starting with the Shipkart example.
description: 
duration: 300 
card_type: cue_card
---


**Optional**
Give any interesting anecdotes of working with the microservice, monolith, or the migration from one to another.

## Shipkart Example :- 
Imagine In the year 2000, there was an entrepreneur named Sachin who started his own e-commerce company called Shipkart.com. In this lecture, we will follow his journey over 15 years, examining the evolution of his company's systems.

He needs some software to host his company’s frontend and backend.

**Ask students:**
What Sachin will need, even before hosting the frontend and backend for his company.
**Ans**: Domain name.

#### Open questions
**What all modules(Services) will be needed?**
Classify student answers into:
* Primary services - Catalog Module, Search Module
* Secondary services - User feedback etc.

Basic modules(services) to start the e-commerce
* Catalog Module
* Search Module
* Cart Module
* Orders Module
* Payments Module
* Notifications Module
* Logistics management services Module - Shipment, returns, tracking
* User module
* Merchant Module

This is how we used to design back in the 2000s. We will start from there and then progress forward.

---
title: Phase 1 of the shipkart website.
description: 
duration: 300 
card_type: cue_card
---

## Phase 1
Sachin is currently in the Proof Of concept or explore(Ideation) phase. He is an engineer, and plans to hire interns to launch as fast as he can.
  
Sachin started with one big service in which he has
* Catalog Module
* Search Module
* Cart Module
* Orders Module
* Payments Module
* Notifications Module
* Logistics management services Module - Shipment, returns, tracking
* User module
* Merchant Module

### Ruby on Rails
Generally, when we want to launch very fast, we choose ROR(Ruby on Rails)
ROR is 
* Very fast for initial load
* Simple
* Vast framework support

**Optional fun fact**
* Even scaler uses Ruby on Rails currently
* When Swiggy started, they initially used WordPress, treating each order as a WordPress blog for managing their database. However, due to their small codebase, they migrated easily.

### Open source e-commerce framework
* Spree commerce
    * Built on Ruby on Rails
    * It is extensible
    * It gives us classes in ROR, which can be changed in the future.

### Other popular e commerce framework
* ATG
* Magento - uses PHP, used by Lenskart 

---
title: Initial system of Shipkart.
description: 
duration: 300 
card_type: cue_card
---

## Initial system of Shipkart
Let’s say Sachin built this system, maybe using spree or by himself. And, we call this the initial architecture of ShipKart. In the real world this is the architecture of Urban Ladder.

![](https://hackmd.io/_uploads/BJeIS30A2.png)

This allowed us for quick launch, it has three main components
* Business logic 
* Database layer 
* Ui layer 

Generally all three are **tightly coupled togethe**r, and in the above example all the goals that Sachin wanted to fulfill were met.
* Launch fast
* Iterate fast
* Less time to market


---
title: Phase 2 of Shipkart.
description: 
duration: 300 
card_type: cue_card
---
## Phase 2
Imagine the year is 2005, and Shipkart is growing.
Let’s say in 2000 they had 2 orders a day, now they have 2000 orders in a day.
The team is bigger now, They've done some custom coding for some features, thus have some custom code on spree.

![](https://hackmd.io/_uploads/HJy_Sn002.png)

Now, in the above system in which everything was together, it is becoming difficult to manage.

Also, we can consider that, the max capacity of the system was 2000 orders a day but now sachin wants to scale more.

 
**Open Question**
**How can we help sachin to further scale this system?**
assuming we have at least 5-10 developers.
**Ans**. Now, the bottleneck will be hardware, 
So, the journey of horizontal scaling starts.

---
title: Introduction of load balancer.
description: 
duration: 300 
card_type: cue_card
---
### Introduction of load balancer
We will start with the introduction of a load balancer.

So, it’s 2005 and this is how their system looks after modifications.
![](https://hackmd.io/_uploads/Sk7oSn0An.png)

* Whenever a request comes to the server it goes to the load balancer.
* So the static public IP is now the IP of the load balancer, the load balancer receives the request.
* Since, we have horizontally scaled the system,we have three application servers, which are replicas, and all the three individual machines are stateless.
* The load  balancer will do the round robin scheduling, which means that we now have three application servers.
* And all of them are talking to one DB.

We can have one more optimisation here 
* We can use secondary DB's.
* These replicas can serve some of my secondary reads, and also power my ETL pipelines.


---
title: Example of how a monolith processes request.
description: 
duration: 300 
card_type: cue_card
---
### Explain
Below picture is a perfect example of monolith.
* We have everything in  one language.
* We have one database.
* All the catalog are tightly coupled.

![](https://hackmd.io/_uploads/SJYuOh0An.png)


### Example of how a monolith processes request.
Let's say we are searching for something-
* The request  will go directly from search to cart directly, because all these are in one system, and a simple procedure call (SPC) will happen. 


---
title: Benefits and the best scenerios of using Monolith.
description: 
duration: 300 
card_type: cue_card
---

### Benefits of using monolith approach
* Ease of development & monitoring.
* Ease of doing end to end testing.
* Ability to do more with a small team.
* Less time to market.
* For initital stages this is very cost-effective.
* Easy to scale.


### So we should always start with Monolith?
**Answer** - 
* Yes, unless we have a plethora of resources specifically time, we should always start with monoliths.
*  In most of cases, the objective is to launch products in the market ASAP, and reach product market fit. In these cases monoliths are best.
* Only for companies which are established and have a certain scale, it is beneficial to go with Microservices first approach.

---
title: Phase 3 of Shipkart.
description: 
duration: 180 
card_type: cue_card
---

## Phase 3
Consider, the current year is 2015-
* Shipkart is now biggest ecommerce website in India.
* There are more than 500 developers in the team.
* Orders have increased from 2000/day to 2000 orders/minutes.
* The Spree codebase has become huge, A lot of complex code has creeped into it.
* The code is currently running on a large number of machines, let’s say 300 machines.

![](https://hackmd.io/_uploads/ByNy8C00h.png)

So, this above system is currently being run on 300 machines -
* In case of any deployment, all changes need to be deployed to all the 300 machines.
* In another case, imagine a new developer comes in. He needs to understand spree and all the modules. To ensure that a change in any module shouldn’t break anything in other modules, because all the modules are tightly coupled.

---
title: Drawbacks of Monolithic systems and its formal definition.
description: 
duration: 300 
card_type: cue_card
---
## Issues with current setup
* Maintenance is hard
* Deployment takes a lot of changes 
* It is hard to do end to end testing.
* Codebase is becoming huge and complex. 
* Binary files becomes huge overtime.
* Even for deploying change in one module, the  entire system is down.

### Drawbacks of Monolith
* Developer onboarding is difficult, because they need to get understanding of each and everything.
* Making change is hard(difficult E2E testing, and cascading failures).
* Independent scalability of services is not possible. 
* Scaling the sysytem is very expensive.
* Including new technology is hard, and the system becomes less adaptive to new technologies.
* It is hard to use use-case specific best technology for individual modules.
* It slowly turns into a Big ball of mud, over the time. As, there is no one who has end to end understanding of the system.
* Bug fixing takes a lot of time
* Slow startup time
* Lots of binaries need to be loaded.
* Deployment are extremely slow


## Formal definition of monolithic function
It is system where your codebase, business logic and database layer, are interconnected and dependent on each other.

---
title: Migration from Monolithic to Microservices.
description: 
duration: 600 
card_type: cue_card
---
In phase 3, our code base is extremely large, so we need to trim it.

**Open question**

### How do you think we can move this system from monolithic to microservices?**
### What should be criteria or basis of trimming this monolith?**
Discuss the various answers given by students.

## Should we deploy all the modules seperately?
While starting with microservices, the initial thought might be to start deploying all the modules in separate services.
But it would only create more issues. Because, even for a simple case in the above example, we will have to deploy 9 different service on 9 different machines.

### Business logic in microservices
* One important thing about microservices is that it should have a business logic unit.
* It should be independently deployable, have its own database.

---
title: Deploying the notification module as a microservice.
description: 
duration: 600 
card_type: cue_card
---

## The journey from monolith to microservices
Let’s discuss the journey from monolith to microservices using Shipkart example.
Now, sachin has good architects,
* These architects were smart enough to figure out that we can platformise the notification service. 
* That any service in the world can use my notification as a service to send notifications.
* Even the database for notification is not dependent on any one.
    * We can have a data model 

| UserID | NotificationId |
| -------- | -------- |

If user is a global entity in my system, and we take the following table out of the Monolithic system, and deploy it as a separate service, we will still be left with userID.
 
| UserID | NotificationId |
| -------- | -------- |


## Deploying Notification service as seperate service
So the first candidate that could be taken out of that monolith and deployed as a service would be Notification service.

And then We can proxy whatever request was going to notification module to the notification microservice.


---
title: Criteria for a module to be picked as a microservice.
description: 
duration: 600 
card_type: cue_card
---
### Criteria for a module to be picked as a microservice
Generally, while picking which modules can be converted into a microservices we check the following parameters-
* Should be an independent module.
* That module should be under a certain scale. So, that once we separate it out,we reduce the scale of monolithic application, as it will used by a lot of services internally.

If you think about notification- 
* Whenever we do payment it returns notification.
* Whenever a refund is there it returns notification. 
* For most of the things there will a notification triggered. 


### How to find out what all modules are under heavy load.
Step 1 : rest API analysis
Step 2 : which modules are under heavy loads
Step 3 : Choose which are easy to separate.

### Making user a microservice
Let's say in Shipkart authentication is inbuilt in user module, and for authorisation all the other services are talking with the user service and it is under very heavy load.
So, we can make user as a global microservices, and for any transaction we can just retain userId.
Also, most of the companies always pick user service to be separated as a microservices.

---
title: Seperating the DB for user service.
description: 
duration: 600 
card_type: cue_card
---
### Seperating the DB for user service
Currently in the monolith of Shipkart 
If a user logs in, and he is trying to get his previous orders.
We will have an order table something like this

![](https://hackmd.io/_uploads/SJL1uzJJT.png)
 
And similarly cart table had all products etc. 
Now, in this order table, the userID is a foreign key
* And whenever we would fetch the orders for an user, we would be unnecessarly fetching the user object, because userId is currently a foreign key.
* So, we can remove this foreign key constraint, by moving this user table to separate database, but the userid is still same.
* Now, whenever we want to fetch the details we will call this API,

Now, we can have all of our apps here 
* Order
* Search etc.
But the source of user data is now a separate service with it’s own DB.
And also Notifications will be a separate service with it’s own DB.

**Additional Benefits**
* We can also have smaller teams for these services


**Open questions** 
**Is getting user details from other machines costlier than joins?**
**Ans** Yes, it might be but we won't need this info all the time. We won't be required to know user details at all for most of the operation, userId would be enough.



## Example of Myntra
Imagine you open your app, you are already logged in, and you want your previous order details.

Now, myntra already have your userId, and knows who is the user.
And, also there is a table with all the orders and userId as a column.

When myntra talks with backend, let’s say using an API
* getOrders(userId)
Now we'll just go to the order details table, which has order details with userId, and i need to use a where clause on UserID.
This way, I don’t need to interact with the user microservice at all.

* By separating the user service to a different DB and a different service, we have simplified codebase.

* And if we onboard someone for user services, he can join and take a understanding of the user service and need not to understand the order service.

After first iteration 
The following could be in one microservice
* Catalog Module
* Search Module
* Cart Module
* Orders Module
* Payments Module
* Logistics management services Module - Shipment, returns, tracking
* Merchant Module



And the user and notification are seperated out

After certain iterations of the carving out microservices/migrations.

The Shipkart would be something like this

![](https://hackmd.io/_uploads/Bynkqgb16.png)


Now all the modules are separated and all modules have their own DB.

---
title: Benefit of microservice arrangement.
description: 
duration: 600 
card_type: cue_card
---
### Benefit of microservice arrangement 
For example
* Let’s say in the catalog, there could be columns which are applicable only on certain products and not all products.
    * Like fabric for deodorants, or fragrance for shoes.
    * These irrelevant fields are still there, adding redundancy to the system
    * Now we can use Mongodb instead of MySQL in catalog. We can remove those redundant column.
* Similarly, for the search microservice we can use elastic search 
* For orders microservice we can use MySQL.
* For cart microservice we can use cassandra.
* For Payment microservice we can user MySQL, as we need high guarantee on transactions.
* User microservice can also be in MySQL
* Notification microservice can be kept in MySQL or anything

---
title: Managing the load on all the microservices.
description: 
duration: 600 
card_type: cue_card
---
But after some point in time. 
* All these microservices are separately deployed,
* Imagine a request comes to load balancer from a Desktop/Mobile.
* Therequest could be get order/Search/addtoCart, 
* Earlier the machine was one, there was one dispatcher and it knew all the controllers, Now there are different services , and when a request comes, 

### How would load balancer know, where to route this request. Or which this request should be sent?


How can Loadbalancer identify where it can send the request?
**Ans** - You should have request routing. 
* Basically we will need API <> Services mapping. And for this we would need an API gateway.
* API gateway is essentially a public facing service in which whenever the call comes to load balancer, it sends it to API gateway, then API gateway read the request header,and based on mapping it will route the request.

All the sessions will now be stored in the API gateway.

Flowchart -
![](https://hackmd.io/_uploads/SJH6igby6.png)


There are two Networks, provided by AWS
* Public Vritual private cloud
* Private Vritual private cloud

* Public VPC, can interact with the internet.
* In Private VPC, machines can interact among themselves.
* And only way to interact with machines in Private VPC to internet is via Public VPC.

---
title: Could the load balancer be a bottleneck? and Benefits of a microservices over Monolith.
description: 
duration: 300 
card_type: cue_card
---
### Could the load balancer be a bottleneck?
Generally the Logic in a LB is very simple, and they are a combination of machines, not just a single machine, thus there are little chances of it being the bottleneck.

### Benefits of a microservices over Monolith
* Independent components.
* Better fault isolation - Non cascading failures.
* Ease of adding new features & deployment.
* Selective Scalability for any specific microservice.
* Tech stack selection could be better depending on the use-case of microservice.
* Developer on-boarding is easy, as we can have smaller teams with clear ownership of a particular microservice.
* Easier detection of bugs

---
title: Communication among microservices.
description: 
duration: 300 
card_type: cue_card
---
**When we are designing microservices in a very big company with 100s of microservices. How these services communicate with each other?**
**Ans**. Rest API -
* Services can call other services API.

Now the problem is that there could be issues with understanding the structure of other API, which might also be in another language.
And, even if we are doing it manually for some services. It won't be possible to do it if we have more 20 services.

* So we might ease it with clients structure. 
* All the services will publish their client in different languages, and these client will have various required methods.
* The other service needs to import the client and call the method to use that microservice.

But Even then we will have to write client in so many different languages, for all the services.

---
title: Better way of for microservices to communicate among each other.
description: 
duration: 300 
card_type: cue_card
---
How these services communicate with each other?
* One format we generally use for communication is Json format.
*  When Json data is sent over a network, It get serialized.
*  And when request finally reaches destination, it gets deserialized.

* But, When there are too many services, this serialization and deserialization becomes very heavy operation. 
* Also the JSON is schemaless, which makes the deserialisation more inefficient.

One solution to this is 
## RPC - Remote procedure call
* It works on binary DATA. 
* Instead of JSON it uses Protobuf, which is a binary data transfer schema.
* For example, There is GRPC which is basically Google’s RPC.


In this system, when A has to send data. It converts the data into binary, and sends it to A’s OS. 
Since we have 7 layers in the OSI model and, Rest works in the Application layer, it is slightly slower than the RPC which works in the transport layer.
 	
So B’s OS finds it in the transport layer, it finds the method in the machine and invokes it.


## How Protobuf is solving the problem
JSON was schemaless, but proto has a fixed schema, even though we have to change the protobuf whenever we are changing requests. It is very fast because servers already know what to expect unlike JSON, where we have to go through key by key to find the mapping with the object.
But, here we just need to compile the protobuf.

**Good to know -** 
We can also use Protobufs in Rest.

---
title: Optimal way of for microservices to communicate among each other.
description: 
duration: 300 
card_type: cue_card
---
## Events
It is the most flexible and popular way of communication in microservices.
Let’s suppose we have a machine A, and it has to interact with other machines, and it does some code changes for smooth interactions.
Now, whenever there are new machines, we will need more changes again and again.

Let's say A is the order service, and whenever there is an order 
* It needs to tell invoice service to generate invoice, 
* Payment service to initiate payment etc.

* But, what if A could just create an event, Let’s say orderCreated and put it into a queue. 
* Now, Whoever wants to do an action on this can subscribe to it. Invoice service can be a consumer, payment service can be another consumer.
* Now even if there are 100 new consumers of this event from A, they can just subscribe to this queue, and get the communication, rather than A doing code changes to communicate with all of them.


[Summarising](https://www.youtube.com/watch?v=V_oxbj-a1wQ )
![](https://hackmd.io/_uploads/SkH9LZ-J6.png)


---
title: Transactions in microservices.
description: 
duration: 300 
card_type: cue_card
---

## Transactions in microservices
### Distributed transactions
* Saga Pattern

![](https://hackmd.io/_uploads/rJojdW-ya.png)

Now, when a client places an order, 
* The order comes to order service.
* From order service to Payment service.
* It will share the payment status with order service.
* If payment is successful, Then order service tells the restaurant to accept the order.
* Order service tells the delivery service to assign a delivery boy.
* And all of this is updated in the Database.

In Monoliths all of this is being done in one simple system, 
And benefits of these are 
* These transactions can be done easily.
* If the transaction fails at any point of time roll back happens.
* All of this is very easy because everything is in one codebase, and in single application.


But once we move to a distributed environment -
 
**There is a saga pattern which gives us some guidelines on how to do transactions.**
There are two ways of implementing saga pattern
1. Orchestration
1. Choreography


---
title: Implementing SAGA Pattern using Orchestration.
description: 
duration: 300 
card_type: cue_card
---

## Implementing SAGA Pattern using Orchestration
![](https://hackmd.io/_uploads/rkYDFW-yp.png)


* Order service will publish an event to a queue, Let’s say **order created**.
* Payment service is listening to this event.
* Payment service Consumes the event and initiates the payment.
* Payment service will then publish an event **payment completed**, which will be listened to by the order service.
* Order service will publish another event **payment completed** Meanwhile the order status will keep changing in the order service.
* Payment completed is listened by the restaurant service.
* And restaurant service publishes an event **order accepted** which is listened by the order service.
* Order service publishes event **order accepted**, which is listened to by delivery service.
* Delivery service assigns a delivery boy, and publishes another event **delivery boy assigned**, which is listened by the order service

If we look at this, the knowledge of the transaction is only with the order service. 
It knows the flow the events
Which event i need to look for and after that we event i need to trigger.

In this setup for transactions, the order service is the **orchestrator**.
* Instead of talking to one another, all the services are talking to the order service.
* It is orchestrating the transaction, and taking care of the step by step process.
* In this case the orchestrator could either be an order service or any other service as well.
* The Orchestrator will talk to all other services, and takes care of the transaction.
* Role of the orchestrator is important in scenarios when you want very fine control of the transaction.


Orchestrator approach is not very common, commonly we use choreography.

---
title: Implementing SAGA Pattern using Choreography.
description: 
duration: 300 
card_type: cue_card
---
## Implementing SAGA Pattern using Choreography
In choreography, there is no central point that controls the transaction, in this we have a queue, and everything is completely event driven.

We all have heard, and event driven systems have becomes popular recently, these are based on choreography.

Let’s look at the choreography for the same case-
![](https://hackmd.io/_uploads/Hkm4UUW1p.png)

### Sequence of events
* Whenever a request comes to order service, the order service creates an order, and publishes an event called **order created**.
* This event goes to a topic called orders, and this event is consumed by payment service.
* The payment service will have the logic on what to do with this event.
* Payment service knows that on receiving an **order created** event it needs to initiate payment, it initiates payment by communicating with payment gateway. 
* Once the payment is successful, payment service publishes event **payment successful**.
* Now, restaurant service is listening to this topic, let’s call this **payment topic**.
* Restaurant service is listening to this topic, and on getting this event it talks with restaurant to accept the order.
* If the order is accepted, the restaurant service will publish the event **order accepted** in another queue.
* Now the delivery service will listen to the **order accepted** event, and assign a delivery boy.
If you observe, there is no single point controlling the transaction, it is happening event by event. And we can say that the queue is the choreographer.

---
title: Rollbacks in distributed transactions.
description: 
duration: 300 
card_type: cue_card
---
## Rollbacks 
### Rollbacks in distributed transactions
1. Publishing negating events/ compensating transactions
    1. Compensating transactions can be defined only for known failures
    1. Eg, payment failed, restaurant rejects order 
1. Self compensating order
    1. Example, For the restaurant accepting the order We will have a monitor, which will run for a designated time, and if the restaurant fails to accept the order within it, it will return the compensation event **order rejected**. And if a certain number of orders get rejected, the restaurant will be blacklisted for the day, as they might have closed but forgot to update.
    1. Another example, let say the assigned delivery hasn’t moved for 10 mins, then it would be better if we assign a new delivery boy.


---
title: Best cases to use Monolith or Microservices.
description: 
duration: 300 
card_type: cue_card
---
**Open question** 
* What are the drawbacks of microservices?
    * Heavy devops effort
    * Complex monitoring, distributed tracing of request
        * A library used for this is Spring sleuth, it adds a request id to your request and using this requestId you can track your request across the services
    * Expertise in sysytem architect.
    * Latency may increase, due to heavy network ops

### When to use Monolith?
* Small team
* A simple application 
* No microservice expertise
* Quick launch

### When to use microservice?
* Complex business logic
* Tight coupling
* Huge scale
* Have expertise
* bandwidth(Huge engineering+Devops team)
