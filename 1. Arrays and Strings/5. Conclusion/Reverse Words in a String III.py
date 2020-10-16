class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        new_str = ''
        for i in range(0, len(str_list)):
            new_str += str_list[i][::-1] + ' '
            
        return new_str[:-1]
