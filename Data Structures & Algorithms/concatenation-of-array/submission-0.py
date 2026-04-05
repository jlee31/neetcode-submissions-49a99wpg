class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        out = [0] * (2 * l)
        for idx in range(l):
            out[idx] = nums[idx]
            out[idx + l] = nums[idx]
        return out