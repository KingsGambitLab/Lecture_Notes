## `merge_LtoR` & `merge_RtoL`

The basic generic procedure for both of these functions is as below, **most of the things we have already discussed**.

 1. First, copy the smaller run into a temporary array.
 2. Start by merging them in a classical way, until one run seems to be contributing elements consistently(winning consistently).
    If one run wins for more than _cur_minGallop_ times consistently, then we enter into galloping mode.
 3. We stay in galloping mode as far as it is performing well.
 4. If we exit galloping mode, then we penalize by incrementing _cur_minGallop_. Then start from step-2 again. **But when to stop?**

**There are two degenerate cases, we check again and again while executing the function, which shows that merge procedure is at its end.** They are based on the two conclusions we have already discussed:

**Conclusion 1.** The last element of $run_1$ is the largest element.
**Conclusion 2.** The first element of $run_2$ is the smallest element.

$len_1$ and $len_2$ are remaining lengths of $run_1$ and $run_2$.

For `merge_LtoR`(left to right),
1. $len_2$ == 0 -> Only elements of $run_1$ are left.
2. $len_1$ == 1 -> It is the last element of $run_1$ and according to conclusion 1, all remaining elements of $run_2$ are smaller than the remaining element in $run_1$.

For `merge_RtoL`(right to left),
1. $len_1$ == 0 -> Only elements of $run_2$ are left.
2. $len_2$ == 1 -> It is the first element of $run_2$ and according to conclusion 2, all remaining elements of $run_1$ are larger than the remaining element in $run_2$.

Finally, implementation.
```cpp
// If len1 <= len2 the mergeLo is called
// First element of run1 must be greater than first element of run2
// and last element of run1 must be greater than all elements of run2
void merge_LtoR(vector<int>& data, int base1, int len1, int base2, int len2)
{    
    // Copy smaller run in temporary buffer
    vector<int> small_run(data.begin() + base1, data.begin() + base1 + len1);

    int cursor1 = 0;
    int cursor2 = base2;
    int dest = base1;

    // Start by first element of run2
    // which is the smallest
    data[dest++] = data[cursor2++];

    // Two degenerate cases
    if (--len2 == 0) {
        while (cursor1 < len1)
            data[dest++] = small_run[cursor1++];
        return;
    }

    if (len1 == 1) {
        while (cursor2 < base2 + len2)
            data[dest++] = data[cursor2++];
        data[dest] = small_run[cursor1];
        return;
    }

    // will be used to end merging for the degenerate case
    bool done = false;

    // cur_minGallop is a global variable
    // Copy it to a local variable for performance
    int minGallop = cur_minGallop;
    while (true) {
        int count1 = 0; // Number of times in a row that first run won
        int count2 = 0; // Number of times in a row that second run won

        // Straightforward merge procedure until
        // one run starts winning consistently
        do {
            if (data[cursor2] < small_run[cursor1]) {
                data[dest++] = data[cursor2++];
                count2++;
                count1 = 0;
                if (--len2 == 0) {
                    done = true;
                    break;
                }
            }
            else {
                data[dest++] = small_run[cursor1++];
                count1++;
                count2 = 0;
                if (--len1 == 1) {
                    done = true;
                    break;
                }
            }
        } while (count1 < minGallop && count2 < minGallop);

        if (done)
            break;

        // One run is winning consistently then galloping
        // may lead to a huge win
        do {
            count1 = gallopRight(small_run, data[cursor2], cursor1, len1, 0);
            if (count1 != 0) {
                len1 -= count1;
                while (count1--)
                    data[dest++] = small_run[cursor1++];

                if (len1 <= 1) {
                    done = true;
                    break;
                }
            }

            data[dest++] = data[cursor2++];
            if (--len2 == 0) {
                done = true;
                break;
            }

            count2 = gallopLeft(data, small_run[cursor1], cursor2, len2, 0);

            if (count2 != 0) {
                len2 -= count2;
                while (count2--)
                    data[dest++] = data[cursor2++];

                if (len2 == 0) {
                    done = true;
                    break;
                }
            }
            data[dest++] = small_run[cursor1++];
            if (--len1 == 1) {
                done = true;
                break;
            }

            minGallop--;
        } while (count1 >= MIN_GALLOP || count2 >= MIN_GALLOP);

        if (done)
            break;

        // Penalty for coming out from gallop mode
        if (minGallop < 0)
            minGallop = 0;
        minGallop++;

    }

    // Assing the global variable back
    // value should be at least 1
    cur_minGallop = max(1, minGallop);

    // Move rest of the things
    if (len1 == 1) {
        while (len2--)
            data[dest++] = data[cursor2++];
        data[dest] = small_run[cursor1];
    }
    else {
        // len2 == 0 && len1 > 1
        while (len1--)
            data[dest++] = small_run[cursor1++];
    }

    // clear memory
    small_run.clear();

}

// If len2 <= len1 the merge_RtoL is called
// First element of run1 must be greater than first element of run2
// and last element of run1 must be greater than all elements of run2
void merge_RtoL(vector<int>& data, int base1, int len1, int base2, int len2) 
{
    // Copy smaller run in temporary buffer
    vector<int> small_run(data.begin() + base2, data.begin() + base2 + len2);

    int cursor1 = base1 + len1 - 1;
    int cursor2 = len2 - 1;
    int dest = base2 + len2 - 1;

    // Start by the last element of run1
    // which is the largest element
    data[dest--] = data[cursor1--];

    // Degenerate cases
    if (--len1 == 0) {
        while (len2--)
            data[dest--] = small_run[cursor2--];
        return;
    }

    if (len2 == 1) {
        while (len1--)
            data[dest--] = data[cursor1--];
        data[dest] = small_run[cursor2];
        return;
    }

    // will be used to end merging for the degenerate case
    bool done = false;

    // cur_minGallop is a global variable
    // Copy it to a local variable for performance
    int minGallop = cur_minGallop;
    while (true) {
        int count1 = 0; // Number of times in a row that first run won
        int count2 = 0; // Number of times in a row that second run won

        // Straightforward merge procedure until
        // one run starts winning consistently
        do {
            if (data[cursor1] > small_run[cursor2]) {
                data[dest--] = data[cursor1--];
                count1++;
                count2 = 0;
                if (--len1 == 0) {
                    done = true;
                    break;
                }
            }
            else {
                data[dest--] = small_run[cursor2--];
                count2++;
                count1 = 0;
                if (--len2 == 1) {
                    done = true;
                    break;
                }
            }
        } while (count1 < minGallop && count2 < minGallop);

        if (done)
            break;

        // One run is winning consistently then we galloping
        // may lead to a huge win
        do {
            count1 = len1 - gallopRight(data, small_run[cursor2], base1, len1, len1 - 1);
            if (count1 != 0) {
                len1 -= count1;
                while (count1--)
                    data[dest--] = data[cursor1--];

                if (len1 == 0) {
                    done = true;
                    break;
                }
            }

            data[dest--] = small_run[cursor2--];
            if (--len2 == 1) {
                done = true;
                break;
            }

            count2 = len2 - gallopLeft(small_run, data[cursor1], 0, len2, len2 - 1);

            if (count2 != 0) {
                len2 -= count2;
                while (count2--)
                    data[dest--] = small_run[cursor2--];

                if (len2 <= 1) {
                    done = true;
                    break;
                }
            }
            data[dest--] = data[cursor1--];
            if (--len1 == 0) {
                done = true;
                break;
            }

            minGallop--;
        } while (count1 >= MIN_GALLOP || count2 >= MIN_GALLOP);

        if (done)
            break;

        // Penalty for coming out from gallop mode
        if (minGallop < 0)
            minGallop = 0;
        minGallop++;

    }

    // Assing the global variable back
    // value should be at least 1
    cur_minGallop = max(1, minGallop);

    // Move rest of the things
    if (len2 == 1) {
        while (len1--)
            data[dest--] = data[cursor1--];
        data[dest] = small_run[cursor2];
    }
    else {
        // len1 == 0 and len2 > 1
        while (len2--)
            data[dest--] = small_run[cursor2--];
    }

    // clear memory
    small_run.clear();

}
```

**Time complexity**: $\mathcal{O}(N_1+N_2)$, where $N_1$ and $N_2$ are lengths of runs.
It is the same as the traditional merge procedure but again constant factor is improved.

Therefore, time complexity of `merge_At` is also $O(N_1+N_2)$. Galloping works in $O(log(i))$, but for asymptotic complexity it will be considered in $O(N_1+N_2)$.
