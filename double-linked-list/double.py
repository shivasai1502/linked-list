class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begin(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        node = ListNode(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def update_at_pos(self, pos, data):
        if pos < 0:
            print('Invalid position')
            return
        temp = self.head
        for _ in range(pos):
            if temp is None:
                print('Invalid position')
                return
            temp = temp.next
        if temp is None:
            print('Invalid position')
        else:
            temp.data = data

    def delete_at_pos(self, pos):
        if pos < 0:
            print('Invalid position')
            return
        temp = self.head
        if pos == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            return
        for _ in range(pos):
            if temp is None:
                print('Invalid position')
                return
            temp = temp.next
        if temp is None:
            print('Invalid position')
        else:
            if temp == self.tail:
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None
            else:
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

dll = DoubleLinkedList()
dll.insert_at_begin(10)
dll.insert_at_begin(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.display()
dll.update_at_pos(2, 25)
dll.display()
dll.delete_at_pos(3)
dll.display()
dll.delete_at_pos(3)
dll.display()
dll.delete_at_pos(0)
dll.display()
dll.delete_at_pos(0)