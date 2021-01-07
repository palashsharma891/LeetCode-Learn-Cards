class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        num = abs(x)
        while num > 0:
            r = num % 10
            rev = rev * 10 + r
            num = num // 10
        if rev < 2147483648 and x > -2147483648:
            if x > 0:
                return rev
            else:
                return -rev
        else:
            return 0
