class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None

def reverse(head):
  if not head:
    return None
  current=head
  new_head=None
  while current:
    new_head=current
    current.next,current.prev=current.prev,current.next
    current=current.prev
  return new_head
def current_ll(elements):
  if not elements:
    return None
  head=Node(elements[0])
  current=head
  for element in elements[1:]:
    new_node=Node(element)
    current.next=new_node
    new_node.prev=current
    current=current.next
  return head
def print_ll(head):
  current=head
  if current:
    print(current.data,end="")
    current=current.next
  while current:
    print(f"->{current.data}",end="")
    current=current.next
  print()
n=int(input())
nums=list(map(int,input().split()))
head=current_ll(nums)
head=reverse(head)
print_ll(head)
