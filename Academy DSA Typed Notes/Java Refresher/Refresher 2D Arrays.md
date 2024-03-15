# Refresher : 2D Arrays



# 2D Arrays
- Store similar types of items
- Sequential storage of elements 
- It has both length and breadth

## Real-Time Application Example of 2D Arrays
- Chess
- Theatre Seats
- Bus
- Egg Tray
- Tic Toe Game

## Syntax

```cpp
int mat[][] = new int[row][col];
```
In 2D arrays, we have square brackets in the declaration but in the 1D array we use one square bracket to declare it(`int[] ar=new int[]`) and in 2D matrix declaration first bracket is used to specify the number of rows and second is for the number of columns.



||||Rows||
|-|-| -------- | -------- | -------- |
|| |&darr; |&darr;  |&darr;  |
||&rarr;|**-**|**-**|**-**|
|**Columns**|&rarr;|**-**|**-**|**-**|
||&rarr;|**-**|**-**|**-**|

In the above matrix, we have 3 rows and 3 columns.


## Example
|-|-|-|-|
|-|-|-|-|
|**-**|**-**|**-**|**-**|
|**-**|**-**|**-**|**-**|

In the above matrix, we have 3 rows and 4 columns, and we can declare it by writing `int[][] mat = new int[3][4]`.

Here also zero-based indexing works,

|    **Col**     |   0   |   1   |   2   |   3   |
|:--------------:|:-----:|:-----:|:-----:|:-----:|
| **Row:** **0** | **-** | **-** | **-** |   -   |
|     **1**      | **-** | **-** | **-** | **-** |
|     **2**      | **-** | **-** | **-** | **-** |

## How a particular cell is represented in a matrix
Every cell is represented in the form mat[rowNo][colNo]


|    **Col**     |     0     |     1     |     2     |     3     |
|:--------------:|:---------:|:---------:|:---------:|:---------:|
| **Row:** **0** | mat[0][0] | mat[0][1] | mat[0][2] | mat[0][3] |
|     **1**      | mat[1][0] | mat[1][1] | mat[1][2] | mat[1][3] |
|     **2**      | mat[2][0] | mat[2][1] | mat[2][2] | mat[2][3] |



---
### Question

How to create a matrix with 5 columns and 7 rows?

**Choices**

- [ ] int[][] mat = new int[5][7];
- [x] int[][] mat = new int[7][5];
- [ ] int[] mat = new int[5][7];


---
### Question

If you have a matrix of size M * N, what is the index of the top left corner?

**Choices**

- [ ] [top][left]
- [ ] [0][N - 1]
- [x] [0][0]
- [ ] [M - 1][N - 1]

---
### Question

If you have a matrix of size M * N, what is the index of the bottom right corner?

**Choices**

- [ ] [bottom][right]
- [ ] [0][M - 1]
- [ ] [N - 1][M - 1]
- [x] [M - 1][N - 1]



---
## Print the top row of a matrix

Given a matrix of size N * M, print its top row.

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


### Solution
 Coordinates of the first row of the matrix are: (0,0), (0,1), (0,2), _ _ _ , (0, M - 1).
 
 Here column Number keeps on changing from 0 to M - 1 and row Number is always 0. 
 
### Pseudocode
```cpp
for(int col = 0; i < M; i++){
    print(mat[0][i]);
}
```


---
## Print the leftmost column of a matrix


### Problem Statement
Given a matrix of size N * M, print its leftmost column.

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


### Solution
 Coordinates of the leftmost column of the matrix are:
 (0,0), 
(1,0),
(2,0), 
_ ,
_ ,
_ ,
(N-1,0).
 
 Here row Number keeps on changing from 0 to N - 1 and the column Number is always 0. 
 
### Pseudocode
```cpp
for(int row = 0; row < N; row++){
    print(mat[row][0]);
}
```

---
## Print matrix row by row



### Problem Statement
Given a matrix of size N * M, print row by row

### Understanding the problem statement
We have to print every row of the matrix one by one, first print the elements of the first row then print the next line character, then print its second-row elements and then again the next line character, and so on till the last row, in this way we have to print all the rows one by one.

 
### Pseudocode
```cpp
for(int row = 0; row < N; row++){
    for(int col = 0; col < M; col++){
        print(mat[row][col]);
    }
    print("\n");
}
```

---
## Print matrix column by column

### Problem Statement
Given a matrix of size N * M, print column by column

### Example
**Input:**

|    **Col**     |  0  |  1  |  2  |
|:--------------:|:---:|:---:|:---:|
| **Row:** **0** |  1  |  3  | -2  |
|     **1**      |  9  |  0  |  8  |



**Output:**
1 9
3 0
-2 8 

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

 
## Pseudocode
```cpp
for(int col = 0; col < M; col++){
    for(int row = 0; row < N; row++){
        print(mat[row][col]);
    }
    print("\n");
}
```


---
## Matrix coding practice


### Java Code for printing matrix row by row and column by column

```java
import java.util.*;
public class Main {
    public static void printRowByRow(int mat[][]) {
        int n = mat.length; // rows
        int m = mat[0].length; // cols
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                System.out.print(mat[row][col] + " ");
            }
            System.out.println();
        }
        System.out.println("-----------------------------");
    }

    public static void printColByCol(int mat[][]) {
        int n = mat.length; // rows
        int m = mat[0].length; // cols
        for (int col = 0; col < m; col++) {
            for (int row = 0; row < n; row++) {
                System.out.print(mat[row][col] + " ");
            }
            System.out.println();
        }
        System.out.println("-----------------------------");
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int m = scn.nextInt();
        int[][] mat = new int[n][m];
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                mat[row][col] = scn.nextInt();
            }
        }
        printRowByRow(mat);
        printColByCol(mat);
    }
}
```


---
## Sum of matrix


### Problem statement
Given a matrix of size N * M as an argument, return its sum.

### Example:
**Input**
||||
|-|-|-|
|1|3|-2|
|9|0|8|

**Output:**
19

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

### PseudoCode
```java
public static int sum(int mat[][]) {
    int n = mat.length; // rows
    int m = mat[0].length; // cols
    int sum = 0;
    for (int row = 0; row < n; row++) {
       for (int col = 0; col < m; col++) {
           sum = sum + mat[row][col];
       }
    }
    return sum;
}
```



---
## Waveform printing

### Problem statement
Given a matrix of size N * M as an argument, print it in waveform.

### Example:
**Input**
|||||
|-|-|-|-|
|1|3|-2|7|
|9|0|8|-1|
|5|6|-2|3|
|3|4|0|2|

**Output:**
1 3 -2 7
-1 8 0 9
5 6 -2 3
2 0 4 3

### Understanding the problem statement
Waveform printing, you have to print the first row of the matrix as it is, then print the second row in reverse order, then print the third row as it is, then print the fourth row in reverse order and so on, in this way, you have to print all the rows of the matrix.

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


### Approach
If the row number of a matrix is even then we have to print as it is, if the row number is odd then we have to print in reverse order.

### PseudoCode
```java
public static void wavePrint(int mat[][]) {
    int n = mat.length; // rows
    int m = mat[0].length; // cols
    for (int row = 0; row < n; row++) {
        if(row%2==0){
            for (int col = 0; col < m; col++) {
                System.out.print(mat[row][col]+" ");
            }
        }
        else{
            for (int col = m - 1; col >= 0; col--) {
                System.out.print(mat[row][col]+" ");
            }
        }
        System.out.println();
    }
}
```

---
## Row wise sum


### Problem statement
Given a matrix of size N * M as an argument, return a row-wise sum.

### Example:

|||||
|-|-|-|-|
|1|3|-2|7|
|9|0|8|-1|
|5|6|-2|3|

**Output:**
[9, 16, 12]

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


### Understanding the problem statement
Return the sum of every row in the form of an array.


### PseudoCode
```java
public static int[] rowWiseSum(int mat[][]) {
    int n = mat.length; // rows
    int m = mat[0].length; // cols
    int[] ans = new int[n];
    for (int row = 0; row < n; row++) {
        int sum=0;
        for (int col = 0; col < m; col++) {
            sum = sum + mat[row][col];
        }
        ans[row] = sum;
    }
    return ans;
}
```


---
## Column-wise max


### Problem statement
Given a matrix of size N * M as an argument, return col-wise max.

### Example:

|||||
|-|-|-|-|
|1|3|-2|7|
|9|0|8|-1|
|5|6|-2|3|

**Output:**
[9, 6, 8, 7]

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


### Understanding the problem statement
Return a maximum of every column in the form of an array.


### PseudoCode
```java
public static int[] colWiseMax(int mat[][]) {
    int n = mat.length; // rows
    int m = mat[0].length; // cols
    int[] ans = new int[m];
    for (int col = 0; col < m; col++) {
        int max = mat[0][col];
        for (int row = 0; row < n; row++) {
            if(mat[row][col] > max){
                max = mat[row][col];
            }
        }
        ans[col] = max;
    }
    return ans;
}
```