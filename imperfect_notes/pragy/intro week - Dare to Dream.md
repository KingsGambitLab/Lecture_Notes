Intro Week - 1 - Dare to Dream
------------------------------

- mute all
- disable mentee sharing
- stop mentee videos
- disable screen annotations

-- --

Intro
-----

- instructor introduction
    - myself: pragy, senior soft engg at IB. worked at directi, gateoverflow. IIT-B masters, machine learning. Passion for teaching
    - anshuman:
        - facebook messaging - 20M messages per minute
        - facebook london office - first 100 engineers
        - interviewbit & scaler
        - stark diff b/w people hired in US vs India
            - indian people are theoritical
                - if you break down and define the task, they will be able to do
                - as you grow, your job is more of taking vaguely defined problems and solving them
                - that practical part was missing in indian devs
- overview of curriculum
- some preview material from different topics
- this is a meeting and not a view because interactive
- superx content is slightly harder and moves at faster pace. might move faster.
- elitex is more indepth with more basics covered
- content and curriculum remains exactly the same
- can move b/w batches
- if struggle with elitex, don't move to superx
- backend vs frontend batch - your choice
- build things from scrath. detailed curriculum will be shared
- classes are recorded. Lecture notes are shared
- if you have something urgent, we can share previous batch videos, but don't overstrain yourself. Take things at the correct pace
- watching recorded is counted in attendance


-- --

Presentation
------------

- left guy is fastest man in India - Abhilal
- right guy is fastest man in Asian - ...
- Usian Bolt - fastest in the world
- bolt is more consistent
- if you're consistent, you'll get the best results
- student example from previous batch
    - extremely consistent
    - never missed a class
    - offer from HCL - 3.5 lakhs
    - consistent for 1 year. > 20 LPA salary
    - Google - Naman Bhalla, 3rd tier college. Extremely consistent.
    - no internship
    - we first got him an internship then job - 4 months
- talent is not why people win
- it is hard work and consistency
- 1% better everyday is all you need to focus on
    - we've figured out the long terms goals. we've a pipeline for you. You can focus on the daily tasks, with the assurance that if you follow them, you will end up being an amazing engineer

- 6 month course
    - but we will help you forever
    - scaler talks will continue
    - always reach out to us for help
    - reach out to us for referrals

- will take questions after the lecture

-- --

Company Questions
-----------------

- random DS/Algo, design questions that have been asked at companies
- not learning, for self evalution
- see where we currently stand
- we will do another such session 4/4.5 months down the line and see what progress we've made
- are you actually spending time in the right direction

- real world problems - so actual company questions

-- --

Facebook Graph
--------------

> friend = edge
> represented as a graph
> given 2 nodes, find out the degree of separation
> unweighted

2 billions nodes and 2 trillion edges
user can have max 5k edges
avg has 1k edges

degree of separation was <= 5, as long as the person had more than 25 friends (not exhaustive, estimate)

consider everyone has DOS <= 5

**Sortest path algo**

will give the correct answer, but nodes is very large

Let's say BFS - O(V+E) time
10^9 computations per second = 33 mins per query

**Don't go beyond the length of 5**

but you will still go over everyone with >=25 friends


**Solution**
Meet in the middle

10^6, else ans=5

![3e17ae37.png](:storage/be7d0ff2-5fef-4871-867c-a6cd3654b57b/3e17ae37.png)

how to check if connected? BBST? Bloom Filter?
can use DSU to check if connected for fast return in O(n)
or can simply use intersection of lists using hashmap in O(n)
or can use sorting in O(n log n)
-- --


Google - Running Median
-----------------------

> Given a stream of integers, find the median at every step
> more difficult: distributed streams. Have multiple servers and partial data is coming at different servers
> cannot pull data into one machine because of memory constraints
> 

Median = mid (odd) or avg of 2 mids (even)

1. sort array and mid number is median - BBST
2. store equal number of < and > numbers - 2 heaps


-- --

Google - Distributed Running  Median
------------------------------------

1. ~~median of medians~~. find median of each server. sort the values and find overall median
    - incorrect
    - 1 2 (4) 8 10
    - 1 2 (100) 101 102
    - median of 4, 100 is 52.
    - 1 1 2 2 4 8 10 | 100 101 102
    - 52 is not the median
3. each server has BBST
4. guess x -> goto each server and count how many numbers are smaller than x and larger than x
5. binary search for the answer x


-- --

DS/Algo 101 - Arrays and Maths
HLD 101
LLD 101 - OOPs design
    - give a problem. ask to code.
    - change requirements. measure the number of changes

Hacking your interview
Celebrity Lecture - CEO, codechef, github, .. 

-- --

from next week, class on alternate days
TAs while solving assignments and homeworks
TA sessions
(choice) super elite split
Mentor sessions (university seniors) + mock interviews every alternate
DS Algo 1.5
CS basics 1 week
HLD - 15 days
LLD - 7 days
Machine Coding - 8 days
Basic of JS, HTML, CSS - 1 week
(choice) Full stack vs Backend - 1 month

-- --

Placement
---------

- april 196 people - 130+ have min ctc+ have jobs, some are yet to graduate. 18.2 LPA. 52 amazon, 3 google, adobe, 12 microsoft, atlassian, cisco


Referral
--------

choice to stop or continue.


-- --

How to succeed at Scalar Academy
--------------------------------

- take notes - your own notes
    - aha
    - important stuff
    - theory & formulae
    - analogies & intuition
- discuss with peers
- 3 hours everyday
- consistency - maintain your streak, even if you're not able to do the stuff completely. 
- feedback forms (because we use them extensively)
- don't have a huge backlog (don't join if major life event)