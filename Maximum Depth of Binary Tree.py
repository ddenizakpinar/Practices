# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root == None:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    if (left > right):
        return left + 1
    else:
        return right + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)
print(maxDepth(root))