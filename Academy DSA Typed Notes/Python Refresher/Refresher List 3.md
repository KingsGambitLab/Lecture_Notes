# Refresher: List 3

## Nested List

### Introduction

- A nested list in Python is a list that can contain other lists as elements.
- It allows you to create a two-dimensional structure, also known as a 2D list, where each element in the outer list can be a list itself.

**Code**:

```python
maths = [1, 1, 1]
science = [2, 2, 2]
history = [3, 3, 3]
subjects = [maths, science, history]
print(subjects)
```

**Output**:

```python
[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```

**Explanation of code**:

- Three separate lists, `maths`, `science`, and `history`, are created.
- These lists are then combined into a single list named `subjects`.
- The `print(subjects)` statement displays the resulting nested list.

---
## Indexing in a 2D List

- Indexing in a 2D list involves accessing elements using two indices: one for the outer list (row) and another for the inner list (column).

**Code**:

```python
print(subjects[0][2])

# row major form
print(subjects)
```

**Output**:

```python
1
[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```

**Explanation of code**:

- The expression `subjects[0][2]` accesses the element in the first row (index 0) and the third column (index 2) of the 2D list.
- The second `print(subjects)` statement displays the entire 2D list.

---
## Iterating a 2D List

### Example 1

**Code**:

```python
for row_index in range(len(subjects)):
    for col_index in range(len(subjects[row_index])):
        print(subjects[row_index][col_index], end = ' ')
```

**Output**:

```python
1 1 1 2 2 2 3 3 3 
```

**Explanation of code**:

- Nested loops iterate through each element of the 2D list, printing them horizontally.

### Example 2

**Code**:

```python
for row_index in range(len(subjects)):
    for col_index in range(len(subjects[row_index])):
        print(subjects[row_index][col_index], end=' ')
    print()
```

**Output**:

```python
1 1 1 
2 2 2 
3 3 3 
```

**Explanation of code**:

- Similar to Example 1, but with an additional `print()` to create a new line after each row.

### Example 3

**Code**:

```python
for col_index in range(len(subjects[0])):
    for row_index in range(len(subjects)):
        print(subjects[row_index][col_index], end = ' ')
    print()
```

**Output**:

```python
1 2 3 
1 2 3 
1 2 3 
```

**Explanation of code**:

- This example transposes the 2D list by iterating through columns first and then rows.

---

### Input in a 2D List

### Example 

**Code**:

```python
def take_list_as_input():
    li = list(map(int, input().split()))
    return li

a = []
for i in range(3):
    a.append(take_list_as_input())
print(a)
```

**Output**:

```python
12 13 14
45 46 47
34 35 36
[[12, 13, 14], [45, 46, 47], [34, 35, 36]]
```

**Explanation of code**:

- The `take_list_as_input()` function reads a line of space-separated integers and converts them into a list.
- The loop collects three such lists to create a 2D list named `a`.

### Row Wise Sum

**Code**:

```python
def take_list_as_input():
    li = list(map(int, input().split()))
    return li

a = []
for i in range(3):
    a.append(take_list_as_input())
print(a)

for row_index in range(len(a)):
    row_sum = sum(a[row_index])
    print(row_sum)
```

**Output**:

```python
1 1 1
2 2 2
3 3 3
[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
3
6
9
```

**Explanation of code**:

- Calculates and prints the sum of each row in the 2D list.


---
## Matrix Addition

**Code**:

```python
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = []

for row_index in range(len(a)):
    temp = []
    for col_index in range(len(a[row_index])):
        temp.append(a[row_index][col_index] + b[row_index][col_index])
    c.append(temp)
print(c)
```

**Output**:

```python
[[2, 4, 6], [8, 10, 12], [14, 16, 18]]
```

**Explanation of code**:

- Performs matrix addition on two 2D lists (`a` and `b`) and stores the result in the list `c`.