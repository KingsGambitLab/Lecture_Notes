## Complete Implementation
```cpp
#include<bits/stdc++.h>
using namespace std;

// Other Global declarations
const int MIN_MERGE = 64;
const int MIN_GALLOP = 7;
int cur_minGallop = MIN_GALLOP;

struct run {
	int base_address, len;
	run() {
		base_address = 0;
		len = 0;
	}
	run(int a, int b)
	{
		base_address = a;
		len = b;
	}
};

vector<run> stack_of_runs;
int stackSize;

int compute_minrun(int n)
{
	int r = 0;

	while (n >= 64) {
		r |= n & 1;
		n >>= 1;
	}
	return n + r;
}

void binarysort(vector<int>& data, int start, int lo, int hi)
{
	//	cout << "binarysort" << endl;
	if (start == lo)
		start++;

	// Iterate from the start index to hi
	for (; start < hi; start++) {
		int ele = data[start];

		// Now find correct position using binary search
		int left = lo, right = start;
		while (left < right) {
			int mid = (left + right) >> 1;
			if (data[mid] > ele)
				right = mid;
			else
				left = mid + 1;
		}

		int n = start - left;

		if (n > 0) {
			int j = start;
			while (j != left) {
				swap(data[j], data[j - 1]);
				j--;
			}
		}
	}
}

// To reverse a descending sequence
void reverseRange(vector<int>& data, int lo, int hi) {
	//	cout << "reverse " << endl;
	while (lo < hi) {
		swap(data[lo++], data[hi--]);
	}
}

// To find the run
int find_Runandmake_Ascending(vector<int>& data, int start, int end)
{
	//	cout << "find_Runandmake_Ascending" << endl;
	if (start + 1 == end)
		return 1;

	int runHi = start + 1;

	// Ascending
	if (data[start] < data[runHi])
		while (runHi < end && data[runHi - 1] < data[runHi])
			runHi++;
	// Descending
	else {
		while (runHi < end && data[runHi - 1] > data[runHi])
			runHi++;

		reverseRange(data, start, runHi - 1);
	}

	return runHi - start;
}

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

// Merges two runs
// parameter i must be stacksize - 2 or stacksize - 3
void mergeAt(vector<int>& data, int i)
{
	int base1 = stack_of_runs[i].base_address;
	int len1 = stack_of_runs[i].len;
	int base2 = stack_of_runs[i + 1].base_address;
	int len2 = stack_of_runs[i + 1].len;

	stack_of_runs[i].len = len1 + len2;
	
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

// This method is called each time a new run is pushed onto the stack,
void mergecollapse(vector<int>& data)
{
	//	cout << "mergecollapse" << endl;
	while (stackSize > 1) {
		int n = (int)stackSize - 2;
		if (n > 0 && stack_of_runs[n - 1].len <= stack_of_runs[n].len + stack_of_runs[n + 1].len) {
			if (stack_of_runs[n - 1].len < stack_of_runs[n + 1].len)
				n--;
			mergeAt(data, n);
		}
		else if (stack_of_runs[n].len <= stack_of_runs[n + 1].len)
			mergeAt(data, n);
		else
			break;
	}
}

// Merges all runs on the stack until only one remains.  This method is
// called once, to complete the sort at last.
void mergeForceCollapse(vector<int>& data) // 
{
	//	cout << "mergeForceCollapse" << endl;
	while (stackSize > 1) {
		int n = stackSize - 2;
		if (n > 0 && stack_of_runs[n - 1].len < stack_of_runs[n + 1].len)
			n--;
		mergeAt(data, n);
	}
}

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
	
	cout << is_sorted(data.begin(),data.end()) << endl;
	
	return 0;
}

```
