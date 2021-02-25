class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        while True:
            s = 0
            while num > 0:
                r = num % 10
                s += r*r
                num //= 10
                print(r, s, num)
            if s < 10:
                if s == 1 or s == 7:
                    return True
                else:
                    return False
            num = s
