# This Doubly LinkedList is going to start from the previous Single LinkedList


# Node Class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# LinkedList Class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
    self.size = 1
  
  def get_head_node(self):
    return self.head_node
  
  def get_last_node(self):
    current_node = self.get_head_node()
    while current_node:
      next_node = current_node.get_next_node()
      if next_node == None:
        return current_node
      current_node = next_node

  def get_previous(self, value):
    if (self.get_head_node().get_value() == value):
      return None
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_next_node().get_value() == value:
        return current_node
      current_node = current_node.get_next_node()

  def get_size(self):
    print(self.size)

  def contains(self, value):
    return self.index_of(value) != -1
  
  def index_of(self, value):
    idx = 0
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() == value:
        return idx
      idx += 1
      current_node = current_node.get_next_node()
    return -1

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    self.size += 1

  def insert_last(self, new_value):
    new_node = Node(new_value)
    last_node = self.get_last_node()
    last_node.set_next_node(new_node)
    self.size += 1

  def remove_first(self):
    current_node = self.get_head_node()
    self.head_node = current_node.get_next_node()
    self.size -= 1

  def remove_last(self):
    last_node = self.get_last_node()
    prev_node = self.get_previous(last_node.get_value())
    prev_node.set_next_node(None)
    self.size -= 1

  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        if current_node.get_next_node().get_value() == value_to_remove:
            current_node.set_next_node(current_node.get_next_node().get_next_node())
            current_node = None
        else :
            current_node = current_node.get_next_node()
    self.size -= 1
    

  def stringify_list(self):
    current_node = self.get_head_node()
    string_list = ''
    while(current_node):
      print(current_node.get_value())
      string_list += str(current_node.get_value()) + '\n'
      current_node = current_node.get_next_node()
    print(string_list)

  def reverse(self):

    previous = self.get_head_node()
    current = self.head_node.get_next_node()
    while current != None:
        next = current.get_next_node()
        current.set_next_node(previous)
        previous = current
        if (next == None):
          self.head_node = current
        current = next

# Testing and Implementation

my_linkedList = LinkedList(5)
my_linkedList.insert_beginning(70)
my_linkedList.insert_beginning(5675)
my_linkedList.insert_beginning(90)
# my_linkedList.stringify_list()
# print('Head -> ', my_linkedList.get_head_node().get_value())
my_linkedList.reverse()
print(my_linkedList.get_head_node().get_value())
print(my_linkedList.get_head_node().get_next_node().get_value())
print(my_linkedList.get_head_node().get_next_node().get_next_node().get_value())
print(my_linkedList.get_head_node().get_next_node().get_next_node().get_next_node().get_value())
# my_linkedList.stringify_list()
# print('Head -> ', my_linkedList.get_head_node().get_value())
# print(my_linkedList.get_head_node().get_next_node().get_value())



