# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        curr1, curr2 = headA, headB
        while curr1 and curr2 and curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
            if curr1 == curr2:
                return curr1
            if not curr1:
                curr1 = headB
            if not curr2:
                curr2 = headA
                
        return curr1
