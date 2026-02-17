class node:
  def __init__(self,value):
    self.value = value
    self.next = None

class singly_linked_list:
  def __init__(self):
    self.head = None

  def append(self,value):
    newnode = node(value)

    if self.head == None:
      self.head = newnode
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = newnode

  def traverse(self):
    if self.head == None:
      print("sll is empty")  
    else:
      curr = self.head 
      while curr is not None:
        print(curr.value, end=" -> ")
        curr = curr.next   # ⭐ important

s11 = singly_linked_list()
s11.append(12)
s11.append(34)
s11.append(45)
s11.append(50)
s11.traverse()