class Node(object):
    def __init__(self,value,next=None):
        self.value = value
        self.next = next



def create_linklist(nums):
    head=Node(nums[0],None)
    p=head
    for i in nums[1:]:
        p.next = Node(i,None)
        p= p.next
    return head

def show_linklist(head):
    nums=[]
    outputs=""
    while head:
        v=head.value
        nums.append(v)
        outputs+="->"+str(v) if outputs else str(v)
        head= head.next
    outputs += "-> None"
    print(outputs)
    return nums

def len_linklist(head):
    if not head:
        return 0
    return len_linklist(head.next)+1
