## Binary Insertion Sort

As we know the main idea of Insertion sort is to take an element and insert it at the correct position. Now, we are going to use binary search to find the correct position, rather than a simple loop.

After finding the correct index, we right-shift elements and insert the element at the correct index.

For an array `[1 4 5 9 10 7 14]`, let's start binary insertion sort from element 7,

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/01.jpg)
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/02.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/03.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/04.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/05.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/06.jpg)

Similarly, for $14$, but it is already at its right position.

```cpp
// @param start: Position of next element to be inserted
// @param low: Lower index of the range
// @param high: Upper index of the range
void binaryInsertionsort(vector<int>& data, int start, int low, int high)
{
    if (start == low)
        start++;

    // Iterate from the start index to high-1
    for (; start < high; start++) {
        int ele = data[start];

        // Now find a correct position using binary search
        int left = low, right = start;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (data[mid] > ele)
                right = mid;
            else
                left = mid + 1;
        }

        int n = start - left;
        // Bring it at the right position
        if (n > 0) {
            int j = start;
            while (j != left) {
                swap(data[j], data[j - 1]);
                j--;
            }
        }
    }
}
```
**Time complexity:** $\mathcal{O}(N^2)$, due to swap operations after finding index using binary search. But the constant factor is lesser than ordinary insertion sort.

Now, we have understood how to find runs. Next, we are going to see how to merge them?

## Merging

While we merging runs, we take too much care to maintain stability. In order to maintain **stability** we always merge consecutive runs, because otherwise, it may result in instability.

**For example**, [2 3 4], [1 2 5], [2 4 5] are three consecutive runs, so if we merge first and third run first, then 2 of the third run will end up before 2 of the second run in the later merge operation.

Now, to maintain information about runs, we are going to use an array, **which is used as a stack**, so whenever a new run comes, we insert it at the top. Now, let's discuss some criteria about merging these runs.

Merging lists of similar sizes tend to perform better than the other case, due to relatively simple logic. It is called **"balanced merge"**.

Now, let's discuss some criteria we use to merge runs efficiently.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/07.jpg)

**Note:** $|X|$ is a size of a run X.

**Criterion 1:** If the stack-size is greater than or equal to 3 and $|Z| <= |Y| + |X|$ is true, 

Then if $|Z|<|X|$, then merge $|Z|$ and $|Y|$ otherwise merge $|X|$ and $|Y|$.

**Criterion 2:** $|Y|<=|X|$ then merge them.

Whenever we push a new run into the stack, we check for these criteria and merge runs accordingly until none of these criteria satisfy. The function does this work is called `mergecollapse`.

Below is a stack of runs, for the shake of simplicity only length of runs are shown. 

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/08.jpg)

Merge until none of these criteria satisfy. Criteria 1 is satisfying so merge,

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/09.jpg)
Again, criteria 1 is satisfying so again merge,
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/010.jpg)

No criteria are satisfying now, so stop.


**Note:** <code>mergeAt()</code> function is used to merge two runs, will be discussed.
```cpp
// This method is called each time a new run is pushed onto the stack
void mergecollapse(vector<int>& data) {
    while (stackSize > 1) {
        int n = (int) stackSize - 2;
        if (n > 0 && stack_of_runs[n - 1].len <= stack_of_runs[n].len + stack_of_runs[n + 1].len) {
            if (stack_of_runs[n - 1].len < stack_of_runs[n + 1].len)
                n--;
            // Procedure to merge runs at id n and n+1
            mergeAt(data, n);
        }
        else if (stack_of_runs[n].len <= stack_of_runs[n + 1].len)
            // Procedure to merge runs at id n and n+1
            mergeAt(data, n);
        else
            break;
    }
}
```

**There are two things to take note:**

1. In order to have a balanced merge, we are delaying the merge by waiting for the next run.
2. If we want to take advantage of cache memory, that is fresh runs are already in the cache, therefore, merging them have less memory overhead, then we should merge the fresh runs as soon as possible.

So, by taking care of both the things, criteria are decided.

Each time a run new is pushed on the stack we call `mergeCollapse` procedure, but it runs until criteria satisfy. Therefore, at the end of this procedure, it is possible that we have more than $1$ runs in the stack.

**Note:** At the end of the merging procedure, `stackSize = 1` means that this last run is the whole sorted array.

So, at the end of the merging procedure(after we have found the last run of the array), if the stack size is more than 1, then we will forcefully merge all the remaining runs. The function does this work is called `mergeForceCollapse()`.

```cpp
// Merges all runs on the stack until only one remains.  This method is
// called once, to complete the sort at last.
void mergeForceCollapse(vector<int>& data)
{
    while (stackSize > 1) {
        int n = stackSize - 2;
        if (n > 0 && stack_of_runs[n - 1].len < stack_of_runs[n + 1].len)
                n--;
        // Procedure to merge runs at id n and n+1
        mergeAt(data, n);
    }
}
```

**Note:** It will be more clear when we will discuss the final "Tim sort function".
