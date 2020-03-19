# Stacks

- who does not know stack?


-- --


Stack
-----

- what are the two most basic operations in a stack?
    - peek can be implemented as pop then push same
- Stack is a LIFO datastructure.
- You can only operate on the top

- where have you used stacks?
    - undo
    - recursion
    - pile of stacks


-- --


Quick
-----
- push_bottom a stack using an auxillary stack
- lifo
- reverses when popped
- equivalence with recursion
    - anything using a stack can be done using recursion
    - draw tree for push_bottom
    - how to implement recursion iteratively using stack?

-- --


Stack in recursion?
-------------------
- 
- push state of function call before calling a sub-function
- Call stack
- Example
    ```
    def fact(n):
        if n <= 1: return 1
        return n * fact(n-1)

    print(fact(3))
    ```
- Call stack
    ```
    fact(1)
    fact(2)
    fact(3)
    print
    main
    ```
    
    
-- --


What is stackoverflow?
----------------------
- How is memory managed?
- 4 types of memory alloted to a program
    ```
    HEAP
    Stack (call stack)
    Global / Static Variables
    Text / Code
    ```
- Each memory is fixed. Compiler / JRE / Interpretter takes care of that.
- So stackoverflow is when you have a very deep recursion
    - infinite recursion


-- --

Reverse a Stack
---------------
2 auxilarry stacks

```
[1 2 3 4]
[]

[]
[4 3 2 1]

[]
[]
[1 2 3 4]


[4 3 2 1]
[]
[]
```
$O(n)$

**Via recursion:**

```
def reverse(stack):
   x = pop()
   reverse(stack)
   push_bottom(x, stack)
```

$O(n^2)$ time

This uses 2 stacks too, one for recursion, one for push_bottom

-- --


Undo-Redo
---------
- Only undo? 1 stack
- Undo-Redo? 2 stacks
- Example of browser history:
    - Click pages, push to undo-stack
    - go back, pop from undo-stack and push in redo-stack
    - go forward, pop from redo-stack and push in undo-stack


-- --


Evaluating Post-Fix expressions
-------------------------------
- Infix: Inorder
    - operator is b/w the operands
    - $a + (b*c) / d$
- Postfix: Postorder
    - operator is after the operands
    - $bc*d/a+$
- Prefix: Preorder

**More examples:**
- infix: $4 * 5 + (2 - (3 * 4)) / 5$
- postfix: $45234*-5/+*$
- can I write it as $34*2- \ldots$ ?
    - No, because operation need not be commutative (matrix multiplication)

**Algorithm for Evaluation:**
- go from left to right
- push operands on stack
- when operator, pop top 2 from stack, apply operator, push result
- give example



-- --



Convert Infix $\to$ Postfix
------------------------
> - Convert  
>    $(1+2) * 3 / (4 - 5) + 6 - 1$
>    to  
>     $21+345-/*61-+$
> - Precedance: `()` > `* /` > `+ -`
> - Can be done in 1 stack

**Algorithm:**
- 4 decisions to make
- what to do when: operand, operator, (, )
- result = []
- stack = []
- operand:
    - append to result
- operator:
    - if stack has higher precedance (or equal), apply all of them first
        ```
        operator: +
        stack:
           *
           *
           -
        ```
    - Applying simply means popping from stack and appending to result
    - Don't pop (
- (
    - push on stack
- )
    - pop from stack until we see (. Pop the ( too
- end
    - pop all from stack and append to result


-- --


Google Question
---------------
> N Stock prices for each day
> ```
> A = [100, 80, 60, 70, 60, 75, 85]
> ```
> Longest consecutive sequence ending at $i$ such that the numbers in the sequence <= A[i]
> Do this for all $i$
> Exmple output:
> ```
> input: 100, 80, 60, 70, 60, 75, 85
> output:  1,  1,  1,  2,  1,  4,  6
> include self.
> ```

**Solution:**
- Keep (price, answer) in stack
- traverse array from left to right
- if smaller than stack top price, push (price, 1)
- if larger or equal
    - keep popping till larger.
    - maintain total answer so far (init by 1)
    - once done, push (price, total)

Works because if there was say 59 at the end which would need to stop at 60, it would aready stop at 75

**Complexity:** $O(n)$
Each element will be pushed once, and popped at max once


-- --


Design a special stack
----------------------
> no restrictions on DS to implement
> operations
> - push
> - pop      - returns false when stack is empty
> - get_mid  - returns false when stack is empty
> - pop_mid  - returns false when stack is empty
> 
> all operations must take $O(1)$
> stack need not be sorted

- can't use array, because how to pop mid in constant?
- use doubly linked list
    - keep a pointer to end of list
    - keep pointer to mid
    - on push, move the mid to right if needed
    - on pop, move the mid to left if needed
- for pop mid, pop the mid and update the mid pointer


-- --


special MIN stack
-----------------
> use stack internally
> operations
> - push
> - pop
> - get_min
> 
> All operations in $O(1)$

**Solution 1:**
- store both the value, and the min so far into the stack
- can split into two stacks - for values, and for mins if we wish

**Further Constraint:**
> - only 1 stack
> - stack can have only 1 value and not tuples

- single space for M (min). init with $\infty$
- push:
    - if stack empty or E >= M:
        - push
    - else:
        - push T = 2E - M
        - M_n = E
        - `this keeps track of previous min`
- get_min
    - return M
- pop
    - T = top
    - if T >= M
        - pop and return T
    - else
        - E = M
        - M_o = 2M - T
        - return E


**Proof:**

- If $E < M$, then $2E - M < E$. Thus, I can know if the min was changed.
- todo: draw diagram by hand


-- --
