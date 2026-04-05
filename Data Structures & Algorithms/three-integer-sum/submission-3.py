class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        nums = sorted(nums) # nlogn
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r] 
                if s == 0:
                    if [nums[i],nums[l],nums[r]] not in ret:
                        ret.append([nums[i],nums[l],nums[r]])
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1

        return ret

'''

seen = {}
for idx, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        return [seen[diff], idx]
    seen[num] = idx


l, r = 0, len(nums) - 1
while l < r:
    if condition:
        l += 1
    else:
        r -= 1

'''