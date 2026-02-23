#https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head # current pointer

        # compare list1 and list2
        while list1 and list2:
            # if list1.val is greater than list2.val
            if list1.val > list2.val:
                cur.next = list2 # change cur pointer to list 2
                list2 = list2.next # change list2 to list2.next
            else:
                cur.next = list1 # change cur pointer to list 1
                list1 = list1.next # change list1 to list1.next
        
            cur = cur.next # change cur to cur.next

        # change cur pointer to the left node
        if list1: cur.next = list1
        else: cur.next = list2

        return head.next