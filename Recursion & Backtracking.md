
## Recursion

- Also called Divide n conquer. 

- Better to say reduce and conquer. 

- Assume that smaller problem will work and build solution for larger problem. 

- Solution starts aggregating at base case. 

## Backtracking 

- A) Element of choice

- B) Explore all possibilities (Solving question in tree like fashion )

**Steps for Coding:**

- Take a decision (When you take a decision, you know that now your problem has been reduced )

- Recur (Solving reduced problem )

- Undo Decision I

**Q1 Gray Code**

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

**Q2- Word Break**

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.

You may assume the dictionary does not contain duplicate words.

```
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
```

_Recursion_

```java
public List<String> wordBreak(String s, Set<String> wordDict) {
        return word_Break(s, wordDict, 0);
    }
    
    public List<String> word_Break(String s, Set<String> wordDict, int start) {
        LinkedList<String> res = new LinkedList<>();
        if (start == s.length()) {
            res.add("");
        }
        for (int end = start + 1; end <= s.length(); end++) {
            if (wordDict.contains(s.substring(start, end))) {
                List<String> list = word_Break(s, wordDict, end);
                for (String l : list) {
                    res.add(s.substring(start, end) + (l.equals("") ? "" : " ") + l);
                }
            }
        }
        return res;
    }
```

_Recursion with memoization__
```java

public List<String> wordBreak(String s, List<String> wordDict) {
        return word_break(s, wordDict, 0);   
    }
    
    HashMap<Integer, List<String>> map = new HashMap<>();
    
    public List<String> word_break(String s, List<String>wordDict, int start){
        if(map.containsKey(start)){
            return map.get(start);
        }
        LinkedList<String> res = new LinkedList<>();
        
        if(start == s.length()){
            res.add("");
        }
        
        for(int end = start + 1; end <= s.length(); end++){
            if(wordDict.contains(s.substring(start, end))){
                List<String> list = word_break(s, wordDict, end);
                for(String l: list){
                    res.add(s.substring(start, end) + (l.equals("") ? "" : " ") + l);
                }
            }
        }
        System.out.println(start);
        System.out.println(res);
        map.put(start, res);
        return res;
    }
```


**Q3- Generate Paranthesis**

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

```

```java

public List<String> generateParenthesis(int n) {
        
        List<String> ans = new ArrayList<>();
        backtrack(ans, "", 0, 0, n);
        
        return ans;
    }
    
    public void backtrack(List<String> ans, String curr, int open, int close, int max){
        if(curr.length() == max * 2){
            ans.add(curr);
            return;
        }
        
        if(open < max){
            backtrack(ans, curr + "(", open + 1, close, max);
        }
        
        if(close < open){
            backtrack(ans, curr + ")", open, close + 1, max);
        }
    }

```

Time Complexity: 

**Q4- Palindrome Partitioning**

Given a string s, partition s such that every substring of the partition is a palindrome.

Print all palindromic partitions. 

Partitioning means that dividing the string into k parts such that: 

1. Maintain order

2. Mutually exlusive partitions - no overlap of elements

3. Mutually exhaustive partitions - union of all subsets gets the entire string. 

4. Every partition should be a palindrome

```
Input: "aab"

Output:
[
  ["aa","b"],
  ["a","a","b"]
]

Invalid: 
["a", "ab"]

```
- Why a backtracking problem? Because you want to find all possible partitions.

- Element of Choice? Do I introduce a partition after ith element or not? 

- How to represent a state? f(i)

- At each step, you have two choice, whether to introduce partition not introduce partition.

- Also at each step, check if the currString till now is palindrome or not. If it is not, we do pruning. 

```java

public class Solution {

            List<List<String>> resultLst;
	    ArrayList<String> currLst;
	    
	    public List<List<String>> partition(String s) {
	        resultLst = new ArrayList<List<String>>();
	        currLst = new ArrayList<String>();
	        backTrack(s,0);
	        return resultLst;
	    }
	    
	    public void backTrack(String s, int l){
	        
		if(currLst.size()>0 //the initial str could be palindrome
	            && l>=s.length()){
	                List<String> r = (ArrayList<String>) currLst.clone();
	                resultLst.add(r);
	        }
		
	        for(int i=l;i<s.length();i++){
	            
		    if(isPalindrome(s,l,i)){
	                if(l==i)
	                    currLst.add(Character.toString(s.charAt(i)));
	                else
	                    currLst.add(s.substring(l,i+1));
	                backTrack(s,i+1);
	                currLst.remove(currLst.size()-1);
	            }
	        }
	    }
	    
	    public boolean isPalindrome(String str, int l, int r){
	        
		if(l==r) return true;
	        while(l<r){
	            if(str.charAt(l)!=str.charAt(r)) return false;
	            l++;r--;
	        }
		
	        return true;
	    }
}

```
**Q5- Word Search**

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

![Screenshot 2020-01-20 at 3 11 05 PM](https://user-images.githubusercontent.com/35702912/72732288-5e957e00-3bbb-11ea-986e-5730c6141a40.png)



```cpp

class TrieNode {
public:
    char ch;
    bool isTerminal;
    unordered_map<char, TrieNode*> children;
    TrieNode(char ch, bool isTerminal) {
        this->ch = ch;
        this->isTerminal = isTerminal;
    }
    
};
class Solution {
public:
    vector<string> result;
    void insert(string word, TrieNode *root) {
        TrieNode* temp = root;
        for(int i = 0; i < word.size(); i++) {
            char ch = word[i];
            if(temp->children.find(ch) != temp->children.end()) {
                temp = temp->children[ch];
            } else {
                temp->children[ch] = new TrieNode(ch, false);
                temp = temp->children[ch];
            }
        }
        temp->isTerminal = true;
        return;
    }
    
    
    void backtrack(vector<vector<char>>& board, TrieNode* root, int i, int j, bool **visited, string str) {
        if(i < 0 or j < 0 or i >= board.size() or j >= board[0].size()) {
            return;
        }
        if(visited[i][j] == true) return;
        char ch = board[i][j];
        if(root->children.find(ch) == root->children.end()) {
            return;
        } else {
            root = root->children[ch];
        }
        if(root->isTerminal == true) {
            result.push_back(str+board[i][j]);
            root->isTerminal = false;
        }
        visited[i][j] = true;
        backtrack(board, root, i+1, j, visited, str+board[i][j]);
        backtrack(board, root, i-1, j, visited, str+board[i][j]);
        backtrack(board, root, i, j+1, visited, str+board[i][j]);
        backtrack(board, root, i, j-1, visited, str+board[i][j]);
        visited[i][j] = false;
        return;
    }
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode *root = new TrieNode('\0', false);
        for(string word: words) {
            insert(word, root);
        }
        bool **visited = new bool*[board.size()];
        for(int i = 0; i < board.size(); i++) {
            visited[i] = new bool[board[0].size()]();
        }
        
        for(int i = 0; i < board.size(); i++) {
            for(int j = 0; j < board[0].size(); j++) {
                TrieNode* temp = root;
                backtrack(board, temp, i, j, visited, "");
            }
        }
        return result;
    }
};

```
