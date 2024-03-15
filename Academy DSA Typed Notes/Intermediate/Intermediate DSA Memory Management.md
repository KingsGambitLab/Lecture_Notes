# Beginner : Memory Management

---
## Introduction to stack

### Idli Maker Examples

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/250/original/Screenshot_2023-09-26_at_5.39.11_PM.png?1695922237" alt= “” width ="700" height="300">


### Stack


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/251/original/Screenshot_2023-09-26_at_5.37.44_PM.png?1695922271" alt= “” width ="600" height="300">

:::success
There are a lot of quizzes in this session, please take some time to think about the solution on your own before reading further.....
:::

---
### Introduction to call stack

#### Example 1
Consider the below code:
```java
int add(int x, int y) {
    return x + y;
}

int product(int x, int y) {
    return x * y;
}

int subtract(int x, int y) {
    return x - y;
}

public static void main() {
    int x = 10;
    int y = 20;
    int temp1 = add(x, y);
    int temp2 = product(x, y);
    int temp3 = subtract(x, y);
    System.out.println(temp1 + temp2 + temp3);
}
```

Following is the call stack execution for above code:


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/252/original/Screenshot_2023-09-26_at_5.41.09_PM.png?1695922314" alt= “” width ="200" height="400">


**Ouput:** 220

#### Example 2
Consider the below code:
```java
int add(int x, int y) {
    return x + y;
}

public static void main() {
    int x = 10;
    int y = 20;
    int temp1 = add(x, y);
    int temp2 = add(temp1, 30);
    int temp3 = add(temp2, 40);
    System.out.println(temp3);
}
```
Following is the call stack execution for above code:


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/067/735/original/explanation.png?1710154203" alt= “” width ="200" height="400">


**Output:** 100

#### Example 3
Consider the below code:
```java
int add(int x, int y) {
    return x + y;
}

static int fun(int a, int b) {
    int sum = add(a, b);
    int ans = sum * 10;
    return ans;
}
static void extra(int w){
    System.out.println("Hello");
    System.out.println(w);
}
public static void main() {
    int x = 10;
    int y = 20;
    int z = fun(x, y);
    System.out.println(z);
    extra(z);
}
```

Following is the call stack execution for above code:
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/050/828/original/Screenshot_2023-09-26_at_5.36.25_PM.png?1695730007" alt= “” width ="150" height="450">



**Output:**
```plaintext
300 
Hello 
310
```

---

### Types of Memory in Java
Following are the types of memory present in Java -
1. **Stack** -<br> All the primitive data type and reference will be stored in stack.
2. **Heap** -<br> Container of that reference is stored in heap. Arrays, ArrayList, Objects are created inside heap. 

**Example 1**
Consider the below code:
```java
public static void main() {
    int x = 10;
    int[] ar = new int[3];
    System.out.println(ar); // #ad1
    System.out.println(ar[2]); // 0
    ar[1] = 7;
}
```
Now, lets analyze the given code - 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/253/original/upload_db1be0d6807a0107d3b4a49f92083d10.png?1695922800" alt= “” width ="400" height="400">



**Note**: 
1. **Primitive data types:** [int, float, double, char, boolean, long] memory will be assigned in stack.
2. **Reference/ address of the container:** will be stored in stack.
3. **Container:** [Array/ Arraylist] will be stored in heap.

**Example 2**
Consider the below code:
```java
public static void main() {
    int x = 10;
    int[] ar = new int[3];
    int[] ar2 = ar;
    System.out.println(ar); // 4k
    System.out.println(ar2); // 4k
}
```
Now, lets analyze the given code - 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/253/original/upload_db1be0d6807a0107d3b4a49f92083d10.png?1695922800" alt= “” width ="300" height="300">




**Example 3**
Consider the below code:
```java
public static void main() {
    int[] ar = new int[3];
    System.out.println(ar); // 5k
    ar[1] = 9;
    ar[2] = 5;
    
    ar = new int[5];
    System.out.println(ar); // 7k
}
```
Now, lets analyze the given code - 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/254/original/upload_838ad761524ff3f484346b1762d842ab.png?1695923038" alt= “” width ="300" height="300">


**Example 4**
Consider the below code:
```java
static void fun(int[] a){
    System.out.println(a); // 9k
    a[1] = 5;
}
public static void main() {
    int[] ar = new int[3];
    System.out.println(ar); // 9k
    ar[0] = 90;
    ar[1] = 50;
    fun(ar);
    System.out.println(ar[1]); // 5
}
```
Now, lets analyze the given code - 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/255/original/upload_96b9617bf2562ab2cf70308c14562662.png?1695923094" alt= “” width ="300" height="300">


**Example 5**
Consider the below code:
```java
public static void main() {
    float y = 7.84f;
    int[][] mat = new int[3][4];
    System.out.println(mat); // 9k
    System.out.println(mat[1]); // 3k
    System.out.println(mat[1][3]); // 0
}
```
Now, lets analyze the given code - 


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/256/original/upload_d6ef6f285e8852ea6483735ea9b275ff.png?1695923118" alt= “” width ="300" height="300">



**Example 6**
Consider the below code:
```java
static void sum(int[][] mat){
    System.out.println(mat); // 2k
    System.out.println(mat[0][0] + mat[1][0]); // 40
}
public static void main() {
    int[][] mat = new int[2][3];
    mat[0][0] = 15;
    mat[1][0] = 25;
    sum(mat);
}
```
Now, lets analyze the given code - 


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/258/original/upload_60fffb5badb5839f531e4a4b49d50280.png?1695923213" alt= “” width ="300" height="300">




**Example 7**

Consider the below code:
```java
static int sumOfRow(int[] arr){
    System.out.println(arr); // 7k
    int sum = 0;
    for (int i = 0; i < arr.length; i++){
        sum = sum + arr[i];
    }
    return sum;
}

public static void main() {
    int[][] mat = new int[2][3];
    mat[0][0] = 9;
    mat[0][1] = 5;
    mat[0][2] = 1;
    int ans = sumOfRow(mat[0]); // 7k
    System.out.println(ans); // 15
}
```
Now, lets analyze the given code - 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/259/original/upload_ebc077e9eb41f97f24666a4fc1c97c6c.png?1695923287" alt= “” width ="300" height="400">

### Question
Predict the Output :
```Java
static void change(int a) {
    a = 50;
}

public static void main(String args[]) {
    int a = 10;
    change(a);
    System.out.println(a);
}
```


**Choices**
- [x] 10
- [ ] 50
- [ ] Error



**Explanation**


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/260/original/upload_88f3bbcc4fd367434b74cf4b394cebe8.png?1695923386" alt= “” width ="200" height="300">



* The parameter variable 'a' of change function is reassigned to the value of 50, because both the functions have their own variables, so the variable "a" of main function is different than of variable "a" in change function.
* Stack changes are temporary.

---
### Question
Predict the output :
```java
static void change(int[]a) {
    a[0] = 50;
}

public static void main(String args[]) {
    int[]a = {10};
    change(a);
    System.out.println(a[0]);
}
```

**Choices**
- [ ] 10
- [x] 50
- [ ] Error

---

**Explanation:**

* The array a in change method and main method both refer to the same array object in the heap.
* Heap changes are permanent changes. 


<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/261/original/upload_b6a922583fd12618a2bb53d4233d6569.png?1695923456" alt= “” width ="200" height="300">



---
### Question
Predict the output : 
```java
static void test(int[]a) {
    a = new int[1];
    a[0] = 50;
}

public static void main(String args[]) {
    int[]a = {10};
    test(a);
    System.out.println(a[0]);
}
```


**Choices**
- [x] 10
- [ ] 50
- [ ] Error

---
**Explanation:**
Inside the test method, a new integer array with length 1 is allocated on the heap memory, and the reference to this array is assigned to the parameter variable a. Hence, now the variable 'a' inside test function and main function point to different references.Heap changes are permanent. 

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/262/original/upload_2880b16a60cdc943bbd8deb67bc51f87.png?1695923573" alt= “” width ="200" height="300">




---
### Question

Predict the output:
```java
static void fun(int[] a) {
    a = new int[1];
    a[0] = 100;
}
public static void main() {
    int[] a = {10, 20, 30};
    fun(a);
    System.out.println(a[0]);
}

```

**Choices**
- [x] 10
- [ ] 100
- [ ] Error
- [ ] inky pinky po

**Explanation:**

Inside the fun method, a new integer array with length 1 is allocated on the heap memory, and the reference to this array is assigned to the parameter variable a. Hence, now the variable 'a' inside test function and main function point to different references.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/263/original/upload_fe68bae5077ef0992c9d7cec41e6c8cb.png?1695923634" alt= “” width ="300" height="300">




---

### Question
Predict the output : 
```java
static void swap(int a,int b) {
    int temp = a;
    a = b;
    b = temp;
}

public static void main(String args[]) {
    int a = 10;
    int b = 20;
    swap(a,b);
    System.out.println(a + " " + b);
}
```


**Choices**
- [x] 10 20
- [ ] 20 10
- [ ] 10 10
- [ ] Error

**Explanation:**

* Swap function is called by value not by reference. 
* So, the changes made in the swap function are temporary in the memory stack.
* Once we got out of the swap function, the changes will go because they are made in temporary variables.
* Hence no swapping is done and variable have the same value as previous.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/264/original/upload_95a36c6cecdaa3e8eb1fa455c50dd9b0.png?1695923691" alt= “” width ="200" height="300">




---
### Question
Predict the output : 
```java
static void swap(int[]a,int[]b) {
    int temp = a[0];
    a[0] = b[0];
    b[0] = temp;
}

public static void main(String args[]) {
    int[]a = {10};
    int[]b = {20};
    swap(a,b);
    System.out.println(a[0] + " " + b[0]);
}
```
**Choices**
- [ ] 10 20
- [x] 20 10
- [ ] 10 10
- [ ] Error

**Explanation:**
Inside swap function, the array variables 'a' & 'b' are passed by reference, so they are pointing to same references in the heap memory as of 'a' & 'b' variables inside main function.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/265/original/upload_30b26edaf41f106c5f23c653f55b87bd.png?1695923815" alt= “” width ="300" height="300">



---
### Question
Predict the output : 
```java
static int[] fun(int[]a) {
    a = new int[2];
    a[0] = 50; a[1] = 60;
    return a;
}
    
public static void main(String args[]) {
    int[]a = {10,20,30};
    a = fun(a);
    System.out.println(a[0]);
}
```

**Choices**
- [ ] 10
- [x] 50
- [ ] Error



**Explanation:**
* When fun method is called on array a, then a new integer array is allocated on the heap memory.
* But since, we are returning the new array in the main method, so now the changes done in fun method persists.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/266/original/upload_ee2fe92543bb6f84908886e2144ef3d2.png?1695923985" alt= “” width ="300" height="300">



---
### Question
Predict the output : 
```java
static void test(int[]a) {
    a = new int[2];
    a[0] = 94;
}
    
public static void main(String args[]) {
    int[]a = {10,20,30};
    test(a);
    System.out.println(a[0]);
}
```


**Choices**
- [x] 10
- [ ] 94
- [ ] Error

**Explanation:** 

Inside the test function, a new integer array with length 2 is allocated on the heap memory, and the reference to this array is assigned to the parameter variable a. Hence, now the variable 'a' inside test function and main function point to different references.

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/267/original/upload_4bebf48ccf793236b9b7077d14c2b3c5.png?1695924086" alt= “” width ="300" height="300">

