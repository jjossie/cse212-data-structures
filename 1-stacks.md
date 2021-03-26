# Stacks

## Overview

A **stack** is a simple data structure with many useful applications. They hold data in a one-dimensional array using a **last-in-first-out** (LIFO) approach. This means that elements added to the stack last will be the first to be removed. Conversely, the first element added to a stack will be removed last. In other words, the only way to remove a given element from a stack is to first remove all elements that were added after it. This concept will be explored further below.

In python, there is no special data type for stacks - we can simply use lists to represent them.

```python
sample_stack = ['z', 'y', 'x']
```

![stack](images/sample_stack_0.png)

## Regular Operations

Stacks' operations are more restricted than lists. While you can add values to the beginning of a dynamic array, you can only add and remove elements from the end of a stack.

Stacks are different from most data structures in that they have only a single access point for regular read/add/remove data operations. To insert a new element, we **push** to the back of the stack. To remove the topmost element, we **pop** from the back of the stack. The back, therefore is the singular point of access to the data structure.

### Push

In python, we can push an element onto a stack with the simple `append()` function.

```python
sample_stack.append('w')
```

![stack 2](images/sample_stack_1.png)

> **Note**: while, in Python, you could perform other operations to add data to this list, such as `.insert()` or simply accessing an index like `sample_stack[1] = "Y"` to alter data, this defeats the purpose of a stack. Not only does this ruin the integrity of the data structure, it also means we lose the performance benefit stacks have over lists (we'll talk about this more later). So basically, even though you *could*, don't.

### Pop

> ### *"POP, POP!"*

-Magnitude, Community (multiple occasions)

## Example Use Cases

yah bro i got no idea

## Exercise Problem

uhh yeah so go ahead and implement a fully functional operating system clipboard stack or something idk
