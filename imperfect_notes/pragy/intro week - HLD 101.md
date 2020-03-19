Intro Week - 3 - HLD 101
------------------------

What is HLD?
------------

1. used to working with code on a single machine
    - you give some input, you get some output
1. how do you scale to 1000 or million or 100 million users?
    - what should your architecture be
1. This is what HLD is about
1. You need to now HLD, LLD to progress in your career

-- --

How do you access Google.com?
-----------------------------

1. Most large systems have
    - business logic at some location
    - many many clients using that sytem
    - via some interface
        - usually a website
    - so, first layer us client
        - on mobile / browser / ipad
1. something like Google.com
1. when you type Google.com, first thing that happens?
    - DNS Lookup/resolution
        - Every device on the internet has an IP. Including your system
            - 0-255 . 0-255 . 0-255 . 0-255
            - 192.168.0.1
        - Similarly, Google.com also has an IP.
        - DNS maps domain names to IPs
            - server which takes in domain name and gives you back IP
            - Google DNS
1. Browser gets the IP address and tries to connect
1. Request goes to Google's servers.
1. Some Magic happens and a response is generated
1. Response is returned back to you
![c04ecd7d.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/c04ecd7d.png)
1. Now, HLD deals with everything that happens in this Magic box
-- --

DELICIO.US
----------

1. 2005/6
1. Bookmarking website
    - chrome wasn't there yet
    - firefx and IE were all the rage
1. If you store bookmarks on one machine
    - how do you access them on another machine?
1. Delicio.us stores all your bookmarks.
    - if you change machines
    - just login to delicio.us
    - all your bookmarks are there

-- --

Humble Beginings
----------------

1. delicio.us started with a single laptop
    - ![dcb4d992.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/dcb4d992.png)
1. Let us walk through how it evolves over time
1. Started getting popuar
    - DB requirement started growing
    - 40 GB storage wasn't enough
    - already at 35GB. Filling at 5 GB / month
    - how do I fix this?
1. Buy a better laptop
    - one with 100GB storage
1. This is **Vertical Scaling**
    - This is how servers would scale in 90's
    - IBM
1. Delicio.us got even more popular
    - 100 GB will last for only 2 more months
    - no better laptop in the market
    - how to fix it now?
1. Buy more laptops
1. DNS issue
    - one domain mapped to only 1 IP
        - usually. Google has multiple IPs
        - you need to be huge to get multiple IPs
1. How to distribute users over different laptops, if I have just 1 ip?
1. Load Balancer
    - because entire website cannot be on one single server. What if I restart?
    - So, multiple macines, and load balancer distributes the requests
    - simply forwards requests and gives back results
    - could be different communication protocol - socket vs http vs protobuf
    - Google has multiple IPs
        - 1 LB with **multiple backups**
        - switching time is seconds to microseconds
1. Note that going from just 1 to 2 laptop requires a LB
    - because the client just has 1 IP and doesn't care what you're doing internally
1. Usualy, LB just reroutes and doesn't do any heavy computation
![12c0d462.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/12c0d462.png)
1. This is called **Horizontal Scaling**.

-- --

Load Balancer
-------------

1. ![6b536bd2.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/6b536bd2.png)
1. How will you design the LB?
    - Round robin - go one by one to each machine
    - No need to consistent hashing here
1. What is M2 goes down?
    - or n/w breaks
1. Keep an alive mapping
    - Health Check
    - Poll/Ping each server. Must respond in 100 ms
    - Or server sends heartbeat
1. What if LB goes down?
    - Backup servers
    - Managed via Zookeeper
1. Most LBs allow configuring Heartbeat vs Polling, frequency, ...
1. What if server is not down, but slow?
    - need rate management
    - measure avg response time
        - assuming requests are similar
    - do some sort of weighted Round Robin
        - weights could be preassigned
        - or based on Avg Response Time
        - or a hybrid approach
    - will need to invalidate the Avg Response Time? Sliding window / TTL
        - because machines can start failing slowly
1. Of course, LB has to be non-blocking
    - so that no request slows down the other requests
    - most requests are IO bound
    - servers are also multicore. So you can process multiple CPU bound requests too!
1. DDOS attacks are usually handled at the LB stage
    - rate limiting by ip/userid
    - whitelisting and blacklisting
1. this is stateless LB. Doesn't matter which server the request goes to

-- --

Stateful LB
-----------

1. Delicio.us could not store all data on one laptop
    - had to split
1. If U1's data is on L1, U1's request should go to L1 and not other servers
1. How to do this?
    - store {userid -> serverid}
        - Too big if we've 8B users
        - 8 bytes + 4 bytes + overhead
        - 100 bytes * 8B = 800 GB
        - Can't fit in RAM
    - userid % N
        - don't need to store anything in memory
    - or some hash function
1. But what if server goes down? Up?
    - every userid will be moved
        - for all userids > N
    - so, a lot of data transmission

1. Hash function should be able to handle such things
1. Consistent Hashing

-- --

Consistent Hashing
------------------

Step 1
------

- userid space
- serverid space
- hash space
- H(uid or sid) -> $[0, 10^{18}]$
- Hash both servers and users
- ![3b3d4e20.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/3b3d4e20.png)
- User gets assigned to the closest server
- Since Hash is almost random, equal probability of user to be assigned to any server


Step 2
------

- What happens if server dies?
- Say s2 dies
- ![37f4f6bf.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/37f4f6bf.png)
- All users of s2 get assigned to s3
    - they should've been distributed equally
- What if I add server?
    - add s5
- only the load of s4 is reduced. Load at s1, s2, s3 is still the same
- ![91393714.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/91393714.png)
- Why hash and not equidistant? How will you add more servers? you will have to move every server


Step 3
------

- create more markers for each server
    - not more copies of server
    - just markers
- helps distribute load more equally
- ![b61475e4.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/b61475e4.png)
- basically, use multiple hash functions H1 .. H100
- Now, if a server dies
    - its users will be almost equally distributed amongst the other servers
    - ![9f4a3dfa.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/9f4a3dfa.png)
- If server added
    - each server gies up some of its users to new server
    - ![8a5888d2.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/8a5888d2.png)


Algorithm
---------

- Store (hash, server) in sorted order
- binary search for user's hash
- ![612e3e58.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/612e3e58.png)
- 

-- --


- Application layer
    - application layer hosts the business logic
    - authentication
    - mostly, all machines in the application layer are running identical code
- Storage Layer
    - need to maintain context
    - stateful
    - ![0e75c7a9.png](/users/pragyagarwal/Boostnote/attachments/a11cb768-9794-4512-9eab-869704a6fe9a/0e75c7a9.png)

-- ---



- Load Balancer gets the request
    - via some protocol - Socket / HTTP
    - how do you prevent the LB from becoming a single point of failure?
        - have multiple load balancers?
            - ip can be located to only one machine, not a bunch of machines
        - Have the domain map to multiple IPs
        - browser takes care of making sure that all ips are fetched and we connect to some ip which is up
    - is needed so that we can
        - ensure that each machine gets almost equal load
        - we can add/remove machines when we want
        - to have a single point of contact for the outside world


- Internet vs Intranet

- Vertical scaling - getting a bigger machine
    - limited by commercial machines
    - compression can only go to some extent
- registering ips with ICANN is a slow process
- Horizontal scaling - get lots of smaller machine
    - need to be able to load balance and distrubute data
    - 