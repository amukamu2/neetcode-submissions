# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        num = set()
        slow = head
        fast = head
        while fast:
            slow = slow.next
            temp = fast.next
            if temp:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
        return False
