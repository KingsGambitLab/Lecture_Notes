
---
title: Recap of previous lecture..
description: A brief summary of the previous lecture.
duration: 300 
card_type: cue_card
---

In the last class, we learned that when we type something on the browser( or search for a website specifically), the first thing browser has to do is talk to a DNS and figure out which IP address the browser should be talking to, and it communicates with the machine at that particular IP. 

And when you go from one machine to multiple machines, you need a load balancer to distribute traffic uniformly, but after a point when the amount of information cannot fit into a single machine, then the model needs to shard. It can be done using consistent hashing.

---
title: Issues in storing code and database on the same machine.
description: Discussing decoupling of code and storage, but its downsides as well.
duration: 300 
card_type: cue_card
---

However, the machines had both the code and storage in the previous model. **Do you think it is a good model?**



![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/549/original/Screenshot_2023-09-20_184326.png?1695215831)




It's not, the reasons being:

* Code and database are tightly coupled, and code deployments cause unavailability.
* Fewer resources are available for the code since the database will also use some of the resources.

So it is better to decouple code and storage. However, the only downside of decoupling is the additional latency of going from one machine to another (code to the database).

---
title: Introduction to the Application server.
description: Establishing the need of an application understanding it’s working.
duration: 300 
card_type: cue_card
---
So it can be concluded that it is not ideal for storing code and database on the same machine. The approach is to separate the code and storage parts to increase efficiency. 

Different machines storing the same code running simultaneously are called **Application Server** Machines or App Servers. Since they don't store data and only have code parts, they are stateless and easily scalable machines.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/550/original/Screenshot_2023-09-20_184333.png?1695215853)


---
title: Introduction to caching.
description: Explaining what is caching and list its types, which we will cover individually in upcoming sections.
duration: 300 
card_type: cue_card
---

## Caching

The process of storing things closer to you or in a faster storage system so that you can get them very fast can be termed caching. 
Caching happens at different places. The first place we start caching is the browser. Browser stores/caches things that you need to access frequently. Now let’s look at different levels of caching.

### Types of caching -
1. In-Browser caching
2. CDN ( Content Delivery Network)
3. Local Caching
4. Global Caching

---
title: In-Browser caching and CDN.
description: Discussing the In-Browser caching and CDN.
duration: 600 
card_type: cue_card
---

## 1: In-Browser caching
We can cache some IPs so that browser doesn't need to communicate with the DNS server every time to get the same IP address. This caching is done of smaller entries that are likely not to change very often and is called in-browser hashing. Browser caches DNS and static information like images, videos, and JavaScript files. This is why a website takes time to load for the first time but loads quickly because the browser caches the information.

How does browser know if IP on DNS has changed? Short answer, it does not. 
Then, how can it remain in sync? 

1. TTL (Time to live): I only store entries with an expiry time (let's say valid for the next 30 mins). So, post 30 mins, browser will re-fetch when entry is asked for. 
2. Incase of IP caching, if the access to IP fails, it can invalidate the entry, so that on retry, we try with DNS again for IP (incase it has changed). 

---
title: CDN.
description: Discussing the In-Browser caching and CDN.
duration: 600 
card_type: cue_card
---

## 2: CDN ( Content Delivery Network)

What happens when you try to load any website including del.icio.us? You will send a request and then get back in response a HTML file, some JS files, and the webpage could have some media files (images/videos). 

Now, imagine you have the browser in some region(say India), and you must fetch the files from the servers located in another region(say the US). When you try to access from your browser, a request is made to the load balancer, and then it goes to the application server and requests files from the file storage. You know that transferring files and other data will be fast for the machines in the same region. But it can take time for machines located on different continents. 

From the website perspective, users worldwide should have a good experience, and these separate regions act as a hindrance. So what’s the solution?

The solution for the problem is CDN, Continent Delivery Network. Examples of CDN are companies like

* Akamai
* Cloudflare
* CloudFront by Amazon
* Fastly

These companies' primary job is to have machines worldwide, in every region. They basically store files and return a corresponding URL. 

So, when you load a webpage, following happens:
 - HTML code is returned to you. You will see skeleton of the pages. 
 - All images and videos have source as CDN url and are fetched async. 
```html
  <img src="{{cdn_url}}" ...> </img>
```
  Very similar thing for JS file or any file to be fetched from CDN. 
 - So your browser first loads the HTML, renders the skeletons, and in the background sends request to CDNs to download the images or videos or JS files.  
  
Ok, 2 more questions then:
 - CDN machines are present all over the world. How do I reach the closest CDN machine? 
This is achieved through ANYCAST. Please read more about it post the class on Anycast (https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/) . 

  - All of this is great. But how is the flow? Basically, how are images uploaded on CDN? How is CDN url stored? 

Imagine, we take the example of Facebook / Instagram. 
 - When you upload an image, it goes to the appserver. 
 - The appserver first stores in a Object Storage system like S3 and gets back the path to the file. Path to the file has a unique identifier to the file. That is what is returned to the client. 
 - So, when the client finally makes the post, it sends some text, along with a single file_path or multiple of them. 
 - When post is stored in DB, you save the content, along with the list of files. 
 - Asynchronously, these files are also uploaded to CDN, and you get back CDN_url, which is also stored in the posts DB. 
 - On post fetch, you return CDN_url if that's available. 

---
title: Local and global caching.
description: discussion of local and global caching.
duration: 300 
card_type: cue_card
---

## 3: Local Caching
It is caching done on the application server so that we don't have to hit the database repeatedly to access data.


## 4: Global Caching
(This will be discussed in more detail in the next class)
This is also termed In-memory caching. In practice, systems like Redis and Memcache help to fetch actual or derived kinds of data quickly.

---
title: Problems related to caching.
description: Explaining the problems related to caching.
duration: 300 
card_type: cue_card
---
## Problems related to caching
There are also two things related to the cache that you can derive from the discussions so far. 
* Cache is limited in size.
* It is not the actual source of truth; that is, the actual data is somewhere else. It stores a replica of data.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/552/original/Screenshot_2023-09-20_184350.png?1695215890)

There are a few problems that you may face:
* Data can become stale and inconsistent with time (Data in Database - actual source of truth - changes. But is not reflected in cache)
* The cache can become full due to its small storage capacity.



So what do you think will be the solution to these two problems:

1. What do you have that doesn’t become inconsistent?
2. How can you add entries if the cache is full?


---
title: Case Invalidation Strategy.
description: Discussing Case Invalidation Strategies as a possible solution to the first problem.
duration: 600 
card_type: cue_card
---
We will be discussing ways to prevent these problems.
## Case Invalidation Strategy
One solution that is proposed so that cache doesn’t become stale is
### TTL (Time to Live) 
This strategy can be used if there is no problem with the cache being invalid for a very short time, so you can have a periodic refresh. Entries in the cache will be valid for only a period. And after that, to again get the entries, you need to fetch them again.
So, for example, if you cache an entry X at timestamp T with TTL of 60 seconds, then for all requests asking for entry X within 60 seconds of T, you read directly from cache. When you go asking for entry X at timestamp T+61, the entry X is gone and you need to fetch again. 

We will look at more cache invalidation strategies in this doc through case studies. 
### Keeping cache and DB in sync
This can be done by the strategies like Write through cache, Write back cache, or Write around the cache.

**Write through cache:** 
Anything to be written is database passes from cache first(there can be multiple cache machines), storing it (updating cache), and then updating it to the database and returning success. If failed, changes will be reverted in the cache. 
It makes the writing slower but reads much faster. For a read-heavy system, this could be a great approach.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/553/original/Screenshot_2023-09-20_184357.png?1695215911)

There are other methodologies as well, like

**Write back cache:** First, the write is written in the cache. The moment write in the cache succeeds, you return success to the client. Data is then synced to the database asynchronously (without blocking current ongoing request).. The method is preferred where you don't care about the data loss immediately, like in an analytic system where exact data in the DB doesn't matter, and analytical trends analysis won't be affected if we lose data or two. It is inconsistent, but it will give very high throughput and very low latency.

**Write around cache:** Here, the writes are done directly in the database, and the cache might be out of sync with the database. Hence we can use TTL or any similar mechanism to fetch the data from the database to cache to sync with it.

---
title: Cache eviction.
description: Discussing the cache eviction as a possible solution for the second problem of how to add entries if the cache is full.
duration: 300 
card_type: cue_card
---

Now let’s talk about the second question: How can you add entries if the cache is full?

Well, for this, you will be using an eviction strategy.

## Cache eviction 
There are various eviction strategies to remove data from the cache to make space for new writes. Some of them are:
* FIFO (First In, First Out)
* LRU (Least Recently Used)
* LIFO (Last In, First Out)
* MRU (Most Recently Used)
The eviction strategy must be chosen based on the data that is more likely to be accessed. The caching strategy should be designed in such a way that you have a lot of cache hits than a cache miss.


---
title: Homework for the next class
description: Listing the topics to be covered in the next class and summary of the current lecture..
duration: 300 
card_type: cue_card
---

For the next class

Problem statements for you to think?
 - How to make code evaluation on Scaler faster?

What happens when you submit code?
Your browser sends the following to Scaler:
 - problem_id
 - code
 - programming_language_id
 - user_id

Now, when the request reaches appserver, the appserver might need more information about your status on this problem. Which it can get from a relational DB. For example, getting the following:
 - user solved status on problem_id
 - problem's input file + path
 - problem's output file + path

Once you have the file path, you would have to go to object storage to download these files. (Do you agree that input and output files should not be stored in relational DB like Mysql?)
Downloading files from an object storage can be a very slow process. If it takes 1 second to download these files, then you'd feel Scaler is slow. 

 - How do we make this process faster? 
 - Also, think about cache invalidation. In an ongoing contest, if you update test data, you would want that it is immediate for all users. How do you ensure 100% consistency? 
