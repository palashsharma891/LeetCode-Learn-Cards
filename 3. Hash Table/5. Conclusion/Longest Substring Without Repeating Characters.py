class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        maxi = 0
        s1 = ''
        
        while j < len(s):
            if s[j] not in s1:
                s1 += s[j]
                j += 1
                maxi = max(maxi, len(s1))
            else:
                s1 = s1[1:]
                
        return maxi
