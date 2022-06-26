# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        Q = [root]
        levels = 0
        nodes_per_level = 1
        
        while Q:
            curr = Q.pop(0)
            if curr.left:
                Q += [curr.left]
            if curr.right:
                Q += [curr.right]
            
            nodes_per_level -= 1
            
            if nodes_per_level == 0:
                levels += 1
                nodes_per_level = len(Q)
                
        return levels
        
        
        #recursive
        #if not root:
         #   return 0
        
        #left_ans = self.maxDepth(root.left)
        #right_ans = self.maxDepth(root.right)
        #return max(left_ans, right_ans) + 1
        
