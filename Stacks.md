
## Stack

- Abstract Datatype
- Linear data structure 
- Sequential Access
- LIFO (Last In First Out)

### Stack Operations

- Push
- Pop
### Implementation of Stack

- Array (Keep the two conditions in mind during interviews)
  - Stack Overflow
  - Stack Underflow
  - **Pros**: Easy to implement. Memory is saved as pointers are not involved.
  - **Cons**: It is not dynamic. It doesn’t grow and shrink depending on needs at runtime.
  - Can use Vectors/ArrayList also
- LinkedList
  - Push() - Add at head. O(1)
  - Pop() - Remove at Head. O(1)
- Queue - Will discuss later

**Q- Given only two operations i.e., push() and pop(), implement insertAtBottom() function**

Approach 1: Using Extra Stack

Approach 2: Using Recursion

```java

insertAtBotton(Stack s, int n){
  if(s.isEmpty()){
    s.push(n);
  }
  int temp = s.pop();
  insertAtBottom(s, n);
  s.push(temp);
}

```

**Q- Reverse a stack** 
(Perform Reversal in same stack)
Approach 1: 
```java

reverse(Stack s){
  if(s.isEmpty()){
    return;
  }
  int temp = s.pop();
  reverse(s, n);
  insertAtBottom(s, temp);
}

```

  Time Complexity - 
  Pushing one element at the bottom - O(n)
  Pushing n elements at the bottom - O(n^2)

Approach 2: Take two auxillary stack


**Q- Implement Sorting using stack**
The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one in sorted order. Here sorted order is important.

Similar to above question. Just implement insertInSortedWay(). 

```java

sortStack(stack S)
    if stack is not empty:
        temp = pop(S);  
        sortStack(S); 
        sortedInsert(S, temp);
 
 
 sortedInsert(Stack S, element)
    if stack is empty OR element > top element
        push(S, elem)
    else
        temp = pop(S)
        sortedInsert(S, element)
        push(S, temp)
 
 ```
 
Time Complexity: O(n^2)
Space Complexity: O(n) 

**Q- Remove consecutive duplicates in a string**
String: kabbal 
Output: kl

**Special case**
String: aaa 
Output: a

Time Complexity: O(string.length)
Space Complexity: O(string.length)

**Q- Valid Paranthesis**

Input: "()[]{}"
Output: true

```java
public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for(int i = 0 ; i < s.length(); i++) {
            char ch = s.charAt(i);
            if(ch == '(' || ch == '[' || ch == '{') {
                st.push(ch);
            } else {
                if(st.isEmpty()) return false;
                char p = st.peek();
                if(ch == ')' && p != '(') return false;
                else if(ch == ']' && p != '[') return false;
                else if(ch == '}' && p != '{') return false;
                else st.pop();
            }
        }
        return st.isEmpty();
    }

```

Time Complexity: O(n)
Space Complexity: O(n)

**Q-- Evaluate Infix Expression**
1. Maintain two stacks, one for integers and one for operators

```java
         //Stack for numbers
         Stack<Integer> numbers = new Stack<>();

        //Stack for operators
        Stack<Character> operations = new Stack<>();
        
        for(int i=0; i<expression.length();i++) {
            char c = expression.charAt(i);
            
            //check if it is number
            if(Character.isDigit(c)){
                //Entry is Digit, it could be greater than one digit number
                int num = 0;
                while (Character.isDigit(c)) {
                    num = num*10 + (c-'0');
                    i++;
                    if(i < expression.length())
                        c = expression.charAt(i);
                    else
                        break;
                }
                i--;
                //push it into stack
                numbers.push(num);
            }else if(c=='('){
                //push it to operators stack
                operations.push(c);
            }
            
            
            else if(c==')') {
                while(operations.peek()!='('){
                    int output = performOperation(numbers, operations);
                    numbers.push(output);
                }
                operations.pop();
            }
            // current character is operator
            else if(isOperator(c)){
                operations.push(c);
            }
        }

        while(!operations.isEmpty()){
            int output = performOperation(numbers, operations);
            numbers.push(output);
        }
        return numbers.pop();
    }

    public int performOperation(Stack<Integer> numbers, Stack<Character> operations) {
        int a = numbers.pop();
        int b = numbers.pop();
        char operation = operations.pop();
        switch (operation) {
            case '+':
                return a + b;
            case '-':
                return b - a;
            case '*':
                return a * b;
            case '/':
                if (a == 0)
                    throw new
                            UnsupportedOperationException("Cannot divide by zero");
                return b / a;
        }
        return 0;
    }

    public boolean isOperator(char c){
        return (c=='+'||c=='-'||c=='/'||c=='*'||c=='^');
    }
```

Time Complexity: O(n)
Space Complexity: O(n)



