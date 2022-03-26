# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # initial values
        node = head.next
        prev_node = head
        my_sum = 0
        
        while node != None:
            
            if node.val == 0:
                
                # merge the nodes between two zeros with a value that equals the sum of all the merged nodes
                prev_node.next = node
                prev_node.next.val = my_sum
                
                # reset value
                prev_node = node
                my_sum = 0
            else:
                my_sum += node.val
                
            node = node.next
        return head.next
        
