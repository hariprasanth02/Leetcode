# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newHead
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     temp=head
    #     prev=None
    #     while temp is not None:
    #         front = temp.next
    #         temp.next=prev
    #         prev=temp
    #         temp=front
    #     return prev
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     if head is None or head.next is None:
    #         return True
    #     slow=head
    #     fast=head
    #     while fast.next is not None and fast.next.next is not None:
    #         slow=slow.next
    #         fast=fast.next.next
    #     newHead = self.reverseList(slow.next)
    #     first=head
    #     second=newHead
    #     while second is not None:
    #         if first.val != second.val:
    #             self.reverseList(newHead)
    #             return False
    #     first=first.next
    #     second=second.next
    #     self.reverseList(newHead)
    #     return True
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

    # Find the middle of the list
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        newHead = self.reverseList(slow.next)

        # Compare both halves
        first = head
        second = newHead
        result = True
        while second is not None:
            if first.val != second.val:
                result = False
                break
            first = first.next
            second = second.next

        # Restore the list (optional)
        slow.next = self.reverseList(newHead)

        return result