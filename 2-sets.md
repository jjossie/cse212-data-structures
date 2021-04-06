# Sets

Imagine a parking lot with assigned parking spaces. If you want to park, you can only park in your assigned space. Even if there are no cars in the parking lot, every parking space exists and is still numbered. However, imagine that in this parking lot, each space may have more than one parking pass assigned to it. So while you will only ever get a single parking pass for this lot, somone else may have the same parking pass. What happens when you want to use your pass, but the assigned spot is already taken? What if the parking lot is full?  We'll address these and other questions below, but this is essentially how sets work. We'll discuss this more below.

## Overview

A set is a data structure initially created with a fixed size, similar to a parking lot with numbered spaces. Operations that typically take O(n) time in other data strucutres, such as membership lookups, can be done in O(1) time. How is this possible? Let's compare sets to dynamic arrays to better understand the concept. In a dynamic array, elements can be added at the end of the list easily (in O(1) time), but all other inserts require shifting the rest of the array one element at a time to prevent any gaps (O(n) time in the worst case). Sets, however, allow gaps in the list and utilize a technique known as **hashing** to determine at which index to place a given element. This means that only a single operation is needed to both determine the index at which an element should be place *and* determine whether a given element exists in the list.

> **Note:** Because hashing generates a seemingly random value to be used as the index for a given item, the order of these items stored in the set is meaningless and can vary drastically.

## Hashing

Hashing is a process wherein data is cryptographically converted to a shorter value representing the original data. In our parking lot analogy, imagine it as a process wherein information about the car (such as color, type, or perhaps something more unique like license plate number) is used to determine which parking pass the car will receive.

>**A note on performance** - So if sets have O(1) lookups, insertions, deletions, and updates, why would we ever use dynamic arrays, which have O(n) time for many of the same operations? As with many things, the benefits of the O(1) operations come at a cost. The main trade-off here is between memory usage and performance. Sets will generally use more memory because even if the set contains no data, it will still take up a constant amount of space in memory. Think of the parking lot - even if no cars are parked in it, the asphalt is still there and the lines are still drawn. Additionally, sets are not preferable over dynamic arrays when duplicate data exists - sets do not allow duplicates.

## Regular Operations

Creating a set in Python can be done using one of two methods:

```python
sample_set = {10, 20, 30}
```

The first method uses curly braces to declare and initialize values for a set in a single statement. The second method is used when you only want to declare an empty set:

```python
sample_set = set()
sample_set.add(10, 20, 30)
```

>Curly braces cannot be used to declare an empty set because Python allows curly braces to represent both set *and* dictionary literals, and an emtpy pair of curly braces defaults to representing an empty dictionary rather than a set.

### Insert

Adding elements to a set in python is simple enough. If, for example, you had initialized the set using `sample_set = set()` as shown above, you could add the elements like so:

```python
sample_set.add(10)
sample_set.add(20)
sample_set.add(30)
```

### Remove

Removing an element from a set is equally simple:

```python
sample_set.remove(20)
```

### Read Operations

While with a dynamic array, you may at times want to look up an element at a given index n, like in `sample_array[0]`. However, with sets, indexes have virtually no meaning because they are abstracted via the process of hashing. In other words, you would never need to look up what element exists at a given index within a set; rather, you may instead need to look up *whether a given element exists* within a set. This can be done with the `in` operator:

```python
if 10 in sample_set:
    print("10 is in the set!")
```

Additionally, you may want to iterate through all items within a set. This can be done using Python's implicit bulit-in `__iter__()` function:

```python
for item in sample_set: # just pretend we already added 20 back to the set
    print(f"I am number {item}")
```

This would yield (order may vary):

```bash
I am number 10
I am number 20
I am number 30
```

>**Note:** Because reading individual items from an index is not possible with sets, updating individual elements' values is also not an applicable operation to the set data structure. Instead, basic insertion and removal is all one will typically need.

## Dealing with Conflicts

Because the number of possible values that could be stored in a set is far greater than the number of possible memory locations for those values, there is a possiblity of the hashing process producing an identical index for two different items. This is like two cars with different license plate numbers being issued the same parking pass. There are basically two ways to go about resolving this:

* **Method 1**: When inserting an item that belongs at an index which is already taken, simply assign it the next available slot (usually the next open one to the right). When looking up that particular value, if it is not at the expected index, keep checking the next slots for that value until either the value is found (value successfuly found in the set) or an empty slot is found (value is not in the set).

> This would be like telling two car owners who are given identical parking passes that whoever gets there first can use the spot, and whoever gets there second must find the next empty spot.

* **Method 2**: When an index conflict arises while inserting, rather than taking the next available space, utilize **chaining** to store both values at the given index. This would mean storing both values in another data structure (probably a set), then storing that set at the original index rather than either of the items directly.

> This would be like having a lift system that allows several cars to be parked in the same space, stacked vertically.

Method 1's major flaw is that it can easily create additional conflicts, which can all stack up on each other, creating unecessary extra operations when inserting or reading. Method 2 prevents this by keeping all conflicts isolated, but comes at the cost of additional overhead and complexity by adding another data structure.

## Example Use Case

Let's go ahead and use the parking lot analogy as a program.

```python
parking_lot = set()
print("Actions: ")
print("1: Park Car, 2: Remove Car, 3: Show parking lot, 4: Quit")
done = False
while not done:
    user_input = input("Select Action: ")
    try:
        selection = int(user_input)
        if selection == 1:
            parking_lot.add(input("Enter the license plate number of the car being parked: "))
        elif selection == 2:
            parking_lot.remove(input("Enter the license plate number of the car to be removed: "))
        elif selection == 3:
            print(parking_lot)
        elif selection == 4:
            done = True
            
    except ValueError:
        print("Invalid Input.")
```

## Problem Exercise

Create a program which, using a set, allows the user to record and keep track of which states you've visited. If sets are used correctly, duplicates will be automatically ignored without the need to add code to do so explicitly.

View the solution [here](code/2-solution.py).
