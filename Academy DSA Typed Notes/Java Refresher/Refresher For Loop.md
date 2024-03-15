# Refresher : For Loop

---
### Question

```java
// 1.
while(// 2.) {
// 3.
// 4.
}
```

Which sequence correctly represents the order of operations in the while loop?

**Choices**

- [ ] Initialisaton , Loop work, Condition , Update
- [ ] Initialisation , update, Loop work , Condition
- [x] Initialisation , Condition, Loop work, Update
- [ ] Loop work, Initialisation, Condition, Update

**Explanation:** 

* **Initialization:** In this step, the loop control variable is initialized to a starting value. It is usually the first step before the loop begins.
* **Condition:** The loop condition is evaluated before each iteration. If the condition is true, the loop body will be executed; otherwise, the loop will terminate.
* **Loop work:** This represents the actual code or operations that are executed inside the loop body during each iteration.
* **Update:** After each iteration, the loop control variable is updated or modified. It prepares the loop for the next iteration by changing its value.

So, the correct flow of the loop is Initialization -> Condition -> Loop work -> Update.

---
## For Loops

The for loop in most programming languages follows the syntax given below:

```java
for(initialization; condition; update) { 
    loop work; 
}
```

The meaning of each step is same as while loop.
For Loop and while can be used interchaneably. They are like Water and Jal.

### Example-1:

Given N as input, Print from 1 to N.

Provided we have input N, this is how the `for` loop looks like:

### Code:

```java 
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number (N): ");
        int N = scanner.nextInt();

        for (int i = 1 ; i <= N; i ++ ) {
            System.out.print(i + " ");
        }

        scanner.close();
    }
}
```

### Explanation

* **Initialization:** `int i = 1`; - Firstly, we initialize i = 1. This sets the starting point for the loop.
* **Condition:** `i <= N`; - Loop continues to execute till `i <= N`. In each iteration, it checks if i <= N. If it is true, the loop work is done; otherwise, the loop terminates.
* **Loop Body (Action):** `System.out.print(i + " ");` - During each iteration, the loop body prints the value of i, followed by a space.
* **Update:** `i ++` - After each iteration, i is incremented by 1. This prepares loop for next iteration.



### Example-2:

Given N as input, print all odd numbers from 1 to N.

### Approach:
* First, we take input from user.
* Then we run the loop from 1 to N.
* Since we want to print only odd numbers, we increment by 2 to skip even numbers.
* The loop body prints the value of `i`


### Code:
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number (N): ");
        int N = scanner.nextInt();

        for (int i = 1; i <= N; i += 2) {
            System.out.print(i + " ");
        }

        scanner.close();
    }
}
```

---
## What are Factors of a Number

**i** is said to be the factor of N if i divides N completely, i.e **N % i = 0**

Let's take an Integer as an example and find its factors:

**Example 1:** Find the factors of 6.
Since 1, 2, 3, 6 divides 6 completely, hence factors of 6 are 1, 2, 3, and 6.

**Example 2:** Find the factors of 10.
Since 1, 2, 5, 10 divides 10 completely hence, the factors of 10 are 1, 2, 5, and 10.


---
### Question
 
What are the factors of 24 ?

**Choices**

- [ ] 2, 3, 4, 6, 8, 12
- [ ] 1, 2, 3, 4, 6, 8, 12
- [x] 1, 2, 3, 4, 6, 8, 12, 24

**Explanation**

Factors of 24 are 1, 2, 3, 4, 6, 8, 12, and 24.

---
## Print the factors of a positive number N

How to print the factors of a positive number N ?

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


### Approach:

* The range of factors of a positive integer N is from 1 to N. 
* We can simply iterate from 1 to N to get all the factors
* If N % i == 0, increment count variable.

### Code:

```java 
import java.util.Scanner;

public class Main {
    public static void printFactors(int N) {
        System.out.print("Factors of " + N + ": ");
        for (int i = 1; i <= N; ++ i) {
            if (N % i == 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number (N): ");
        int N = scanner.nextInt();

        printFactors(N);

        scanner.close();
    }
}
```

---
### Question

Definition of Prime :
If a number **"N"** is divisible by **1** and itself is called **Prime Number**.

**Choices**

- [ ] True
- [x] False

**Explanation:**

As per above definition, 1 will also be a Prime Number since its factors are 1 and itself.
But we know 1 is not a Prime Number, hence the definition is wrong.

**Correct Definition:** A prime number has exactly two factors.

**For example:**
2 is a prime number because it has only two factors, 1 and 2.
3 is a prime number because it has only two factors, 1 and 3.
5 is a prime number because it has only two factors, 1 and 5.

---
## Prime Numbers

### How to check if a number is prime or not?

* We just need to check if N has exactly 2 factors, then it is Prime. 
* So, we can make use of previous code to get the factors of N and check if factors are 2 or not.

### Code: 

```java 
import java.util.Scanner;

public class Main {
    public static boolean isPrime(int number) {
        int divisorCount = 0;

        for (int i = 1; i <= number; ++ i) {
            if (number % i == 0) {
                divisorCount ++ ;
            }
        }

        return (divisorCount == 2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int divisorCount = 0;
        System.out.print("Enter a number: ");
        int N = scanner.nextInt();

        for (int i = 1; i <= N; ++ i) {
            if (N % i == 0) {
                divisorCount ++ ;
            }
        }

        if (isPrime(N)) {
            System.out.println("Prime");
        } else {
            System.out.println("Not Prime");
        }

        scanner.close();
    }
}
```

---
### Question

What is the smallest prime number?

**Choices**

- [ ] 0
- [ ] 1
- [x] 2
- [ ] 3

**Explanation:**

The smallest prime number is 2. Also, it is the only even prime number.

---
## Break and Continue statements

### Explanation of Break statement

The `break` statement is used to exit or terminate the nearest enclosing loop prematurely. When the `break` statement is encountered inside a loop, it immediately stops the loop's execution and transfers control to the statement following the loop. It helps avoid unnecessary iterations and is often used to terminate a loop early based on a specific condition.


The code for finding if a number is prime or not can be modified using `break` statement to avoid more efforts

In the given code, the goal is to check if the number N is prime or not. We can use the `break` statement to optimize the loop and avoid unnecessary iterations. The idea is that if we find any divisor of N, other than 1 and N, we can conclude that N is not prime, and there is no need to check further.

Here's the modified code using the `break` statement:

```java 
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int N = scanner.nextInt();

        int divisorCount = 0;
        for (int i = 1; i <= N; i ++ ) {
            if (N % i == 0) {
                divisorCount ++ ;
                if (divisorCount > 2) {
                    // If we find more than 2 divisors, break the loop
                    break;
                }
            }
        }

        if (divisorCount == 2) {
            System.out.println(N + " is a prime number.");
        } else {
            System.out.println(N + " is not a prime number.");
        }

        scanner.close();
    }
}
```

* If `cnt` is greater than 2 (meaning N has more than two divisors), the break statement is used to terminate the loop early, avoiding unnecessary iterations.
* After the loop, it checks if `cnt` is equal to 2. If `cnt` is exactly 2, it means N has exactly two divisors (1 and N), so it is prime.
* Depending on the value of `cnt`, it prints either "Prime" or "Not Prime" on the screen.

### Explaination of Continue statement

The `continue` statement is used to skip the rest of the current iteration in a loop and move on to the next iteration immediately. When the `continue` statement is encountered inside a loop, it interrupts the current iteration's execution and starts the next iteration of the loop.

We can use the continue statement to skip odd numbers and only print the even numbers between 1 and N.

```java 
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number (N): ");
        int N = scanner.nextInt();

        System.out.print("Even numbers between 1 and " + N + ": ");
        for (int i = 1; i <= N; ++ i) {
            if (i % 2 != 0) {
                // Skip odd numbers using continue statement
                continue;
            }
            System.out.print(i + " ");
        }
        System.out.println();

        scanner.close();
    }
}
```

* The code takes the input N from the user using `std::cin`.
* It then enters a for loop that iterates from 1 to N.
* Inside the loop, there is an if condition: `if (i % 2 != 0)`.
* The condition checks if `i` is odd (i.e., not divisible by 2). If `i` is odd, the continue statement is executed, and the rest of the loop's body is skipped.
* Therefore, when `i` is odd, the loop moves on to the next iteration, effectively skipping the odd numbers.
* For all even values of i, the loop prints the even numbers between 1 and N, separated by spaces.

---
## How to Solve Questions with T Test Cases

To solve questions with T test cases, you'll need to write a program that can handle multiple test cases. Typically, the input for each test case will be provided one after the other, and your program should process each test case and produce the corresponding output.

Here's a general approach to handle T test cases in your program:

* Read the value of T (the number of test cases) from the input.
* Use a loop to iterate T times to process each test case.
* For each test case, read the input data specific to that test case.
* Perform the required operations or computations for that test case.
* Output the result for that test case.
* Repeat steps 3 to 5 until all T test cases are processed.

Here's an example to illustrate the process:

```java 
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of test cases (T): ");
        int T = scanner.nextInt();

        for (int t = 1; t <= T; ++ t) {
            // Read input data specific to the current test case
            // For example, prompt the user to enter data for each test case
            // int N = scanner.nextInt();
            // String input = scanner.next();
            // ...

            // Perform computations or operations for the current test case
            // For example, process the input data and calculate the result
            // int result = processData(N, input);
            // ...

            // Output the result for the current test case
            // For example, print the result for each test case
            // System.out.println("Result for Test Case " + t + ": " + result);
            // ...
        }

        scanner.close();
    }
}
```

---
## Scope of Variables

### Explanation
The scope of a variable refers to the region of a program where that variable is accessible and can be used. It determines the portion of the code in which a variable exists and retains its value.

```java 
import java.lang.*;
import java.util.*;

class Main {
	
	// public static void main(String args[]) { 
		
	// 	// Scope of Variable
	// 	// Useful lifetime of a variable
		
	// 	int x = 10;
	// 	//....
	// 	//....
	// 	//....
	// 	System.out.println(x);		
	// 	//....
	// 	//....
	// } // closing of the parent bracket 
	// // Line 10-18 is the scope of the variable
	
	public static void main(String args[]) { 
		// Case 1
		// int x = 10;
		// int y = 15;
		// {
		// 	System.out.println(x + " " + y);
		// }
		
		// Case 2
		// int x = 10;
		// {
		// 	int y = 15;
		// 	System.out.println(x + " " + y);
		// }
		// {
		// 	System.out.println(x + " " + y);
		// }
		
		// Case 3
		// int x = 10;
		// int y = 15;
		// {
		// 	y = 10;
		// 	System.out.println(x + " " + y);
		// }
		// {
		// 	System.out.println(x + " " + y);
		// }
	}
}
```

The provided Java code demonstrates different cases illustrating variable scope in Java. Let's go through each case:

**Case 1:**

```java 
public static void main(String args[]) { 
    int x = 10;
    int y = 15;
    {
        System.out.println(x + " " + y);
    }
}

```

In this case, `x` and `y` are declared and initialized in the main method. Inside the block (denoted by curly braces {}), both `x` and `y` are accessible since they are in the same scope. **The output will be "10 15"**.

**Case 2:**

```java 
public static void main(String args[]) { 
    int x = 10;
    {
        int y = 15;
        System.out.println(x + " " + y);
    }
    {
        System.out.println(x + " " + y);
    }
}

```

In this case, `x` is declared and initialized in the main method. Inside the first block, `x` is accessible since it is in the same scope. However, `y` is declared within this block and is only accessible within this block. Attempting to access `y` in the second block will result in a compilation error because it is outside of its scope. **The output will be "10 15"**, **followed by a compilation error for the second System.out.println(x + " " + y);**.

**Case 3:**

```java 
public static void main(String args[]) { 
    int x = 10;
    int y = 15;
    {
        y = 10;
        System.out.println(x + " " + y);
    }
    {
        System.out.println(x + " " + y);
    }
}

```

In this case, `x` and `y` are declared and initialized in the main method. Inside the first block, `x` and `y` are accessible since they are in the same scope. The value of `y` is modified to 10 inside the block. **The output will be "10 10"**. In the second block, `x` is accessible, but `y` is not redeclared, so the modified value from the previous block will be used. The output will be "10 10".

