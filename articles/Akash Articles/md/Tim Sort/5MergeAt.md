## MergeAt()

Now, let's discuss `mergeAt` procedure, which is used to merge two runs.

Let $base_i$ and $len_i$ are base address and length of $run_i$, respectively.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/21.jpg)

We perform two operations before merging two runs:

 1. Find index of the first element of $run_2$ into $run_1$. If the index turns out to be the last, then no merging is required.

    ![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/22.jpg)

    Otherwise just increment the base address for $run_1$, because the elements before this index are already in place.
    
    ![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/23.jpg)

 2. Similarly, find index of the last element of $run_1$ in $run_2$. If the index turns out to be the first, then no merging is required.

    ![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/24.jpg)
    
    Otherwise set $len_2$ to this index, because the elements after this index are already in place.
    ![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/25.jpg)

After performing this operation you notice that all elements of $run_2$ are less than last element of $run_1$ and first element fo $run_1$ is greater than first element of $run_2$, i.e. $run_1[base_1] > run_2[base_2]$. These implies two things:

Conclusion 1. The last element of $run_1$ is the largest element.
Conclusion 2. The first element of $run_2$ is the smallest element.
 
We will see how useful these conclusions are! Just keep it in mind.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/26.jpg)

Now, Let say we are merging two sorted arrays of size _$len_1$_ and _$len_2$_. In traditional merge procedure, we create a new array of size $len_1$+$len_2$. But in Tim sort's merge procedure, we just create a new temporary array of size $min(len1,len2)$ and we copy the smaller array into this temporary array.

The main intention behind it is to decrease **merge space overhead**, because it reduces the number of required element movements.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Tim_Sort/27.jpg)

Notice that we can do merging in both directions: **left-to-right**, as in the traditional mergesort, or **right-to-left**.

Now, suppose the $len_1$ is less than $len_2$, then we will create a temporary copy of $run_1$. To merge them, we are not going to allocate any more memory, but we will merge them directly into the main array, in **left-to-right** direction. In the other case($len_2$ < $len_1$), we will merge them in **right-to-left** direction. 

**The reason for different directions is that by doing this we are able to do merging in the main list itself.** You will be able to see this when we will see `merge_LtoR` and `merge_RtoL`.

```cpp

// Merges two runs
// parameter i must be stacksize - 2 or stacksize - 3
void mergeAt(vector<int>& data, int i)
{
    int base1 = stack_of_runs[i].base_address;
    int len1 = stack_of_runs[i].len;
    int base2 = stack_of_runs[i + 1].base_address;
    int len2 = stack_of_runs[i + 1].len;

    stack_of_runs[i].len = len1 + len2;
    
    // Copy the third last run to 2nd last
    if (i == stackSize - 3)
        stack_of_runs[i + 1] = stack_of_runs[i + 2];

    stackSize--;

    // Find position of first element of run2 into run1
    // prior elements of run1 are already in place
    // so just ignore it
    int pos1 = gallopRight(data, data[base2], base1, len1, 0);
    base1 += pos1;
    len1 -= pos1;
    if (len1 == 0)
        return;

    // Find where the last element of run1 goes into run2
    // subsequent elements of run2 are already in place
    // so just ignore it
    len2 = gallopLeft(data, data[base1 + len1 - 1], base2, len2, len2 - 1);
    if (len2 == 0)
        return;

    if (len1 <= len2)
        merge_LtoR(data, base1, len1, base2, len2);
    else
        merge_RtoL(data, base1, len1, base2, len2);
}
```

Time complexity will be discussed in the next article.
