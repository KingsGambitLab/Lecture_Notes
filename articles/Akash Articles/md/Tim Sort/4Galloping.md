## Galloping

Standard merging procedure for merging two sorted arrays array_1: [10] and array_2: [1,2,3,4,6,9,14] goes as below:

CREATE GIF
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/11.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/12.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/13.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/14.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/15.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/16.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/17.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/18.jpg)

As you can see we are consistently taking elements from array_2 until we reach $14$. But can we do better? Yes, use galloping.

The idea of galloping is to perform exponential search to find a correct position, rather than comparing elements one by one.

**For example**, if we find the correct position of $10$ in array_2 using exponential search, then it will perform better than this traditional procedure.

**Does Galloping work in every situation?**

Certainly no, when we are not achieving a sufficient index jump by performing exponential search, then we might end up having more comparisons than classical merge procedure. But what is a sufficient jump?

It is decided to be a constant $7$, it is called **minimum gallop**(MIN_GALLOP). If index-jump is at least 7, then it is guaranteed to perform better than the traditional procedure. 

Other than that we have a new variable called _current_min_gallop_, which is assigned to constant MIN_GALLOP(7) at the start of the algorithm.

We use galloping mode during the merge. To avoid the drawbacks of galloping mode, we perform actions as below:

1. If we find that we are taking elements from one array more than or equal to _current_min_gallop_ times consistently, then we enter into galloping mode.
2. After entering into galloping mode, we continue to remain into galloping mode if and only if we find that we have a jump of more than or equal to MIN_GALLOP(7). Otherwise, we exit gallop mode. If galloping mode is a success, then we decrease _current_min_gallop_ by $1$ per one success. It promotes galloping mode.
    **Note:** In galloping mode we are using MIN_GALLOP constant to check for the success of galloping mode and to enter into galloping mode we are using _current_min_gallop_ variable.
3. After we exit galloping mode, we increase _current_min_gallop_ by one, to discourage a return to galloping mode again. This is to make sure that next time we recover the lost of more comparisons.

So, **we are trying to balance the whole situation by taking advantage of galloping.** Sometimes, the value of _current_min_gallop_ becomes so large that we never enter into galloping mode.

**The whole procedure discussed above will be helpful in merge procedure.** Now, we come back to pure galloping.

Note that we can do galloping(exponential search) from any side of the array, either left or right because we are just intended to find a position and that can be approached by doing exponential search from any side.

The starting position for the search is called a "$hint$". Sometimes it is better to search from the left and sometimes from the right. For the given array below,

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/19.jpg)

If we want to find position for $3$, then starting from index 0($hint = 0$) is efficient, but if we are looking for position of $13$ then starting from index $len-1$($hint = len-1$) is more efficient. **It is particularly efficient for big arrays.**

**Procedure for _galloping_:**

 1. If $key < data[base+hint]$, then it indicates that we should do galloping towards the left side because element at the starting position is greater than the key.
 2. Otherwise, we do galloping towards the right side.
 3. To do galloping. we first find the range for the key using the procedure we used in exponential search.
 4. At last, we do binary search over the range to find the correct position.

We have two types of galloping function `gallopRight` and `gallopLeft`, the main difference between them is, `gallopRight` and `gallopLeft` returns rightmost index and leftmost index respectively in case if there are equal elements.

For example, for the array given below,

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/110.jpg)

If you find a position of 13 by using galloping, then `gallopLeft` will return 6, but `gallopRight` will return 9.

In simple mode, it is trivial to maintain stability, but to maintain stability while merging in galloping mode, we sometimes use `gallopRight` and sometimes `gallopLeft`. Just to get the basic idea, see the below example, it will be more clear when we will the merge procedure.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/111.jpg)

Now, if we are finding a position of run2[0] in run1, then we will use `gallopRight`, but if we are finding a position for run1[3] in run2, then we will use `gallopLeft`.

We have a slightly modified binary search methods for both of them.

Below is the implementation of both functions. It is simply a slightly modified exponential search.

```cpp
// Returns k, 0 <= k <= n such that a[b + k - 1] <= key < a[b + k]
// Rightmost index in case of equal elements
int gallopRight(vector<int>& data, int key, int base, int len, int hint)
{
    int ofs = 1;
    int lastofs = 0;
    
    if (key < data[base + hint]) {
        int maxofs = hint + 1;

        // Gallop towards Left side
        // Find range for key using Exponentiation
        while (ofs < maxofs && key < data[base + hint - ofs]) {
            lastofs = ofs;
            ofs = (ofs << 1) + 1;
        }
        if (ofs > maxofs)
            ofs = maxofs;

        int tmp = lastofs;
        lastofs = hint - ofs;
        ofs = hint - tmp;

    }
    else {
        int maxofs = len - hint;

        // Gallop towards Right side
        while (ofs < maxofs && key >= data[base + hint + ofs]) {
            lastofs = ofs;
            ofs = (ofs << 1) + 1;
        }
        if (ofs > maxofs)
            ofs = maxofs;
        lastofs += hint;
        ofs += hint;
    }
    lastofs++;

    // Binary search over the range to find a position
    while (lastofs < ofs) {
        int mid = (lastofs + ofs) / 2;
        if (key < data[base + mid])
            ofs = mid;
        else
            lastofs = mid + 1;
    }
    return ofs;
}

// Returns k, 0 <= k <= n such that a[b + k - 1] < key <= a[b + k]
// Leftmost index in case of equal elements
int gallopLeft(vector<int>& data, int key, int base, int len, int hint)
{
    int ofs = 1;
    int lastofs = 0;
    if (key <= data[base + hint]) {
        int maxofs = hint + 1;
        
        // Gallop towards Left side
        // Find range for key using Exponentiation
        while (ofs < maxofs && key <= data[base + hint - ofs]) {
            lastofs = ofs;
            ofs = (ofs << 1) + 1;
        }
        if (ofs > maxofs)
            ofs = maxofs;

        int tmp = lastofs;
        lastofs = hint - ofs;
        ofs = hint - tmp;

    }
    else {
        int maxofs = len - hint;

        // Gallop towards right side
        while (ofs < maxofs && key > data[base + hint + ofs]) {
            lastofs = ofs;
            ofs = (ofs << 1) + 1;
        }
        if (ofs > maxofs)
            ofs = maxofs;
        lastofs += hint;
        ofs += hint;
    }
    lastofs++;

    // Binary search over the range to find a position
    while (lastofs < ofs) {
        int mid = (lastofs + ofs) / 2;
        if (key <= data[base + mid])
            ofs = mid;
        else
            lastofs = mid + 1;
    }
    return ofs;
}

```

**Time complexity:** It is same as exponential search, $O(log(i))$. But due to $hint$ mechanism, overall it works better than traditional exponential search.
