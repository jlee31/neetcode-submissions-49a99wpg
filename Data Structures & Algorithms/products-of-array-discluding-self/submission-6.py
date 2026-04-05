class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force o(n)
        n = len(nums)
        ret = [0] * n
        for i in range(n):
            curr = 1
            for j in range(n):
                if i == j:
                    continue
                curr *= nums[j]
            ret[i] = curr

        return ret
         
