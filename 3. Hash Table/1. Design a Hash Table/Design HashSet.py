class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = [-1] * 1000001

    def add(self, key: int) -> None:
        if self.val[key] == -1:
            self.val[key] = 1

    def remove(self, key: int) -> None:
        self.val[key] = -1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.val[key] == 1:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
