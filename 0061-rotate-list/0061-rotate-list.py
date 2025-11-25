# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findNthNode(self,temp,k):
        cnt = 1
        while temp != None:
            if cnt == k:
                 return temp
            cnt += 1
            temp = temp.next
        return temp
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        tail =head
        len=1
        while tail.next != None:
            tail=tail.next
            len+=1
        if k % len == 0:
             return head
        k=k%len
        tail.next=head
        newLastNode=self.findNthNode(head,len - k)
        head=newLastNode.next
        newLastNode.next=None
        return head
        