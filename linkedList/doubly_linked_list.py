# class Node:
#   def __init__(self, value, next_node=None, prev_node=None):
#     self.value = value
#     self.next_node = next_node
#     self.prev_node = prev_node
    
#   def set_next_node(self, next_node):
#     self.next_node = next_node
    
#   def get_next_node(self):
#     return self.next_node

#   def set_prev_node(self, prev_node):
#     self.prev_node = prev_node
    
#   def get_prev_node(self):
#     return self.prev_node
  
#   def get_value(self):
#     return self.value
    
# class DoublyLinkedList:
#   def __init__(self):
#     self.head_node = Node(None)
#     self.tail_node = Node(None)
  
#   def add_to_head(self, new_value):
#     new_head = Node(new_value)
#     current_node = self.head_node
#     if current_node != None:
#       current_node.set_prev_node(new_head)
#       new_head.set_next_node(self.head_node)
#     self.head_node = new_head
#     if self.tail_node == None:
#       self.tail_node = new_head

#   def add_to_tail(self, new_value):
#     # create a new_tail node with the new value
#     new_tail = Node(new_value)
#     # create a current_node var which is equal to list's tail_node
#     current_node = self.tail_node
#     # If current_node is not None:
#     if current_node != None:
#     #  - new_tail prev to current_node
#       new_tail.set_prev_node(current_node)
#     #  - current_node next to new_tail
#       current_node.set_next_node(new_tail)
#     # list's tail_node should be equals to new_tail
#     self.tail_node = new_tail
#     # if list's head_node is None:
#     if self.head_node == None:
#     #  - list's head_node equals to new_tail
#       self.head_node = new_tail

#   def remove_head(self):
#     # create a var removed_head which is the current head of the list
#     removed_head = self.head_node
#     # if current_head == None:
#     if removed_head == None:
#     #  - return None
#       return None
#     # set list's head_node equals to removed_head's next node
#     self.head_node = removed_head.get_next_node()
#     # If lists head_node is not None
#     if self.head_node != None:
#     #  - Set list's head node's prev node to None
#         self.head_node.set_prev_node(None)
#     # If removed+_head is equal to list's tail node
#     if removed_head == self.tail_node:
#     #  - use remove_tail
#       self.remove_tail() 
#     # return the removed_head
#     return removed_head

#   def remove_tail(self):
#     # create a var for the deleted_tail = self.tail_node
#     deleted_tail = self.tail_node
#     # if deleted_tail == None:
#     if deleted_tail == None:
#       # return None
#       return None
#     # set the list's tail to the prev node of the deleted tail
#     self.tail_node = deleted_tail.get_prev_node()
#     # if new tail is not None
#     if self.tail_node != None:
#       # Set the list's tail node to None
#       self.tail_node.set_next_node(None)
#     # if the removed tail was also the head
#     if deleted_tail == self.head_node:
#       # call remove_head
#       self.remove_head
#     # Return deleted tail
#     return deleted_tail

#   def remove_by_value(self, value):
#     # get the head node and save it in a var called current_node
#     current_node = self.head_node
#     # if current_node is None
#     if current_node == None:
#       # return None
#       return None
#     # start a loop that keeps going while current_node is not None
#     while current_node != None:
#       # get the prev and next nodes from current_node
#       print('Before anything', current_node.get_value())
#       prev_node = current_node.get_prev_node()
#       next_node = current_node.get_next_node()
#       # if current_node value is equal to the given value
#       if current_node.get_value() == value:
#         # set current node next, prev and itself to None
#         current_node.set_prev_node(None)
#         current_node.set_next_node(None)
#         # set its next node to next_node var
#         prev_node.set_next_node(next_node)
#         # set its next node to next_node var
#         next_node.set_next_node(prev_node)
#         # verify if current_node is head if so set head to the next
#         if current_node == self.head_node:
#           self.head_node = next_node
#         # verify if current_node is tail if so set head to the prev
#         if current_node == self.tail_node:
#           self.tail_node = prev_node
#         current_node = None
#       else:
#         current_node = next_node



# dll = DoublyLinkedList()
# # dll.add_to_tail(2)
# # print(dll.tail_node.get_value())
# # dll.add_to_tail(6)
# # print(dll.tail_node.get_value())
# dll.add_to_head(15)
# dll.add_to_head(30)
# dll.add_to_head(76)
# dll.add_to_tail(100)
# dll.add_to_tail(145)
# dll.add_to_tail(111)
# print(dll.head_node.get_value())
# print(dll.head_node.get_next_node().get_value())
# dll.remove_by_value(76)
# print('//////////////////////')
# print(dll.head_node.get_value())
# print(dll.head_node.get_next_node().get_value())


class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value


class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node
    if current_tail != None:
      current_tail.set_next_node(new_node)
      new_node.set_prev_node(current_tail)

    self.tail_node = new_node

    if self.head_node == None:
      self.head_node == new_node





    
    


l = LinkedList()
# print(l.head_node())
l.add_to_head(6)
l.add_to_head(10)
l.add_to_tail(111)
l.add_to_tail(22)
print(l.head_node.get_value())
print(l.head_node.get_next_node().get_value())
print(l.head_node.get_next_node().get_next_node().get_value())
