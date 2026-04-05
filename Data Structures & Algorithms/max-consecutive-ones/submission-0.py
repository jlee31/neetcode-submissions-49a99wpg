class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        l = len(nums)
        count = 0
        for i in range(l):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0:
                count = 0
            max_len = max(max_len, count)
        return max_len