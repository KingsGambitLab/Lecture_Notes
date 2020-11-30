## Data Types

- Can start with bioler plate
- taking students help to write it
```cpp
    #include<iostream>

    using namespace std;

    int main() {

        int a = 5;
        float b = 5.7;
    }
```
- Ask what type of data is stored in int and float
- Ask why it is called "float" not decimal
    - IEEE define these type of numbers as floating point numbers
    - Numbers are made up of digits and have a decimal point, the decimal point can be between any two digits - so decimal point is kind of floating around

- Introduce characters and "char" data type
```cpp
    char c = 'A';
    string s = "ABC";
```
- Discuss primitive / compound data types in reference to char/string

- Dive more into characters

- Ask how many alphabet english have
    - 26? No
    - only 1 i.e A - Z
- alphabet in Hindi - 2
- alphabet in Japanese - 3 - Kanji , hiragona, katakana

- So what type of Alphabet we use in C++ or other languages
    - **ASCII alphabet**

- ASCII alphabet has 1 byte of space - 8 bits
- ask how many characters would be possible with 8 bits
    - 2 ^ 8 = 256 characters
    - ask if students understand - if not,explain
- Introduce some basic characters/letters 
    - A - Z -> 26 characters
    - a - z -> 26 characters
    - 0 - 9 -> 10 characters
    - and many special characters - ~`!@#$%......
- Ask if they can guess the remaining characters
    - Backspace , Escape , Carriage return etc

- show ASCII table 
    - Discuss ASCII code
    - Discuss about extended set
    - Discuss different characters
        - A - Z
        - a - z
        - 0 - 9
        - special characters
        - Currencies and excents - in latin/perish - some characters have two or more excents
        - characters like aplha , bita , 1/2 , 1/4 , infinity , sqaure root , >= , <= etc
        - box printing characters - show them with the command top/htop , how GUI is beneficial but then tell them how terminal was used when no GUI was there and Box printing characters were used at that time
        - dicuss the characters in the starting of the table - ex - SOH , STX , NUL
        - can discuss the backspace('\b') , carriage return('\r') and free line character('\n')
        - can explain carriage return by playing a video of typewriter
        - why escape sequence is needed
        - show with some code examples

- disucuss about Unicode
    - what is unicode?
    - how it is different than ASCII code? - 2 bytes rather than 1 byte 
    - languages that have unicode - python , ruby , java etc.

- **How these characters are represented inside the computer**?
    - Are these characters represented as it is ? aur is there any different way?
    - everything is represented using binary representation
    - ask - what would be binary value of 'A'?
        - 'A' implies 65 -> 1000001
        - ask if students understand binary representation, if not explain
    - so, computer stores in binary rather than storing it as 'A' or 65

    - **But how does computer knows if I am talking about number 65 or the character 'A' ?
        - computer doesn't know and doesn't care
        - it depends upon quotes and the data type conversion
    ```cpp
        int a = 65;
        char ch = 'A';

        /*computer would store same thing '1000001' in the memory for both cases*/
        /* But the program will intepret it differently based on data type */
    ```

- **Size of datatypes**
    - char has 1 byte which is already discussed
    - discuss int and float
    - before moving forward , print size of some basic datatypes
    ```cpp
    int main() {
        cout << "char " << sizeof(char) << endl;
        cout << "int " << sizeof(int) << endl;
        cout << "short int " << sizeof(short int) << endl;
        cout << "long long int " << sizeof(long long int) << endl;
        cout << "float " << sizeof(float) << endl;
        cout << "double " << sizeof(double) << endl;
        cout << "bool " << sizeof(bool) << endl;

    }
    ```
    - ask what could the result printed represent ? bits or bytes?

    - Dicuss size of int
        - 4 bytes - 32 bits of size
        - how many total no can we represent using this much amount of space ?
        - 2 ^ 32 numbers
        - can we represent 1 , 2 , 3 ..... 2 ^ 32 , yes.
        - But we left zero
        - can we represent 0 , 1, 2 , 3 ,,,, 2 ^ 32 - 1,yes
        - But we left negative numbers
        - Dicuss signed and unsigned and print sizes of both
        ```cpp
        cout << "signed " << sizeof(signed int) << endl;
        cout << "unsigned " << sizeof(unsigned int) << endl;
        ```
        - discuss how the sizes are same
        - unsigned -> 0 , 1 ,2 , ..... 2 ^ 32 - 1
        - signed - this is default behaviour -> -2 ^ 32 ....... 0 ....... 2 ^ 32 - 1

        - **We know how to represent positve numbers using binary representation , but how to represent negative numbers ?**
        - How to represent (-10) ?


- **Representation of negative numbers**
    - discuss some adjustments
    - Adjustment 1:
        - can represent no's alternatively
        ```
        00000 -> 0
        00001 -> 1
        00010 -> -1
        00011 -> 2
        00100 -> -2 .........
        ```
        - the logic behind old binary representation vanishes
        - becomes difficult to manage

    - Adjustment 2 :
        - can first represent negative no's and then positive 
        ```
        00000 -> -3
        00001 -> -2
        00010 -> -1
        00011 -> 0
        00100 -> 1
        00101 -> 2
        00110 -> 3

    - Discuss how computer is mad up of circuits
    - how we take help of addition while doing other arithmetic operations
    - ex -> 9 - 5 = 9 + (-5)
    - Now discuss what's bad about previous two approaches - how these approaches are making circuits complex and how these are taking away the sense of binary representation

    - start building up for 2's complement approach
    ```
        10  -> 1010
        -10 -> abcd
        -----------
        0   -> 0000
    ```
    - assume that -10 is represented by abcd , now we have to find some abcd such that 10 + (-10) gives us 0 and 0's representation remains '0000'

    - abcd comes out to be 0110 by hit and try
    - but result comes as 10000 which is not zero - explain that if the size is only 4 bits than we can ignore the left most bit because it won't be stored , so eventually result becomes 0
    
    - But now -10 -> 0110 which is also the representation of 6 -> 0110 , so how do we differ between -10 and 6
    - can we take an extra bit which would be called signed bit and would tell us about the sign

    ```
           S|
    10  -> 0|1010
    6   -> 0|0110
    -10 -> 1|0110

    0 -> positive
    1 -> negative

    ```
    - but we can't hit and try always , so how to reach to abcd if the no is negative ?
    - it is called 2's complement
    - before that let us see what is complement ?
         - it is nothing but toggling every bit
         - 10110 -> (complement) -> 01001
         - also called one's complement
    - what is 2's complement then ?
        - 1 's complement + 1 -> 2 's complement
        ```
        10 (1010) -> (1's complement ) -> 0101 

        1010
        0101 -> 1's complement
           1 -> addition of 1
        0110 -> 2's complement

        this is what we gets when we find 'abcd' for -10
        ```

    - so , negative no's can be represented as -
    ```
    let say we have number -x 
     -x -> 1|2's complement of x
    ```

    - why we choose this representation ?
        - computers are just circuits
        - now we can have a seperate citcuit which would give us 2's complement and thus we can get our negative number without complexing things
    
    - No , if we are given with negative no we can represent it in binary but what if binary representation of a negative no is given than how to get to the actual no ?
    ```
    10 -> negate -> -10 -> negate -> 10
    so similarly
    10 -> 2's compliment -> 0110 -> 2's compliment -> 1010
    ```
    - taking 2's compliment again can give us the original number


- **Does characters have signed behaviour?**
    ```cpp
    char ch = 200;
    cout << ch << endl;
    ```
    - run this thing
    - in the output window ,a warning will be shown that 200 is converted to -56 , why ? what is this?
    - this is because char is signed by default
    - char has 8 bits -> 2 ^ 8 = 256 characters
    - actual range -> -128 ...... 0 ..... 127 
    - but why 200 goes to -56 ? 
        - this is called wrap around
        - as soon as numbers starts increasing after 127 the computer start again taking it to back i.e -128 , we can say a cyclic thing happens
    
    - **does the same thing happend in int if we exceed limits ?**
        - yes
        - wrap around happens in both signed and unsigned int

    ```
    max unsigned no - 4294967295 - 11111.....111 - 32 times
    if we add 1 to this
     1111111..111111111
     0000000........001
    ------------------
    1000000000000000000 - the leftmost bit will vanish, so only zero remains
    -> 4294967295 + 1 -> 0 
    ```

    - So this was some introduction about datatypes , float are represented in a completely different way , we'll take it in some other class
    - and we would discuss type conversion in one of upcoming class
    
