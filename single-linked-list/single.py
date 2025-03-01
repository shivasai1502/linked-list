class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def update_at_pos(self, pos, data):
        if pos < 0:
            print('Invalid position')
            return
        if pos == 0:
            self.insert_at_begin(data)
            return
        new_node = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            print('Invalid position')
        else:
            new_node.next = temp.next
            temp.next = new_node

    def delete_at_pos(self, pos):
        if pos < 0:
            print('Invalid position')
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None or temp.next is None:
            print('Invalid position')
        else:
            temp.next = temp.next.next
            
    def delete_at_end(self):
        if self.head is None:
            print('List is empty')
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        
    def delete_specific(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None




    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()



    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_begin(10)
    llist.insert_at_begin(20)
    llist.insert_at_begin(30)
    llist.print_list()

    llist.insert_at_end(40)
    llist.insert_at_end(50)
    llist.print_list()

    llist.update_at_pos(2, 25)
    llist.print_list()

    llist.delete_at_pos(2)
    llist.print_list()

    llist.delete_at_end()
    llist.print_list()

    llist.delete_specific(20)
    llist.print_list()



'''
documantation:

    insert_at_begin(self, data): This method inserts a new node at the beginning of the linked list.
    insert_at_end(self, data): This method inserts a new node at the end of the linked list.
    update_at_pos(self, pos, data): This method updates the node at the given position with the new data.  
    delete_at_pos(self, pos): This method deletes the node at the given position.
    delete_at_end(self): This method deletes the last node of the linked list.
    delete_specific(self, key): This method deletes the node with the given key.
    print_list(self): This method prints the linked list.

'''

