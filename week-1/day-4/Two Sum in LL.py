class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def create_ll(elements):
    if not elements:
        return None
    head=Node(elements[0])
    current=head
    for element in elements:
        current.next=Node(element)
        current=current.next
    return head
def two_sum(head,t):
    if not head:
        return None
    current=head
    nums=[]
    while current:
        nums.append(current.data)
        current=current.next
    l,r=0,len(nums)-1
    while l<r:
        if nums[l]+nums[r]==t:
            return (nums[l],nums[r])
        elif nums[l]+nums[r]<t:
            l+=1
        else:
            r-=1
n=int(input())
nums=list(map(int,input().split()))
t=int(input())
head=create_ll(nums)
print(two_sum(head,t))
