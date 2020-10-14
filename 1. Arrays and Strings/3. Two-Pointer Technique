class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front, last = 0, len(s) - 1
        for i in range(len(s)//2):
            s[front], s[last] = s[last], s[front]
            front, last = front + 1, last - 1
