class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    union_set = set()

    if llist_1:
        current_1 = llist_1.head
        while current_1:
            union_set.add(current_1.value)
            current_1 = current_1.next

    if llist_2:
        current_2 = llist_2.head
        while current_2:
            union_set.add(current_2.value)
            current_2 = current_2.next

    union_list = LinkedList()
    for val in union_set:
        union_list.append(Node(val))
    return union_list

def intersection(llist_1, llist_2):
    set_1 = set()
    set_2 = set()
    
    if llist_1:
        current_1 = llist_1.head
        while current_1:
            set_1.add(current_1.value)
            current_1 = current_1.next

    if llist_2:
        current_2 = llist_2.head
        while current_2:
            set_2.add(current_2.value)
            current_2 = current_2.next
    
    intersection_set = set_1.intersection(set_2)
    intersection_list = LinkedList()
    for val in intersection_set:
        intersection_list.append(Node(val))
    return intersection_list

# Test case 1

# linked_list_1 = LinkedList()
# linked_list_2 = LinkedList()

# element_1 = [3,2,4,35,6,65,6,4,3,21]
# element_2 = [6,32,4,9,6,1,11,21,1]

# for i in element_1:
#     linked_list_1.append(i)

# for i in element_2:
#     linked_list_2.append(i)

# print (union(linked_list_1,linked_list_2))
# print (intersection(linked_list_1,linked_list_2))
#expected ---> 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
#expected ---> 4 -> 21 -> 6 -> 

# Test case 2

# linked_list_3 = LinkedList()
# linked_list_4 = LinkedList()

# element_1 = [3,2,4,35,6,65,6,4,3,23]
# element_2 = [1,7,8,9,11,21,1]

# for i in element_1:
#     linked_list_3.append(i)

# for i in element_2:
#     linked_list_4.append(i)

#print (union(linked_list_3,linked_list_4))
#print (intersection(linked_list_3,linked_list_4))
#expected ---> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
#expected ---> nothing

# Test Case 3

# linked_list_5 = LinkedList()
# linked_list_6 = LinkedList()

# element_1 = []
# element_2 = [1,7,8,9,11,21,1]

# for i in element_1:
#     linked_list_5.append(i)

# for i in element_2:
#     linked_list_6.append(i)
# print (union(linked_list_5,linked_list_6))
# print (intersection(linked_list_5,linked_list_6))
#expected ---> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
#expected ---> nothing

# Test Case 4

# linked_list_7 = LinkedList()
# linked_list_8 = LinkedList()

# element_1 = [1,2,3]
# element_2 = [1,2,3]

# for i in element_1:
#     linked_list_7.append(i)

# for i in element_2:
#     linked_list_8.append(i)
# print (union(linked_list_7,linked_list_8))
# print (intersection(linked_list_7,linked_list_8))
#expected ---> 1 -> 2 -> 3 ->
#expected ---> 1 -> 2 -> 3 ->

# Test Case 5

# linked_list_9 = None
# linked_list_10 = None

# element_1 = []
# element_2 = []

# for i in element_1:
#     linked_list_9.append(i)

# for i in element_2:
#     linked_list_10.append(i)
# print (union(linked_list_9,linked_list_10))
# print (intersection(linked_list_9,linked_list_10))
#expected ---> nothing
#expected ---> nothing