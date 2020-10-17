class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        
        if self.head is None:
            return -1
        
        current = self.head
        for i in range(index):
            current = current.next
            
        return current.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            self.head = Node(val)
        else:
            node = Node(val)
            curr = self.head
            for i in range(self.length-1):
                curr = curr.next

            curr.next = node
        self.length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.length:
            return
        
        if index == 0:
            self.addAtHead(val)
            
        #if index == self.length:
            #self.addAtTail(val)
        else:
            node = Node(val)
            curr = self.head
            for i in range(index-1):
                curr = curr.next

            node.next = curr.next
            curr.next = node
        
            self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index-1):
                curr = curr.next
            if curr.next:
                curr.next = curr.next.next
            else:
                curr.next = None

        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
