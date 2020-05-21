# String Concatenation Problem

String concatenation is an operation to join strings end-to-end.

For example, concatenation of string `"Interview"` with `"Bit"` results in `"InterviewBit"`. We denote concatenation as + operator on strings ex. `"Interview"+"Bit"="InterviewBit"`.

Before we go further let's first understand some notions.

- Mutable objects are those which are modifiable and immutable objects are not modifiable.
- The rule for an immutable object is that once they are created, you can not change the object itself, but you can change the reference to the object.
    For example, you have an immutable string `a = "immutable"`. Now, any kind of modifications (like `a[2] = '-'`) is not allowed, but reassignment `a  = "it's immutable"` is allowed.
- Therefore, Immutable objects and constant objects are different notions, as reassignment is not allowed in case of constant objects.

Let's see how "string concatenation" works internally.

If we are concatenating mutable string `a` with `b`, then it happens as follows,

```
i = 1
while i <= b.length
    append b[i] to a
    i++
```

**Note that above implementation is the best way to do so, but it still depends on the method used to concatenate strings, we will discuss it, keep reading!**

Let say the size of string `a` is $N$ and string `b` is $M$. So what are the time and space complexities?

**Time complexity:** $O(M)$<br>
**Space complexity:** $O(N+M)$

Note that it does not matter whether `b` is mutable or immutable because we are appending to string `a`.

But what happens when you are concatenating to an immutable string? As we know we cannot modify immutable string and therefore we can not simply append characters as in the mutable case. So, how it works in the case of immutable string?

First of all it creates a new string of size `length(a)+length(b)`. Then it copies string `a` and then strings `b` to it such that the resulting string is concatenated string(`a+b`).

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/String_builderN%5E2.png)

So what are the time and space complexities in this case?

**Time complexity:** $O(N+M)$<br>
**Space complexity:** $O(N+M)$

Note that in reality it has allocated more memory than the mutable case. It is observable when we are concatenating many strings rather than one.

let say we are concatenating $M$ strings of length $N$ to an immutable string which is empty at the start. Then what will be the time complexity?

**Answer:** $N + (N+N) + (N+N+N) + .... + M*N)=(N*(1+2+..+M)) = (N*(M*(M+1))/2) = O(N*M^2)$

Which is quadratic in terms of the number of strings($M^2$), whereas if the string is mutable at the start, it will take only $O(N*M)$(a linear function of $M$).

Space complexity is also similar. But useless old strings are declared as garbage, and the garbage collector will take care of that.

**But why do we have immutable strings in the first place?**

Although most of the time objects we create are mutable, there are reasons why many programming languages like java, python, C#, javascript, Go have immutable inbuilt strings.

Note that there are ways to impose immutability even if we have inbuilt mutable strings in a programming language.

Here are some most common briefly discussed reasons for having inbuilt immutable strings:

1. **Synchronization:** Immutable strings are thread-safe,  since they won't be changed when accessed from multiple threads, rather new copies will be created.

2. **Caching:** Caching of hashcodes of string objects is very important for performance reason and begin immutable guarantees that hashcode will always be the same.

3. **Security:** Strings are used to store sensitive pieces of information like usernames, passwords, connection URLs, etc. If strings are mutable, then a connection or file would be changed and this can lead to a serious security threat.

Therefore, immutable strings have lots of advantages, but a single downside is a concatenation problem and therefore we should learn how to deal with it.

Now, we are going to discuss dos and don'ts to concatenate strings in Java, Python, Javascript, C++. Where first three have inbuilt immutable strings and C++ has inbuilt mutable strings, but still we face this issue.

**Important Notes:** 
- **"Bad way" in a further discussion means it works the immutable way as discussed above, $O(N*M^2)$ and "good way" works the mutable way,  $O(N*M)$.**
- **`str_arr` is an array of strings which is assumed to already have all strings we want to concatenate.**

## Java

### Don'ts 

`+ operator` and `concat()` methods are bad ways to concatenate strings in java because they create new strings on each concatenation as discussed before.

```java
// Using + operator
String s = "";
for (int i = 0; i < N; i++)
    s = s + str_arr[i];
// Using concat() method
for (int i = 0; i < N; i++)
    s.concat(str_arr[i]);
```

### Dos

Using `StringBuilder` is the best way to handle strings, which are changing quite often, in java.

```java
// Using stringbuilder
StringBuilder builder = new StringBuilder();
for (int i = 0; i < N; i++)
    builder.append(str_arr[i]);
// Finally get the string
String s = builder.toString();
```

There is also something called `StringBuffer`, but it is less efficient than `StringBuilder`.

## Python

Don't use `+` operator to concatenate strings in python as well.

### Dos

The best way to concatenate strings in python is to use a list to store all the strings we want to concatenate and then we can just simply use `join()` function at last.

**Note that you add or remove strings from the list at any place and when you want your concatenated string back, you can simply use `join()` function.**

```py
s = ""
ans = s.join(str_arr)
# Note that s is a seperator and can be any string
# you want to seperate your strings with,
# for example
# s = "-"
# str_arr = ["InterviewBit","Scaler"]
# ans = s.join(str_arr)
# ans is "InterviewBit-Scaler".
```

## Javascript

### Don'ts

Like Java in Javascript, using `+ operator` and `concat()` methods are bad.

```js
let i;

// + operator
let s = "";
for(i = 0; i < str_arr.length; i++)
    s = s + str_arr[i];

// concat() function
let s = "";
for(i = 0; i < str_arr.length; i++)
    s.concat(str_arr[i]);
// Note that in concat you can provide any number
// of arguments seperated by comma
```

**Modern javascript engines also optimizes `+ operator`.**

### Dos

In javascript, using `+=` operator is the fastest way to concatenate strings. But when we are supposed to concatenate a variable number of strings, then using `join()` on an array of strings is the flexible way.

```js
// += operators
let s = "";
for(i = 0; i < str_arr.length; i++)
    s += str_arr[i];

// join() method
// Note that argument to join is a seperator
// You can pass any seperator. Default is ','
let s = "";
s = str_arr.join('');
```

## C++

### Don'ts

Although C++ strings are mutable, `+ operator` on C++ strings is not working the good way. It works the bad way.

```cpp
string s = "";
for(int i = 0; i < str_arr.size(); i++)
    s = s + str_arr[i];
```

### Dos

`+= operator` and `append()` are good ways to concatenate strings in C++.

```cpp
// += operator
string s = "";
for(int i = 0; i < str_arr.size(); i++)
    s += str_arr[i];

// string append()
string s = "";
for(int i = 0; i < str_arr.size(); i++)
    s.append(str_arr[i]);
```
