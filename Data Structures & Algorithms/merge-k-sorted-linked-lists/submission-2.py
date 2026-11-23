# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        dummy = ListNode()
        curr = dummy

        while heap:
            _, i, smallest = heapq.heappop(heap)
            curr.next = smallest
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, i, smallest.next))
            curr = curr.next
        return dummy.next
        

        