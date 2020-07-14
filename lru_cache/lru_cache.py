from doubly_linked_list.doubly_linked_list import DoublyLinkedList
"""
Our LRUCache class keeps track of the max number of nodes it
can hold, the current number of nodes it is holding, a doubly-
linked list that holds the key-value entries in the correct
order, as well as a storage dict that provides fast access
to every node stored in the cache.
"""


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        current = self.storage.head
        while current is not None:
            if current.value[0] == key:
                self.storage.move_to_front(current)
                return current.value[1]
            current = current.next
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        current = self.storage.head
        replaced = False
        while current is not None and replaced is not True:
            if current.value[0] == key:
                current.value[1] = value
                self.storage.move_to_front(current)
                replaced = True
            current = current.next

        if self.length == self.limit and replaced is not True:
            self.storage.remove_from_tail()
            self.storage.add_to_head([key, value])
        elif replaced is not True:
            self.storage.add_to_head([key, value])
            self.length = self.storage.length
