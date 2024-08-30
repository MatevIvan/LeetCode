# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # create a temp list with a blank first node
        temp = ListNode()
        # set the current node to the temp list
        current = temp
        
        # while both nodes are not empty
        while list1 and list2:
            # if the value in list1 is less than or equal to the value in list2 
            if list1.val <= list2.val:
                # set the next node to the remainder of list1
                current.next = list1
                # cycle to the next item in list1
                list1 = list1.next
            # if list2 value was larger than the list1 value
            else:
                # set the next node to the remainder of list2
                current.next = list2
                # cycle to the next item in list2
                list2 = list2.next
            # cycle to the next item in the current list
            current = current.next
        # Note that for this while loop, we are cycling through both lists, but only one list at a time

        # if list1 still has values
        if list1:
            # set the remainder of list1 as the next node
            current.next = list1
        # if list2 still has values
        elif list2:
            # set the remainder of list2 as the next node
            current.next = list2
        
        # return temp.next because the first item was a filler node
        return temp.next