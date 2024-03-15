# Refresher: Strings 2

### Question

What is the output of the following?
```python
a = "Age:"
print(a + 23)
```

**Choices**

- [ ] Age:23
- [ ] Age:
- [x] Error
- [ ] Age: 23

In the given code, there is an attempt to concatenate a string ("Age:") with an integer (23). This operation is not allowed in Python without explicit conversion and hence will output an error.

---
### Question

What is the output of the following?
```python
a = "Hello"
b = a * 3
print(len(b) == (len(a) * 3))
```

**Choices**

- [x] True
- [ ] False
- [ ] Error

The output is True, because the length of the string `b` is compared to the result of multiplying the length of `a` by 3, and they are equal.

---
### Question

What is the output of the following?
```python
s = 'Name : {}, Age : {}'
print(s.format(25, 'John'))
```

**Choices**

- [ ] Name : John, Age : 25
- [x] Name : 25, Age : John
- [ ] Error


The `format` method replaces the `{}` placeholders in the string with the provided values in the order they appear. In this case, `25` is placed where the first `{}` is, and `'John'` is placed where the second `{}` is, resulting in the output "Name : 25, Age : John".

---
### Question

What is the output of the following?
```python
s = 'Name : {name}, Gender : {}, Age : {age}'
print(s.format('Male', age = 25, name = 'John'))
```

**Choices**

- [x] Name : John, Gender : Male, Age : 25
- [ ] Name : Male, Gender : John, Age : 25
- [ ] Error


The `format` method is used to substitute values into the placeholders `{}`, `{name}`, and `{age}` in the string `s`. The values provided in the `format` method are 'Male' for the first placeholder, 'John' for the `{name}` placeholder, and 25 for the `{age}` placeholder. The resulting string is "Name : John, Gender : Male, Age : 25".



---
## Count Uppercase Letters

## Count Number of Uppercase Letters

### Problem

Given a string, the task is to count the number of uppercase letters in the string.

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


### Solution

The solution involves iterating through each character in the string and checking if its ASCII value falls within the range of uppercase letters (A-Z) using the `if` case. Specifically, it ensures that the character is greater than or equal to the ASCII value of 'A' and less than or equal to the ASCII value of 'Z'. For each uppercase letter found, a counter is incremented.

```python
def count_upper(a):
    count = 0
    for char in a:
        if ord('A') <= ord(char) <= ord('Z'):
            count += 1
    return count

# Example Usage
result = count_upper("ThisIsAString")
print(result)
```

### Output
```plaintext
4
```

### Explanation

In this example, the function `count_upper` takes the input string "ThisIsAString" and iterates through each character. For each character that is an uppercase letter, the counter is incremented. The final count is returned, indicating that there are 4 uppercase letters in the input string.




---
## More Functions in Strings

## More Functions

### join()

### Explanation
The `join()` method concatenates elements of an iterable using a specified separator.

### Example
```python
# Example
separator = '.'
result = separator.join(['Hi', 'there'])
print(result)  # Output: 'Hi.there'

# Example 2
result = '.'.join(['2', '31'])
print(result)  # Output: '2.31'

result = '.'.join([2, 3])
print(result)  # Error

```

#### Explanation
In this example, the elements 'Hi' and 'there' are joined with a dot (`.`) as the separator, resulting in the string 'Hi.there'.

### upper()

### Explanation
The `upper()` method converts all characters in a string to uppercase.

### Example
```python
# Example
a = 'ThisIsAString'
result = a.upper()
print(result)  # Output: 'THISISASTRING'

# Example 2
a = 'ThisIsAString12348$#'
result = a.upper()
print(result)  # Output: 'THISISASTRING12348S#'

```

### Explanation
The `upper()` function transforms all characters in the string 'ThisIsAString' to uppercase, resulting in 'THISISASTRING'.

### lower()

### Explanation
The `lower()` method converts all characters in a string to lowercase.

### Example
```python
# Example
a = 'ThisIsAString'
result = a.lower()
print(result)  # Output: 'thisisastring'

# Example 2
a = 'ThisIsAString12348$#'
result = a.lower()
print(result)  # Output: 'thisisastring12348$#'

```

### Explanation
The `lower()` function transforms all characters in the string 'ThisIsAString' to lowercase, resulting in 'thisisastring'.

### isupper()

### Explanation
The `isupper()` method checks if all characters in a string are uppercase.

### Example
```python
# Example
a = 'AbC1234sg'
result = a.isupper()
print(result)  # Output: False

# Example 2
a = 'ABC1234SG'
result = a.isupper()
print(result)  # Output: True
```

### Explanation
The `isupper()` function returns `False` because not all characters in the string 'AbC1234sg' are uppercase. Numbers and special characters are ignored.

### islower()

### Explanation
The `islower()` method checks if all characters in a string are lowercase, ignoring numbers and special characters.

### Example
```python
# Example 1
a = 'abc1234$#'
result = a.islower()
print(result)  # Output: True

# Example 2
a = 'ABC1234$#'
result = a.islower()
print(result)  # Output: False
```

### Explanation
The `islower()` function returns `True` because all characters in the string 'abc1234$#' are lowercase.

### isalpha()

### Explanation
The `isalpha()` method checks if all characters in a string are alphabetic.

### Example
```python
# Example
a = 'Scaler Academy'
result = a.isalpha()
print(result)  # Output: False

# Example
a = 'Scal3rAcademY'
result = a.isalpha()
print(result)  # Output: False
```

### Explanation
The `isalpha()` function returns `False` because the string 'Scaler Academy' contains spaces and is not purely alphabetic. The next example has a number in between and hence is not alphabetic.

### isdigit()

### Explanation
The `isdigit()` method checks if all characters in a string are digits.

### Example
```python
# Example
a = '123'
result = a.isdigit()
print(result)  # Output: True

# Example
a = '1a2b3'
result = a.isdigit()
print(result)  # Output: False
```

### Explanation
The `isdigit()` function returns `True` because all characters in the string '123' are digits. The next example returns `False` because of the alphabetic characters in the string.

### isalnum()

### Explanation
The `isalnum()` method checks if all characters in a string are alphanumeric.

### Example
```python
# Example
a = 'Abc1234'
result = a.isalnum()
print(result)  # Output: True

# Example 2
a = 'Abc12348S#'
result = a.isalnum()
print(result)  # Output: False
```

### Explanation
The `isalnum()` function returns `True` because all characters in the string 'Abc1234' are alphanumeric. The second example has special character, `#` and hence returns `False`.

### endswith()

### Explanation
The `endswith()` method checks if a string ends with a specified suffix.

### Example
```python
# Example
a = 'Scaler Academy'
result = a.endswith('Academy')
print(result)  # Output: True

# Example 2
a = 'Python Programming'
result = a.endswith('Academy')
print(result)  # Output: False
```

### Explanation
The `endswith()` function returns `True` because the string 'Scaler Academy' ends with the specified suffix 'Academy'.

```python
# Program to Count Alphabets and Digits in a String

# User input
s = input()

# Initialize counters
alpha_count = 0
digit_count = 0

# Iterate through each character in the input string
for char in s:
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        digit_count += 1

# Print the result
print(f'Alphabet count is {alpha_count} and digit count is {digit_count}')
```

### Explanation

- The program takes user input as a string `s`.
- Two counters (`alpha_count` and `digit_count`) are initialized to keep track of the number of alphabets and digits.
- The program iterates through each character in the input string using a `for` loop.
- For each character, it checks if it is an alphabet using `char.isalpha()` and increments the `alpha_count` accordingly.
- Similarly, if the character is a digit (`char.isdigit()`), the `digit_count` is incremented.
- Finally, the program prints the counts using an f-string.

### Example

**Input:**
```python
Hello123World
```

**Output:**
```plaintext
Alphabet count is 10 and digit count is 3
```

In the input string "Hello123World," there are 10 alphabets (H, e, l, l, o, W, o, r, l, d) and 3 digits (1, 2, 3).



---
### Question

What is the output of the following?
```python
a = [1, 2, 3, 4, 5]
print('|'.join(a))
```

**Choices**

- [ ] 1|2|3|4|5
- [x] Error
- [ ] |1|2|3|4|5|

The `join` method in Python is used to concatenate a list of strings with a specified delimiter. However, in the given code, the list `a` contains integers, not strings. The `join` method expects a list of strings, so attempting to join a list of integers will result in a TypeError.

---
### Question

What is the output of the following?
```python
a = 'Scaler123'
print(a.upper())
```

**Choices**

- [ ] Error
- [ ] Scaler123
- [ ] sCALER123
- [x] SCALER123

The `upper()` method in Python is used to convert all characters in a string to uppercase. In this case, the string 'Scaler123' is assigned to variable `a`, and `a.upper()` is then called, resulting in 'SCALER123' as the output.

---
### Question

What is the output of the following?
```python
a = 'scaler123'
print(a.islower())
```

**Choices**

- [x] True
- [ ] False


The output of the given Python code is `True`. The `islower()` method checks if all the characters in the string are lowercase, and in this case, all characters in the string 'scaler123' are lowercase.

---
### Question

What is the output of the following?
```python
a = 'scaler123'
print(a.isalpha())
```

**Choices**

- [ ] True
- [x] False


The output of the given Python code is `False`. This is because the `isalpha()` method checks if all the characters in the string are alphabetic (letters) and does not allow for numbers or other characters. In the given string 'scaler123', the presence of '123' makes the method return `False`.

---
### Question

What is the output of the following?
```python
a = 'scaler123'
print(a.endswith('ler'))
```

**Choices**

- [ ] True
- [x] False


The output of the given Python code is `False`. This is because the string assigned to variable `a` ('scaler123') does not end with the substring 'ler'. Therefore, the `endswith()` method returns `False`.

---
## List and String Comparison

### List Comparison

List comparison in Python involves comparing two lists element-wise. The comparison starts from the first elements of both lists, and the result is determined based on the comparison of corresponding elements.

### Example 1

```python
[1, 2, 3, 4, 5] < [1, 3]
# Output: True
```

### Explanation
In this example, the comparison evaluates to `True` because the first list is considered "less than" the second list. The comparison is element-wise, and it stops as soon as a pair of elements is found where the first element is less than the second element.

### Example 2

```python
[1, 3, 0] > [1, 3]
# Output: True
```

### Explanation
Here, the comparison evaluates to `True` because the first list is considered "greater than" the second list. Again, the comparison is element-wise, and it stops as soon as a pair of elements is found where the first element is greater than the second element.

### Example 3

```python
[1, 3] == [1, 3]
# Output: True
```

### Explanation
The comparison `[1, 3] == [1, 3]` checks if both lists are equal element-wise. In this case, the result is `True` because every corresponding pair of elements is the same.

### Example 4

```python
[1, 2, 3] > [1, 1000, 2000, 3000]
# Output: True
```

### Explanation
The comparison `[1, 2, 3] > [1, 1000, 2000, 3000]` evaluates to `True` because the first list is considered "greater than" the second list. The comparison is still element-wise, and it stops as soon as a pair of elements is found where the first element is greater than the second element.


### String Comparison

String comparison in Python involves comparing two strings lexicographically, character by character. The comparison is case-sensitive, with uppercase letters considered "less than" their lowercase counterparts. The comparison stops as soon as a pair of characters is found where the condition (e.g., less than, greater than, equal to) is satisfied. The overall result of the string comparison reflects the outcome of these character-wise comparisons.

### Example 1

```python
'A' > 'a'
# Output: False
```

### Explanation
In this example, the comparison `'A' > 'a'` evaluates to `False` because, in the ASCII table, uppercase 'A' has a lower ASCII value than lowercase 'a'.

### Example 2

```python
'Aakar' > 'Sudip'
# Output: False
```

### Explanation
Here, the comparison `'Aakar' > 'Sudip'` evaluates to `False` because, in the lexicographic order, the substring 'Aakar' is considered "less than" the substring 'Sudip'. The comparison stops at the first differing character.




---
## List Comprehension

List comprehension is a concise way to create lists in Python. It offers a more readable and efficient alternative to traditional loops. The syntax involves expressing the creation of a list in a single line.

### Example 1

```python
# Create a list of squares till n-1
n = 5
li = [i ** 2 for i in range(1, n)]
print(li) # Output: [1, 4, 9, 16]
```

This example uses list comprehension to create a list of squares for values from 1 to n-1.

### Example 2

```python
# Create a list of squares for values from 1 to n
n = 5
li = [i ** 2 for i in range(1, n + 1)]
print(li) # Output: [1, 4, 9, 16, 25]
```


Here, the list comprehension creates a list of squares for values from 1 to n.

### Example 3

```python
# Create a list of all even elements
n = 5
li = [i for i in range(1, n * 2) if i % 2 == 0]
print(li) # Output:  [2, 4, 6, 8, 10]
```

This example creates a list of all even elements from 1 to n*2 using list comprehension. 

### Example 4

```python
# Create a list of tuples (i, j) for values of i and j in the given range
n = 3
li = [(i, j) for i in range(n) for j in range(i)]
print(li) # Output: [(1, 0), (2, 0), (2, 1)]
```

This example creates a list of tuples (i, j) using nested list comprehension. It includes pairs where j is less than i. 


---
## Pattern Printing

### Pattern 1: Increasing Rows of Stars


Print the following pattern ?

```python
*
* *
* * *
* * * *
```

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


### Code

```python
n = int(input())
for i in range(1, n + 1):
    print('*' * i)
```

This code takes an input `n` and uses a loop to print rows of stars. The number of stars in each row increases from 1 to `n`.

### Pattern 2: Right-aligned Triangle

Print the following pattern ?


```python
   *
  * *
 * * *
* * * *
```

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::


To print the given pattern, you can use two nested loops. The outer loop controls the rows, and the inner loop controls the columns. For each row, you need to print spaces followed by asterisks in a specific pattern. Consider the number of spaces needed before each asterisk to achieve the desired right-aligned triangular pattern.


### Code

```python
n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)
```

This code prints a right-aligned triangle of stars. The number of spaces before the stars decreases, and the number of stars in each row increases.

### Pattern 3: Diamond Pattern

Print the following diamond pattern ?
```python
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::



To print the given diamond pattern, you can follow these steps:

1. Observe the pattern carefully, especially how the number of spaces and stars change in each row.
2. Divide the pattern into two parts: the upper half and the lower half.
3. For the upper half, start with fewer spaces and more stars, incrementing the number of stars in each row.
4. For the lower half, start with fewer spaces and more stars, decrementing the number of stars in each row.

### Code

```python
n = int(input())
m = n // 2

for i in range(1, m + 1):
    print(' ' * (m - i) + '*' * (2 * i - 1), sep = '')

for i in range(m, 0, -1):
    print(' ' * (m - i) + '*' * (2 * i - 1), sep = '')
```

This code prints a diamond pattern. The first loop prints the upper half, and the second loop prints the lower half of the diamond.
