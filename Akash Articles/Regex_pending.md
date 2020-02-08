## Regular Expression (RegEx)

You may have noticed that, when you are filling a form it is showing you an error like, "Please enter valid email address" or "Please enter valid phone number". Do you know how that can be verified? You will say, yes, that can be done simply by writing an algorithm for it, Right?

You can create an algorithm to verify the pattern of an email address or any such other kind of patterns in strings. But creating an algorithm for each such new patterns is really tedious. Here is when **Regular Expression** comes into the picture.

Well. What does the name **Regular Expression(RegEx)** mean? Regular Expression represents the sequence of characters that defines some(**regular**) search pattern(**expression**).

RegEx is a standardized tool to do the following works:
1. Find and verify patterns in a string.
2. Extract particular data present in the form of substrings.
3. Replace, split and rearrange particular parts of a string.

**Practical Applications** includes Syntax highlighting systems, Data scraping and wrangling.

Let's see a sample code written in Regex which verifies an email address:

![enter image description here](https://lh3.googleusercontent.com/YVHHFniqi8kybwGasP5erNxTnbnNrZz-xio236kBf1W-aFkXllY54gf955LNKbCKtmNIXG0dtbfP)

Very confusing but interesting, right? At the first sight it seems weird, but it is easier to understand once you learn the fundamentals of RegEx.

Let's begin the journey with RegEx!

**Note:** 
1. In all the images below, the first section is a RegEx code and below is a text, in which the matches are shown-the shaded regions show the match.
2. **Alpha-numeric character** is the one which belongs to any of $0-9,A-Z,a-z$ ranges.

## Simple Alpha-numeric character matching

Simple matching of a specific word can be done as the following:

![enter image description here](https://lh3.googleusercontent.com/YGfz9u58rRKD0ABrSKDv7ZJOEMaIMGdFWgJWGGNzCFNakCtfAZVk1UEm7mBS4lIX1LFXoV420cmY=s800)

As you can see it matches "Reg" in the text. Similarly, what will be the match for pattern **"Ex"** in the same text above?

![enter image description here](https://lh3.googleusercontent.com/LkJXO79wn08dvgX5Q2JXHtyN7MW38AeNdV7fjG6lk7MNsiamx9iOekEGQg-WS9OLQMWxBuspjSkh=s800)

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
**Note:** **Groups** in the above output is a RegEx concept we will look very soon, keep reading.

Now, you can change the pattern and string in the code above to observe other patterns as we will learn below.

## Character classes:

![IMG](https://lh3.googleusercontent.com/dlLzL3teyEoax1JsdF7JeGP6DZOJll-UgnZqFkJtBeAVJhM1xMnXBHVeJYf_cUFLmj-f1qPO8asf=s800)

What if you want to match both "soon" and "moon" or basically words ending with "oon"?

![enter image description here](https://lh3.googleusercontent.com/bsRHqYuPZIQ7Yra4-zyF1BX2pIYDukCEtTfCK3rjaCTRmTAuo_fuHTVK5sJjbTdbXjGTVq1z5eYc=s800)

What did you observe? You can see that adding $[sm]$ matches both $soon$ and $moon$. Here $[sm]$ is called character class, which is basically a list of characters we want to match.

More formally, $[abc]$ is basically either $a$ or $b$ or $c$.

Predict the output of the following:

1. **RegEx code:** ```[ABC][12]```
**Text:** A1 grade is the best, but I scored A2.

Answer:

![enter image description here](https://lh3.googleusercontent.com/2JgAwwprVtZ8AfQMLoB9PEi7NoyJXxrEqv_46tLvdtCBKo4HBcPlbi3atyKsWJTwJLBTneyA_C0j=s800)


2. **RegEx code:** ```[0123456789][12345]:[abcdef][67890]:[0123456789][67890]:[1234589][abcdef]```
**Text:** Let's match 14:f6:89:3c mac address type of pattern. Other patterns are 51:a6:90:c5, 44:t6:u9:3d, 72:c8:39:8e.

Answer:

![enter image description here](https://lh3.googleusercontent.com/d2ynsBn5p8gIzvQeKewe8VrPiEu0EyOoNiEBkj_Co8fq_12FKhWK81V1Rcc2YCs3or9d4sCbuGtA=s800)

Now, if we put **^**, then it will show a match for characters other than the ones in the bracket.

![soon moon noon woon](https://lh3.googleusercontent.com/rj-zgBEZ7Fdv6rckQgHC90L_j7y1X7jj8veTZQoOKGQ2RSiEHPxPeSZUZoJE9yLW-o2dvXj6OI1j=s800)

Predict the output for the following:

 **RegEx code:** ```[^13579]A[^abc]z3[590*-]```
**Text:** 1Abz33 will match or 2Atz30 and 8Adz3*.

Answer:

![enter image description here](https://lh3.googleusercontent.com/BXaE8cxW7PcMJcfoUTlY-xBm9qNuhB5isy-PDLS5hIqQGIdRWiUf4viVxHF5yn5DJ0wHtoqHYKmP=s800)


Writing every characters(like $[0123456789]$ or [abcd]) is some what slow and also errorneous, what is the short-cut?

## Ranges
Ranges makes our work easier. Consecutive characters can simply be replaced by putting a dash between the first and last character.

![regex](https://lh3.googleusercontent.com/PWRFyDwe-89sdNSbmGc528PZXWhoX_-GNq0gQ8X9fOA-NX1Q4hzQNq1-Ty1LYjjsL8L4nVbSgvaq=s800)

Predict the output of the following regex:

 **RegEx code:** ```[a-d][^l-o][12][^5-7][l-p]```
**Text:** co13i, ae14p, eo30p, ce33l, dd14l.

Answer:

![enter image description here](https://lh3.googleusercontent.com/pgDHTvxQZ35ybyF7ozdeSGEBchiK8huiMQ3PfQWIgPSrzWoca8BpEoQ1yht8qyA4VVOdP6dNa-sl=s800)


**Note:** If you write the range in reverse order i.e. 9-0, then it is an error.

STILL REMAINING
------------------------------------------
## Predefined Character Classes

There are many special characters in regex: \w, \W, \d, \D. 

## Alternation


## Quantifiers(Repetitions)


## Anchors


## Word Boundaries


## Groups & Capturing


## Backreferencing



TAKE SOME WELL KNOWN EXAMPLES


