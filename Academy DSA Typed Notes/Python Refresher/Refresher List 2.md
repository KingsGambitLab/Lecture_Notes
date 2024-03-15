# Refresher: List 2

## Builtin Functions

### Index

- Given a value and a list, find the element and print "Found" else "Not found"

**Code**:

```python
# Solution 1
li = list(map(int, input().split(' ')))
value = int(input())
for index in range(len(li)):
    if li[index] == value:
        print('Found at', index)
        break
else:
    print('Not found')
```

**Output**:

```plaintext
1 2 3 4 5 6
3
Found at 2
```

- Displaying index

**Code**:

```python
# Solution 2
li = list(map(int, input().split(' ')))
value = int(input())
if value in li:
    print('Found at', li.index(value))
else:
    print('Not found')
```

**Output**:

```plaintext
1 2 3 4 5 6
3
Found at 2
```

**Explaination**:

- Solution 1 uses a for loop to iterate through the list and check if each element is equal to the given value. If found, it prints the index and breaks out of the loop. If not found, it prints "Not found."
- Solution 2 uses the `in` operator to check if the value is present in the list. If found, it prints the index using the `index()` function. If not found, it prints "Not found."

### max

-  Given a list, you have to find the maximum element in this list.

**Code**:

```python
li = [-13, -53, -23, -21, -55]
max_value = li[0]
for item in li:
    if max_value < item:
        max_value = item
print(max_value)
```

**Output**:

```plaintext
-13
```

**Code**:

```python
li = [-13, -53, -23, -21, -55]
max_value = None
for item in li:
    if max_value is None or max_value < item:
        max_value = item
print(max_value)
```

**Output**:

```plaintext
-13
```

**Explaination**:

- The first solution initializes `max_value` with the first element of the list and iterates through the list, updating `max_value` if a larger element is found.
- The second solution initializes `max_value` to `None` and iterates through the list, updating `max_value` if a larger element is found. The `is None` check is used to handle an empty list case.

### Printing max Value

**Code**:

```python
li = [-13, -53, -23, -21, -55]
print(max(li))

print(max(1, 2, 3, 4, 5, 3, 4, 5, 1))
```

**Output**:

```plaintext
-13
5
```

**Explaination**:

- The `max()` function is used to directly find the maximum value in the list or a set of values.

### Printing min Value


**Code**:

```python
li = [-13, -53, -23, -21, -55]
print(min(li))

print(min(1, 2, 3, 4, 5, 3, 4, 5, 1))
```

**Output**:

```plaintext
-55
1
```

**Explaination**:

- The `min()` function is used to directly find the minimum value in the list or a set of values.

### Slicing

In this section, we will learn how to slice the list `[49, 6, 71]` from the given list 

**Code**:

```python
li = [2, 23, 49, 6, 71, 55]

def sub_list(li, startIndex, endIndex):
    new_li = []
    for i in range(startIndex, endIndex + 1):
        new_li.append(li[i])
    return new_li

print(sub_list(li, 2, 4))
```

**Output**:

```plaintext
[49, 6, 71]
```

**Explaination**:

- The `sub_list` function takes a list and two indices as input and returns a new list containing elements from the start index to the end index.

### More slicing examples


#### li[:end]
**Code**:
```python
a = list(range(10))
print(a)
print(a[::-2])
```
**Output**:
```plaintext
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 7, 5, 3, 1]
```
**Explanation**:
- `a[::-2]` creates a new list by slicing `a` with a step of -2, starting from the end.
- It includes every second element in reverse order, resulting in `[9, 7, 5, 3, 1]`.

#### li[start:end]
**Code**:
```python
a = [5, 2, 3, 9, 8]
print(a[1:5])
```
**Output**:
```plaintext
[2, 3, 9, 8]
```
**Explanation**:
- The slice `a[1:5]` extracts elements starting from index 1 up to (but not including) index 5 from list `a`.

#### li[start:]
**Code**:
```python
a = [5, 2, 3, 9, 8]
print(a[2:])
```
**Output**:
```python!
[3, 9, 8]
```
**Explanation**:
- The slice `a[2:]` extracts elements starting from index 2 till the end of the list `a`.

#### li[start\:end:range]
**Code**:
```python
a = [5, 2, 3, 9, 8]
print(a[1:4:2])
```
**Output**:
```python
[2, 9]
```
**Explanation**:
- The slice `a[1:4:2]` extracts elements starting from index 1 up to (but not including) index 4 with a step of 2.
- It includes every second element in the specified range, resulting in `[2, 9]`.


---
## Problem Solving

### Question

Right shift the given array:

**li = [2,3,4,5,6]
n = [0,n - 1]
Output = [3,4,5,6,2]**

:::warning
Please take some time to think about the solution approach on your own before reading further.....
:::

### Solution 1

**Code**:

```python
li = [2,3,4,5,6]
n = int(input())
for i in range(n):
    a = li.pop(0)
    li.append(a)
print(li)
```

**Output**:

```python
3
[5, 6, 2, 3, 4]
```

## Solution 2

**Code**:

```python
li = [2,3,4,5,6]
n = int(input())
print(li[n:] + li[:n])
```

**Output**:

```python
3
[5, 6, 2, 3, 4]
```
