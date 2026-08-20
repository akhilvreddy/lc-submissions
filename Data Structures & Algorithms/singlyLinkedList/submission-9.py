class ListNode:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next
    
class LinkedList:
    
    def __init__(self):
        self.head = self.tail = ListNode()

    
    def get(self, index: int) -> int:
        curr = self.head
        while curr and index >= 0:
            curr = curr.next
            index -= 1
        
        return curr.val if curr else -1
        

    def insertHead(self, val: int) -> None:
        self.head.next = ListNode(val, self.head.next)
        if self.tail == self.head:
            self.tail = self.tail.next
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr.next:
            curr.next = curr.next.next
            self.tail = curr if not curr.next else self.tail
            return True
        return False
        
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
        
