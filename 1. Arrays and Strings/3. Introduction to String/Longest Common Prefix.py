class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        try:
            shortest = min(strs, key=len)
        except:
            return ''
        max_substr = ''
        f = 0
        for i in range(len(shortest)):
            prefix = shortest[:i+1]
            for s in strs:
                if not prefix == s[:i+1]:
                    f = 1
            if f == 0 and len(prefix) > len(max_substr):
                max_substr = prefix
                
        return max_substr
