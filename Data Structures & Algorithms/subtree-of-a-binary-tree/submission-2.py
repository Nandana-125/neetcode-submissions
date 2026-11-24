# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(a,b):
            if not a and not b : 
                return True 
            
            if not a or not b or a.val != b.val : 
                return False 

            
            leftcheck = same(a.left,b.left)
            rightcheck = same(a.right,b.right)

            return leftcheck and rightcheck 


        if not subRoot:
            return True 
        if not root : 
            return False 

        if same(root, subRoot):
            return True 
        
        left = self.isSubtree(root.left,subRoot) 
        right = self.isSubtree(root.right,subRoot) 

        return left or right 
        