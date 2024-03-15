# Refresher : 1D Arrays
# Introduction To Arrays

---
## Definition

Array is the sequential collection of same types of data. The datatype can be of any type i.e, int, float, char, etc. Below is the declaration of the array:
```java
int arr[] = new int[5];
```
It can also be declared as:
```java
int[] arr = new int[5]
```
Here, ‘int’ is the datatype, ‘arr’ is the name of the array and ‘n’ is the size of an array. 
We can access all the elements of the array as arr[0], arr[1] ….. arr[n-1]. 

**Note:** Array indexing starts with 0.


---
### Question
Maximum index of array of size N is ?

Choose the correct answer

**Choices**

- [ ] 1
- [ ] 0
- [x] N-1
- [ ] N


---
### Question
Given an array as arr = {3,4,1,5,1}. What is ths sum of all elements in the array?

Choose the correct answer

**Choices**

- [ ] 12
- [ ] 13
- [x] 14
- [ ] 15


---
## Question 1

Take an integer array **arr** of size **N** as input and print its sum.

#### TestCase
##### Input
```java
N = 5
arr = {1,2,3,4,5}
```
##### Output
```plaintext
15
```

#### Explanation
To calculate the sum of all the elements in the array, we need a variable say **sum** which is initially zero. Then iterate all the elements and adding them to **sum**.

#### PseudoCode
```java
int sum = 0;
for (int i = 0; i < n; i++) {
    sum = sum + arr[i];
}
System.out.println("Sum is " + sum);
```
\
---
### Question
Given an array as arr = {3,4,1,5,1}. Find the maximum element.

Choose the correct answer

**Choices**

- [ ] 3
- [ ] 4
- [x] 5
- [ ] 1


---
## Question 2

Take an integer array **arr** of size **N** as input and print its maximum element.

#### TestCase
##### Input
```plaintext
N = 5
arr = {1,2,3,4,5}
```
##### Output
```plaintext
5
```

#### PseudoCode
```java
int maximum_element = 0;
for (int i = 0; i < n; i++) {
    if (maximum_element < arr[i]) maximum_element = arr[i];
}
system.out.println("Sum is " + maximum_element);
```

---
### Question

What will be the output of the above code with
N = 5
arr = {-3, -7, -2, -10, -1}
array as input ?

Choose the correct answer

**Choices**

- [ ] -7
- [ ] -1
- [x] 0
- [ ] 2

**Explanation**

Initially we have assumed 0 as the max element in the array and in the given case, all the element is smaller than 0. So, the max element is 0.

---
### Question 2 PseudoCode 

**Note:** We can fix it by initially assigning arr[0] to the maximum_element.
So the updated pseudocode is:

```java
int maximum_element = arr[0];
for (int i = 0; i < n; i++) {
    if (maximum_element < arr[i]) maximum_element = arr[i];
}
system.out.println("Sum is " + maximum_element);
```

---
## Question 3

Take an integer array **arr** of size **N** as input and return its minimum element.

#### TestCase
##### Input
```java
N = 5
arr = {1,2,3,4,5}
```
##### Output
```plaintext
1
```

#### PseudoCode
```java
public static int findMin(int arr[], int n) {
    int minimum_element = arr[0];
    for (int i = 0; i < n; i++) {
        if (minimum_element > arr[i]) minimum_element = arr[i];
    }
    return minimum_element;
}
```

---
## Question 4
Take an integer array **arr** of size **N** as input and check whether an integer **k** is present in that or not.

#### TestCase
##### Input
```java
N = 5
arr = {1,2,3,4,5}
k = 4
```
##### Output
```plaintext
true
```

#### Explanation
To check whether an integer **k** is present in the array or not, we need to check each element and compare it with **k**. If none of the element is equal to **k**,then return false.

#### PseudoCode
```java
public static boolean findK(int arr[], int n, int k) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == k) return true;
    }
    return false;
}
```

---
### Question
Given an array as arr = {3,4,1,5,1}. What is the frequency of 1?

Frequency of any element is defined as the number of occurences of that element in the array.

Choose the correct answer

**Choices**

- [ ] 0
- [ ] 1
- [x] 2
- [ ] 3

---
## Question 5

Take an integer array **arr** of size **N** as input. Return the frequency of **K** in the array.

#### TestCase

##### Input
```java
N = 6
arr = {1,2,3,4,5,1}
k = 1
```
##### Output
```plaintext
2
```


**Note:** Here frequency is the number of times the element **k** occurs in the array.

#### PseudoCode
```java
public static int frequencyK(int arr[], int n, int k) {
    int frequency = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == k) frequency++;
    }
    return frequency;
}
```


---
## Question 6

Given an integer array as an input, return the frequency count of the array.

#### TestCase
##### Input
```java
arr = {1,1,2,1,3,1,3}
```
##### Output
```plaintext
{4,4,1,4,2,4,2}
```

#### PseudoCode
```java
int[] frecount(int arr[]) {
    int n = arr.length;
    int[] ans = new int[n];
    for (int i = 0; i < n; i++) {
        ans[i] = frequencyK(arr, n, arr[i]);
    }
    return ans;
}
```


---
## Question 7

Given an integer array as an input, check whether it is strictly increasing.


#### TestCase
##### Input
```plaintext
N = 5
arr = {1,2,3,4,5}
```
##### Output
```plaintext
true
```
##### Explanation
All the element in the array is in sorted order. So, we can say that it is in strictly increasing order.
As
```plaintext
1 < 2 < 3 < 4 < 5
```

#### PseudoCode
```java
public static boolean strictlyincreasing(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] >= arr[i + 1]) return false;
    }
    return true;
}
```