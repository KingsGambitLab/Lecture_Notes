## Run
 
 Run is an ordered(sorted) sub-array. It can be non-decreasing or decreasing. The input array is to be split into Runs.

![enter image description here](https://lh3.googleusercontent.com/CNvldwkU56Hva_WMGiFUTV4FTU7VeOBM-NFfRgPWqfBt6o9UkGETs7qflxoe-FCop2zlxD5KM3rr)

Below is a structure for Run.
```cpp
    struct run {
        // Starting address of a run
        int base_address;
        // length of run
        int len;
        run() {
            base_address = 0;
            len = 0;
        }
        run(int a, int b) {
            base_address = a;
            len = b;
        }
    };
```

## Minimum Run length 
Minimum run length is the minimum length of such run. Its value is decided based on the number of elements($n$) in the list. Let's see the algorithm to find it out.
    
Roughly the computation is:
- If $n < 64$, return $n$
- Else if n is an exact power of $2$, return $32$.
- Else return an integer $k$, $32 <= k <= 64$, such that $n/k$ is close to, but strictly less than, an exact power of $2$.
    
```cpp
        int compute_minrun(int n)
        {
            int r = 0;

            while (n >= 64) {
                r |= n & 1;
                n >>= 1;
            }
            return n + r;
        }
```

Here, 64 is a standard value decided by the inventor such that the **min-run length**, for a list of size greater than 63, will turn out to be in the range 32 to 64 inclusive. 

The main reason for this is that we are going to use modified insertion sort to sort this small chunk of data and insertion sort performs better on an array of small size.

## Why do we find runs?
There is no need to sort already sorted data, therefore to take advantage of already sorted data present in the list. We find runs.

## How to find a "Run"?

A **Run** can be increasing or decreasing, so the minimum length of a **Run** is $2$, because any sequence of length 2 is either increasing or decreasing.

Whether the run is increasing or decreasing, can be decided based on the first two elements. After finding a type(increasing or decreasing) of a run, we find its length by running a loop until the corresponding condition is satisfied.

In the case of a decreasing run, we reverse the list in the end.

For a given array `13 9 5 4 10 14 16`, let's find runs.

![enter image description here](https://lh3.googleusercontent.com/hCmQ1gKRonCEyIgHxzGI-_QtsDE3u9WXvc9Biix9xjEiWhlU4gTRMFECNjS_bUEg-JSEfqpUeRNV)

![enter image description here](https://lh3.googleusercontent.com/0wSo1NmDagPDbBiUrAsRIkm_nADA4eiYH1YUqzYbDMT-ZbQdx-wXVqN1yxXDbz8RYnuJiNGKbVrx)

![enter image description here](https://lh3.googleusercontent.com/y6NDKmBb9eDSbAAXgAS9zCr63FS2g58wecjQOnopyAhsQpwR5zzPxM0yaWkmxqT9GvvZZtUMLno4)

![enter image description here](https://lh3.googleusercontent.com/MjmPJm7lyFE8G5GvSrPf7l6qfkRTzUh5pRDqJ3uylORLZ239KKGOPTu0Um5e8wjNoqZMpeSRkDVQ)

![enter image description here](https://lh3.googleusercontent.com/V7nyWxDBPjKEqO1hCIMnwqU7ifu9Z2p4YHVHtDUrlaVPgvCATPPeG3WuSq7jOlqRCFempWm5mT8P)

![enter image description here](https://lh3.googleusercontent.com/lbX6Cvu9F3uhUwiX17cS3A-QfLF3aNpbjSpIRWXFRrXrTO_tKIesOec6cxUYhkgY1XuPGTwmibop)

![enter image description here](https://lh3.googleusercontent.com/ntfTHXnrjP0Fcm0OntLRK5XnvtpyioTiEkJoid4q2N5Fn1Mol6q-8wqT6pJuDhiDrMSOnGpTpUpl)

Now, we have found a run `4 5 9 13`. Similarly, next run `10 14 16` is already ascending, so no need to reverse it.

```cpp
// Find run and return its length
// @param start: Start position for the next run
int find_Runandmake_Ascending(vector<int>& data, int start)
{
    int end = data.size();
    if (start + 1 == end)
        return 1;

    int runHi = start + 1;

    /// Ascending
    if (data[start] < data[runHi])
        while (runHi < end && data[runHi - 1] < data[runHi])
            runHi++;
    /// Descending
    else {
        while (runHi < end && data[runHi - 1] > data[runHi])
            runHi++;

        reverseRange(data, start, runHi - 1);
    }

    return runHi - start;
}

// To reverse elements from the range lo to hi
void reverseRange(vector<int>& data, int lo, int hi) {
    while (lo < hi)
        swap(data[lo++], data[hi--]);
}
```
**Time complexity:** $\mathcal{O}(N)$, where $N$ is size of found run. It is trivial to understand.

**If the length of the run is less than the constant min-run length, then we use binary insertion sort to add elements until the length becomes min-run length.**
