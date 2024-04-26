from collections import deque

def maxDepth(root):
    max_depth=0
    if root is None:
        return 0
    q=deque()
    q.append((root, 1))
    while q:
        cur_node,cur_depth=q.popleft()
        max_depth=max(max_depth, cur_depth)
        if cur_node.left:
            q.append((cur_node.left, cur_depth+1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth+1))  
    return max_depth

def maxDepth_postorder(root):
    max_depth=0
    if root is None:
        return max_depth
    
    left_depth=maxDepth_postorder(root.left)
    right_depth=maxDepth_postorder(root.right)
    max_depth=max(left_depth,right_depth)+1
    return max_depth

class TreeNode():
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def array2tree(arr):
    q = deque()
    root = TreeNode(arr[0])
    q.append(root)

    idx = 1
    while idx < len(arr):
        cur_node = q.popleft()

        # left Node
        if arr[idx] != None:
            cur_node.left = TreeNode(arr[idx])
            q.append(cur_node.left)
        idx += 1

        # right Node
        if arr[idx] != None:
            cur_node.right = TreeNode(arr[idx])
            q.append(cur_node.right)
        idx += 1
    return root

root=array2tree([3,9,20,None,None,15,7])

print(maxDepth(root))