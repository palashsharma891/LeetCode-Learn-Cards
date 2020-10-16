class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        new_string = ''
        for i in range(len(str_list)-1, -1, -1):
            new_string += str_list[i] + ' '
            print(new_string, i)
            
        return new_string[:-1]
