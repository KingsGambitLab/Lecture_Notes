Tries - Remedial
----------------

```python
class Node:
    children: Dict[char, Node]
    terminal: bool
    character: char
```

Why Tries
---------

Space optimization.
Store the list of all words / movies.

In hashmap, store the keys and values. Key will be (hash, str). Value will be value.
Saves space by using common prefixes

Re**trie**val


```python
def add(node, word):
    if not word:
        node.terminal = True
        return
    ch = word[0]
    if ch not in node.children:
        node.children[ch] = Node(ch)
    add(node.children[ch], word[1:])
    
```


-- --

Search
------

> Given words list, find all words with given prefix

Make trie of the words

-- --

> Given words list, find all words with given suffix.

Make trie of reverse words. Search in reverse.

-- --

Unique Prefix Array
-------------------

> Given list of words, find the unique prefixes.
> input: zebra, dog, dove, duck
> output: z, dog, dov, du

Keep count of how many times a node was used when building the trie.
Each node now stores how many words have that prefix.

counter to child check: zebra, zebras

-- --

Maximum Xor Pair
----------------

> Array with +ve integers
> 

Trie with numbers as bitstrings.
Go opposite of current number to find the max xor

-- --

Min Xor Pair
------------

n^2, O(n log n) by sorting

O(n) with tries

-- --

Maximum XOR Subarray
--------------------

Find the prefix XOR.
note: prefix needs inverse function.
xor's inverse it xor.

Now reduced to Max Xor Pair

-- --

Subarray Xor < k
----------------

> count the number of such subarrays

![33f050b7.png](:storage/41b46a45-1bba-436f-ac52-f4c88d4822be/33f050b7.png)

-- --

Number of triplets in array having subarray xor equal
-----------------------------------------------------

> xor(A[i:j]) == xor(A[j:k])

Take prefix xor. If value repeats at i, j, then all splits of A[i:j] work.
just count.

don't keep hashmap, keep trie



-- --

Word Search
-----------

> Given a 2D board and a list of words from the dictionary, find all words in the board.
> Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

![f5890cb4.png](:storage/41b46a45-1bba-436f-ac52-f4c88d4822be/f5890cb4.png)


```python
def findWords(board, words):
    trie_root = insert_all(words)
    visited = board_of_false
    found = set()
    for row in board:
        for cell in row:
            w = backtrack(board, trie_root, i, j, visited, '')
            found.add_all(w)

def backtrack(board, node, i, j, visited, s):
    if i < 0 or j < 0 or i >= N or j >= N: return
    if visited[i][j] return
    
    ch = board[i][j]
    
    if ch not in node.children:
        return
    
    node = node.children[ch]
    if node.terminal:
        result.add(str + ch)
        # can remove the terminal flag if needed
    
    visited[i][j] = True
    process(board, node, i+1, j, visited, str + ch)
    process(board, node, i-1, j, visited, str + ch)
    process(board, node, i, j+1, visited, str + ch)
    process(board, node, i, j-1, visited, str + ch)
    visited[i][j] = False
```

-- --

Make Word
---------

> input: sam, sung, samsung
> output

```
sam: 
   sam
sung: 
   sung
samsung: 
   sam sung
   samsung
```

Insert all words into trie

```python
search(w, node):
    x, y = w
    val = []
    if x in trie:
        possibles = search(y, root)
        val = append x to all possibles
    possibles = search(y, node_child)
    val.extend(possibles)
    return val
```

-- --

> Longest word in dict that can be built one char at a time

> a at

-- --