# Python Linked List Implementation Guide

A comprehensive guide to understanding and implementing Linked Lists in Python, including different types, operations, and practical examples.

## Table of Contents
- [Introduction](#introduction)
- [Types of Linked Lists](#types-of-linked-lists)
- [Time Complexity](#time-complexity)
- [Common Use Cases](#common-use-cases)
- [Best Practices](#best-practices)
- [Contributing](#contributing)

## Introduction

A Linked List is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked lists don't store elements in contiguous memory locations.

### Basic Node Structure
```python
class Node:
    def __init__(self, data):
        self.data = data    # Store the actual data
        self.next = None    # Reference to next node
```

## Types of Linked Lists

### 1. Singly Linked List
- Each node points to the next node
- Last node points to None

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
```

### 2. Doubly Linked List
- Each node has references to both next and previous nodes

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
```

### 3. Circular Linked List
- Last node points back to the first node

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
```


## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Access    | O(n)          |
| Search    | O(n)          |
| Insertion | O(1)*         |
| Deletion  | O(1)*         |

\* When inserting/deleting at the beginning. O(n) when inserting/deleting at a specific position.

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

