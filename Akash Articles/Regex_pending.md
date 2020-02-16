
## Regular Expression (RegEx)

While filling online forms, haven't you come across errors like "Please enter valid email address" or "Please enter valid phone number".

Annoying as they may be, there's a lot of black magic that the computer does before it determines that, the details you've entered are incorrect.

Can you think out, what is that black magic? If you are familar with algorithms, then you will say, we can write an algorithm for the same. 

Yes, we can write an algorithm to verify different things. But we have a standard tool which is particularly designed for the similar kind of purposes. 

It is **Regular Expression**. We call it **RegEx** for short. RegEx makes our work a lot easier. Let's see some basic examples where RegEx becomes handy.

Suppose, you are in search of an averge price of a particular product on amazon. The following regular expression will find you any price(\$12, \$75.50) on the webpage: `\$([0-9]+)\.([0-9]+)`.

Quite interesting!

Let's look at another example. You have a long list of documents with different kinds of extensions. You are particularly looking for data files having **.dat** extension. 

`^.*\.dat$` is a regular expression which represents a set of string ending with **.dat**. Regular expression is a standardized way to encode such patterns. 

Well. What does the name **Regular Expression(RegEx)** represent? Regular Expression represents the sequence of characters that defines a regular search pattern.

RegEx is a standardized tool to do the following works:
1. Find and verify patterns in a string.
2. Extract particular data present in the form of substrings.
3. Replace, split and rearrange particular parts of a string.

We are going to look at all the three things above.

Let's begin the journey with RegEx!

**Note:** 
1. In all the images below, the first section is a RegEx code and below is a text, in which the matches are shown-the shaded regions show the match. All the images are taken using regexr.com.
2. In all the images, Small dot between words in the text shows a space.
3. **Alpha-numeric character** is the one which belongs to any of $0-9,A-Z,a-z$ ranges.
4. String is a sequence of characters.

## Simple Alpha-numeric character matching

Simple matching of a specific word can be done as the following:

![enter image description here](https://lh3.googleusercontent.com/YGfz9u58rRKD0ABrSKDv7ZJOEMaIMGdFWgJWGGNzCFNakCtfAZVk1UEm7mBS4lIX1LFXoV420cmY=s1600)

As you can see it matches "Reg" in the text. Similarly, what will be the match for "Ex" in the same text above?

![enter image description here](https://lh3.googleusercontent.com/LkJXO79wn08dvgX5Q2JXHtyN7MW38AeNdV7fjG6lk7MNsiamx9iOekEGQg-WS9OLQMWxBuspjSkh=s1600)

Do you notice anything? It is a **case sensitive**.

**Note:** Most of the programming languages have libraries for RegEx and almost similar kind of syntax usages. Here we will see how to implement in **Javascript**.

Here is a basic code in Javascript. Here pattern is written in /_____/g, where g is a modifier, which is used find all matches rather than stopping at the first match.

**Note:** The function **exec** returns null, if there is no match and match data otherwise.
```js
// Main text (string) in which we are finding
// Patterns
var str = "RegEx stands for Regular Expression!";

// Pattern string
var pattern = /Reg/g;

// This will print all the data of matches
// across the whole string
while(result = pattern.exec(str))
{
	console.log(result); // printing
}

// This will be the output
/*
[
  'Reg',
  index: 0,
  input: 'RegEx stands for Regular Expression!',
  groups: undefined
]
[
  'Reg',
  index: 17,
  input: 'RegEx stands for Regular Expression!',
  groups: undefined
]
*/
```

**Note:** **Groups** in the above output is a RegEx concept we will look at it soon, keep reading.

Now, you can change the pattern and string in the code above to observe other patterns as we will learn below.

## Character classes:

![IMG](https://lh3.googleusercontent.com/dlLzL3teyEoax1JsdF7JeGP6DZOJll-UgnZqFkJtBeAVJhM1xMnXBHVeJYf_cUFLmj-f1qPO8asf=s1600)

What if you want to match both "soon" and "moon" or basically words ending with "oon"?

![enter image description here](https://lh3.googleusercontent.com/bsRHqYuPZIQ7Yra4-zyF1BX2pIYDukCEtTfCK3rjaCTRmTAuo_fuHTVK5sJjbTdbXjGTVq1z5eYc=s1600)

What did you observe? You can see that adding `[sm]` matches both $soon$ and $moon$. Here `[sm]` is called character class, which is basically a list of characters we want to match.

More formally, `[abc]` is basically either `a` or `b` or `c`.

Predict the output of the following:

1. **RegEx code:** ```[ABC][12]```
**Text:** A1 grade is the best, but I scored A2.

Answer:

![enter image description here](https://lh3.googleusercontent.com/2JgAwwprVtZ8AfQMLoB9PEi7NoyJXxrEqv_46tLvdtCBKo4HBcPlbi3atyKsWJTwJLBTneyA_C0j=s1600)


2. **RegEx code:** ```[0123456789][12345]:[abcdef][67890]:[0123456789][67890]:[1234589][abcdef]```
**Text:** Let's match 14:f6:89:3c mac address type of pattern. Other patterns are 51:a6:90:c5, 44:t6:u9:3d, 72:c8:39:8e.

Answer:

![enter image description here](https://lh3.googleusercontent.com/d2ynsBn5p8gIzvQeKewe8VrPiEu0EyOoNiEBkj_Co8fq_12FKhWK81V1Rcc2YCs3or9d4sCbuGtA=s1600)

Now, if we put `^`, then it will show a match for characters other than the ones in the bracket.

![soon moon noon woon](https://lh3.googleusercontent.com/rj-zgBEZ7Fdv6rckQgHC90L_j7y1X7jj8veTZQoOKGQ2RSiEHPxPeSZUZoJE9yLW-o2dvXj6OI1j=s1600)

Predict the output for the following:

 **RegEx code:** ```[^13579]A[^abc]z3[590*-]```
**Text:** 1Abz33 will match or 2Atz30 and 8Adz3*.

Answer:

![enter image description here](https://lh3.googleusercontent.com/BXaE8cxW7PcMJcfoUTlY-xBm9qNuhB5isy-PDLS5hIqQGIdRWiUf4viVxHF5yn5DJ0wHtoqHYKmP=s1600)


Writing every characters(like `[0123456789]` or `[abcd]`) is some what slow and also errorneous, what is the short-cut?

## Ranges
Ranges makes our work easier. Consecutive characters can simply be replaced by putting a dash between the first and last character.

![regex](https://lh3.googleusercontent.com/PWRFyDwe-89sdNSbmGc528PZXWhoX_-GNq0gQ8X9fOA-NX1Q4hzQNq1-Ty1LYjjsL8L4nVbSgvaq=s1600)

Predict the output of the following regex:

 **RegEx code:** ```[a-d][^l-o][12][^5-7][l-p]```
**Text:** co13i, ae14p, eo30p, ce33l, dd14l.

Answer:

![enter image description here](https://lh3.googleusercontent.com/pgDHTvxQZ35ybyF7ozdeSGEBchiK8huiMQ3PfQWIgPSrzWoca8BpEoQ1yht8qyA4VVOdP6dNa-sl=s1600)


**Note:** If you write the range in reverse order (ex. 9-0), then it is an error.

Predict the output of the following regex:

**RegEx code:** ``[a-zB-D934][A-Zab0-9]``
	**Text:** t9, da, A9, zZ, 99, 3D, aCvcC9.
Answer: 
![enter image description here](https://lh3.googleusercontent.com/ftl29tcq2QeaOCMpRs6kwEwtNYaxvTzkkLB-2SGi2WjkSWvUfAMmTTrE7NXtyORo8gaptghcnJQJ=s1600)

## Predefined Character Classes

 1. **`\w` & `\W`**: `\w` is just a short form of a character class `[A-Za-Z0-9_]`.

	![enter image description here](https://lh3.googleusercontent.com/UzEtYLNxnrtpDgOIW1N9SeyJ5Nyeh51hHIb516CwPOJutVSkWQZpcDfo09lSXmGzDMxDgtoikJAU=s1600)
	`\W` is equivalent to ``[^\w]``.
![enter image description here](https://lh3.googleusercontent.com/cKEXAPheBxESGkBoe8zOONJP3REvaTUhYs4FPkPizMU4t-v2_enG-9Jk8tgF-HX6Wxrn0jQATBes=s1600)

	
 2. **`\d` & `\D`**: `\d` matches any digit character. It is equivalent to character class `[0-9]`.

	![enter image description here](https://lh3.googleusercontent.com/Q1WTXPIBFR0fCJ7QT5jdU_XummS39Jqzi96l1g_ijg-LA4hoSLf05pscFT32lW-39yEPC5uDP-V_=s1600)
	`\D` is equivalent to ``[^\d]``.
![enter image description here](https://lh3.googleusercontent.com/JWIIzBQOIqi7lPIkrveW6h_gL1C5sWd_0cNGCswkBxRGoNKDB9ZKN4Zwd21BdEmfuluuzu-THYpc=s1600)
3. **`\s` & `\S`**: `\s` matches white space characters. Tab(`\t`), newline(`\n`) & space(` `) are whitespace characters.
	![enter image description here](https://lh3.googleusercontent.com/LbokzFHfw58rfmDUlcVoktdYHZtbWi76ddM-6-qyTiNVnk4s0Ea9KfC1KHRJkjTvDYRnbKXprkPr=s1600)

	Similarly, `\S` is equivalent to ``[^\s]``.
![enter image description here](https://lh3.googleusercontent.com/Vp2QdnqK-WOhuZaCZW82IBVNCPmVC--O2te2XzXKqCKwZJe4FKoJVHlzevhBgNfUSzF-34FcZFof=s1600)
	
 4. **dot(`.`)**: Dot matches any character except `\n`(line break or new line character) and `\r`(carriage-return character). It is known as **wildcard matching**.

	![enter image description here](https://lh3.googleusercontent.com/jwBp2XH1lL9ZRu_wASyTYsD03p81_3DIRjfHWtH5cA3jpSDuGfmE3P5A0RIhSfbrusmoV8w1D9k1=s1600)

**Note:** `\r` is known as windows style new line character.

Predict the output of the following regex:

1.  **RegEx code:** ``[01][01][0-1]\W\s\d``
	**Text:** Binary to decimal data: 001- 1, 010- 2, 011- 3, a01- 4, 100- 4.
Answer: 
![enter image description here](https://lh3.googleusercontent.com/YzmmRMcSqjhJPHthh_MwLnGldVl4nYR86Bb83viXeT2SM0koPmFjFKOathYXxxLyLKSz96Gkigcl=s1600)
2. **RegEx code:**
**Text:**


## Alternation (OR operator)

As we have seen **character class**, it can be used to match a single character out of several possible characters, Alternation is more generic. It can also be used to match an expression out of several possible expressions.

![enter image description here](https://lh3.googleusercontent.com/JxvB4lPgFBxk0FA-d3XapsLPad_JnhegB7NJ7BpRqmZkNuLwivUTAl08ek14EwpIM42LoIeB2O_c=s1600)

In the above example, ``cat|dog|lion`` basically means either cat or dog or lion. Here we have used specific patterns(cat, dog & lion) but we can use any regular expression. For example,

![enter image description here](https://lh3.googleusercontent.com/syg6gq9LBaQfA43tyVVlIqHd3oD0jbhBnxrLkho21EsD4DoUy2gGfJZoLgWaz0PA5BxWHghdybRD=s1600)

### Problem with OR operator: 
Suppose that you want to match two words either **Set** or **SetValue**. What will be the regular expression? 

From what ever we have learned till now, you will say ``Set|SetValue`` will be the answer. But it is not correct.

![enter image description here](https://lh3.googleusercontent.com/fcX6JOLw9u7YK0Sbeec_0tol5IbcxFHR4zlb3TSgCoMb3tlkZlGWCNd-9KNc832YMcuG7TcceJyz=s1600)

If you try `SetValue|Set`, then it is working. 

![enter image description here](https://lh3.googleusercontent.com/H8y8thO6EVan-NfxRKoGSEZG-ObgbX4EdfvHMJznr37m1Q-DekLpHMce3OqdAlje9jNQFy2ZK4u2=s1600)

Can you observe anything from it?

**OR operator** tries to match starting from the first word(in the expression), if it is a match, then it will not try to match next word(in the expression) at the same place in text.

Predict the output of the following regex:
1. **RegEx code:**
**Text:**

2. **RegEx code:**
**Text:**


## Quantifiers (Repetition)

We have seen that to match 3 digit patterns we can use ``[0-9][0-9][0-9]``. What if we have n digit patterns? We have to write `[0-9]` n times, but that is really waste of time. Here is when quantifiers comes for help.

 1. **Limiting repetitions(``{min, max}``):** To match n digit pattern we can simply write ``[0-9]{n}``. Instead of ``{n}`` by providing minimum and maximum values as ``[0-9]{min, max}``, we can match a pattern repeating min to max times.

	Let's see an example to match all numbers between 1 to 999.
![enter image description here](https://lh3.googleusercontent.com/i-Xd_gn0AYks2HX3HL-8kbVQWHaUzuuO5VO2ZoV5sqxIfFRyniKMEWNvM758zIfFb1ArY3q08dp5=s1600)
	**Note:** If you don't write the upper bound(``{min,}``), then it basically means, there is no limit for maximum repetitions.


 2. **``+`` quantifier:** It basically means ``{1,}``-at least one occurrence.
![enter image description here](https://lh3.googleusercontent.com/_f5hQYEghXft3ZttKB7r177rDXXT4m04TQlkjnsg-2E5fkUAOZNUxeLYvWIt6T7B2XLTeVUkoXu1=s1600)

 3. **``*``quantifier:** It is equivalent to ``{0,}``-zero or more occurrences.
Let's 
![enter image description here](https://lh3.googleusercontent.com/vGqELFywEUZ5jilWFotcN_l4IC0MCpg45TMAB2k3x80nAm6gn_2R9NB3h8KMiXNB6aG3HlZ2C0Hs=s1600)

4.  **``?`` quantifier:** It is equivalent to ``{0,1}``, either zero or one occurrence. ``?`` is very useful for optional occurrences in patterns.

	Let's see an example to match negative and positive numbers.
![enter image description here](https://lh3.googleusercontent.com/YBbsvb14Aoje2CB32deP6kszaZ0OcUWThaK71y5RZ7q6eqQ8H4EkL8XzZOB9IoSKB_Tav37lE__W=s1600)

**Nature of Quantifiers:**
HTML tag is represented as <tag_name>some text</tag_name>. For example, <title>Regular expression</title>

So can you figure out an expression that will match both <tag_name> & </tag_name>?

Most of the people will say, it is `<.*>`. But it gives different result.
![enter image description here](https://lh3.googleusercontent.com/dYECtAiwn0dWJwY0K8gzb6U_vrzoihid1bgJxEvHA3G64Wm49dM5BVl5V41AHb3D1MxQ_t1MNXhh=s1600)
So, rather than matching up till first `>`, it matches the whole tag. So, quantifiers are greedy by default. It is called **Greediness!**

To make it lazy, we use `?` quantifier. That stops the regex engine going further(makes it optional).
![enter image description here](https://lh3.googleusercontent.com/7Em674dudMFsnG-T5PiM8wpXBH8FOp3AW3o992orHzA49lO9muYkmAi4-NDKP4FV-Ay926fKdtEt=s1600)


Predict the output of the following regex:
1. **RegEx code:**
**Text:**

2. **RegEx code:**
**Text:**


**Note:**  Now you may be thinking, what if we want to match characters like ***, ?, +, {, },** etc in the text. We will look at it shortly. Keep reading!

## Boundary Matchers

Now, we will learn how to match pattern at specific positions, like before, after or between some characters. For this purpose we use special characters like `^`,`$`,`\b & \B`,`\A`,`\z & \Z`, which are known as anchors.


**Note:** 
- Line is a string which ends at line break character like, `\n` or `\r`.
- There is a slight change in javascript code we were using uptill now. Instead of `/____/g`, we will now use `/____/gm`. Modifier 'm' is used to perform multiline search. Notice it in next images!
- Word character can be represented by, `[A-Za-z0-9_]`.

 1. **Anchor `^`**: It is used to match patterns at the very start of a line.
For example,
![enter image description here](https://lh3.googleusercontent.com/AsEJmx-zVHGJAIOK7wzOpJLXC_EFtszcSvDE3ByluMDZkAh01Z6Z48n0LqZXLnjq0e7CiKqyXoWG=s1600)

	It will show a match only if the pattern is occuring at the start of the line.

 2. **Anchor `$`**: Similarly, ``$`` is used to match patterns at the very end of a line.

	![enter image description here](https://lh3.googleusercontent.com/iwj0YbwW5I5ocLglFFypayBFmNpHClc3Bew-DXer_XYhvhJ2QMd0z4ZFEpgc_sZqMFA91HgbkxYz=s1600)

	It will show a match only if the pattern is occuring at the end of a line.
Example using both `^` and `$`:
	![enter image description here](https://lh3.googleusercontent.com/udplrGsLdQkeEkwCZl06ZmqM7M-kSP18Lyk7w0qFqrB46EAZJhJalhQ3WbPPnzcNt4jeHJxlgAXi=s1600)


 3. **Anchors `\b` & `\B`**: `\b` is called **word boundary character**. 

	Let's first observe some examples:
![enter image description here](https://lh3.googleusercontent.com/RJqHdBX--517Xuq4MWDVoGsBoOFGIbWhqs8YOwWFU-LKjwSQLfVuQPHTgWjxU3rR54D6bg2TNxJu=s1600)
	
	
	What did you observe? Our pattern is starting and ending with word characters and so the match occurs only if the substring is starting(`[a-z]`) and ending(`\d`) at word characters which are required in our pattern-`[a-z]` and `\d` respectively.  Now let's look at one more example.	
	![enter image description here](https://lh3.googleusercontent.com/NYHZmEuDDxajsib_cG248-x-L1YgxAR-Tn3KqYgnOJSM1uk1EQgbjTHTL_E9C-tNVjQ1qIxZyU_e=s1600)

	What did you observe? 
	**First observation:** Our pattern is starting with a non-word character and ending with a word character. So the match occurs only if there is a word character before the starting of a match string and there is a required `\d` character at the end.

	**Second observation:**	One new thing to observe is that, If our pattern is starting(or ending) with a word character, then the match can still occur if there is a non-word character before(or after) the match string.

	
	`\b` need not be used in pair. You can use a single `\b`.
	
	`\B` is just a complement of `\b`.



**Note:** `\A` and `\z & \Z` are another anchors which are used to match at very start of input text and at very end of input text respectively. But it is not supported in Javascript.

Predict the output of the following regex:

1. **RegEx code:**
**Text:**

2. **RegEx code:**
**Text:**


## Groups & Capturing

Grouping is the most useful feature of regex. Grouping can be done by placing regular expression inside round brackets. 

It unifies the regular expressions inside it as a single unit. Let's look at its usages one by one:

1. It makes the regular expression more readable and sometimes it is an inevitable thing.
![enter image description here](https://lh3.googleusercontent.com/JVFtW5n8xGothhQa-MCzSV-oIEFM7zpjOJWDAOto_JrjQalqcEt29LtCT4m62FZHuVLgntRJVJYN=s1600)
Suppose we want to match both the sentences, then grouping is the inevitable thing.
![enter image description here](https://lh3.googleusercontent.com/CotGZFIfY0VW1yVHb2W2p7vqRaUmZXNLgS4IZoAOiPxU8O5813uR0LKGzmXUpkzfp6vVH1X1HE5T=s1600)

2. To apply quantifiers to one or more expressions.
![enter image description here](https://lh3.googleusercontent.com/cSn7JesNbcMaaXb_tFi1ymMlKtZxe7G09jROJtWuu7kPvUmAGOU_CDiVp9k0NQ8FuCistLgW4vUg=s1600)
Similarly, you can use other quantifiers.

3. To extract and replace substrings using groups. So we call groups **Capturing groups**, becuase we are capturing data(substrings) using groups.

	In this part we will see how to extract and replace data using groups in Javascript.

	In the output array, the first data is a match string followed by matched groups in the order.
	
	```js
	var str = "2020-01-20";

	// Pattern string
	var pattern = /(\d{4})-(\d{2})-(\d{2})/g;

	//                ^       ^       ^
	//group-no:	  1       2       3

	var result = pattern.exec(str);

	console.log(result);
	/* Output will be:
	[
	  '2020-01-20', //-------pattern
	  '2020', //-----First group
	  '01', //-------Second group
	  '20', //-------Third group
	  index: 0,
	  input: '2020-01-20',
	  groups: undefined
	]
	*/
	// Data extraction
	console.log(result[1]); // First group
	console.log(result[2]); // Second group
	console.log(result[3]);	// Third group
	```
	`Replace` is another function which is used to replace and rearrange the data using groups.
	
	```js
	var str = "2020-01-20";

	// Pattern string
	var pattern = /(\d{4})-(\d{2})-(\d{2})/g;

	//                ^       ^       ^
	//group-no:	  1       2       3

	// Data replacement
	var ans=str.replace(pattern, '$3-$2-$1');

	console.log(ans);
	// Output will be: 20-01-2020
	```

	Predict the output of the following regex:
	1. **RegEx code:**
**Text:**

	2. **RegEx code:**
**Text:**


## Characters with special meaning

We have seen that we are using `*`, `+`, `.`, `$`, etc for different purposes. Now, you may be thinking, what if we want to match them themselves. For that purpose, we have to escape them using escape character(backslash-\\) .

Below is the table for these kind of characters and their escaped version, along with their usages.

| Character |            Usage            | Escaped version |
|:---------:|:---------------------------:|:---------------:|
|     \     |       escape character      |        \\\       |
|     .     |  predefined character class |        \\.       |
|     \|     |         OR operator         |        \\\		 |       
|    *      |        as quantifier        |        \\*       |
|     +     |        as quantifier        |        \\+       |
|     ?     |        as quantifier        |        \\?       |
|    ^      |       boundary matcher      |        \\^       |
|    $      |       boundary matcher      |        \\$       |
|    {      |    in quantifier notation   |        \\{       |
|    }      |    in quantifier notation   |        \\}       |
|    [      | in character class notation |        \\[       |
|     ]     | in character class notation |        \\]       |
|    (      |      in group notation      |        \\(       |
|    )      |      in group notation      |        \\)       |

Sometimes, it is also preferred to use escaped forward slash(`/`).


## Backreferencing

Backreferencing is used to match same text again. Backreferences match the same text as previously matched by a capturing group. Let's look at an example:

![enter image description here](https://lh3.googleusercontent.com/VrwREOtqL_b2IPbzM2qJQVAiP9Q8XWoAny41UodrLlEzWBxUbOJZ3WTvR7T0b-9zHn7iOqN8op3l=s1600)

The first captured group is (`\w+`), now we can use this group again by using a backreference (`\1`), at the closing tag, which matches the same text as in captured group `\w+`. 

You can use backreferencing for any captured group as \group_no. 

Let's have one more example:

![enter image description here](https://lh3.googleusercontent.com/Wx30vdBz2zif4zqMt1P6rJIh9b3NBOWz0XMzGZR50gU5n8p4sxhtCRWYl1j5hWYfJpI6jC5VEDEX=s1600)

Predict the output of the following regex:
1. **RegEx code:**
**Text:**

2. **RegEx code:**
**Text:**




## Practical Applications of RegEx 
1. Syntax highlighting systems
2. Data scraping and wrangling.
3. In find and replace facility of text editors
