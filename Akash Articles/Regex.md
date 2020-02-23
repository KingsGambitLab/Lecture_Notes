## Regular Expression (RegEx)

While filling online forms, haven't you come across errors like "Please enter valid email address" or "Please enter valid phone number".

Annoying as they may be, there's a lot of black magic that the computer does before it determines that, the details you've entered are incorrect.

Can you think out, what is that black magic? If you are familiar with algorithms, then you will say we can write an algorithm for the same.

Yes, we can write an algorithm to verify different things. But we have a standard tool, which is particularly designed for the similar kind of purposes.

It is **Regular Expression**. We call it **RegEx** for short. RegEx makes our work a lot easier. Let's see some basic examples where RegEx becomes handy.

Suppose, you are in search of an averge price of a particular product on amazon. The following regular expression will find you any price(ex. `$12`, `$75.50`) on the webpage: `\$([0-9]+)\.([0-9]+)`.

Quite interesting!

Let's look at another example. You have a long list of documents with different kinds of extensions. You are particularly looking for data files having **.dat** extension. 

`^.*\.dat$` is a regular expression which represents a set of string ending with **.dat**. Regular expression is a standardized way to encode such patterns. 

Well. What does the name **Regular Expression(RegEx)** represent? Regular Expression represents the sequence of characters that defines a regular search pattern.

RegEx is a standardized tool to do the following works:
1. Find and verify patterns in a string.
2. Extract particular data present in the text.
3. Replace, split and rearrange particular parts of a string.

We are going to look at all the three things above.

Let's begin the journey with RegEx!

**Note:** 
1. In all the images below, the first section is a RegEx and below is a text, in which the matches are shown-the shaded regions show the match. All the images are taken using regexr.com. You can use it to do  experiments on regex.
2. In all the images, Small dot between words in the text shows a space.
3. **Alpha-numeric character** belongs to anyone of the $0-9,A-Z,a-z$ ranges.
4. String is a sequence of characters and substring is a contiguous part of a string.

## Simple Alpha-numeric character matching

Simple matching of a specific word can be done as the following:

![enter image description here](https://lh3.googleusercontent.com/YGfz9u58rRKD0ABrSKDv7ZJOEMaIMGdFWgJWGGNzCFNakCtfAZVk1UEm7mBS4lIX1LFXoV420cmY=s1600)

As you can see it matches "Reg" in the text. Similarly, what will be the match for "Ex" in the same text above?

![enter image description here](https://lh3.googleusercontent.com/LkJXO79wn08dvgX5Q2JXHtyN7MW38AeNdV7fjG6lk7MNsiamx9iOekEGQg-WS9OLQMWxBuspjSkh=s1600)

Do you notice anything? It is a **case sensitive**.

**Note:** Most of the programming languages have libraries for RegEx. They have almost similar kind of syntax. Here, we will see how to implement it in **Javascript**.

Below is a basic code in Javascript for regex. The patterns are written in `/_____/g`. Where `g` is a modifier, which is used to find all matches rather than stopping at the first match.

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

**Note:** **Groups** in the above output is a RegEx concept. We will look at it, keep reading.

Now, you can change the expression and text in the code above, to observe other patterns.

## Character classes:

![IMG](https://lh3.googleusercontent.com/dlLzL3teyEoax1JsdF7JeGP6DZOJll-UgnZqFkJtBeAVJhM1xMnXBHVeJYf_cUFLmj-f1qPO8asf=s1600)

What if you want to match both "soon" and "moon" or basically words ending with "oon"?

![enter image description here](https://lh3.googleusercontent.com/bsRHqYuPZIQ7Yra4-zyF1BX2pIYDukCEtTfCK3rjaCTRmTAuo_fuHTVK5sJjbTdbXjGTVq1z5eYc=s1600)

What did you observe? You can see that, adding `[sm]` matches both $soon$ and $moon$. Here `[sm]` is called character class, which is basically a list of characters we want to match.

More formally, `[abc]` is basically 'either a or b or c'.

Predict the output of the following:

1. **RegEx:** ``[ABC][12]``
**Text:** A1 grade is the best, but I scored A2.

	Answer:
	![enter image description here](https://lh3.googleusercontent.com/2JgAwwprVtZ8AfQMLoB9PEi7NoyJXxrEqv_46tLvdtCBKo4HBcPlbi3atyKsWJTwJLBTneyA_C0j=s1600)


2. **RegEx:** ```[0123456789][12345]:[abcdef][67890]:[0123456789][67890]:[1234589][abcdef]```
**Text:** Let's match 14:f6:89:3c mac address type of pattern. Other patterns are 51:a6:90:c5, 44:t6:u9:3d, 72:c8:39:8e.

	Answer:

	![enter image description here](https://lh3.googleusercontent.com/d2ynsBn5p8gIzvQeKewe8VrPiEu0EyOoNiEBkj_Co8fq_12FKhWK81V1Rcc2YCs3or9d4sCbuGtA=s1600)

Now, if we put `^`, then it will show a match for characters other than the ones in the bracket.

![soon moon noon woon](https://lh3.googleusercontent.com/rj-zgBEZ7Fdv6rckQgHC90L_j7y1X7jj8veTZQoOKGQ2RSiEHPxPeSZUZoJE9yLW-o2dvXj6OI1j=s1600)

Predict the output for the following:

**RegEx:** ```[^13579]A[^abc]z3[590*-]```
**Text:** 1Abz33 will match or 2Atz30 and 8Adz3*.

Answer:

![enter image description here](https://lh3.googleusercontent.com/BXaE8cxW7PcMJcfoUTlY-xBm9qNuhB5isy-PDLS5hIqQGIdRWiUf4viVxHF5yn5DJ0wHtoqHYKmP=s1600)

Writing every character (like `[0123456789]` or `[abcd]`) is somewhat slow and also erroneous, what is the short-cut?

## Ranges
Ranges makes our work easier. Consecutive characters can simply be replaced by putting a dash between the smallest and largest character.

For example, `abcdef` --> `a-f`, `456` --> `4-6`, `abc3456` --> `a-c3-6`, `c367980` --> `c36-90`.

![regex](https://lh3.googleusercontent.com/PWRFyDwe-89sdNSbmGc528PZXWhoX_-GNq0gQ8X9fOA-NX1Q4hzQNq1-Ty1LYjjsL8L4nVbSgvaq=s1600)

Predict the output of the following regex:

1. **RegEx:** ```[a-d][^l-o][12][^5-7][l-p]```
**Text:** co13i, ae14p, eo30p, ce33l, dd14l.

	Answer:
	![enter image description here](https://lh3.googleusercontent.com/pgDHTvxQZ35ybyF7ozdeSGEBchiK8huiMQ3PfQWIgPSrzWoca8BpEoQ1yht8qyA4VVOdP6dNa-sl=s1600)


	**Note:** If you write the range in reverse order (ex. 9-0), then it is an error.

2. **RegEx:** ``[a-zB-D934][A-Zab0-9]``
	**Text:** t9, da, A9, zZ, 99, 3D, aCvcC9.
Answer: 
![enter image description here](https://lh3.googleusercontent.com/ftl29tcq2QeaOCMpRs6kwEwtNYaxvTzkkLB-2SGi2WjkSWvUfAMmTTrE7NXtyORo8gaptghcnJQJ=s1600)



## Predefined Character Classes

 1. **`\w` & `\W`**: `\w` is just a short form of a character class `[A-Za-Z0-9_]`. `\w` is called word character class.

	![enter image description here](https://lh3.googleusercontent.com/UzEtYLNxnrtpDgOIW1N9SeyJ5Nyeh51hHIb516CwPOJutVSkWQZpcDfo09lSXmGzDMxDgtoikJAU=s1600)
	`\W` is equivalent to ``[^\w]``. `\W` matches everything other than word characters.
![enter image description here](https://lh3.googleusercontent.com/cKEXAPheBxESGkBoe8zOONJP3REvaTUhYs4FPkPizMU4t-v2_enG-9Jk8tgF-HX6Wxrn0jQATBes=s1600)

	
 2. **`\d` & `\D`**: `\d` matches any digit character. It is equivalent to character class `[0-9]`.
	![enter image description here](https://lh3.googleusercontent.com/Q1WTXPIBFR0fCJ7QT5jdU_XummS39Jqzi96l1g_ijg-LA4hoSLf05pscFT32lW-39yEPC5uDP-V_=s1600)
	`\D` is equivalent to ``[^\d]``. `\D` matches everything other than digits.
![enter image description here](https://lh3.googleusercontent.com/JWIIzBQOIqi7lPIkrveW6h_gL1C5sWd_0cNGCswkBxRGoNKDB9ZKN4Zwd21BdEmfuluuzu-THYpc=s1600)

3. **`\s` & `\S`**: `\s` matches whitespace characters. Tab(`\t`), newline(`\n`) & space(` `) are whitespace characters. These characters are called non-printable characters.
	![enter image description here](https://lh3.googleusercontent.com/LbokzFHfw58rfmDUlcVoktdYHZtbWi76ddM-6-qyTiNVnk4s0Ea9KfC1KHRJkjTvDYRnbKXprkPr=s1600)

	Similarly, `\S` is equivalent to ``[^\s]``. `\S` matches everything other than whitespace characters.
![enter image description here](https://lh3.googleusercontent.com/Vp2QdnqK-WOhuZaCZW82IBVNCPmVC--O2te2XzXKqCKwZJe4FKoJVHlzevhBgNfUSzF-34FcZFof=s1600)
	
 4. **dot(`.`)**: Dot matches any character except `\n`(line-break or new-line character) and `\r`(carriage-return character). Dot(`.`) is known as a **wildcard**.
	![enter image description here](https://lh3.googleusercontent.com/jwBp2XH1lL9ZRu_wASyTYsD03p81_3DIRjfHWtH5cA3jpSDuGfmE3P5A0RIhSfbrusmoV8w1D9k1=s1600)

**Note:** `\r` is known as a windows style new-line character.

Predict the output of the following regex:

1.  **RegEx:** ``[01][01][0-1]\W\s\d``
	**Text:** Binary to decimal data: 001- 1, 010- 2, 011- 3, a01- 4, 100- 4.
Answer: 
![enter image description here](https://lh3.googleusercontent.com/YzmmRMcSqjhJPHthh_MwLnGldVl4nYR86Bb83viXeT2SM0koPmFjFKOathYXxxLyLKSz96Gkigcl=s1600)

### Problems

1. Write a regex to match 28th February of any year. Date is in dd-mm-yyyy format.

	Answer: `28-02-\d\d\d\d`

2. Write a regex to match dates that are not in March. Consider that, the dates are valid and no proper format is given, i.e. it can be in dd.mm.yyyy, dd\mm\yyyy, dd/mm/yyyy format.

	Answer: `\d\d\W[10][^3]\W\d\d\d\d`

	Note that, the above regex will also match dd-mm.yyyy or dd/mm\yyyy kind of wrong format, this problem can be solved by using backreferencing.


## Alternation (OR operator)

**Character class** can be used to match a single character out of several possible characters. Alternation is more generic than character class. It can also be used to match an expression out of several possible expressions.

![enter image description here](https://lh3.googleusercontent.com/JxvB4lPgFBxk0FA-d3XapsLPad_JnhegB7NJ7BpRqmZkNuLwivUTAl08ek14EwpIM42LoIeB2O_c=s1600)

In the above example, ``cat|dog|lion`` basically means 'either cat or dog or lion'. Here, we have used specific expression(cat, dog & lion), but we can use any regular expression. For example,

![enter image description here](https://lh3.googleusercontent.com/syg6gq9LBaQfA43tyVVlIqHd3oD0jbhBnxrLkho21EsD4DoUy2gGfJZoLgWaz0PA5BxWHghdybRD=s1600)

### Problem
- Find a regex to match boot or bot.
 Answer: There more than one possible answers: `boot|bot`, `b(o|oo)t`. Last expression is using a group.


### Problem with OR operator: 
Suppose, you want to match two words **Set** and **SetValue**. What will be the regular expression?

From whatever we have learned so far, you will say, ``Set|SetValue`` will be the answer. But it is not correct.

![enter image description here](https://lh3.googleusercontent.com/fcX6JOLw9u7YK0Sbeec_0tol5IbcxFHR4zlb3TSgCoMb3tlkZlGWCNd-9KNc832YMcuG7TcceJyz=s1600)

If you try `SetValue|Set`, then it is working. 

![enter image description here](https://lh3.googleusercontent.com/H8y8thO6EVan-NfxRKoGSEZG-ObgbX4EdfvHMJznr37m1Q-DekLpHMce3OqdAlje9jNQFy2ZK4u2=s1600)

Can you observe anything from it?

**OR operator** tries to match a substring starting from the first word(or expression)-in the regex. If it is a match, then it will not try to match the next word(or expression) at the same place in text.

Find out an regex which matches each and every word in the following set: `{bat, cat, hat, mat, nat, oat, pat, Pat, ot}`. The regex should be as small as possible.

**Hint:** Use character-class, ranges and or-operator together.

Answer: `[b-chm-pP]at|ot`

## Quantifiers (Repetition)

To match 3 digit patterns, we can use ``[0-9][0-9][0-9]``. What if we have n digit patterns? We have to write `[0-9]` n times, but that is a waste of time. Here is when quantifiers come for help.

 1. **Limiting repetitions(``{min, max}``):** To match n digit patterns, we can simply write ``[0-9]{n}``. Instead of n, by providing minimum and maximum values as ``[0-9]{min, max}``, we can match a pattern repeating min to max times.

	Let's see an example to match all numbers between 1 to 999.
![enter image description here](https://lh3.googleusercontent.com/i-Xd_gn0AYks2HX3HL-8kbVQWHaUzuuO5VO2ZoV5sqxIfFRyniKMEWNvM758zIfFb1ArY3q08dp5=s1600)
	**Note:** If you don't write the upper bound(``{min,}``), then it basically means, there is no limit for maximum repetitions.

 2. **``+`` quantifier:** It is equivalent to ``{1,}``-at least one occurrence.
![enter image description here](https://lh3.googleusercontent.com/_f5hQYEghXft3ZttKB7r177rDXXT4m04TQlkjnsg-2E5fkUAOZNUxeLYvWIt6T7B2XLTeVUkoXu1=s1600)

 3. **``*``quantifier:** It is equivalent to ``{0,}``-zero or more occurrences.	![enter image description here](https://lh3.googleusercontent.com/vGqELFywEUZ5jilWFotcN_l4IC0MCpg45TMAB2k3x80nAm6gn_2R9NB3h8KMiXNB6aG3HlZ2C0Hs=s1600)

4.  **``?`` quantifier:** It is equivalent to ``{0,1}``, either zero or one occurrence. ``?`` is very useful for optional occurrences in patterns.

	Let's see an example to match negative and positive numbers.
![enter image description here](https://lh3.googleusercontent.com/YBbsvb14Aoje2CB32deP6kszaZ0OcUWThaK71y5RZ7q6eqQ8H4EkL8XzZOB9IoSKB_Tav37lE__W=s1600)
	
### Problems

1. Find out a regex to match positive integers or floating point numbers with exactly two characters after the decimal point.

	Answer: `\d+(\.\d\d)?`

2. Predict the output of the following regex:
RegEx: `[abc]{2,}`
Text: 
<code>aaa
abc
abbccc
avbcc
</code>

	Answer: 
![enter image description here](https://lh3.googleusercontent.com/Uo7nokSqOEM8zLuOuA2a56q74vvBUmvmNQiUjdPSfn2H9yzTVRAW2DZlfCEsOaZJxhWg7tIdBLcv=s1600)

**Nature of Quantifiers:**
HTML tag is represented as <tag_name>some text</tag_name>. For example, `<title>Regular expression</title>`

So, can you figure out an expression that will match both <tag_name> & </tag_name>?

Most of the people will say, it is `<.*>`. But it gives different result.
![enter image description here](https://lh3.googleusercontent.com/dYECtAiwn0dWJwY0K8gzb6U_vrzoihid1bgJxEvHA3G64Wm49dM5BVl5V41AHb3D1MxQ_t1MNXhh=s1600)
So, rather than matching up till first `>`, it matches the whole tag. So, quantifiers are greedy by default. It is called **Greediness!**

Now, if we use `?`, then following happens.
![enter image description here](https://lh3.googleusercontent.com/7Em674dudMFsnG-T5PiM8wpXBH8FOp3AW3o992orHzA49lO9muYkmAi4-NDKP4FV-Ay926fKdtEt=s1600)

### Lazy matching:
As we have seen, the default nature of quantifier is greedy, so it will match as many characters as possible.

![enter image description here](https://lh3.googleusercontent.com/ye_RJ7Gc34O3BL6zMFEFodtbHsrK9hnwfQ3sxYWkrDHHdUtR6JvOcPT77kKMaNtn3IJonpmWNz1E=s1600)

To make it lazy, we use `?` quantifier, which turns the regex engine to match as less characters as possible which satisfies the regex.
![enter image description here](https://lh3.googleusercontent.com/tHhbib6sbPqxvj9Or7SB2Gk6ODGjzwuAS0NOSi0FUb60SRaoc8RuxyGcGJqqWbInHmP6Z0eiQRua=s1600)

**Note:** Now, you may be thinking, what if we want to match characters like `*, ?, +, {, }` in the text. We will look at it shortly. Keep reading!

Predict the output of the following regex:

1. Predict the output of the following regex: 
RegEx: `(var|let)\s[a-zA-Z0-9_]\w* =\s"?\w+"?;`
	Text: 
	<code>var carname = "volvo";
console.log(carname);
let age = 8;
var date = "23-03-2020";</code>

	Answer: 
	![enter image description here](https://lh3.googleusercontent.com/svrWV_MmE9x6WNVelmFRArJ-cvsY6VgUIUhT74KsvG0wdyifVmgOoMitGZHJ-ZjM1zgCJH6ID-S3=s1600)

## Boundary Matchers

Now, we will learn how to match patterns at specific positions, like before, after or between some characters. For this purpose we use special characters like `^`,`$`,`\b & \B`,`\A`,`\z & \Z`, which are known as anchors.

**Notes:** 
 - Line is a string which ends at a line-break or a new-line character `\n`.
 - There is a slight change in javascript code, we were using up till now. Instead of `/____/g`, we will now use `/____/gm`. Modifier 'm' is used to perform multiline search. Notice it in next images!
 - Word character can be represented by, `[A-Za-z0-9_]`.

 - **Anchor `^`**: It is used to match patterns at the very start of a line.
For example,
![enter image description here](https://lh3.googleusercontent.com/AsEJmx-zVHGJAIOK7wzOpJLXC_EFtszcSvDE3ByluMDZkAh01Z6Z48n0LqZXLnjq0e7CiKqyXoWG=s1600)

	It will show a match, only if the pattern is occuring at the start of the line.

 - **Anchor `$`**: Similarly, ``$`` is used to match patterns at the very end of a line.
	![enter image description here](https://lh3.googleusercontent.com/iwj0YbwW5I5ocLglFFypayBFmNpHClc3Bew-DXer_XYhvhJ2QMd0z4ZFEpgc_sZqMFA91HgbkxYz=s1600)

	It will show a match, only if the pattern is occuring at the end of a line.

	Example, both `^` and `$`,
	![enter image description here](https://lh3.googleusercontent.com/udplrGsLdQkeEkwCZl06ZmqM7M-kSP18Lyk7w0qFqrB46EAZJhJalhQ3WbPPnzcNt4jeHJxlgAXi=s1600)


 - **Anchors `\b` & `\B`**: `\b` is called **word boundary character**. 

	Below is a list of positions, which qualifies as a **boundary** for `\b`:
	If Regex-pattern is ending(or starting) with,
	- A word character, then boundary is itself(word character). Let's call it a word boundary.
	- A non-word character, then boundary is the next word-character. Let's call it a non-word boundary.

	So, in short `\b` is only looking for word-character at boundaries, so it is called **word boundary character**.

	Let's first observe some examples to understand it's working:
![enter image description here](https://lh3.googleusercontent.com/RJqHdBX--517Xuq4MWDVoGsBoOFGIbWhqs8YOwWFU-LKjwSQLfVuQPHTgWjxU3rR54D6bg2TNxJu=s1600)
	
	What did you observe? Our regex-pattern is starting and ending with a word character. So, the match occurs only if there is a substring starting and ending at word characters, which are required in our regex `[a-z]` and `\d` respectively.

	Now, let's look at one more example.
	![enter image description here](https://lh3.googleusercontent.com/NYHZmEuDDxajsib_cG248-x-L1YgxAR-Tn3KqYgnOJSM1uk1EQgbjTHTL_E9C-tNVjQ1qIxZyU_e=s1600)
Here `\+` will show a match for `+`.

	What did you observe? 
	**First observation:** Our pattern is starting with a non-word character and ending with a word character. So, the match occurs only if there is a substring having a non-word boundary at starting and word boundary at the ending.

	**Second observation:**	Non-word character after a word-boundary does not affect the result.	

	`\b` need not be used in pair. You can use a single `\b`. 

	![enter image description here](https://lh3.googleusercontent.com/ZQWwiNznl_P_foHiLgoxmwN7b0xRN54qMHUk9B4wSuiDDKSWdkOY9rjSwjTGvbEWKqptvLG2i_Rk=s1600)

	`\B` is just a complement of `\b`. `\B` matches at all the positions that is not a word boundary. Observe two examples below:
		![enter image description here](https://lh3.googleusercontent.com/gDCZqZbdNHcP9XetuE8hqx_7BLE2rh27Z1Bnz-SPUKJmj-_qEdFrXfP4xCzpPCxA7RYN1ZP6L0Zk=s1600)

	![enter image description here](https://lh3.googleusercontent.com/ucV3anQWFfYhO7qaXcU7-25bqR3W7KO87aSCVcd_GDMFtfEvWmqK-JvC0jJ62KQevzfhPdn4DMTC=s1600)

**Note:** `\A` and `\z & \Z` are another anchors, which are used to match at the very start of input text and at very end of input text respectively. But it is not supported in Javascript.

Predict the output of the following regex:

1. **RegEx:** ```^[\w$#%@!&^*]{6,18}$```
**Text:**
<code>This is matching passwords of length between 6 to 18:
Abfah45$
gadfaJ%33
Abjapda454&1 spc
bjaphgu12$
Note that no whitespace characters are allowed.</code>
Answer: 
![enter image description here](https://lh3.googleusercontent.com/bsQ8pb1a2tBRUHfE8ul2wiJ_7rRQjilptThKAy2WY2P0ndudVI8UEsiyn8eXLGbRvY6hj7Fdg6GM=s1600)

2. RegEx: `\b\w+:\B`
Text: <code>1232: , +1232:, abc:, abc:a, abc89, (+abc::)</code>
Answer: ![enter image description here](https://lh3.googleusercontent.com/TgLgYDWKd9wbBmzzq1_m-CRh4t5ndAoLnB-6nH0kWTpJSkZk9ePhH_5j2uFByAzxLUSlGeeLf5HR=s1600)

## Groups & Capturing

Grouping is the most useful feature of regex. Grouping can be done by placing regular expression inside round brackets. 

It unifies the regular expressions inside it as a single unit. Let's look at its usages one by one:

1. It makes the regular expression more readable and sometimes it is an inevitable thing.
![enter image description here](https://lh3.googleusercontent.com/JVFtW5n8xGothhQa-MCzSV-oIEFM7zpjOJWDAOto_JrjQalqcEt29LtCT4m62FZHuVLgntRJVJYN=s1600)
Suppose, we want to match both the sentences in the above text, then grouping is the inevitable thing.
![enter image description here](https://lh3.googleusercontent.com/_LLeROC6R9eAel9CF-FpwRvm4T2styQe60Qv4Zokhvky_6pbGrLJSWYd5TLaz5NwB6zaOwd3fKmX=s1600)

2. To apply quantifiers to one or more expressions.
![enter image description here](https://lh3.googleusercontent.com/cSn7JesNbcMaaXb_tFi1ymMlKtZxe7G09jROJtWuu7kPvUmAGOU_CDiVp9k0NQ8FuCistLgW4vUg=s1600)
Similarly, you can use other quantifiers.

3. To extract and replace substrings using groups. So, we call groups **Capturing groups**, becuase we are capturing data(substrings) using groups.

	In this part, we will see how to extract and replace data using groups in Javascript.

	**Data Extraction:**
	
	Observe the code below.
	```js
	var str = "2020-01-20";

	// Pattern string
	var pattern = /(\d{4})-(\d{2})-(\d{2})/g;

	//                ^       ^       ^
	//group-no:	  1       2       3

	var result = pattern.exec(str);

	// printing
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
	In the output array, the first data is a match string followed by the matched groups in the order.
	
	**Data Replacement:**
	
	`Replace` is another function, which can be used to replace and rearrange the data using regex. Observe the code below.
	
	```js
	var str = "2020-01-20";

	// Pattern string
	var pattern = /(\d{4})-(\d{2})-(\d{2})/g;

	//                ^       ^       ^
	//group-no:	  1       2       3

	// Data replacement using $group_no
	var ans=str.replace(pattern, '$3-$2-$1');

	console.log(ans);
	// Output will be: 20-01-2020
	```
	As you can see, we have used `$group_no` to indicate the capturing group.

Predict the output of the following regex:

1. RegEx: `([abc]){2,}(one|two)`
Text: 
<code>aone
cqtwo
abone
actwo
abcbtwoone
abbcccone
</code>

	Answer: ![enter image description here](https://lh3.googleusercontent.com/oPAS6ExWeAQoTEc7GRnrd4iuCmeSZt1-6Jv58t1_clZgHkpT9U1qPJFEXE780Bdz9oTeypFEgpRy=s1600)

2. RegEx: `([\dab]+(r|c)){2}`
Text: 
<code>1r2c
ar4ccc
12abr12abc
acac, accaca, acaaca
aaar1234234c, aaa1234234c
194brar, 134bcbb-c </code>

	Answer: ![enter image description here](https://lh3.googleusercontent.com/7t717TZSxuWDD92l58z8v0zInRNqiGvdP1q_AGPrN419PfxrMsHj27SaliwSC6EK2KZHWWvsr___=s1600)



## Characters with special meaning

We have seen that, we are using `*`, `+`, `.`, `$`, etc for different purposes. Now, if we want to match them themselves, we have to escape them using escape character(backslash-\\) .

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
| -|range operator | NA

Sometimes, it is also preferred to use escaped forward slash(`/`).

## Backreferencing

Backreferencing is used to match same text again. Backreferences match the same text as previously matched by a capturing group. Let's look at an example:

![enter image description here](https://lh3.googleusercontent.com/VrwREOtqL_b2IPbzM2qJQVAiP9Q8XWoAny41UodrLlEzWBxUbOJZ3WTvR7T0b-9zHn7iOqN8op3l=s1600)

The first captured group is (`\w+`), now we can use this group again by using a backreference (`\1`) at the closing tag, which matches the same text as in captured group `\w+`.

You can backreference any captured group by using `\group_no`.

Let's have two more examples:

![enter image description here](https://lh3.googleusercontent.com/Wx30vdBz2zif4zqMt1P6rJIh9b3NBOWz0XMzGZR50gU5n8p4sxhtCRWYl1j5hWYfJpI6jC5VEDEX=s1600)

![enter image description here](https://lh3.googleusercontent.com/Ji2buSF895THR4SIILfEou2SJMmuFExrpJsG8xWoxPSl6O-hDv7wPOHP1b_145NYh-M0yQYe0BxE=s1600)

**Problems:**

1. Match any palindrome string of length 6, having only lowercase letters.
Answer: `([a-z])([a-z])([a-z])\3\2\1`

2. RegEx: `(\w+)oo\1le`
Text: `google, doodle jump, ggooggle, ssoosle`

	Answer: 
![enter image description here](https://lh3.googleusercontent.com/y_4mk8QPlH0dWWqzXVhm5_V9wZlieX36x_sPTfX_Tr86l5SFD0so0ejYXD2dy2BiadXWHGVzxfkW=s1600)

**Note:** For group numbers more than 9, there is a syntax difference.

## Named Groups
Regular expressions with lots of groups and backreferencing can be difficult to maintain, as adding or removing a capturing group in the middle of the regex turns to change the numbers of all the groups that follow the added or removed group.

In regex, we have facility of named groups, which solves the above issue. Let's look at it.

We can name a group by putting `?<name>` just after opening the paranthesis representing a group. For example, `(?<year>\d{4})` is a named group.

Below is a code, we have already looked in **capturing groups** part. You can see, the code is more readable now.

```js
	var str = "2020-01-20";

	// Pattern string
	var pattern = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/g;

	//                ^       ^       ^
	//group-no:	  1       2       3

	// Data replacement using $<group_name>
	var ans=str.replace(pattern, '$<day>-$<month>-$<year>');

	console.log(ans);
	// Output will be: 20-01-2020
```

Backreference syntax for numbered groups works for named capture groups as well. `\k<name>` matches the string that was previously matched by the named capture group `name`, which is a standard way to backreference named group.

![enter image description here](https://lh3.googleusercontent.com/GbalU1cVIs8G5kP_pTXBj8eC1MF1M3vNVFaeAvnFcVyOUPg7mhBDoVu8nye9oC4inIg_4Vnzst1y=s1600)

## Practical Applications of RegEx 
1. Syntax highlighting systems
2. Data scraping and wrangling
3. In find and replace facility of text editors

Now that, you have learned RegEx. Let's look at some classical examples of RegEx.

## Classical examples

1. **Number Ranges:**
Can you find a regex matching all integers from 0 to 255?

	First, Let's look at how can we match all integers from 0 to 59:
	![enter image description here](https://lh3.googleusercontent.com/my4yBp9jXoS3wHCjkL_OVD3EjmsUtj61hIWKCssvS5PH0et26vbhhSIoM5Jphx-FVwK6yvc0qT7u=s1600)

	As you can see, we have used `?` quantifier to make the first digit(0-5) optional. Now, can you solve it for 0-255?

	Hint : Use OR operator.

	We can divide the range 0-255 into three ranges: 0-199, 200-249 & 250-255. Now, creating an expression, for each of them independently, is easy.
	
	|	Range| RegEx |
	|	:--:	|	:--:	|
	| 0-199 | `[01][0-9][0-9]` |
	| 200-249| `2[0-4][0-9]`|
	| 250-255| `25[0-5]`|

	
	Now, by using OR operator, we can match the whole 0-255 range.
	
	![enter image description here](https://lh3.googleusercontent.com/ao-aGXzSqOsICjuE8DlAmTtNCvMWVHKeStYMlccX3ounTHaTlI4qLNhAcm7jM_3P0FPAjXi0k2zB=s1600)

    As you can see, the above regex is not going to match 0, but 000. So, how can you modify the regex which matches 0 as well, rather than matching 001 only?
    
	![enter image description here](https://lh3.googleusercontent.com/qxfoJm05roxaS3FwOoTy0Nr88Ku2KvZPHRUl7_HB5ybcpUhLspgQAbitJjvV-J5Gi4OG2upbTl9K=s1600)

	We have just used `?` quantifier.

2. **Validate an IP address:**

	IP address consists of digits from 0-255 and 3 points(`.`). Valid IP address format is (0-255).(0-255).(0-255).(0-255).

	For example, 10.10.11.4, 255.255.255.255, 234.9.64.43, 1.2.3.4 are Valid IP addresses.

	Can you find a regex to match an IP-address?

	We have already seen, how to match number ranges and to match a point, we use escaped-dot(`\.`). But in IP address, we don't allow leading zeroes in numbers like 001. 

	So, We have to divide the range in four sub-ranges: 0-99, 100-199, 200-249, 250-255. And finally we use OR-operator.
	
	![enter image description here](https://lh3.googleusercontent.com/UXWulQq4P0STobfIjrW4Um5jaqwSqTPx3KSSYYvEg_HZJ22a5wNQYio3qQUtzgidIOxLO_M48M9p=s1600)

	So, Regex to match IP Address is as below:
	![enter image description here](https://lh3.googleusercontent.com/n2CaC-8Q8NH-H5RkDrCM4AQQkV2PamIAlA3dwljdRsW33WWoj18qJEIN5iyzjLzfifHj-dh-IW-u=s1600)
	
	**Note:** The whole expression is contiguous, for the shake of easy understanding it is shown the way it is.

### Bonus Problem:

Predict the output of the following regex:

**RegEx:** ``\b(0|(1(01*0)*1))*\b``
**Text:** This RegEx denotes the set of binary numbers divisible by 3:
0,11,1010, 1100, 1111, 1001

Answer: 

![enter image description here](https://lh3.googleusercontent.com/d4c8LeDk2JahKEQXXkMfPwDoDEmO6ijmqd4u3aHDUJ9_At1DZY95HSGZMPbJPn4Mptlfp3p1XZ4x=s1600)
