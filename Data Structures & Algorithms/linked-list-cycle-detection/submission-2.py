# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        curr = head 
        index = -1 

        while curr:
            visited.append(curr)
            if curr.next in visited : 
                index = 0 
                break
            curr = curr.next 
        
        if index == -1 :
            return False 
        else: 
            return True 
                
        