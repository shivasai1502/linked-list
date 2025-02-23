# Python Linked List Implementation Guide

A comprehensive guide to understanding and implementing Linked Lists in Python, including different types, operations, and practical examples.

## Table of Contents
- [Introduction](#introduction)
- [Types of Linked Lists](#types-of-linked-lists)
- [Basic Operations](#basic-operations)
- [Implementation Examples](#implementation-examples)
- [Time Complexity](#time-complexity)
- [Common Use Cases](#common-use-cases)
- [Best Practices](#best-practices)

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

## Basic Operations

### 1. Insertion
```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

def insert_at_position(self, data, position):
    if position == 0:
        self.insert_at_beginning(data)
        return
    new_node = Node(data)
    current = self.head
    for i in range(position - 1):
        if current is None:
            raise IndexError("Position out of range")
        current = current.next
    new_node.next = current.next
    current.next = new_node
```

### 2. Deletion
```python
def delete_node(self, key):
    current = self.head
    if current and current.data == key:
        self.head = current.next
        return
    while current and current.next:
        if current.next.data == key:
            current.next = current.next.next
            return
        current = current.next
```

### 3. Traversal
```python
def display(self):
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
```

## Implementation Examples

### Example 1: Creating and Using a Singly Linked List
```python
# Create a linked list
llist = SinglyLinkedList()

# Add elements
llist.append(1)
llist.append(2)
llist.append(3)

# Display the list
llist.display()  # Output: 1 -> 2 -> 3 -> None

# Insert at beginning
llist.insert_at_beginning(0)
llist.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Delete a node
llist.delete_node(2)
llist.display()  # Output: 0 -> 1 -> 3 -> None
```

### Example 2: Implementing a Stack using Linked List
```python
class LinkedListStack:
    def __init__(self):
        self.linked_list = SinglyLinkedList()

    def push(self, data):
        self.linked_list.insert_at_beginning(data)

    def pop(self):
        if not self.linked_list.head:
            raise IndexError("Stack is empty")
        data = self.linked_list.head.data
        self.linked_list.head = self.linked_list.head.next
        return data
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

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
