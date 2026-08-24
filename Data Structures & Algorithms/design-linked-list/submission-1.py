class ListNode:
    def __init__(self, val = -1, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.find(index).val

    def find(self, index: int) -> ListNode:
        if index >= self.size:
            return None
        curr = self.head
        while curr and index >= 0:
            curr = curr.next
            index -= 1
        return curr if curr else None

        


        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            nodeBefore = self.find(index-1)
            nodeAfter = nodeBefore.next
            node = ListNode(val, nodeBefore, nodeAfter)
            nodeBefore.next, nodeAfter.prev = node, node
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        node = self.find(index)
        if node:
            nodeBefore, nodeAfter = node.prev, node.next
            nodeBefore.next = nodeAfter
            nodeAfter.prev = nodeBefore
            self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)