# Refresher: Arraylists

# Arrays
Arrays have some disadvantages:
- Fixed-size(we cannot increase or decrease size of array)
- Size should be known in advance.

Due to these arrays are not suitable for some situations.


---
## ArrayList
ArrayList have all the advantages of arrays with some additional features
- Dynamic size
- Does not require to know the size in advance.


## Examples
Here are some real-world examples where using an ArrayList is preferred in comparison to using arrays.

- Shopping list
- New tabs of the browser
- Youtube playlist


## Syntax
```java
ArrayList<Type> arr = new ArrayList<Type>();
```
- Here Type has to be a class, it can not be a primitive.
- Primitives can be int, long, double, or boolean.
- Instead of primitives we can use wrapper classes and custom objects, which means we can use Integer, Long, Double, String, etc.

---
## Basic Operations

### Inserting element
We can add an element in the arraylist using `add()` and it adds an element at the end of the list.

### Get
It will fetch elements from the ArrayList using an index.

### Size
`size()` will give us the size of the ArrayList.

### Remove
It removes the element from the ArrayList present at a particular index.

### Set
It updates the value of a particular index to the new value.

```java
import java.util.*;
import java.lang.*;
class Main{
    public static void main(String args[]){
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        //printing ArrayList
        System.out.println(arr);
        
        // add
        arr.add(2);
        arr.add(-1);
        arr.add(5);
        
        
        System.out.println(arr);
        
        //get
        System.out.println("2nd element is: "+arr.get(2));
        // System.out.println(arr.get(-1)); it gives an error as the -1 index does not exist for arr
        // System.out.println(arr.get(3)); it gives an error as 3 index does not exist for arr
        
        
        // Size
        System.out.println("Size is: " + arr.size());
        
        // Remove
        arr.remove(1);
        System.out.println(arr);
        
        
        // Set
        arr.set(1, 8);
        System.out.println(arr);
    }
}
```

**Output**

```plaintext
[]
[2, -1, 5]
2nd element is: 5
Size is: 3
[2, 5]
[2, 8]
```

---
# Taking Arraylist as an input

```java
import java.util.*;
import java.lang.*;
class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        
        // Taking ArrayList as input
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        int n = sc.nextInt();
        for(int i = 0 ; i < n ; i++){
            int tmp = sc.nextInt();
            arr.add(tmp);
        }
        System.out.println(arr);
    }
}
```


---
## Problem Statement
Given an ArrayList as input, return an ArrayList of the multiples of 5 or 7.

## Example
**Input:** [1, 5, 3, 0, 7]
**Output:** [5, 0, 7]

## Solution
Iterate over the input ArrayList, and check if the element is divisible by 5 or 7 then simply add it to the result ArrayList.

## PsuedoCode

```java
import java.util.*;
import java.lang.*;
class Main{
    public static ArrayList<Integer> multiples(ArrayList<Integer> arr){
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for(int i = 0; i < arr.size(); i++){
            int val = arr.get(i);
            if(val % 5 == 0 || val % 7 == 0)
                ans.add(val);
        }
        return ans;
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        
        // Taking ArrayList as input
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        int n = sc.nextInt();
        for(int i = 0 ; i < n ; i++){
            int tmp = sc.nextInt();
            arr.add(tmp);
        }
        System.out.println(multiples(arr));
    }
}
```



---
## Problem Statement
Given two integers A and B as input, return an ArrayList containing first B multiples of A.

## Example
**Input:** A = 2, B = 4
**Output:** [2, 4, 6, 8]

**Explanation:** First four multiple of 2 are A * 1 = 2 * 1 = 2, A * 2 = 2 * 2 = 4, A * 3 = 2 * 3 = 6, A * 4 = 2 * 4 = 8



## PsuedoCode

```java
import java.util.*;
import java.lang.*;
class Main{
    public static ArrayList<Integer> firstB(int A, int B){
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for(int i = 1; i <= B; i++){
            ans.add(A * i);
        }
        return ans;
    }
    public static void main(String args[]){
        
        System.out.println(firstB(3, 5));
    }
}
```

**Output:**
```plaintext
[3, 6, 9, 12, 15]
```


---
# 2D Arrays

We can imagine 2D arrays as array of arrays.

## 2D ArrayList
2D ArrayList are ArrayList of ArrayLists


## Syntax
```java
ArrayList< ArrayList<Type> > mat = new ArrayList< ArrayList<Type> >();
```

## Basic Operations
- **Add:** We can add ArrayList inside 2D ArrayList. We can ArrayLists of different sizes in a single 2D ArrayList.
- Get
- Size
- Remove
- Set

```java
import java.util.*;
import java.lang.*;
class Main{
    public static void main(String args[]){
        ArrayList< ArrayList<Integer> > list2d = new ArrayList< ArrayList<Integer> >();
        
        // Add
        ArrayList<Integer> a1 = new ArrayList<Integer>();
        a1.add(1);
        a1.add(4);
        list2d.add(a1);
        
        
        ArrayList<Integer> a2 = new ArrayList<Integer>();
        a2.add(0);
        list2d.add(a2);
        
        ArrayList<Integer> a3 = new ArrayList<Integer>();
        a3.add(10);
        a3.add(-5);
        a3.add(1);
        list2d.add(a3);
        
        System.out.println(list2d);
        
        
        // Get
        System.out.println(list2d.get(0));
        System.out.println(list2d.get(2).get(1));
        
        
        // Size
        System.out.println(list2d.size());
        System.out.println(list2d.get(1).size());
        
        
        // Remove
        list2d.remove(1);
        System.out.println(list2d);
        
        
        // Set
        ArrayList<Integer> a4 = new ArrayList<Integer>();
        a4.add(-2);
        a4.add(5);
        a4.add(8);
        list2d.set(0,a4);
        System.out.println(list2d);
        
        
        // Update a list element
        list2d.get(1).set(1, -15);
        System.out.println(list2d);
    }
}
        
```

**Output:**
```plaintext
[[1, 4], [0], [10, -5, 1]]
[1, 4]
-5
3
1
[[1, 4], [10, -5, 1]]
[[-2, 5, 8], [10, -5, 1]]
[[-2, 5, 8], [10, -15, 1]]
```



---
## Problem Statement
Given a 2D Arraylist as input, print it line by line.

## Explanation
Every nested list of 2D ArrayList is to be printed in different lines and the elements in a single line are separated by space.

## Example
**Input:** [[1, 4], [0], [10, -5, 1]]
**Output:** 
1 4
0
10 -5 1


## Code
```java
import java.util.*;
import java.lang.*;
class Main{
    public static void print2DList(ArrayList< ArrayList<Integer> > list2d){
        for(int i = 0 ; i < list2d.size() ; i++){
            // get the ith ArrayList
            ArrayList<Integer> ls = list2d.get(i);
            
            //Print the ith list
            for(int j = 0 ; j < ls.size() ; j++){
                System.out.print(ls.get(j) + " ");
            }
            System.out.println();
        }
    }
    public static void main(String args[]){
        ArrayList< ArrayList<Integer> > list2d = new ArrayList< ArrayList<Integer> >();
        
        ArrayList<Integer> a1 = new ArrayList<Integer>();
        a1.add(1);
        a1.add(4);
        list2d.add(a1);
        
        
        ArrayList<Integer> a2 = new ArrayList<Integer>();
        a2.add(0);
        list2d.add(a2);
        
        ArrayList<Integer> a3 = new ArrayList<Integer>();
        a3.add(10);
        a3.add(-5);
        a3.add(1);
        list2d.add(a3);
        
        
        print2DList(list2d);
    }
}
```

**Output:**
```plaintext
1 4 
0 
10 -5 1 
```



---
## Problem Statement
Given an integer N as input, return the numeric staircase.


## Example
**Input:** 3

**Output:** 
```plaintext
[
    [1].
    [1, 2],
    [1, 2, 3]
]
```


## Code

```java
import java.util.*;
import java.lang.*;
class Main{
    public static ArrayList< ArrayList<Integer> > staircase(int N){
        ArrayList< ArrayList<Integer> > ans = new ArrayList< ArrayList<Integer> >();
        
        for(int row = 1 ; row <= N ; row++){
            ArrayList<Integer> rw = new ArrayList<Integer>();
            for(int col = 1 ; col <= row ; col++){
                rw.add(col);
            }
            ans.add(rw);
        }
        return ans;
    }
    public static void main(String args[]){
        System.out.println(staircase(3));
    }
}
```

**Output:**
```plaintext
[[1], [1, 2], [1, 2, 3]]
```



---
# Some pointers

- Use Java 8 Oracle JDK - Language 
- Gets easier with use