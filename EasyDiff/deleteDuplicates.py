# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if the head is empty return none
        if not head:
            return None
        # set the head reference to temp
        temp = head
        # while the current node and the next node aren't empty
        while temp and temp.next:
            # if the current node value is equal to the value of the next node
            if temp.val == temp.next.val:
                # set the current node pointer to skip over the next node
                temp.next = temp.next.next
            else:
                # only change the temp node if the node values are different
                temp = temp.next
        # return the original head
        return head