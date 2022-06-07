# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #DFS - recursive
        def dfs(root, level, ans):
            if not root:
                return
            if len(ans) < level+1:
                ans.append([])
            ans[level].append(root.val)
            dfs(root.left, level+1, ans)
            dfs(root.right, level+1, ans)
        
        ans = []
        dfs(root, 0, ans)
        return ans
    
        #DFS iterative mein bas swap(curr.right, curr.left) and pop(0) ya popleft() ki jagah sirf pop()
        
        
        
        #BFS
        '''
        if not root:
            return []
        ans, q = [], [root]
        while q:
            row = []
            l = len(q)
            for i in range(l):
                curr = q.pop(0)
                row += [curr.val]
                if curr.left:
                    q += [curr.left]
                if curr.right:
                    q += [curr.right]

            ans += [row]
            
        return ans'''
