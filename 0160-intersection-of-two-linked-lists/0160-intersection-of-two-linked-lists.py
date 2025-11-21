# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if headA == None or headB == None:
        #     return None
        # t1=headA
        # t2=headB
        # while t1 != t2:
        #     t1=t1.next
        #     t2=t2.next
        #     if t1 == t2:
        #     return t1
        #     if t1 == None:
        #         t1=headA
        #     if t2 == None:
        #         t2=headB

        p1,p2 = headA,headB
        while p1 != p2:
           p1 = headB if p1 is None else p1.next
           p2 = headA if p2 is None else p2.next
        return p1