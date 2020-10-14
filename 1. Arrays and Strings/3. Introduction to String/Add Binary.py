class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #return format((int(a, 2) + int(b, 2)), 'b')
        
        #result = int(a, 2) + int(b, 2)
        #return format(result, 'b')
        
        result = int(a, 2) + int(b, 2)
        num = result
        ans = ''
        
        while num >= 2:
            if num % 2 == 0:
                ans += '0'
            else:
                ans += '1'
            num //= 2
            
        ans += str(num)
                
        return ans[::-1]
