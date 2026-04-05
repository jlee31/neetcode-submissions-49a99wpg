class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxSum = nums[0]
        l = len(nums)

        for i in range(1,l):
            maxSum = max(nums[i], maxSum+nums[i])
            res = max(maxSum, res)
        
        return res