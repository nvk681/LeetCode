# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        return_value = None
        temp = None
        while l1 is not None or l2 is not None:
            a = 0 if l1 is None else l1.val
            b = 0 if l2 is None else l2.val
            sum_value = a+b+carry
            carry = int((sum_value)/10)
            new_item = ListNode(sum_value%10)
            if return_value is None:
                return_value = new_item
                temp = new_item
            else:
                temp.next = new_item
                temp = temp.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        if carry > 0:
            temp.next = ListNode(carry)
            
        return return_value
       