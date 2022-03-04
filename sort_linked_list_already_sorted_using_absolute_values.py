class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortLinkedList(self, head):
        positive_head = ListNode(0)
        current_positive = positive_head
        negative = None
        last_negative = None
        parser = head 
        while parser:
            if parser.val >= 0:
                current_positive.next = ListNode(parser.val)
                current_positive = current_positive.next
            else:
                temp = ListNode(parser.val)
                temp.next = last_negative
                last_negative = temp
                if negative is None:
                    negative = temp
            parser = parser.next
        if negative is not None:
            negative.next = positive_head.next
        else:
            last_negative = positive_head.next
        return last_negative
        
        