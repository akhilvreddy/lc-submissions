class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = Node()

    
    def get(self, index: int) -> int:
        curr = self.head
        while curr and index >= 0:
            curr = curr.next
            index -= 1
        return curr.val if curr else -1


        

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        if self.tail == self.head:
            self.tail = self.head.next
        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head
        while curr.next and index > 0:
            curr = curr.next
            index -= 1
        
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
        
