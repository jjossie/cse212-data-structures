# Trees

## Overview

A tree is a data structure wherein elements are linked to one another such that all links can lead back to a single source. When represented visually, it can resemble an upside-down tree, hence the name. When compared to stacks and sets, trees have sligthly less efficient regular operations, but they make up for it in other ways. For example, trees can start out tiny and grow to be massive with no issues. They are similar to sets in that placement of the data within the structure does not matter to the user of said structure. Additionanally, they do not waste memory like sparsed arrays (sets) which may have empty memory being used.

## (t)Re(e)lationships

To understand the basic structure of trees, let's look at the smallest example of one:

![tree root](images/tree_root_2.png)

This tree contains only a single element: the number 10. In this case, 10 is the **root** node. This is the single source to which all elements within a tree lead back. Let's look at a bigger example.

![tree example 2](images/tree_root_leaves.png)

Notice the **leaf** nodes 2, 9, and 15. All nodes at the bottom of a tree are considered leaves because the tree extends no further from them. They are nodes that do not have **children**. What does that mean?

![parents & children](images/tree_parent_child.png)

The directional flow of a tree from top to bottom defines parent-child relationships within a tree. For any given node, its **parent** is the node appearing above it, from which an arrow is pointed to the given node. Conversely, any nodes to which a given node points are its **children**. Let's look at the node 7 as an example. As shown by the blue boxes, it is a parent node, and 2 and 9 are its child nodes. However, it is also a child node, as demonstrated by the orange boxes, of the parent node 10.

Why is this important? These parent-child relationships allow us to break down trees into simpler subsets of data called subtrees. An example:

![subtrees](images/tree_main_and_sub.png)

Let's take a look again at the 7 node. We can think of 7 as the root node of a subtree of the main tree we're looking at. This subtree can be treated entirely as a normal tree. It still has leaves - 2 and 9 - and they are still child nodes of 7. Ok, so that makes sense, but why is it useful?

## Recursion

The concept of subtrees allows us to unlock the true power of trees using recursive functions. **Recursion** is the process of a large problem being broken down into smaller and smaller problems until a solution can be found. The condition under which that solution is found is called a **base case**. In practice, this means a function will call itself, passing in a smaller and smaller data set until that base case is reached. Subtrees allow us to break a large data set down into smaller data sets - in other words, smaller problems. Typically, the base case of a recursive call on a tree is when the size of the current subtree is 1, because the node being looked at has no children - it is a leaf.

>To avoid the possibility of infinite recursion, the function will typically check for the base case condition (is the problem solved or solvable) before performing a recursive call.

## Regular Operations

Most regular operations in trees are quite efficient, although not quite as efficient as insert/lookup operations from a stack or a set. While stacks and sets can do these in O(1) time, trees typically perform them in O(log n) time. This is because some amount of searching is required to find a given element. However, it is not O(n) because not every element needs to be visited - instead, the data set shrinks upon each comparison, similar to binary searches. While this may make sets and stacks seem better, trees have the advantage of much greater flexibility with memory usage. Trees can start out tiny and grow to be massive with no issues. Additionanally, they do not waste memory like sparsed arrays (sets) which may have empty memory being used.

### Read

Lookups in a tree always start by looking at the root. If the root element matches what is being searched for, then the job is done - that element is returned. If not, however, a decision must be made - where to look for the element next. Looking at our tree example from above, if we were looking for the number 12, we would have to compare 12 to the value at the current node (remember, we're still at the root node 10). Because 12 is greater than 10, we would then look for 12 starting at the next node to the right. This would be done with a recursive call - instead of again using the entire tree as the data set to be operated on, the subtree using 12 as the root node would be passed into this recursive call. Now 12 is compared to 12, and the element has been found. This example of using a greater/less than comparison to make decisions for finding elements within a tree is how a **binary search tree** operates.

>Binary search trees are not the only kind of tree. The process used to decide where a given element is expected to exist within a tree is not limited to only a greater/less than comparison - many other decision making processes could be used. However, binary comparision works best for trees where the number of children a given node can have is limited to 2.

### Insert

Insert operations perform exactly the same way as lookups - a series of recursive calls and decisions regarding the direction of tree traversal would be made. In this case, however, what we are looking for is a suitable empty space to place a given node.

<!-- ### Update -->

<!-- ### Delete -->

## Basic Implementation

Python does not have a built-in implemenation of a tree data structure. However, one can be made using a simple base Node class like the following, which simply stores a data variable and pointers for two child nodes:

```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
```

A function would need to be added to perform operations like insertion. This one takes two parameters, both of which are instances of Node. One will be the root of a tree, and the other will be a new node to be added. Notice that the function is recursive - if an empty space is not found to the left or to the right of the root, it breaks the tree into a smaller problem by performing the same function on a subtree starting at the non-empty node to the left or right! Also note that after insertion, a new node will always be a leaf.

```python
def insert(root, node):
    if node.data > root.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    elif node.data < root.data:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
```

Now that we can insert data into the array, let's make sure we can read it somehow. This operates in almost the same way as the recursive function, except that we pass in the root of a tree and the raw data we are looking for, rather than a node to be added (meaning we won't need to call `Node()` when calling this function, assuming we already have a populated tree).

```python
def contains(root, data):
    if root.data == data:
        return True
    elif data < root.data:
        if root.left is None:
            return False
        else:
            return contains(root.left, data)
    elif data > root.data:
        if root.right is None:
            return False
        else:
            return contains(root.right, data)
```

## Example Use Case

Let's say you wanted to use a tree to store phone numbers in an address book. Because phone numbers are unique, you could use a binary search tree to store phone numbers and check for membership. Using the three code blocks above as a foundation for our binary search tree, have the user add several phone numbers and check for them using the tree:

```python
def get_number():
    valid = False
    while not valid:
        try:
            user_input = int(input("Enter a Phone Number: "))
            if len(str(user_input)) == 10 and user_input >= 0:
                valid = True
            else:
                print("Not a valid phone number.")
        except ValueError:
            print("Please enter only numbers.")
    return user_input

def main():
    print("1: Add Phone Number, 2: Check for Phone Number, 3: Quit")
    root_number = None
    done = False
    while not done:
        user_input = input("Select Action: ")
        try:
            selection = int(user_input)
            if selection == 1:
                if root_number is None:
                    root_number = Node(get_number())
                else:
                    insert(root_number, Node(get_number()))
            elif selection == 2:
                if root_number is None:
                    print("Tree is empty.")
                else:
                    num = get_number()
                    print(f"{num} is in the tree: {contains(root_number, num)}")
            elif selection == 3: 
                done = True
        except ValueError:
            print("Invalid Input.")

if __name__ == "__main__":    
    main()
```

## Exercise Problem

Currently, the binary search tree above will allow one of each phone number to be entered into the database. This works because phone numbers are unique. What if, however, we wanted to keep track of something less unique, like first names? Your challenge is to modify the binary search tree used in the previous example to allow duplicate values to be stored in the tree.

>**Hint:** use an additional member variable in the Node class.

View the solution [here](code/3-solution.py).
