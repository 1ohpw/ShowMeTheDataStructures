class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DLList(object):
    def __init__(self):
        self.sentinel = Node(None, None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def prepend(self, insert_node):
        if insert_node.next:
            old_next = insert_node.next
            old_prev = insert_node.prev
            old_prev.next = old_next
            old_next.prev = old_prev
        insert_node.prev = self.sentinel
        insert_node.next = self.sentinel.next
        self.sentinel.next = insert_node
        insert_node.next.prev = insert_node
    
    def pop_last(self):
        last_node = self.sentinel.prev
        new_last = last_node.prev
        new_last.next = last_node.next
        self.sentinel.prev = new_last
        return last_node
    
class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.used_list = DLList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        node = self.cache.get(key, None)
        if node:
            self.used_list.prepend(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache or self.capacity <= 0:
            return

        if len(self.cache) == self.capacity:
            key_to_remove = self.used_list.pop_last().key
            self.cache.pop(key_to_remove)

        node = Node(key, value)
        self.cache[key] = node
        self.used_list.prepend(node)

#Test Cache
our_cache = LRU_Cache(5)

#Test Case 1
#print(our_cache.get(1))
#expected --> -1

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


#Test Case 2
#print(our_cache.get(1))       
#expected --> 1

#Test Case 3
#print(our_cache.get(2))      
#expected --> 2

#Test Case 4
#print(our_cache.get(9))
#expected --> -1

our_cache.set(5, 5) 
our_cache.set(6, 6)

#Test Case 5
#print(our_cache.get(3))
#expected --> -1

#Test Cache 2
our_small_cache = LRU_Cache(1)
our_small_cache.set(1, 1) 

#Test Case 6
# print(our_small_cache.get(1))
#expected --> 1
our_small_cache.set(2, 2) 
# print(our_small_cache.get(1))
#expected --> -1

#Test Cache 3
our_empty_cache = LRU_Cache(0)

#Test Case 7
our_empty_cache.set(1, 1) 
# print(our_empty_cache.get(1))
#expected --> -1