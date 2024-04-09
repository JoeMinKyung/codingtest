from collections import deque
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


def LCA(root, p, q):
    if root == None:
        return None

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if root.val == p or root.val == q: # root 가 아닌 root.val을 해줘야한다.
        return root.val
    elif left and right:
        return root.val
    return left or right

root = array2tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(LCA(root, 6, 4))

