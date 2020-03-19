# Miscelleneous Problems 13

## Game Of Ways

### Problem Statement

Batman is about to take off from Gotham’s airport which has m runways(numbered from 1 to m) of length n units.
As always, the Joker has come up with an insane game to have fun with Batman.


The rules of the game are as follows::

 - Batman’s plane can take off only after running for n-units distance in the runways. 
 - Batman can start on any runway and end on any runway.
 - Batman can switch his plane from runway i to j only if i and j  are coprime. 
 - If the batman fails to switch his plane to a coprime runway, after running for 1 unit distance on a single runway, the Joker will bomb the plane.

The Joker does not want to kill the batman, because what will he do without him. So he asks for your help to find out number of ways in which Batman can take off his plane without getting bombed.

As the answer can be very large, output answer modulo (1000000007)

----------

**Input Format**
```
First argument given is an Integer A, Length of the runway.
Second argument given is an Integer B, 
Number of different runways available
```
    
   
**Output Format**
```	
Return a single integer X, the number of ways Batman can take off his plane without getting bombed.
As X can be very large, return X MOD 10^9+7
```    
**Constraints**
```
1 <= A <= 1000000000
0 <= B <= 10
```
**For Example**
```C++
Input 1:
    A = 1
    B = 3
  Output 1:
    3

Input 2:
    A = 2
    B = 3
  Output 1:
    7

Explanation:
  For test 1:
      3 Ways Starting at 1, 2, 3

  For test 2:
      1st way: starting and covering whole distance at runway 1.
      i.e 1 -> 1 (1 and 1 are co-prime so Batman can continue on
      runway 1 without getting bombed)
      2nd way: starting and covering distance of 1 at runway 1 
      and covering remaining distance at runway 2. i.e 1 -> 2
      3rd way: starting and covering distance of 1 at runway 1 
      and covering remaining distance at runway 3. i.e 1 -> 3
      similarly there are 4 more ways i.e 2 -> 1, 2 -> 3, 3 -> 
      1, 3 -> 2

      we can't go from 2 -> 2 and 3 -> 3 as per given rules.
```
### Brute force
- Generate all permutations of 1,...,B of size A. 
- Check if all the consicutive elements are co-prime. Count all such permutations.
- Time Complexity: B^A.

### First Approach
- It should be clear from the question that we need a graph of size B. 
- Let's apply dynamic programing on this graph.
- Let dp[i][k] be the number of ways to start at i and run a length of k. 
- dp[i][1] = 1 for all i.
- $dp[i][k] = \sum_{j \in adj[i]}dp[j][k-1]$

**Code**
```C++
int gcd(int i, int j){
    if(i>j) return gcd(j,i);
    else if (i == 0) return j;
    else{
        int k = j%i;
        return gcd(k, i);
    }
}

bool coPrime(int i, int j){
    return gcd(i,j) == 1;
}
void printArray(vector<vector<int>> adj){
    for(int i = 0 ; i<adj.size(); ++i){
        cout << i << ": " ;
        for(auto cell: adj[i]){
            cout << cell << " ";
        }
        cout << endl;
    }
}
int Solution::solve(int A, int B) {
    if(A == 0) return 0;
    vector<vector<int>> adj(B);
    for(int i = 0; i< B; ++i){
        for(int j = i ; j<B; ++j){
            if(coPrime(i+1,j+1)){
                adj[i].push_back(j);
                if(i!=j){
                    adj[j].push_back(i);
                }
            }
        }
    }
    //printArray(adj);
    vector<int> dp_old(B);
    vector<int> dp_new(B);
    for(int i = 0; i < B; ++i){
        dp_new[i] = 1;
    }
    int mod = 1000000007;
    for(int k = 2; k<=A; ++k){
        dp_old = dp_new;
        for(int i = 0; i< B; ++i){
            dp_new[i] = 0;
            for(auto j : adj[i]){
                dp_new[i] += dp_old[j]%mod;
                dp_new[i] %= mod;
            }
        }
    }
    int res= 0;
    for(int i= 0; i<B; ++i){
        res += dp_new[i]%mod;
        res %= mod;
        
    }
    return res;
}
```
### Second Approach(Matrix Exponentiation)
- If we look at the adj matrix, $A$ and its powers, we find some nice patterns.
  - $A^1[i][j]$ will be 1 if there is an edge between i and j.
  - $A^2[i][j] = \sum_{k \in\{0,n-1\}}A^1[i][k]* A^1[k][j]$
  - $A^2[i][j]$ will have number of paths of size two between i and j.
  - $A^4[i][j] = \sum_{k \in\{0,n-1\}}A^2[i][k]* A^2[k][j]$
  - $A^4[i][j]$ will have number of paths of size four between i and j.
  - In general $A^n[i][j]$ will have number of paths of size n between i and j.
- If our track length is t, then $\sum_{i,j \in\{0,n-1\}}A^t[i][j]$ will be give us all the possible paths of length t.

**Code**
```C++
#define ll long long int

int mod = 1000000007;
int gcd(int i, int j){
    if(i>j) return gcd(j,i);
    else if (i == 0) return j;
    else{
        int k = j%i;
        return gcd(k, i);
    }
}

bool coPrime(int i, int j){
    return gcd(i,j) == 1;
}
void printArray(vector<vector<ll>> adj){
    for(int i = 0 ; i<adj.size(); ++i){
        cout << i << ": " ;
        for(auto cell: adj[i]){
            cout << cell << " ";
        }
        cout << endl;
    }
}
void copy(vector<vector<ll>> &A, vector<vector<ll>> &B){
    int n = A.size();
    for(int i= 0; i<n ; ++i){
        for(int j = 0; j<n ;++j){
            B[i][j] = A[i][j];
        }
    }
}
void square(vector<vector<ll>> &A){
    int n = A.size();
    vector<vector<ll>> temp(n, vector<ll>(n));
    copy(A,temp);
    for(int i = 0; i<n ; ++i){
        for(int j = 0; j<n ;++j){
            A[i][j] = 0;
            for(int k = 0; k<n; ++k){
                A[i][j] = (A[i][j]%mod + ((temp[i][k]%mod)*(temp[k][j]%mod))%mod)%mod;
            }
        }
    }
}
void multiply(vector<vector<ll>> &A, vector<vector<ll>> &B){
    int n = A.size();
    vector<vector<ll>> temp(n, vector<ll>(n));
    copy(A,temp);
    for(int i = 0; i<n ; ++i){
        for(int j = 0; j<n ;++j){
            A[i][j] = 0;
            for(int k = 0; k<n; ++k){
                A[i][j] = (A[i][j]%mod + ((temp[i][k]%mod)*(B[k][j]%mod))%mod)%mod;
            }
        }
    }
}
void print(vector<vector<ll>> A){
    cout << "-------------" << endl;
    for(auto row: A){
        for(auto cell: row){
            cout << cell << " " ;
        }
        cout << endl;
    }
}
void pow_matrix(vector<vector<ll>> &adj,int A, vector<vector<ll>> &orignal){
    //print(adj);
    //cout << A << endl;
    if(A == 1) return;
    int n = adj.size();
    pow_matrix(adj, A/2, orignal);
    square(adj);
    if(A%2 == 1){
        multiply(adj, orignal);
    }
}

int Solution::solve(int A, int B) {
    if(A == 0) return 0;
    if(A == 1) return B;
    vector<vector<ll> > adj(B, vector<ll> (B,0));
    for(int i = 0; i< B; ++i){
        for(int j = 0 ; j<B; ++j){
                adj[i][j] = (coPrime(i+1, j+1))? 1: 0;
        }
    }
    int n = B;
    vector<vector<ll>> identity(n, vector<ll>(n,0));
    copy(adj,identity);
    pow_matrix(adj, A-1, identity);
    long long int sum = 0;
    for(int i= 0; i<B; ++i){
        for(int j = 0; j<B; ++j){
            sum = (sum%mod + adj[i][j]%mod)%mod;
            sum %= mod;
        }
    }
    return (int)sum;
}
```
## Subarray Transformations

### Problem Statement

Given an array A of size N **(1-indexed)** with all elements **initially 0**. You have to perform T transformations and return the **final** value of array.

Each transformation is of the form Xi , Yi.

In the ith transformation do the following operation Yi times,

**Subarray from index 1 to Xi is taken and choose the cell having minimum value and if there are many cells with same minimum value then choose cell having minimum index. Add 1 to the chosen cell.**

**Input**

```
2D array with 1st transformation as (array[0][0], 
array[0][1]),...Tth transformation as (array[T - 1][0], 
array[T - 1][1]).
```

**Output**

```
Return array of length N with arr[0] with value of 1st 
element,... arr[N - 1] with value of Nth element.
```

**Constraints**

```C++
1 <= N <= 1000
0 <= T <= 10000
1 <= Xi <= N
1 <= Yi <= 100000
```
### Brute Force
- We can find the minimum cell in $O(X)$. 
- In every step we have to increase it by one $Y$ times. This will in total take $O(X* Y)$.
- There are $T$ such updates. Thus it will take $O(X* Y* T)$ time.
- That will be $O(10^{12})$ it will give TLE.
- We are doing repetative work while increasing the minimum.

### Hints
- Observation: All nodes will be in non-increasing order.
- To find patterns in questions like these it is advisable to do a dry run on an small array.
- Initially, the array is all zeros. Let it be $[0,0,0,0,0]$
- X = 3, Y = 7
- $3,2,2,0,0$
- X = 5, Y = 6
- $3,2,2,2,2$, | Y = 2
- $3,3,3,2,2$, | Y = 0
- In first case we filled all nodes till $X$ by $Y/X$. And added 1 in $Y%X$ nodes.
- In second case we filled all nodes after 2 to level of 2. And then filled remaining $Y$ after 3.
- So, we will have two nodes $i,j$ such that if we fill all nodes after j the gain will be less than or equal to $Y$. And if we fill all nodes after i to level of i the gain will be greater than $Y$
- Here 
  - $i<j$ 
  - $A[i] > A[i+1]$
  - $A[j] > A[j+1]$
- We fill all the nodes after j to level of j. And fill nodes after $i$ like the first case.

### Code

```C++
bool isValid(vector<long long> psum, int i, int X, int Y, int h){
    long long sum = psum[X] - psum[i];
    return h*(X-i) - sum <= Y;
}
void update(vector<int> &array, int X, int Y){
    int n = array.size();
    vector<long long> psum(n,0);
    psum[0] = array[0];
    for(int i=1; i<n; ++i){
        psum[i] += psum[i-1] + array[i];
    }
    int h;
    for(int i = 0; i<=X; ++i){
        h = array[i];
        if(i<X && array[i] != array[i+1] && isValid(psum, i, X, Y, h)){
            for(int j = i+1; j <= X; ++j){
                Y -= h-array[j];
                array[j] = h;
            }
            break;
        }
    }
    int idx = 0;
    while(array[idx] != h){
        ++idx;
    }
    int layers = Y/(X-idx+1);
    int remaining = Y%(X-idx+1);
    for(int i = idx ; i <= X; ++i){
        array[i] += layers;
        Y -= layers;
        if(remaining > 0){
            array[i]++;
            Y--;
            remaining--;
        }
    }
    return;
}
vector<int> Solution::solve(int A, vector<vector<int> > &B) {
    vector<int> array(A,0);
    for(auto b : B){
        update(array, b[0]-1, b[1]);
    }
    return array;
}
```
### Time Complexity
- Since we are running a loop of size $O(X)$ twice for every update, $O(X* T)$.

## Sum of Inversions

### Problem Statement

Consider a random permutation P of numbers [1, 2, .., N]. This permutation is called special if there is no element P[i] in P such that **P[i] = i+1** (Consider 0 based indexing). In other words, a permutation is special if it is a derangement (no number is at its "natural" (ordered) place). 

Given a number N, find the sum of inversions in all the special permutations of numbers [1, 2, ..., N] modulo **1000000007**. An inversion in an array P is a pair P[i], P[j] such that P[i] > P[j] and i<j.

**Constraints:**
1 <= N <=  20

**Example:**

```C++
Input:
N = 3

Output: 
4

Explanation:
For N=3, special permutations are [3,1,2] and [2,3,1]
Number of inversions in [3,1,2] = 2   ( (3,1) and (3,2) )
Number of inversions in [2,3,1] = 2   ( (3,1) and (2,1) )
Thus, sum of inversions = 2+2 = 4.
```
-----------
### Brute Force
- We can create all the permutations.
- Check if they are derangements.
- And find inversions in them.
- This will take $O(n!* n\log{n})$ time.

### Hints
- When ever the brute force is of the order $n!$. Try to think of bit masking dp.
- In bit masking we represented the subset of a set of size n by a n-digit binary number.
- The benefit of this representation is that we can use that number as key in a hash map to store information about perticular sets.
- In this problem, the information that we want to store is the number of inverstions in all the special permutations of a given subset. We also need to store the number of special permutations of every given subset.
- Set bits in mask would be arranged at positions [idx, idx+1, ...., n]
- Here $ids = n - unset_bit + 1$
```C++
   int cnt = setbits_count(mask, n);   //no. of set bits in mask
    
    
    int idx = n-cnt+1;       //set bits in mask would be arranged at positions [idx, idx+1, ...., n]
    ll rank = 0;
    
    
    for(int i=0; i<n; i++){
        if(mask & (1<<i) ){    //if number i+1 is yet to be arranged
            if(idx != i+1){    //according to our rule, a number cannot be at its original index
                
                node temp = util(mask^(1<<i), n);       //arrange the number (i+1) and calculate the ans for resulting mask
                
                dp[mask].ans = (dp[mask].ans + 
                (temp.ans + ((temp.perm)*rank)%mod)%mod)%mod;    
                dp[mask].perm = (dp[mask].perm + temp.perm)%mod;
            }
            //rank = no. of numbers less than (i+1) in the mask
            //for mask 11010 -> rank in iteration i=3 in for loop is 1 which means
            // there is 1 number in the mask less than 4 (and that number is 2 in this case)
            rank += 1;
        }
    }
```
### Hints on Website
This type of problems requires a special DP formulation known as Bitmask DP. Those who are not familiar with the concept are advised to Google it before proceeding further.

Consider the following DP formulation:

mask = bitmask where i-th set bit from the left means number i is yet to be used in generating a special permutation.
e.g.: mask = 5 => mask = 101 (binary) => Current permutation 2 _ _.  Use  numbers [1,3] to fill the blanks in the current permutation.
 
cnt = no. of unset bits in mask (mask = 5 => mask = 101 (binary) => no. of unset bits = 1)

dp[mask] = sum of inversions of all the special permutations that can be generated using the numbers corresponding to set bits in mask such that the numbers should be arranged at positions [cnt+1, cnt+2, .., N] 

e.g.: 
mask = 101
One number is already fixed at position 1 and that number is 2. Permutation generated till this point is 2 _ _. Now we have to arrange the remaining numbers [1,3] at blank positions and form a special permutation. 

Recursion tree for N = 3 looks like following:

```
                111
    /           |              \
  011(1__)   101(2__)         110(3__)
              /   \             /     \
            001   100         100     010
           (21_) (23_)       (32_)    (31_)
```

Here, 011 at level 2 in the tree is not extended further as it is not a valid permutation (011 corresponds to permutation 1 _ _  and 1 cannot be at its correct position according to our rule of special permutations). Similarly  "100" (child of "110" in level 3) is also not a valid permutation as that corresponds to permutation 32_.  
This type of formulation will require us to ignore the branches of tree that form a non-valid permutation and consider those which forms a valid permutation. Now, the only challenge is to count the sum of inversions at every node of the tree. This is left as an exercise to the reader. Coding part is very easy once you have thought of a way to augment the recursion tree to store necessary information.

Time complexity of this approach would be O(C*N*(2^N)) which is much less than O(N!).

For any given N, our answer is simply dp[(1<<N)-1].
For N=3, our answer is dp[7]   ( 7 = "111" in binary)

**Code**
```C++

#define mod 1000000007
#define maxn 20
#define ll long long

//Node to store the information of a state in dp
struct node{
	ll perm;
	ll ans;
	bool vis;
	node(): perm(0), ans(0), vis(0){}
}dp[1<<maxn];

//count the number of set bits in mask 
int setbits_count(int mask, const int n){
	int cnt = 0;
	for(int i=0; i<n; i++){
		if(mask & (1<<i)) cnt++;
	}
	return cnt;
}


node util(int mask, const int n){
	//Check if this subproblem is already solved
	if(dp[mask].vis != 0) return dp[mask];
	
	//base case
	if(mask == 0){
		dp[mask].perm = 1;
		dp[mask].vis = 1;
		return dp[mask];
	}
	
		
	int cnt = setbits_count(mask, n);   //no. of set bits in mask
	
	
	int idx = n-cnt+1;       //set bits in mask would be arranged at positions [idx, idx+1, ...., n]
	ll rank = 0;
	
	
	for(int i=0; i<n; i++){
		if(mask & (1<<i) ){    //if number i+1 is yet to be arranged
			if(idx != i+1){    //according to our rule, a number cannot be at its original index
				
				node temp = util(mask^(1<<i), n);       //arrange the number (i+1) and calculate the ans for resulting mask
				
				dp[mask].ans = (dp[mask].ans + (temp.ans + ((temp.perm)*rank)%mod)%mod)%mod;    
				dp[mask].perm = (dp[mask].perm + temp.perm)%mod;
			}
			//rank = no. of numbers less than (i+1) in the mask
			//for mask 11010 -> rank in iteration i=3 in for loop is 1 which means
			// there is 1 number in the mask less than 4 (and that number is 2 in this case)
			rank += 1;
		}
	}
	
	dp[mask].vis = 1;
	
	return dp[mask];
}

int Solution::solve(int n){
	int mask = (1<<n) - 1;    //initial mask --> 111...1  "n ones"
	
for(int i=0; i< (1<<n); i++){
		dp[i].ans = 0;
		dp[i].perm = 0;
		dp[i].vis = 0;
	}

	return util(mask , n).ans;
}

```

### Dry Run
- A = 3
- 100 0 0
  001 0 1
  101 1 1
  010 0 1
  011 0 1
  111 4 2
- 111 4 2
  - 101 1 1
    - 100 0 0
    - 001 0 1
  - 011 0 1
    - 010 0 1

### Time Complexity
- $O(n* 2^n)$
