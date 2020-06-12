Z-function and z-algorithm

Z-algorithm is a **string-matching algorithm**, which is used to find a place where a string is found within a larger string. For example, `p = "ab"` and `s = "abbbabab"`, then KMP will find us `[0,4,6]` because $s$ has 3 occurrences of `"ab"`. It uses the value of **z-function** to do so.

Let's first see what is a **z-function**.

# Z-Algorithm
Z-function for a given string $s$ of length $n$ returns an array $z$ of length $n$, where $z[i]$ represents the length of the longest common prefix of string $s$(i.e. $s[0,n-1]$) and suffix of $s$ starting at $i$ i.e. $s[i,n-1]$.

**Note:** $s[l,r]$ represents substring of $S$ starting at index $l$ and ending at index $r$. Here, we are taking zero based indices.

Note that the value of $z[0]$ is not properly defined so we take it as zero($0$).

For example, 
1. $z("cccc") = [0,3,2,1]$
    Why $z[1]=3$? 
    Because $s[0,2] = s[1,3] = "ccc"$.
2. $z("ababab")=[0,0,4,0,2,0]$
    Why $z[2] = 4$? 
    Because $s[0,3] = s[2,5] = "abab"$.
3. $z("abacaba") = [0,0,1,0,3,0,1]$
    Why $z[4] = 3$?
    Because $s[0,2] = s[4,6] = "aba"$.

Can you figure out how do we find the value of z-function?

## Trivial Algorithm

The basic way to find the value of z-function is to do brute force. For index - $i$, we find it following way.
```
z[i] = 0;
while(i + z[i] < n && s[z[i]] == s[i + z[i]])
    z[i]++;
```

Simply, do this for every index.

```cpp
vector<int> z_function(string s) {
    int n = (int) s.size();
    vector<int> z(n);
    for (int i = 1; i < n; ++i)
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            z[i]++;
    return z;
}
```

## Efficient Algorithm

Now, we will take advantage of previously computed values as much as possible.

**Note:** $s[l,r]$ represents substring of $s$ starting at index $l$ and ending at index $r$.

Suppose we are given two indices $l$ and $r$ and also we are informed that $s[0,r-l]$ and $s[l,r]$ are equal. And we are finding value of z[i] such that $l<=i <= r$.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Z-algorithm/1.jpg)

How can we take advantage of that information to find $z[i]$?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Z-algorithm/2.jpg)

We can see that $s[i,r]$ and $s[i-l,r-l]$ are equal. Now, look at $z[i-l]$ and think how can we take advantage of it to find $z[i]$?

$z[i-l]$ tells us that $s[0,z[i-l]-1]$ and $s[i-l,i-l+z[i-l]-1]$ are equal and therefore $s[0,z[i-l]-1]$ and $s[i,i+z[i-l]-1]$ are equal, which means that $z[i]=z[i-l]$.

Confused? Go through the series of images below that will make the whole thing clear.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Z-algorithm/3.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Z-algorithm/4.jpg)

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Z-algorithm/5.jpg)

**But if $i+z[i-l]-1>r$, then it is ambiguous as we don't know anything about characters beyond $r$.**

And therefore we simply take $z[i]=min(z[i-l],r-i+1)$, which does not go beyond $r$.

Now, we will run brute force algorithm:

```
// As per the discussion
z[i] = min(z[i-l],r-i+1);
while(i + z[i] < n && s[z[i]] == s[i + z[i]])
    z[i]++;
``` 

After that if $i+z[i]$ is going beyond $r$, then we simply update indices $[l,r]$ as $l = i$ and $r = i + z[i]$, to maintain the **rightmost segment match** to take the advantage of previous values as much as possible for next indices as well.

**Note that initially $[l,r]$ segment is taken as $[0,0]$**. So, we start by doing brute force, or generally for an index $i$,

1. If $i<=r$, then we will take advantage of the previous value and then do brute force.
2. Else if $i>r$, we directly do brute force as we can't take advantage of any previous value.

```cpp
vector<int> z_function(string s) {
    int n = (int) s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        // Take advantage of previous value
        if (i <= r)
            z[i] = min (r - i + 1, z[i - l]);
        
        // Now do it usual brute-force way
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            ++z[i];
        
        // Set new range [l,r]
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}
```

### Time complexity

$O(N)$, as at each step of the algorithm $r$ at least increases one step, and the maximum possible value of r is $n-1$.

## Z-algorithm

Z-algorithm is used to search all occurrences of pattern-string $p$ in a string $s$ in $O(N)$.

For example, `p = "ab"` and `s = "abbbabab"`, then Z-algorithm will find us `[0,4,6]` because $s$ has 3 occurrences of `"ab"`.

Basic idea here is to create a new string having $p$ as a prefix and $s$ as a suffix i.e. `new_str = p + '#' + s`.

**To make sure that the value of Z-function does not exceed the length of $p$, we add a character that is never going to appear in string $s$ like `'#'`**.

Now, we will find Z-function of `new_str`.

Let say $m$ is the length of $p$.

$Z[i] = m$, means that `new_str[0..m-1]` is equal to `new_str[i...i+m-1]`, which is bacially means $p$(=`new_str[0...m-1]`) is equal to `new_str[i...i+m-1]`.

And therefore **all indices-$i$ where the values of Z-function $Z[i]$ equals to the length of $p$ means it is an occurrence of $p$ in $s$.**

```cpp
int main()
{
    string s,p;
    s = "abbbabab";
    p = "ab";
    int n = s.size(), m = p.size();

    // To save memory concatenate
    // s in p
    p += "#";
    p += s;
    // p = "ab#abbbabab";
    vector<int> z = z_function(p);

    // p = "ab#abbbabab";
    //         ^
    //        m+1
    cout << "occurences in s at the following indices: ";
    for(int i = m + 1; i < z.size(); i++) {
        if(z[i] == m) {
            cout << i - m - 1 << " ";
        }
    }
    
    return 0;
}
```

Z-function can also be used to solve various string related problems. Let's see some applications.

## To find the period of a string

Period of a string is the shortest length such that a larger string $s$ can be represented as a concatenation of one or more copies of a substring($t$).

For example, `s = "ababab"` has a period of $2$, where `t = "ab"`.

Let's see how to find the period of $s$ using the value of z-function of $s$.

**First of all note that the length of string $s$($n$) is divisible by the period of string.** Therefore, we can divide string $s$ into multiple blocks of the same length as a period of $s$.

First of all, we will find all divisors of $n$ and value of z-function of $s$. Now, we will need to find smallest divisor of $n$ for which $i+z[i] = n$, which is period of string $s$. Why?

$z[i]$ represents length of the longest common prefix of $s[0,n-1]$ and $s[i,n-1]$. As $i$ is divisor of $n$, we can divide the whole string into blocks of length $i$.

From the value of $z[i] = n-i$($\because i+z[i]=n$), we can see that the first block($s[0,i-1]$) is equal to the second block starting at $i$ i.e. $s[i,i+i-1]$, which is also equal to third block $s[2*i,3*i-1]$ and similarly all blocks turns out to be equal.

Therefore, smallest $i$ such that $n\% i=0$ and $i+z[i]=n$, is period of string $s$. If there is no such $i$, then string is not periodic as we cannot divide string into equivalent blocks.

```cpp
vector<int> getDivisors(int n)
{
    vector<int> v; 
    for (int i=1; i<=sqrt(n); i++)
        if (n%i==0) 
        {
            v.push_back(i);
            if (n != i*i)
                v.push_back(n/i);
        }
    return v;
}

int main()
{
    string s,p;
    s = "abcabcabc";
    int n = (int) s.size();
    vector<int> divs = getDivisors(n);
    sort(divs.begin(),divs.end());
    
    vector<int> z = z_function(s);
    int period = 0;
    for(auto i:divs) {
        if(i < n && z[i] + i == n) {
            period = i;
            break;
        }
    }
    
    if(period)
        cout << period << endl;
    else
        cout << "String is not periodic" << endl;
    
    return 0;
}

```

### String compression

Now, we know how to find a period of a string and therefore we can compress string as only one block of size $i$ which repeats all over again and again in $s$.

To retrieve the string back from the compressed version, we can attach its real length i.e. length of $s$.

```cpp
int main()
{
    string s,p;
    s = "abcabcabc";
    int n = (int) s.size();
    vector<int> divs = getDivisors(n);
    sort(divs.begin(),divs.end());
    
    vector<int> z = z_function(s);
    int period = 0;
    for(auto i:divs) {
        if(i < n && z[i] + i == n) {
            period = i;
            break;
        }
    }
    
    if(period != 0) {
        // A way to represent a compressed string
        // Attatch real length of string to retrieve easily
        pair<string, int> compressed_str{s.substr(0,period), n};
    }
    else {
        cout << "can't be compressed by this method" << endl;
    }
    
    return 0;
}
```

## Number of distinct substrings in a string

**Problem statement:** Find the number of unique substrings in a given string $s$.

**Brief idea:** Basic idea here is to take an empty string $t$ and add characters one by one from string $s$ and along with that check how many new substrings are created, due to the addition of a character in $t$, using z-function.

Let say we have already added some characters to $t$ from $s$ and $k$ is the number of distinct substrings currently. Now, we are adding a character $c$ to $t$, $t = t+c$. 

Note that total number of new substrings created by appending a character to any string($t$) is equal to the length of new string($t=t+c$) created. **For example, Appending `'d'` in `"abc"` creates 4 new substrings: `"d"`, `"cd"`, `"bcd"`, `"abcd"`.**

But how to find the number of new unique substrings created by the addition of $c$ **using z-function**?

**Hint:** Reverse $t$.

By reversing $t$, our task burns down into computing how many prefixes there are that don't appear anywhere else in $t$, which can be done by finding the z-function of $t$.

After finding value of z-function, we will find maximum value $z_{max}$($z_{max} = max\{z[i]\}, \forall i$) in the z-function of reversed $t$, which shows the length of longest prefix which is already in $t$ as a substring and it also implies that all smaller prefixes are already present as substrings in $t$.

Therefore, we will deduct this number of already present substrings i.e. $z_{max}$, from the total number of new substrings i.e. $|t|$.

Where $|t|$ is the length of $t$.

Finally, the number of new unique substrings created by the addition of a character turns out to be $|t|-z_{max}$.

**Note that $|t|$ is the length of $t$ after adding a character.**

```cpp
// Returns maximum of z[i]
int z_function(string& s) {
    int n = (int) s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    int mx = 0;
    for (int i = 1; i < n; ++i) {
        // Take advantage of previous value
        if (i <= r)
            z[i] = min (r - i + 1, z[i - l]);
        
        // Now do it usual brute-force way
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            ++z[i];
            
        mx = max(z[i], mx);
        
        // Set new range [l,r]
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return mx;
}

int main()
{
    string s,p;
    s = "abc";
    int n = s.size();
    
    string t, temp;
    int unique_substr = 0;
    
    for(int i=0; i < n; i++) {
        t += s[i];
        temp = t;
        reverse(temp.begin(), temp.end());
        // |t| - mx
        unique_substr += (int)t.size() - z_function(temp);
    }

    // Total number of unique substrings    
    cout << unique_substr << endl;
    
    return 0;
}
```
**Complexity**: $O(N^2)$, where $N$ is the length of $s$.

For each character appended, we are computing z-function in $O(N)$, which gives a time complexity of $O(N^2)$ in total.
