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

# class Queue:
  
#   def __init__(self, max_size=None):
#     self.head = None
#     self.tail = None
#     self.max_size = max_size
#     self.size = 0
    
#   def enqueue(self, value):
#     if self.has_space():
#       item_to_add = Node(value)
#       print("Adding " + str(item_to_add.get_value()) + " to the queue!")
#       if self.is_empty():
#         self.head = item_to_add
#         self.tail = item_to_add
#       else:
#         self.tail.set_next_node(item_to_add)
#         self.tail = item_to_add
#       self.size += 1
#     else:
#       print("Sorry, no more room!")
         
#   def dequeue(self):
#     if self.get_size() > 0:
#       item_to_remove = self.head
#       print(str(item_to_remove.get_value()) + " is served!")
#       if self.get_size() == 1:
#         self.head = None
#         self.tail = None
#       else:
#         self.head = self.head.get_next_node()
#       self.size -= 1
#       return item_to_remove.get_value()
#     else:
#       print("The queue is totally empty!")
  
#   def peek(self):
#     if self.size > 0:
#       return self.head.get_value()
#     else:
#       print("No orders waiting!")
  
#   def get_size(self):
#     return self.size
  
#   def has_space(self):
#     if self.max_size == None:
#       return True
#     else:
#       return self.max_size > self.get_size()
    
#   def is_empty(self):
#     return self.size == 0
  
#   def reverse(self):
#     # verify if the queue is not empty
#     if self.is_empty():
#       return 'The Queue is empty'
#     # verify if list has just one element
#     if self.get_size() == 1:
#       return self.head
#     q_list = []
#     counter = self.get_size()

#     while counter > 0:
#       q_list.append(self.dequeue())
#       counter -= 1
    
#     for i in range(0, len(q_list)):
#       value = q_list.pop()
#       self.enqueue(value)



    

# my_q = Queue()
# my_q.enqueue(5)
# my_q.enqueue(10)
# my_q.enqueue(15)
# my_q.enqueue(40)

# # 5 -> 10 -> 15 -> 20

# # 20 -> 15 -> 10 -> 5
# print('head before', my_q.head.get_value())
# # print(my_q.peek())
# my_q.reverse()
# # print(my_q.head.get_value())
# print('head after', my_q.head.get_value())

class Queue:
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def peek(self):
    return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def is_empty(self):
    return self.get_size() == 0

  def enqueue(self, value):
    new_element = Node(value)
    if self.size == 0:
      self.head = new_element
    else:
      self.tail.set_next_node(new_element)

    self.tail = new_element
    self.size += 1
  
  def dequeue(self):
    if self.get_size() == 0:
      return 'The queue is empty'
    item_removed = self.head

    if self.get_size() == 1:
      self.head = None
      self.tail = None
    else:
      new_head = item_removed.get_next_node()
      item_removed.set_next_node(None)
      self.head = new_head

    self.size -= 1
    return item_removed.get_value()
  
  def reverse(self):
    if self.is_empty():
      return 'Queue is empty'
    
    counter = self.get_size()
    if counter == 1:
      return self.head
    
    q_list = []

    while counter > 0:
      q_list.append(self.dequeue())
      counter -= 1
    
    for i in range(0, len(q_list)):
      self.enqueue(q_list.pop())

  def stringnify(self):
    str_queue = ''
    current = self.head

    while current:
      str_queue += str(current.get_value()) + ' '
      current = current.get_next_node()

    return str_queue
    
    

    
q = Queue()
q.enqueue(5)
q.enqueue(53)
q.enqueue(3)
# print(q.is_empty())
# print('size', q.get_size())
q.enqueue(15)
q.enqueue(56)
print(q.stringnify())
# print('head', q.peek())
# print(q.head.get_value())
# print(q.tail.get_value())
# print(q.head.get_next_node().get_next_node().get_next_node().get_value())
# print(q.dequeue())
# print(q.dequeue())
# print(q.head)
# print(q.tail)
# print(q.head.get_value())
# print(q.tail.get_value())
# print(q.is_empty())
# print('size', q.get_size())
# print('head', q.peek())
q.reverse()
print(q.stringnify())
# print('size', q.get_size())
# print('head', q.peek())
# print(q.stringnify())