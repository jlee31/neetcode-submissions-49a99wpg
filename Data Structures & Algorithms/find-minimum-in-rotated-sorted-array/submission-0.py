class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        min = 10000000000000;
        for i in range(l):
            if nums[i] < min:
                min = nums[i]
        return min