# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        res = []
        forward = True
        while queue:
            layer = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr:
                    layer.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if layer:
                if forward:
                    res.append(layer)
                    forward = False
                else:
                    res.append(reversed(layer))
                    forward = True
        
        return res





