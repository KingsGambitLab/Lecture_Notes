# Tim Sort

Tim sort is the algorithm behind Java and Python's inbuilt `sort()` function. It is a hybrid algorithm, which uses concepts behind insertion sort and merge sort.

## Why to learn Tim Sort?

As we know, asymptotic notation hides some information in it, which is the constant factor associated with it. The constant factor depends upon the type of hardware and the amount of resources used by the algorithm for the provided input data. It is necessary to consider the constant factor to evaluate the real time complexity.

**For example**, Insertion sort outperforms Merge sort for a small list of elements, even if asymptotically Insertion sort and Merge sort works with complexity $\mathcal{O}(N^2)$ and $\mathcal{O}(N\log{N})$ respectively. Why?

Merge sort uses recursive calls and $\mathcal{O}(N)$ extra space. Due to this memory overhead and overhead of recursive calls, the constant factor for merge sort turned out to be higher than insertion sort for a small list of elements. Therefore, $C_1(N^2) < C_2(N\log{N})$, for small N.

**Notes:**

 - Here, **Overhead** is any combination of excess or indirect computation time, memory or other resources that are required to perform a specific task on the computer.
 - N is the size of the input data.

As we know Quick sort, Merge sort and Heap sort has the time complexity of $\mathcal{O}(N\log{N})$. Tim sort also has the same time complexity, but it is designed such that the associated constant factor is as low as possible.

Tim sort is an **adaptive algorithm**, which means that it changes its behavior based on the patterns observed in the input data. That is why it is an **intelligent algorithm** and works well for real-world data.

Tim sort is a **stable algorithm**, it is one of the distinctive feature of this algorithm.

**Note:** Heap sort and Quick sort are not stable algorithms.

If you observe any array of integers, then you will find disjoint subarrays of already sorted(increasing or decreasing) data.

For example, `[10 13 12 7 5 15 17]` array contains three already sorted subarrays `[10 13 | 12 7 5 | 15 17]`. First and third runs are increasing and second one is decreasing.

## Brief explanation of Tim sort algorithm

1. The whole array is split into subarrays such that these subarrays are sorted(as discussed above). If a subarray is sorted in a descending manner, then it is reversed.
**Note:** We use some criteria regarding the minimum size of these subarrays.
2. Then we use merge operation to merge these sorted subarrays. This merge operation is an advanced version of the merge routine used in the standard merge sort procedure.

    Finally, we have a completely sorted array.
