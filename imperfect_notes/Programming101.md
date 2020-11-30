## Initial start
- Check if everyone has interface familiarity
- Talk to them about importance of two way conversation
- importance of asking question and "There are No     stupid questions"
- Any other stuff related to previous lecture

## Overview of the current lecture
- **what we will do**
    - Basic of programming
    - the very first steps in coding
    - will discuss about the computer and how it evolved
    - then would be writing a very basic code to start with programming

- **Focus on - A lot of assumptions will be made**
    - So need not understand everything
    - no need to panic if you don't understand anything
    - Can relate to it school's classes where you were made to cram mathematical tables without telling what's it for - or any other example but relate

- introduce ideone.com if using that

- Tell them that we would be using C++ (or any other lang)

## What is a computer?
- Dicuss this question, take inputs
- computer -> compute = to compute something
- Humans were called as computers before - because humans were hired as assistants to do calculations
- Start building a story here
    - Introduce with some current great things done by computer not just calculations
    - start with the story in ancient times
    - refer computer as "Smart rock" - rock with electrical signals
    - discuss two inventions 
        - how to put electricity in rock
        - how to make a rock think
    - can build on this story more using turing's war help example
    - can use example of punch cards
- Computer is a machine that does whatever you tell it to do
- computer does everything very fast
    - take a calculation like 9888.2142421 * 242434.5442423242
    - discuss in how much time they can do it
    - dicuss in how much time the computer does with reference to speed of light
    - computer can do same computation 4 time while light covers 1 feet

## Why and what we need to tell computer ? 
- Can play a video here of rajpal yadav in waqt movie where he asks a lot of question (motive - make it goal specifc)
- In the same way computer is dumb , you have to tell it every single detail
- Now discuss the operation of addition of two numbers and what you need to tell computer to do it
    - What do you mean by numbers?
    - from where these number would come?
    - how large are these numbers ?
    - what is addition or how it is performed?
    - how to take input from keyboard?
    - where do I store the input?
    - Where to I store the result?
    - should I output the result?
    - How to output?

## How to tell / How to interact with computer ?
- Explain by taking some example how just doing electrical signals can perform operation - how computer does it (Need to find examples here)
- then relate up/down voltage to 0 & 1 - introduce binary and tell this is what computer understands
- Then dicuss the bad thing about talking in binary
- So we need to find a simpler way to interact

- Can we interact in English/Hindi/Japanese
- no becuase there are ambiguous - explain with an example
- Example - Buffalo BUffalo Buffallo Buffalo Buffalo BUffalo Buffallo Buffalo 
- ask what they understand by the statement
- explain how it is ambiguous 
- meaing - The Buffallo of the city Buffallo, that bullies the buffallo of the city Buffallo , are themselves bullied by the buffallo of the city of Buffallo
- we needed to find / invent unambigouos language - the language in which a sentence can only be interpreted in one single way
- so languages like C+= , java , python were introduced

- but still computer only understand 0 & 1
- **We need to find a way to take programs in the "high level" unambiguous language and convert it into binary (1s and 0s) that the computer can execute & understand**
    - Can demonstrate this thing by considering it as a black box / translator (eg - English to Hindi)
    - after explaining why we need - we can introduce the names - "compiler" , "interpreter" , "Assembler" , "Linker"

## The beginning of coding
- start with the initial code
- refer it as boiler plate / template
- tell students again that they need not understand everything - just assume
```cpp
    #include<iostream>

    using namespace std;

    int main() {
        return 0;
    }
```
- this is starting pattern which is to followed always when writing code in C++

**First program**

- start by writing a "Hello World" program
```cpp
   int main(){
       cout << "Hello World";
       return 0;
   }
   ```
- Now ask what if in place of World you want to print your age (can be name if you want to introduce string datatype) that would be entered by the user
- use this to explain the need of variable
- how variables are declared 
- declare a string variable 
- how input is taken
- **Again focusing on the fact that cin, cout and string would be cleared later**
```cpp
    int main() {
        // variable declaration
        // <data-type> <name>
        int age; // integer 
                 // allocate some memory in RAM
        cin >> age;
        cout << "age: " << age;
    }
```
- Explain in brief what happens when you declare a variable , memory allocation
- give a brief about everything you write in code
- Tell them about comments - by taking example - like sometimes you write meaning of a word in Hindi at the side of a page but when you read the page you only use english 
- While explaing "int" - you can take some time to explain different kind of numbers
```
- Natural Numbers -> 1 , 2 , 3...
- Whole Numbers -> 0 , 1 , 2 , 3...
- Integers -> -3 , -2 , -1 , 0 , 1 , 2...
- Rational Numbers -> can be expressed in p/q form - has decimal and decimal values either ends or repeats 
- Irrational Numbers - no p/q form , ex - Pi , sqaureroot(2) etc.
```
**Program to add two Numbers**
- Now refer to start of the lecture where we wrote things computer would ask to add two numbers
- refering those questions  , start writng code
```cpp
    int main() {
        int a;
        int b;

        cin >> a >> b;

        int result = a + b; // explain addition operator

        cout << result;
    }
```
- try to refer the whole code to the previous discussion
- discussion assignement operator
- How it is different from mathematical equal operator

- Cover any point if required


