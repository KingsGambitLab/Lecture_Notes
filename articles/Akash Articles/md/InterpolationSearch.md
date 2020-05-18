# Interpolation Search

Suppose, we have a very long sorted list and we are searching for a key-$X$. Let say, we have a mechanism that takes us directly to an index near to $X$, to determine which side to go next for searching, rather than to the middle index of the range in case of binary search.

**For example**, we are looking for a key that is near to the end of a long list. So, this mechanism will indicate that we should start searching close to the end of the list. This may lead to fewer comparisons than ordinary binary search.

In binary search, we use simple formula $(l+r)/2$ to find the mid index. But now, we are going to use a different formula. So the question is, how to determine such a formula that finds an index near to the key($X$)? Here is when interpolation comes into the picture.

Interpolation is a well-known concept in mathematics, which is used in many fields of engineering and science for estimations. Here also we are going to use it to determine an approximate index for a key. Particularly we are going to use linear interpolation. Let's understand it from a geometrical perspective.

We are given that a line passes through two points $(x_1, y_1)$ & $(x_2, y_2)$. Now, we are given a value $y$ and we are asked to find $x$ such that $(x,y)$ is on the line.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Interpolation%20Search/1.jpg)

Now, by the equation to find a slope, below formula can be used to find $x$,

$\Large{\frac{y-y_1}{x-x_1} = \frac{y_2-y_1}{x_2-x_1}}$

$\Large{{x-x_1} =\frac{(y-y_1)\times (x_2-x_1)}{y_2-y_1}}$

$\Large{{x} =x_1 + \frac{(y-y_1)\times (x_2-x_1)}{y_2-y_1}}$

In order to find a formula for arrays, we need to have some characteristics of data, other than it is sorted. Like, the given data follows linear distribution or exponential distribution or uniform distribution over some range.

Let say our array values follow a linear distribution, i.e. if we put indexes on $x$ axis and corresponding array values on $y$ axis, then it roughly creates a line. For example, given array `[0,2,4,6,8,10,12]` exactly follows linear distribution.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Interpolation%20Search/2.jpg)

If you condsider index as $x$ values and array values as $y$, then for three points $(high,arr[high])$, $(low,arr[low])$, $(x,key)$ the formula turns out to be as below:

$x = mid = low + \Large\frac{(key - arr[low]) \times (high - low)}{ (arr[high] - arr[low])}$

Where $low$ and $high$ are lower bound and upper bound of the search range, respectively.

If you use the above formula, then it will directly tell the position of any element in the array in one go. For example, $X=6$ and $low = 0, high = 6$

$mid = 0 + \large\frac{6*(6-0)}{12-0} = 3$

Which is exactly the index of an element $6$.

Now, if the given index is not exactly the index of the key, then other than the mid index formula the algorithm is similar to binary search, with some very intuitive conditions.

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

Therefore, when the data is exactly linearly distributed, then interpolation search finds the key in one go.

In case if the data roughly(not exactly) creates a line, then also interpolation search is expected to work well. For example, `[0 1 2 4 9 11 14 15 16 19]`. Try to search for some keys using this formula. Works well, only two comparisons.

**So, particularly when the data is uniformly distributed over some range, then interpolation search works very well, like only $\lceil log(log(n))\rceil$ comparisons.**

Let's have an example run for array `[0 1 2 4 9 11 14 15 16 19]` and key = 16,

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Interpolation%20Search/3.jpg)
![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Interpolation%20Search/4.jpg)


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
    vector<int> list{0, 1, 2, 4, 9, 11, 14, 15, 16, 19};
    int key = 16;
    
    cout << interpolation_search(list,key) << endl;
    
    return 0;
}
```

### Quiz time
Similarly, Can you find a formula for the exponential distribution case?

**Hint 1:** Use logarithm.
**Hint 2:** Logarithm brings down exponentialy distributed data to linearly distributed data.
**Answer:**
$mid = low + \large\frac{(\log(key) - \log(arr[low])) * (high - low) }{(\log(arr[high]) - \log(arr[low]))}$

## Time Complexity

**Interpolation search works very well when the data follows some kind of distribution and we are able to bring this distribution down to uniform distribution by using some mechanism(as we have done in exponential case).**

For the above case, it works in $\mathcal{O}{(\log({\log{n}}))}$, which is quite good.

But in worst case(no distribution) it might take $\mathcal{O}{(n)}$.
