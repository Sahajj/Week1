class Node:
   def __init__(self, my_data):
      self.data = my_data
      self.next = None

class linked_list:
   def __init__(self):
      self.head = None
     
   def add_data(self,my_data):
      new_node = Node(my_data)
      new_node.next = self.head
      self.head = new_node
   
   def reverse(self):
      prev = None
      current = self.head
      while(current is not None):
         next = current.next
         current.next = prev
         prev = current
         current = next
      self.head = prev
   
   def print_it(self):
      temp = self.head
      while(temp):
         print(temp.data)
         temp = temp.next

my_list = linked_list()
my_list.add_data(47)
my_list.add_data(89)
my_list.add_data(34)
my_list.add_data(11)

print("The list is : ")
my_list.print_it()
print("The list is being reversed")
my_list.reverse()
print("The reversed list is : ")
my_list.print_it()