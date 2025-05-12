# DSA: Strings


## String

A string can be defined as a sequence of characters or in other words we can say that it is an array of characters.

### Example
Below are the examples of string:
```
"Welcome to Scaler"
"Hello World!"
```
**Note:** String is represented using double quote i.e, `""`. All the characters of string must be inside this quote.

### Character
A character is a single symbol that represents a letter, number, or other symbol in a computer's character set. Characters are used to represent textual data, and they are typically represented using its ASCII value. 
### Example
```
'a'
'B'
'1'
'_'
```

Computer store everything in binary. So, how do we store strings in computer?

Each character has corresponding decimal value associated to it which is known as ASCII value.

**'A' to 'Z'** have ASCII from **65 to 90**
**'a' to 'z'** have ASCII from **97 to 122**
**'0' to '9'** have ASCII from **48 to 57**

Each character '?', '!', '\*', ... has a corresponding ASCII associated with it.

### Some Operations:
**Note:** Characters can also be printed using its ascii value. for example, the ascii value of 'A' is 65, so it can be printed as
```CPP=
char ch = (char)65;
print(ch);    
/* 
character 'A' gets printed; we are assigning Integer to Char,hence in some languages typecasting will be required.
*/
```

```cpp=
char ch = (char)('a' + 1);
/*
When we do arithmetic operations on characters, automatically computations happen on their ASCII values.
 */
print(ch); //'b' will get printed
```

```cpp=
int x = 'a';
/*
No need to typecast since we are assigning Char to Int (smaller data type to bigger, so it will not overflow)
*/
print(x); //97 will be printed

```

---
## Problem 1 Togglecase

### Problem Statement

Given a string consisting of only alphabets(either lowercase or uppercase). Print all the characters of string in such a way that for all lowercase character, print its uppercase character and for all uppercase character, print its lowercase character.

### TestCase
#### Input
```
"Hello"
```

#### Output
```
"hELLO"
```

#### Explanation

Here, there is only one uppercase character present in the string i.e, 'H' so convert it to lowercase character. All other characters are in lowercase, hence they are converted into uppercase characters.


---
### Question
What is the output for String = "aDgbHJe" ?

### Choices
- [ ] ADGBHJE
- [ ] aDgbHJe
- [x] AdGBhjE
- [ ] adgbhje

---

## Approach - Subtract or Add 32


### Observation
The key observations are:
* Lowercase characters can be changed into uppercase by subtracting 32 from its ASCII values.
* Uppercase charactes can be changed into lowercase by adding 32 from its ASCII values.

The above points are derived from the fact that for every alphabet, the difference between its ascii value in lowercase and uppercase is 32.

### Pseudocode
```javascript
function solve(string A) {
    N = A.size(); //use function present in your language to get length
    for (i -> 0 to N - 1){
        if(A[i] >= 'a' && A[i] <= 'z'){
            A[i] = (char)(A[i] - 32);
        }
        else{
            A[i] = (char)(A[i] + 32);
        }
    }
    return A;
}
```

> Problem 1 Changing same string is not possible in Java or Python

NOTE: 
1. In above code, we are making changes to the same given string. 
2. This is not possible in languages like Java and Python, since we cannot change a string. Example: If we have "Scaler", then if we try changing it to "Scalar", then it won't do changes to same string.
3. The concept is known as "String Immutability", that we shall learn later in this session.
4. So, what to do for these languages ? We can create a new string and keep adding a character to it ?

### Pseudocode
```javascript
function solve(String A) {
    res = "";

    for(i -> 0 to A.length() - 1) {
        if(A[i] >= 'a' && A[i] <= 'z') {
            res += (char)(A[i] - 32);
        }
        else {
            res += (char)(A[i] + 32);
        }
    }
    return res;
}
```

The above code will create a new string everytime a character is added, which means adding one characters can take O(N) time, making it highly un-optimal in Java. Hence, the above code will give TLE in Java.

Though in Python, string handling is optimized for operations like these on small to moderately sized strings. Python efficiently manages new string creation and memory, which prevents performance degradation in many practical scenarios. Hence, the above code shall work for Python for small strings, but for large strings, it can fail.

> How to make the code work for Java and large inputs in Python ? (next section)

### Using character array instead


**`String is nothing but array of characters, so at the start of the program we can convert the string to array of characters and rather perform operations on that character array. Once done, we can convert it back to string.`**

### Pseudocode
```javascript!
----JAVA----
String solve(String A) {
    char arr[] = A.toCharArray(); //for java

    for(int i=0; i < arr.length;i++) {
        if(arr[i] >= 'A' && arr[i] <= 'Z') {
            arr[i] = (char)(arr[i] + 32);
        } 
        else {
            arr[i] = (char)(arr[i] - 32);
        }
    }

    return new String(arr);
}

----PYTHON----
class Solution:
    def solve(self, A):
        char_list = []
        for c in A:
            if 'A' <= c <= 'Z':
                char_list.append(chr(ord(c) + 32))
            else:
                char_list.append(chr(ord(c) - 32))
        return ''.join(char_list)
```
### Complexity
Time Complexity- **O(N)**.
Space Complexity- **O(1)**.

---
### Question
Considering the immutability of strings in most programming languages, if you start with an empty string and keep adding one character at a time, how many string objects will be created when forming the string "abcdef"?

### Choices
- [ ] 7
- [x] 6
- [ ] 12
- [ ] 1

### Explanation

In most programming languages, strings are immutable. This means that each time you modify a string, a new string object is created. If you start with an empty string and add one character at a time to form the string "abcdef", the process would look like this:

"" -> "a"
"a" -> "ab"
"ab" -> "abc"
"abc" -> "abcd"
"abcd" -> "abcde"
"abcde" -> "abcdef"
Each step creates a new string object, resulting in a total of 6 string objects.

---
## Substring

A substring is a contiguous sequence of characters within a string. A substring concept in string is similar to subarray concept in array.

**A substring can be:**
1. Continous part of string.
2. Full string can be a substring.
3. A single character can also be a subsring.

### Example

Suppose, we have a string as
```
"abc"
```
There are total 6 substring can be formed from the above string. All substrings are
```
"a"
"b"
"c"
"ab"
"bc"
"abc"
```

---
### Question
How many total substrings will be there for the String "bxcd" ?

### Choices
- [ ] 7
- [ ] 8
- [x] 10
- [ ] 9

### Explanation
All the substrings are as follows-
```
"b", "x", "c", "d", "bx", "xc", "cd", "bxc", "xcd", "bxcd"
```
We can also find the count using n*(n+1)/2

---

## Problem 2 Check Palindrome

Check whether the given substring of string **s** is palindrome or not.
A palindrome is the sequence of characters that reads the same forward and backward.for example, "nayan", "madam", etc.

### TestCase

#### Input
```
s = "anamadamspe"
start = 3
end = 7
```
#### Output
```
true
```
#### Explanation
The substring formed from index 3 to 7 is "madam" which is palindrome.

## Approach
Below is the simple algorithm to check whether the substring is palindrome or not:
* Initialize two indices *start* and *end* to point to the beginning and *end* of the string, respectively.
* While *start* is less than *end*, do the following:
    * If the character at index *start* is not equal to the character at index *end*, the string is not a palindrome. Return false.
    * Else, increment *start* and decrement *end*.
* If the loop completes without finding a non-matching pair, the string is a palindrome. Return true.

### Pseudocode
```javascript
function ispalindrome(character array s[], start, end){
    while(start<end){
        if(s[start]!=s[end]){
            return false;
        }
        else {
            start++;
            end--;
        }
    }
    return true;
}
```


### Complexity

Time Complexity- **O(N)**.
Space Complexity- **O(1)**.


---
## Problem 3 longest palindromic substring

### Problem Statement

Given a string **s**, calculate the length of longest palindromic substring in **s**.

### TestCase
#### Input
```
"anamadamm"
```
#### Output
```
5
```
#### Explanation
The substring "madam" of size 5 is the longest palindromic substring that can be formed from given string.



### Question
What is the length of longest palindromic substring within string "feacabacabgf" ?

### Choices
- [ ] 6
- [ ] 3
- [x] 7
- [ ] 10


---
### Question
What is the length of longest palindromic substring within string "a d a e b c d f d c b e t g g t e" ?

### Choices
- [ ] 6
- [ ] 3
- [x] 9
- [ ] 10

---

## Brute Force Approach

The naive approach is to for all the substring check whether the string is palindrome or not. if it is palindrome and its size is greater than the previous answer(which is initially 0), then update the answer.

### Pseudocode

```javascript
function longestPalindrome(character array s[]){
    N = s.size();
    ans = 0;
    for(i -> 0 to N - 1){
        for(j -> i to N - 1){
            if(ispalindrome(s,i,j)){
                ans = max(ans, j-i+1);
            }
        }
    }
    return ans;
}
```

### Complexity

Time Complexity- **O(N^3)**.
Space Complexity- **O(1)**.

## Optimized Approach

### Idea
The key idea here is that:
* For odd length substring, take every character as a center and expand its center and gets maximum size palindromic substring.
* For even length substring, take every adjacent character as a center and expand its center and get maximum size palindromic substring.


### Pseudocode
```javascript
function longestpalindrome(character array s[]){
    maxlength=0;
    N = s.size();
    for(c -> 0 to N - 1){
    
        //odd length string
        left = right = c;
        
        while(left>=0 and right<N){
            if(s[left]!=s[right]){
                break;
            }
            left--;
            right++;
        }
        maxlength=max(maxlength,right-left-1);
        
        //even length string
        left=c;
        right=c+1;
        while(left>=0 and right<N){
            if(s[left]!=s[right]){
                break;
            }
            left--;
            right++;
        }
        maxlength=max(maxlength,right-left-1);
    }
    return maxlength;
}
```

### Complexity

Time Complexity- **O(N^2)**.
Space Complexity- **O(1)**.

---

## Immutability of Strings

**Article that students should go through** -
> Suggesting Instructor to also go through this link once.
https://www.scaler.com/topics/why-string-is-immutable-in-java/

In languages like **Java, C#, JavaScript, Python and Go**, strings are immutable, which means that once a String object is created, its value cannot be changed. If you try to modify it, such as through concatenation or other operations, a new String object is created with the modified value, and the original String remains unchanged.

```cpp=
String s1 = "Hello";     // String literal
String s2 = "Hello";     // String literal
String s3 = s1;     // same reference
```

![](https://hackmd.io/_uploads/SkGyXywRh.png)

* As seen above, because strings with the same content share storage in a single pool, this minimize creating a copy of the same value. 
* That is to say, once a String is generated, its content cannot be changed and hence changing content will lead to the creation of a new String.

```cpp=
//Changing the value of s1
s1 = "Java";

//Updating with concat() operation
s2.concat(" World");

//The concatenated String will be created as a new instance 
//and an object should refer to that instance to get the concatenated value.
String newS3 = s3.concat(" Scaler");

System.out.println("s1 refers to " + s1);
System.out.println("s2 refers to " + s2);
System.out.println("s3 refers to " + s3);
System.out.println("newS3 refers to " + newS3);
```

### Output

```cpp=
s1 refers to Java
s2 refers to Hello
s3 refers to Hello
news3 refers to Hello Scaler
```

![](https://hackmd.io/_uploads/BkzzEkPC3.png)

As shown above, considering the example:

* String s1 is updated with a new value and that's why a new instance is created. Hence, s1 reference changes to that newly created instance "Java".
* String s2 and s3 remain unchanged as their references were not changed to a new instance created after performing concat() operation.
* "Hello World" remains unreferenced to any object and lost in the pool as s2.concat() operation (in line number 5) is not assigned to any object. That's why there is a reference to its result.
* String newS3 refers to the instance of s3.concat() operation that is "Hello Scaler" as it is referenced to new object newS3.

**Hence, Strings are immutable and whenever we change the string only its reference is changed to the new instance.**

### Why is String Immutability needed ?

1. **Security:** Strings are often used to store sensitive data like passwords, file paths, and network connections. If strings were mutable, they could be altered when being passed between methods, which would lead to security vulnerabilities.

2. **Caching and Performance:** The JVM can safely cache String literals because their values don't change. This allows for efficient memory usage and better performance since multiple references can point to the same String literal in the string pool.


### String Builder in Java

In Java, for operations where many characters need to be appended to a string, it is more efficient to use a StringBuilder or StringBuffer.. These classes are designed for such use cases because they maintain a mutable sequence of characters, and they can expand their capacity without needing to copy the contents every time a new character is added.

With StringBuilder, adding a character is typically O(1) on average, making it much more efficient for concatenating strings or characters repeatedly. After all modifications, the StringBuilder can be converted back to a String using its .toString() method.

Here’s a quick example of using StringBuilder for adding characters:
```javascript
StringBuilder sb = new StringBuilder();
for (int i = 0; i < n; i++) {
    sb.append('a');  // Adds a character efficiently
}
String result = sb.toString();  // Converts StringBuilder to String
```

Using StringBuilder is the recommended approach when constructing strings dynamically in Java, especially in loops or where multiple concatenations are involved.

Please share with students for more methods for string builder - https://docs.google.com/document/d/1umCzDQqPUUD21XneFwYniwAMRp2r_Rf4iWaRNRS1h6s/edit


---

## Problem 4 Reverse String Word By Word

### Problem Statement
Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in "s" are separated by at least one space.

Return a string of the words in reverse order, concatenated by a single space. The returned string should only have a single space separating the words, even if there were multiple spaces in the input string. Leading or trailing spaces should be removed.

### Examples
**Example 1:**
Input:
s = "Scaler is the best"
Output:
"best the is Scaler"

Explanation:
The input string "Scaler is the best" contains four words: "Scaler", "is", "the", and "best". When reversed, the words become "best", "the", "is", and "Scaler". These are concatenated with a single space.

**Example 2:**
Input:
s = " hello world "
Output:
"world hello"

Explanation:
The input string " hello world " contains two words: "hello" and "world". Leading and trailing spaces are removed, and the words are reversed and concatenated with a single space.

### Approach 1:

<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/095/596/original/Screenshot_2024-11-05_at_3.22.49_PM.png?1730800414" width=600 />

### Code
JAVA
```cpp 
class Solution {
    public String reverseWords(String s) {
         A = A.trim();
        String[] words = A.split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            sb.append(words[i]);
            if (i > 0) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}
```

PYTHON
```py
class Solution:
    def solve(self,A):
        A = A.strip()
        A = A.split()
        A = A[::-1]
        return ' '.join(A)
```

C++
```cpp
string reverseWords(string s) {
    // Step 1: Split the string into words
    vector<string> words;
    string word = "";
    for (char c : s) {
        if (c != ' ') {
            word += c;  // Build the current word
        } else if (c == ' ' && word != "") {
            words.push_back(word);  // Add the word to the list
            word = "";  // Reset the word
        }
    }
    if (word != "") {
        words.push_back(word);  // Add the last word if any
    }

    // Step 2: Reverse the list of words
    reverse(words.begin(), words.end());

    // Step 3: Join the reversed words with a single space
    string result = "";
    for (int i = 0; i < words.size(); i++) {
        result += words[i];
        if (i < words.size() - 1) {
            result += " ";  // Add space between words, not after the last word
        }
    }

    return result;
}
```

### Approach


Suppose we want to reverse words in the string "I like Scaler", this can be done by first reversing each word individually and then reversing the whole word.

Step 1:
"I like Scaler" -> "I ekil relacS"

Step 2:
"I ekil relacS" -> "Scaler like I"

Note that for this to work, we first need to preprocess the string so that it does not contain any leading, trailing or extra in between spaces.

### Code

C++

```cpp
class Solution {
  public:
  string reverseWords(string s) {
    // reverse the whole string
    reverse(s.begin(), s.end());

    int n = s.size();
    int idx = 0;
    for (int start = 0; start < n; ++start) {
      if (s[start] != ' ') {
        // go to the beginning of the word
        if (idx != 0) s[idx++] = ' ';

        // go to the end of the word
        int end = start;
        while (end < n && s[end] != ' ') s[idx++] = s[end++];

        // reverse the word
        reverse(s.begin() + idx - (end - start), s.begin() + idx);

        // move to the next word
        start = end;
      }
    }
    s.erase(s.begin() + idx, s.end());
    return s;
  }
};
```

JAVA
```java
class Solution {
    public StringBuilder trimSpaces(String s) {
        int left = 0, right = s.length() - 1;
        // remove leading spaces
        while (left <= right && s.charAt(left) == ' ') ++left;

        // remove trailing spaces
        while (left <= right && s.charAt(right) == ' ') --right;

        // reduce multiple spaces to single one
        StringBuilder sb = new StringBuilder();
        while (left <= right) {
            char c = s.charAt(left);

            if (c != ' ') sb.append(c);
            else if (sb.charAt(sb.length() - 1) != ' ') sb.append(c);

            ++left;
        }
        return sb;
    }

    public void reverse(StringBuilder sb, int left, int right) {
        while (left < right) {
            char tmp = sb.charAt(left);
            sb.setCharAt(left++, sb.charAt(right));
            sb.setCharAt(right--, tmp);
        }
    }

    public void reverseEachWord(StringBuilder sb) {
        int n = sb.length();
        int start = 0, end = 0;

        while (start < n) {
            // go to the end of the word
            while (end < n && sb.charAt(end) != ' ') ++end;
            // reverse the word
            reverse(sb, start, end - 1);
            // move to the next word
            start = end + 1;
            ++end;
        }
    }

    public String reverseWords(String s) {
        // converst string to string builder
        // and trim spaces at the same time
        StringBuilder sb = trimSpaces(s);

        // reverse the whole string
        reverse(sb, 0, sb.length() - 1);

        // reverse each word
        reverseEachWord(sb);

        return sb.toString();
    }
}
```

PYTHON
```python
class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != " ":
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # converst string to char array
        # and trim spaces at the same time
        l = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # reverse each word
        self.reverse_each_word(l)

        return "".join(l)
```
