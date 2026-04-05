class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        clean = ""
        for letter in s:
            if letter.isalnum():
                clean += letter.lower()

        r = 0
        l = len(clean) - 1
        while r <= l:
            if clean[r] != clean[l]:
                return False
            r += 1
            l -= 1
        return True
        

