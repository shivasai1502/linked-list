# Double Linked List

This repository contains an implementation of a double linked list in Python. The `double.py` file includes the `ListNode` and `DoubleLinkedList` classes, which provide methods for inserting, updating, deleting, and displaying nodes in the list.

## Theoretical Concepts

A double linked list is a type of linked list in which each node contains a data part and two pointers, `prev` and `next`, which point to the previous and next nodes in the sequence, respectively. This allows traversal of the list in both forward and backward directions.

### Advantages
- **Bidirectional Traversal**: Nodes can be traversed in both forward and backward directions.
- **Ease of Deletion**: Deleting a node is more efficient as we have direct access to the previous node.

### Disadvantages
- **Increased Memory Usage**: Each node requires extra memory for the `prev` pointer.
- **Complexity**: Operations like insertion and deletion are more complex compared to a singly linked list due to the need to update two pointers.

## Classes

### ListNode
Represents a node in the double linked list.
- `__init__(self, data)`: Initializes a new node with the given data, setting `prev` and `next` to `None`.

### DoubleLinkedList
Represents the double linked list.
- `__init__(self)`: Initializes an empty double linked list with `head` and `tail` set to `None`.
- `insert_at_begin(self, data)`: Inserts a new node with the given data at the beginning of the list.
- `insert_at_end(self, data)`: Inserts a new node with the given data at the end of the list.
- `update_at_pos(self, pos, data)`: Updates the node at the specified position with the given data.
- `delete_at_pos(self, pos)`: Deletes the node at the specified position.
- `display(self)`: Displays the data of all nodes in the list.

## Usage

To use the double linked list, create an instance of `DoubleLinkedList` and call its methods as needed. Below is an example:

```python
dll = DoubleLinkedList()
dll.insert_at_begin(10)
dll.insert_at_begin(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.display()  # Output: 20 10 30 40 50
dll.update_at_pos(2, 25)
dll.display()  # Output: 20 10 25 30 40 50
dll.delete_at_pos(3)
dll.display()  # Output: 20 10 25 40 50
dll.delete_at_pos(3)
dll.display()  # Output: 20 10 25 50
dll.delete_at_pos(0)
dll.display()  # Output: 10 25 50
dll.delete_at_pos(0)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any questions or inquiries, please contact the repository owner.
