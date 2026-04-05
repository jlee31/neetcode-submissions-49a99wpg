class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        curr = []

        def backtrack():
            if len(curr) == l:
                res.append(curr[:]) # append a snapshot
                return
                
            for x in nums:
                if x not in curr:
                    curr.append(x)
                    backtrack()
                    curr.pop()
        
        backtrack()
        return res