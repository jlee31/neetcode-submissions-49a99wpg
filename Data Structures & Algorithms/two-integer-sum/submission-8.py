class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l = len(nums)
        # for i in range(l):
        #     for j in range(i + 1, l):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        seen = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], idx]
            seen[num] = idx