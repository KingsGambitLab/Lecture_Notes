# Refresher : Patterns

## Question 1
Given **N** as input, print * **N** times.

#### TestCase

##### Input
```plaintext
5
```
##### Output
```plaintext
* * * * * 
```
#### PseudoCode
```java
function pattern(int N) {
    for (int i = 1; i <= N; i++) {
        system.out.print(' * ');
    }
}
```

---
## Question 2

Given **N** as input. Print a square of size **N * N** containing * in each cell.

#### TestCase

##### Input
```plaintext
5
```
##### Output
```plaintext
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```
#### PseudoCode
```java
function pattern(int N){
    for(int i = 1 ; i <= N ; i ++ ){
        for(int j = 1 ; j <= N ; j ++ ){
            system.out.print(' * ');
        }
        system.out.println();
    }
}
```

---
## Question 3

Given **N**,**M** as input, print a rectangle of size **N * M** containing * in each cell.

#### TestCase

##### Input
```plaintext
N = 3
M = 4
```
##### Output
```plaintext
* * * * 
* * * *
* * * *
```
#### PseudoCode
```java
function pattern(int N,int M){
    for(int i = 1 ; i <= N ; i ++ ){
        for(int j = 1 ; j <= M ; j ++ ){
            system.out.print(' * ');
        }
        system.out.println();
    }
}
```

---
## Question 4

Given **N** as input, print a staircase pattern of size **N**.

#### TestCase

##### Input
```plaintext
5
```
##### Output
```plaintext
*
* *
* * *
* * * *
* * * * *
```
#### Observation
The key observation here is that:
* The staircase pattern formed the right-angled triangle.
* The number of stars in each row is equal to the row number.
    

| Row | Stars |
|:---:|:-----:|
|  1  |   1   |
|  2  |   2   |
|  3  |   3   |
|  4  |   4   |


#### PseudoCode
```java
function pattern(int N){
    for(int i = 1 ; i <= N ; i ++ ){
        for(int j = 1 ; j <= i ; j ++ ){
            system.out.print(' * ');
        }
        system.out.println();
    }
}
```

---
## Question 5

Given **N** as input, print the pattern as shown below.

#### TestCase

##### Input 1
```plaintext
N = 3
```
##### Output 1
```plaintext
*
* 2
* 2 *
```
##### Input 2
```plaintext
N = 4
```
##### Output 2
```plaintext
*
* 2
* 2 *
* 2 * 4
```
#### Observation
The key observations are:
* For even column numbers, print * .
* For odd column numbers, print the column number.
#### PseudoCode
```java
function pattern(int N){
    for(int i = 1 ; i <= N ; i ++ ){
        for(int j = 1 ; j <= i ; j ++ ){
            if(j % 2 == 1) system.out.print(' * ');
            else system.out.print(j);
        }
        system.out.println();
    }
}
```

---
## Question 6

Given **N** as input, print the pattern as shown below.

#### TestCase

##### Input 1
```plaintext
N = 3
```
##### Output 1
```plaintext
* _ *
* _ *
* _ *
```
##### Input 2
```plaintext
N = 4
```
##### Output 2
```plaintext
* _ _ *
* _ _ *
* _ _ *
* _ _ *
```
#### Observation
The key observation here is that:
* The first and last column number of each row is * .
* There are total (N - 2) spaces in between stars( * ).
    

#### PseudoCode
```java
function pattern(int N){
    for(int i = 1 ; i <= N ; i ++ ){
        system.out.print(' * ');
        for(int j = 2 ; j <= N - 1 ; j ++ ){
            system.out.print('_');
        }
        system.out.print(' * ');
        system.out.println();
    }
}
```

---
## Question 7

Given **N** as input, print the pattern as shown below.

#### TestCase

##### Input 1
```plaintext
N = 3
```
##### Output 1
```plaintext
* * * 
* *
*
```
##### Input 2
```plaintext
N = 4
```
##### Output 2
```plaintext
* * * *
* * *
* *
*
```
#### Observation
As shown in above, the number of stars in each row is one less than the previous row except 1st row where number of stars is **N**. Hence, we can derive the formula:
* Number of stars in each row is equal to the (N - rowNumber + 1).

For N = 4,

  
| Row | Stars |
|:---:|:-----:|
|  1  |   4   |
|  2  |   3   |
|  3  |   2   |
|  4  |   1   |  

#### PseudoCode
```java
function pattern(int N){
    for(int i = 1 ; i <= N ; i ++ ){
        for(int j = i ; j <= N ; j ++ ){
            system.out.print(' * ');
        }
        system.out.println();
    }
}
```

---
## Question 8

Given **N** as input, print the pattern as shown below.

#### TestCase
##### Input 1
```plaintext
N = 3
```
##### Output 1
```plaintext
*   *
*  *
* *
```
##### Input 2
```plaintext
N = 4
```
##### Output 2
```plaintext
*     *
*   *
*  *
* *
```
#### Observation
The key observation here is that:
* The first and last character of each row is ' * '.
* Number of spaces in each row is one less than the previous row except first row where number of spaces between stars is **N - 1**. Hence we can say that there are total (N - rowNumber) spaces in between stars( * ).


For N = 4,

  
| Row | Total number of spaces between stars |
|:---:|:-----:|
|  1  |   3   |
|  2  |   2   |
|  3  |   1   |
|  4  |   0   |  
    

#### PseudoCode
```java
function pattern(int N) {
    for (int i = 1; i <= N; i++) {
        system.out.print(' * ');
        for (int j = 1; j <= N - i; j++) {
            system.out.print(' ');
        }
        system.out.print(' * ');
        system.out.println();
    }
}
```

---
## Question 9

Given **N** as input, print the pattern as shown below.

#### TestCase

##### Input 1
```plaintext
N = 3
```
##### Output 1
```plaintext
    *
  * *
* * *
```
##### Input 2
```plaintext
N = 4
```
##### Output 2
```plaintext
      *
    * *
  * * *
* * * *
```
#### Observation
The key observation here is that:
* Number of spaces in each row is one less than the previous row except 1st row where number of spaces are **N - 1**. Hence we can say that there are total (N - rowNumber) spaces in the starting of each row.
* Number of sars in each row is one more than the previous row except 1st row where number of stars are **1**. Hence we can say that there are total (rowNumber) stars at the last of each row.


For N = 4,

  
| Row | Total number of spaces | Total number of stars |
|:---:|:----------------------:|:---------------------:|
|  1  |           3            |           1           |
|  2  |           2            |           2           |
|  3  |           1            |           3           |
|  4  |           0            |           4           |
    


#### PseudoCode
```java
function pattern(int N) {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N - i; j++) {
            system.out.print(' ');
        }
        for (int j = 1; j <= i; j++) {
            system.out.print(' * ');
        }
        system.out.println();
    }
}
```
---
## Question 10
Given **N** as input, print the pattern as shown below.

#### TestCase
##### Input 1
```plaintext
N = 4
```
##### Output 1
```plaintext
********
***  ***
**    **
*      *
```
#### Observation
The key observation here is that:
* There are total (N - rowNumber + 1) stars in the begining and end of each row.
* There are total ((rowNumber - 1) * 2) spaces between these stars.
   
   For N = 4,

  
| Row | Stars | Spaces | Stars |
|:---:|:-----:|:------:|:-----:|
|  1  |   4   |   0    |   4   |
|  2  |   3   |   2    |   3   |
|  3  |   2   |   4    |   2   |
|  4  |   1   |   6    |   1   |

#### PseudoCode
```java
function pattern(int N) {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N - i + 1; j++) {
            system.out.print(' * ');
        }
        for (int j = 1; j <= (i - 1) * 2; j++) {
            system.out.print(' ');
        }
        for (int j = 1; j <= N - i + 1; j++) {
            system.out.print(' * ');
        }
        system.out.println();
    }
}
```

---
## Question 11

Given **N** as input, print the pattern as shown below.

#### TestCase
##### Input 1
```plaintext
N = 4
```
##### Output 1
```plaintext
   *
  ***
 *****
*******
```
#### Observation
The key observation here is that:
* Number of spaces in each row is one less than the previous row except 1st row where number of spaces are **N - 1**. Hence we can say that there are total (N - rowNumber) spaces in the starting of each row.
* Number of stars in each row is two more than the previous row except 1st row where number of stars are **1**. Hence we can say that there are total ((rowNumber - 1) * 2 + 1) stars between these spaces.
   
   For N = 4,

  
| Row | Spaces | Stars | Spaces |
|:---:|:-----:|:------:|:-----:|
|  1  |   3   |   1    |   3   |
|  2  |   2   |   3    |   2   |
|  3  |   1   |   5    |   1   |
|  4  |   0   |   7    |   0   |

#### PseudoCode
```java
function pattern(int N) {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N - i; j++) {
            system.out.print(' ');
        }
        for (int j = 1; j <= (i - 1) * 2 + 1; j++) {
            system.out.print(' * ');
        }
        for (int j = 1; j <= N - i + 1; j++) {
            system.out.print(' ');
        }
        system.out.println();
    }
}
```
