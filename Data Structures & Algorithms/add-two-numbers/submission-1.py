# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy 
        curr1 = l1 
        curr2 = l2  
        carry = 0 
        while curr1 or curr2 : 

            if curr1 is None: 
                tail.next = ListNode((curr2.val + carry)%10)
                carry = (curr2.val+carry) // 10 
                curr2 = curr2.next
            else:
                if curr2 is None: 
                    tail.next = ListNode((curr1.val+carry)%10)
                    carry = (curr1.val+carry) // 10 
                    curr1 = curr1.next
                else:
                    s = carry + curr1.val + curr2.val
                    carry = s//10
                    tail.next = ListNode(s%10)
                    curr1 = curr1.next 
                    curr2 = curr2.next
            
            
            tail = tail.next 
        
        if carry != 0 : 
            tail.next = ListNode(carry)
        
        return dummy.next
    
        
        



        