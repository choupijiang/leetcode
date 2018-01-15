"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        p = head

        while p:
            tmpNode = RandomListNode(p.label)
            tmpNode.next = p.next
            p.next = tmpNode
            p = p.next.next

        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        newHead = head.next
        pold = head
        pnew = newHead

        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pold.next

        pold.next = None
        pnew.next = None

        return newHead
