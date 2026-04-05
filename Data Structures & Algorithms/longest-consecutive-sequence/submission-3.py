class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        l = len(nums)
        longest = 0
        currlongest = 0
        for i in range(l):
            s.add(nums[i])

        for num in nums:
            if num-1 not in s:
                j = 0
                while num + j in s:
                    currlongest += 1
                    j += 1
                longest = max(longest, currlongest)
                currlongest = 0
        
        return longest
            