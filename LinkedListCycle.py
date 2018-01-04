#! /usr/bin/env python

"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # ## hash table
        # hashmap = set([])
        # while(head):
        #     if head in hashmap:
        #         return True
        #     else:
        #         hashmap.add(head)
        #     head = head.next
        # return False

        # two point
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next

        while(slow!=fast):
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True