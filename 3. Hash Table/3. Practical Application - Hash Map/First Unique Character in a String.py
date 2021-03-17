class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s_dict = {}
        
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
                
        for key in s_dict:
            if s_dict[key] == 1:
                return s.find(key)
            
        return -1
