## Exponential Search

Exponential search is an algorithm for searching in a sorted list. As we know for a sorted list of size $n$, binary search works in $\log{(n)}$, but can we do better that this?

Apparantely, no. But what if we use some mechanism to determine a smaller index-range in which the element we are searching(say $X$) belongs?

For example, we are searching for $8$ in the list ${2,4,5,8,9,10}$. Now, if we use binary search then the searching index-range will be $1$ to $6$. But we can see that if we binary search in the index-range $3$ to $6$ then also we will be able to find $8$.

Note that the number of comparisons for index-range $3$ to $6$ is lesser than the ordinary binary search, this is the main idea behind the **Exponential search**. 

But how do we determine the index-range for a given element?

As the name of the algorithm suggests, we are going to use exponentiation. We find an index of form $2^k$(starting from $k$=$0$), such that the element at that index is greater than $X$. 

After that we do binary search over the index-range $2^{k-1}$ to $2^k$. It is easy to see that $X$ is in the index-range $2^{k-1}$ to $2^k$, because element at index $2^{k-1}$ is lesser then $X$ and element at index $2^k$ is greater than $X$.

Now, Let's see the implementation.

```cpp
#include <bits/stdc++.h>
using namespace std;

int binary_search(vector<int>& list, int l, int r, int key)
{
    while(l <= r) {
    	int mid = (l + r)/2;
    	if(list[mid] == key)
    		return mid;
    	else if(list[mid] < key)
    		l = mid + 1;
    	else
    		r = mid - 1;
    }
    
    return -1; 
}

int exponential_search(vector<int>& list, int key)
{
	int size = list.size() - 1;
	
	if(list[0] == key)
		return 0;

	// Finding range
    int bound = 1;
    while (bound < size && list[bound] < key)
        bound *= 2;
	
    return binary_search(list, bound/2, min(bound + 1, size), key);
}

int main()
{
	vector<int> list{3,5,6,7,8,10,17,20,24,27};
	int key = 10;
	
	cout << exponential_search(list,key) << endl;
	
	return 0;
}
```
**Note:** It is assumed that the elements in the list are unique.

### Quiz Time
Can you figure out the time complexity in terms of the index($i$) of the element?
**Answer:** $log(i)$
**Explanation:** In order to find an index of form $2^k$, such that $list[2^k] > key$, we are running the while loop $\lceil\log{i}\rceil$ times, that is $\mathcal{O}(\log(i))$ time complexity.

After that, binary search on the range $2^{\log(i)-1}$ to $2^{\log(i)}$, that is interval of size $2^{\log(i)-1}$, takes $\log{(2^{\log(i)-1})}$ comparisons, which leads to $\mathcal{O}(\log(i))$ complexity.

So the overall time complexity is $\mathcal{O}(\log(i))$.

Can you figure out the best time complexity?
**Answer:** $\mathcal{O}(1)$
**Explanation:** When the element we are searching is at the first index.

### When to use exponential search?
Worst case time-complexity of exponential search is $\log(n)$. 

We can see that, when the element is near to the front of the list, exponential search performs better than binary search. 

Therefore, when the list size is very big and it looks like the element is too far from the end of the list, use exponential search.

## Interpolation Search

Suppose, we have a very long sorted list and we are searching $X$. Let say, we have a mechanism that takes us directly to an index near to $X$, rather than to the middle element of the range, in case of binary search.

**For example**, we are looking for a key which is near to the end of a long list. So, by this mechanism it will indicate that we should start searching close to the end of the list.

In binary search, we use simple formula $(l+r)/2$ to find the mid index. But now, we are going to use different formula. So the question is, how to determine such a formula which finds an index near to the key($X$)?

In order to find such a formula, we need to have some characteristics of data, other than it is sorted. Like, the given data follows linear distribution or exponential distribution or normal distribution or some other distributions. 

For linear distribution case, the formula is as below:

$mid = low + ((key - arr[low]) * (high - low) / (arr[high] - arr[low]))$

Where $low$ and $high$ are lowerbound and upperbound of the search range, respectively.

**Note:** Other than the mid index formula the algorithm is similar to binary search, with some very intuitive conditions.

```
// After determining mid from the above formula
// procedure is same as binary search
if (list[mid] < key)
	low = mid + 1;
else if (list[mid] > key)
	high = mid - 1;
else
	return mid;

```

![enter image description here](https://lh3.googleusercontent.com/wtZUN15MdVpeP__i3VL6tEwwcasjWDBSrq_jDRHGji_HMuFNbZ_yriiqjz9uML4dkwgU7hzx6HXC)

```cpp
#include <bits/stdc++.h>
using namespace std;

int interpolation_search(vector<int>& list, int key)
{
	int size = list.size();
    int low = 0, high = size - 1, mid;

    while ((list[high] != list[low]) && (key >= list[low]) && (key <= list[high])) {
	
		// Linear distribution case        
        mid = low + ((key - list[low]) * (high - low) / (list[high] - list[low]));

        if (list[mid] < key)
            low = mid + 1;
        else if (list[mid] > key)
            high = mid - 1;
        else
            return mid;
    
    }

    if (key == list[low])
        return low ;
    else
        return -1;
}

int main()
{
	vector<int> list{3,5,6,7,8,10,17,20,24,27};
	int key = 10;
	
	cout << interpolation_search(list,key) << endl;
	
	return 0;
}
```

Similarly, for exponential distribution case, the formula is as below:

$mid = low + ((\log(key) - \log(arr[low])) * (high - low) / (\log(arr[high]) - \log(arr[low])))$

**Time Complexity**

If the data follows some distributions, then it works in $\mathcal{O}{(\log({\log{n}}))}$, which is quite good. 

But in worst case it might take $\mathcal{O}{(n)}$.
