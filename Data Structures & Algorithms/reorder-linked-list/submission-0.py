# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head 
        stack = []

        while tail: 
            stack.append(tail)
            tail = tail.next
        
        curr = head 
        for _ in range(len(stack) // 2):
            temp = curr.next 
            node = stack.pop()
            curr.next = node 
            node.next = temp 
            curr = temp 
        
        curr.next = None



            
        


        