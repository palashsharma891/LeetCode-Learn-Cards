# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], [(root, False)]
        
        while stack:
            curr, visited = stack.pop()
            
            if curr:
                if visited:
                    ans += [curr.val]
                else:
                    stack += [(curr.right, False)]
                    stack += [(curr, True)]
                    stack += [(curr.left, False)]
        
        return ans
        
        
        
        
        
        #Recursive
        #def helper(root, ans):
         #   if not root:
          #      return
           # helper(root.left, ans)
            #ans += [root.val]
            #helper(root.right, ans)
            
        #ans = []
        #helper(root, ans)
        #return ans
