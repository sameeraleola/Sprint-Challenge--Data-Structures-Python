from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # # Oldest is first in (head)
        # Make sure there's room
        if len(self.storage) < self.capacity:
            # It is not full so add it to the tail
            self.storage.add_to_tail(item)
            # Keep track of the last item added
            self.current = self.storage.tail
        else:
            # Remove the head then add the new node
            new_head = self.storage.head.next
                self.next.prev = self.prev


    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
               
  

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        item = self.storage.head
        while item:
            if item.value i!= None:
                list_buffer_contents.append(item.value)
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
