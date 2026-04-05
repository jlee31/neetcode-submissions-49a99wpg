class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using prefix product
        n = len(nums)
        total = 1
        forward = [0] * n
        forward[0] = 1
        backward = [0] * n
        backward[n-1] = 1
        ret = [0] * n
        for i in range(1,n):
            forward[i] = forward[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            backward[j] = backward[j+1] * nums[j+1]
        for i in range(n):
            ret[i] = forward[i] * backward[i]
        return ret