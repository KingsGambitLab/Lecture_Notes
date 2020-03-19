
**Q1- Stock Span Problem**

The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.

For example: {100, 80, 60, 70, 60, 75, 85}
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

_Approach 1_ -> Brute Force 

Time Complexity: O(n^2)
Space Complexity: O(1)

_Approach 2_ -> 

If value at arr[i] > arr[i-1], then all the elements in the span of arr[i - 1] will be included in my span, so it makes sense not to make those calculations again. We can simply jump back to that element which was not a part of span of arr[i-1]

```java
tatic void calculateSpan(int price[], int n, int S[]) 
    { 
        // Create a stack and push index of first element to it 
        Stack<Integer> st = new Stack<>(); 
        st.push(0); 
        
        // Span value of first element is always 1 
        S[0] = 1; 
  
        // Pop elements from stack while stack is not empty and top of stack is smaller than price[i] 
        while (!st.empty() && price[st.peek()] <= price[i]) 
          st.pop(); 
  
        // If stack becomes empty, then price[i] is greater than all elements on left of it, i.e., price[0], price[1],               //..price[i-1]. Else price[i] is greater than elements after top of stack 
        S[i] = (st.empty()) ? (i + 1) : (i - st.peek()); 
  
        // Push this element to stack 
        st.push(i); 
        } 
    } 
```
Time Complexity: O(n)
Space Complexity: O(n)

**Q2- Next Greater Element I**
Find the just greater element on right side of each element.
Ex - 4 5 2 25
Ans- 5 25 25 -1

Ex - 10 7 4 2 9 10 11 3 2
Ans- 11 9 9 9 10 11 -1 -1 -1

_Approach 1:_ Use two loops: The outer loop picks all the elements one by one. The inner loop looks for the first greater element for the element picked by the outer loop. If a greater element is found then that element is printed as next element, otherwise -1 is printed.

Time Complexity: O(n^2)
Space Complexity: O(1)

_Approach 2:_
  Intuition:
  In case of a decreasing sequence, the answer is always going to be -1 for all elements till I dont encounter a increasing   sequence/number. 
  For eg: 5 4 3 2 1
          -1 -1 -1 -1 -1
          
          5 4 3 2 1 10
          10 10 10 10 10 -1
          
          For all the elements less than 10 in a decreasing sequence are going to have the answer 10. 
          
          11 4 3 2 10 12
          
          Till 2, it is a decreasing sequence. After that, it is a increasing sequence then. So, for all the elements less             than 10, the elements are going to have an answer 10. 
          Now the question is reduced to 11 10 12. Again 11 and 10 is a decreasing sequence, so the answer for them is going           to be 12 12. 
          
```java
static void printNGE(int arr[], int n)  
    { 
        int i = 0; 
        stack s = new stack(); 
        s.top = -1; 
        int element, next; 
        s.push(arr[0]); 
        for (i = 1; i < n; i++)  
        { 
            next = arr[i]; 
            if (s.isEmpty() == false)  
            {  
                element = s.pop(); 
                while (element < next)  
                { 
                    System.out.println(element + "-->" + next); 
                    if (s.isEmpty() == true) 
                        break; 
                    element = s.pop(); 
                } 
                if (element > next) 
                    s.push(element); 
            } 
            s.push(next); 
        } 
        while (s.isEmpty() == false)  
        { 
            element = s.pop(); 
            next = -1; 
            System.out.println(element + "-->" + next); 
        } 
```
Time Complexity: O(n) 
Space Complexity: O(n)


**Q3- Next Smaller Element**

**Q4- Maximum area of a rectangle in a histogram**
Input: 7 bars of heights {6, 2, 5, 4, 5, 1, 6}
Output: Max Area = 12

**Q5- Maximal Rectangle**
Input:
[

  ["1","0","1","0","0"],
  
  ["1","0","1","1","1"],
  
  ["1","1","1","1","1"],
  
  ["1","0","0","1","0"]
  
]
Output: 6

```java
public int leetcode84(int[] heights) {
        Stack < Integer > stack = new Stack < > ();
        stack.push(-1);
        int maxarea = 0;
        for (int i = 0; i < heights.length; ++i) {
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i])
                maxarea = Math.max(maxarea, heights[stack.pop()] * (i - stack.peek() - 1));
            stack.push(i);
        }
        while (stack.peek() != -1)
            maxarea = Math.max(maxarea, heights[stack.pop()] * (heights.length - stack.peek() -1));
        return maxarea;
    }

    public int maximalRectangle(char[][] matrix) {

        if (matrix.length == 0) return 0;
        int maxarea = 0;
        int[] dp = new int[matrix[0].length];

        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[0].length; j++) {

                // update the state of this row's histogram using the last row's histogram
                // by keeping track of the number of consecutive ones

                dp[j] = matrix[i][j] == '1' ? dp[j] + 1 : 0;
            }
            // update maxarea with the maximum area from this row's histogram
            maxarea = Math.max(maxarea, leetcode84(dp));
        } return maxarea;
    }
  
```

**Q6- Remove Duplicates and answer should be lexicographically smallest**

Input: bcabc
Output: abc

Input: cbacdcbc
Output: acdb

For bab, you always want to remove the first b, because it is followed by a smaller character. 

```java
class Solution {
    public String removeDuplicateLetters(String s) {

        Stack<Character> stack = new Stack<>();

        // this lets us keep track of what's in our solution in O(1) time
        HashSet<Character> seen = new HashSet<>();

        // this will let us know if there are any more instances of s[i] left in s
        HashMap<Character, Integer> last_occurrence = new HashMap<>();
        for(int i = 0; i < s.length(); i++) last_occurrence.put(s.charAt(i), i);

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            // we can only try to add c if it's not already in our solution
            // this is to maintain only one of each character
            if (!seen.contains(c)){
                // if the last letter in our solution:
                //     1. exists
                //     2. is greater than c so removing it will make the string smaller
                //     3. it's not the last occurrence
                // we remove it from the solution to keep the solution optimal
                while(!stack.isEmpty() && c < stack.peek() && last_occurrence.get(stack.peek()) > i){
                    seen.remove(stack.pop());
                }
                seen.add(c);
                stack.push(c);
            }
        }
    StringBuilder sb = new StringBuilder(stack.size());
    for (Character c : stack) sb.append(c.charValue());
    return sb.toString();
    }
}
```
Time Complexity: 0(length of string)
Space Complexity: 0(1)

**Q7- Decode an encrypted string**

Given a String A and an integer B. String A is encoded consisting of lowercase English letters and numbers. A is encoded
in a way where repetitions of substrings are represented as substring followed by the count of substrings.

Input: “ab2c3” k = 8
Output: ababc ababc ababc  "a"

You have to find and return the Bth character in the decrypted string.

Note: Frequency of encrypted substring can be of more than one digit. For example,
in “ab12c3”, ab is repeated 12 times. No leading 0 is present in the frequency of substring.

Approach: We dont care about the characters that occur after k? Lets see how we can solve it without expanding the string. Do we see a pattern in this string? String repeated thrice. Lets say I have a string of substring length 5 which is repeated n times, then can we find the kth character by (k%5) i.e., (8%5) = 3. Now find 3rd character in ababc. We see again a pattern in this. A repeated subtring of length 2. So, now find 3%2. 

((((1+1) * 2) + 1)*3)
```cpp
string Solution::solve(string A, int B) {
    stack < pair<string, int > > st;
    int i, n = A.size();
    int len = 0;
    int num;
    int k = B;
    string curr;
    string temp = "";
    for(i=0; i<n; i++){
        if(A[i] >= 'a' && A[i] <= 'z'){
            len++;
            curr = A[i];
            st.push({curr, len});
        }else{
            num = 0;
            while(i < n && A[i] >= '0' && A[i] <= '9'){
                num = num*10;
                num += A[i]-'0';
                i++;
            }
            if(len*num >= k){
                break;
            }
            len = len*num;
            i--;
        }
    }
    pair <string, int> p;
    while(!st.empty()){
        p = st.top();
        st.pop();
        
        k = k%p.second;
        if(k == 0){
          return p.first;
        }
    }
}

Time Complexity: 0(length of string)
Space Complexity: 0(length of string)

```
**Q8- Number of Valid Subarrays**

Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:
The leftmost element of the subarray is not larger than other elements in the subarray.
Input: [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].


```java 
public int validSubarrays(int[] nums) {
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        for (int num : nums) {
            while (!stack.isEmpty() && num < stack.peek()) {
                stack.pop();
            }
            stack.push(num);
            res += stack.size();
        }
        return res;
    }
```
Time Complexity: O(n) 
Space Complexity: O(n)

