class Solution:
    def isPalindrome(self, s: str) -> bool:

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ `'''
        no_punct = ""

        for char in s:
            if char not in punctuations:
                no_punct = no_punct + char
        print(no_punct)
        return no_punct.lower() == no_punct[::-1].lower()
