#！ coding:utf-8
from TreeNode import Node

def create_tree():
    """生成满二叉树"""
    n2= Node(3)
    m2= Node(4)
    n3= Node(5)
    m3= Node(6)
    n1 = Node(2,n2,m2)
    m1 = Node(3,n3,m3)
    root = Node(1,n1,m1)
    return root


def loop_btree(root):
    """层序遍历"""
    lines=[root] #队列
    lens=[]
    levelindex=1
    while lines:
        temp=[]
        cnt=0
        cur_values=[]
        while lines:
            node= lines.pop()
            cur_values.append(str(node.value))
            cnt+=1
            if node.left:
                temp.insert(0,node.left)
            if node.right:
                temp.insert(0,node.right)
        lens.append(cnt)
        print("第{}层 有{}个\n {}".format(levelindex,cnt,",".join(cur_values)))
        if not temp:
            break
        lines= temp
        levelindex+=1
    print("每一层的元素个数",lens)



def pre_loop(root):
    if not root:
        return
    print(root.value)
    pre_loop(root.left)
    pre_loop(root.right)


def mid_loop(root):
    if not root:
        return
    mid_loop(root.left)
    print(root.value)
    mid_loop(root.right)


def aft_loop(root):
    if not root:
        return
    mid_loop(root.left)
    mid_loop(root.right)
    print(root.value)
    







if __name__ == '__main__':
    # nums=[1,2,3,4,5,6,7,8,9]
    """
         1
      2     3
    3  4   5  6
    
    """
    root=create_tree()
    loop_btree(root)
    #前序遍历
    # pre_loop(root)
    #后序遍历
    # aft_loop(root)
    #中序遍历
    mid_loop(root)
