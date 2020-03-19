# Miscelleneous Problems 20

## Balls in Boxes
### Problem Statement
Given an array of integers **A** of size **N** and an another array of strings **B** of size **N**. Each string in **B** is binary and of exact size **10**.

There are some Boxes having following characterstics:-
```
    A[i] represents the cost of ith Box.
    One Box can contain atmost 10 different colored balls in it.
    B[i][j] = '1' indicates that ith Box contains jth colored ball.
    B[i][j] = '0' indicates that ith Box doesn't contains jth colored ball.
```

Find and return **minimum** amount of money needed to buy the boxes such that you have **maximum distinct colored balls** in the end.

**Input Format**
```
    The first argument given is the integer array A.
    The second argument given is the string array B.
```    
**Output Format**
```	
	Return minimum amount of money needed to buy the boxes such that you have maximum distinct 
  colored balls in the end.
```

**Constraints**
```
    1 <= N <= 10000
    0 <= A[i] <= 10^9
    B[i][j] = {'0' ,'1'}
```    
**For Example**
```
	Example Input 1:
	    A = [20, 10, 9]
	    B = ["0110001010", 
      "0111110000", "1111111111"]
    Example Output 1:
	    9
	Example Explanation 1:
	    As box 3 contains balls of all colors, buying only this box is sufficient.
	
	Input 2:
	    A = [20, 10, 9]
	    B = ["0110001010", 
      "0111110001", "1111111110"]
    Output 2:
	    19
``` 
### Brute Force
- We can consider all subsets of boxes. For each subset we can calculate the total number of distinct balls and total cost to buy.
- Now, we can find the minimum cost among all the subsets with maximum distint balls.
- This approach will take $O(2^A \times A)$

### Hints
- With the brute force we are taking subsets of boxes. Can we take subsets of balls?
- For a given subset of balls we have to find the minimum cost to get that subset using first i boxes.
- At a given dp state, we have two variables a mask and an index. Now, we have the choice either to take index'th box or not to take it. 
- We can calculate the maximum possible distinct balls. Now, after running the loop if we find that the number of ones in the mask is less than maximum we can set that dp to be Infinity. This will make sure that we ignore all the cases where our 1-count will be less than max possible.

### Code
```C++
#include <iostream>
#include <cstdio>
#include <cassert>
#include <fstream>
#include <set>
#define lli long long
#define MAX 10004
#define INF 10000000000000000LL
using namespace std;
int mx;
lli A[MAX];
int val[MAX];
bool vis[MAX][1024];
lli dp[MAX][1024];
int n;
void validate(string s)
{
    int sz = (int)s.size();
    assert(sz == 10);
    for ( int i = 0; i < 10; i++ ) assert(s[i] == '0' || s[i] == '1');
}
lli f(int idx, int mask)
{
    if ( idx == n ) {
        if ( __builtin_popcount(mask) == mx ) return 0;
        return INF;
    }
    if ( vis[idx][mask] ) return dp[idx][mask];
    vis[idx][mask] = true;
    lli ans = min(f(idx + 1, mask), A[idx] + f(idx + 1, mask | val[idx]));
    dp[idx][mask] = ans;
    return ans;
}
int main()
{
    freopen("inp5.txt", "r", stdin);
    freopen("out5.txt", "w", stdout);
    string s;
    set <int> distinctBalls;
    cin >> n;
    assert(n >= 1 && n <= 10000);
    for ( int i = 0; i < n; i++ ) {
        cin >> A[i];
        cin >> s;
        assert(A[i] >= 0 && A[i] <= 1000000000);
        validate(s);
        for ( int j = 0; j < 10; j++ ) {
            if ( s[j] == '1' ) distinctBalls.insert(j), val[i] |= (1 << j);
        }
    }
    mx = (int)distinctBalls.size();
    cout << f(0, 0) << endl;
    return 0;
}
```
### Time Complexity
- Since we are calculating the every dp state only once. The time complexity will be $O(n \times 2^{10})$.

### Dry Run
- Let's say we have only two colors.
- N = 3
- A = {5, 10, 20}
- B = {10, 01, 11}
|Mask|Index|Dp|Expression(min)|
|:--|:--|:--|:--|
|00|0|15 |dp[1][00],A[0](=5) + dp[1][10]|
|00|1|20 |dp[2][00],A[1](=10) + dp[2][01]|
|10|1|10 |dp[2][10],A[1](=10) + dp[2][11]|
|00|2|20 |dp[3][00],A[2](=20) + dp[3][11]|
|01|2|20 |dp[3][01],A[2](=20) + dp[3][11]|
|10|2|20 |dp[3][10],A[2](=20) + dp[3][11]|
|11|2|0 |dp[3][11],A[2](=20) + dp[3][11]|
|00|3|INF||
|01|3|INF||
|10|3|INF||
|11|3|0| |


## The Ghost Type

### Problem Statement
Gengar has got an integer **A**. Now using his ghostly powers, he can create the permutation from **1** to **A** of this given number.

Since, he's a special kind of Poke'mon, so he thinks he deserves special permutations. He wants to find the total number of special permutations of length **N**, consisting of the integers from **1** to **A**.

A permutation is called special if it satisfies following condition:

If **P<sub>x</sub> & P<sub>y</sub> == P<sub>x</sub>**, then **x** < **y**, where **x** and **y** are two distinct indices of permutation and **P** is the permutation itself. "**&**" denotes the bitwise and operation.

Help Gengar in finding the number of such permutations.

**Input Format:**
```
    First and only argument of 
    input conatins a single integer A
```
**Output Format:**

    Ouput a string denoting the answer.

**Constraints:**

    1 <= A <= 20

**For Example:**
```
Example Input 1:
   A = 3
Example Output 1:
   2
Explanation 1:
    Special Permutation are: [1, 2, 3] and [2, 1, 3]
Example Input 2:
    A = 4
Example Output 2:
    8
```
### Brute Force
- Given a permutation we can check in $O(n^2)$ time whether it is special or not. 
- We can consider all the permutations of $1...A$. Then we can count special permutations.
- This approach will take $O(2^n \times n^2)$.
### Hints
- If we look at a subset of numbers which are already there in the permutation from $1...i$, we can choose the next number to include. 
- Next element to include will be one whose all x's are included.
- Thus if we start from an empty subset, we can build the complete set in buttom up manner.
### Code
```C++
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll  long long int
#define pi pair<ll,ll>
#define pii pair<ll,pi>
#define f first
#define mp make_pair
#define mod 1000000007
#define s second
#define pb push_back
vector<int>submask[22];
bool vis[1<<22];
ll dp[1<<22];
int N;
ll rec(int mask){
    if(mask==(1<<(N+1))-2) return 1;
    if(vis[mask]) return dp[mask];
    vis[mask] = 1;
    ll &ret = dp[mask];
    ret=0;
    int x;
    for(int i=1;i<=N;i++){
        if(!(mask&(1<<i))){
            bool ok = true;
            for(int j = 0; j < submask[i].size(); j++){
                x = submask[i][j];
                if(!(mask&(1 << x ))) ok=false;
            }
            if(ok){
                ret += rec(mask|(1<<i));
            }
        }
    }
    return ret;
}
int main(){
    for(int i=1;i<=20;i++){
        for(int j=i-1;j>=1;j--){
            if( (i&j)==j ) submask[i].pb(j);
        }
    }
    cin >> N;
    cout<<rec(0);
}
```
### Time Complexity
- We are running a loop of $O(n)$ for every mask. For every candidate we need to check with all its x's. That will also take $O(n)$ time.
- Thus the total time will be $O(n! \times 2^n)$.

### Dry Run
- N = 4
- Submask
  - 1(001) : {}
  - 2(010) : {}
  - 3(011) : {1,2}
- Dp
|Mask|Expression|Dp Value|
|000|dp[001] + dp[010]|2|
|001|dp[011]|1|
|010|dp[011]|1|
|011|dp[111]|1|
|111| | 1|
## Micro and Lucky Tree

### Problem Statement
Micro purchased a tree having **A** nodes numbered from **1** to **A**. It is rooted at node numbered **1**. But unfortunately that tree turned out to be bad luck. After he purchased that tree, he lost his job and girlfriend. So he went to his astrologer friend Mike for help.

Mike told him to assign a value in the range **1** to **B** (inclusive) to each node making sure that luck factor of all leaf nodes is **1**. Luck factor of a leaf node **v** is defined as *gcd* of values of all nodes lying in path from root to **v** (inclusive). Now Micro wants to know how many ways are there to make his tree lucky. That's where Mike failed, so he asked for your help.

**Input Format:**
```
First argument of input is a integer A
Second argument of input is a integer B
Third argument of input is an integer array C of size A. where C[i] denote the parent of i+1 th 
node. C[0] = 1
```
**Output Format:**
```
    Return a single integer denoting 
    answer mod 1000000007
```
**Constraints:**
```
    1 <= A <= 50000
    1 <= M <= 30
    1 <= C[i] <= A
```
**For Example:**
```
Example Input 1:
    A = 3, B = 2, C = [1, 1, 1]
Example Output 1:
    5
Explanation 1:
    possible values of node1, node2, 
    node3 are:
    (2, 1, 1)
    (1, 1, 2)
    (1, 2, 2)
    (1, 1, 1)
    (1, 2, 1)
Example Input 2:
    A = 4, B = 3, C = [1, 3, 1, 3]
Example Output 2:
    71
```
### Brute Force
- We can take all arrangements and test the conditions by doing a traversal on the tree. This will take  $O(n)$ per arrangement.
- This approach will take $O(A^B \times A)$.

### Hints
- If we can calculate the number of arrangements possible, for a sub tree rooted at a given node, we can solve this question.
- All we need to know is the gcd of all the numbers till that node.
### Code
```Python
dfs(from, g)
{
    if DP[from][g] != -1:            
    // If we have already computed the values we will just return it
        return DP[from][g]
    if node from is a leaf:
        ret = 0
        for i from 1 to m:           // Trying all the possible values at leaf 
            if gcd(i, g) == 1:       // and checking number of integers, i,  assigned at leaf
                ret = ret + 1        // such that gcd(i, j)=1
        dp[from][g] = ret
        return ret
    ret = 0
    for i from 1 to m:                // Trying all the possible values at node i (from 1 to m)
        g1 = gcd(i, g)                //  and compute the GCD of values of all nodes lying in path from 1 to i
        ways = 1                    //  and pass it in the DFS call to children of i
        for to = children of node from    // Computing the value \(DP\) of the node
            ways = (ways * dfs(to, g1))   // by multiplying the values of the children
        ret = (ret + ways)
    dp[from][g] = ret
    return ret
}
```
### Time Complexity
- $O(A \times B)$.

### Dry Run
```
Tree:
      1
     / \
    2   3
```
B = 3
```
      1   -> 9
      2   -> 4
      3   -> 4
      ---------
            17
```