<html>
<head>
<script type="text/javascript"
   src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js">
</script>
</head>

<body onload = "start()">

Do you know how the "auto-completion feature" provided by different software like IDEs, Search Engines, command-line interpreters, text editors, etc works?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/1.png)

Below is an input box, which has an autocomplete feature for "country names". Try it out!

<input type="text" id = "trie" placeholder="Enter country name" onkeyup="suggest()" onfocusout="done()">

<ul id="suggest" style="list-style-type:none">

</ul>

The basic data structure behind all these scenes is **Trie**.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/2.png)

Spell checkers can also be designed using **Trie**.

# Trie
String processing is widely used across real-world applications, for example data analytics, search engines, bioinformatics, plagiarism detection, etc. 

Trie is a very useful and special kind of data structure for string processing.

Below is a very simple representation of trie consisting of `"cat"`, `"bat"`, `"dog"` strings.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/lastadd.jpg)

Now, suppose we are given a string-array and we are told that check whether `"cat"` string is present in the array. Then we can check it via brute force-compare with each and every string present in the string-array, which would take $O(N*length("cat"))$ in the worst-case situation, where $N$ is the number of string in the array.

Now, if you create a trie from all the strings present in the array, then you can simply check it in $O(length("cat"))$ time by traversing through trie(confused? we will see it soon), which is very efficient and therefore trie is an efficient information re<b><i>trie</i></b>val data structure.

## Introduction

Trie is a tree of nodes, where the specifications of a node can be given as below:

Each node has, 
1. An array of size of the alphabet(see the note below) to store links to other nodes.
2. A boolean variable.

**Notes** 

1. For an easy understanding purpose, we are assuming that all strings contain only lowercase alphabet letters, i.e. `alphabet_size` is $26$.
2. We will discuss the traditional implementation here, although we can use some data structures like hash table in each node.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/3.png)

**We will see "why do we need these two variables?" soon.**

```cpp
struct trie_node 
{
    // Array of pointers of type 
    // trie_node
    vector<trie_node*> links;
    bool isEndofString;

    // Constructor
    trie_node()
    {
        links.assign(alphabet_size, nullptr);
        isEndofString = false;
    }
};
```

Now, we have seen how a trie node looks like. Let's see **how we are going to store strings in a trie using this kind of node.**

## How to insert a string in a trie?

Look at the image below, which represents a string "act" stored in a trie. Observe something!

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/4.png)

**Note: Empty places in the array have null values(`nullptr` in c++).**

1. **Other than the root node, each node in trie represents a single character.** In the above image, $2^{nd}$, $3^{rd}$, $4^{th}$ node represents `'a'`, `'c'`, and `'t'` respectively.
2. **The node at which the string ends, we set isEndofString to true.** See last node in the image above.

Therefore, now for the shake of ease we are going to represent the nodes of trie as below.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/5.png)

And therefore representation of trie containing string "act" will be as below.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/6(1).jpg)

**Note:** Root node will be shown empty, as it only represents an empty string, so to speak.

Now, observe the trie below, which contains two strings "act" and "ace".

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/7(1).jpg)

Note that the node representing character `c` in the above trie, in a magnified sense would look as below:

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/8.png)

What did you observe?

A common prefix of `"ace"` and `"act"` is `"ac"` and therefore we are having the same nodes until we traverse `"ac"` and then we create a new node for character `e`.

Therefore, we are not creating any new node until we need one and **Trie is a very efficient data storage, when we have a large list of strings sharing common prefixes.** It is also known as **prefix tree**.

Now, look the trie below, which contains three strings `"act"`, `"ace"` and `"cat"`.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/9(1).jpg)

Let's see a proper algorithm to insert a string in a trie.

1. Starting from the root, if there is already a node representing the corresponding character of a string, then simply traverse.
2. Otherwise, create a new node representing the corresponding character.
3. At the end of the string, set `isEndofString` to true in the last ending node.

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

If you don't have `isEndofString` variable, then you will not be able to correctly check whether `on` is present or not. Because it is the prefix of `once`.

**Algorithm**:

1. Starting from the root, try to traverse the corresponding character of the string. If a link is present, then go ahead.
2. Otherwise, simply given string is not present in the trie.
3. If you are successfully able to traverse all corresponding characters of the string, then check whether the query string is present or not via `isEndofString` variable of the last node.

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
Can you find recursive version of the above function?

**Recursive version:**
```cpp
// @param: root -> root of the trie
// @param: s -> the string we are deleting
// @param: i -> index of s currently reached via recursive traversal
bool Rec_search(trie_node* root, string& s, int i = 0)
{
    // No link present
    // so string is not present
    if(root == nullptr)
        return false;
    if(i == s.size()) {
        // present
        if(root->isEndofString)
            return true;
        else
            return false;
    }
    // Recusively traverse using links
    return Rec_search(root->link[s[i]-'a'], s, i+1);
}
```

**Time Complexity:** $O(N)$, where $N$ is the length of the string we are searching for.

## Delete

How will you delete `"ace"` from the trie below?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/9(1).jpg)

Things to take care about while you are deleting a string from the trie,
1. It should not affect any other string present in the trie.
2. Therefore, we are only going to delete **the nodes which are present only due to the presence of the given string**. And no other string is passing through them.

We are going to use a recursive procedure. If the string is not present, then we will return `false` and `true` otherwise. **Recursive procedure for delete is a modified version of the recursive search procedure** and therefore  make sure you understand that.

Can you figure it out on your own?

**Procedure:**

1. We are traversing the trie recursively, the same way as in `Rec_search()` procedure.
2. While traversing, if we find that no link is present(`root == nullptr`) for the current character, then the string is not present in the trie and return `false`.
3. If we are successfully able to traverse the whole string until `i==s.size()`, then finally check `isEndofString` of the last node. If the string is present(`isEndofString = true)`, then set it to `false` and return `true`. Otherwise, return `false`-not present.
4. Now, while backtracking stage of the recursion, delete nodes if it is no longer needed after deletion of the given string.

Now, go through the code below with very intuitive comments.

```cpp
// Checks whether any link is present
bool isEmptyNode(trie_node* node)
{
    for(auto i:node->link)
        if(i != nullptr)
            return false;
    return true;
}

// Returns true if the string is successfully deleted
// And if the string is not present in the trie then returns false.
bool deleteString(trie_node* root, string& s, int i = 0)
{
    if(root == nullptr)
        return false;
    
    if(i == s.size()) {
	    // present
        if(root->isEndofString) {
            // delete it
            root->isEndofString = false;
            return true;
        }
        else 
            return false;
    }
    
    bool ans = deleteString(root->link[s[i]-'a'], s, i+1);
    
    // String is present
    if(ans) {
        // Check whether any other string
        // passes through this link node
        // If not passing, then delete it
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

**Time Complexity:** $O(N)$, where $N$ is the length of the string we are deleting.

## Trie as an array

The availability of dynamic arrays allows us to create Trie without using pointers.

Now, we are going to store trie as a dynamic array of `TrieNodes`. In this implementation, we are going to use an array of integers instead of pointers in `TrieNode` and as a link, we are going to store the index of a node rather than the address of a node in the former case.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/11.jpg)

See the below implementation of trie as an array, which is quite similar and intuitive as the previous implementation.

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
But it has a downside that you can not generally delete strings present in the trie. Why?

Try deleting a single node(other than last one), you will realize that indexes of each subsequent node will change, and also deleting in an array has a very bad performance.

It is an easy implementation, but with a single downside. Therefore, use as per the requirement.

## Count the total number of words present in a Trie

How will you find the number of words(strings) present in the trie below?

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/9(1).jpg)

Ultimately, It means to find the total number of nodes having `true` value of `isEndofString`. Which can be easily done using recursive traversal of all the nodes present in the trie.

The basic idea of the recursive procedure is as follow: 

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
**Time complexity:** $O(\text{Number of nodes present in the trie})$, as we are visiting each and every node. <br>
**Space complexity:** $O(1)$

## Print all words stored in Trie

It is similar to finding the total number of words but instead of adding $1$ for each `isEndofString`'s true value, we are going to store the word representing that particular end.

The code is similar to finding the total number of words.

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
**Time complexity:** $O(\text{Number of nodes present in the trie})$, as we are visiting each and every node. <br>
**Space Complexity:** $O(\text{Total length of all words present in the trie})$

## Auto-suggestion features

How will you design the autocompletion feature using Trie?

For example, we have stored C++ keywords in a trie. Now, when you type `"n"` it should show all keywords starting from `"n"`. For simplicity, only keywords starting from `"n"` are shown in the trie below,

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/12(1).jpg)

How will you print all keywords starting from `"n"`? OR how will you print all keywords having `"n"` as a prefix?

Simply use `printAllWords()` on node `n`, and the problem is solved!

A common procedure is as below:

1. Traverse nodes in trie according to the given uncomplete string `s`. If we are successfully able to traverse `s`, then there are keywords having a prefix of `s`. Otherwise, there will be nothing to suggest.

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


**Time complexity:** $O(\text{Length of S + Total length of all suggestions excluding common prefix(S) from all})$, where `s` is the string you want suggestions for. <br>
**Space complexity:** $O(\text{Total length of all possible suggestions})$

It is a widely used feature, as discussed at the start of the article.

There is also something called **"Ternary Search Tree"**. When each node in the trie has most of its links used(having many similar prefix words), a trie is substantially more space-efficient and time-efficient than the ternary search tree.

But, If each node stores a few links, then the ternary search tree is much more space-efficient, because we are using $26$ pointers in each node of trie and many of them may be unused.

Therefore, use as per the requirements.

## Dictionary using Trie

What are the common features of an English dictionary?

1. Efficient Lookup of words
2. As the dictionary is very large, Lesser memory usages

Hashtable can be used to implement a dictionary. After precomputation of hash for each word in $O(M)$, where $M$ is the total length of all words in the dictionary, we can have efficient lookups if we design a very efficient hashtable. 

But as the dictionary is very large there will be collisions between two or more words. Still, you can design a hash table to have efficient look-ups.

But hashtable has a very high space usages, as we simply store each word and attatched data. But what if we design it using a trie?

As in a dictionary we have many common-prefix words, trie will save a substantial amount of memory consumption. Trie supports look-up in $O(\text{word length})$, which is higher than a very efficient hash table.

Other advantages of the trie are as below:
1. Auto-complete feature
2. It also supports ordered traversal of words with given prefix
3. No need for complex hash functions

So, if you want some of the above features, then using a trie is good. Also, we don't have to deal with collisions.

Note that in the dictionary along with a word, we have explanations or meanings of that word. That can be handled by separately maintaining an array that stores all those extra stuff. Then store one integer in the `TrieNode` structure to store the index of the corresponding data in the array.

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

The below image shows a typical trie structure for the dictionary.

![enter image description here](https://github.com/KingsGambitLab/Lecture_Notes/blob/master/articles/Akash%20Articles/md/Images/Trie/13.jpg)

<script>
function TrieNode(key) {
  this.key = key;  
  this.parent = null;  
  this.children = {};  
  this.end = false;
}

TrieNode.prototype.getWord = function() {
  var output = [];
  var node = this;
  
  while (node !== null) {
    output.unshift(node.key);
    node = node.parent;
  }
  
  return output.join('');
};


function Trie() {
  this.root = new TrieNode(null);
}

Trie.prototype.insert = function(word) {
  var node = this.root;
  
  for(var i = 0; i < word.length; i++) {
    if (!node.children[word[i]]) {
      node.children[word[i]] = new TrieNode(word[i]);
      
      node.children[word[i]].parent = node;
    }
    
    node = node.children[word[i]];
    
    if (i == word.length-1) {
      node.end = true;
    }
  }
};

Trie.prototype.contains = function(word) {
  var node = this.root;
  
  for(var i = 0; i < word.length; i++) {
    if (node.children[word[i]] || node.children[word[i]]) {
      node = node.children[word[i]];
    } else {
      return false;
    }
  }
  
  return node.end;
};

Trie.prototype.find = function(prefix) {
  var node = this.root;
  var output = [];
  
  for(var i = 0; i < prefix.length; i++) {
    if (node.children[prefix[i].toLowerCase()]) {
      node = node.children[prefix[i].toLowerCase()];
	} else if(node.children[prefix[i].toUpperCase()]) {
		node = node.children[prefix[i].toUpperCase()];
	} else {
      return output;
    }
  }
  
  findAllWords(node, output);
  
  return output;
};

function findAllWords(node, arr) {
  if (node.end) {
    arr.unshift(node.getWord());
  }
  
  for (var child in node.children) {
    findAllWords(node.children[child], arr);
  }
}

var trie = new Trie();

function start() {
	countries = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegowina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait", "Kyrgyzstan", "Lao, People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia, The Former Yugoslav Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia (Slovak Republic)", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zambia", "Zimbabwe"];

	for(let i=0;i<countries.length;i++) {
		trie.insert(countries[i]);
	}
}


function suggest() {

	var myNode = document.getElementById("suggest");
  	myNode.innerHTML = '';

	var s = document.getElementById("trie").value;

	if(s.length == 0) return;

	var ans = trie.find(s);

	if(ans.length == 0) return;
	var sstring = "";
	for(let i=0;i<ans.length;i++){
		let j = 0;
		sstring += "<li>";
		sstring += "<b>";
		while(j < s.length) {
			if (j == 0) {
				let c = ans[i][j].toUpperCase();
				sstring += c;
			}
			else {
				let c = ans[i][j].toLowerCase();
				sstring += c;
			}
			j++;
		}
		sstring += "</b>";
		while(j < ans[i].length)
			sstring += ans[i][j++].toLowerCase();
		sstring += "</li>";
	}
	document.getElementById("suggest").innerHTML = sstring;
}

function done() {

	document.getElementById("trie").value = "";
	document.getElementById("suggest").innerHTML = "";
}

</script>



</body>


</html>
