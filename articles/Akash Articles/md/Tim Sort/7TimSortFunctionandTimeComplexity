Finally, let's discuss Tim sort function.

It is trivial to understand if you have understood the whole thing so far.

The procedure is as follows:
1. First check whether the list size is smaller than 64, then simply use binary insertion sort and we are done. Otherwise,
2. Use `compute_minrun()` function to find a _minimum run length_, as discussed before.
3. Next, use `find_Runandmake_Ascending()` function to find a run.
4. If the length of the run is smaller than _minimum run length_, then use binary insertion sort to insertion elements until the length of the run becomes equal to _minimum run length_.
5. Insert this run to the stack and execute `mergecollapse()` procedure.
6. Go to step 3, until the whole data is explored.
7. If the stack size is greater than 1, then use `mergeForceCollapse()` procedure at the end.

Finally, we have a completely sorted array.


```cpp
void Timsort(vector<int>& data)
{
    int low = 0, high = data.size();
    int remaining = data.size();

    if (remaining < MIN_MERGE)
    {
        int runlen = find_Runandmake_Ascending(data, low, high);
        binarysort(data, runlen, low, high);
        return;
    }

    int minRun = compute_minrun(remaining);

    do {

        int runlen = find_Runandmake_Ascending(data, low, high);

        // If run length is smaller than minRun, then use binarySort
        if (runlen < minRun) {
            int force_len = remaining <= minRun ? remaining : minRun;
            binarysort(data, low + runlen, low, low + force_len);
            runlen = force_len;
        }

        stack_of_runs[stackSize].base_address = low;
        stack_of_runs[stackSize].len = runlen;

        stackSize++;

        mergecollapse(data);

        low += runlen;
        remaining -= runlen;

    } while (remaining != 0);

    if (stackSize > 1)
        mergeForceCollapse(data);
}
```

Finally, we have learned Tim sort.

## Time Complexity of Tim sort

**Best case complexity** is $\mathcal{O}(N)$, which is observed when the whole data is already sorted.

Average and worst-case complexity is $\mathcal{O}(NlogN)$.

We are not going into the proof, but let's try to understand. 

As we have seen _merging_ and _find run_ operations have $O(N)$ complexities, but the final complexity is based on the number of times we are using the same element while `mergeCollapse` and `mergeForceCollapse` procedures. And as per the criteria discussed, the overall complexity turned out to be $\mathcal{O}(NlogN)$.

**Space complexity:** $\mathcal{O}(N)$
