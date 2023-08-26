class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBST(nodes, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    root = TreeNode(nodes[mid])
    root.left = constructBST(nodes, start, mid - 1)
    root.right = constructBST(nodes, mid + 1, end)
    return root

def rangeSumBST(root, start, end):
    if not root:
        return 0
    
    if root.val < start:
        return rangeSumBST(root.right, start, end)
    elif root.val > end:
        return rangeSumBST(root.left, start, end)
    else:
        return root.val + rangeSumBST(root.left, start, end) + rangeSumBST(root.right, start, end)

# Input: Number of nodes in the binary search tree
n = int(input())
# Input: Nodes of the binary search tree
nodes = list(map(int, input().split()))
# Input: Range start and end values
start, end = map(int, input().split())

root = constructBST(sorted(nodes), 0, len(nodes) - 1)

result = rangeSumBST(root, start, end)
print(result)
