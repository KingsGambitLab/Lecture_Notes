# Backtracking 1

## What is Bracktracking ?

The above process is known as **Backtracking**.

Let's try to understand the concept of backtracking by a very basic example. We are given a set of words represented in the form of a tree. The tree is formed such that every branch ends in a word.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/170/original/backtracking1.jpeg?1696932758" width="500" />

Our task is to find out if a given word is present in the tree. Let's say we have to search for the word **AIM**. A very brute way would be to go down all the paths, find out the word corresponding to a branch and compare it with what you are searching for. You will keep doing this unless you have found out the word you were looking for.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/171/original/backtracking2.jpeg?1696932836" width="500" />

In the diagram above our brute approach made us go down the path for ANT and AND before it finally found the right branch for the word AIM.

The backtracking way of solving this problem would stop going down a path when the path doesn't seem right. When we say the path doesn't seem right we mean we come across a node which will never lead to the right result. As we come across such node we back-track. That is go back to the previous node and take the next step.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/172/original/backtracking3.jpeg?1696932854" width="500" />

In the above diagram backtracking didn't make us go down the path from node N. This is because there is a mismatch we found early on and we decided to go back to the next step instead. Backtracking reduced the number of steps taken to reach the final result. This is known as pruning the recursion tree because we don't take unnecessary paths.

---
## Problem 1 Print Valid Parenthesis


### Problem Statement
Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.

A = 3
[ "((()))", "(()())", "(())()", "()(())", "()()()" ]

### Explanation

As shown in the picture below: ) is an invalid string, so every string prefixed with it is also invalid, and we can just drop it.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/173/original/5.png?1696932991" width="500" />

To ensure that the current string is always valid during the backtracking process, we need two variables `left_count` and `right_count` that record the number of left and right parentheses in it, respectively.

Therefore, we can define our recursive function as `solve(cur_string, left_count, right_count)` that takes the current string, the number of left parentheses, and the number of right parentheses as arguments. This function will build valid combinations of parentheses of length 2n recursively.

The function adds more parentheses to cur_string only when certain conditions are met:

* If **`left_count < n`**, it suggests that a left parenthesis can still be added, so we add one left parenthesis to cur_string, creating a new string new_string = cur_string + (, and then call `solve(new_string, left_count + 1, right_count)`.

* If **`left_count > right_count`**, it suggests that a right parenthesis can be added to match a previous unmatched left parenthesis, so we add one right parenthesis to cur_string, creating a new string new_string = cur_string + ), and then call solve(new_string, left_count, right_count + 1).

This function ensures that the generated string of length 2n is valid, and adds it directly to the answer. By only generating valid strings, we can avoid wasting time checking invalid strings.

---
## Print Valid Parenthesis Dry Run and Pseudocode


### Dry Run for N = 2, means overall length will be 4.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/059/943/original/Screenshot_2023-12-21_at_7.38.01_PM.png?1703167693" width="500"/>

- Here **"(())" and "()()"** are valid answers.

### PseudoCode
```cpp=
function solve(str, N, opening, closing){ //also taking given N value in parameter
    // base case
    if(str.length == 2N){
        print(str);
        return;
    }
    if(opening < N){
        solve(N, str+'(' , opening+1, closing)
    }
    if(closing < opening){
        solve(N, str+')' , opening, closing+1)
    }
}
```

### Complexity
- **Time Complexity:** O(2<sup>N</sup>)
- **Space Complexity:** O(N)

---
## Definition of Subset and Subsequences


### Definition of Subset and Example
A subset is often confused with subarray and subsequence but a subset is nothing but any possible combination of the original array (or a set).

For example, the subsets of array arr = [1, 2, 3, 4, 5] can be:

[3, 1]
[2, 5]
[1, 2], etc.
So, we can conclude that subset is the superset of subarrays i.e. all the subarrays are subsets but vice versa is not true.

### Definition of Subsequence and Example
As the name suggests, a subsequence is a sequence of the elements of the array obtained by deleting some elements of the array. One important thing related to the subsequence is that even after deleting some elements, the sequence of the array elements is not changed. Both the string and arrays can have subsequences.

The subsequence should not be confused with the subarray or substring. The subarray or substring is contiguous but a subsequence need not to be contiguous.

For example, the subsequences of the array arr : [1, 2, 3, 4] can be:

[1, 3]
[2, 3, 4]
[1, 2, 3, 4], etc.

Note: A subarray is a subsequence, a subsequence is a subset but the reverse order is not correct.

---
## Problem 2 Subsets


Given an array with distinct integers. Return  all the subsets using recursion.

### Example

**Input:** [1, 2, 3]
**Output:** {[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]}

Total Subsets possible are **2^N** 
For every element, there can be two options:
- It is **considered** as part of a subset
- It is **not considered** as part of a subset

Say there are **3 elements**, for each of them we have above two options, hence **2 * 2 * 2 = 2^N^** are the total options.

### Approach

The approach to solve the problem is to use backtracking. 

For each element, I have two choices whether to keep it or not, I execute my choice and then ask recursion to do the remaining work.

Let us take an example of `[1, 2, 3]`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/611/original/Screenshot_2023-10-14_at_12.48.48_PM.png?1697267948" width="500"/>


### Psuedocode

```cpp=
initialize ans list;

function subsets(list A, list currset, idx){

    //base case
    if(idx == A.size){
        ans.add(currset);
        return;
    }

    //for every ele in A, we have 2 choices 

    //choice 1 : keep it in currset
    currset.add(A[idx]);
    subsets(A, currset, idx+1);

    //choice 2 : Don't keep it in currset
    currset.remove_back();
    subsets(A, currset, idx+1);
}
```

### Dry Run
A = {2, 6, 9}

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/621/original/IMG_ACCE165F2ED6-1.jpeg?1697272534" width="800"/>

Continued

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/053/622/original/IMG_7A8C88629961-1.jpeg?1697272592" width="800"/>

### Complexity 
- **Time Complexity:**  O(2^N^)
- **Space Complexity:** O(N)

### NOTE: 
* *For producing individual sorted subsets, we need to sort the given array first. We will get the desired result with this since elements are being processed in sequence.* 
* *Moreover, if it is asked to sort the final array, then once we have generated all subsets, we can sort answer array before returning.*

### Psuedocode for getting sorted 

```cpp=
initialize ans list;
function subsets(list A, list currset, idx){

    //base case
    if(idx == A.size){
        ans.add(currset);
        return;
    }

    //for every ele in A, we have 2 choices 

    //choice 1 : keep it in currset
    currset.add(A[idx]);
    subsets(A, currset, idx+1);

    //choice 2 : Don't keep it in currset
    currset.remove_back();
    subsets(A, currset, idx+1);
}
```

---


### Question
What is the count of total permutations of a string with unique characters? (N=String length)

### Choices

- [ ] N$^2$
- [ ] N + (N + 1) / 2
- [ ] N * (N - 1) / 2
- [x] N!

---
## Fitness Meets Variety

### Problem

A popular Fitness app **FitBit**, is looking to make workouts more exciting for its users. The app has noticed that people get bored when the same exercises are shown in the same order every time they work out. To mix things up, **FitBit** wants to show all the different ways the exercises can be arranged so that each workout feels new.

Your challenge is to write a program for **FitBit** that takes a string **A** as input, where each character in the string represents a different exercise. Your program should then find and display all possible arrangements of these exercises.

**Example:**
A = Push-ups
B = Squats
C = Burpees
D = Planks

Then different ways of doing the exercise includes -
ABCD
ACBD
ADBC
ADCB
.
.
etc...

This problem is same as getting permutations.

---
## Problem 3 Permutation

Given a string with distinct elements. Print all permutations of it without modifying it. 

### Example
For string **abc**, of length 3, we have total 3! = 6 permutations:
- abc
- acb
- bac
- bca
- cab
- cba

**Input:** abc
**Output:** abc acb bac bca cab cba


### Constraint
We don't have duplicate characters in a string.

---
## Permutations Idea

- Every permutation has n number of characters, where n is the length of the original string.
- So initially we have n number of empty spots.
`_ _ _`
- And we need to fill these empty spots one by one.
- Let us start with the first empty spot, which means from the 0th index.
- For the 0th index we have three options, `a, b, and c`, any of the three characters can occupy this position.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/171/original/upload_0abf2bd81e5b53817696c11f014cc9ca.png?1697613060" width="300"/>

- If `a` will occupy 0th index, then we have `a _ _`, and if `b` will occupy 0th index, then we have `b _ _`, and if `c` will occupy 0th index, then we have `c _ _`,

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/172/original/upload_364bad15c465630226ebbc98779a6d3c.png?1697613083" width="400"/>

- Now the first spot is occupied, now we have to think about the second spot.
- Now for a second spot we have only options left.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/174/original/upload_2a38e8136fc2617770465018b5af1300.png?1697613113" width="400"/>

- Now when the character occupies the second spot, then we get.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/175/original/upload_66f805654ae3f8cd1fda572e55b0c34a.png?1697613142" width="500"/>

- Now for the last spot, every string has left with a single character, like in `a b _`, we are only left with the character `c`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/177/original/upload_436a54570d0816cdfe3aa5e8bbfabe51.png?1697613229" width="500"/>


- Now this character will occupy the last spot.


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/178/original/upload_6c85f4358549b98ac08cf4f97c8171a8.png?1697613260" width="500"/>

We are setting characters at positions one by one. So **We need to keep track of visited/used characters.**

---
## Permutations PsuedoCode


```cpp
function permutations1(character arr[], idx, ans[N], visited[N]){
    if(idx == arr.length){
        print(ans[])
        return
    }
    for(i -> 0 to N - 1){ // All possibilities
        if(visited[i] == false){ // valid possibilities
            visited[i] = true;
            ans[idx] = arr[i];
            permutations1(arr, idx + 1, ans, visited); // recursive call for next index
            visited[i] = false; //undo changes
        }
    }
}
```

---
## Permutations - Dry Run


Let us suppose we have the string `arr[] = a b c` , and initially ans array is empty, `ans[] = _ _ _`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/179/original/upload_078759cd3474f5320a513fb2a368988b.png?1697613308" width="300"/>


- Initially, we are at index 0, 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/180/original/upload_09b0f2e04af2646653401912f7bdf11e.png?1697613336" width="300"/>

- Now i vary from 0 to `n-1`, so it will go from 0 to 2, as here the length of the string is 3.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/181/original/upload_6a469a8219e1a655017a207a21d09a20.png?1697613366" width="400"/>

- Now when `i = 0`, we will check that `visited[i] == false`, so this condition is true, we mark `visited[i] == true` and `ans[0] = arr[0] = a`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/182/original/upload_e4640b1635abf383ca90d29bc8d5c358.png?1697613396" width="300"/>

- Now it makes a recursive call for the next index, `permutations1(arr, 1, ans, visited)`

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/183/original/upload_88edd4512c97a6dde2d3c315f711e918.png?1697613421" width="500"/>

- Inside this call, `idx != arr.length`, so we will continue further, now inside this call, the loop will go from 0 to 2.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/184/original/upload_0d20be040bcf8c504abc12224bcadd57.png?1697613451" width="400"/>

- But in case `i = 0`, now `visited[0] != false`, so in this iteration we will not enter inside the if condition, i will simply get incremented.


- Now `i = 1`,  we will check that `visited[i] == false`, so this condition is true, we mark `visited[1] == true` and `ans[1] = arr[1] = b`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/185/original/upload_b27ef00f4cf93cd4b7f09cc8dbe9aa2e.png?1697613482" width="300"/>

- Now it will make recussive call for `idx + 1`, `permutations1(arr, 2, ans, visited)`

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/186/original/upload_576781e6dedc3c669d373a23b090798c.png?1697613508" width="400" />

- Now inside this new recursive again loop will run from 0 to 2.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/187/original/upload_fde4ce4ddcc35d80971d5cd59443ecea.png?1697613538" width="400" />

- Now when `i = 0`, now `visited[0] != false`, so in this iteration, we will not enter inside the if condition, i will simply get incremented.
- Now `i = 1`, again `visited[1] != false`, so in this iteration, we will not enter inside the if condition, i will simply get incremented.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/188/original/upload_359a967fc34e931c591a6a1905528841.png?1697613567" width="400" />

- Now `i = 2`,  we will check that `visited[i] == false`, so this condition is true, we mark `visited[2] == true` and `ans[2] = arr[2] = c`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/190/original/upload_a58c34a007477508cf23705adccd3cbf.png?1697613618" width="200" />

- Now it will make recussive call for `idx + 1`, `permutations1(arr, 3, ans, visited)`

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/191/original/upload_bbfc59007f79a5a86ba08ac548919790.png?1697613649" width="400"/>

- Inside this call, our `idx == arr.length`, so print `ans`, so **abc will be printed**, and it will return. And after returning `visited[2] = false`.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/192/original/upload_07d6ae1b0fed0c6bedfc84b683e474d0.png?1697613689" width="400" />


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/193/original/upload_11c5e9b4db673d5f7ea44a7a032efa05.png?1697613725" width="300" />


- Now for `arr, 2, ans, visited`, all iterations are completed. So it will also return and `visited[1] = false`

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/194/original/upload_0028a2144ea0380f98c6647b95f62530.png?1697613757" width="400" />

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/195/original/upload_f50656c21e03faf10aaadd839d20ea50.png?1697613780" width="300" />


- Now for `arr, 1, ans, visited`, we are left for the iteration `i = 2`, so it will check for `visited[i] == false`, as `visited[2] = false`, so go inside the if condition and `visited[2] == true` and `ans[1] = arr[2] = c`

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/196/original/upload_a978fb05a4dac41b99dfcb5a635d3b67.png?1697613812" width="250" />

- Now it will make the recursive call for `arr, 2, ans, visited`. And inside this call again loop will run from 0 to 2. Now `visited[0] == true`, so it will for `i = 1`, and so it will check for `visited[i] == false`, as `visited[1] = false`, so go inside the if condition and `visited[1] == true` and `ans[2] = arr[1] = b`


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/197/original/upload_25cac80b472a378908a107f9a9a6bdb0.png?1697613836" width="300" />

- Now it will make recussive call for `idx + 1`, `permutations1(arr, 3, ans, visited)`

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/198/original/upload_7444728790ca1e74595a2c3d3aaeae07.png?1697613863" width="400"/>

- Now inside this call `idx == arr.length`, so it will print `ans`, so **acb will be printed**, and it will return.

In this way, all the permutations will be printed.

