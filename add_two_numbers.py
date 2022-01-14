# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if l1.val == 0:
        #     return l2
        # if l2.val == 0:
        #     return l1
        num1 = 0
        num2 = 0
        i = 1
        while l1 is not None: 
            num1 = num1+(l1.val*i)
            i = i*10 
            l1 = l1.next
        i = 1
        while l2 is not None: 
            num2 = num2+(l2.val*i)
            i = i*10 
            l2 = l2.next
        l1 = num1+num2
        if l1 != 0:
            temp = ListNode(l1%10)
            l1 = l1//10
            head = temp
            while l1 != 0:
                tem = l1%10
                l1 = l1//10
                a = ListNode(tem)
                # a.next = temp
                temp.next = a
                temp = a
        else: 
            return ListNode()
        return head
            