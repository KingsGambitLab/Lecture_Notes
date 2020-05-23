Do you know how autocompletion provided by different softwares like IDEs, Search Engines, command-line interpreters, text editors, etc works?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/1.png)

The basic data structure behind all these scenes is **Trie**.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/2.png)

Spell checkers can also be designed using **Trie**.

# Trie
String processing is widely used across real world applications, for example data analytics, search engines, bioinformatics, plagiarism detection, etc. 

Trie is very useful and special kind of data structure for string processing.

## Introduction

Trie is basically a tree of nodes, where specification of a node can be given as below:

Each node has, 
1. An array of datatype node and of size of alphabet.
2. A boolean value(We will see why it is needed).

We will see usages of these two variables soon.

```cpp
struct trie_node 
{
	// Array of pointers of type 
	// trie_node
	vector<trie_node*> links;
	bool isEndofString;

	trie_node(bool end = false)
	{
		links.assign(alphabet_size, nullptr);
		isEndofString = end;
	}
};
```

**Note:** For easy understanding purpose, we are assuming that all strings contain lowercase alphabet letters that is alphabet size is $26$. **We can convert characters to a number by using `c-'a'`, `c` is a lowercase character.**

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/3.png)

Now, we have seen how trie node looks like. Let's see how we are going to store strings in a trie using these kind of nodes.

## How to insert a string in a trie?

Look at the image below, which represents a string "act" stored in a trie. Observe something!

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/4.png)

What did you observe?

Observations:
1. **Other root node, each node in trie represents a single character.**
2. **We set isEndofString to true in the node at which the string ends.**

Therefore, now for the shake of ease we are going to represent the nodes of trie as below.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/5.png)

**Note: Empty places in array have null values.**

And therefore representation of trie containing string "act" will be as below.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/6(1).jpg)

**Note:** Root node will be shown empty, as it only represents an empty string, so to speak.

Now, observe the trie below, which contains two strings "act" and "ace".

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/7(1).jpg)

Note that the node representing character `c` in the above trie, in magnified sense would look as below:

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/8.png)

What did you observe?

Common prefix of `"ace"` and `"act"` is `"ac"` and therefore we are having same nodes until we traverse `"ac"` and then we create a new node for character `e`.

Therefore, we are not creating any new node until we need one and **Trie is a very efficient data storage, when we have a large list of strings sharing common prefixes.** It is also known as **prefix tree**.

Now, observe the trie below, which contains three strings `"act"`, `"ace"` and `"cat"`.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/9(1).jpg)

Let's see proper algorithm to insert a string in a trie.

1. Starting from the root, if there is already a node representing corresponding character of a string, then simply traverse.
2. Otherwise, create a new node representing corresponding character.
3. At the end of string, set `isEndofString` to true in the last ending node.

```cpp
void insert(trie_node* root, string s)
{
	trie_node* temp = root;
	int n = s.size();
	for(int i = 0; i < n; i++){
		if(temp->link[s[i]-'a'] == nullptr)
			temp->link[s[i]-'a'] = new trie_node();
		// Traverse using link
		temp = temp->link[s[i]-'a'];
	}
	temp->isEndofString = true;
}
```

**Time Complexity:** $O(N)$, where $N$ is the length of the string we are inserting.

## Searching in Trie

Can you figure out, how can we check whether the given string is present in trie or not, from whatever we have discussed so far?

For example, if you are searching `"aco"` in the trie below, then how will you do?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/9(1).jpg)

**Can you see, why `isEndofString` is needed?**

Observe the trie given below and try to search whether `"on"` is present or not.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/10(1).jpg)

If you don't have `isEndofString` variable, then you will not be able to correctly check whether `on` is present or not. Because it is prefix of `once`.

**Algorithm**:

1. Starting from the root, try to traverse corresponding character of the string. If a link is present, then go ahead.
2. Otherwise, simply given string is not present in the trie.
3. If you are successfully able to traverse according to the string, then check whether the query string is really present or not via `isEndofString` variable of a last node.

```cpp
bool search(trie_node* root, string s)
{
	trie_node* temp = root;
	int n = s.size();
	for(int i = 0; i < n; i++){
		// There is not further link
		if(temp->link[s[i]-'a'] == nullptr)
			return false;
		temp = temp->link[s[i]-'a'];
	}
	return temp->isEndofString;
}
```

## Delete

How will you delete `"ace"` from the trie below?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/9(1).jpg)

Things to take care about while you are deleting a string from the trie,
1. It should not affect any other string present in the trie.
2. Therefore, we are only going to delete **the nodes which are present only due to the presence of the given string**. And no other string is passing through them.

We are going to use recursive procedure. If the string is not present, then we will return `false` and `true` otherwise.

1. We are traversing trie via the given string recursively.
2. While traversing, if we find that no link is present(`nullptr`) for the current character, then string is not present in the trie and return `false`.
3. If we are successfully able to traverse the string(`i==s.size())`, then finally check `isEndofString` of the last node. If the string is really present, then return `true`. Otherwise return `false`.
4. Now, while backtracking stage of recursion, delete nodes if it is no longer needed after deletion of the given string.

Now, Go through the code below, very intuitive comments are written.
```cpp
// Checks whether any link is present
bool isEmptyNode(trie_node* node)
{
	for(auto i:node->link)
		if(i != nullptr)
			return false;
	return true;
}

// Returns true, if the string is successfully deleted
// And if the string is not present in the trie then returns false.
// @param: root -> root of the trie
// @param: s -> string we are deleting
// @param: i -> index of @s currently reached via recursive traversal
bool deleteString(trie_node* root, string& s, int i = 0)
{
	// Means string is not present
	if(root == nullptr)
		return false;
	
	// Successfully traversed the whole string
	if(i == s.size()) {
		
		// Check whether the string is really present 
		// by checking `isEndofString` variable of the last node
		if(root->isEndofString) {
			root->isEndofString = false;
			return true;
		}
		else 
			return false;
	}
	
	bool ans = deleteString(root->link[s[i]-'a'], s, i+1);
	
	// String is present
	if(ans)	{

		// Check whether any other string
		// passes through this node
		// Not passing, then delete this node
		if(isEmptyNode(root->link[s[i]-'a'])) {

			// Deallocate used memory
			delete root->link[s[i]-'a'];
			root->link[s[i]-'a'] = nullptr;
		}
		return true;
	}
	
	// Not present the return false
	return false;
}
```

## Trie as an array

Availability of dynamic arrays allow use to create Trie without using pointers.

Now, we are going to store trie as a dynamic array of `TrieNodes`. In this implementation, we are going to use an array of integers instead of pointers in `TrieNode` and as a link, we are going to store index of a node rather than address of a node in the former case.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/11.jpg)

See the below implementation of trie as an array, which is quite similar and intuitive as previous implementation.

```cpp
struct TrieNode
{
	vector<int> id_link;
	bool isEndofString;
	
	TrieNode(bool end = false)
	{
		end = isEndofString;
		id_link.assign(26,-1);
	}
};

void insert(vector<TrieNode>& trie, string s)
{
	int temp = 0;
	int n = s.size();
	for(int i = 0; i < n; i++) {
		if(trie[temp].id_link[s[i]-'a'] == -1) {
			trie[temp].id_link[s[i]-'a'] = (int)trie.size();
			trie.push_back(TrieNode());
		}
		temp = trie[temp].id_link[s[i]-'a'];
	}
	trie[temp].isEndofString = true;
}

bool search(vector<TrieNode>& trie, string s)
{
	int temp = 0;
	int n = s.size();
	for(int i = 0; i < n; i++) {
		if(trie[temp].id_link[s[i]-'a'] == -1)
			return false;
		temp = trie[temp].id_link[s[i]-'a'];
	}
	return trie[temp].isEndofString;
}
```
But it has a downside that you can not delete strings present in the trie. Why?

Try deleting a single node, you will realize that indexes of each subsequent node will change and moreover deleting in an array has a very bad performance.

It is easy implemention, but with single downside. Therefore, use as per the requirement.

## Count total number of words present in a Trie

How will you find the number of words(strings) present in the trie below?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/9(1).jpg)

Ultimately, It means to find the total number of nodes having `true` value of `isEndofString`. Which can be easily done using recursive traversal of all the nodes present in the trie.

The basic idea of recursive procedure is as follow: 

Start from the $\text{root}$ node and go through all $26$ positions of the `link` array. For each not-null link, recursively call `countWords()` considering that linked node as a $\text{root}$. And therefore formula will be as below:

$\text{TotalWords} = \text{TotalWords} + \text{countWords}(link_i)$, do it for all not-null links.

Finally, add $1$ to $\text{TotalWords}$ if the current node has `isEndofString = true`.

```cpp
int countWords(trie_node* root)
{
	int total = 0;
	if(root == nullptr)
		return 0;
	for(auto i:root->link)
		if(i != nullptr)
			total += countWords(i);
	total += root->isEndofString;
	return total;
}
```
**Time complexity:** $O(\text{Number of nodes present in the trie})$, as we are visiting each and every node.
**Space complexity:** $O(1)$

## Print all words stored in Trie

It is similar to finding total number of words but instead of adding $1$ for each `isEndofString`'s true value, we are going to store the word representing that particular end.

The code is similar as finding total number of words.

```cpp
void printAllWords(trie_node* root, vector<string>& ans, string s="")
{
	if(root == nullptr)
		return;
	for(int i = 0; i < alphabet_size; i++) {
		if(root->link[i] != nullptr) {
			char c = 'a' + i;
			string temp = s;
			temp += c;
			printAllWords(root->link[i], ans, temp);
		}
	}
	if(root->isEndofString)
		ans.push_back(s);
}
```
**Time complexity:** $O(\text{Number of nodes present in the trie})$, as we are visiting each and every node.
**Space Complexity:** $O(\text{Total length of all words present in the trie})$

## Auto-suggestion features

How will you design autocompletion feature using Trie?

For example, we have stored C++ keywords in a trie. Now, when you type `"n"` it should show all keywords starting from `"n"`. For simplicity only keywords starting from `"n"` are shown in the trie below,

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/12(1).jpg)

How will you print all keywords starting from `"n"`? OR how will you print all keywords having `"n"` as prefix?

Simply use `printAllWords()` on node `n`, and problem is solved!

Common procedure is as below:

1. Traverse nodes in trie according to the given uncomplete string `s`. If we are successfully able to traverse `s`, then there are keywords having prefix of `s`. Otherwise, there will be nothing to suggest.

2. Now, use `printAllWords()` considering the last node(after traversal of trie according to `s`) as a root.

```cpp
void autocomplete(trie_node* root, string s)
{
	int n = s.size();
	trie_node* temp = root;
	for(int i = 0; i < n; i++) {
		if(temp->link[s[i]-'a'] == nullptr)
			return;
		temp = temp->link[s[i]-'a'];
	}
	vector<string> suggest;
	printWords(temp, suggest, s);
	for(auto i:suggest)
		cout << i << endl;
	/*
	OR
	printWords(temp, suggest);
	for(auto i:suggest)
		cout << s << i << endl;
	*/
}
```


**Time complexity:** $O(\text{Length of S + Total length of all suggestions excluding common prefix(S) from all})$, where `s` is the string you want suggestions for.
**Space complexity:** $O(\text{Total length of all possible suggestions})$

It is widely used feature, as discussed at the start of the article.

There is also something called **"Ternary Search Tree"**. When each node in the trie has most of its links used(having many similar prefixe words), trie is substantially more space efficient and time efficient than  ternary search tree.

But, If each node stores few links, then ternary search tree is much more space efficient, because we are using $26$ pointers in each node of trie and many of them may be unused.

Therefore, use as per the requirements.

## Dictionary using Trie

What are common features of an english dictionary?

1. Efficient Lookup of words
2. As dictionary is very large, Less memory usages

Hashtable can be used to implement dictionary. After precomputation of hash for each word in $O(M)$, where $M$ is total length of all words in the dictionary, we can have efficient lookups if we design a very efficient hashtable. 

But as dictionary is very large there will be collisions between two or more words. But still you can design hash table to have efficient look-ups.

But space usages is very high, as we simply store each words. But what if we design it using a trie?

As in a dictionary we have many common-prefix words, trie will save substantial amount of memory consumption. Trie supports look-up in $O(word length)$, which is higher than a very efficient hash table.

Other advantages of trie is as below:
1. Auto-complete feature
2. It also supports ordered traversal of words with given prefix
3. No need for complex hash functions

So, if you want some of the above features then using trie is good for you. Also, we don't have to deal with collisions.

Note that in dictionary along with a word, we have explanations or meanings of that word. That can be handled by seperately maintaining an array which stores all those extra stuffs. Then store one integer in the `TrieNode` structure to store the index of the corresponding data in the array.

```cpp
struct trie_node 
{
	// Array of pointers of type 
	// trie_node
	vector<trie_node*> links;
	bool isEndofString;
	// To store id of data
	int idOfData;
};
```

Below image shows a typical trie structure for dictionary.


![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/13(1).jpg)
