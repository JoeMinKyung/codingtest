from collections import deque
class Node:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value=value
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self) -> None:
        self.root=None

def bfs(root):
        visited=[]
        if root is None:
            return 0
        q= deque()
        q.append(root)
        while q:
            cur_node=q.popleft()
            visited.append(cur_node.value)
            
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return visited
    
def preorder(cur_node):
    if cur_node is None:
        return
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

def inorder(cur_node):
    if cur_node is None:
        return
    preorder(cur_node.left)
    print(cur_node.value)
    preorder(cur_node.right)

def postorder(cur_node):
    if cur_node is None:
        return
    preorder(cur_node.left)
    preorder(cur_node.right)
    print(cur_node.value)

bt= BinaryTree()
bt.root=Node(value=1)
bt.root.left=Node(value=2)
bt.root.right=Node(value=3)
bt.root.left.left=Node(value=4)
bt.root.left.right=Node(value=5)
bt.root.right.right=Node(value=6)
bt.root.left.left.left=Node(value=7)
bt.root.left.left.right=Node(value=8)
print(bfs(bt.root))
preorder(bt.root)