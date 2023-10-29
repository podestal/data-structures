# We'll be using our Node class
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

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
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

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def insert_last(self, new_value):
    new_node = Node(new_value)
    last_node = self.get_last_node()
    last_node.set_next_node(new_node)

  def remove_first(self):
    current_node = self.get_head_node()
    self.head_node = current_node.get_next_node()

  def remove_last(self):
    last_node = self.get_last_node()
    prev_node = self.get_previous(last_node.get_value())
    prev_node.set_next_node(None)

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

  def stringify_list(self):
    current_node = self.get_head_node()
    string_list = ''
    while(current_node):
      string_list += str(current_node.get_value()) + '\n'
      current_node = current_node.get_next_node()
    print(string_list)


my_linkedList = LinkedList(5)
my_linkedList.insert_beginning(70)
my_linkedList.insert_beginning(5675)
my_linkedList.insert_beginning(90)
my_linkedList.stringify_list()
# my_linkedList.remove_node(5)
my_linkedList.insert_last(999)
my_linkedList.stringify_list()
# my_linkedList.remove_first()
my_linkedList.stringify_list()
print(my_linkedList.get_previous(90))
my_linkedList.remove_last()
my_linkedList.remove_last()
my_linkedList.stringify_list()



