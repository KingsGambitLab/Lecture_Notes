# Miscelleneous Problems 14

## Valuable Nodes
### Problem Statement
Given a tree T containing N nodes numbered [1,2, ..., N] rooted at node 1. Each node has a value associated with it. You need to choose some of the nodes from the tree such that the sum of values of the chosen nodes is maximum possible. Moreover, if you have chosen a node V you cannot choose any of its children or grand children.
In simple words, you have to choose a subset of nodes such that no two nodes in the chosen set have a parent-child relation or grandfather-grandchild relation between them.

**Constraints:**
1 <= N <= 500,000
1 <= value of node <= 10,000

**Input:**

```
vector<int> A : A[i] --> Parent of node number i+1. 
                (A[2] = 1 means parent of node number 3 is 1).
vector<int> B : value[i] --> value associated with 
                node number i+1.

Note: Parent of node number 1 is 0 (A[0] = 0).
```
**Output:**
A number containing the maximum possible sum. 
`(As the answer can be large, output the answer modulo 1000000007)`

**Example:**

```
Input:
A : [0, 1, 1, 1, 3, 3, 6, 6]
B: [1, 2, 3, 4, 5, 100, 7, 8]

Output:
111 
Node number 2, 4, 5 and 6 are chosen. Sum = 2 + 4 + 5 + 100 = 111
```
### Brute Force
- The absolute brute force would be to take every subset.
- Check if it contains a child-parent or grandchild-grandparent relationship.
- Maximize the sum of values among these subsets.

### Hints
- Can we optimize the above brute force?
- We can select the node only if its child and grandchild are not selected.
- Can we reduce this problem to an array problem? That array problem will look as follows:
  - You are given an array. There is a value stored at every cell. You need to find a subset with highest value sum. If you include A[i] into the set, you cannot include A[i-2], A[i-1], A[i+1], and A[i+2] into the set.
- The above problem can be solved using Dynamic Programming. 
  - We can store, for all index i, the maximum value of a valid subset of A[0..i].
  - $dp[i] = max(dp[i-3]+A[i], dp[i-1])$
  - We just look at $dp[i-3]$ and $dp[i-1]$ as $dp[i-2]$ is already included in $dp[i-1]$.
- Can we apply a similar approach to our tree problem?

### Code
```C++
#define ll long long int
int mod = 1000000007;
int getMaxDP(int node, vector<vector<int>> &child, vector<vector<int>> &ggchild, vector<int> &dp, vector<int> &value){
    if(dp[node] != -1) return dp[node];
    int first = 0, second = 0;
    first = value[node]%mod;
    for(auto ggc: ggchild[node]){
        first = (first%mod + getMaxDP(ggc,child,ggchild,dp,value)%mod)%mod;
    }
    for(auto c: child[node]){
        second = (second%mod + getMaxDP(c,child,ggchild,dp,value)%mod)%mod;
    }
    return max(first, second);
}
int Solution::solve(vector<int> &A, vector<int> &B) {
    int n = A.size();
    vector<vector<int>> adj(n);
    vector<vector<int>> ggchild(n);
    vector<int> dp(n,-1);
    for(int i = 1; i<n; ++i){
        adj[A[i]-1].push_back(i);
    }
    for(int i = 0; i<n; ++i){
        for(auto c: adj[i]){
            for(auto gc: adj[c]){
                for(auto ggc: adj[gc]){
                    ggchild[i].push_back(ggc);
                }
            }
        }
    }
    return getMaxDP(0,adj,ggchild,dp,B);
}
```
### Time Complexity
- Since we are calculating every dp only once the time complexity will be $O(E+V)$. Since it is a tree the time complexity will be $O(n)$.
### Dry Run
```C++
A : [0, 1, 1, 1, 3, 3, 6, 6]
B: [1, 2, 3, 4, 5, 100, 7, 8]
Children:
1: 2,3,4
2: 
3: 5, 6
4:
5:
6: 7, 8
7:
8:
Great Grand Children
1: 7,8
2: 
3: 
4:
5:
6:
7:
8:
DP:
1: max(DP(2)+DP(3)+DP(4), B(1)+DP(7)+DP(8))
                  = max(2+105+4, 1+7+8) = 111
2: B(2) = 2
3: max(DP(5) + DP(6), B(3)) = max(100+5, 3) = 105
4: B(4) = 4
5: B(5) = 5
6: max(DP(7)+DP(8), B(6)) = max(7+8, 100) = 100
7: B(7) = 7
8: B(8) = 8
```

## String Rotation
### Problem Statement
Give a string S find lexicographically smallest string possible after circular rotation.

**Lexicographically smallest**: First string in dictionary order.

**Circular rotation**: Pushing the last character to the start.

**Input Format**
```
Argument 1: Length of the String
Argument 2: Given string
```

**Constraint**
```
0 < |S| <= 5000 
```
**Sample Input 1**
```
BCABDADAB
```  
**Sample Output 1**
```
ABBCABDAD
```
### Brute Force
- Consider all rotations and minimize over all of them.

### Hints
- This is a simple question included to encourage all of you to solve at least one problem.
- So, Go ahead and solve this question.

### Code
```C++
string Solution::solve(int A, string B) {
    string doubleB = B + B;
    set<string> s;
    for(int i = 0; i < A; ++i){
        s.insert(doubleB.substr(i,A));
    }
    return *s.begin();
}
```
### Time Complexity
- Each string comparision may take $O(n)$ time. Here, $n$ is the length of string.
- We have to compare strings $O(n)$ times. Thus the total time complexity will be $O(n^2)$.
- If we use a set, the time complexity will be $O(n^2\log{n})$. This is because insertion in set will take $O(n\log{n})$ time.

## Ways to Arrange Two Objects

### Problem Statement
You are given two types of objects : A and B. There is an infinite supply of both the type of objects . 
All the objects of type A are identical and same is the case with all the objects of type B. 

Given two integers N and L, find the number of ways in which you can arrange the N objects such that you don't have L or more 
consecutive objects of type A together.

**Constraints:**

```
1 < N < 100001

1 < L < 100001

1 < N*L < 100001
```

**Input Format**

```

Input consists on one line containing the value of N and L.
```

**Output Format**

```
Return number of ways modulo 10^9 + 7
```

**Example:**

```
Input:4 2

Output: 8

Explanation:

{B,B,B,B}

{B,B,B,A}

{B,B,A,B}

{B,A,B,B}

{A,B,B,B}

{A,B,A,B}

{A,B,B,A}

{B,A,B,A}
```
### Brute Force
- We can consider all the possible arrangements of A and B.
- For each arrangement, we can check if there are L consicutive A's. We can neglect those arrangements and count others.
- This approach will take $O(n * 2^n)$ time.

### Hints
- We can neglact some arrangements even before making them if at each i we keep count of consecutive A's ending at i. 
- Suppose there are L-1 A's ending at i. For example L = 3 and N = 6 and i = 3
  - ${B, A, A}$ now on the next step we can not include A.
- Can we memoize these states in dp?

### Solution
- Dp state: dp[i][j] number of arrangements of A and B of length i with j consicutive A's towards the end.
- $dp[i][0]=\sum_{k\in{[0,L-1]}}dp[i-1][k]$
- $dp[i][j]_{j>0} = dp[i-1][j-1]$
### Code
```C++
int mod = 1000000007;
int Solution::solve(int A, int B) {
    vector<vector<int>> dp(A+1, vector<int>(B,0));
    dp[0][0] = 1;
    for(int i = 1; i <= A; ++i){
        for(int j = 0; j< B; ++j){
            if(j == 0){
                int val = 0;
                for(int k = 0; k<B; ++k){
                    val = (val%mod + dp[i-1][k]%mod)%mod;
                }
                dp[i][j] = val;
            }else{
                dp[i][j] = dp[i-1][j-1];
            }
        }
    }
    int res = 0;
    for(int k=0; k < B; ++k){
        res = (res%mod + dp[A][k]%mod)%mod;
    }
    return res;
}
```
### Time Complexity
- It takes $O(1)$ time to calculate most of the dp states. There are $O(N)$ corresponding to $dp[i][0]$ that will take $O(L)$ time.
- There are $O(N* L)$ dp states. Thus the time complexity will be $O(N* L)$.
### Dry Run
N = 4, L = 2
|j->|0|1|
|:--|:--|:--|
|i = 0|1|0|
|1|1|1|
|2|2|1|
|3|3|2|
|4|5|3|
|Answer| 8||