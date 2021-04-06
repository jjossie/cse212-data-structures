# Stacks

## Overview

A **stack** is a simple data structure with many useful applications. They hold data in a one-dimensional array using a **last-in-first-out** (LIFO) approach. This means that elements added to the stack last will be the first to be removed. Conversely, the first element added to a stack will be removed last. In other words, the only way to remove a given element from a stack is to first remove all elements that were added after it. This concept will be explored further below.

In python, there is no special data type for stacks - we can simply use lists to represent them.

```python
sample_stack = ['z', 'y', 'x']
```

![stack](images/sample_stack_0.png)

## Regular Operations

Stacks' operations are more restricted than lists. While you can add values to the beginning of a dynamic array, you can only add and remove elements from the end of a stack. In other words, stacks have only a single access point for regular read/add/remove data operations. To insert a new element, we **push** to the back of the stack. To remove the topmost element, we **pop** from the back of the stack. The back, therefore is the singular point of access to the data structure.

While this may seem like a disadvantage, it does come with a significant benenfit: every operation on a stack is O(1) performance. This is because the last index of the list being used to store the stack can be determined with a simple `len(sample_stack) - 1`, at which point a lookup from a list at a given index is also a simple O(1) operation. No searching or extra processing is needed to add an element to the back of a stack or to remove the last element from it. With our example above, the index `2` would be the back of the stack.

### Push

In python, we can push an element onto a stack with the simple `append()` function. Python automatically knows that `2` is effectively the back of the stack and the next element should be inserted at index `3`.

```python
sample_stack.append('w')
```

![stack 2](images/sample_stack_1.png)

> **Note**: while, in Python, you could perform other operations to add data to this list, such as `.insert()` or simply accessing an index like `sample_stack[1] = "Y"` to alter data, this defeats the purpose of a stack. Not only does this ruin the integrity of the data structure, it also means we lose the performance benefit stacks have over lists. So basically, even though you *could*, don't.

### Pop

Similarly, we can remove values from the stack with a simple function on the list. This time, it's actually named appropriately: `pop()`. This function will not just remove the last element in the stack; it will return its value to the calling expression.

As with `.append()`, Python knows that `3` is the back of the stack and will remove the element at that index.

```python
last_value = sample_stack.pop()
```

![stack 3](images/sample_stack_2.png)

> ### *"POP, POP!"*

#### *- Magnitude, from the television series Community (multiple occasions)*

## Example Use Case

Say we wanted a program that would reverse any text the user types. It could look like this:

```python
stack = []
phrase = input("Enter a word or phrase: ")
for char in phrase:
    stack.append(char)

reversed_phrase = ""
for i in range(0, len(stack)):
    reversed_phrase += stack.pop()

print(reversed_phrase)
```

## Exercise Problem

Write a program using a stack that will allow the user to write words and phrases one after another, and will print back the last phrase from the history when they type "undo".

View a possible solution [here](code/1-solution.py).
