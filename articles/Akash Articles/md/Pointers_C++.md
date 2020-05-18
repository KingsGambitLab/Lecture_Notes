**Prerequisites:** Basic C++

# Pointers in C++

Do you know what happens inside the computer, when we instantiate(create) a variable?

Free memory is automatically assigned to that variable and its value will be stored in the memory.

let's see how it looks like in computer memory. 

The smallest unit of data is 1 bit, but the smallest addressable unit of memory is 1 byte(8 bits).

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/1.jpg)

Let say we are instantiating an integer, `int a = 3;`. We know that the size of an integer is 4 bytes. So, a computer will find some free 4 bytes and store its value.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/2.png)

Note that, **The address of a variable means the address of its first byte.** So basically, when we read or write a variable, a computer only reads or writes some number of bytes according to the size of a variable(4 bytes in case of an integer).

Generally, we don't have to worry about which memory-address is assigned, we can directly use the name of the variable to manipulate its value.

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    int a = 3;
    cout << a << "\n"; // Prints 3
    a += 1;
    cout << a << "\n"; // Prints 4
    return 0;
}
```
Therefore, when you use variable `a` computer goes to its memory-address and reads or writes its value. Can we check what address is assigned to a variable?

**Address-of operator(&)** can be used to find the address of a variable.

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    int a = 1;
    cout << a << "\n"; // Prints 1
    // Prints memory-address of variable a
    cout << &a << "\n";
    return 0;
}
```
Note that address of a variable is also an integer but it can not be stored in integer. For example, `int b = &a;` is **invalid**. We need something special, let's see what.

Now, suppose we have a mechanism that allows us to **manipulate the variable via its address**, then what kind of advantages we can take?

Let's see an easy to understand the advantage. Suppose, we want to pass a large variable to a function.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/3.jpg)

Passing via usual way(by value) will create a copy of the large variable.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/4.png)

But now we will pass the address of a variable and use the mechanism to avoid a copy of the large variable.
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/5.png)

So basically, we are passing values indirectly using just the address of a variable.

This mechanism is known as a **Pointer**. **Pointer** is a special kind of variable that stores the address of a variable. So they point to the address of a variable, and therefore it is a **Pointer**.

Before discussing how to declare a pointer variable, let's see how to access a value at a given memory-address? We have a **dereference operator($*$)**.

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    int a = 1;
    cout << &a << "\n"; // Prints memory-address
    cout << *(&a) << "\n"; // Prints 1
    cout << a << "\n"; // Prints 1
    return 0;
}
```

### How to declare a pointer variable?

Syntax to declare a pointer variable is the same as normal variables, just an additional asterisk($*$) between data type and variable name.

Syntax: `datatype *name;`

```cpp
/// Declarations of pointer variable
int *a;
double *b;

struct coordinate{
    double x;
    double y;
};
coordinate *c;
```
Pointer variables stores memory-address(which is an integer), therefore on 32-bit machine and 64-bit machine it's size is 4-bytes and 8-bytes respectively.

Take care while declaring two pointers in single line,
```cpp
// ptr2 is an integer not pointer
int *ptr1, ptr2;
// Both are pointers
int *ptr1, *ptr2;
```
The best practice is to declare pointers in different lines.

### How to assign a value to a pointer variable?

As we know, pointer variables store the address of another variable. Therefore, **the value must be an address of a predeclared variable of the same datatype as of pointer variable**.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/6.png)

```cpp
#include <iostream>
using namespace std;

int main()
{
    // Pointer variables
    int a = 2;
    
    // Use address-of operator(&)
    int *b = &a;

    // Prints address of variable a
    cout << &a << "\n";
    // b also contains address of a
    cout << b << "\n";
    
    return 0;
}
```
**Output**: <code>0x7ffd578993d4
0x7ffd578993d4</code>

Observe below thing:
```cpp
int a = 3;
int b = 5;

int *ptr1 = &a;
int *ptr2;

ptr2 = &b; // Points to b

ptr2 = ptr1; // Now points to a
```

### How to use "dereference operator" on a pointer variable?

Dereference operator is used on pointers to access the values(or content) it is pointing to. It is called **dereferencing a pointer**.

```cpp
#include <iostream>
using namespace std;

struct coordinates{
    double x;
    double y;
};
 
int main()
{
    int one = 1;
    int *ptr = &one;
    
    // Use dereference operator
    cout << *ptr << "\n";
    
    coordinates a{1.5, 4.5};
    coordinates *z = &a;
    
    // Use dereference operator
    cout << "(" << (*z).x << ", " << (*z).y << ")" << "\n";
    
    return 0;
}
```
**Output**:
<code>1
(1.5, 4.5)
</code>

**Notes** 
1. If you try to dereference an uninitialized pointer, then it is an error.
2. If you want to access struct(or class) members from pointer of type struct(or class) without using dereference operator, then there is another operator(`->`), which is known as a **"member selection operator"**.

    For the above code example, you can access members of z as below:
    `cout << "(" << z->x << ", " << z->y << ")" << "\n";`

So far, you have understood what is a pointer and how to use it. Now, let's discuss more details.

## Null Pointer

Pointers can also be initialized with a special **null value** other than memory-address, which represents that pointer does not point to anything. There are three different ways to assign null value to pointers:

1. Use simple zero  --> `ptr = 0`
2. Use `NULL` macro --> `ptr = NULL`
3. Use C++ keyword `nullptr` --> `ptr = nullptr`

**Note:** Using `nullptr` is the standard way to do so.

**All these values are false values under conditional statements.**

```cpp
#include <iostream>
using namespace std;

int main()
{
    int *a;
    
    // First way
    a = 0;
    // Second way
    a = NULL;
    // Third and the safest way
    a = nullptr;
    
    if(!a)
        cout << "I am null" << "\n";
    
    return 0;
}
```
It is always a good thing to initialize a pointer with a null value if we are not initializing it with any other value.

## Void Pointer

Void pointer is a special type of pointer that can be used to point objects of any data type. Therefore, it is called a **general-purpose pointer**.

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    int a = 1;
    double b = 2;
    float c = 3;
    
    void *ptr = nullptr;
    
    // All things below are valid
    ptr = &a;
    ptr = &b;
    ptr = &c;
    
    return 0;
}
```
Now, when you want to dereference it, you have to explicitly cast it to a corresponding data type.

```cpp
#include <iostream>
using namespace std;
 
struct coordinate{
    int x;
    int y;
};
 
int main()
{
    int a = 1;
    double b = 2;
    coordinate c{1, 3};
    
    void *ptr;
    
    ptr = &a;
    cout << *((int*)ptr) << "\n"; // 1

    ptr = &b;
    cout << *((double*)ptr) << "\n"; // 2

    ptr = &c;
    cout << ((coordinate*)ptr)->x << " " << ((coordinate*)ptr)->y << "\n"; // 1 3
    
    return 0;
}
```
**Note:** Casting can be done by some other ways as well.

Void pointer is used when you are dealing with objects of different data types. It is important in C language, but in C++, mostly it is not used because there are many easy ways(templates) to deal with that scenario. 

It becomes helpful if you are working with mix C and C++ environment.

Now, let's discuss how pointers and arrays are closely related.

## Pointers and Arrays

Let's observe something in the following code:

```cpp
#include <iostream>
using namespace std;

int main()
{
    int array[4] = {1, 6, 9, 11};
    
    // Both things below prints the same thing:
    // Address of the first element
    cout << array << "\n";
    cout << &array[0] << "\n";

    // Dereferencing
    // Both prints 1
    cout << *array << "\n";
    cout << array[0] << "\n";
    
    return 0;
}
```
What did you observe?

You can see that arrays are also using pointer, which points to the first element of the array.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/7.png)

But a fixed array is not exactly a pointer, let's see:

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    int array[4] = {1, 6, 9, 11};
    
    int *ptr = array;
    
    // sizeof int = 4 byte => 4 * 4 = 16 byte
    cout << sizeof(array) << "\n"; // 16
    
    // For 64-bit machine, size of pointer is 8 byte
    cout << sizeof ptr << "\n"; // 8
    
    return 0;
}
```
Therefore, a fixed array and a pointer are not the same. One more difference will unfold in pointer arithmetic.

**Note:** `sizeof` is a standard C++ operator.

**Can we move to other elements of the array by using the address of the first element?**

Yes, add `sizeof(data type of array)` bytes to the address of the first element and you will get the address of the second element and so on. Now, It is time to introduce **Pointer arithmetic**.

## Pointer arithmetic

In C++, we can use basic math operations(addition and subtraction) on pointer as well. But it is different. If you add(or subtract) integer $a$ to pointer containing some address, then it will add(or subtract) `a*sizeof(data type of the pointer)`(ex. `a*(4 byte)` for integer pointer) to its address.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/8.png)

As array elements are continuous(sequential) in memory, **pointer arithmetic is basically used when we access array elements using [] operator(ex. array[3]).** 

Note that `3[array]` and `array[3]` are considered as same.

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    int array[4] = {1, 6, 9, 11};
    
    int *ptr = array;
    
    // Addresses
    cout << ptr << "\n";
    cout << ptr + 1 << "\n";
    cout << array + 2 << "\n";
    cout << ptr + 3 << "\n";
    
    // Values
    cout << *ptr << "\n"; // 1
    cout << *(ptr + 1) << "\n"; // 6
    cout << *(ptr + 2) << "\n"; // 9
    ptr += 3;
    cout << *(ptr) << "\n"; // 11
    
    return 0;
}
```
**Output:**
<code>0x7ffeffe090f0
0x7ffeffe090f4
0x7ffeffe090f8
0x7ffeffe090fc
1
6
9
11
</code>

**Note:** If you try to dereference memory-address outside this array bound, it is unpredictable which value you will get.

Note that we can use `++`, `--`, `+=`, `-=` operators on a pointer, but not on the array. Therefore, in the array, it only makes sense to use `+ operator`.

```cpp
int array[4] = {1, 6, 9, 11};
int a = *(array + 1); // valid
array += 1;  // invalid

int *ptr = array;
ptr +=1 // valid
ptr -=1 // valid
```

Now, let's check how well you have understood things so far.

### Quiz

1. Predict the output of the following C++ program:
    ```cpp
    #include <iostream>
    using namespace std;
     
    struct test {
        int size;
        int arr[4];
    };
     
    int main()
    {
        test a;
        a.size = 4;
        a.arr[0] = 1;
        a.arr[1] = 2;
        a.arr[2] = 3;
        a.arr[3] = 4;
        
        test *ptr = &a;
        
        cout << ptr->size << "\n";
        cout << *(ptr->arr) << " ";
        cout << *((*ptr).arr+1) << " ";
        cout << *(ptr->arr+2) << " ";
        cout << ptr->arr[3] << "\n";
        
        return 0;
    }
    ```
    **Answer:**
    <code>4
    1 2 3 4</code>
2. Predict the output of the following C++ program:
    ```cpp
    #include <iostream>
    using namespace std;
     
    int main()
    {
        int a[4]{0, 2, 5, 7};
        cout << *a << " ";            
        int *ptr = a + 3;
        cout << ptr[-1] << " ";
        cout << 3[a] << " ";
        cout << *&*(a+1) << "\n";
        return 0;
    }
    ```
    **Answer:**
        `0 5 7 2`

## Pointers to Pointers

Pointer to Pointer is a pointer that holds the address of another pointer variable. It can be declared by putting two asterisks (`**`) instead of one.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/9.png)

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a;
    int *b;
    
    // Declaration of pointer to pointer
    int **c;

    a = 5;
    b = &a;

    // Assign address of anonther pointer
    c = &b;
    
    cout << *b << " " << **c; // 5 5
    
    return 0;
}
```
Dereferencing of a pointer to pointer work as follows: We use a dereference operator two times.

`**c => *(*c) => *(b) => *(&a) => a`

Similarly, we can have pointer to pointer to pointer... For example, `int ***ptr` or `int ****ptr`.

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    int a = 5;
    int *b = &a;
    int **c = &b;

    // Pointer to pointer to pointer
    int ***d = &c;
    
    cout << ***d << "\n"; // 5
    
    return 0;
}
```
**Pointer to pointer and 2D-array**
2D-arrays are pointers to pointers. They are stored in continuous memory as 1D-arrays, but pointer arithmetic makes our work easier. 

Observe the below image and try to understand the shown pointer arithmetic.

Note that, `a[x][y]` in pointer arithmetic sense is basically `*(*(a+x)+y)`. 

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Pointers/10.png)

Here `sizeof(a[0])` or `sizeof(*a)` is 3 integers, i.e. 12 bytes and therefore in pointer arithmetic, if we add 1 to `a`, then it basically adds 12 bytes.

Now, attempt the quiz below, it will make the whole thing clear.

### Quiz
1. Predict the output of the following program:
    ```cpp
    #include <iostream>
    using namespace std;

    int main()
    {
        int a[3][3]{
                    {1, 2, 3},
                    {4, 5, 6},
                    {7, 8, 9}
                   };
        
        cout << **a << "\n";
        cout << *(*(a + 2) + 1) << "\n";
        cout << *(*a + 5) << "\n";
        cout << *(a[1]) << "\n";
        cout << *(a[2] + 2) << "\n";
        cout << 1[1[a]] << "\n";
        
        return 0;
    }
    ```
    **Answer**:<code>1
8
6
4
9
5</code>
2. Predict the output of the following program:
    Note that `char*` datatype is basically an array of characters, string.
    ```cpp
    #include <iostream>
    using namespace std;

    int main()
    {
        // (char*) converts C++ string to c-style string
        char *strings[3] = {
                            (char*)"Interview",
                            (char*)"InterviewBit", 
                            (char*)"Scaler"
                           };
        
        // Pointer to Pointer to Pointer
        char *(*ptr)[3] = &strings;
        
        cout << (*ptr)[1] + 9;
        
        return 0;
    }
    ```
    **Answer:**
    `Bit`
    
## Pointers vs References

### Intro to references
A reference variable acts as an alias for another variable. Reference can be declared by putting `&` sign in place of `*` for pointer, ex. `int &a`, and value can be assigned by using variable name directly, instead of the address of the variable(in the case of pointers).

Syntax: `datatype &name = var_name;`

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    int a = 5;
    
    // Pointer
    int *ptr = &a;
    
    // Reference
    int &ref = a;
    
    // Accessing value
    cout << *ptr << "\n"; // 5
    cout << ref << "\n"; // 5
    
    return 0;
}
```

**Intrinsically, references are using pointers but it is easy to use as we don't have to use dereferencing like pointers to access values.** 

**That is, it acts as an alias for a variable.**

### Differences between Pointers and References

If reference is easy to use, then why should we use pointers? Here are the differences between References and Pointers, which distinguish them:

1. References must be initialized when they are declared but pointers don't need so.
    ```cpp
    #include <iostream>
    using namespace std;
     
    int main()
    {
        int a = 5;
        
        // Reference
        int &ref = a; // valid
        
        int &ref2; // invalid
        ref2 = a;  // invalid
        
        // Pointer
        int *ptr = &a; // valid

        int *ptr2;    // valid
        ptr2 = &a;  // valid
        
        return 0;
    }
    ```
2. References can not be reassigned, but pointers can be reassigned. 

    Note that if you try to reassign a reference, then it will change the content of the object it is currently referencing.
    ```cpp
    #include <iostream>
    using namespace std;
     
    int main()
    {
        int a = 1;
        int b = 2;
        
        // Pointer
        int *ptr = &a; // valid
        ptr = &b;  // valid
        
        cout << *ptr << "\n";
        cout << a << "\n";
        
        // Reference
        int &ref = a; // valid
        ref = b;  // will change a to b
        
        cout << ref << "\n";
        cout << a << "\n";
        
        return 0;
    }
    ```
3. There is no such thing as **null value** for references.
4. There is nothing like "reference to reference".
    For example, `int &&ref_to_ref` is invalid declaration, but we do have `int **ptr_to_ptr`.

Therefore, use pointers and references as per the requirements.

## Passing arguments to functions

Now, we know how pointers and references work. Now, let's have a closer look at how we use pointers and references to pass variables effectively.

### Pass by value
In pass by value, we use normal variables as a function parameter. For example, consider the below code.

```cpp
#include<iostream>
using namespace std;

struct foobar {
    int size;
    int arr[50];
};

int sum(foobar b)
{
    int sum = 0;
    for(int i{0}; i < b.size; i++)
        sum += b.arr[i];
    return sum;
}

int main()
{
    foobar a;
    a.size = 10;
    for(int i{0}; i < a.size; i++){
        a.arr[i] = i+1;
    }
    cout << sum(a) << "\n";
    return 0;
}
```
In function `sum(foobar b)`, variable `a` is passed by value. So, basically when we pass `a` to `sum(a)`, **it will make a copy variable `b`**. Which means that it will allocate new memory of amount `sizeof(a)`.

Now, imagine a situation when you want to pass a variable containing an array of say 1,00,000 integers to a function, then by this method, you will end up copying such a big variable. 

But, can we do it without copying? Can you find out the solution from what we have discussed so far?

"**Use Pointers or use References**"

### Pass by address

So, we can use a pointer as a parameter and as an argument pass address of variable `a`.

```cpp
#include<iostream>
using namespace std;

struct foobar {
    int size;
    int arr[50000];
};

int sum(foobar *b)
{
    int sum = 0;
    for(int i{0}; i < b->size; i++)
        sum += b->arr[i];
    return sum;
}

int main()
{
    foobar a;
    a.size = 50000;
    for(int i{0}; i < a.size; i++)
        a.arr[i] = i+1;
    cout << sum(&a) << "\n";
    return 0;
}
```
Therefore, we just end up allocating new memory of amount of size of a pointer(4 or 8 byte) instead of large array.

**Note that you can modify the content of variable `a` inside the function via dereferencing. But in pass by value, you can modify copy `b` which will not affect `a`.**

**If you don't want to allow modification, then use `const` keyword in parameters.** We will discuss it soon.

Another thing to take note is that we are passing address by value, and therefore modifying the address of parameter pointer will not affect the actual address. See the quiz question below.

**Quiz**
Predict the output of the following:
```cpp
    #include <iostream>
    using namespace std;

    void f(int *ptr1, int *ptr2)
    {
        ptr1 = nullptr;
        *ptr2 = 10;
    }

    int main()
    {
        int a = 5, c = 9;
        int *b = &a, *d = &c;
        f(b, d);
        cout << *b << " " << *d << "\n";;
        return 0;
    }
```
**Answer:** `5 10`

Now, if you want to modify the address inside the function, then use pass by reference.

### Pass by reference

We use reference as a parameter for this case. Same as pass by address, in this case also we can manipulate variables without making any extra copy.

It is easy to use because we don't have to use `*` or `->` operators as in case of pointer. Therefore, if the same thing can be achieved by using reference, then use reference rather than pointer.

```cpp
#include<iostream>
using namespace std;

struct foobar {
    int size;
    int arr[50000];
};

int sum(foobar &b)
{
    int sum = 0;
    for(int i{0}; i < b.size; i++)
        sum += b.arr[i];
    return sum;
}

int main()
{
    foobar a;
    a.size = 50000;
    for(int i{0}; i < a.size; i++){
        a.arr[i] = i+1;
    }
    cout << sum(a) << "\n";
    return 0;
}
```
Now, if you pass address by reference, then you can modify address as well. Recall the last quiz!

```cpp
#include <iostream>
using namespace std;

void f(int* &ptr1)
{
    ptr1 = nullptr;
}

int main()
{
    int a = 5;
    int *b = &a;
    f(b);
    if(!b)
        cout << "become null\n";
    return 0;
}
```

**Output:** `become null`

Let's see what is **constant pointer**, **constant reference** & **pointer to constant value**. These things are useful when you are using pass by address or pass by reference and don't want to allow to change variables inside the function.

1. **Constant pointer**:
    ```cpp
    int var = 1;
    
    // const pointer initialized with address of var
    int *const ptr = &var;
    
    int var2 = 2;
    
    // Now you can not change it to point some other variable
    ptr = &var2; // ERROR
    
    // But change of value is allowed
    *ptr = 3; // Valid

    ```
2. **Pointer to constant & non-constant value**:
    ```cpp
    const int var = 1;
    
    // Pointer to const value
    // Note that it is not a constant pointer    
    const int *ptr = &var;
    *ptr = 6; // Invalid, ERROR
    
    int foo = 2;
    
    // Pointer to non-const value
    const int *ptr2 = &foo;
    
    // Does not allow to change value via dereferencing
    *ptr2 = 4; // Invlid, ERROR
    foo = 4; // Allowed
    
    // ptr points to a new const value
    ptr = &foo; // Allowed
    ```
    **Const pointer to a const value:**
    ```cpp
    int bar = 3;
    // It can neither point to another variable
    // nor its value can be changed through dereferencing
    const int *const ptr3 = &bar;

    int foo = 5;
    ptr3 = &foo; // Invalid

    *ptr3 = 6; // Invalid
    ```
3. **Constant reference:** Most of the rules are same as const pointer, but recall that **reference can not be reinitialized**.
    ```cpp
    int x = 5;
    const int &ref1 = x;
    
    x = 6; // valid
    ref1 = 6; // invalid
    
    const int y = 7;
    // Reference to const value
    const int &ref2 = y;
    ```

**Therefore, basically you can use `function(const int* ptr)` or `function(const int &ref)` to prevent modification inside functions.**

## Dynamic Memory Allocation

Dynamic memory allocation happens at run time, so basically it allows us to use memory as the need arises at the run time, rather than allocating some fixed maximum amount of memory our program is expected to use. 

The later is not efficient because most of the applications we use are dynamic and we don't know beforehand how much memory we will need.

For example, we announced a programming contest and we are collecting data from each registrant. So, we do not know how many people are going to register in advance, which is completely dynamic.

**Using pointers is the only way you can dynamically allocate memory in C++.** How?

We use `new` operator to allocate memory dynamically. There are two types of syntax:

1. Single variable: `datatype *name = new datatype;`
Ex. `int *ptr = new int;`
2. Array of variables: `datatype *name = new datatype[length]`
Ex. `int *ptr_arr = new int[10];`
Note that length can be any value you provide at run time or compile time.

The way `new` operator works is that it first checks whether a computer has free memory of the amount requested by a programmer.

If yes, then it will return the address of that available memory. In case that much memory is not available, it will result in `bad_alloc` exception followed by termination of the program.

**One of the advantages of using dynamic memory allocation is that it uses a much larger pool of memory managed by the operating system called the "heap" to allocate memory, which allows us to allocate a larger amount of memory than usual.**

Therefore, allocate memory dynamically when a large amount of memory is required.

Dynamically allocated memory remains allocated until we deallocate it explicitly using `delete` operator.

Syntax for `delete` operator is as below:
1. Single variable: `delete name`
Ex. `delete ptr`
2. Array of variables: `delete[] name`
Ex. `delete[] ptr_arr`

Note that `ptr` and `ptr_arr` are addresses of newly allocated memory.

**Now, if we forget to deallocate the memory explicitly, then it gives rise to some problems because this memory can not be used by another program until it is deallocated.**

To deallocate memory, we have to maintain the address of the new allocated memory(as seen in `delete`), if we somehow lose it, then we will not be able to deallocate it anymore and **memory leak** will occur.

### Memory leak

Memory leak occurs when new memory is allocated dynamically and never deallocated. Let's see some scenarios when memory leak occurs.

1. Memory leaks can result from a pointer going out of scope. Because we have lost the address of newly allocated memory.
    ```cpp
    #include <iostream>
    using namespace std;

    void f()
    {
        int *ptr = new int;
    }

    int main()
    {
        f();
        // Memory remains allocated
        // because we haven't deallocated
        // before we lost the address
        return 0;
    }
    ```

2.  A memory leak can occur if a pointer holding the address of the dynamically allocated memory is assigned another value.
    ```cpp
    #include <iostream>
    using namespace std;

    int main()
    {
        int a = 1;
        int *ptr = new int;
        ptr = &a; // memory leak!
        // We have lost the address
        return 0;
    }

    ```
3. Double-allocation results in a memory leak.
    ```cpp
    #include <iostream>
    using namespace std;

    int main()
    {
        int *ptr = new int;
        ptr = new int; // previous address lost
        return 0;
    }
    ```
Now, can you figure out what kind of problems it can create?

A memory of a computer is responsible for the proper functioning of the system. All applications running on a computer have some amount of memory requirements. If it can not be satisfied, then the system will stop working(will hang).

Now, due to memory leaks, there will be useless allocated memory. As this kind of memory grows in size, it will affect the performance of the computer(due to less amount of available memory). And in the worst-case situation, the system will stop working correctly.

**Note that in modern systems, operating systems deallocates memory allocated during a run of a program at the end of execution.** But while the program is running and you don't get enough memory, then program will break down.

There is also a concept of **automatic memory management**, which means that programmers don't have to take care about allocating or deallocating objects manually.

Programming languages like python, C#, java, ruby, Go provides **automatic memory management** feature along with garbage collection. **Garbage** here stands for memory which is no longer in use by the program like in the case of **Memory leak**. **Garbage Collection** means that it automatically deallocates garbage memory. Therefore in these languages, we don't have to worry about this issue.

**Rust** programming language also has manual memory management, but when a variable whose data is allocated manually goes out of scope, it will automatically deallocate that memory unless it is moved to be owned by another variable. Rust and C++ also has something known as **Smart pointers**, which also solves **dangling pointer problem**.

Memory leak is a programming issue and we must take care of it.

**Only Solution:** Deallocate before anything goes wrong.

### Dangling pointer

A pointer that is pointing to a deallocated memory is called a **dangling pointer**.

**Problems due to dangling pointer:**
1. Dereferencing a dangling pointer will give undefined result. Note that it will not give any compiler or run time error, but some random result.
2. Deallocation of dangling pointer will result in abort call(core dumped).

```cpp
#include <iostream>
using namespace std;

int main()
{
    int *ptr = new int;
    *ptr = 4;
    
    delete ptr;
    
    // Now ptr is a dangling pointer
    // Both things below: Dereferencing & 
    // redeleting will lead to bad behavior
    cout << *ptr << endl;
    delete ptr;
	
	ptr = new int;
	*ptr = 3;
	
	int *ptr2 = ptr;
	
	delete ptr;
	
	// ptr2 is now dangling pointer
	// because it is pointing to deallocated memory
    
    return 0;
}
```

**A way to avoid this scenario**:

To deal with this problem, a good way is to set the pointer to `nullptr` immediately after deallocating a pointer. Now, you can check whether the pointer is alredy deallocated by just checking whether it is a `nullptr`.

```cpp
#include <iostream>
using namespace std;

int main()
{
    int *ptr = new int;
    *ptr = 4;
    
    delete ptr;
	// Make it NULL
	ptr = nullptr;
   
    if(ptr) {
        cout << *ptr << endl;
        // Safe deallocation
	    delete ptr;
	}	
    return 0;
}
```

Note that dereferencing a null pointer will lead to abort call.

Now, consider the situation below:

```cpp
#include<iostream>
using namespace std;

int main()
{
	int *ptr = new int;
	*ptr = 3;
	
	int *ptr2 = ptr;
	
	delete ptr;
	ptr = nullptr;
	
	// Results in undefined behavior
	// ptr2 is not null!
	if(ptr2)
		delete ptr2;

	return 0;
}
```
Note that "assign to `nullptr`" technique will not work in this situation. Because a dangling pointer `ptr2` still contains address of `ptr`, which is not null. Therefore, it results in undefined behavior.

Now, what is the solution (other than taking care while programming)? In C++, a popular technique to avoid dangling pointers is to use "**smart pointers**". But we are not going to discuss it here, as this is an introductory article.

## Other usages of pointer

1. Pointers can be used to pass a function as a parameter to another function.
2. This is useful in data structures, such as linked lists and trees, to form chains using pointers.
