from LinkNode import Node


def create_linklist(nums):
    head=Node(nums[0],None)
    p=head
    for i in nums[1:]:
        p.next = Node(i,None)
        p= p.next
    return head

def show_linklist(head):
    nums=[]
    while head:
        v=head.value
        nums.append(v)
        print(v)
        head= head.next
    return nums

def reverse_linklist(head):
    """递归的方式
    较难理解
    pre递归那行一直压栈，直到满足None条件才返回，
    1->2->3-4->5-N
    5-N->4->3->2->1
    第一次返回的时候，head =4  ，pre =5-> N，
    head.next.next =head 让它成环，4->5->4... pre变为5->4->5.. 也是环
    然后再断开4-N ,则 pre 变成5->4-N
    返回到head 3 时候
    继续
    ...
    然后再断开3-N ,则 pre 变成5->4->3-N
    返回到head 2 时候
    继续
    ...
    然后再断开2-N ,则 pre 变成5->4->3->2->N
    返回到head 1 时候
    继续
    ...
    然后再断开2-N ,则 pre 变成5->4->3->2->1-N

    总结： 递归的实现很巧妙，编程之美
    有个成环，再拆环的步骤，

    """
    if not head.next or not head:
        return head
    pre = reverse_linklist(head.next)
    head.next.next =head
    head.next=None
    return pre

def reverse_linklist1(head):
    """迭代的方式实现
    最为简单粗暴，无算法
    """
    pre =None
    while head:
        v= head.value
        pre = Node(v,pre)
        head = head.next
    return pre


def reverse_linklist2(head):
    """双指针法实现：
    原理就是从head开始移动，每移动一个，就放在pre头的位置
    需要保存下次的head，temp
    """
    cur= head
    pre=None
    while cur:
        temp = cur.next
        cur.next =pre
        pre= cur
        cur = temp
    return pre




if __name__ == '__main__':
    nums=[1,2,3,4,5,6,7,8,9]
    head = create_linklist(nums)
    show_linklist(head)
    print("xxxx"*20)
    head1 = reverse_linklist2(head)
    show_linklist(head1)

