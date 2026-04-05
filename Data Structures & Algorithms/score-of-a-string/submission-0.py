class Solution:
    def scoreOfString(self, s: str) -> int:
        l = len(s)
        score = 0
        for i in range(l - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score