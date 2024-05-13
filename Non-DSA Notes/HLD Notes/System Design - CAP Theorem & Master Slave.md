---
title: Introduction to CAP theorem.
description: Introduction to the CAP theorem.
duration: 300
card_type: cue_card
---

## CAP Theorem

The CAP theorem states that a distributed system can only provide two of three properties simultaneously: **Consistency, Availability, and Partition tolerance. **

Let’s take a real-life example; say a person named Rohit decides to start a company, “reminder”, where people can call him and ask him to put the reminder, and whenever they call him back to get the reminder, he will tell them their reminders. 

For this, Rohit has taken an easy phone number as well, 123456. 
Now his business has started flourishing, and he gets a lot of requests, and he notes reminders in the diary. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/691/original/upload_59d627985c2b423f4798461a771cea0a.png?1695237630)



After a while, this process becomes hectic for Rohit alone, because he can only take one call at a time, and there are multiple calls waiting. Now, Rohit hires someone called “Raj”, and both manage the business. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/692/original/upload_a1debf1968a849fcb29f920f4dca4411.png?1695237652)


One day, Rohit gets a call from a person named “X” asking him the time of his flight, But Rohit was not able to get any entry for X. So, he says that he doesn't have a flight, but unfortunately, that person has that flight, and he missed it because of Rohit. 
The problem is when person “X” called for the first time, the call went to “Raj”, so Raj had the entry, but Rohit didn’t. They have two different stores, and they are not in sync. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/693/original/upload_826022847ed315cc9b9009e86d9da93e.png?1695237676)

---
title: Inconsistency in distributed systems
description: Discussion on inconsistencies in a distributed system.
duration: 300
card_type: cue_card
---


**Problem 1:** Inconsistency
It’s a situation where different data is present at two different machines.

**Solution 1:** 
Whenever a write request comes, both of them write the entry and then return success. In this case, both are consistent. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/694/original/upload_6c95413266feecf6f6ceb8081d1c7955.png?1695237698)

---
title: Availability in distributed systems
description: Discussion on Availability in a distributed system.
duration: 300
card_type: cue_card
---

**Problem 2:** Availability problem. 
Now one day, Raj is not there in the office, and a request comes. So because of the previous rule, only when both of them write the entry then only they will return success. Therefore the question is How to return the success now.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/695/original/upload_d87bfa2808651828f3fd55250f0571a7.png?1695237719)

**Solution 2:**
When the other person is not there to take the entry, then also we will take the entries, but the next day, before resuming, the other person has to ensure they catch up on all entries before marking themselves as active (before starting to take calls). 

---
title: Network Partition in distributed systems
description: Discussion on Network Partition in a distributed system.
duration: 300
card_type: cue_card
---


**Problem 3:** Network Partition. 
Imagine someday both Raj and Rohit have a fight and stop talking to each other. Now, if a person X calls Raj to take down a reminder, what should Raj do? Raj cannot tell Rohit to also note down the entry, because they are not talking to each other. 
If Raj notes the reminder and returns success to X, then there is an inconsistency issue. [X calls back and the call goes to Rohit who does not have the entry]. 
If Raj refuses to note the reminder and returns failure to stay consistent, then it’s an availability issue. Till Raj and Rohit are not talking to each other, all new reminder requests will fail. 

Hence, if there are 2 machines storing the same information but if a network partition happens between them then there is no choice but to choose between Consistency and Availability. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/696/original/upload_7b40910f3886b207e0ae5b30dc567d41.png?1695237743)

---
title: Introduction to PACELC theorem
description: Introduction to the PACELC theorem
duration: 300
card_type: cue_card
---

## PACELC Theorem:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/697/original/upload_7172167c80f74ea04ced6acdf361ab5a.png?1695237772)

In the case of network partitioning (P) in a distributed computer system, one has to choose between availability (A) and consistency (C).
But else (E), even when the system is running normally in the absence of partitions, one has to choose between latency (L) and consistency (C). 
**Latency** is the time taken to process the request and return a response.  

So If there is no network partition, we have to choose between extremely low Latency or High consistency. They both compete with each other.  

Some Examples of When to choose between Consistency and Availability. 

1. In a banking system, Consistency is important.
    2. so we want immediate consistency.
    3. but in reality, ATM transactions (and a lot of other banking systems) use eventual consistency
4. In a Facebook news feed-like system, availability is more important than the consistency. 
5. For Quora, Availability is more important. 
6. For Facebook Messenger, Consistency is even more important than availability because miscommunication can lead to disturbance in human relations. 

---
title: Introduction to Master Slave System
description:
duration: 300
card_type: cue_card
---

**Master Slave System:**

In Master-Slave systems, Exactly one machine is marked as Master, and the rest are called Slaves. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/698/original/upload_241a3d0c6cf5bb9cd82048ebf6fd8ca3.png?1695237800)


1. Master Slave systems are Highly Available and not eventually consistent. 

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/699/original/upload_f50184da06f5e8ddd9c0cb97da9f0726.png?1695237822)

**Steps**:
1. Master system takes the write. 
If the write is successful, return success. 
2. Try to sync between slave1 and slave2. 


Example: Splunk, where we have a lot of logs statements now, there is so much throughput coming in, we just want to process the logs even if we miss some logs, it’s ok. 

2. Master-Slave systems that are Highly Available and eventually consistent:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/700/original/upload_06987f8f3888e77f2537fa5d5e655613.png?1695237848)

**Steps**: 
1. The Master system takes the write, and if one slave writes, then success is returned. 
2. All slaves sync. 

Example:   Computing news feed and storing posts, there we don’t want the post to be lost; they could be delayed but eventually sync up. 

3.  Master Slave that are Highly Consistent:

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/701/original/upload_593c17178a4cb1b76260dc48a2cf012a.png?1695237882)

**Steps**:
1. Master and all slave take the writes, if all have written, then only return success. 
Example: The banking system. 

---
title: Features and drawbacks of Master Slave System
description:
duration: 300
card_type: cue_card
---

**In Master-Slave systems,**
* All writes first come to Master only. 
* Reads can go to any of the machines. 
* Whenever the Master system dies, a new election of the master will take place based on a different elections algorithm. 

**Drawbacks of Master-Slave System:**
1. A single master can become the bottleneck when there are too many writes.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/702/original/upload_1c795a6743467b8572ed36fa7950346d.png?1695237935)
2. In highly consistent systems, slaves increase which increases the rate of failure and latency also increases.
![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/703/original/upload_869ef105a6076b143b39e3a8e4037181.png?1695237966)

For example, For highly consistent systems, if there are 1000 slaves, the Master-slave system will not work. We have to do more sharding. 

