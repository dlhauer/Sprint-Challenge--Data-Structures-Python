from doubly_linked_list import DoublyLinkedList
from dll_queue import Queue


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.order = Queue()

    def append(self, item):
        if len(self.storage) == self.capacity:
            node = self.order.dequeue()
            node.value = item
            self.order.enqueue(node)
        else:
            self.storage.add_to_tail(item)
            self.order.enqueue(self.storage.tail)

    def get(self):
        list_buffer_contents = [''] * len(self.storage) 
        node = self.storage.head
        i = 0
        while node:
            list_buffer_contents[i] = node.value
            i += 1
            node = node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

def print_list(head):
    while head:
        print(head.value)
        head = head.next

