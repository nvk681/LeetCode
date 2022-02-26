# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_pointer, fast_pointer = head, head
        dummy = ListNode(0)
        dummy.next = head
        slow_pointer, fast_pointer = dummy, dummy
        lenght = n
        for i in range(n+1):
            fast_pointer = fast_pointer.next
        while fast_pointer is not None:
            lenght += 1
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        slow_pointer.next = None if slow_pointer.next is None else slow_pointer.next.next
        return dummy.next