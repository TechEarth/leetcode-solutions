# https://youtu.be/QfJsau0ItOY

class Solution:
    def isBalanced(self, root):
        
        def dfs(root):
            if not root: return True, 0  
            
            lb, lh = dfs(root.left)      
            rb, rh = dfs(root.right)
            
            b = abs(lh - rh) <= 1 and lb and rb

            return b, 1 + max(lh, rh)
        
        b, h = dfs(root)
        return b
    
# Time: O(N)
# Space: O(1)