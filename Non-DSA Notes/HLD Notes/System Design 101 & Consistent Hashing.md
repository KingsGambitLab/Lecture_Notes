
---
title: Module Introduction
description: A brief definition of system design.
duration: 300 
card_type: cue_card
---

## Module introduction

Before we begin the classes, let me share some resources and ground rules for this module. 

- **Tentative curriculum:** https://docs.google.com/spreadsheets/d/1VYizqsjlbcurqAMtDsDaCBIIZuTjqH_w3cJfTUNaejw/edit#gid=0 (please go through after the class)
    - If you are a beginner, it is important that you quickly browse through the notes before the class happens. Will make it easier for you to understand the classes. 
    - This also has some pre-requisite reading material. All of you should go through it. 
- All of you should be a part of the **HLD whatsapp group**. Please check your messages for the link. If not, can someone in the class post the link to join the group?
    - We will keep sharing resources here. Also, we will keep discussing various scenarios / problems here. I will also be part of the group. 
- **What is system design:** Till now, we focussed heavily on LLD. Which means that for a given project, how should we design schema, API, or structure the code. System design is the study of how to design the architecture of software, what database to use, what kind of caching, how does information flow and how do you make your system reliable / fast / fault tolerant. 
    - If some of the above terms don't make sense right now, do not worry. We will discover these one by one. 

- **What is not going to happen in system design:** System design is not about knowledge. It's more about developing the problem solving skill of being able to make right design choices. You won't be judged on your knowledge of what Twitter uses, but rather if asked to design twitter news feed, are you able to rationalise and explain how you'd design it and why? 
    - Implementation of what we teach is done in the backend project section. All HLD classes are going to focus on the above problem solving skill. 

---
title: Why do we need distributed system
description: An example highlighting the need of distributed systems.
duration: 300 
card_type: cue_card
---

## Why do we need distributed systems?

Let’s take a real story of a website that started on a single laptop in a dorm room (Exactly how we write code today). Back in 2003, there was a website that went by the name of Del.icio.us (https://en.wikipedia.org/wiki/Delicious_(website)). 

Browsing the internet was completely based on bookmarks and you would lose bookmarks the moment you changed browser / machine. So, delicious built a bookmarking website. You login, and then bookmark websites using delicious tool. That way, when you go to any other machine/browser, all you need to do is to login into delicious with your account to get access to all your bookmarks. Basically, largely delicious implemented following 2 functions:

```sql
addBookmark(userId, site_url)
getAllBookmarks(userId)
```
If you were to code those 2 functions on your laptop, would you be able to? Assume you store entries in MySQL database which is also on your laptop. 
If yes, congratulations. Your version of delicious is almost ready. 

---
title: DNS and ICANN
description: How internet works
duration: 300 
card_type: cue_card
---

## DNS and ICANN

**Problem 1**: How do I ensure that when people type del.icio.us in their browsers, they reach my laptop? 

The internet world only understands IP Address. How do people know the IP address of my laptop when they type del.icio.us? 

> How many of you have ever built a personal website? 

How do you setup your personal website today? 
* You go to GoDaddy (or similar websites) to buy a domain. 

Ok, but how does GoDaddy know which domain name is available? People can buy domains from GoDaddy / NameCheap / domains.google and tons of other websites.

There must be a central place maintaining domain names and their owners. And yes, there is. It’s called ICANN (The Internet Corporation for Assigned Names and Numbers). It’s non profit and has a directory of all registered domain names along with their owner details and the date validity. 


---
title: How can people globally and uniquely identify a domain name
description: Example of a bookmarking website Del.icio.us highlighting how IP addresses are tied to domain names
duration: 300 
card_type: cue_card
---

## How can people globally and uniquely identify a domain name?

Alright. But that still does not solve my problem. If I go to GoDaddy and buy delicious domain name, is my issue solved? A random user’s browser still does not know how to reach my laptop. 

So, that means I should be able to associate my domain name to my laptop’s IP address. That is exactly what happens. You can create “A” record in GoDaddy / Namecheap that is then registered centrally. 
* Further reading:
    * https://www.namecheap.com/support/knowledgebase/article.aspx/319/2237/how-can-i-set-up-an-a-address-record-for-my-domain/
    * https://support.dnsimple.com/articles/differences-between-a-cname-alias-url/ 

Ok, so now ICANN knows IP address of my laptop tied to delicious domain name that I bought. 
Which means theoretically, when someone types delicious in their browser, they can get the IP address they need to go to from ICANN. But is that a good design? 

Not really. All internet traffic will need to go to ICANN first. That's more than the traffic of Google/FB, etc. combined. ICANN becomes the single point of failure for the entire internet. 

---
title: Need of DNS, and how it works
description: A brief description of what DNS is and how it works.
duration: 300 
card_type: cue_card
---

## Need of DNS

Ok, then what do we do? Imagine if there were thousands of machines all around the internet that had a **copy of the information** there on ICANN. Then my problem could have been solved. Because now people typing delicious on their browser, could find out the IP address from these machines. 

Very simplistically, these machines are called DNS machines (Domain Name Servers). While the DNS architecture is decently complicated (You can read https://support.dnsimple.com/articles/differences-between-a-cname-alias-url/ if interested), in simple words, DNS machines maintain a copy of information present centrally and they keep pinging every few hours to get any recent updates from the central machines. 
[Not spending time on DNS architecture since the class is not on DNS. We did the discussion to give an insight into how internet works]. 

---
title: DNS questions
description: who maintains DNS
duration: 300 
card_type: cue_card
---

## DNS questions

Ok, you might have the following questions:
 - Who owns these DNS machines? 
 - How do DNS machines stay updated as entries change in ICANN? 

Let's go one by one. 
On who owns DNS, who benefits from maintaining these machines:
 - One is your Internet Service Provider (ISPs like Airtel, Tata, etc.). If your Domain Name -> IP resolution is slow, your entire internet will feel slow. So, they would want to maintain these machines to make IP lookup faster. This is the default DNS setup. If you don't change anything manually, your machine is most probably talking to a DNS machine from your ISP. 
 - There are other companies who benefit from more people using the internet. For example, Google or CDN providers. Hence, Google owns some DNS machines, and so do companies like CloudFlare. 

Q2. How do DNS machines stay updated? 
Ofcourse, if they keep asking ICANN for the entire dump, it's going to make ICANN machines crash. So, they ask for the change after a particular timestamp. 
And they do it infrequently. 
General direction given is that if you change your A / cname records, it takes up to 24 hours for every DNS machine to catch up. 

---
title: Static vs dynamic IP
description: Ensuring Host IP does not keep changing
duration: 300 
card_type: cue_card
---

## Static vs dynamic IP

Ok, let's come back to our Delicious example. 

How does a machine get an IP address? When you connect to the internet, your ISP assigns one of the available IP addresses (IP address not assigned to any active machine on the internet) to you. 

Ok, how does ISP find such an address? Typically, ISPs own a range of IP addresses to assign. They get one from there. 

In our delicious example, let's say when my laptop connects to the internet, it gets an IP address 10.20.30.40. 
And hence, what IP address should I feed in ICANN? Correct, 10.20.30.40. 

But imagine if my laptop disconnects. When it reconnects, is it guaranteed to get the same IP again? No. What if it gets 10.21.31.41? 
Then, all requests to delicious will fail. Because users would be trying to connect to 10.20.30.40. 

That's a problem. How do we solve it? 
The IP address stated above is a dynamic IP address. 
You can also reserve an IP address for yourself by paying more money. It's called static IP address. Sort of like paying more money to get a custom number plate for your bike. 

---
title: Distribution of load
description: A brief discussion of why load balancing is required and how it helps in increasing availability of the system.
duration: 300 
card_type: cue_card
---

## Distribution of load

Ok, so now we are live. Delicious is now serving users. 
There is a small problem though. Everytime I want to add new features and re-deploy and re-start my laptop with new code, delicious is unavailable for a few seconds. That’s not good. So, what do I do? 

Infact, if my laptop reboots or disconnects from the internet, again website is down. Not good, right? 

Maybe instead of one laptop, I have multiple laptops with same code and same information (We will figure out how to keep this information in sync). However, when my code is being deployed to a laptop X, how do I ensure no traffic is coming to X? 
We need a Load Balancer which keeps track of laptops, which ones are running and is responsible to split the load equally. 

How does Load balancer do that? 
* Which machines are alive? - Heartbeat / Health Check
* Splitting load? - Round robin / Weighted Round Robin / Ip Hash 

> Note: Please spend time here explaining Round robin / Weighted Round robin. Very similarily, explain heartbat and health check mechanisms. Important to land the message that Load Balancer knows about machines and tracks their live/dead status. 

https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/ has example of a config setup of a load balancer. 

---
title: What is sharding and why do we need it
description: An example highlighting the need of splitting the information you have between machines.
duration: 300 
card_type: cue_card
---

## What is sharding and why do we need it?

Imagine, Del.icio.us becomes majorly popular. It starts getting massive traffic. It starts getting a million new bookmarks every day. 
Now, remember this is 2004. Best machines had 40GB hard disk. If you were getting 1 Million new bookmarks every day, and every bookmark is 200 bytes roughly, then you are adding 200MB of new bookmarks every day. Which means you will run out of space in 6 months. What do you do? 

We can get better machines. Maybe machines with higher storage, better CPU. They'd be expensive but will buy us more time. 
This is called vertical scaling. 

However, vertical scaling will not solve the problem for me permanently. 

So, that means I need some way of splitting data between the machines. Then, if I have 100 such machines, my total storage becomes 
   $40GB * 100 = 4TB$
That is called horizontal scaling. 

How do I split data though? 


You will have to consider splitting the information you have between machines. This is called sharding. 


---
title: How sharding works
description: A sneak peek into detailed working of sharding.
duration: 300 
card_type: cue_card
---

## How sharding works?

**Step 1**: Choose sharding key. Basically what information should not get split between machines, and should reside in the same machine. 
Show what happens if you choose site_url as the sharding key. getAllBookmarks has to go to all machines. 
We choose user_id to be the sharding key, which means a user and all their bookmarks go to one shard. 

**Step 2**: Build out an algo for userId -> shard mapping. 

Following constraints:
* Finding shard given userID should be extremely lightweight. Can’t add a lot of load to LB. 
* Load should be somewhat equally distributed (no load skew)
* Addition of new shards should be easy and should not cause major downtime. 
* Same for removal of shards. 

---
title: Various approaches to sharding.
description: A brief discussion of the various approaches of sharding.
duration: 300 
card_type: cue_card
---

## Approaches to Sharding

Let’s check certain approach for sharding. 

**Approach 1:** Assign userId to userId % number_of_shards. While this approach is great, it fails when number of shards change, as it causes almost every user’s data to be copied to another machine. Massive downtime when shard is added.

**Approach 2:** Range based assignment. Load skew - first adopters more likely to be busier users. Also, every range’s total storage usage will only increase as they add more bookmarks. Addition of new shard does not help existing shards. 

Let’s look at the real approach used in most cases - Consistent Hashing. 


---
title: Introduction to consistent hashing.
description: Demonstration of how consistent hashing works using an example.
duration: 300 
card_type: cue_card
---


## Consistent Hashing 

Imagine a circle with points from $[0, 10^{18}]$. Imagine there is a hash function H1, which maps every machineId to a number in $[0, 10^{18}]$, which you then mark on the circle. Similarly, there is another hash function H which maps userId to $[0, 10^{18}]$. 

Let’s assume we assign a user to be present on the first machine in the cyclic order from the hash of the user. 



![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/547/original/Screenshot_2023-09-20_184255.png?1695215796)

For example, in the diagram above, Deyan and Affrica are assigned to Node 2, Freddie and Srushtika on Node 5 and so on. 
In implementation, if you have a sorted array with hashes of nodes, then for every user, you calculate the hash, and then binary search for the first number bigger than the given hash. That machine is what the user will be assigned to. 

However, this design suffers from an issue. What happens when you remove a shard. Let’s say Node 2 is down. All load of Node 2 (Deyan + Africa) get assigned to Node 5 and Node5’s load basically doubles. At such high load, there is a good probability that Node 5 dies which will triple the load for Node 4. Node4 can also die and it will trigger cascading failure. 

---
title: Optimizing the consistent hashing.
description: Discussion the modification in consistent hashing algorithm to minimise chances of cascading failure.
duration: 300 
card_type: cue_card
---

## Optimizing the consistent hashing

So, we modify the consistent hashing a little bit. Instead of one hash per machine, you use multiple hashing functions per machine (the more, the better). So, Node 1 is present at multiple places, Node 2 at multiple places and so forth. 


![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/548/original/Screenshot_2023-09-20_184304.png?1695215817)


In the above example, if node A dies, some range of users is assigned to B, some to D and some to C. That is the ideal behavior. 


---
title: Data transfer
description: How will data be transferred when shards are added or removed. 
duration: 300 
card_type: cue_card
---

## Data transfer

Typically, when you add a shard, if you immediately make it active, then it will have no data. Queries will fail. 
That's bad. 

So, we typically folllow a process of warming up the shard before making it active. 

 - **Timestamp T1:**<br> Start the transfer of relevant users to the new shard. Relevant users are the users who would have been on this shard if it was added. Note the shard is not added yet, and hence is not getting any traffic. 

 - **Timestamp T2:**<br> Transfer is complete. We now add the new shard, and it starts getting traffic. Only problem is that there might be new entries added for these users between T1 and T2 (very small number of entries, but non zero). 
     - So, we start the copy process of incremental data for users between T1 and T2. This should be very quick. For those few seconds, following 2 options:
         - I reject the incoming requests on new shard and compromise availability.
         - Or I return response which might be inconsistent (compromise consistency). 

See you in the next lecture! 
