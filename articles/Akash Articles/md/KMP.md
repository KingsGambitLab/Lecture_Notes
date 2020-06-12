Prefix function and KMP-algorithm

KMP-algorithm is a widely used **string-matching algorithm**, which is used to find a place where a string is found within a larger string. For example, `p = "ab"` and `s = "abbbabab"`, then KMP will find us `[0,4,6]` because $s$ has 3 occurrences of `"ab"`. It uses the value of **prefix function** to do so.

Let's first see what is a **prefix function**.

# Prefix function

Prefix function for a given string($s$) of length $n$ returns an array $\Pi$ of length $n$, such that $i^{th}$ element of an array contains length of longest proper prefix of $S[0,i]$ which is also suffix of $S[0,i]$.

Where, $S[l,r]$ represents substring of $S$ starting at index $l$ and ending at index $r$.

**Note:** A proper prefix of a string is a prefix that is not equal to the string itself.

**For example**, $\text{prefix function("aaab")}$ returns $\Pi = [0,1,2,0]$. Can you figure out why it has value $2$ at index $2$(0-based)?

Because $S[0,1]$ is equal to $S[1,2]$.

Note that **$\Pi[0]$ is always zero.**

Mathematically, it can be written as,

$\Pi[i] = \max_ {k = 0 \dots i} \{k : s[0, k-1] = s[i-(k-1), i] \}$

## Trivial Algorithm

Basic algorithm to find such a value say at index $i$ is to compare all prefixes and suffixes of substring $S[0, i]$ one by one, of course, of the same lengths.

```
for(len = 1; len <= i; len++)
    if(s.substr(0,len) == s.substr(i-len+1,len)
        pi[i] = max(pi[i], len);
```

**Note that value at any index can not exceed $i$, $\forall i\in[0,n-1]$**.

```cpp
vector<int> prefix_function(string& s) {
    int m = (int)s.size();    
    vector<int> pf(m, 0);
    
    for (int i = 1; i < m; i++)
        for (int len = i; len > 0; len--)
            // break at first longest match, efficient!
            if (s.substr(0, len) == s.substr(i-len+1, len)) {
                pf[i] = len;
                break;
            }
    return pf;
}
```

**Time complexity:** $O(n^3)$

Can we do better? 

## Efficient Algorithm

We will take advantage of previously computed values as much as possible. We are going to reach the most efficient version($O(n)$) step by step.

### Step 1

The value of prefix function at any index $i$ can either increase by at most 1 or decrease by certain amount. That means, $\Pi[i] <= \Pi[i-1] + 1$. Why?

Suppose, for a given string "$s_0s_1s_2s_3s_4s_5s_6s_7s_8$", we are told that $\Pi[7]=3$, means "$s_0s_1s_2$" and "$s_5s_6s_7$" are equal substrings.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/KMP/1.jpg)

Now, suppose that $s_3$ and $s_8$ are equal, then what can we say about $\Pi[8]$?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/KMP/2.jpg)

$\Pi[8]$ will be 4. We can see that $\Pi[8] = \Pi[7]+1$. What if $s_3$ and $s_8$ are not equal?

We can not say anything about value of $\Pi[8]$, because depending on the value of $s_8$, there are many possibilities like, 

1. "$s_0s_1s_2$" = "$s_6s_7s_8$" OR
2. "$s_0s_1$" = "$s_7s_8$" OR
3. "$s_0$" = "$s_8$" OR
4. $\Pi[8]=0$

**But, now it will certainly be less than or equal to $\Pi[7]$.**

Therefore, $\Pi[i] <= \Pi[i-1] + 1$ is always true.

Formal proof for at most one increase can be given as below,

1. If $\Pi[i+1]>\Pi[i]+1$, then we can take the suffix ending in position $i$ with the length $\Pi[i]$ and remove the last character from it. 
2. We will end up with a suffix ending in position $i-1$ with the length $\Pi[i]−1$, which is better than $\Pi[i]$, that means we get a contradiction. 
3. Because $\Pi[i]$ represents the length of **the longest** proper prefix which is also a suffix.

By finding the value of prefix function using the truth discussed above, we will end up having only $O(N)$ string comparisons because of the value of prefix function(in total) increases by at most $N$ steps and also decreases by at most $N$ steps(see in reverse mode). Therefore, total complexity now is $O(N*N)$-as one string comparison takes $O(N)$.

```cpp
vector<int> prefix_function(string& s) {
    int m = (int)s.size();    
    vector<int> pf(m, 0);
    
    for (int i = 1; i < m; i++)
        for (int len = pi[i-1] + 1; len > 0; len--)
            // break at the first longest match
            if (s.substr(0, len) == s.substr(i-len+1, len)) {
                pf[i] = len;
                break;
            }
    return pf;
}
```

### Step 2

In step-1, we have seen that the value of prefix function overall increases by at most n steps, but due to string comparisons we ended up having $O(N^2)$ complexity. Here we will eliminate string comparisons completely.

Now, suppose that we are finding value of $\Pi[i]$ for string $s$, then from the value of $\Pi[i-1]$ we know that prefix of $s[0,i-1]$ of length $\Pi[i-1]$ is equal to the suffix of substring $s[0,i-1]$ of length $\Pi[i-1]$ i.e. $s[0,(\Pi[i-1]-1)] = s[(i-\Pi[i-1]),i-1]$

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/KMP/3.jpg)

As discussed in step-1, if $s[\Pi[i-1]]$ is equal to $s[i]$, then $\Pi[i] = \Pi[i-1]+1$.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/KMP/4.jpg)

If $s[\Pi[i-1]] != s[i]$, then we are in search for a next **longest prefix**(say has lenght $k$) which supports $s[0,k-1]=s[i-k,i-1]$, such that $s[k]=s[i]$ may turn out to be true.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/KMP/5.jpg)

Note that now anyway, the value of $\Pi[i]$ will be less than or equal to $\Pi[i-1]$, as discussed in step-1.

If $s[k] = s[i]$, then we can say that $\Pi[i]=k+1$ because $s[0,k]$ is the **longest prefix** which matches with a suffix and that is the definition of $\Pi[i]$.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/KMP/6.jpg)

The value-$k$ we are searching is exactly what $\Pi[\Pi[i-1]-1]$ represents. Why?

Points to note:

1. We know that $s[0,(\Pi[i-1]-1)] = s[(i-\Pi[i-1]),i-1]$.
2. If $s[\Pi[i-1]] != s[i]$, then value of $\Pi[i] <= \Pi[i-1]$ - from step-1.
3. We are searching for $k$, whose value must be less than $\Pi[i-1]$ because in case $s[k] = s[i]$(i.e. $\Pi[i]=k+1$), then 

    $\Pi[i] <= \Pi[i-1]  \implies k+1$ $<=$ $\Pi[i-1] \implies k < \Pi[i-1]$

Therefore, basically we are searching for the **longest proper prefix** of length less than $\Pi[i-1]$ such that it matches a suffix of $s[0,(\Pi[i-1]-1)]$(which equals to $s[(i-\Pi[i-1]),i-1]$ **from point-1 above**), which is the definion of the prefix function at index $\Pi[i-1] -1$ i.e. $\Pi[\Pi[i-1]-1]$.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/KMP/7.jpg)

If $s[k]=s[i]$, then we stop and assign $\Pi[i]=k+1$. Otherwise, we similarly go like $k = \Pi[\Pi[\Pi[i] - 1] - 1]$, $k = \Pi[\Pi[\Pi[\Pi[i] - 1] - 1]-1]$, ... until $k = 0$. Then if $s[i]=s[0]$, we assign $\Pi[i]=1$, and $\Pi[i]=0$ otherwise.

```cpp
vector<int> prefix_function(string& s) {
    int m = (int)s.size();
    
    vector<int> pf(m);
    
    for (int i = 1; i < m; i++) {
        int k = pf[i-1];
        while (k > 0 && s[i] != s[k])
            k = pf[k-1];
        if (s[i] == s[k])
            k++;
        pf[i] = k;
    }
    return pf;
}
```

**Time complexity:** $O(N)$, where $N$ is the length of the string $s$. Because now we are not doing any string comparisons.

## Knuth-Morris-Pratt Algorithm(KMP-algorithm)

KMP algorithm is used to search all occurrences of pattern-string $p$ in a string $s$ in $O(N)$.

For example, `p = "ab"` and `s = "abbbabab"`, then KMP will find us `[0,4,6]` because $s$ has 3 occurrences of `"ab"`.

**KMP is the most used algorithm in all inbuilt libraries of different programming languages to find "substring matches".**

Basic idea here is to create a new string having $p$ as a prefix and $s$ as a suffix i.e. `new_str = p + '#' + s`.

**To make sure that the value of prefix-function does not exceed the length of $p$, we add a character that is never going to appear in string $s$ like `'#'`**.

Now, we will find prefix function of `new_str`.

Let say $m$ is the length of $p$.

$\Pi[i] = m$, means that `new_str[0,m-1]` is equal to `new-str[i-m,i]`, which is bacially means $p$(=`new_str[0,m-1]`) is equal to `new_str[i-m,i]`.

And therefore **all indices-$i$ where the values of prefix function $\Pi[i]$ equals to the length of $p$ means it is an occurrence of $p$ in $s$.**

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
    vector<int> pi = prefix_function(p);

    // p = "ab#abbbabab";
    //         ^
    //        m+1
    cout << "occurences in `s` at the following indices: ";
    for(int i = m + 1; i < pi.size(); i++) {
        if(pi[i] == m) {
            cout << i - 2 * m << " ";
        }
    }
    
    return 0;
}
```

Prefix function can also be used to solve various string related problems. Let's see some applications.

## Find a period of a string

Period of a string is the shortest length such that a larger string $s$ can be represented as a concatenation of one or more copies of a substring($t$).

For example, `s = "ababab"` has a period of $2$, where `t = "ab"`.

Let's see how to find a period of $s$ using the value of prefix function of $s$.

**First of all note that length of string $s$($n$) is divisible by a period of string.**

As we know for a string of length $n$, $\Pi[n-1]$ represents the length of longest proper prefix which is also suffix. Now, let $k = n - \Pi[n-1]$.

Now, if $n$ is divisible by $k$, then we can divide the string $s$ into multiple blocks of length $k$.

$k=n-\Pi[n-1] \implies \Pi[n-1] = n-k$

That means, prefix of length $n-k$ and suffix of length $n-k$ are equal, as per the definition of $\Pi[n-1]$. 

If you compare all blocks from the start and the end, then it turns out that all blocks of k size are equal. This means that $k$ is the period of $s$, as the same blocks of size $k$ repeats in $s$.

Now, why $k$ is the smallest such period?

Because otherwise, the value of $\Pi[i-1]$ will be greater than $n-k$.

If $k$ does not divide $n$, then the string is not periodic as we cannot divide the string into equivalent blocks.

```cpp
int main()
{
    string s;
    s = "abbabbabb";
    int n = s.size();
    
    vector<int> pi = prefix_function(s);
    
    int possible_period = n - pi[n - 1];
    
    if(n % possible_period == 0) {
        cout << "periodic with " << possible_period << endl;
    }
    else {
        cout << "Not periodic string" << endl;
    }
    
    return 0;
}
```

**Time Complexity:** $O(N)$, $N$ is the length of $s$.

### Compressing a string

Now, we know how to find a period of a string and therefore we can compress string as only one block of size $k$ which repeats all over again and again in $s$.

To retrieve the string back from the compressed version, we can attach its real length i.e. length of $s$.

```cpp
int main()
{
    string s;
    s = "abbabbabb";
    int n = s.size();
    
    vector<int> pi = prefix_function(s);
    
    int possible_period = n - pi[n - 1];
    
    if(n % possible_period == 0) {
        string compressed = s.substr(0,possible_period);
        // A way to represent compressed string
        // Attatch real length to retrieve string back
        pair<string,int> compressed_str{s.substr(0,possible_period), n};
    }
    else {
        cout << "can not be compressed by this method" << endl;
    }
    
    return 0;
}
```

## Number of unique substrings in a string

**Problem statement:** Find the number of unique substrings in a given string $s$.

**Brief idea:** Basic idea here is to take an empty string $t$ and add characters one by one from string $s$ and along with that check how many new substrings are created, due to the addition of a character in $t$, using prefix-function.

Let say we have already added some characters to $t$ from $s$ and $k$ is the number of distinct substrings currently. Now, we are a adding character $c$ to $t$, $t = t+c$. 

Note that total number of new substrings created by appending a character to any string($t$) is equal to the length of new string($t=t+c$) created. **For example, Appending `'d'` in `"abc"` creates 4 new substrings: `"d"`, `"cd"`, `"bcd"`, `"abcd"`.**

But how to find the number of new unique substrings created by the addition of $c$ **using prefix function**?

**Hint:** Reverse $t$.

By reversing $t$, our task burns down into computing how many prefixes there are that don't appear anywhere else in $t$, which can be done by finding the prefix function of $t$.

After finding value of prefix function, we will find maximum value $\Pi_{max}$($\Pi_{max} = max\{\Pi[i]\}, \forall i$) in the prefix function of reversed $t$, which shows the length of longest prefix which is already in $t$ as a substring and it also implies that all smaller prefixes are already present as substrings in $t$.

Therefore, we will deduct this number of already present substrings i.e. $\Pi_{max}$, from the total number of new substrings i.e. $|t|$.

Where $|t|$ is the length of $t$.

Finally, the number of new unique substrings created by the addition of a character turns out to be $|t|-\Pi_{max}$.

**Note that $|t|$ is the length of $t$ after adding a character.**

```cpp
int prefix_function(string& s)
{
    int m = (int)s.size();
    vector<int> pf(m);
    
    int mx = 0;
    
    for (int i = 1; i < m; i++) {
        int k = pf[i-1];
        while (k > 0 && s[i] != s[k])
            k = pf[k-1];
        if (s[i] == s[k])
            k++;
        pf[i] = k;
        mx = max(mx, pf[i]);
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
    
    for(int i = 0; i < n; i++) {
        t += s[i];
        temp = t;
        reverse(temp.begin(),temp.end());
        unique_substr += (int)t.size() - prefix_function(temp);
    }
    
    // Total number of unique substrings
    cout << unique_substr << endl;
    
    return 0;
}
```

**Complexity**: $O(N^2)$, where $N$ is the length of $s$.

For each character appended, we are computing prefix function in $O(N)$, which gives a time complexity of $O(N^2)$ in total.
