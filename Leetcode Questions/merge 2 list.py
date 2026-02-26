class node:
  def __init__(self,val=0,next = None):
    self.val = val
    self.next = None

class solution:
  def merge2lists(self,head1,head2):

    if head1 is None:
      return head2
    if head2 is None:
      return head1

    if head1.val <= head2.val:
      head1.next = self.merge2lists(head1.next,head2)
      return head1
    else:
      head2.next = self.merge2lists(head1,head2.next)
      return head2
    
a = node(1)
a.next = node(2)
a.next.next = node(3) 

b = node(4)
b.next = node(5)
b.next.next = node(6)

result = solution().merge2lists(a,b)

while result:
  print(result.val,end="  ")
  result = result.next

        