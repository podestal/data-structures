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


dll = DoublyLinkedList()
dll.add_to_head(15)
dll.add_to_head(30)



  
    