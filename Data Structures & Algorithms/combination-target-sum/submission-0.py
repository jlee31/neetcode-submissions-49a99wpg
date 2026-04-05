class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        curr = []
        n = len(nums)

        def backtrack(i, cur_sum):
            # base cases
            if cur_sum == target:
                ret.append(curr[:])
                return
            
            if cur_sum > target or i == n:
                return

            backtrack(i+1, cur_sum)

            # make choice
            curr.append(nums[i])
            # backtrack
            backtrack(i, cur_sum+nums[i])
            # undo choice / backtrack step
            curr.pop()
        
        backtrack(0,0)
        return ret