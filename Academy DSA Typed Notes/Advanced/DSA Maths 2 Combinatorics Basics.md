# Maths 2: Combinatorics Basic


## Agenda

* Addition and Multiplication Rule
* Permutation basics
* Combination basics and properties
* Pascal Triangle
* Find N-th column title

---
## Addition and Multiplication Rule Example 1


### Example - 1

Given 10 girls and 7 boys, How many different pairs can be formed?

**Note: pair = 1 boy + 1 girl**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/402/original/upload_16c7dda2cfb92de07aa0da616c14e6fa.png?1697695941" width="500"/>

Since each pair consists of one boy and one girl, you can pair each of the 7 boys with any of the 10 girls. This results in a total of 7 boys × 10 girls = 70 different pairs that can be formed.

---
## Addition and Multiplication Rule Example 2

### Example - 2

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/403/original/upload_df4cecb847475f527b0b065f450e1ee4.png?1697695989" width="500"/>


**Approach:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/404/original/upload_3288e1ad8ab8bf9dfbab49e8176bcf58.png?1697696013" width="500"/>

To reach Agra via Delhi from Pune, you can combine the ways to get from Pune to Delhi (3 ways) with the ways to get from Delhi to Agra (2 ways).

So, the total number of ways to reach Agra via Delhi from Pune is:

3 ways (Pune to Delhi) * 2 ways (Delhi to Agra) = 6 ways.

---


### Question

No. of ways of reaching Agra from Pune ?
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/640/original/Screenshot_2023-10-21_at_12.15.51_PM.png?1697870821" width="400" />

### Choices

- [ ] 72
- [ ] 12
- [x] 18
- [ ] 20

### Explanation

To go to Pune to delhi , there are 3 ways. And do go from delhi to agra there are 4 ways. From pune to Mumbai there are 2 ways, from Mumbai to agra there are 3 ways.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/406/original/upload_083f6fd771433dbecded9b1766c41221.png?1697696156" width="500"/>

To calculate the number of ways to reach Agra from Pune through different routes, you need to consider the combination of routes from Pune to Delhi and from Delhi to Agra, as well as the routes from Pune to Mumbai and from Mumbai to Agra. Then, you can add these possibilities together.

From Pune to Delhi, there are 3 ways.
From Delhi to Agra, there are 4 ways.

From Pune to Mumbai, there are 2 ways.
From Mumbai to Agra, there are 3 ways.

So, to find the total number of ways to reach Agra from Pune via these routes, you add the possibilities:

(3 ways from Pune to Delhi * 4 ways from Delhi to Agra) + (2 ways from Pune to Mumbai * 3 ways from Mumbai to Agra) = $(3 * 4) + (2 * 3) = 12 + 6 = 18$ ways.

There are 18 different ways to reach Agra from Pune through these routes.

* (Multiplication) = AND: Used when counting possibilities that occur together in sequence.
* (Addition) = OR: Used when counting possibilities that occur in separate ways.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/411/original/upload_f652c91e49444d681f084737296d046d.png?1697696353" width="500"/>

---
## Most Varied Meal Combo

### Scenerio
**Zomato**, features an exciting option for its users - meal combos. Each combo includes one main course, one *dessert*, and one *beverage*, offering a complete dining experience from various restaurants. Zomato believes that a greater variety of combos can significantly enhance customer satisfaction.

### Problem Statement

You're tasked with helping **Zomato** identify which restaurant offers the most variety in its meal combos. You're provided with a list, shaped like a grid or a 2D matrix **A**, where each row corresponds to a different restaurant's offerings. 

Each row is divided into three parts: 
1. A[i][0] tells you the number of main courses, 
2. A[i][1] the number of desserts, and 
3. A[i][2] the number of beverages a restaurant offers.

Your challenge is to analyze this data and pinpoint which restaurant gives its customers the most options to mix and match their meal combo.

### Examples
#### Example 1 : 
```csharp
A = [
    [3, 2, 2],   # Restaurant 1
    [4, 3, 3],   # Restaurant 2
    [1, 1, 1]    # Restaurant 3
]
```
#### Output  :    $2$
#### Explanation for input 1 : 
- Restaurant 1 offers 12 combos (3 mains x 2 desserts x 2 beverages)
- Restaurant 2 offers 36 combos (4 mains x 3 desserts x 3 beverages)
- Restaurant 3 offers 1 combo (1 main x 1 dessert x 1 beverage)

So, Restaurant 2 provides the most variety with 36 possible combinations.

### Solution
1. **Understanding the Combinations:** The number of ways to form a meal combo at each restaurant is determined by the product of the number of main courses, desserts, and beverages. This is based on the combinatorial principle where each choice of a main course can be combined with each choice of a dessert and each choice of a beverage.


2. **Iterating through Restaurants:** For each restaurant (each row in the matrix):
    - Multiply the numbers from the three columns together (main courses x desserts x beverages).
    - This product gives the total number of unique meal combos that can be created using the menu items listed by the restaurant.


3. **Tracking Maximum Variety**: As you compute the number of possible combinations for each restaurant, you need to keep track of which restaurant has the highest number. This involves:
    - Maintaining a variable to store the maximum number of combinations found so far.
    - Keeping an index or identifier for the restaurant that offers these maximum combinations.

4. **Result**: After evaluating all the rows, the restaurant with the highest product (representing the maximum number of meal combos) is identified as offering the most variety.


---
## Permutation


### Explanation

Permutation is defined as the arrangements of objects. In permutation, **order matters**. To simplify `(i, j) != (j, i)`

### Example - 1

Given 3 distinct characters, in how many ways can we arrange them?

**Approach:**

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/413/original/upload_7568dff00780afa54e072374f327036d.png?1697696426" width="500"/>

---


### Question

In how many ways n distinct characters can be arranged?

### Choices

- [ ] N * (N + 1) / 2
- [x] N! (N Factorial)
- [ ] N ^ 2
- [ ] N


### Explanation:

N distinct characters can be arranged in n! (n factorial) ways. This means that for each distinct character you have, you can multiply the total number of arrangements by the count of characters. Here's the formula:

---
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/449/original/N!.png?1697704088" width="500"/>

---
## nPr Formulae

### Example - 2

Given N distinct characters, in how many ways you can arrange R out of N distinct chracters?

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/450/original/nPr.png?1697704431" width="500"/>

**Approach:**

When arranging 2 distinct characters from a set of 4, and order matters (e.g., AB and BA are considered different arrangements), the number of ways is indeed $4 * 3 = 12$ ways.

When arranging **R** characters out of **N** distinct characters:

* For the first position, you have **N** choices
* For the second position, since you've used one character, you have **N-1** choices.
* For the third position, you have **N-2** choices, and so on.

This continues until the **R-th** position, for which you have $N-(R-1)$ choices.

Thus, the total number of ways to arrange **R** characters out of **N** distinct characters is `N ∗ (N − 1) ∗ (N − 2) ∗ ... ∗ (N − (R − 1))`.



<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/415/original/upload_63876d8d7294076b99a93712b6c490f4.png?1697696591" width="500"/>




Here:

* **n** is the total number of distinct characters.
* **r** is the number of characters you want to arrange.
* **nPr** represents the permutations of **n** items taken **r** at a time.

---
## Combination


### Explanation

Combination is defined as the number of ways to select something.

**Note:** In combination, **order of selection does not matter**. To simplify `(i, j) = (j, i)`


### Example - 1

Given 4 players, count the number of ways of selecting 3 players.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/416/original/upload_2220fb8671ac7d6ddf6020bad13d7a26.png?1697696630" width="500"/>

### Example - 2

Given 4 players, write the number of ways to arrange players in 3 slots

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/417/original/upload_437149b5f107414c3e9c7de3abaab121.png?1697696655" width="500"/>

* **Number of Selections (x):** You are selecting 3 players out of 4, which is represented as **4C3**, and it equals 4.
* **Number of Arrangements in Each Selection (6):** There are 3! (3 factorial) ways to arrange 3 players within 3 slots, which is 6.
* **Total Number of Arrangements:** Multiply the number of selections by the number of arrangements in each selection:

Number of Selections * Number of Arrangements in Each Selection = $4 * 6 = 24$

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/418/original/upload_640820c7d18e2637883e9bf2cf19f1ad.png?1697696708" width="500"/>


---
## nCr Formulae


### Example - 3

Given **n** distinct elements, in how many ways we can select **r** elements s.t `0 <= r <= n`

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/419/original/upload_8d51bb5d67f2e1164fb4455f0514a47a.png?1697696754" width="500"/>

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/420/original/upload_39ee568b2cb0325e3e13071203ebeaa6.png?1697696789" width="500"/>

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/421/original/upload_45755c9cfa7b404d5cfe1a348e9b800d.png?1697696823" width="500"/>


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/422/original/upload_e304bd1176a20d8529433879998f60c9.png?1697696867" width="500"/>

---
## Properties of Combination


### Property - 1 

The number of ways of selecting **0** items from **N** items, i.e. number of ways to **not select anything**, will always be **1**. 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/423/original/upload_593decf3cd709e2904f9238a8641f134.png?1697696921" width="500"/>

### Property - 2

The number of ways of selecting **n** items from **n**, i.e. number of ways to **select everything** will also be **1**.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/424/original/upload_329467ded9b7afdc7a63d51f5e237fa2.png?1697696949" width="500"/>


### Property - 3

Number of ways of selecting **(n-r)** items from **n**:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/426/original/upload_0d1e20a0920a46798d66c9421f0d58dd.png?1697697011" width="500"/>

---
## Special Property


### Property - 4

Given **n** distinct elements, select **r** items:

For each elements, we have 2 options, either to select or not select:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/428/original/upload_872a1a64f356a30283360e845c6aef3a.png?1697697049" width="500"/>

**Select Case:**
When you choose to "select" an element from the available n distinct elements, it means that you are including that specific element as one of the r items you want to pick. In this case:

* You decrease the number of items you need to select by 1, so it becomes r - 1.
* You decrease the total number of available elements by 1, as you've already chosen one element, so it becomes n - 1.
* You continue the selection process, considering the reduced values of r and n.

**Reject Case:**
When you choose to "reject" an element, it means that you are not including that particular element as part of your selection. In this case:

* You keep the number of items you need to select the same, which remains as r.
* You decrease the total number of available elements by 1, as you've decided not to choose one element, so it becomes n - 1.
* You continue the selection process with the same value of r and the reduced value of n.

---
## Problem 1 Pascal Triangle


### Pascal Triangle
### Problem Description

Generate Pascal's triangle for given value of `n`.

### Example

Pascal Triangle for `n = 4` is given below

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/430/original/upload_b7eeb6693170725bdea0966e6ffc36d7.png?1697697147" width="500"/>

**Brute Force:** For each and every value, calculate the factorial and print it.

`c[i][j]` represents the element in the i-th and j-th column. Each element is the sum of the two numbers directly above it from the previous row. In combinatorial terms, `c[i][j]` indicates the number of ways to choose j items from a set of i items without repetition and without order.

But as we know that, factorial grows very fast as the number increases, hence this approach won't work properly.

### Optimized Approach

* Pascal's Triangle elements are calculated using `c[i][j] = c[i - 1][j] + c[i - 1][j - 1]`, summing elements from the row above.
* Start with `c[0][0] = 1`, forming the foundation of the triangle. 
* Calculate rows iteratively using the relation, reusing previous row values to minimize redundant calculations.
* Utilize only two rows (previous and current) to calculate and update elements, saving memory.
* Print each row's elements to see Pascal's Triangle emerge from the calculated values.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/431/original/upload_7497467fe55b22426bb897d29269c1c5.png?1697697410" width="500"/>

### Pseudo Code

```java 
function pascalsTriangle(n) {
    nCr[n][n] = {0};
    for (i -> 0 to n) {
        nCr[i][0] = 1;
        nCr[i][i] = 1;
        for (j -> 1 to i - 1) {
            nCr[i][j] = nCr[i-1][j] + nCr[i-1][j-1];
            // If mentioned in the question to take % M then:
            // nCr[i][j] = (nCr[i-1][j] + nCr[i-1][j-1]) % M;
        }
        return nCr;
    }
}
```

### Complexity
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(N^2)$

---
## Problem 2 Finding N-th column title


### Problem Description

Find the n-th column title, the columns are titled as A, B, C... and after Z, it is AA, AB, AC... and so on. Given the column number, find the title of the column.


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/435/original/upload_a4a321d8e25bd825591baf4bb16ceb8b.png?1697697568" width="500"/>

Base for mapping A-Z will be 26

### Example

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/436/original/upload_ac79c11bd69ab4ca16e15931c263e9e7.png?1697697604" width="500"/>

### Approach

* Start with the given number **n**.
* For each digit of the column title (from right to left):
   * Find the remainder when **n** is divided by 26.
   * Map the remainder to the corresponding letter ('A' to 'Y' for 1-25, 'Z' for 0).
   * Append the letter to the Excel column title.
   * Divide **n** by **26** (integer division) to process the next digit.
* Repeat step 2 until n becomes zero.
* The resulting string is the Excel column title for the original number n.


### Code
```java 
function columnTitle(n) {
    ans = "";
    while(n > 0) {
        ans = (char) ((n - 1) % 26 + 'A') + ans; // char + string
        n = (n - 1) / 26
    }
    return ans
}
```

### Complexity
**Time Complexity:** O(log(N)) [base 26]
**Space Complexity:** O(1)

