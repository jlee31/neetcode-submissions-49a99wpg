class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers) - 1
        r = 0
        while (r <= l):
            if numbers[r] + numbers[l] == target:
                return [r+1, l+1]
            elif numbers[r] + numbers[l] < target:
                r += 1
            elif numbers[r] + numbers[l] > target:
                l -= 1