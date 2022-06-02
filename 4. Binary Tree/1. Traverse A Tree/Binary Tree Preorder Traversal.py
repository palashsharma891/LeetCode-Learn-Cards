# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:  
                    res.append(node.val)
                else:  # preorder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res
        
        
        
        
        #Recursive
        #def helper(root, ans):
         #   if not root:
          #      return
           # ans += [root.val]
            #helper(root.left, ans)
            #helper(root.right, ans)
            
        #ans = []
        #helper(root, ans)
        #return ans
