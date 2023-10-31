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

dll = DoublyLinkedList()
dll.add_to_tail(2)
print(dll.tail_node.get_value())
dll.add_to_tail(6)
print(dll.tail_node.get_value())
# dll.add_to_head(15)
# dll.add_to_head(30)



  
    