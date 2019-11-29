# Miscelleneous Problems 15
## Bits and Bytes
### Problem Statement
You are given a binary string **S**.

You process it through a series of operations starting from the left where:  
    1) In the first operation, you remove the first bit of the number and append it to the right.  
    2) In the second operation, you remove the first 2 bits of the processed string one by one and append them to the right.  
    3) In the third operation, you now remove the first 3 bits of the new string one by one and append them to the right.  
    4) In the ith operation, you remove the first i bits of the new string one by one and append them to the right.

You have to find the minimum number of operations it takes to get back the original string.

Number of operations cannot be 0.

**Constraints:**

```
1 <= length of S <= 10^5
```

**Input:**

```
S : Binary string
```

**Output:**

```
Minimum number of operations to get back the 
original string.
```

**Example:**

```
Input: 
S: 111

Output:
1

In the first operation, the leftmost bit (1) 
gets appended to the end of the string, and you 
get the same string as the original, hence 
answer is 1.

Input: 
S: 101

Output:
2

In the first operation, the leftmost bit (1) 
gets appended to the end of the string, and you 
get the string 011.

In the second operation, the 2 leftmost bits get 
appended to the end (011 => 110 => 101), we get 
the same string as the original, hence answer is 
2.

```
### Brute Force
- For every i from 1 to $\infty$, We can rotate the string by i digits and check if the new string is same as the original string.
- Time Complexity, We may run into an infinity loop.
- Suppose we can be sure that we will get our result in $O(n)$. For every i we will need $O(n)$ time. So, the total time will be $O(n^2)$.

### Hints
- We can see that by $i^{th}$ operation we will have rotated $\frac{i*(i+1)}{2}$ times. Let's call this $T_i$.
- If for some $i$, $T_i$ is divisible by $len(s)$, we can say we will definetely get our string back.
- For $i = 2* len(s)-1$, $T_i$ will obviously be divisible by $len(s)$.
- So, we can run a loop from $1$ to $2* len(s) -1$ on $i$. And check if $T_i$ will be divisible by $len(s)$ or not.
- This will run in $O(n)$ time. 
- Will it give the smallest such i?
- The string may have a pattern repeating over and over again. For example : $s=101101101$, answer will be $2$.
- Can we find the length of the shortest repeating sequence? We can use KMP algorithm to do that. 
- What will be the lps of above string? Answer: $LPS = [001123456]$.
- If $len(s)-LPS[len(s)-1]$ divides $len(s)$, $len(s)-LPS[len(s)-1]$ is the length of the repeating sequence.
- Now, we have to match $T_i$ with length of repeating pattern if there is a repeating pattern.

### Code
```C++
typedef long long ll;

ll minLEN(string s,ll lps[]){
    lps[0]=0;
    ll len=0;
    ll p=1;
    while(p<s.length()){
        if(s[p]==s[len]){
            len++;
            lps[p]=len;
            p++;
        }else{
            if(len!=0){
                len=lps[len-1];
            }else{
                lps[p]=0;
                p++;
            }
        }
    }
    len=lps[s.length()-1];
    if(s.length()%(s.length()-len)==0){
        return s.length()-len;
    }else return s.length();
}

int Solution::minOperations(string A) {
    ll lps[200003];
    ll len=minLEN(A,lps);
    ll ans;
    for(ll i=1;;i++){
        if((i*(i+1)/2)%len==0){
            ans=i;
            break;
        }
    }
    return ans;
}
```
### Time Complexity
- $i$ ranges from $1$ to $2* len(s)$ in worst case. For each i we do constant amount of work. Thus the time complexity will be $O(n)$.
- KMP will take $O(n)$ additional time.

### Dry Run
```
s = 100100100
lps = [0,0,0,1,2,3,4,5,6]
length we need = 9-6 = 3
i = 2 , T_i = 3
answer = 2
```
## Conditional Swaps
### Problem Statement
Given an array A consisting of every number from 1 to N arranged in a random order.

It is also possible to swap a particular element at index i with an element at index i+1 for a particular set of indices.

The indices for which these swaps are allowed are given in the form of a string S of 1's and 0's.

If the i'th position of a string has 1, then it is possible to swap the i'th element of index with the (i+1)'th element else it is not allowed.

There is no limit on the number of swaps allowed, that is, you can make any number of swaps (as long as they are valid).

Find if it is possible to arrange the array in ascending order using any amount of swaps. 

**Constraints:**

```
1.   2 <= N <= 100000
2.   String S contains n-1 characters and is 
     made up of only 0's and 1's.
```

**Input:**
Integer N (size of array) , array of containing elements from 1 to N in random order, string S made up of 1's and 0's

**Output:**
Return a string "YES" if it is possible to arrange array in ascending order, else return "NO". 

**Example:**

Input: 

```
N:6
Array:[1 2 5 3 4 6]
S:01010
```

Function return:

```
NO
```
### Brute Force
- We can try to run bubble sort or insertion sort on the array based on the string S. 
- If in any step of bubble sort we encounter that we can not swap an element which needs to be swaped we output "NO". If we are able to sort the array, we output "YES".
- Time Complexity: $O(n^2)$.
### Hints
- Can we take element at position $i$ and bring it to position $j$ if there are $0's$ between $i$ and $j-1$? No.
- Numbers are between $1$ to $N$. So, we already know the exact position of every entry. 
- Can we not just check if the current position of an element and its sorted position are swapable? Yes
- Can we use prefix sum to do the above in $O(1)$ time? Yes
### Code
```C++
typedef int ll;
string Solution::solve(int A, vector<int> &B, string C) {
    ll n,use;
	    n=A;ll arr[n+1];
	   // cin>>use;
	    for(ll i=1;i<=n;i++)
	    {
		arr[i]=B[i-1];
	    }
	    string s,ans;
	    s=C;
	    ll pref[n];
	    pref[1]=s[0]-'0';
	    for(ll i=2;i<n;i++)
	    {
		pref[i]=pref[i-1]+s[i-1]-'0';
	    }
	    ll flag=0;
	    for(ll i=1;i<=n;i++)
	    {
    		ll temp=arr[i];
    		if(i<temp)
    		{
    		    if(i==1)
    		    {
    		        if(pref[temp-1]==temp-i or i==temp)
    		        continue;
    		        else
    		        {
    		            ans="NO";
    		            flag=1;
    		            break;
    		        }
    		    }
    		    else
    		    {
    		        if(pref[temp-1]-pref[i-1]==temp-i or i==temp)
    		        continue;
    		        else
    		        {
    		            ans="NO";
    		            flag=1;
    		            break;
    		        }
    		    }
    		}
    		else
    		{
    		        if(temp==1)
    		        {
    		            if(pref[i-1]==i-temp or i==temp)
    		                continue;
    		            else
    		            {
    		                ans="NO";
    		                flag=1;
    		                break;
    		            }
    		        }
    		        else
    		        {
    		            if(pref[i-1]-pref[temp-1]==i-temp or i==temp)
    		            continue;
    		            else
    		            {
    		                ans="NO";
    		                flag=1;
    		                break;
    		            }
    		        }
    
    
    		}


	    }
	    if(!flag)
	    ans="YES";
	    
	    return ans;
	    
}
```
### Time Complexity
- The above algorithm runs in $O(n)$ time.

### Dry Run
```
N:6
Array:[1 2 5 3 4 6]
S:01010
Sorted Position: [0 1 4 2 3 5]
Prefix Sum Array: [0 1 0 1 0]
```
|i|Sorted Position| Equal| Is it possible to Move|
|:--|:--|:--|:--|
|0|0|Yes|-|
|1|1|Yes|-|
|2|4|No|No|
|Break ||||
## Random Attendance
### Problem Statement
Dr. Dhruv is a superb professor of Mathematics. He is so lenient that he doesn't even take attendance. But his students are not so cooperative. 
Frustrating of all aspects is that students have stopped attending classes of Dr. Dhruv. Dr. Dhruv is really disappointed and he has decided to start taking attendance.  There are A students in his class. Ordinary professors take a roll call as [1, 2, 3, ..., A] but Dr. Dhruv is no ordinary man. He has come up with a different method of taking roll call. His method is as follows:

He has a list B of K random integers which means that he will call out only K students. He will first treat the numbers [1, 2, 3, .., A] as strings 
["1", "2", "3", .., "A"]. Then he will sort this vector of strings in lexicographic order (see example below). Now, Dr. Dhruv will call the numbers 
which are at B[i]-th (0 <= i < K) position in the sorted order (see example below).

Simply putting, if the sorted order is S, then he will call students in the order { S[B[0] - 1], S[B[1] - 1], ..., S[B[K-1] - 1] }. You need to output the numbers in the sequence that Dr. Dhruv will call.

Note: Dr. Dhruv needs this task to finish quickly and hence expected time complexity `O(K*log(A))`

**Constraints:**

```
1 <= K <= 1000  and K <= A
1 <= B[i] <= A (Elements of B may not be distinct, 
i.e, he can call a student multiple times)
1 <= A <= 10^9   (Yes, Dr. Dhruv can teach 
10^9 students at a time)
```

**Example:**

```
Input:
A = 12, B = [2, 5]

Output:
ans = [10, 2]

Sorted list S: ["1", "10", "11", "12", 
        "2", "3", "4", "5", ...., "9"]
ans = [2nd number, 5th number] = [10, 2]
```
### Brute Force
- We can create a list of strings S: ["1", "2","3","4"...,"A"].
- We can sort this list.
- And for every i store S[B[i]-1] in answer array.
- This approach will take $O(k\times n\log^2{n})$.
- This will give TLE.

### Hints
- Without creating S, can we calculate the number of elements starting with "1".
|Number Of Digits|Numbers|Total|
|:--|:--|:--|
|1|1|1|
|2|10,11, ... 19|11|
|3|100, 101, ... 199|111|

- For every digit we can calculate the number of elements starting with that digit.
- We can calculate this number for every position in the answer.

### Code
```C++
//Note: Two functions are defined just 
//for the sake of understanding.
//function_one and function_two can be 
//combined into one function using a flag variable
 
/*
function_two(n,k) computes the rest 
of the digits of the kth required number.
*/
string function_two(string s, int k){
	// Base case, first string is empty in this case
	if(k==1) return "";
 
	k-=1;     //Don't consider empty string
 
	int l = s.size();
	int f = s[0]-'0';
	int temp = stoi(string(l,'1'));   // 1111111...	l digits
 
	//Case when length of s is 1
	if(l==1) return to_string(k-1);
 
	string rem = s.substr(1);
 
	//Note that i here starts from 0
	for(int i=0; i<10; i++){
		//Here we calculate the number 
    //of numbers starting from i.
		//There will be multiple cases 
    //to handle which becomes clear
		//after a little thinking.
 
		if(i == f) temp/=10;
		int buffer = temp;
		if(i == f) buffer += stoi(rem) + 1;
 
		if(k > buffer){
			k-=buffer;
			continue;
		}
		if(i == f) return to_string(i) + function_two(rem, k);
		return to_string(i) + function_two(to_string(9*(temp/10)), k);
	}
 
}
 
/*
function_one(n,k) computes the first 
digit of the kth required number.
function_one and function_two are 
separate as 1st digit can't be zero whereas
rest of the digits can be zero.
*/
string function_one(string s, int k){
 
	int l = s.size();                 //length of the number
	int f = s[0]-'0';                 //first digit of the number
	int temp = stoi(string(l,'1'));   // 1111111...	l digits
 
	//Base case, only 1 digit number
	if(l==1) return to_string(k);
 
	//Utility string, used below in the for loop
	string rem = s.substr(1);
 
	//find the number of numbers say 
  //num starting from x (x <= i).
	//if k > num, first digit is not i, 
  //else first digit is i.
 
	//Note that i here starts from 1.
	for(int i=1; i<10; i++){
		//Here we calculate the number of 
    //numbers starting from i.
		//There will be multiple cases 
    //to handle which becomes clear
		//after a little thinking.
 
		if(i == f) temp/=10;
		int buffer = temp;
		if(i == f) buffer += stoi(rem) + 1;
 
		if(k > buffer){
			k-=buffer;
			continue;
		}
		if(i == f) return to_string(i) + function_two(rem, k);
		return to_string(i) + function_two(to_string(9*(temp/10)), k);
	}
}
 
 
 
vector<int> Solution::solve(int A,const vector<int> &B){
	string str = to_string(A);
 
	int m = B.size();
	vector<int> ans(m);
 
	//function_one(n,k) give kth 
  //number in the sorted order of strings ["1", "2", ..., "n"]
	for(int i=0; i<m; i++)	
  ans[i] = stoi(function_one(str,B[i]));
 
	return ans;
}
```
### Time Complexity
- This approach will work in $O(k \times \log{n})$. Because there are $O(\log{n})$ digits in A and every digit take $O(1)$ time.

### Dry Run
```
A : 5789
B : [ 1789]
```
|Place|Digits|Rank|Numbers with Digit|
|:--|:--|:--|:--|
|1|1|1789|1111|
|1|2|678|1111|
|2||||
|Empty will first element||||
|2|0|677|111|
|2|1|566|111|
|2|2|455|111|
|2|3|344|111|
|2|4|233|111|
|2|5|122|111|
|2|6|11|111|
|26||||
|3|0|10|11|
|260||||
|4|0|9|1|
|...||||
|4|8|1|1|
|2608||||
