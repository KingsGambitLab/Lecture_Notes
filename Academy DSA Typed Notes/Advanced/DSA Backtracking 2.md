  # Backtracking 2


## Agenda
1. Print paths in staircase problem
2. Print all paths from source to destination
3. Shortest path in a matrix with huddles

---
## Problem 1 Print paths in Staircase

### Problem Statement
You are climbing a staircase and it takes **A** steps to reach the top.

Each time you can either climb **1 or 2** steps. In how many distinct ways can you climb to the top?

You need to return all the **distinct** ways to climb to the top in **lexicographical order**.

### Examples
**Input** 1:
`A = 2`

**Output** 1: `[ [1, 1], [2] ]`

**Explanation** 1:  Distinct ways to reach top: 
- 1 + 1,
- 2


**Input** 2: 
`A = 3`

**Output** 2: `[ [1, 1, 1], [1, 2], [2, 1] ]`


**Explanation** 2: Distinct ways to reach top: 
- 1 + 1 + 1, 
- 1 + 2, 
- 2 + 1.

**Note:** If you return `[1, 2]` before `[1, 1, 1]` then it will be considered wrong as it's not following the lexicographical ordering.

---
## Print paths in Staircase Approach


### Approach 
**Recursive Approach:**

We can approach this problem recursively. At each step, we have two choices:

- Take 1 step.
- Take 2 steps.

We can explore both choices recursively until reaching the top of the staircase. Whenever we reach the top (i.e., no more steps remaining), we add the current path to the list of distinct paths.

**Base Case:** 
- If there are no steps remaining **(A == 0)**, we have reached the top, so we add the current path to the list of paths.

**Handling Lexicographical ordering :** If we simply generate paths exhausting `1` before `2` it will result in the paths being generated in **lexicographical order.** 

**Example** : `[1, 1, 1]` is lexicographically smaller than `[1, 2]` which is lexicographically smaller than `[2, 1]`

**Recurrence Logic:**
- If there is at least one step remaining (A >= 1), we can continue exploring paths:
    - If there is at least 1 step remaining, we take 1 step and explore paths recursively for A - 1 steps.
    - If there are at least 2 steps remaining, we take 2 steps and explore paths recursively for A - 2 steps.

---

### Question

To **print all paths in a Staircase** using recursion, what are the recursive states to be used from the state `generatePaths(A, currentPath)`?


### Choices
- [ ] generatePaths(A - 2, currentPath + [1]) and generatePaths(A - 1, currentPath + [2]) 
- [ ] generatePaths(A - 2, currentPath + [2]) 
- [x] generatePaths(A - 2, currentPath + [2]) and generatePaths(A - 1, currentPath + [1]) 
- [ ] generatePaths(A - 1, currentPath + [1]) 


### Explanation:

According to our understanding we have two options standing on some stair : 
- **Take 1** step : `generatePaths(A - 1, currentPath + [1])`
- **Take 2** steps : `generatePaths(A - 2, currentPath + [2])`

To generate all paths, you need to consider both recursive states. Therefore, the correct answer is:

`generatePaths(A - 2, currentPath + [2]) and generatePaths(A - 1, currentPath + [1])`

The entire pseudo code will look as follows.

---
### PseudoCode:
```cpp
function generatePaths(A, currentPath, allPathsAnswer) {
    // Base case: if remaining steps is 0, add the current path to the list of paths
    if (A == 0) {
        allPathsAnswer.append(currentPath);
        return;
    }
    
    // If remaining steps is positive, continue exploring paths
    if (A >= 1) {
        currentPath.append(1); // Take 1 step
        generatePaths(A - 1, currentPath, paths);
        currentPath.pop_back(); // Backtrack
    }
    if (A >= 2) {
        currentPath.append(2); // Take 2 steps
        generatePaths(A - 2, currentPath, paths);
        currentPath.pop_back(); // Backtrack
    }
}

function WaysToClimb(A) {
   initialize list of list allPathsAnswer -> final answer;
   
    initialise an empty list curpath;

   generatePaths(A, curpath, allPathsAnswer);
   return allPathsAnswer;
}
```

### Complexity Analysis 
**Time Complexity :  O(2^N^) to generate all paths**
**Space Complexity : O(N) stack memory**

Where **N** is the number of total stairs



---
## Problem 2 Print all paths from source to destination


### Problem Statement
You are given the dimensions of a rectangular board of size **A x B**. You need to print **all the possible paths** from **top-left** corner to **bottom-right** corner of the board.

You can only move **down** (denoted by '**D**') or **right** (denoted by '**R**') at any point in time.

You have to print the paths in **lexicographical order.**

### Examples
**Input** 1 : 
`A = 3 , B = 2`

**Output** 1 : `DDR DRD RDD`

**Explanation** 1: The size of the matrix is 3x2.
You are currently standing at (0, 0), the possible paths to bottom right cell (2, 1) are : 
- (0, 0) -> (1, 0) -> (2, 0) -> (2, 1)  which corresponds to DDR
- (0, 0) -> (1, 0) -> (1, 1) -> (2, 1)  which corresponds to DRD
- (0, 0) -> (0, 1) -> (1, 1) -> (2, 1)  which corresponds to RDD

**NOTE** : Printing DRD, RDD before DDR would be incorrect as the output should be given in Lexicographical order. 



**Input** 2 : 
`A = 1 , B = 2`

**Output** 2 : `R`


**Explanation** 2: The size of the matrix is 1x2.
You are currently standing at (0, 0), the possible paths to bottom right cell (0, 1) are : 
- (0, 0) -> (0, 1)  which corresponds to R

This is the only possible path.

---
## Print all paths from source to destination Approach


### Approach
Let's solve it using recursion :

- We start at the top left corner of the maze and recursively call the function for both horizontal and vertical movements until we reach the bottom right corner of the maze.
- To implement this, we define a function called **printMazePaths** that takes **four** arguments:
    - the **current** **row** and **column** (say **sr** and **sc**), the **destination row and column** (say **dr** and **dc**), and a string for storing **path travelled so far** (say **psf**).
- At each step, we check if we have reached the destination or not : 
    - If we have, we simply **print the path**.
    - If not, we make two recursive calls, one for moving horizontally and one for moving vertically.

- **Base case** : When we have either gone beyond the boundaries of the maze or when we have reached the destination. In both cases, we simply **return** without doing anything.

---


### Question

To print all paths in **lexicographical order** the easiest way is to ?


### Choices
- [ ] Generate those paths first, which exhaust  **right** moves before **down** moves
- [x] Generate those paths first, which exhaust  **down** moves before **right** moves
- [ ] Generate all paths first in any order then, then **sort** them treating as strings 
- [ ] Generate paths going down / right in random order

### Explanation:

To print the paths in lexicographical order, the paths need to be sorted. But, generating all paths and then sorting the paths won't be efficient.

**Observation :** Notice that the letter **D** is lexicographically smaller than **R**. This means that sorting the string would bring all **D** to the front and push all **R** to the back.

- Option 2 : is the correct answer because lexicographical order is similar to dictionary order, where 'down' moves (D) should be considered before 'right' moves (R) if they were characters in a string.

**Answer :** So exhausting **D** moves before **R** is out answer. 

The entire pseudo code will look as follows.

### PseudoCode : 
```cpp
function print_maze_paths(sr, sc, dr, dc, psf, ans):
    if sr > dr or sc > dc:
        return
    if sr == dr and sc == dc:
        ans.add(psf) // add the path so far to ans
        return

    # First explore paths going D to build in lexicographical order
    
    print_maze_paths(sr + 1, sc, dr, dc, psf + "D", ans)  
    
    print_maze_paths(sr, sc + 1, dr, dc, psf + "R", ans)

function PrintAllPaths(self, A, B):
    ans = [] // empty list 
    print_maze_paths(0, 0, A - 1, B - 1, "", ans)
    return ans
```

### Complexity Analysis 
**Time Complexity :  O(2^N+M^) to generate all paths**
**Space Complexity : O(N+M) stack memory**

Where **N and M** are the dimensions of matrix

---
## Problem 3 Shortest path in a Binary Maze with Hurdles


### Problem Statement
Given an **MxN** matrix where each element can either be **0** or **1**. We need to find the length of **shortest path** between a given **source** cell to a **destination** cell.

A cell with value **0** denotes that it's a hurdle. The path can only be created out of the cells with values **1**.

If **NO** path exists then print -1.

### Examples 
**Input** 1 : 
```javascript!
       0  1  2  3
A = 0[[1, 1, 0, 0],
    1[0, 1, 1, 0],
    2[0, 0, 1, 1],
    3[0, 0, 0, 1]]
B = 0, C = 0
D = 3, E = 3
```


**Output** 1 : `6`

**Explanation** 1: The only valid shortest path is (0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2) -> (2,3) -> (3,3) 


**Input** 2 : 
```ruby
       0  1  2
A = 0[[1, 1, 1],
     1[1, 0, 1],
     2[1, 1, 1]]
B = 0, C = 0
D = 0, E = 2
```

**Output** 2 : `2`


**Explanation** 2: One of the shortest paths is (0,0) -> (0,1) -> (0,2) 


**Input** 3 : 
```javascript
A = [[1, 0, 1],
     [1, 0, 1],
     [1, 0, 1]]
B = 0, C = 0
D = 0, E = 2
```

**Output** 3 : `-1`


**Explanation** 3: There is no path so we print **-1** instead. 

### Approach 

**Let's solve this problem using DFS Backtracking approach**
1. Start from the given source cell in the matrix and explore all four possible paths.
2. Check if the destination is reached or not.
3. Explore all the paths and backtrack if the destination is not reached.
4. And also keep track of visited cells using an array.

### Implementation Approach
- **Explore Path Function**: Define a recursive backtracking function explores all possible paths from the current cell (i, j) to the destination cell (D, E).

- **Recursive Idea**:
    - For each possible direction (right, down, left, up): Calculate the next cell coordinates.
    ```
    All directions are:
     left: (i, j) ——> (i, j – 1)
     right: (i, j) ——> (i, j + 1)
     up: (i, j) ——> (i - 1, j)
     down: (i, j) ——> (i + 1, j )
     ```
    - Check if the next cell is within the matrix boundaries, is not an obstacle (value is 1), and has not been visited yet.
    - Mark the next cell as visited and recursively call the same function with the next cell and increment the path length.
    - Backtrack by marking the next cell as unvisited to explore other potential paths.

- Define **Shortest Path Function**: 
    - Initialize the visited matrix to keep track of visited cells during the exploration.
    - Mark the source cell as visited.
    - Start the path exploration from the source cell using the **Explore Path** function.
    - After the exploration, check if **FinalAnswer** has been updated. If not, return **-1** indicating no path was found; otherwise, return the **FinalAnswer**.

- **Base Case** : If the current cell say **(i, j)** is the destination cell **(D, E)**, update the **FinalAnswer** with **minPath** with the current path length if it is shorter than the previously recorded path length.

---


### Question

Say that you are currently inside the matrix on the `cell[i][j]` with value 1. What are the conditions neccesary to go to `cell[i + 1][j]` ?


### Choices
- [ ] `cell[i + 1][j] == 1`
- [ ] `cell[i + 1][j] == 1 and i < number of rows`
- [ ] `i < number of rows` 
- [x] `cell[i + 1][j] == 1 and i + 1 < number of rows`

### Explanation


To move from cell[i][j] to cell[i+1][j], the following conditions must be satisfied:

1. `cell[i + 1][j]` must not have a hurdle i.e. have the value 1.
2. `i + 1` must be within the bounds of the matrix, i.e., `i + 1` should be less than the total number of rows.


Thus, the correct condition is `cell[i + 1][j] == 1 and i + 1 < number of rows`.

The entire pseudo code will look as follows.

---

### PseudoCode: 

```cpp 
declare common variable FinalAnswer 

// up, down, right, left

row[] = {-1, 1, 0, 0}
col[] = {0, 0, 1, -1}

function explore_path(A, visited, i, j, D, E, path_length):
    if i == D and j == E:
        FinalAnswer = min(FinalAnswer, path_length)
        return

    for k -> 0 to 3:
        ni = i + row[k]
        nj = j + col[k]
        if 0 <= ni < rows and 0 <= nj < cols and A[ni][nj] == 1 and not visited[ni][nj]:
            visited[ni][nj] = True
            explore_path(A, visited, ni, nj, D, E, path_length + 1)
            visited[ni][nj] = False  # Backtrack


function FindShortestPath(A, B, C, D, E):
    FinalAnswer = infinity
    N = len(A)
    M = len(A[0])

    initialise `visited` matrix with false values of size (N x M)
        
    visited[B][C] = True
     explore_path(A, visited, B, C, D, E, 0)

    return  FinalAnswer if  FinalAnswer != infinity else -1
```

### Complexity Analysis 
**Time Complexity :  O(4^N*M^)** because in worst case we can have all cells valid and we have to explore 4 choices for each of the N * M cells

**Space Complexity : O(N*M) stack memory**

Where **N and M** are the dimensions of matrix

> Bonus, this can also be solved efficiently using BFS
