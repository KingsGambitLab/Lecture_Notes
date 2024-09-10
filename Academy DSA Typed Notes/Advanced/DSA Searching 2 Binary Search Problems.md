# Searching 2: Binary Search Problems

## Another formula for finding mid

Sometimes when people try to find the middle point of something (like an array), they use a simple formula: 
**`$mid = (low+high) / 2$`**
However, this can sometimes cause problems, especially if the numbers are very big. Let me explain with an example:
 
Imagine we can only handle numbers up to 100, and we have a list of 100 items. The last position in this list is 99. If we want to find something near the end, say between position 98 and 99, adding these numbers together gives us 197. This is a problem because 197 is bigger than 100 and our system can't handle it, which might cause errors or give us a negative number when we try to find the middle.

To avoid this problem, we can use a different way to find the middle: 
**`$mid = low + ( (high-low) / 2 )$`**
Using our example, this would be, **`$98 + ( (99-98)/2 ) = 98.5$`**, which rounds down safely to 98. This method makes sure we don't go over our limit and keeps everything working smoothly.




<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/051/918/original/upload_8464c14ddc9d5166e7118e05dcbfdc72.png?1696271394" width="500"/>


---
## Problem 1 Searching in Rotated Sorted Arrays

### Scenario:
Imagine you have an array that was sorted initially, but someone rotated it at an unknown index. The resulting array is a rotated sorted array. The challenge is to find a specific element in this rotated array without reverting to linear search.

**Suppose we have the following rotated sorted array:**
```javascript
Original Sorted Rotated Array: [4, 5, 6, 7, 8, 9, 1, 2, 3]
```
Let's say we want to find the element 7 within this rotated array using a brute-force approach (Linear Search).

### Brute-Force Approach:

* Iterate and get the element. T.C: O(N)


### Optimised Approach
 **`A rotated sorted array can be visualized as being split into two parts: part 1 and part 2.`**
  > Crucially, both part 1 and part 2 are sorted individually, but every element in part 1 is greater than those in part 2 due to the rotation.
<img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/290/original/upload_7109177bd564db28fb52884947596f19.jpeg?1697636298" width=600 />



**`How to identify in which part mid point is present?`**
  
> To determine which part the midpoint belongs to (part 1 or 2), compare it with the 0th element.
> -- If arr[mid] >= arr[0], then it belongs to part 1. Otherwise, it's in part 2.

**`How to identify where is the target ?`**
> If the midpoint is the equals to the target, you've found it.
   #### If not, then check if the target lies in the same part as the midpoint. 
   * If yes, both target and midpoint is within the same sorted part, perform a binary search in that part to move your midpoint towards the target.
 <img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/292/original/upload_e222ee12696646bb515fe8b21149991b.png?1697636367" width=600 />
  * If no, move your search towards the other part, effectively approaching the midpoint towards target.
 <img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/293/original/upload_8ab6fabad4f92c55665e78291b1befb5.png?1697636388" width=600 />

* **Result:**
  * Return the index of the target if found, or -1 if not.

### Example: 

**Scenario:**
Consider the rotated sorted array **[4, 5, 6, 7, 0, 1, 2]** and our target is 0.

**Solution:**
* Using the provided algorithm:
* Initialize left to 0 and right to 6.
* Calculate mid as (left + right) // 2, which is 3.
* Check if nums[mid] (element at index 3) is equal to the target (0). It's not equal.
* Check if target (0) is less than nums[0] (4). It's not.
* Check if nums[mid] (7) is greater than or equal to nums[0] (4). It's true.
* Update left to mid + 1, making left equal to 4.
* Calculate mid as (left + right) // 2, which is 5.
* Check if nums[mid] (element at index 5) is equal to the target (0). It is equal.
* Return mid, which is 5.

 **We found the target 0 at index 5.**

---
### Searching in Rotated Sorted Arrays 


### Pseudocode:

```cpp
function searchRotatedArray(nums, target):
    left = 0
    right = length(nums) - 1

    while left <= right:
        mid = left + (right - left) / 2

        if nums[mid] == target:
            return mid
        
        if target < nums[0]:
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

    return -1
```

### Complexity Analysis:
The time complexity of this modified Binary Search algorithm is still O(log n), making it efficient even in rotated sorted arrays.
**Reason**:
* **Divide and Conquer:**<br> The algorithm works by repeatedly dividing the search space in half. In each step, it either eliminates half of the remaining elements or finds the target element. This is a characteristic of binary search, which has a time complexity of O(log N).
* **Comparison Operations:**<br> The main operations within each iteration are comparisons of the target element with the middle element. Since we're dividing the array in half with each comparison, we need at most O(log N) comparisons to find the element or determine that it's not present.
* **No Need to Examine All Elements:**<br> Unlike linear search, which would require examining all N elements in the worst case, binary search significantly reduces the number of elements that need to be considered, leading to a logarithmic time complexity.

---


### Question
Consider a rotated sorted array of distinct integers. What is the worst-case time complexity of finding a specific target element in this array using binary search?

### Choices
- [ ] O(1)
- [ ] O(n)
- [x] O(log n)
- [ ] O(n log n)

---
## Problem 2 Finding the square root of a number

### Motivation:
Imagine you're working on a mathematical problem or a scientific simulation that requires the square root of a number. Calculating square roots manually can be time-consuming, and a reliable and fast method is needed. Binary Search provides an elegant way to approximate square roots efficiently.

### Brute-Force Algorithm to Find the Square Root:

```cpp
function sqrt_with_floor(x):
    if x < 0:
        return "Undefined"  // Square root of a negative number is undefined

    if x == 0 or x == 1:
        return x  // Square root of 0 or 1 is the number itself

    // Start from 1 and increment until the square is greater than x
    guess = 1
    while guess * guess <= x:
        guess = guess + 1

    // Since the loop ends when guess^2 > x, the floor(sqrt(x)) is guess - 1
    return guess - 1
```

### Binary Search Principle for Square Root:
The key idea is to search for a number within a certain range that, when squared, is closest to the target value. We'll repeatedly narrow down this range until we achieve a satisfactory approximation.

**Intuition**:
* **Binary search:** You then start a binary search within this range. The midpoint of the range is calculated, and you compute the square of this midpoint.
* **Comparison:** You compare the square of the midpoint to the original number (x). Three cases can arise:
  * **Exact Match:** If the square of the midpoint is exactly equal to x, you've found a value very close to the square root.
  * **Square Less Than x:** If the squared midpoint is less than x, it suggests that midpoint can be the answer but we can get the more closer value towards right only(if present). So, adjust the search range to be [midpoint+1, right end of current range].
  * **Square Greater Than x:** If the squared midpoint is greater than x, it indicates the square root lies to the left of the midpoint. Consequently, adjust the search range to be [left end of current range, midpoint-1].
* **Convergence:** You repeat the binary search by calculating new midpoints and comparing the squares until you converge on an approximation that is sufficiently close to the actual square root.

For example:
 <img src="https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/054/294/original/upload_42e49c38798729971da9ece87233dca8.png?1697636550" width=600 />

### Example: Finding Square Root using Binary Search

**Scenario:**
We want to find the square root of the number 9 using Binary Search.

**Solution:**
* Initialize left = 1 and right = 9 (since the square root of 9 won't be greater than 9).
* Calculate mid = (left + right) / 2 = 5.
* Compare 5 * 5 with 9.
* Since 25 is greater than 9, narrow the search to the left half.
* Update right = 4.
* Calculate mid = (left + right) / 2 = 2.
* Compare 2 * 2 with 9.
* Since 4 is less than 9, adjust the range to the right half.
* Update left = 3.
* Calculate mid = (left + right) / 2 = 3.
* Compare 3 * 3 with 9.
* We found an exact match! The square root of 9 is 3.

---
## Finding the square root of a number 

### Pseudocode:
Here's a simple pseudocode representation of finding the square root using Binary Search:

```cpp
function findSquareRoot(target):
    if target == 0 or target == 1:
        return target
    
    left = 1
    right = target
    result = 0

    while left <= right:
        mid = left + (right - left) / 2

        if mid * mid == target:
            return mid
        else if mid * mid < target:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result
```

### Analysis and Complexity:

In each step of the Binary Search, we compare the square of the middle element with the target value. Depending on the result of this comparison, we adjust the search range. Since Binary Search divides the range in half with each step, the time complexity of this algorithm is O(log n), where n is the value of the target number.

### Use Cases:
Finding the square root using Binary Search has applications in various fields, such as mathematics, engineering, physics, and computer graphics. It's often used when precise square root calculations are required, especially in scenarios where hardware or library-based square root functions are not available.


---
## Problem 3 Median of two sorted Arrays

## Problem Statement
Given two sorted arrays A and B of sizes m and n, respectively, your task is to find the **median** of the two sorted arrays. 

The median is the middle value in an ordered list of numbers. If the combined size of the two arrays (i.e., m + n) is odd, the median is the middle element. If the combined size is even, the median is the average of the two middle elements.

![median_def](https://hackmd.io/_uploads/B1ENZJU2R.png)



**Example:**

A = [1,3,4,7,10,12]
B = [2,3,6,15]

median = 5

**Explantation**

On merging the two arrays, the resulting array when sorted, would look like [1,2,3,3,4,6,7,10,12,15].
Hence, the median is (4+6)/2 = 5


### Brute Force Approach

The brute force approach to find the median of two sorted arrays involves merging both arrays into a single sorted array, and then finding the median of this merged array.

Steps:
1. Merge the two sorted arrays into one sorted array.
2. Find the median of the merged array.

### Implementation for Brute Force

```cpp
def findMedianBruteForce(arr1, arr2):
    merged = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]
```

### Complexity Analysis for Brute Force:
* **Time Complexity** : 
 Merging Two Arrays: O(m + n) where m and n are the lengths of the two arrays.
 Finding the Median: O(1).
 Overall Time Complexity: **0(m+n)**
* **Space Complexity :**
 The additional space is required to store the merged array, hence space complexity: **0(m+n)**

### Optimized Approach

**Observations:**

1. Whenever we are dealing with sorted arrays, we should atleast once think about Binary Search to reduce Time Complexity.

![bs](https://hackmd.io/_uploads/rJ4VEyUnA.png)

2. We know when we finally merge these arrays, we will have half elements on the left of median and half on the right of it. If we fix the number of elements from the first array that we will keep on the left, the number for second array gets fixed

![obs1](https://hackmd.io/_uploads/BkjSrJIhC.png)


**Steps:** 

1) Assume two arrays, A and B, where A is the smaller one.
2) Use binary search on the smaller array to partition it and the larger array such that the elements on the left partition are less than or equal to the elements on the right partition. It is sufficient to check the boundary elements to ascertain that.

![l1r1](https://hackmd.io/_uploads/rJBiBy8h0.png)
![l2r2](https://hackmd.io/_uploads/SyhorJUh0.png)


Lets take a few examples to solidify this step
![case1](https://hackmd.io/_uploads/Hymx8kLh0.png)

If we choose 4 as the number of elements to be on the left from the A, B needs to have 1 element on the left part. We can see that this is not a valid partition as 7 > 3 violates the requirement.

![case2](https://hackmd.io/_uploads/rJ6VIJL2R.png)

If we choose 2 elements from A to be on the left, B needs to have 3. Here too 6>4 violates the condition.

![case3](https://hackmd.io/_uploads/SyZYUkL3C.png)

For 3 elements from A, our condition is satisified.

3) Find the maximum element on the left and the minimum element on the right. The median is calculated based on whether the total number of elements is odd or even.

**Implementation for Optimized approach**

```cpp
function findMedianOptimized(arr1, arr2):
    if length(arr1) > length(arr2):
        # Ensure arr1 is smaller than arr2
        swap(arr1, arr2)

    x = length(arr1)
    y = length(arr2)
    low = 0
    high = x

    # Binary search on the smaller array (arr1)
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # maxX is the largest element on the left side of arr1
        if partitionX == 0:
            maxX = negative infinity
        else:
            maxX = arr1[partitionX - 1]

        # maxY is the largest element on the left side of arr2
        if partitionY == 0:
            maxY = negative infinity
        else:
            maxY = arr2[partitionY - 1]

        # minX is the smallest element on the right side of arr1
        if partitionX == x:
            minX = positive infinity
        else:
            minX = arr1[partitionX]

        # minY is the smallest element on the right side of arr2
        if partitionY == y:
            minY = positive infinity
        else:
            minY = arr2[partitionY]

        # Check if we found the correct partition
        if maxX <= minY and maxY <= minX:
            # If total elements are even
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            # If total elements are odd
            else:
                return max(maxX, maxY)

        # If maxX > minY, we took too many elements from arr1
        elif maxX > minY:
            high = partitionX - 1
        # If maxY > minX, we took too few elements from arr1
        else:
            low = partitionX + 1

```

### Complexity Analysis of Optimized Approach:

* Time Complexity: **O(log(min(m, n)))**.
* Space Complexity: **O(1)** (no extra space except variables for the binary search).


