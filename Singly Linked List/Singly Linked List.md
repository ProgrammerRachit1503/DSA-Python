Singly Linked List in Python

This document provides an overview of the Python implementation of a Singly Linked List. This code was developed as a learning exercise and includes a comprehensive set of methods for list manipulation, as well as several sorting algorithms adapted for this data structure.

## Core Concepts

The implementation is built on two primary classes: Node and LinkedList.

### The Node Class

The Node is the fundamental building block of the linked list. Each node is a simple object that contains:

- `value`: The data stored in the node (can be of any type).

- `next`: A pointer that references the next Node in the sequence. If it's the last node, this pointer is None.

### The LinkedList Class

This class acts as the manager for the entire list. It holds the core logic for all operations and maintains three key attributes:

- `head`: A pointer to the very first Node in the list.

- `tail`: A pointer to the very last Node. Keeping track of the tail allows for highly efficient additions to the end of the list (O(1) time complexity).

- `length`: An integer that stores the current number of nodes in the list. This provides an instant way to check the list's size without having to traverse it.

## Basic Operations (CRUD)

This LinkedList class supports a full range of methods for creating, reading, updating, and deleting nodes.

### Adding Nodes

- `append(value)`: Adds a new node to the end of the list. This is an efficient O(1) operation because we directly access the tail.

- `prepend(value)`: Adds a new node to the beginning of the list. This is also an efficient O(1) operation as it only requires updating the head.

- `insert(index, value)`: Inserts a new node at a specific position within the list.

### Removing Nodes

- `pop()`: Removes the last node from the list. In a singly linked list, this is an O(n) operation because we must traverse the list from the head to find the second-to-last node.

- `pop_first()`: Removes the first node from the list. This is an efficient O(1) operation.

- `remove(index)`: Removes a node from a specific position.

### Accessing and Modifying Data

- `get(index)`: Retrieves the node at a given index.

- `set_value(index, value)`: Updates the value of the node at a given index.

## Advanced Algorithms

Beyond basic manipulations, this implementation includes several more complex algorithms.

### `reverse()`

This method reverses the linked list in place. It does this by iterating through the list and reversing the direction of the next pointers for each node. The original `head` becomes the new `tail`, and the original `tail` becomes the new `head`.

### `merge(other_list)`

This method merges a second sorted linked list into the current one, ensuring the final combined list remains sorted. It works by comparing the nodes from both lists and linking them in the correct order.

### Sorting Algorithms on a Linked List

Sorting a linked list presents a unique challenge because you cannot instantly access elements by an index as you would with an array. These algorithms are adapted to work by traversing the nodes and swapping their values.

- `bubble_sort()`: Implements the bubble sort algorithm by repeatedly stepping through the list, comparing adjacent nodes, and swapping their values if they are in the wrong order.

- `selection_sort()`: Implements selection sort by repeatedly finding the minimum value in the unsorted part of the list and swapping it with the value at the beginning of that unsorted part.

- `insertion_sort()`: Implements insertion sort by building a sorted list one element at a time. It takes each node from the unsorted portion and inserts it into its correct position in the sorted portion.

## Utilities and Testing

The file also contains helper functions (`create_linked_list`, `linked_list_to_list`) and a robust suite of `test_...` functions. These tests ensure the sorting algorithms are implemented correctly by checking them against various scenarios, including empty lists, reversed lists, and lists with duplicate values.