class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        ret = 0
        l = 0

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            width = (r - l) + 1
            ret = max(width, ret)
            seen.add(s[r])

        return ret