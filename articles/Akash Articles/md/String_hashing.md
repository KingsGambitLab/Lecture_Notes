String Hashing and Rabin Karp
Prerequisites: Prefix sums, Modular Arithmetic

# String Hashing

All the data we store on a computer is either numbers or character strings or complex form of them.

We store data and retrieve it when needed. It becomes very expensive-in terms of time and computational power-to find out the needed data from a very large pool of data.

Usually, data can be considered as a key-value pair. The key part is used when we are searching for the data and the value part contains the information related to it(key).

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/String%20Hashing/sh1.png)

Key-the main part to search the required data-can be an integer or a string. For example, in the English dictionary we have string-keys but students' data accessible using their registration numbers has integer-keys(reg. no.).

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/String%20Hashing/sh2.png)

Now, what is the complexity of comparing two integers in terms of asymptotic notation?

Answer: $O(1)$

What about comparing two strings of the same length $n$?

Answer: $O(n)$

A basic way to find required data requires a comparison of keys. So, It is always preferred to have keys as an integer, because we can compare any two integers in $O(1)$ but comparing large strings has bad performance.

But what if we can turn a string-key to an integer-key?

The mechanism to turn a string into an integer is known as **"String Hashing"**. We need a hash function to do so.

Let say $\text{hash}(s)$ function returns hash(integer) of the provided string($s$). Generally, we want to map strings to numbers on a fixed range $[0,m)$, so that **string comparison turns to an integer comparison($O(1)$)**.

Our goal is only satisfied if hash function returns $\text{hash}(s) \neq \text{hash}(t)$, for different strings $s \neq t$. Because otherwise, it will create problems like we may end up comparing two different strings as same strings because their hashes are same.

When the hash function returns same hash for different strings, It is called a **"collision"**. We will discuss it soon, but let's first see how do we calculate a hash.

## How to calculate a hash for a given string?

There are many complex hashing functions to find hash of a string, but **polynomial rolling hash method** is widely used. Its formula is as below:

$\text{hash}(s) = (s_0 + s_1 \cdot p + s_2 \cdot p^2 + ... + s_{n-1} \cdot p^{n-1}) \mod m = (\sum_{i=0}^{n-1} s_i \cdot p^i) \mod m$

What are $s_i$, $p$ and $m$?
1. $s_i$ is the hash of character at the $i^{th}$ index in $s$. For example, string having only lower case characters we calculate hash as `s[i]-'a'+1`. Ex. `'a'->1`, `'b'->2`, `'c'->3`, ....
    Note that if we take a hash of `'a'` as $0$, then all strings `"a"`, `"aa"`, `"aaa"`, `"aaaa"`, ... will have the same hash-0, which will create problems.
2. $p$ is a prime number, which is taken to be greater than the number of distinct characters we are expecting in a string. $31$ in case of only lowercase characters and $53$ in case of lowercase and uppercase characters both.
3. $m$ is also a prime number, which is chosen such that we can handle integer overflows(using `long long`). Generally, it is taken to be $10^9+7$ or $10^9+9$.

Proper choice of $p$ and $m$ help us to avoid collisions.

```cpp
long long hash(string& s) {
    int p = 31;
    int m = 1e9 + 9;
    long long Hash = 0;
    long long p_pow = 1;
    for (char c : s) {
        Hash = (Hash + (c - 'a' + 1) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    }
    return Hash;
}
```

## How to minimize collision probability?

For $m$ around $10^9$, the collision probability for two string is $\approx 10^{-9}$, which is quite low.

But as the number of strings increases, let say we are evaluating hashes of $10^6$ different strings and comparing them with each other, then the probability of at least one collision happening is almost $1$. This almost guarantees that at least one collision will occur and we may end up with wrong results.

**Usually, in competitive programming environment it works fine.**

But, how to decrease collision probabilities?

One easy way: we can just compute two different hashes for each string (by using two different $p$ and/or different $m$) and **compare their pairs** instead. It decreases the probability to around $10^{-6}$, which was around $1$ before.

## How to find and compare hashes of substrings?

Suppose we want to compare two substrings, we can find their hash and compare easily. Now, what if we are given too many queries for substrings comparisons? Can we use the prefix-sum method here as well?

Yes. In simple prefix-sums, we can find subarray sum in $O(1)$ after precomputation of prefix-sums. Now, note that to find a hash of a string we are also doing the overall sum of terms of form $s_i*p^i$.

Therefore, here we will store prefix-sums of these terms, i.e. at the $i^{th}$ index the value will be,

$h[i] = (\sum_{j=0}^{i-1} s_j \cdot p^j) \mod m, i \in [1,n]$

$h[0]$ will be $0$, as in usual prefix-sums.

Given string "$s_0s_1s_2s_3s_4s_5$", we want to compare two substrings "$s_0s_1s_2$" and "$s_3s_4s_5$". Simple formula of hashing for "$s_0s_1s_2$" will be $((s_0+s_1*p+s_2*p^2) \mod m)$ and for "$s_3s_4s_5$" will be $((s_3+s_4*p+s_5*p^2) \mod m)$.

Now, how can we use prefix-sums to find the above hashes effectively?

For "$s_0s_1s_2$" substring, $h[3]$ already have value $(s_0+s_1*p+s_2*p^2) \mod m$, but for "$s_3s_4s_5$" substring (same as prefix-sums) here $h[6]-h[3]$ gives, $(s_3*p^3+s_4*p^4+s_5*p^5) \mod m$. But actual value we want is $(s_3+s_4*p+s_5*p^2) \mod m$.

Now, there are two ways to compare these hashes, 
1. Multiply $((s_0+s_1*p+s_2*p^2) \mod m)$ by $p^3$ to get $((s_0*p^3+s_1*p^4+s_2*p^5) \mod m)$
2. Divide $((s_3*p^3+s_4*p^4+s_5*p^5) \mod m)$ by $p^3$ to get $((s_3+s_4*p+s_5*p^2) \mod m)$-in modular arithmetic sense it means to multiply by modular inverse of $p^3$.

Either of these methods brings down the comparisons to usual hash comparisons-$(((s_0+s_1*p+s_2*p^2) \mod m)$ == $((s_3+s_4*p+s_5*p^2) \mod m))$-we want.

```cpp
int p = 31;
int m = 1e9 + 9;

string s = "abcabc";
int n = s.size();

vector<long long> p_pow(n);
p_pow[0] = 1;

// Precomputation of all powers
for (int i = 1; i < n; i++) 
    p_pow[i] = (p_pow[i-1] * p) % m;

// Prefix sums
vector<long long> h(n + 1, 0); 
for (int i = 0; i < n; i++)
    h[i+1] = (h[i] + (s[i] - 'a' + 1) * p_pow[i]) % m;

if((h[6] - h[3] + m) % m == h[3] * p_pow[3] % m) {
    cout << "equal substrings" << endl;
}
```

Similarly, we can do it for any substring.

Let say, you want to compare "$s_1s_2s_3s_4$" and "$s_7s_8s_9s_{10}$" substrings, then you should compare `(h[5] - h[1] + m ) % m` and `((h[11] - h[7]) * p_pow[7-1]) % m`

This is how we can find and compare the hash of substrings efficiently.

## Rabin-Karp Algorithm

Rabin-Karp algorithm is an algorithm to find all occurrences of a pattern(or substring)`p` into a larger string `s` using the string-hashing method. For example, `p = "ab"` and `s = "abbab"`, then $0$ and $3$ are indexes where p is present as a substring.

Can you figure out how to do so using string hashing?

We are going to compare the hash of all substrings of `s` having the same length as `p` one by one, with the hash of `p`. If the hash matches, then it is an occurrence of `p` and so on. 

We will use the same method as discussed before, to find hashes of substrings efficiently.

```cpp
vector<int> Rabin_Karp(string& s, string& p) {
    int p = 31; 
    int m = 1e9 + 9;
    int s_sz = s.size(), p_sz = p.size();

    int mn = max(s_sz, p_sz);
    vector<long long> p_pow(mn);
    p_pow[0] = 1;

    // Precomputation of all powers
    for (int i = 1; i < mn; i++) 
        p_pow[i] = (p_pow[i-1] * p) % m;

    // Prefix sums
    vector<long long> h(s_sz + 1, 0);
    for (int i = 0; i < s_sz; i++)
        h[i+1] = (h[i] + (s[i] - 'a' + 1) * p_pow[i]) % m;
    
    // Compute hash of s
    long long hash_p = 0;
    for (int i = 0; i < p_sz; i++) 
        hash_p = (hash_p + (p[i] - 'a' + 1) * p_pow[i]) % m;

    vector<int> occurrences_id;
    for (int i = 0; i + p_sz - 1 < s_sz; i++) { 
        long long cur = (h[i+n] + m - h[i]) % m; 
        if (cur == hash_p * p_pow[i] % m)
            occurrences_id.push_back(i);
    }
    return occurrences_id;
}
```

### Time complexity

$O(|s| + |p|)$, where s is the length of larger string and p is the length of the pattern string.

$O(|p|)$ is required for calculating the hash of the pattern and $O(|s|)$ for comparing the hash of each substring of length $|p|$ with the hash of the pattern.

## Check whether the substring is a palindrome

You are given left($l$) and right($r$) indices of a substring, you are required to check whether the given substring is palindrome or not.

We will simply compare hashes of two half parts of substring. Hashes are same means that two half parts are same and substring is a palindrome.

If there are many queries of this type, then each query can be answered in $O(1)$, after $O(n)$ preprocessing.

```cpp
#include <bits/stdc++.h>
using namespace std;
int m = 1e9 + 9;
int p = 31;

// 0-based indices
bool ispalindrome(int l, int r, vector<long long>& h, vector<long long>& p_pow)
{
    // length = 1 is always palindrome
    if(r - l == 0)
        return true;
    int len = r - l + 1;
    int half = len / 2;
    
    // Hash of two halfs
    int firsthalf = (h[l + half] - h[l] + m) % m;
    int secondhalf = (h[r + 1] - h[r - half + 1] + m) % m;
    
    // Take care about powers
    if((firsthalf * p_pow[r - half - l + 1] % m) == secondhalf)
        return true;
    else 
        return false;
}

int main()
{
    string s = "ooopooo";
    int n = s.size();

    int mn = n;
    vector<long long> p_pow(mn);
    p_pow[0] = 1;

    // Precomputation of all powers
    for (int i = 1; i < mn; i++) 
        p_pow[i] = (p_pow[i-1] * p) % m;

    // Prefix sums
    vector<long long> h(n + 1, 0);
    for (int i = 0; i < n; i++)
        h[i+1] = (h[i] + (s[i] - 'a' + 1) * p_pow[i]) % m;

    cout << ispalindrome(0, 6, h, p_pow) << endl;

    return 0;
}
```

## Number of unique substrings

The idea here is to compute hashes of each substring of same length and find the number of unique hashes, which can be easily done using data structures like `set` and do this for every possible substring-lengths i.e. $\text{length} \in [1,n]$.

```cpp
int count_unique_substrings(string const& s) {
    int p = 31;
    int m = 1e9 + 9;
    int n = s.size();
    
    vector<long long> p_pow(n);
    p_pow[0] = 1;
    for (int i = 1; i < n; i++)
        p_pow[i] = (p_pow[i-1] * p) % m;

    vector<long long> h(n + 1, 0);
    for (int i = 0; i < n; i++)
        h[i+1] = (h[i] + (s[i] - 'a' + 1) * p_pow[i]) % m;

    int cnt = 0;
    for (int len = 1; len <= n; len++) {
        set<long long> hash_set;
        for (int i = 0; i <= n - len; i++) {
            long long cur_h = (h[i + len] + m - h[i]) % m;
            cur_h = (cur_h * p_pow[n-i-1]) % m;
            hash_set.insert(cur_h);
        }
        cnt += hash_set.size();
        hash_set.clear();
    }
    return cnt;
}
```

**Time Complexity:** $O(n^2\log(n))$ : $O(n^2)$ is to find indices of each substring and finding hash in $O(1)$. $O(\log(n))$ is taken to insert a hash in the set.
