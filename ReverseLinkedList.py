# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        curr = head
        while curr:
            currtemp = curr.next
            curr.next = pre
            pre = curr
            curr = currtemp
        return pre