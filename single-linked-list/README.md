# Python Linked List Implementation Guide

A comprehensive guide to understanding and implementing Singly Linked Lists in Python, including operations and practical examples.

## Table of Contents
- [Introduction](#introduction)
- [Time Complexity](#time-complexity)
- [Operations](#operations)
- [Common Use Cases](#common-use-cases)
- [Best Practices](#best-practices)
- [Contributing](#contributing)

## Introduction

A Singly Linked List is a linear data structure where each element is stored in a node, and each node points to the next node in the sequence. Unlike arrays, linked lists don't store elements in contiguous memory locations.

### Basic Node Structure

### Singly Linked List
- Each node points to the next node
- Last node points to None

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Access    | O(n)          |
| Search    | O(n)          |
| Insertion | O(1)*         |
| Deletion  | O(1)*         |

\* When inserting/deleting at the beginning. O(n) when inserting/deleting at a specific position.

## Operations

### Singly Linked List Operations
- `insert_at_begin(self, data)`: Inserts a new node at the beginning of the linked list.
- `insert_at_end(self, data)`: Inserts a new node at the end of the linked list.
- `update_at_pos(self, pos, data)`: Updates the node at the given position with the new data.
- `delete_at_pos(self, pos)`: Deletes the node at the given position.
- `delete_at_end(self)`: Deletes the last node of the linked list.
- `delete_specific(self, key)`: Deletes the node with the given key.
- `print_list(self)`: Prints the linked list.
- `reverse(self)`: Reverses the linked list.

## Common Use Cases
- Implementing stacks and queues
- Undo/Redo functionality in software
- Memory allocation
- Music playlist management
- Browser history
- Image viewer (Previous/Next)

## Best Practices
1. Always maintain proper references between nodes
2. Handle edge cases (empty list, single node)
3. Consider using sentinel nodes for easier operations
4. Implement proper error handling
5. Keep track of the list size if needed
6. Use type hints for better code readability
7. Implement proper `__str__` and `__repr__` methods

## Contributing
Feel free to submit issues and enhancement requests!
