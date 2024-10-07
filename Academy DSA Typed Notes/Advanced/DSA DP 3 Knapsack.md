# DP 3: Knapsack


## Subset Sum


### Problem Statement:
You are given an integer array nums. Determine whether it is possible to partition the array into two subsets such that the sum of elements in both subsets is equal. Return true if possible, and false otherwise.

**Example 1**:
Input: nums = [1, 5, 11, 5]
Output: true
**Explanation**:

The array can be partitioned into two subsets: {1, 5, 5} and {11}, both with sum 11.

**Example 2**:
Input: nums = [1, 2, 3, 5]
Output: false
**Explanation**:

It is not possible to partition the array into two subsets with equal sums.


**Key Insight**:

- The problem reduces to checking whether we can find a subset whose sum is equal to half of the total sum of the array.
- If the total sum of the array is odd, it is immediately impossible to partition the array into two subsets with equal sums.
If the total sum is even, we need to check if there exists a subset whose sum is half of the total sum.

**Problem Restatement**:

- Let the total sum of the array be S.
- If S % 2 != 0, return false.
- Otherwise, find out if there exists a subset in nums whose sum equals S / 2. This is a classic subset sum problem.

### Approach 1: Brute Force (Inefficient)
**Idea**: Explore all possible subsets and check if any subset has a sum equal to S / 2.

**Steps**:

Generate all possible subsets of nums.
For each subset, calculate the sum and check if it equals S / 2.
**Complexity**: O(2^n)


**Flaws**:

- This approach becomes highly inefficient for large arrays due to the exponential number of possible subsets.

## Subset Sum optimized approach

### Approach 2: Dynamic Programming (Optimized Solution)
**Key Insight**: Use dynamic programming to determine if there exists a subset with sum S / 2.

**State Definition**:

- Let target = S / 2. We need to determine if a subset of nums can achieve this target sum.
- Use a boolean DP array dp where dp[j] represents whether a subset with sum j is achievable using the elements in the array.

**State Transition**:

- Initialize dp[0] = true, because a subset with sum 0 is always possible (the empty subset).
- For each element num in nums, update the DP array for sums from target down to num:
dp[j] = dp[j] or dp[j - num]
- This means: If we can form a sum j - num, we can also form the sum j by including the current element num.

### Pseudocode (Dynamic Programming Approach):

``` cpp 
function canPartition(nums):
    totalSum = sum(nums)
    
    # If totalSum is odd, we cannot partition the array into two equal subsets
    if totalSum % 2 != 0:
        return false

    target = totalSum / 2
    dp = array of size (target + 1) initialized to false
    dp[0] = true  # We can always form a sum of 0

    # Process each number in nums
    for num in nums:
        # Update the dp array from target down to num
        for j from target down to num:
            dp[j] = dp[j] or dp[j - num]

    # The result is whether we can form the sum 'target'
    return dp[target]
    
```

**Explanation**:
**Initialization**:

- dp[0] = true because a sum of 0 can always be formed with an empty subset.
- All other dp[j] values are initially false, as no subset sums have been processed yet.

**State Transition**:

- For each element num in nums, iterate backward from target down to num.
- For each j, if dp[j - num] is true, set dp[j] = true, indicating that the sum j can now be formed by adding num to the subset.

**Final Result**:

- After processing all elements, the value dp[target] will tell us if it's possible to form a subset with sum target.

###  Complexity Analysis:
**Time Complexity**: (n×target)
**Space Complexity**: O(target)

## Knapsack
### Knapsack Problem

Given N objects with their values Vi profit/loss their weight Wi. A bag is given with capacity W that can be used to carry some objects such that the total sum of object weights W and sum of profit in the bag is maximized or sum of loss in the bag is minimized.

We will try Knapsack when these combinations are given: 
* number of objects will be N
* every object will have 2 attributes namingly value and  weight
* and capacity will be given

---
## Problem 1 Fractional Knapsack

### Problem Statement 
Given N cakes with their happiness and weight. Find maximum total happiness that can be kept in a bag with capacity = W (cakes can be divided)

### Example:
N = 5;        W = 40
Happiness of the 5 cakes = [3, 8, 10, 2, 5]
Weight of the 5 cakes = [10, 4, 20, 8, 15]
Goal - happiness should be maximum possible and the total sum of weights should be <= 40.

### Approach

**`Since we can divide the objects, hence they can be picked based on their value per unit weight.`**

**`For per unit weight, below are the happiness values:`**
* Cake 1:  `happiness = 0.3`;
* Cake 2: `happiness = 2`;
* Cake 3: `happiness = 0.5`; 
* Cake 4: `happiness = 0.25`;
* Cake 5: `happiness = 0.33`; 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/281/original/upload_72db79387a8a773bb3e539c979b5156d.png?1695931887" width=500/>


### Solution

**`Arrange the cakes in descending order with respect to happiness/weight and start picking the element`**
* Select the 2nd cake (happiness = 2), reducing capacity to 36(40-4).
* Choose the 3rd cake (happiness = 0.5), further reducing capacity to 16(36-20).
* Opt for the 5th cake (happiness = 0.33), leaving a capacity of 1(16-15).
* Take a part of the 1st cake (happiness = 0.3), using up the remaining capacity.
* Total happiness achieved: 23.3 (8 + 10 + 5 + 0.3).

**Time complexity** of the above solution is O(Nlog(N)) because it requires sorting with respect to `happiness/weight`.

**Space complexity** of the above solution is O(1).*

### Pseudo Code 
```cpp=

class Items {
    declare cost, weight, value, ind;
    constructor Items(weight, value, cost){
        this.weight = weight;
        this.value = value;
        this.cost = cost;
    }
}

function solve(A[], B[], C) {
    iVal = new array of Items of size A.length;
    for (i -> 0 to A.length - 1) {
        cost = (A[i]*1.0) / B[i];
        iVal[i] = Items(B[i], A[i], cost);
    }
    sort(iVal, on comparision logic compare(Items o1, Items o2){
            if(o1.cost >= o2.cost){
                place o1 first ;
            }else {
                place o2 first ;
            }
                
        }
    });
    
    totalValue = 0.0;
    for (i -> 0 to A.length - 1) {
        curWt = iVal[i].weight;
        curVal = iVal[i].value;
        if (C  >= curWt) {
            C = C - curWt;
            totalValue += curVal;
        }
        else {
            totalValue += (C * iVal[i].cost);
            break;
        }
    }

    return (totalValue * 100);

}


```


### Flipkart's Upcoming Special Promotional Event

Flipkart is organizing a **`promotional event`** where they aim to craft an exclusive "**`combo offer`**" that **`maximizes customer satisfaction`**. This combo will be composed of various items selected based on their **`customer reviews`**.

The challenge lies in ensuring that the combined cost of these selected items does not exceed a set budget for the combo. T*he goal is to strategically pick items that together deliver the greatest value and satisfaction to customers while adhering to the predefined price limit*.

**Example:**
Let’s say Flipkart has a budget of $100 for a promotional combo offer. They analyze various items like headphones, books, and kitchen gadgets, each with customer ratings and individual prices:

**`Headphones`**: price: **$60**, rating: **9/10**.
**`Book`**: price: **$20**, rating: **7/10**.
**`Kitchen Gadget`**: price: **$45**, rating: **8/10**.

***They could choose the following combos:***

Combo 1: Headphones + Book = $80 (total satisfaction: 9 + 7 = 16)
Combo 2: Headphones + Kitchen Gadget = $105 (over the budget)
Combo 3: Book + Kitchen Gadget = $65 (total satisfaction: 7 + 8 = 15)

The best choice under the budget with the highest satisfaction score is Combo 1, consisting of the headphones and the book, offering a combined satisfaction rating of 16, and costing $80, which is under the $100 budget.

This is the real life example of a problem that we are about to study.

---
## Problem 2 0-1 Knapsack 

## 0-1 Knapsack
In this type of knapsack question, **division of object is not allowed.**

### Question

Given N toys with their happiness and weight. Find maximum total happiness that can be kept in a bag with capacity W. Division of toys are not allowed.

---

### Question
In the Fractional Knapsack problem, what is the key difference compared to the 0/1 Knapsack?

### Choices
- [ ] Items can only be fully included or excluded.
- [x] Items can be partially included, allowing fractions.
- [ ] The knapsack has infinite capacity.
- [ ] The knapsack has a fixed capacity.



### Explanation

 In the Fractional Knapsack problem, items can be included in fractions, enabling optimization of the total value based on weight.


---
##  0-1 Knapsack Example

### Example:
N = 4; W = 7
Happiness of the 4 toys = [4, 1, 5, 7]
Weight of the 4 toys = [3, 2, 4, 5]

> If we buy toys based on maximum happiness or maximum happiness/weight we may not get the best possible answer.

### Brute Force Approach:
* Consider all subsets of items and select the one with highest summation of happiness.

Since there are in total 2^N^ subsequences and we have to consider each of them. Therefore the time complexity is: <img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/285/original/Screenshot_2023-09-29_015000.png?1695932414" width=120/>

### Dry Run of Brute Force Apporach

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/286/original/upload_1da8c9bd0252023a1565544101017689.png?1695932481" width=700/>

In the above figure each element is taken and its selection is determined based on happiness and weight.

>  Here we can notice optimal sub structure as well as overlapping sub problems.
> *Thus we can use dynamic progamming in this case*

If index and capacity can define one unique state total number of unique states are `O(N * (W + 1))` which is `O(N * W)`, as index will go from 0 to N - 1 and weight will go from 0 to W.

```cpp
dp[N][W] = max happiness (considering N objects and capacity W)
```

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/288/original/upload_714587c8730fa95bdd9fb19f8674a224.png?1695932582" width=500/>

> Here taking N = i and W = j, we have two choices either to select dp[i][j] or to reject it. On selecting it will result into` h[i] + dp[i - 1][j - wt[i]]`(h[i]=happiness of i) and on rejecting it will be `dp[i - 1][j]`.

### Base Case
* for all j when i = 0, dp[0][j] = 0
* for all i when j = 0, dp[i][0] = 0

### Psuedocode

```java
//for all i,j dp[i][j]=0
for(i --> 1 to N){ // 1based index for input
    for(j--> 1 to W){
      if(wt[i] <= j){
        dp[i][j] = max(dp[i - 1][j], h[i] + dp(i - 1)(j - wt[i]))
        }else{
           dp[i][j] = dp[i - 1][j]
        }
        }
    }
return dp[N][w]
}
```


The dimensions should be (N + 1) * (W + 1) as the final answer would be at dp[N][W]

### Dry run
taking the N = 4 and W = 7
Happiness of the 4 toys = [4, 1, 5, 7]
Weight of the 4 toys = [3, 2, 4, 5]

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/289/original/upload_be304bd2a67fc2d8a5ce4be744955f8b.png?1695932731" width=700/>

*  Initially, we filled the `dp` matrix with zeros. Now, we will fill every position one by one.
    - At i = 1, j = 1
      wt[i] = wt[1] = 3
      since wt[i] > j, dp[i][j] = dp[i - 1][j] => dp[1][1] = dp[0][1] = 0
* At i = 1, j = 2
   wt[i] = wt[1] = 3
    since wt[i] > j, dp[i][j] = dp[i - 1][j] => dp[1][2] = dp[0][2] = 0
* At i = 1, j = 3
   wt[i] = wt[1] = 3
      since wt[i] <= j, dp[i][j] = max(dp[i - 1][j], h[i] + dp[i - 1][j - wt[i]])
      => dp[1][3] = max(dp[0][2], h[1] + dp[0][0]) = max(0, 4 + 0) = 4

Similary we wil follow the above to fill the entire table.

> Time complexity for the above code is O(N * W)

> Space Complexity for the above code is O(N * W), we can furture optimize space complexity by using 2 rows. So the space complexity is O(2W) which can be written as O(W).

---
## Problem 3 Unbounded Knapsack 
## Unbounded Knapsack or 0-N Knapsack
* objects cannot be divided
* same object can be selected multiple times

### Question

Given N toys with their happiness and weight. Find more total happiness that can be kept in a bag with capacity W. Division of toys are not allowed and infinite toys are available.

### Example

N = 3; W = 8
Happiness of the 3 toys = [2, 3, 5]
Weight of the 3 toys = [3, 4, 7]

*In this case we will select second index toy 2 times. Happiness we will be 6 and weight will be 8.*

Now here as we do not have any limitation on which toy to buy index will not matter, only capacity will matter.

---


### Question
We have Weight Capacity of 100
- Values = [1, 30]
- Weights = [1, 50]

What is the maximum value you can have?

### Choices
- [ ] 0
- [x] 100
- [ ] 60
- [ ] 80


### Explanation
There are many ways to fill knapsack.

-  2 instances of 50 unit weight item.
- 100 instances of 1 unit weight item.
- 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.

We get maximum value with option 2, i.e **100**


---
## Unbounded Knapsack Dry Run



### Dry Run for Brute Force Appoarch

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/292/original/upload_ad6449c2f3d6f906c8147fdd39fd37bb.png?1695961094" width=700/>

Step 1:
* if we select toy with index 1, capacity left will be `8 - wt of toy 1 = 8 - 3 = 5`. And the happiness will be `h = 2`
* Similarily if we select toy with index 2, capacity left will be `8 - wt of toy 2 = 8 - 4 = 4`. And the happiness will be `h = 3`
* if we select toy with index 3, capacity left will be `8 - wt of toy 3 = 8 - 7 = 1`. And the happiness will be `h = 5`

Step 2:
After buying toy 1
* Now if we buy toy 1, capacity will reduce to 2 and happiness will become 4
* Similary if we buy toy 2, capacity will reduce to 1 and happiness will become 5
* We cannot buy toy 3 as the capacity will be exceeded.


We will follow similar steps to find all the possiblity.

> We will pick the toy with maximum happiness that is 6 in this case after selecting toy 2 firstly and then selecting toy 2 again.

Here we can notice optimal sub structure as well as overlapping sub problems. Thus we can apply dynamic programming.

* Unqiue states here will be` W + 1 = O(W)` because the capacity can be from 0 to W

Base case for the above question:
* if capacity is 0, happiness is 0. So, `dp[0] = 0`

Equation `dp[i] = max(h[i] + dp[i - wt[j]])` for all toys j

### Psuedocode
```java
for all i, dp[0] = 0
for (i --> 1 to W){
    for(j --> 1 to N){
        if(wt[j] <= i)
        dp[i] = max(h[i] + dp[i - wt[j]])
    }
} return dp[W]
```

### Complexity
**Time Complexity:** O(N * W)
**Space Complexity:** O(W)

---

