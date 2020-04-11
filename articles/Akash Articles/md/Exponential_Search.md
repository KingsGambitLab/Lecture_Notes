## Exponential Search

Exponential search is an algorithm for searching in a sorted list. For a sorted list of size $n$, binary search works in $\log{(n)}$, but can we do better that this?

Apparantely, no. But what if we use some mechanism to determine a smaller index-range, in which the element we are searching(say $X$) belongs?

For example, we are searching for $8$ in the list ${2,4,5,8,9,10}$. Now, if we use binary search then the searching index-range will be $1$ to $6$. But we can see that if we binary search in the index-range $3$ to $6$ then also we will be able to find $8$.

Note that the number of comparisons for smaller index-range is lesser than the ordinary binary search, this is the main idea behind **Exponential search**.

But how do we determine such index-range for a given element?

As the name of the algorithm suggests, we are going to use exponentiation. We find an index of form $2^k$(starting from $k$=$0$), such that the element at that index is greater than $X$.

After that we do binary search over the index-range $2^{k-1}$ to $2^k$. It is easy to see that $X$ is in the index-range $2^{k-1}$ to $2^k$, because element at index $2^{k-1}$ is lesser then $X$ and element at index $2^k$ is greater than $X$.

Let's have an example,

![enter image description here](https://lh3.googleusercontent.com/5NjJTuBXtIAxPlwv9ZoFG9SLNRN56E_iC4zXIZ1pDu4ipFRkuAlG001c9STTgTfSOFtVTlIu11mM)

![enter image description here](https://lh3.googleusercontent.com/hIiFWzFhtnV4RKNsIMPdcwxryes9DYMkX9HM6Kp4lE0nx8aJKy1U4DO6FEQauxukZnoKG54zAMpN)

![enter image description here](https://lh3.googleusercontent.com/bGRaeI3f4bucSeNqT1JFEFsc8HK8nh8o8sikRhV6QcaOar4qAYV9ITN3pD5TV6CEQsavzO0K4wEh)

![enter image description here](https://lh3.googleusercontent.com/UeoCFXPtEcQ6ucUCkn1FbOST2PI7DjiLXnDHlK-EoX5hXDj4Zj12mjVvvlYZt2UpEFYzCiZrg_vo)
![enter image description here](https://lh3.googleusercontent.com/xVS0E4OEd_aLFb2HpcFbqqpgoQQIlq2kak07LDuCFiYO7nyzmJvBlmWs6EL4dISlR36BhqcVBwD_)

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
**Answer:** $\mathcal{O}(log(i))$
**Explanation:** In order to find an index of form $2^k$, such that $list[2^k] > key$, we are running the while loop $\lceil\log{i}\rceil$ times, that is $\mathcal{O}(\log(i))$ time complexity.

After that, binary search on the range $2^{\log(i)-1}$ to $2^{\log(i)}$, that is interval of size $2^{\log(i)-1}$, takes $\log{(2^{\log(i)-1})}$ comparisons, which leads to $\mathcal{O}(\log(i))$ complexity.

So the overall time complexity is $\mathcal{O}(\log(i))$.

Can you figure out the best time complexity?
**Answer:** $\mathcal{O}(1)$
**Explanation:** When the element we are searching is at the first index.

### When to use exponential search?
Worst case time-complexity of exponential search is $\mathcal{O}(\log(n))$. 

When the element is near to the front of the list, exponential search performs better than binary search for the case of very large list. 

For an example purpose, Let say for below array we are searching for 3,`[1,3,4,6,10,14,18,20,22,23,25,28,30,33,36,39,40,41]`. Then it is easy to see that binary search certainly takes more comparisons then exponential search.

**Therefore, when the list size is very big and it looks like the element is too far from the end of the list, use exponential search.**
