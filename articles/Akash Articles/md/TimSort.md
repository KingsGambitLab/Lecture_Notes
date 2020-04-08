# Tim Sort

Tim sort is the algorithm behind Java and Python's inbuilt `sort()` function. It is a hybrid algorithm, which uses concepts behind insertion sort and merge sort.

## Why to learn Tim Sort?

As we know, asymptotic notation hides some information in it, which is the constant factor associated with it. Constant factor depends upon the type of hardware and the amount of resources used by the algorithm for the provided input data. It is necessary to consider constant factor to evaluate the real time complexity.

**For example**, Insertion sort outperforms Merge sort for a small list of elements, even if asymptotically Insertion sort and Merge sort works with complexity $\mathcal{O}(N^2)$ and $\mathcal{O}(N\log{N})$ respectively. Why?

Merge sort uses recursive calls and $\mathcal{O}(N)$ extra space. Due to this memory overhead and overhead of recursive calls, the constant factor for merge sort turned out to be higher than insertion sort for a small list of elements. Therefore, $C_{is}(N^2) < C_{ms}(N\log{N})$, for small N.

**Notes:**

 - Here, **Overhead** is any combination of excess or indirect computation time, memory or other resources that are required to perform a specific task on computer.
 - Suffix $is$ and $ms$ stands for insertion sort and merge sort respectively. 
 - For the shake of simplicity, overhead is considered in constant factors $C_{is}$ and $C_{ms}$.
 - N is the size of the input data.

As we know Quick sort, Merge sort and Heap sort has the time complexity of $\mathcal{O}(N\log{N})$. Tim sort also has the same time complexity, but it is designed such that the associated constant factor is as low as possible.

Tim sort is an **adaptive algorithm**, which means that it changes its behavior based on the patterns observed in the input data. That is why it is an **intelligent algorithm** and more optimal than other sorting algorithms.

Tim sort is a **stable algorithm** and we take too much care to maintain stability.

## Brief explanation of tim sort algorithm

1. The whole array is splitted into subarrays such that these subarrays are sorted. If a subarray is sorted in descending manner, then it is reversed. 
**Note:** We use some criteria regarding the minimum size of these subarrays.
2. Then we use merge operation to merge these sorted subarrays. This merge operation is an advanced version of the merge routine used in the standard merge sort procedure.

	Finally, we have completely sorted array.

Now, let's discuss the entire algorithm.

 ## Run 
 
 _Run_ is an ordered(sorted) sub-array. It can be non-decreasing or decreasing. The input array is to be splitted into _Runs_.

Below is a structure for _Run_.
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

Here, 64 is a standard value decided by the inventor such that the **min-run length**, for a list of size greater than 63, will turned out to be in the range 32 to 64 inclusive. 

The main reason for this is that we are going to use modified insertion sort to sort this small chunk of data and insertion sort performs better on an array of small size.

## Why do we find runs?
There is no need to sort already sorted data, therefore inorder to take advantage of already sorted data present in the list. We find runs.

## How to find a "Run"?

A **Run** can be increasing or decreasing, so minimum length of a **Run** is $2$, because any sequence of length 2 is either increasing or decreasing.

Whether the run is increasing or decreasing, can be decided based on the first two elements. After finding a type(increasing or decreasing) of a run, we find its length by running a loop until the corresponding condition is satisfied.

In the case of decreasing run, we reverse the list in the end.

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
If the length of the run is less than the constant **min-run length**, then we use **binary insertion sort** to add elements until the length becomes min-run length.

## Binary Insertion Sort

As we know the main idea of Insertion sort is to take an element and insert it at the correct position. Now, we are going to use binary search to find correct position, rather than a simple loop.

After finding the correct index, we right-shift the data from that index by 1 and insert the element at the correct index.

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
		// Shift by 1 towards right
		if (n > 0) {
			int j = start;
			while (j != left) {
				swap(data[j], data[j - 1]);
				j--;
			}
		}

		data[left] = ele;
	}
}
```

Now, we have understood how to find runs. Next we are going to see how to merge them?

## Merging

While we merging runs, we take too much care to about stability. In order to maintain **stability** we always merge consecutive runs, because otherwise it may result in instability.

For example, [2 3 4], [1 2 5], [2 4 5] are three consecutive runs, so if we merge first and third run first, then 2 of third run will end up before 2 of second run in the later merge operation.

Now, to maintain information about runs, we are going to use an array, which is used as a stack, so whenever a new run comes, we insert it at the top. Now, let's discuss some criteria about merging this runs.

Merging lists of similar sizes tends to perform better than the other case, due to relatively simple logic. It is called **"balanced merge"**. 

Now, let's discuss some criteria we use to merge runs efficiently.

![enter image description here](https://lh3.googleusercontent.com/oNnCn_wv0fTCSN-myagncWWjagqzEoVfnGOz0n2srsmWu8HZKWr88tPIVH-Cr9_LJQZ8cxH4jPfb)

Criterion 1: If the stack-size is greater than or equal to 3 and $|Z| <= |Y| + |X|$ is true, then if $|Z|<|X|$, then merge $|Z|$ and $|Y|$ otherwise merge $|X|$ and $|Y|$.

Criterion 2: $|Y|<=|X|$ then merge them.

Whenever we push a new run into the stack, we check for these criteria and we merge runs accordingly until none of these criteria satisfy.

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

There are two things to take a note:

1. In order to have balanced merge, we are delaying the merge by waiting for a next run.
2. If we want to take advantage of cache memory, that is fresh runs are already in the cache therefore merging them have less memory overhead, then we should merge the fresh runs as soon as possible.

So, by taking care of both the things, criteria are decided.

After we have found all the runs, we merge all the remaining runs as per below procedure.

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

Now, let's discuss a new concept **Galloping**.

## Galloping

Standard merging procedure for merging two sorted arrays array_1: [10] and array_2: [1,2,3,4,6,9,14] goes as below:

CREATE GIF
![enter image description here](https://lh3.googleusercontent.com/fGNXjeqWRQEtqN3ZjxR55HsZv61YSpxgT98dpXaCe2YMmBNaJz9O5jrMFRamL1GV3DkAuWhUVuOV)

![enter image description here](https://lh3.googleusercontent.com/pDUhaOlftbV2L3ITwk18SVkVG5NXuGoMJ1XDC3q50IjgYAn-c-DJmP6l2nILbwe32ulWNnW0FkbC)

![enter image description here](https://lh3.googleusercontent.com/MQw924q3lie_KKdFj1AaAWnMghDVP7TCcugsp71Uk4Z8VdvvJ-I5IaMknrBG7N0T-XCmZqAB4wtB)

![enter image description here](https://lh3.googleusercontent.com/jUk_Vzny2Ro0bRttqEEsd8627CbHZ7jVkdjZzeLbpBCic5oNhCDhEy8naQA68xKmkO9ucDH7A933)

![enter image description here](https://lh3.googleusercontent.com/RDQTt974n5uox1D9LtQhMpgyf9v3_aqc8fL4q9jwYmbJo1nrlGgUPUZNSf63DGPoJ2U54oTcEjp6)

![enter image description here](https://lh3.googleusercontent.com/9Ma4pKJQPO866e8PdytQZnZ3ljcuO-A38mNT9QNU6qsn7ZvgCAiU4dLbyyfBkAiBa9WdRMef8o1Z)

![enter image description here](https://lh3.googleusercontent.com/2ilz_WMDaNbLNdQ5xop1vwHjMkufbNt8KH93pAE6JIDIPUl9Ub0JH6YdZZJIK9e_jkJu3oKpLG6j)

![enter image description here](https://lh3.googleusercontent.com/ZY8fNtYIR3ZbWESgVeUm20GuFpz-34X7YqHvSxKmmwtsFIwWmDfDuJiNSX1UpccRkz2ap3I7oN5v)

As you can see we are consistently taking element from array_2 until we reach $14$. But can we do better? Yes, use galloping.

The idea of galloping is to perform exponential search to find a correct position, rather than comparing elements one by one.

**For example**, if we find correct position of $10$ in array_2 using exponential search, then it will be a huge win in terms of **taken time**.

**Does Galloping work in every situation?**

Certainly no, when we are not achieving a sufficient index jump by performing exponential search, then we might end up having more comparisons than classical merge procedure. But what is a sufficient jump?

It is decided to be a constant $7$, it is called **minimum gallop**(MIN_GALLOP). Other than that we have a new variable called _current_min_gallop_, which is assigned to constant MIN_GALLOP(7) at the start of the algorithm.

We use galloping mode during merge. To avoid the drawbacks of galloping mode, we perform actions as below:

1. If we find that we are taking elements from one array more than or equal to _current_min_gallop_ times consistently, then we enter into galloping mode.
2. After entering into galloping mode, we continue to remain into galloping mode if and only if we find that we have a jump of more than or equal to MIN_GALLOP(7). Otherwise we exit gallop mode. If galloping mode is a success, then we decrease _current_min_gallop_ by $1$ per one success. It promotes galloping mode.
	**Note:** In galloping mode we are using MIN_GALLOP constant to check for the success of galloping mode and to enter into galloping mode we are using _current_min_gallop_ variable.
3. After we exit galloping mode, we increase _current_min_gallop_ by one, to discourage a return to galloping mode again. This is to make sure that next we recover the lost of more comparisons.

So, **we are trying to balance the whole situation by taking the advantage of galloping.** Sometimes, the value of _current_min_gallop_ becomes so large that we never enter into galloping mode.

The whole procedure discussed above will be helpful in merge procedure. Now, we come back to pure galloping.

Note that we can do galloping(exponential search) from any side of the array, either left or right, because we are just intended to find a position and that can be approached by doing exponential search from any side.

The starting position for the search is called a "$hint$". Sometimes it is better to search from left and sometimes from right. For the given array below,

![enter image description here](https://lh3.googleusercontent.com/jkr4R3v4liODaPlf3MzaGwXpTg83InKn6lOxX3XwdilDeDkZZO6RegRb8ZaFyHxRddkz7BdOPXFH)

If we want to find position for $3$, then starting from index 0($hint = 0$) is efficient, but if we are looking for position of $13$ then starting from index $len-1$($hint = len-1$) is more efficient.

**Procedure for _galloping_:**

 1. If $key < data[base+hint]$, then it indicates that we should do galloping towards left side, because element at the starting position is greater than the key.
 2. Otherwise, we do galloping towards right side.
 3. To do galloping. we first find range for the key using the procedure we use in exponential search.
 4. At last, we do binary search over the range to find the correct position.

We have two types of galloping function `gallopRight` and `gallopLeft`, the main difference between them is, `gallopRight` and `gallopLeft` returns rightmost index and leftmost index respectively in case if there are equal elements.

For example, for the array given below,

![enter image description here](https://lh3.googleusercontent.com/FxAq82p754Q1Zkpdzca65jujMzeCx-9ho_rBWF2mUWJo5fu7-q8siSlVVgsJ4_Obln-B6i-AKJ5Y)

If you find a position of 13 by using galloping, then `gallopLeft` will return 6, but `gallopRight` will return 9.

In simple mode it is trivial to maintain stability, but to maintain stability while merging in galloping mode, we sometimes use `gallopRight` and sometimes `gallopLeft`. Just to get the basic idea, see the below example, it will be more clear when we will the merge procedure.

![enter image description here](https://lh3.googleusercontent.com/s-xqdPcSotlep3yl-xYqiFNzcEhbfBih0ZqLFS_uNXJN_pGoTGsXKcu9VJTRcYykYb4tqyLt_4XJ)

Now, if we are finding a position of run2[0] in run1, then we will use `gallopRight`, but if we are finding a position for run1[3] in run2, then we will use `gallopLeft`.

We have a slightly modified binary search methods for both of them.

Below is the implementation for both the functions.

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

Now let's discuss `mergeAt` procedure, which is used to merge two runs.

Let $base_i$ and $len_i$ are base address and length of $run_i$, respectively.

![enter image description here](https://lh3.googleusercontent.com/-k-_xBINQS8RL2TU4ZLKmht0qtGB-cVRD0THTWGRIf14dNUn2BdtBON29uwN1cmvVzU_eFjbFYyR)

We perform two operations before merging two runs:

 1. Find index of the first element of $run_2$ into $run_1$. If the index turns out to be the last, then no merging is required.

	![enter image description here](https://lh3.googleusercontent.com/erUBBF7EjNlid-Z_o78Pp98jJ3lIr2KOKPDg-HNGQllB7cStXz5mGr0eu9VE_HyFfmB9BE48mO-F)

	Otherwise just increment the base address for $run_1$, because the elements before this index are already in place.
	
	![enter image description here](https://lh3.googleusercontent.com/r3inmg14-vASclUZDd2kNv6mbhYilCfXa4mZ4PQY40g_navG2k6xoABLpEufnuIZUFqJUD_RzxFg)

 2. Similarly, find index of the last element of $run_1$ in $run_2$. If the index turns out to be the first, then no merging is required. 

	![enter image description here](https://lh3.googleusercontent.com/erUBBF7EjNlid-Z_o78Pp98jJ3lIr2KOKPDg-HNGQllB7cStXz5mGr0eu9VE_HyFfmB9BE48mO-F)
	
	Otherwise set $len_2$ to this index, because the elements after this index are already in place.
	
	![enter image description here](https://lh3.googleusercontent.com/mzSFF0qSzGFQbWLL1HQeKOwllLfJzdfDHPWKoJHddGbwR4wP_iaclklp7jQUomGAM0uNrJpb7xVa)

After performing this operation you notice that all elements of $run_2$ are less than last element of $run_1$ and first element fo $run_1$ is greater than first element of $run_2$, i.e. $run_1[base_1] > run_2[base_2]$. These implies two things:

Conclusion 1. The last element of $run_1$ is the largest element.
Conclusion 2. The first element of $run_2$ is the smallest element.
 
We will see how useful these conclusions are! Just keep it in mind.

![enter image description here](https://lh3.googleusercontent.com/-k-_xBINQS8RL2TU4ZLKmht0qtGB-cVRD0THTWGRIf14dNUn2BdtBON29uwN1cmvVzU_eFjbFYyR)

Now, Let say we are merging two sorted arrays of size _$len_1$_ and _$len_2$_. In traditional merge procedure, we create a new array of size $len_1$+$len_2$. But in Tim sort's merge procedure, we just create a new temporary array of size $min(len1,len2)$ and we copy the smaller array into this temporary array.

The main intention behind it is to decrease **merge space overhead**, because it reduces the number of required element movements.

![enter image description here](https://lh3.googleusercontent.com/Ljf7l2doSHfEoRX7gP1pFSYTCqgNhSc7a1Me2toR4dKWvwfupFq_DYe_FIck5kUJfbxDk9QrnYH-)

Notice that we can do merging in both directions: **left-to-right**, as in the traditional mergesort, or **right-to-left**.

Now, suppose the $len_1$ is less than $len_2$, then we will create a temporary copy of $run_1$. To merge them, we are not going to allocate any more memory, but we will merge them directly into the main array, in **left-to-right** direction. In the other case($len_2$ < $len_1$), we will merge them in **right-to-left** direction. 

**The reason for different directions is that, by doing this we are able to do merging in the main list itself.** You will be able to see this when we will see `merge_LtoR` and `merge_RtoL`.

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

Now, let's discuss `merge_LtoR` and `merge_RtoL`. 

The generic procedure for both of this functions is as below, most of the things we have already discussed in galloping part.

 1. First copy the smaller run into temporary array.
 2. Start by merging them in a classical way, until one run seems to be contributing elements consistently, let's call it a win. If one run wins for more than _cur_minGallop_ times consistently, then we enter into galloping mode.
 3. We stay into galloping mode as far as it is performing good.
 4. If we exit galloping mode, then we penalize by incrementing _cur_minGallop_. Then start from step-2 again.

**There are two degenerate cases, we check again and again while executing the function, which shows that merge procedure is at its end.** They are based on the two conclusions we have alredy discussed:

Conclusion 1. The last element of $run_1$ is the largest element.
Conclusion 2. The first element of $run_2$ is the smallest element.

For _merge_LtoR_, 
1. $len_2$ == 0 $\implies$ Only $run_1$ elements are left.
2. $len_1$ == 1 $\implies$ According to conclusion 1, all remaining elements of $run_2$ are smaller than the remaining element in $run_1$.

For _merge_RtoL_,
1. $len_1$ == 0 $\implies$ Only $run_2$ elements are left.
2. $len_2$ == 1 $\implies$ According to conclusion 2, all remaining elements of $run_1$ are larger than the remaining element in $run_2$.

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

	// Used to end merge in degenerate case
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

	// Rest of the things
	if (len1 == 1) {
		while (len2--)
			data[dest++] = data[cursor2++];
		data[dest] = small_run[cursor1];
	}
	else {
		while (len1--)
			data[dest++] = small_run[cursor1++];
	}

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

	data[dest--] = data[cursor1--];
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

	// Used to end merge in degenerate case
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

	// Rest of the things
	if (len2 == 1) {
		while (len1--)
			data[dest--] = data[cursor1--];
		data[dest] = small_run[cursor2];
	}
	else {
		while (len2--)
			data[dest--] = small_run[cursor2--];
	}

	small_run.clear();

}
```

Tim sort function is as below. It is trivial to understand, if you have understood the whole thing above.

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

Finally, We have learned Tim Sort.

```cpp
// Other Global declarations
const int MIN_MERGE = 64;
const int MIN_GALLOP = 7;
int cur_minGallop = MIN_GALLOP;

vector<run> stack_of_runs;
int stackSize;

int main()
{
	srand(unsigned(time(0)));

	vector<int> data;
	
	for(int i=0;i<200000;i++)
		data.push_back(rand());
		
	int size = data.size();

	// Standard procedure to find max. stack size for given n
	int stack_max_size = (size < 120 ? 5 : size < 1542 ? 10 : size < 119151 ? 19 : 40) * 256;

	stack_of_runs.resize(stack_max_size);
	for (int i = 0; i < stack_max_size; i++) {
		stack_of_runs[i] = run();
	}

	stackSize = 0;

	Timsort(data);
	
	return 0;
}

```

## Time Complexity

**Best case complexity** is $\mathcal{O}(N)$, which is observed when the whole data is already sorted.
In the **worst case**, Timsort takes $\mathcal{O}(NlogN)$.
Average complexity is $\mathcal{O}(NlogN)$.

Space complexity is $\mathcal{O}(N)$.
