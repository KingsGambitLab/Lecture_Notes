## Basic things for Motivation/ First Essential talk

**Importance of Small Difference**
- Example 1 :
    - Ask about Breaking Bad
    - discuss the importance of extra 3% clear crystals that walter white made
- Example 2 :
    - show Pictures of fastest man in India , Asia , World
    - discuss the impact of small millisec difference in timings
- Depict it with the equation - ``` (1.01)^365 = 37.78 ```


**Qualities Essential to be the Best**
- Ask about some essential qualities needed
- Discuss the importance of few - 
    - Consistency
    - Persistance
    - Hardwork in right direction
    - The will power


**Performace Equation**
- Discuss about the Performace Equation - ``` Performance = Potential - interference ```
- why the potential should be increased and interference should be decreased
- How can the performance be enhanced
    - Attend All Classes
    - Be Mindful
    - **Learning is important**


## Many technologies, Where to start from?

- discuss about multiple technologies available , maybe ask students about some names
    - frontend - js,react , angular , vue etc
    - backend - java , python , ruby etc
    - Machine Learning
    
- introduce Data structures and Algorithms
    - define and differentiate
        - Data Structure - Something we need to organise data / keep data / Store data
        = Algorithms - the process / the steps
        - give an example of toothbrush being placed in kitchen 
    - discuss about the importance of Data structures and Algorithms
    - Eventually reach to the conclusion that Data structure and Algorithms are important
    
## Building a site more important than learning about Data Structures and Algorithms ?**

- Ask the question and then discuss the result with examples
- Example 1 : **E-Commerce**
    - Dicuss the flow from searching a product to buying it
    - Discuss why we need Data structures and Algorithms in following functionalities
        - Searching a Product - need to be fast
        - Sorting - basis of price , category , reviews etc
        - Search typeahead - throw the name of **trie** just to introduce a wow-factor
        - Concurrency problem - 1 product , 2 buyers
    - Eventually convince that DSA is more important than just building a site

- Example 2 : **Food Delivery**
    - Finding nearest restaurant
    - Sorting the list of restaurant - basis of name , reviews , location
    - **Utilisation of resources** (Explain with the help of diagram)
        - Shortest path of delivery
        - Shortest time is another factor to consider
        - more factors which finally helps in better utilisation of resources
        
- Ask if it's now clear that DSA is the basic building block
        
## How Problem Solving works?
- Dicuss about the computer and decision making
- How the computer doesn't have mind of its own
- How every step needed to be told to computer based on several decisions
 
- Example 1 : **ATM Machine**
    - Discuss the process outline
    - Discuss the process in detail using decision tree (Don't introduce the name yet)
    - after drawing a basic decision tree - introduce with the name "Decision Tree"
    - Keep on focusing on the importance of decisions in problem solving
    ![ATM-MACHINE-DECISION_TREE](https://github.com/sofdev-ms/Lecture_Notes/blob/Intro_to_Programming/imperfect_notes/attachments/IMG_0016.jpg)

- Example 2 : **Super Mario**
    - Engage students by asking about the game
    - Discuss what decision making happend when you press ```->``` arrow
    ![SUPER-MARIO-DECISION-TREE](https://github.com/sofdev-ms/Lecture_Notes/blob/Intro_to_Programming/imperfect_notes/attachments/IMG_0015.jpg)

- Example 3 : **Pubg Game**
    - Engage students by asking about the game
    - Discuss what decision making happens while a person shoots in pubg
    - How does energy/health reduction happens , what are different variables involved to make one decision
        - Aim
        - Distance
        - Type of Gun
        - Body Armor

## "Observation" - The key to solve Problems

- Discuss about Guass
    - Ask students if they know about him, what they know
    - state the problem - tell them his teacher gave him the problem
    - Problem : Find the sum of numbers from 1 -> 100
    - discuss that He didn't jump on problem directly, **made observation** (focus on observation)
    ![SUM-OF-NUMBERS](https://github.com/sofdev-ms/Lecture_Notes/blob/Intro_to_Programming/imperfect_notes/attachments/IMG_0014.jpg)
 
 - **Prime Numbers**
    - What are prime Numbers
    - why 1 and 0 are not prime
    - Given a number check if it's prime or not - ask students for the solution
    
        - Approach 1 : Iterate from 1 -> N and check if it is divisble or not
        
        - Approach 2 : Sqaure root approach - traverse only till square root 
            - Intution - factors always occurs in pairs - focus on presenting it as an observation
            - give proof by examples
            - Time analysis between O(N) and O(squareRoot(N))
            
                - Considering one % (mod operation - ask if they know) takes 1 msec
                
                    N | Approach 1 - N steps | Approach 2 - sqaureRoot(N) steps
                    -- | -------------------- | --------------------------------
                    11 | 11 msec | 3 msec
                    101 | 101 msec | 10 msec
                    100000 | 16.6 min | 1 sec
                    10^18 | 116 days | 1.66 min
             - Ask them if they appreciate the improvement in timings - put more focus

- **Find sqaure root of a given Number**
    - Explain the problem - have to find the integer part
    
    - Approach - 1 :
        - iterate i from 1 to N and check if square of i is <= N
        - if square <= N - it is current ans
        - else stop the process - **WHY?** - Explain
    - Ask if the Approach 1 is fast enough to increase the curiosity
    
    - Approach - 2 :
        - start by stating an observation
        - pick some random element and check if it's square is <= or > than N
        - based on previous checks decide to ignore one part - properly explain this with example
        - now rather than picking random , pick middle element
        - reason for picking middle element - it always removes atleast half of the prospect solution
        ![LOG-N](https://github.com/sofdev-ms/Lecture_Notes/blob/Intro_to_Programming/imperfect_notes/attachments/IMG_0013.jpg)
    
    - Discuss the time Analysis
    
## How Data Structures helps in Problem Solving?

- Discuss how just the way of organising the data can optimise the solution
- Give example of toothBrush , how toothbrush stored in kitchen would result in ineffeciency

- **Dictionary Word Search**
    - Discuss the process of searching a word in dictionary
    - Relation with the sqaure root problem
    - Name of the Algorithm - Binary Search
    
- How are we able to apply the Binary Search
    - Order matters (Main situation)
    - Arrangement of Data Matters / Organisation of Data Matters
    
- **HC Verma** Example - searching a word in HC verma
    - Why Binary search won't work 
    - No particular organisation of data
    - Can sort all the words - But is it effecient ? NO!
    
    - Discuss Index / Appendix
    - How data is stored in a different way which improves efficency
    
    word | page nos.
    ---- | ---------
    velocity | 100 101 167
    
    - Data Structure used - **Inverted Index**
    - All search engines use this to optumise the search
    
## Conclusion
    - Importance of Observation
    - Importance of Data structures and Algorithms
    - Importance of 3 essential qualities
    - Further work
 
 
 
 
 
