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
    self.head_node = Node(None)
    self.tail_node = Node(None)
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_node = self.head_node
    if current_node != None:
      current_node.set_prev_node(new_head)
      new_head.set_next_node(self.head_node)
    self.head_node = new_head
    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    # create a new_tail node with the new value
    new_tail = Node(new_value)
    # create a current_node var which is equal to list's tail_node
    current_node = self.tail_node
    # If current_node is not None:
    if current_node != None:
    #  - new_tail prev to current_node
      new_tail.set_prev_node(current_node)
    #  - current_node next to new_tail
      current_node.set_next_node(new_tail)
    # list's tail_node should be equals to new_tail
    self.tail_node = new_tail
    # if list's head_node is None:
    if self.head_node == None:
    #  - list's head_node equals to new_tail
      self.head_node = new_tail

  def remove_head(self):
    # create a var removed_head which is the current head of the list
    removed_head = self.head_node
    # if current_head == None:
    if removed_head == None:
    #  - return None
      return None
    # set list's head_node equals to removed_head's next node
    self.head_node = removed_head.get_next_node()
    # If lists head_node is not None
    if self.head_node != None:
    #  - Set list's head node's prev node to None
        self.head_node.set_prev_node(None)
    # If removed+_head is equal to list's tail node
    if removed_head == self.tail_node:
    #  - use remove_tail
      self.remove_tail() 
    # return the removed_head
    return removed_head
  
  def remove_tail(self):
    pass

dll = DoublyLinkedList()
# dll.add_to_tail(2)
# print(dll.tail_node.get_value())
# dll.add_to_tail(6)
# print(dll.tail_node.get_value())
dll.add_to_head(15)
dll.add_to_head(30)
print(dll.head_node.get_value())
dll.remove_head()
print(dll.head_node.get_value())
dll.remove_head()
print(dll.head_node.get_value())



  
    