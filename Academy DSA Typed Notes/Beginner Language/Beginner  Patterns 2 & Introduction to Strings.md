# Beginner: Patterns 2 & Introduction to Strings

---

### Agenda

1. Print reverse triangle V
2. Print numeric triangle /\
3. Strings
4. next() vs nextLine()
5. How to deal with different type of inputs
6. Character Pattern

---

### Problem Statement
Print the following pattern:

For example, 

N = 5
```
* * * * *
 * * * *
  * * *
   * *  
    *
```

N = 4
```
* * * *
 * * *
  * *
   *
```

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

### Observation
Lets consider the spaces as "_"
```
* _ * _ * _ * _ * _
_ * _ * _ * _ * _
_ _ * _ * _ * _ 
_ _ _ * _ * _ 
_ _ _ _ * _ 
```

Now lets assume we are removing the spaces after every '*', then
```
* * * * *
_ * * * *
_ _ * * * 
_ _ _ * * 
_ _ _ _ * 
```
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/588/original/observation.jpg?1706503692" width=600/>

While printing stars, remember to print a space after every star, to get the our required reverse triangle pattern.

### Code

```java 
for (int i = 0; i < N; i++) {

   //loop to print i spaces
    for (int j = 1; j <= i; j++) {
        System.out.print(" ");
    }
    
    //loop to print n-i stars
    for (int j = 1; j <= n - i; j++) {
        System.out.print("* ");
    }
    
    System.out.println();
}
```


---

### Problem Statement
Print the following pattern:

For example, 

N = 5
```
0 0 0 0 1 0 0 0 0 
0 0 0 2 3 2 0 0 0 
0 0 3 4 5 4 3 0 0 
0 4 5 6 7 6 5 4 0 
5 6 7 8 9 8 7 6 5 
```
N = 4
```
0 0 0 1 0 0 0  
0 0 2 3 2 0 0  
0 3 4 5 4 3 0  
4 5 6 7 6 5 4  
```

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

### Approach

Lets divide the pattern into two halfs,

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/063/594/original/patter.png?1706505291" width=500/>

Lets consider the 2 halves separately,

### First Half

| **0** | **0** | **0** | **0** | **1** |
|-------|-------|-------|-------|-------|
| **0** | **0** | **0** | **2** | **3** |
| **0** | **0** | **3** | **4** | **5** |
| **0** | **4** | **5** | **6** | **7** |
| **5** | **6** | **7** | **8** | **9** |

Lets create a table, on observing the pattern.
| row | zeros   | start | end       |
|-----|---------|-------|-----------|
| 1   | 4 [5-1] | 1     | 1 [2\*1-1] |
| 2   | 3 [5-2] | 2     | 3 [2\*2-1] |
| 3   | 2 [5-3] | 3     | 5 [2\*3-1] |
| 4   | 1 [5-4] | 4     | 7 [2\*4-1] |
| 5   | 0 [5-5] | 5     | 9 [2\*5-1] |

We can come up with an generalized pattern on observing the values of the table based on the value i.

| ith row | (n - i) zeros | starts with i | ends with 2 * i - 1 |
|---|---|---|---|

### Psuedo code for First Half

```java
// Printing (n - i) zeros
for (int j = 1; j <= n - i; j++){
    System.out.print(0 + " ");
}

int lim = 2 *i - 1;
// Printing the increasing numbers from i to 2*i-1
for (int j = i; j <= lim; j++){
    System.out.print(j + " ");
}
```

### Second Half

| **0** | **0** | **0** | **0** |
|-------|-------|-------|-------|
| **2** | **0** | **0** | **0** |
| **4** | **3** | **0** | **0** |
| **6** | **5** | **4** | **0** |
| **8** | **7** | **6** | **5** |

Lets create a table, on observing the pattern.

| row | start     | end | zeros |
|-----|-----------|-----|-------|
| 1   |           |     | 4     |
| 2   | 2 [2\*2-2] | 2   | 3     |
| 3   | 4 [2\*3-2] | 3   | 2     |
| 4   | 6 [2\*4-2] | 4   | 1     |
| 5   | 8 [2\*5-2] | 5   | 0     |

We can come up with an generalized pattern on observing the values of the table based on the value i.

| ith row | starts with (i * 2 - 2) | ends with i | (n  i) zeros |
|---|---|---|---|

Here **starts with (i * 2 - 2)** can be even simplified, by using the end value of the previous calculation as **end - 1**.


### Psuedo code for Second Half

```java
// For the Second Half
// Printing the decreasing numbers
int lim = 2 *i - 1;
for (int j = lim - 1; j >= i; j--){
    System.out.print(j + " ");
}

//loop to print n - i zeros
for (int j = 1; j <= n - i; j++){
    System.out.print(0 + " ");
}
```




### Overall Code

``` java
for (int i = 1; i <= n; i++){
    
    // For the First Half
    //loop to print n - i zeros
    for (int j = 1; j <= n - i; j++){
        System.out.print(0 + " ");
    }
    
    int lim = 2 *i - 1;
    // Printing the increasing numbers from i to 2*i-1
    for (int j = i; j <= lim; j++){
        System.out.print(j + " ");
    }
    
    // For the Second Half
    // Printing the decreasing numbers
    for (int j = lim - 1; j >= i; j--){
        System.out.print(j + " ");
    }
    
    //loop to print n - i zeros
    for (int j = 1; j <= n - i; j++){
        System.out.print(0 + " ");
    }
    
    System.out.println();
}
```



---

### Reading Inputs for Strings

**1. sc.next()-> cannot take spaces as input**

Ques1:
```java
Input: "Hello World"
String s1 = sc.next();
System.out.println(s1);

String s2 = sc.next(); 
System.out.println(s2);
```
Output:
```plaintext
Hello
World
```

Explanation:

s1 will have first word, Hello
s2 will have next word, World




**2. sc.nextLine() -> can take spaces as well, until next line is encountered.** 

Ques1:
```java
Input: Hello World
String s3 = sc.nextLine();
System.out.println(s3);
```

Output:
```plaintext
Hello World
```

---

# Question 
Input : 

```
Hello World
```
```
Scanner scn = new Scanner(System.in);
String str1 = scn.next(); 
String str2 = scn.next(); 
System.out.println(str1);
System.out.println(str2);
```

# Choices

- [x] Hello <br> World
- [ ] Hello
- [ ] World
- [ ] None of the above

---

Output:
```plaintext
Hello
World
```


Explanation:

str1 will have, Hello
str2 will have next word, World


---

# Question

Input: 
```
Hello Welcome in Scaler
```

```
Scanner scn = new Scanner(System.in);
String str1 = scn.next(); 
String str2 = scn.nextLine(); 
System.out.println(str1);
System.out.println(str2);	
```

# Choices

- [ ] Hello
- [ ] Error
- [x] Hello <br> Welcome in Scaler
- [ ] None of the above

---

Output:
```plaintext
Hello
Welcome in Scaler
```

Explanation:

str1 will have first word, Hello
str2 will have complete line after hello, Welcome in scaler(including space before welcome). 

---

**Rule:** When the inputs are given in separate lines, and we take a String input using nextLine() after taking number input[nextInt(), nextLong(), nextFloat(), nextDouble()] or a single word [next()] then we get a empty String.
        
### Example

### Input
```
45
Hello World!
```
``` java 
Scanner sc = new Scanner(System.in);
int x = sc.nextInt(); // x[45]
String st = sc.nextLine(); // st -> Empty String
String st2 = sc.nextLine(); // st2 -> "Hello World!"
System.out.println(st); 
System.out.println(s2); 
```
  
### Output
```

Hello World!
```
---


# Question

Predict the output :
```
Input- 
11
Super Excited!
```
```
Scanner scn = new Scanner(System.in);
int x = scn.nextInt();
String str = scn.nextLine();
System.out.println(x);
System.out.println(str);	
```

# Choices

- [ ] 11 Super Excited!
- [ ] Error
- [ ] 11 <br> Super Excited!
- [x] 11
       
---



# Question

Predict the output :
```
Input- 
11
Super Excited!
```
```
Scanner scn = new Scanner(System.in);
int x = scn.nextInt();
String str = scn.nextLine();
System.out.println(x);
System.out.println(str);
System.out.println("The End");	
```

# Choices

- [ ] 11 Super Excited! The End
- [x] 11 <br> <br> The End
- [ ] Error
- [ ] 11 <br> Super Excited! <br> The End

       
---


### Character:
A character represent a single symbol. 

There are different types of characters:
* Uppercase characters : ['A' - 'Z']
* Lowercase characters : ['a' - 'z']
* Numeric characters: ['0' - '9']
* Special characters: ['@', '#', '\$', '%', '&'...]

There are a total of 128 characters. 


### Syntax

**Example 1:**
```java
char ch = 'a';
System.out.println(ch);
```
**Output:**  
```plaintext
a
```

**Example 2:**
```java
char ch = 'ab';
System.out.println(ch);
```
**Output:**  
```plaintext
Error: Only a single symbol is a character.
```

---


### Problem Statement
Write a program to print all characters from A to Z.



### Code
```java
public static void printCharacters(String str) {
    for(char i = 'A'; i <= 'Z'; i++) {
        System.out.println(i);
    } 
}
```
---


### Character Stairacase Pattern

N = 5
```
A 
A B 
A B C 
A B C D 
A B C D E 
```

N = 3
```
A 
A B 
A B C 
```

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

### Approach 
Consider the spaces as underscores (for better visualization).

Lets take N = 5,
```
A _ 
A _ B _ 
A _ B _ C _ 
A _ B _ C _ D _ 
A _ B _ C _ D _ E _ 
```

Lets assume we are printing the standard stair case pattern, 

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

Now both the patterns is similar. So, instead of printing numbers, we just create a new variable, which starts with **A**, then increment inside the innerloop.


### Code

``` java 
for (int i = 1; i <= N; ++i) {
    char ch = 'A';
    for (char j = 1; j <= i; j++) {
        System.out.print(ch + " ");
        ch++;
    }
    System.out.println();
}
```
---
