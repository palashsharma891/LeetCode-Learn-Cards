# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        runner = walker = head

        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                seeker = head
                while seeker != walker:
                    walker = walker.next
                    seeker = seeker.next
                return walker
