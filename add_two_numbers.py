# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        result, pointer, carry = None, None, 0
        while l1 is not None and l2 is not None:
            a = l1.val + l2.val + carry
            carry = a//10
            val = a%10
            temp = ListNode(val)
            if not result:
                pointer, result = temp, temp
            else:
                pointer.next = temp
                pointer = pointer.next
            l1, l2 = l1.next, l2.next
        if l1 is not None or l2 is not None:
            l = l1 if l1 else l2
            while l:
                a = l.val + carry
                carry = a//10
                val = a%10
                pointer.next = ListNode(val)
                pointer = pointer.next
                l = l.next
        if carry != 0:
            pointer.next = ListNode(carry)
            pointer = pointer.next
        return result
       